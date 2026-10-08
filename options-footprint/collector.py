"""
Options footprint collector.

Builds a labeled dataset of the options activity that came BEFORE big stock moves,
plus a control group of ordinary days, so we can measure whether a put/call
collapse actually predicts anything.

Data comes from Alpaca (free with your existing keys): daily stock bars, the list
of option contracts per ticker (including expired ones), and daily bars per
contract. Put/call ratio = total put volume / total call volume across the chain.

Standard library only, so it runs in Windows PowerShell with no installs:
    python collector.py nightly                 # everything below, for the last week
    python collector.py find-movers --start 2026-04-01 --min-move 15
    python collector.py collect --lookback 15
    python collector.py controls --per-event 2
    python collector.py features
    python collector.py compare --ticker WOLF   # Alpaca put/call vs Alpha Vantage values on file

Environment variables (PowerShell:  $env:NAME = "value"):
    ALPACA_KEY_ID, ALPACA_SECRET_KEY   (paper-trading keys work)

Every Alpaca response is cached in data/cache/, so reruns are fast and free.
Note: Alpaca options history starts February 2024, and it has no historical open
interest, so volume-versus-open-interest has to come from another source later.
"""
import argparse
import re
import csv
import datetime as dt
import hashlib
import json
import os
import random
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # find store.py next to this file
from store import Store  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
CACHE = os.path.join(DATA, "cache")
EVENTS = os.path.join(DATA, "events.csv")
DAILY = os.path.join(DATA, "daily_features.csv")
CONTROLS = os.path.join(DATA, "controls.csv")
FEATURES = os.path.join(DATA, "event_features.csv")

EVENT_FIELDS = ["ticker", "event_date", "event_type", "move_pct", "prior_close",
                "event_close", "catalyst", "label", "notes"]
DAILY_FIELDS = ["ticker", "date", "put_call_ratio", "put_call_alpaca", "call_volume",
                "put_volume", "short_otm_call_volume",
                "call_vol_short", "call_vol_medium", "call_vol_long",
                "call_vol_otm", "call_vol_atm", "call_vol_itm",
                "stock_close", "stock_volume", "source_put_call", "source_price"]

# Volatile, optionable small and mid caps. Edit freely (Alpaca takes 100 per call).
UNIVERSE = """WOLF PLUG SOUN RGTI QUBT IONQ ACHR JOBY LUNR RKLB ASTS OKLO SMR NNE BBAI
RXRX UPST AFRM SOFI HIMS CLSK MARA RIOT CIFR IREN APLD CORZ WULF OPEN LCID RIVN NIO
CHPT BLNK QS SLDP FCEL BE ENPH RUN""".split()

ALPACA_HISTORY_START = "2024-02-01"
STANDARD_OPTION_SYMBOL = re.compile(r"^[A-Z]{1,5}\d{6}[CP]\d{8}$")
ERRORS = os.path.join(DATA, "errors.csv")

# "core" = the hand-picked list above. "all" = every active US stock with listed options.
DEFAULT_UNIVERSE = "all"
BIG_MOVE_REVIEW = 200.0      # one-day moves above this are kept but labeled for a quick look:
                             # usually real (buyouts, drug approvals), occasionally a share reissue
MIN_PRICE = 5.0              # "all" mode: skip stocks under $5 (penny-stock pumps)
MIN_AVG_SHARE_VOLUME = 500_000   # "all" mode: skip thinly traded stocks
MAJOR_EXCHANGES = {"NYSE", "NASDAQ", "AMEX", "ARCA", "BATS"}
MAX_EXPIRY_DAYS = 1100     # whole chain, including long-dated contracts (matches Alpha Vantage)
SHORT_DATED_DAYS = 14      # "short-dated" = expires within two weeks
OTM_PCT = 0.05             # "out of the money" = strike at least 5% above the close
MEDIUM_DATED_DAYS = 60     # 15-60 days = medium dated; beyond that = long dated
CALL_BUCKETS = ("call_vol_short", "call_vol_medium", "call_vol_long",
                "call_vol_otm", "call_vol_atm", "call_vol_itm")


# ---------------------------------------------------------------- helpers
def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", restval="")
        w.writeheader()
        w.writerows(rows)


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def iso(d):
    return d.isoformat() if isinstance(d, dt.date) else d


def is_monthly(date_str):
    """Standard monthly options expire on the third Friday (Thursday if Friday is a holiday)."""
    d = dt.date.fromisoformat(date_str)
    return (d.weekday() == 4 and 15 <= d.day <= 21) or (d.weekday() == 3 and 14 <= d.day <= 20)


def chunk_key(symbols):
    """Short fingerprint of a contract list, so a changed list never reuses an old cache file."""
    import hashlib
    return hashlib.sha1(",".join(symbols).encode()).hexdigest()[:12]


def add_days(d, n):
    return (dt.date.fromisoformat(d) + dt.timedelta(days=n)).isoformat()


def safe_end(end_date):
    """Alpaca's free tier refuses the most recent 15 minutes; stop the range 20 minutes ago."""
    now = dt.datetime.now(dt.timezone.utc)
    end_of_day = dt.datetime.fromisoformat(end_date).replace(tzinfo=dt.timezone.utc) + dt.timedelta(days=1)
    cutoff = now - dt.timedelta(minutes=20)
    return end_date if end_of_day <= cutoff else cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- Alpaca
_last_request = [0.0]
MIN_SECONDS_BETWEEN_REQUESTS = 0.4    # about 150 a minute, leaving room under Alpaca's free
                                      # limit of 200 for the ladder backtest (30 a minute)


def http_json(url, headers=None):
    for attempt in range(8):
        try:
            wait = _last_request[0] + MIN_SECONDS_BETWEEN_REQUESTS - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            _last_request[0] = time.monotonic()
            req = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:              # rate limited (e.g. two jobs sharing the key): back off
                time.sleep(min(60, 2 ** attempt))
                continue
            body = e.read().decode("utf-8", "replace")[:500]
            safe_url = url.split("?")[0]
            message = f"Alpaca refused {safe_url} with HTTP {e.code}: {body}"
            if e.code in (401, 403):   # keys or plan problem: every call will fail, so stop
                sys.exit(message)
            raise RuntimeError(message)  # one bad request: the caller logs it and moves on
    raise RuntimeError("Alpaca kept rate-limiting; try again in a minute.")


