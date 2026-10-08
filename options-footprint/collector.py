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
import json
import os
import random
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

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
DEFAULT_UNIVERSE = "core"
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
MIN_SECONDS_BETWEEN_REQUESTS = 0.35   # about 170 a minute, under Alpaca's free limit of 200


def http_json(url, headers=None):
    for attempt in range(5):
        try:
            wait = _last_request[0] + MIN_SECONDS_BETWEEN_REQUESTS - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            _last_request[0] = time.monotonic()
            req = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:              # rate limited: back off and retry
                time.sleep(2 ** attempt)
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


def option_daily_volume(ticker, dates, closes):
    """Per day: call volume, put volume, put/call, and short-dated out-of-the-money call volume."""
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
    # Contracts adjusted after a split or merger get non-standard symbols (e.g. "1CHPT...") that
    # the bars endpoint rejects, and their strikes no longer match the stock price anyway.
    symbols = sorted(s for s in contracts if STANDARD_OPTION_SYMBOL.match(s))
    totals = {d: {k: 0 for k in ("call", "put", "short_otm_call") + CALL_BUCKETS} for d in dates}
    for i in range(0, len(symbols), 100):
        chunk = symbols[i:i + 100]
        pages = alpaca_get("https://data.alpaca.markets", "/v1beta1/options/bars",
                           {"symbols": ",".join(chunk), "timeframe": "1Day",
                            "start": start, "end": safe_end(end), "limit": 10000},
                           cache_name=f"optbars_{ticker}_{start}_{end}_{chunk_key(chunk)}.json")
        for page in pages:
            for sym, bars in (page.get("bars") or {}).items():
                c = contracts.get(sym)
                if c is None:          # not one we asked for; ignore
                    continue
                for b in bars:
                    d = b["t"][:10]
                    if d not in totals:
                        continue
                    kind = c["type"]                   # "call" or "put"
                    totals[d][kind] += b["v"]
                    close = closes.get(d)
                    days_left = (dt.date.fromisoformat(c["expiration_date"]) - dt.date.fromisoformat(d)).days
                    if kind != "call":
                        continue
                    strike = float(c["strike_price"])
                    # Where did the call buying land? By time to expiration...
                    if days_left <= SHORT_DATED_DAYS:
                        totals[d]["call_vol_short"] += b["v"]
                    elif days_left <= MEDIUM_DATED_DAYS:
                        totals[d]["call_vol_medium"] += b["v"]
                    else:
                        totals[d]["call_vol_long"] += b["v"]
                    # ...and by strike versus the stock price.
                    if close:
                        if strike >= close * (1 + OTM_PCT):
                            totals[d]["call_vol_otm"] += b["v"]
                            if days_left <= SHORT_DATED_DAYS:
                                totals[d]["short_otm_call"] += b["v"]
                        elif strike <= close * (1 - OTM_PCT):
                            totals[d]["call_vol_itm"] += b["v"]
                        else:
                            totals[d]["call_vol_atm"] += b["v"]
    out = {}
    for d, t in totals.items():
        out[d] = {"call_volume": t["call"], "put_volume": t["put"],
                  "short_otm_call_volume": t["short_otm_call"],
                  "put_call_alpaca": round(t["put"] / t["call"], 3) if t["call"] else ""}
        out[d].update({k: t[k] for k in CALL_BUCKETS})
    return out


# ---------------------------------------------------------------- dataset plumbing
def load_daily():
    return read_csv(DAILY)


def save_daily(daily):
    write_csv(DAILY, sorted(daily, key=lambda r: (r["ticker"], r["date"])), DAILY_FIELDS)


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


def log_error(event, ex):
    rows = read_csv(ERRORS)
    rows.append({"when": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M"),
                 "ticker": event["ticker"], "event_date": event["event_date"],
                 "error": str(ex)[:300]})
    write_csv(ERRORS, rows[-500:], ["when", "ticker", "event_date", "error"])


# ---------------------------------------------------------------- commands
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
    events = read_csv(EVENTS)
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
    added = 0
    for sym, date, move, pc, c in found:
        if (sym, date) in have:
            continue
        n = len(by_date[date])
        events.append({"ticker": sym, "event_date": date, "event_type": "close_to_close",
                       "move_pct": f"{move:.1f}", "prior_close": pc, "event_close": c,
                       "catalyst": "Unconfirmed",
                       "label": ("check_corporate_action" if move > BIG_MOVE_REVIEW
                                 else "sector_day" if n >= crowd else "unknown"),
                       "notes": f"{n} of {len(bars)} scanned names up {args.min_move:g}%+ that day"})
        added += 1
    write_csv(EVENTS, events, EVENT_FIELDS)
    # Only keep price history for tickers that have events; the full universe would make
    # the file far too large for GitHub.
    keep = {e["ticker"] for e in events}
    daily = load_daily()
    raw = stock_bars(sorted(keep & set(bars)), add_days(args.start, -35), end)  # raw: matches option strikes
    merge_stock_bars(daily, raw)
    save_daily(daily)
    flagged = sum(1 for f in found if f[2] > BIG_MOVE_REVIEW)
    print(f"Scanned {len(bars)} tickers: {len(found)} moves of {args.min_move:g}%+, {added} new events added"
          f" ({flagged} over {BIG_MOVE_REVIEW:g}% kept but flagged for review).")