def alpaca_get(base, path, params, cache_name=None):
    if cache_name:
        os.makedirs(CACHE, exist_ok=True)
        cpath = os.path.join(CACHE, cache_name)
        if os.path.exists(cpath):
            with open(cpath, encoding="utf-8") as f:
                return json.load(f)
    kid, sec = os.environ.get("ALPACA_KEY_ID"), os.environ.get("ALPACA_SECRET_KEY")
    if not (kid and sec):
        sys.exit("Set ALPACA_KEY_ID and ALPACA_SECRET_KEY first.")
    headers = {"APCA-API-KEY-ID": kid, "APCA-API-SECRET-KEY": sec}
    pages, token = [], None
    while True:
        p = dict(params)
        if token:
            p["page_token"] = token
        data = http_json(f"{base}{path}?{urllib.parse.urlencode(p)}", headers)
        pages.append(data)
        token = data.get("next_page_token") if isinstance(data, dict) else None
        if not token:
            break
    if cache_name:
        with open(cpath, "w", encoding="utf-8") as f:
            json.dump(pages, f)
    return pages


def stock_bars(symbols, start, end, adjustment="raw"):
    pages = []
    for i in range(0, len(symbols), 100):
        pages += alpaca_get("https://data.alpaca.markets", "/v2/stocks/bars",
                            {"symbols": ",".join(symbols[i:i + 100]), "timeframe": "1Day",
                             "start": start, "end": safe_end(end), "limit": 10000,
                             "adjustment": adjustment, "feed": "sip"})
    out = {}
    for page in pages:
        for sym, bars in (page.get("bars") or {}).items():
            out.setdefault(sym, []).extend(
                {"date": b["t"][:10], "close": b["c"], "volume": b["v"]} for b in bars)
    return out


def option_contracts(ticker, exp_from, exp_to):
    """All call and put contracts (active and expired) expiring in the range."""
    contracts = []
    for status in ("active", "inactive"):
        pages = alpaca_get("https://paper-api.alpaca.markets", "/v2/options/contracts",
                           {"underlying_symbols": ticker, "status": status,
                            "expiration_date_gte": exp_from, "expiration_date_lte": exp_to,
                            "limit": 10000},
                           cache_name=f"contracts_{ticker}_{exp_from}_{exp_to}_{status}.json")
        for page in pages:
            contracts.extend(page.get("option_contracts") or [])
    return {c["symbol"]: c for c in contracts}


def new_totals(dates):
    return {d: {k: 0 for k in ("call", "put", "short_otm_call") + CALL_BUCKETS} for d in dates}


def add_bars(pages, contracts, closes, totals):
    """Add one Alpaca options-bars response into the per-day totals."""
    for page in pages:
        for sym, bars in (page.get("bars") or {}).items():
            c = contracts.get(sym)
            if c is None:          # not one we asked for; ignore
                continue
            kind = c["type"]       # "call" or "put"
            expiry = dt.date.fromisoformat(c["expiration_date"])
            strike = float(c["strike_price"])
            for b in bars:
                d = b["t"][:10]
                t = totals.get(d)
                if t is None:
                    continue
                v = b["v"]
                t[kind] += v
                if kind != "call":
                    continue
                days_left = (expiry - dt.date.fromisoformat(d)).days
                # Where did the call buying land? By time to expiration...
                if days_left <= SHORT_DATED_DAYS:
                    t["call_vol_short"] += v
                elif days_left <= MEDIUM_DATED_DAYS:
                    t["call_vol_medium"] += v
                else:
                    t["call_vol_long"] += v
                # ...and by strike versus the stock price.
                close = closes.get(d)
                if close:
                    if strike >= close * (1 + OTM_PCT):
                        t["call_vol_otm"] += v
                        if days_left <= SHORT_DATED_DAYS:
                            t["short_otm_call"] += v
                    elif strike <= close * (1 - OTM_PCT):
                        t["call_vol_itm"] += v
                    else:
                        t["call_vol_atm"] += v


def finish_totals(totals):
    out = {}
    for d, t in totals.items():
        out[d] = {"call_volume": t["call"], "put_volume": t["put"],
                  "short_otm_call_volume": t["short_otm_call"],
                  "put_call_alpaca": round(t["put"] / t["call"], 3) if t["call"] else ""}
        out[d].update({k: t[k] for k in CALL_BUCKETS})
    return out


def standard_symbols(contracts):
    # Contracts adjusted after a split or merger get non-standard symbols (e.g. "1CHPT...") that
    # the bars endpoint rejects, and their strikes no longer match the stock price anyway.
    return sorted(s for s in contracts if STANDARD_OPTION_SYMBOL.match(s))


def option_daily_volume(ticker, dates, closes):
    """Per day: call and put volume, put/call, and where the call volume landed. One window."""
    if not dates:
        return {}
    start, end = min(dates), max(dates)
    contracts = option_contracts(ticker, start, add_days(end, MAX_EXPIRY_DAYS))
    # Weekly expirations are only listed a few weeks ahead, so far-out weeklies didn't trade yet
    # during the window. Keep everything near-term, and only monthly (third Friday) expirations
    # beyond that, which covers the long-dated contracts without wasting calls.
    near = add_days(end, MEDIUM_DATED_DAYS)
    contracts = {s: c for s, c in contracts.items()
                 if c["expiration_date"] <= near or is_monthly(c["expiration_date"])}
    symbols = standard_symbols(contracts)
    totals = new_totals(dates)
    for i in range(0, len(symbols), 100):
        chunk = symbols[i:i + 100]
        pages = alpaca_get("https://data.alpaca.markets", "/v1beta1/options/bars",
                           {"symbols": ",".join(chunk), "timeframe": "1Day",
                            "start": start, "end": safe_end(end), "limit": 10000},
                           cache_name=f"optbars_{ticker}_{start}_{end}_{chunk_key(chunk)}.json")
        add_bars(pages, contracts, closes, totals)
    return finish_totals(totals)


def option_full_history(ticker, dates, closes, deadline):
    """Every trading day since Alpaca's options history begins, in one pass over every contract.
    Each contract is fetched once over its whole life, so this costs (contracts / 100) requests
    no matter how many events the ticker has. Returns None if the time budget runs out."""
    today = dt.date.today().isoformat()
    contracts = option_contracts(ticker, ALPACA_HISTORY_START, add_days(today, MAX_EXPIRY_DAYS))
    symbols = standard_symbols(contracts)
    totals = new_totals(dates)
    for i in range(0, len(symbols), 100):
        if time.monotonic() > deadline:
            return None
        chunk = symbols[i:i + 100]
        pages = alpaca_get("https://data.alpaca.markets", "/v1beta1/options/bars",
                           {"symbols": ",".join(chunk), "timeframe": "1Day",
                            "start": ALPACA_HISTORY_START, "end": safe_end(today), "limit": 10000})
        add_bars(pages, contracts, closes, totals)
    print(f"  {ticker}: {len(symbols)} contracts, {len(dates)} trading days")
    return finish_totals(totals)


# ---------------------------------------------------------------- dataset plumbing
_STORE = None


def db():
    """The database (Neon, when DATABASE_URL is set) or the CSV files otherwise."""
    global _STORE
    if _STORE is None:
        _STORE = Store()
        print(f"Storage: {_STORE.kind}")
    return _STORE


def save(ticker, daily):
    """Write only the rows that changed, so nightly runs stay light on the database."""
    changed = [r for r in daily if r.pop("_dirty", False)]
    if changed:
        db().save_daily(ticker, changed)
    return len(changed)


def merge_stock_bars(daily, bars):
    index = {(r["ticker"], r["date"]): r for r in daily}
    for sym, rows in bars.items():
        for b in rows:
            r = index.get((sym, b["date"]))
            if r is None:
                r = {"ticker": sym, "date": b["date"]}
                daily.append(r)
                index[(sym, b["date"])] = r
            if not r.get("stock_close"):
                r["stock_close"], r["stock_volume"], r["source_price"] = b["close"], b["volume"], "alpaca"
                r["_dirty"] = True


def window_end(event):
    """Last trading session that counts as 'before' the move."""
    if event["event_type"] == "after_hours":
        return event["event_date"], True           # the event day's own session counts
    return event["event_date"], False


def days_before(ticker, event, n, daily):
    end, inclusive = window_end(event)
    days = sorted(r["date"] for r in daily if r["ticker"] == ticker
                  and (r["date"] < end or (inclusive and r["date"] == end)))
    if event.get("event_type") == "two_day":       # drop the first up day
        days = days[:-1]
    return days[-n:]


def ensure_prices(ticker, start, end, daily):
    have = [r for r in daily if r["ticker"] == ticker and start <= r["date"] <= end and r.get("stock_close")]
    if len(have) < 5:
        merge_stock_bars(daily, stock_bars([ticker], start, end))


def fill_window(ticker, dates, daily, refresh=False):
    index = {(r["ticker"], r["date"]): r for r in daily}
    def missing(d):
        r = index.get((ticker, d), {})
        return not r.get("put_call_alpaca") or r.get("call_vol_short", "") == ""
    todo = [d for d in dates if refresh or missing(d)]
    if not todo:
        return
    closes = {d: to_float(index[(ticker, d)]["stock_close"]) for d in dates if (ticker, d) in index}
    vols = option_daily_volume(ticker, todo, closes)
    for d, v in vols.items():
        index[(ticker, d)].update(v)
        index[(ticker, d)]["_dirty"] = True


def log_error(event, ex):
    db().log_error({"logged_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "ticker": event["ticker"], "event_date": event["event_date"],
                    "error": str(ex)[:300]})


# ---------------------------------------------------------------- commands
# Whole-word patterns that mark a fund rather than an operating company. Deliberately narrow:
# real companies are often listed as "Ordinary Shares" or "Depositary Shares", so "shares" alone
# is not used, and words like "ultra" must be whole words (so Ultragenyx stays in).
FUND_PATTERN = re.compile(
    r"\b(etf|etn|exchange traded|index fund|daily target|leveraged|inverse|"
    r"[-+]?[1-5](?:\.\d+)?x|ultra(?:pro|short)?|bull \dx|bear \dx|"
    r"proshares|direxion|ishares|spdr|invesco|vanguard|wisdomtree|graniteshares|"
    r"t-rex|tradr|defiance|yieldmax|roundhill|volatility shares)\b", re.IGNORECASE)


def looks_like_fund(name):
    """ETFs and other funds: big moves in a leveraged index fund aren't anyone's inside knowledge."""
    return bool(FUND_PATTERN.search(name or ""))


def universe_symbols(mode):
    if mode == "core":
        return UNIVERSE
    today = dt.date.today().isoformat()
    pages = alpaca_get("https://paper-api.alpaca.markets", "/v2/assets",
                       {"status": "active", "asset_class": "us_equity"},
                       cache_name=f"assets_{today}.json")
    assets = [a for page in pages for a in (page if isinstance(page, list) else [])]
    def ok(a):
        sym = a.get("symbol", "")
        return (a.get("tradable") and a.get("exchange") in MAJOR_EXCHANGES
                and a.get("exchange") != "ARCA"          # NYSE Arca lists mostly ETFs
                and not looks_like_fund(a.get("name", ""))
                and sym.isalpha() and len(sym) <= 5)
    with_options = [a["symbol"] for a in assets if ok(a) and "options_enabled" in (a.get("attributes") or [])]
    if not with_options:
        print("Warning: Alpaca did not flag any assets as options-enabled; scanning all major-exchange stocks.")
        with_options = [a["symbol"] for a in assets if ok(a)]
    return sorted(set(with_options))


def find_movers(args):
    """Scan the universe for one-day closes up at least --min-move percent."""
    end = args.end or dt.date.today().isoformat()
    mode = getattr(args, "universe", None) or DEFAULT_UNIVERSE
    symbols = universe_symbols(mode)
    # Extra history so the "all" mode filters have 20 days of volume to average.
    # Split-adjusted prices for spotting moves, so a reverse split doesn't look like a 3,000% rally.
    bars = stock_bars(symbols, add_days(args.start, -35), end, adjustment="split")
    events = db().events()
    have = {(e["ticker"], e["event_date"]) for e in events}
    # Also skip the second day of an already-logged two-day move.
    have |= {(e["ticker"], add_days(e["event_date"], -1)) for e in events if e["event_type"] == "two_day"}
    # An after-hours event shows up as a gap the next session; don't log it twice.
    have |= {(e["ticker"], add_days(e["event_date"], n)) for e in events
             if e["event_type"] == "after_hours" for n in (1, 2, 3)}
    by_date, found = {}, []
    for sym, rows in bars.items():
        for i in range(1, len(rows)):
            prev, cur = rows[i - 1], rows[i]
            if cur["date"] < args.start:
                continue
            move = (cur["close"] / prev["close"] - 1) * 100
            if move < args.min_move:
                continue
            if mode != "core":
                recent = [r["volume"] for r in rows[max(0, i - 21):i - 1]]
                if (prev["close"] < MIN_PRICE or len(recent) < 15
                        or statistics.mean(recent) < MIN_AVG_SHARE_VOLUME):
                    continue
            found.append((sym, cur["date"], move, prev["close"], cur["close"]))
            by_date.setdefault(cur["date"], []).append(sym)
    # With thousands of tickers, several 15% movers happen every day, so "many movers at once"
    # scales with the universe: at least 3 names, or 0.5% of everything scanned.
    crowd = max(3, int(0.005 * len(bars)))
    added, new_events = 0, []
    for sym, date, move, pc, c in found:
        if (sym, date) in have:
            continue
        n = len(by_date[date])
        new_events.append({"ticker": sym, "event_date": date, "event_type": "close_to_close",
                       "move_pct": f"{move:.1f}", "prior_close": pc, "event_close": c,
                       "catalyst": "Unconfirmed",
                       "label": ("check_corporate_action" if move > BIG_MOVE_REVIEW
                                 else "sector_day" if n >= crowd else "unknown"),
                       "notes": f"{n} of {len(bars)} scanned names up {args.min_move:g}%+ that day"})
        added += 1
    db().save_events(new_events)
    # Store raw prices (they match option strikes) only for tickers that just got new events;
    # everything else already has its prices.
    keep = sorted({e["ticker"] for e in new_events} & set(bars))
    if keep:
        raw = stock_bars(keep, add_days(args.start, -35), end)
        for t in keep:
            daily = db().daily(t)
            merge_stock_bars(daily, {t: raw.get(t, [])})
            save(t, daily)
    flagged = sum(1 for f in found if f[2] > BIG_MOVE_REVIEW)
    print(f"Scanned {len(bars)} tickers: {len(found)} moves of {args.min_move:g}%+, {added} new events added"
          f" ({flagged} over {BIG_MOVE_REVIEW:g}% kept but flagged for review).")