def collect(args, rows=None, label="events"):
    """Fill pre-move windows. Stops cleanly at --max-minutes; rerun to continue where it left off."""
    daily = load_daily()
    rows = rows if rows is not None else read_csv(EVENTS)
    deadline = time.monotonic() + 60 * getattr(args, "max_minutes", 50)
    done = 0
    for n, e in enumerate(rows, 1):
        if e["event_date"] < ALPACA_HISTORY_START:
            continue
        if time.monotonic() > deadline:
            print(f"Time budget reached after {done} {label}; saved. Run it again to continue.")
            break
        try:
            ensure_prices(e["ticker"], add_days(e["event_date"], -60), e["event_date"], daily)
            window = days_before(e["ticker"], e, args.lookback, daily)
            fill_window(e["ticker"], window, daily)
        except Exception as ex:   # log it, keep going; rerunning retries failed ones
            log_error(e, ex)
            print(f"{label} {n}/{len(rows)}: {e['ticker']} {e['event_date']} FAILED: {str(ex)[:150]}")
            continue
        done += 1
        print(f"{label} {n}/{len(rows)}: {e['ticker']} {e['event_date']} ({len(window)} days)")
        if done % 10 == 0:
            save_daily(daily)  # don't lose progress if the job is cut off
    save_daily(daily)


def controls(args):
    """Random quiet dates for the same tickers, so we can measure false positives."""
    daily, events = load_daily(), read_csv(EVENTS)
    rng = random.Random(42)
    rows = read_csv(CONTROLS)
    have = {(r["ticker"], r["event_date"]) for r in rows}
    for e in events:
        tk = e["ticker"]
        days = sorted(r["date"] for r in daily if r["ticker"] == tk and r.get("stock_close"))
        closes = {r["date"]: to_float(r["stock_close"]) for r in daily if r["ticker"] == tk}
        event_days = [x["event_date"] for x in events if x["ticker"] == tk]
        ok = []
        for i in range(args.lookback + 1, len(days)):
            d, p = days[i], days[i - 1]
            if d < ALPACA_HISTORY_START:
                continue
            if any(abs((dt.date.fromisoformat(d) - dt.date.fromisoformat(x)).days) < 15 for x in event_days):
                continue
            if closes.get(d) and closes.get(p) and abs(closes[d] / closes[p] - 1) < 0.05:
                ok.append(d)
        existing = sum(1 for r in rows if r["ticker"] == tk)
        need = max(0, args.per_event * len(event_days) - existing)
        for d in rng.sample(ok, min(need, len(ok))):
            if (tk, d) not in have:
                rows.append({"ticker": tk, "event_date": d, "event_type": "control", "label": "control"})
                have.add((tk, d))
    write_csv(CONTROLS, rows, EVENT_FIELDS)
    collect(args, rows, label="control")
    print(f"{len(rows)} control dates on file.")


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
    daily = load_daily()
    rows = [compute(e, daily, args.lookback) for e in read_csv(EVENTS) + read_csv(CONTROLS)]
    write_csv(FEATURES, rows, FEATURE_FIELDS)
    ev = [r for r in rows if r["label"] != "control"]
    ct = [r for r in rows if r["label"] == "control"]
    print(f"{len(ev)} events, {len(ct)} controls -> {FEATURES}")
    for group, name in ((ev, "events"), (ct, "controls")):
        drops = [r["put_call_drop_ratio"] for r in group if "put_call_drop_ratio" in r]
        if drops:
            hits = sum(1 for x in drops if x >= 5)
            print(f"  {name}: {hits}/{len(drops)} had a put/call drop of 5x or more")


def compare(args):
    """Check Alpaca-computed put/call against the Alpha Vantage values already on file."""
    daily = load_daily()
    rows = sorted((r for r in daily if r["ticker"] == args.ticker and r.get("put_call_ratio")),
                  key=lambda r: r["date"])
    if not rows:
        sys.exit(f"No Alpha Vantage values on file for {args.ticker}.")
    ensure_prices(args.ticker, add_days(rows[0]["date"], -5), rows[-1]["date"], daily)
    fill_window(args.ticker, [r["date"] for r in rows], daily, refresh=True)
    save_daily(daily)
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


def nightly(args):
    """The automatic loop: seed new movers from the past week, then collect and score."""
    start = add_days(dt.date.today().isoformat(), -args.days_back)
    find_movers(argparse.Namespace(start=start, end=None, min_move=args.min_move,
                                   universe=getattr(args, "universe", None)))
    collect(argparse.Namespace(lookback=args.lookback, max_minutes=50))
    controls(argparse.Namespace(per_event=args.per_event, lookback=args.lookback, max_minutes=40))
    features(argparse.Namespace(lookback=args.lookback))


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
    e = sub.add_parser("compare"); e.add_argument("--ticker", default="WOLF")
    n = sub.add_parser("nightly"); n.add_argument("--days-back", type=int, default=7)
    n.add_argument("--universe", choices=["core", "all"])
    n.add_argument("--min-move", type=float, default=15); n.add_argument("--lookback", type=int, default=15)
    n.add_argument("--per-event", type=int, default=2)
    args = p.parse_args()
    {"find-movers": find_movers, "collect": collect, "controls": controls, "features": features,
     "compare": compare, "nightly": nightly}[args.cmd](args)


if __name__ == "__main__":
    main()