def collect(args, rows=None, label="events"):
    """Fill pre-move windows, one stock at a time. Events already filled are skipped without
    touching the database. Stops cleanly at --max-minutes; rerun to continue."""
    st = db()
    is_controls = rows is not None and label == "control"
    rows = rows if rows is not None else st.events()
    todo = [e for e in rows if e.get("window_filled") != "yes" and e["event_date"] >= ALPACA_HISTORY_START]
    print(f"{label}: {len(rows) - len(todo)} already filled, {len(todo)} to fill.")
    deadline = time.monotonic() + 60 * getattr(args, "max_minutes", 50)
    by_ticker = {}
    for e in todo:
        by_ticker.setdefault(e["ticker"], []).append(e)
    done = 0
    for t, evs in by_ticker.items():
        if time.monotonic() > deadline:
            print(f"Time budget reached after {done} {label}; saved. Run it again to continue.")
            return False
        daily = st.daily(t)
        filled = []
        for e in evs:
            try:
                ensure_prices(t, add_days(e["event_date"], -60), e["event_date"], daily)
                window = days_before(t, e, args.lookback, daily)
                fill_window(t, window, daily)
            except Exception as ex:   # log it, keep going; rerunning retries failed ones
                log_error(e, ex)
                print(f"{label}: {t} {e['event_date']} FAILED: {str(ex)[:150]}")
                continue
            e["window_filled"] = "yes"
            filled.append(e)
            done += 1
        save(t, daily)
        (st.save_controls if is_controls else st.save_events)(filled)
        print(f"{label}: {t} {len(filled)}/{len(evs)} filled ({done}/{len(todo)} overall)")
    return True


def controls(args):
    """Random quiet dates for the same tickers, so we can measure false positives. Only loads
    a stock's history when it actually needs more control days."""
    st = db()
    events, rows = st.events(), st.controls()
    rng = random.Random(42)
    have = {(r["ticker"], r["event_date"]) for r in rows}
    event_days, control_count = {}, {}
    for e in events:
        event_days.setdefault(e["ticker"], []).append(e["event_date"])
    for r in rows:
        control_count[r["ticker"]] = control_count.get(r["ticker"], 0) + 1
    new_rows = []
    for tk, edays in sorted(event_days.items()):
        need = args.per_event * len(edays) - control_count.get(tk, 0)
        if need <= 0:
            continue
        daily = st.daily(tk)
        days = [r["date"] for r in daily if r.get("stock_close")]
        closes = {r["date"]: to_float(r["stock_close"]) for r in daily}
        ok = []
        for i in range(args.lookback + 1, len(days)):
            d, p = days[i], days[i - 1]
            if d < ALPACA_HISTORY_START:
                continue
            if any(abs((dt.date.fromisoformat(d) - dt.date.fromisoformat(x)).days) < 15 for x in edays):
                continue
            if closes.get(d) and closes.get(p) and abs(closes[d] / closes[p] - 1) < 0.05:
                ok.append(d)
        for d in rng.sample(ok, min(need, len(ok))):
            if (tk, d) not in have:
                new_rows.append({"ticker": tk, "event_date": d, "event_type": "control", "label": "control"})
                have.add((tk, d))
    st.save_controls(new_rows)
    rows = st.controls()
    finished = collect(args, rows, label="control")
    print(f"{len(rows)} control dates on file ({len(new_rows)} new).")
    return finished


def compute(row, daily, lookback, signal_window=3):
    """Features for the days before one event (or control date)."""
    tk = row["ticker"]
    days = set(days_before(tk, row, lookback, daily))
    hist = sorted((r for r in daily if r["ticker"] == tk and r["date"] in days), key=lambda r: r["date"])

    def pcr_of(r):  # prefer our own Alpaca number, fall back to Alpha Vantage
        v = to_float(r.get("put_call_alpaca"))
        return v if v is not None else to_float(r.get("put_call_ratio"))

    pcr = [(r["date"], pcr_of(r)) for r in hist if pcr_of(r) is not None]
    vol = [to_float(r["stock_volume"]) for r in hist if to_float(r.get("stock_volume"))]
    close = [to_float(r["stock_close"]) for r in hist if to_float(r.get("stock_close"))]
    calls = [to_float(r.get("call_volume")) for r in hist if to_float(r.get("call_volume")) is not None]
    otm = [to_float(r.get("short_otm_call_volume")) for r in hist if to_float(r.get("short_otm_call_volume")) is not None]
    f = {"ticker": tk, "event_date": row["event_date"], "label": row.get("label", ""),
         "move_pct": row.get("move_pct", ""), "days_with_put_call": len(pcr)}
    if len(pcr) >= signal_window + 2:
        recent = [v for _, v in pcr[-signal_window:]]
        base = [v for _, v in pcr[:-signal_window]]
        base_med = statistics.median(base)
        f["baseline_put_call_median"] = round(base_med, 3)
        f["recent_put_call_min"] = round(min(recent), 3)
        f["put_call_drop_ratio"] = round(base_med / max(min(recent), 0.01), 1)
        # Lowest point anywhere in the window, and how many sessions before the move it was.
        low_date, low = min(pcr, key=lambda x: x[1])
        f["window_put_call_min"] = round(low, 3)
        f["sessions_from_low_to_event"] = sum(1 for d, _ in pcr if d > low_date) + 1
    if len(calls) >= signal_window + 2 and statistics.median(calls[:-signal_window]) > 0:
        f["call_volume_recent_vs_baseline"] = round(
            max(calls[-signal_window:]) / statistics.median(calls[:-signal_window]), 2)
    if len(otm) >= signal_window + 2:
        base = statistics.median(otm[:-signal_window])
        f["short_otm_call_recent_max"] = int(max(otm[-signal_window:]))
        if base > 0:  # blank when the baseline was zero; the raw max above still shows the spike
            f["short_otm_call_recent_vs_baseline"] = round(max(otm[-signal_window:]) / base, 2)
    for col in CALL_BUCKETS:
        series = [to_float(r.get(col)) for r in hist if to_float(r.get(col)) is not None]
        if len(series) >= signal_window + 2:
            base = statistics.median(series[:-signal_window])
            if base > 0:
                f[f"{col}_spike"] = round(max(series[-signal_window:]) / base, 2)
    if len(vol) >= 4:
        f["stock_volume_last_vs_avg"] = round(vol[-1] / statistics.mean(vol[:-1]), 2)
    if len(close) >= 2:
        f["price_change_in_window_pct"] = round((close[-1] / close[0] - 1) * 100, 1)
        f["max_daily_abs_move_pct"] = round(max(abs(b / a - 1) for a, b in zip(close, close[1:])) * 100, 1)
    return f


FEATURE_FIELDS = ["ticker", "event_date", "label", "move_pct", "days_with_put_call",
                  "baseline_put_call_median", "recent_put_call_min", "put_call_drop_ratio",
                  "window_put_call_min", "sessions_from_low_to_event",
                  "call_volume_recent_vs_baseline", "short_otm_call_recent_max",
                  "short_otm_call_recent_vs_baseline",
                  ] + [f"{c}_spike" for c in CALL_BUCKETS] + [
                  "stock_volume_last_vs_avg", "price_change_in_window_pct", "max_daily_abs_move_pct"]


def features(args):
    """Event and control features. By default only rows not scored yet; --all recomputes everything."""
    st = db()
    rows = st.events() + st.controls()
    done = set() if getattr(args, "all", False) else {(f["ticker"], f["event_date"]) for f in st.features()}
    todo = [r for r in rows if (r["ticker"], r["event_date"]) not in done]
    by_ticker = {}
    for r in todo:
        by_ticker.setdefault(r["ticker"], []).append(r)
    out = []
    for t, rs in by_ticker.items():
        daily = st.daily(t)
        out += [compute(r, daily, args.lookback) for r in rs]
    st.save_features(out)
    print(f"Features: {len(out)} computed, {len(done)} already on file.")


def compare(args):
    """Check Alpaca-computed put/call against the Alpha Vantage values already on file."""
    daily = db().daily(args.ticker)
    rows = [r for r in daily if r.get("put_call_ratio")]
    if not rows:
        sys.exit(f"No Alpha Vantage values on file for {args.ticker}.")
    ensure_prices(args.ticker, add_days(rows[0]["date"], -5), rows[-1]["date"], daily)
    fill_window(args.ticker, [r["date"] for r in rows], daily, refresh=True)
    save(args.ticker, daily)
    print(f"{'date':<12}{'alpha vantage':>14}{'alpaca':>10}{'calls':>10}{'puts':>10}")
    diffs = []
    for r in rows:
        av, al = to_float(r["put_call_ratio"]), to_float(r.get("put_call_alpaca"))
        print(f"{r['date']:<12}{av:>14.2f}{(al if al is not None else float('nan')):>10.2f}"
              f"{r.get('call_volume', ''):>10}{r.get('put_volume', ''):>10}")
        if al is not None:
            diffs.append(abs(al - av))
    if diffs:
        print(f"\nAverage absolute difference: {statistics.mean(diffs):.3f} over {len(diffs)} days")
        print("Under ~0.05 means Alpaca is good enough to replace Alpha Vantage.")


HISTORY_MIN_EVENTS = 3        # tickers with this many events get their full daily history
STATUS_FILE = os.path.join(ROOT, "backfill_status.txt")


def mover_tickers():
    """Stocks with several big moves: the original, hindsight-chosen list."""
    counts = {}
    for e in db().events():
        counts[e["ticker"]] = counts.get(e["ticker"], 0) + 1
    return sorted(t for t, n in counts.items() if n >= HISTORY_MIN_EVENTS)


def wide_tickers():
    return sorted(r["ticker"] for r in db().backend.read("wide_universe"))


def history_tickers():
    return sorted(set(mover_tickers()) | set(wide_tickers()))


WIDE_N = 300                                         # how many stocks the wide list samples
WIDE_MIN_OK = 200                                    # fewer than this means the selection went wrong
WIDE_SELECT_START, WIDE_SELECT_END = "2024-01-02", "2024-01-31"   # known before the history begins


def run_log(step, message):
    print(f"[{step}] {message}")
    try:
        db().backend.upsert("run_log", [{"logged_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                         "step": step, "message": message[:1000]}])
    except Exception as ex:   # noqa: BLE001 - logging must never break a job
        print(f"(could not save the log line: {ex})")


def had_options(sym):
    """True if any call or put on this stock expired between February and June 2024 (so its options
    were trading when the history starts). One small request per status; no paging."""
    kid, sec = os.environ.get("ALPACA_KEY_ID"), os.environ.get("ALPACA_SECRET_KEY")
    headers = {"APCA-API-KEY-ID": kid, "APCA-API-SECRET-KEY": sec}
    for status in ("inactive", "active"):
        q = urllib.parse.urlencode({"underlying_symbols": sym, "status": status, "limit": 1,
                                    "expiration_date_gte": "2024-02-01", "expiration_date_lte": "2024-06-30"})
        try:
            data = http_json(f"https://paper-api.alpaca.markets/v2/options/contracts?{q}", headers)
        except RuntimeError:
            continue
        if (data or {}).get("option_contracts"):
            return True
    return False


def select_wide(args):
    """Pick the wide list once: a random sample of liquid stocks with options, using ONLY January 2024
    data (price and share volume), so whether a stock later moved plays no part in choosing it.
    Delisted stocks are included too, so later failures aren't quietly left out."""
    if wide_tickers() and not getattr(args, "reselect", False):
        print(f"Wide list already chosen ({len(wide_tickers())} stocks).")
        return
    today = dt.date.today().isoformat()
    status_of, seen = {}, {"active": 0, "inactive": 0, "active_with_options": 0}
    for status in ("active", "inactive"):
        pages = alpaca_get("https://paper-api.alpaca.markets", "/v2/assets",
                           {"status": status, "asset_class": "us_equity"},
                           cache_name=f"assets_{status}_{today}.json")
        for a in (a for page in pages for a in (page if isinstance(page, list) else [])):
            seen[status] += 1
            seen["active_with_options"] += status == "active" and "options_enabled" in (a.get("attributes") or [])
            sym = a.get("symbol", "")
            if (a.get("exchange") in MAJOR_EXCHANGES and a.get("exchange") != "ARCA"
                    and not looks_like_fund(a.get("name", "")) and sym.isalpha() and len(sym) <= 5):
                # Alpaca no longer tags which stocks have options, so that is checked per stock below.
                status_of.setdefault(sym, status)
    symbols = sorted(status_of)
    print(f"Wide list: {len(symbols):,} candidate stocks (active with options, plus delisted).")
    bars = stock_bars(symbols, WIDE_SELECT_START, WIDE_SELECT_END)
    eligible, with_bars = [], 0
    for sym in symbols:
        b = bars.get(sym) or []
        if len(b) < 15:
            continue
        with_bars += 1
        price = sum(x["close"] for x in b) / len(b)
        volume = sum(x["volume"] for x in b) / len(b)
        if price >= MIN_PRICE and volume >= MIN_AVG_SHARE_VOLUME:
            eligible.append((sym, price, volume))
    rank = lambda s: hashlib.sha1(f"wide-v1|{s}".encode()).hexdigest()
    # In a fixed random order, keep stocks that had option contracts trading in early 2024.
    chosen, checked = [], 0
    for e in sorted(eligible, key=lambda e: rank(e[0])):
        if len(chosen) >= args.n:
            break
        checked += 1
        if had_options(e[0]):
            chosen.append(e)
    db().backend.upsert("wide_universe", [{"ticker": s, "status": status_of[s], "avg_price": round(p, 2),
                                            "avg_volume": round(v), "selected": today} for s, p, v in chosen])
    overlap = len({s for s, _, _ in chosen} & set(mover_tickers()))
    run_log("wide-select", f"assets listed: {seen['active']:,} active ({seen['active_with_options']:,} with options), "
            f"{seen['inactive']:,} delisted; after exchange/fund filters: {len(symbols):,} "
            f"({sum(1 for v in status_of.values() if v == 'active'):,} active); with 15+ January 2024 bars: "
            f"{with_bars:,}; met price and volume bar: {len(eligible):,}; checked for options: {checked}; "
            f"chosen: {len(chosen)} ({sum(1 for s_, _, _ in chosen if status_of[s_] == 'active')} still listed); "
            f"already big movers: {overlap}.")
    print(f"Wide list: {len(eligible):,} stocks met the January 2024 bar (price ${MIN_PRICE:.0f}+, "
          f"{MIN_AVG_SHARE_VOLUME:,}+ shares a day); sampled {len(chosen)} at random, {overlap} of them already "
          f"in the big-movers list.")


def select_only(args):
    """Choose (or with --reselect, re-choose) the wide list without pulling any history."""
    if getattr(args, "reselect", False):
        old = wide_tickers()
        if old and db().kind == "postgres":
            db().backend.conn.execute("delete from wide_universe")
        run_log("wide-select", f"re-choosing the wide list (it had {len(old)} stocks).")
    select_wide(argparse.Namespace(n=args.n, reselect=False))


def wide(args):
    """Choose the wide list (once) and pull each stock's full daily options history. Resumable;
    writes 'done' or 'more' to backfill_status.txt for the workflow."""
    select_wide(args)
    n = len(wide_tickers())
    if n < WIDE_MIN_OK:
        # Something went wrong choosing the list: stop here rather than chain hours of work on it.
        run_log("wide", f"STOPPED: only {n} stocks on the wide list (expected about {WIDE_N}). Check the "
                        f"wide-select note above, then rerun select-wide.")
        with open(STATUS_FILE, "w") as f:
            f.write("stopped")
        return
    finished = history(args, time.monotonic() + 60 * args.max_minutes)
    if finished:
        run_log("wide", f"full options history done for all {n} wide-list stocks.")
    with open(STATUS_FILE, "w") as f:
        f.write("done" if finished else "more")
    left = [t for t in history_tickers() if t not in {r["ticker"] for r in db().history_done()}]
    print("Wide history complete." if finished else f"Wide history: {len(left)} stocks to go; another round needed.")


def history(args, deadline=None):
    """Full daily options history for every ticker with several events. Resumable per ticker.
    Returns True when every eligible ticker is done."""
    deadline = deadline or time.monotonic() + 60 * getattr(args, "max_minutes", 50)
    done = {r["ticker"] for r in db().history_done()}
    todo = [t for t in history_tickers() if t not in done]
    print(f"Full history: {len(done)} tickers done, {len(todo)} to go.")
    today = dt.date.today().isoformat()
    for t in todo:
        if time.monotonic() > deadline:
            return False
        daily = db().daily(t)
        try:
            merge_stock_bars(daily, stock_bars([t], add_days(ALPACA_HISTORY_START, -5), today))
            rows = {r["date"]: r for r in daily if r["ticker"] == t and r["date"] >= ALPACA_HISTORY_START}
            closes = {d: to_float(r.get("stock_close")) for d, r in rows.items()}
            result = option_full_history(t, sorted(rows), closes, deadline)
        except Exception as ex:
            log_error({"ticker": t, "event_date": "full-history"}, ex)
            print(f"  {t}: FAILED {str(ex)[:150]}")
            continue
        if result is None:            # ran out of time mid-ticker; it restarts next run
            return False
        for d, v in result.items():
            rows[d].update(v)
            rows[d]["_dirty"] = True
        save(t, daily)
        db().mark_history(t, today)
    return True


def backfill(args):
    """Everything, under one time budget. Writes 'done' or 'more' to backfill_status.txt so the
    GitHub workflow knows whether to launch another round."""
    deadline = time.monotonic() + 60 * args.max_minutes
    left = lambda: max(1.0, (deadline - time.monotonic()) / 60)
    if args.round <= 1:
        find_movers(argparse.Namespace(start=args.start, end=None, min_move=args.min_move,
                                       universe=args.universe))
    finished = history(args, deadline)
    if finished:   # windows for history tickers are already filled, so these are quick
        finished = collect(argparse.Namespace(lookback=args.lookback, max_minutes=left()))
    if finished:
        finished = controls(argparse.Namespace(per_event=args.per_event, lookback=args.lookback,
                                               max_minutes=left()))
    features(argparse.Namespace(lookback=args.lookback, all=False))
    with open(STATUS_FILE, "w") as f:
        f.write("done" if finished else "more")
    print("Backfill complete." if finished else "Backfill not finished yet; another round needed.")


def nightly(args):
    """The automatic loop: seed new movers from the past week, then collect and score."""
    start = add_days(dt.date.today().isoformat(), -args.days_back)
    find_movers(argparse.Namespace(start=start, end=None, min_move=args.min_move,
                                   universe=getattr(args, "universe", None)))
    collect(argparse.Namespace(lookback=args.lookback, max_minutes=40))
    # Keep the full-history tickers current: fill in the last few sessions (only recent rows
    # are loaded, so this stays cheap even with hundreds of tickers).
    today = dt.date.today().isoformat()
    tracked = sorted({r["ticker"] for r in db().history_done()})
    # New trading days' prices for every tracked stock, 100 stocks per request.
    try:
        fresh = stock_bars(tracked, add_days(today, -10), today) if tracked else {}
    except Exception as ex:
        log_error({"ticker": "*", "event_date": today}, ex)
        fresh = {}
    for t in tracked:
        try:
            daily = db().daily(t, since=add_days(today, -20))
            merge_stock_bars(daily, {t: fresh.get(t, [])})
            recent = sorted(r["date"] for r in daily)[-5:]
            fill_window(t, recent, daily)
            save(t, daily)
        except Exception as ex:
            log_error({"ticker": t, "event_date": today}, ex)
    controls(argparse.Namespace(per_event=args.per_event, lookback=args.lookback, max_minutes=30))
    features(argparse.Namespace(lookback=args.lookback, all=False))


def migrate(args):
    """One-time copy of the CSV files in data/ into the database. Safe to rerun (it upserts)."""
    if db().kind != "postgres":
        sys.exit("Set DATABASE_URL to your Neon connection string first.")
    from store import TABLES
    src = Store(url="")   # the CSV files
    for table in TABLES:
        rows = src.backend.read(table)
        if table == "events":
            # Windows already filled in the old files don't need re-checking.
            done = {(f["ticker"], f["event_date"]) for f in src.backend.read("event_features")
                    if (to_float(f.get("days_with_put_call")) or 0) >= 10}
            for r in rows:
                if (r["ticker"], r["event_date"]) in done:
                    r["window_filled"] = "yes"
        if table == "controls":
            done = {(f["ticker"], f["event_date"]) for f in src.backend.read("event_features")
                    if (to_float(f.get("days_with_put_call")) or 0) >= 10}
            for r in rows:
                if (r["ticker"], r["event_date"]) in done:
                    r["window_filled"] = "yes"
        for i in range(0, len(rows), 5000):
            db().backend.upsert(table, rows[i:i + 5000])
        print(f"  {table}: {len(rows)} rows copied")
    print("Migration complete.")


def write_lessons_page(q, has, lessons):
    """LESSONS.md: every generation's lessons document, plus the weekly reasoning of each lineage's
    latest runs (what the agent said each week, including weeks it passed)."""
    out = [f"# Agent notes ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
           "Every lessons document each generation passed on, oldest first, then what the agents wrote",
           "week by week in their latest runs. Lineages without -v2 are the first test, whose weekly",
           "replies were cut off (no trades) and were not saved.", ""]
    for lin, gen, model, created, text in lessons:
        out += [f"## {lin}, generation {gen} ({model}, {created})", "", text or "(empty)", ""]
    if has("agent_runs"):
        latest = q("select distinct on (lineage, phase) run_id, lineage, generation, phase from agent_runs "
                   "where replies is not null order by lineage, phase, started desc")
        for run_id, lin, gen, phase in sorted(latest, key=lambda r: (r[1], r[3] != "train")):
            out += [f"## Weekly notes: {lin}, generation {gen}, {phase}", ""]
            trades = {}
            reasons = {}
            for wi, action, exp, strike, ex, ret, why in q(
                    f"select week_index, action, expiry, strike_pct, exit_rule, ret_pct, reason from agent_trades "
                    f"where run_id = '{run_id}' order by week_index"):
                what = "stock" if action == "stock" else f"call {exp}d +{strike:g}% {ex}"
                trades.setdefault(wi, []).append(f"{what} {ret:+.0f}%" if phase == "train" else what)
                reasons[wi] = why
            weeks = q(f"select week_index, why from agent_weeks where run_id = '{run_id}' order by week_index") \
                if has("agent_weeks") else []
            if not weeks:   # runs from before weekly notes were saved: weeks with trades only
                weeks = sorted(reasons.items())
                out.append("(weeks the agent passed were not recorded for this run)")
            for wi, why in weeks:
                bought = "; ".join(trades.get(wi, [])) or "pass"
                out.append(f"- week {wi + 1} [{bought}]: {why}")
            out.append("")
    with open(os.path.join(ROOT, "LESSONS.md"), "w") as f:
        f.write("\n".join(out) + "\n")


def status(args):
    """Progress snapshot written to STATUS.md (the GitHub status workflow commits it)."""
    st = db()
    lines = [f"# Status ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC, storage: {st.kind})", ""]
    if st.kind != "postgres":
        lines.append("Not connected to the database (DATABASE_URL not set).")
    else:
        q = lambda sql: st.backend.conn.execute(sql).fetchall()
        one = lambda sql: q(sql)[0][0]
        ev = one("select count(*) from events")
        ev_filled = one("select count(*) from events where window_filled = 'yes'")
        ct_filled = one("select count(*) from controls where window_filled = 'yes'")
        lines += [
            "## Backfill",
            f"- Big moves logged: {ev:,} across {one('select count(distinct ticker) from events'):,} stocks",
            f"- Pre-move windows filled: {ev_filled:,} of {ev:,}",
            f"- Stocks eligible for full history (3+ moves): "
            f"{one('select count(*) from (select ticker from events group by ticker having count(*) >= 3) x'):,}; "
            f"done: {one('select count(*) from history_done'):,}",
            f"- Control days: {one('select count(*) from controls'):,} "
            f"(filled {ct_filled:,})",
            f"- Daily rows: {one('select count(*) from daily'):,}; database size: "
            f"{one('select pg_size_pretty(pg_database_size(current_database()))')}",
            ""]
        sizes = q("select relname, pg_total_relation_size(relid), n_live_tup from pg_stat_user_tables "
                  "order by 2 desc")
        lines += ["## Table sizes"] + [f"- {n}: {b / 1e6:.0f} MB, about {r:,} rows" for n, b, r in sizes]
        lines += ["", "## Labels"]
        lines += [f"- {lab or 'none'}: {n:,}" for lab, n in q("select label, count(*) from events group by label order by 2 desc")]
        lines += ["", "## Ladder backtest"]
        has = lambda t: one(f"select to_regclass('public.{t}') is not null")
        lines += [f"- {g}: {d:,} days, {n:,} contracts ({f:,} could be bought)" for g, d, n, f in (q(
            "select grp, count(distinct (ticker, signal_date)), count(*), count(*) filter (where filled='yes') "
            "from ladder_trades group by grp order by grp") if has("ladder_trades") else [])] or (
            ["- raw trades archived to a GitHub Release; summary kept in ladder_report"]
            if one("select count(*) from ladder_report") else ["- no trades yet"])
        rep = q("select move_pct, rule, days_fired, hit_rate_pct, lift, lift_half1, lift_half2, drop_lift, "
                "median_fwd_return_pct, run_date from signal_report order by move_pct, lift desc")
        if rep:
            lines += ["", f"## Signal report (run {rep[0][9]}): rally within 10 sessions",
                      "| big move | rule | fired | hit % | lift | 1st half | 2nd half | drop lift | median 10-day return % |",
                      "|---|---|---|---|---|---|---|---|---|"]
            lines += [f"| {m:g}% | {r} | {n:,} | {h} | {l} | {l1} | {l2} | {dl} | {md} |"
                      for m, r, n, h, l, l1, l2, dl, md, _ in rep]
        lines += ["", "## Flags (daily shortlist)",
                  f"- {one('select count(*) from flags'):,} flags; latest signal date: {one('select max(signal_date) from flags')}"]
        runs = q("select lineage, generation, phase, model, trades, profit_usd, baseline_profit_usd, mean_ret, "
                 "median_ret, win_rate, baseline_mean, baseline_win, "
                 "case when replies is null then '' else coalesce(bad_replies, 0) || '/' || replies end, "
                 "cost_usd, status from agent_runs order by started") if has("agent_runs") else []
        if runs:
            lines += ["", "## Trader generations",
                      "| lineage | gen | phase | model | trades | profit $ | random profit $ | mean % | median % | win % | random mean % | random win % | unreadable | cost $ | status |",
                      "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
            lines += ["| " + " | ".join("" if v is None else str(v) for v in r) + " |" for r in runs]
        lessons = q("select lineage, generation, model, created, text from agent_lessons "
                    "order by lineage, generation") if has("agent_lessons") else []
        latest = {}
        for lin, gen, model, created, text in lessons:
            latest[lin] = (gen, model, text)
        for lin, (gen, model, text) in sorted(latest.items()):
            lines += ["", f"### Latest lessons: {lin} lineage, generation {gen} ({model})", "", text]
        write_lessons_page(q, has, lessons)
        if has("wide_universe"):
            n_w = one("select count(*) from wide_universe")
            n_wd = one("select count(*) from wide_universe w join history_done h using (ticker)")
            lines += ["", "## Wide list (chosen without hindsight)",
                      f"- {n_w} stocks chosen; full options history done for {n_wd}"]
        if has("run_log"):
            lines += ["", "## Job notes (latest 8)"]
            lines += [f"- {w} {s_}: {m}" for w, s_, m in q(
                "select logged_at, step, message from run_log order by id desc limit 8")] or ["- none"]
        lines += ["", f"## Errors ({one('select count(*) from errors'):,} total, latest 8)"]
        lines += [f"- {w} {t} {e}: {msg[:160]}" for w, t, e, msg in q(
            "select logged_at, ticker, event_date, error from errors order by id desc limit 8")] or ["- none"]
    with open(os.path.join(ROOT, "STATUS.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("find-movers"); a.add_argument("--start", required=True)
    a.add_argument("--end"); a.add_argument("--min-move", type=float, default=15)
    a.add_argument("--universe", choices=["core", "all"])
    b = sub.add_parser("collect"); b.add_argument("--lookback", type=int, default=15)
    b.add_argument("--max-minutes", type=float, default=50)
    c = sub.add_parser("controls"); c.add_argument("--per-event", type=int, default=2)
    c.add_argument("--max-minutes", type=float, default=50)
    c.add_argument("--lookback", type=int, default=15)
    d = sub.add_parser("features"); d.add_argument("--lookback", type=int, default=15)
    d.add_argument("--all", action="store_true", help="recompute every row, not just new ones")
    e = sub.add_parser("compare"); e.add_argument("--ticker", default="WOLF")
    n = sub.add_parser("nightly"); n.add_argument("--days-back", type=int, default=7)
    n.add_argument("--universe", choices=["core", "all"])
    n.add_argument("--min-move", type=float, default=15); n.add_argument("--lookback", type=int, default=15)
    n.add_argument("--per-event", type=int, default=2)
    h = sub.add_parser("history"); h.add_argument("--max-minutes", type=float, default=50)
    w = sub.add_parser("wide", help="choose the hindsight-free wide list and pull its options history")
    w.add_argument("--max-minutes", type=float, default=100)
    w.add_argument("--n", type=int, default=WIDE_N)
    w.add_argument("--reselect", action="store_true")
    sw = sub.add_parser("select-wide", help="choose the wide list only (no history)")
    sw.add_argument("--n", type=int, default=WIDE_N)
    sw.add_argument("--reselect", action="store_true")
    sub.add_parser("migrate", help="copy the CSV files in data/ into the database (one time)")
    sub.add_parser("status", help="write a progress snapshot to STATUS.md")
    f = sub.add_parser("backfill"); f.add_argument("--max-minutes", type=float, default=100)
    f.add_argument("--round", type=int, default=1); f.add_argument("--start", default="2024-03-01")
    f.add_argument("--min-move", type=float, default=15); f.add_argument("--lookback", type=int, default=15)
    f.add_argument("--per-event", type=int, default=2); f.add_argument("--universe", choices=["core", "all"])
    args = p.parse_args()
    {"find-movers": find_movers, "collect": collect, "controls": controls, "features": features,
     "compare": compare, "nightly": nightly, "history": history, "backfill": backfill,
     "migrate": migrate, "status": status, "wide": wide, "select-wide": select_only}[args.cmd](args)


if __name__ == "__main__":
    main()
