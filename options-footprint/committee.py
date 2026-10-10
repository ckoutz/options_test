"""
Committee generations: four independent agents, stock bundles, a code-kept scorebook, and an editor.

Data split (python committee.py build-pool --archive ladder_trades.csv.gz):
  - Every stock is dealt into one of 8 BUNDLES, matched on how many big moves it had and how
    volatile it is. Bundles 7 and 8 are held back for the final exam and never used before it.
  - Months from March 2024 to January 2026 are cut into 3-month blocks; one month in each block,
    picked at random, is a blind SCORING month and the rest are TRAINING months. Candidates whose
    10-session outcome would run into a month of the other kind are dropped (the buffer), so no
    outcome straddles training and scoring.
  - February 2026 onward is the TEST period: the one-time forward final exam.

One generation (python committee.py loop):
  1. Four agents each start from the notes and scorebook passed down by the previous generation.
     Independently, each walks the six training bundles in the same shuffled order, week by week:
     it rates every candidate from -2 to +2 and may buy up to 3 (stock or a call). Results show up
     two weeks later. After each bundle it rewrites its own working notes; after the last it states
     its strongest ideas as testable rules.
  2. SCOREBOOK: code tests every rule on every training candidate in all six bundles, including
     stocks the author never saw, and reports trades, returns, a 95% range, how buying every
     candidate the same way did, and how many bundles the rule beat that in.
  3. EDITOR: a fifth agent reads the four agents' notes and their scorebook results and writes
     the combined notes (no length limit) and rules for the next generation. Only the editor's
     notes and the training scorebook of its rules pass on.
  4. BLIND SCORING: a fresh agent trades the scoring months with the editor's notes and no
     feedback, and the editor's rules are scored mechanically on those months. Neither result is
     ever shown to a later generation.

    python committee.py build-pool --archive ladder_trades.csv.gz
    python committee.py loop --generations 5
    python committee.py final-test --generation 7
    python committee.py report                      # writes COMMITTEE.md
"""
import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import gzip
import json
import math
import os
import random
import re
import statistics
import sys
import threading
import time
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C  # noqa: E402
import scorer as S     # noqa: E402
import agents as A     # noqa: E402

N_BUNDLES = 8
HOLDOUT_BUNDLES = (7, 8)
TRAIN_BUNDLES = (1, 2, 3, 4, 5, 6)
TEST_START = "2026-02-01"
FIRST_MONTH = "2024-03"
BUFFER_DAYS = 15                  # about 10 trading sessions
PER_WEEK = 10                     # candidates per bundle per week (up to 6 big movers + 4 wide-list)
N_AGENTS = 4
MAX_PICKS = 3
REVEAL_DAYS = 14
LABEL_TO_KEY = {label: key for key, label, _ in A.FEATURES}
CFG = {"lineage": "committee", "options_only": False, "seed": "none"}

SEED_NOTES = """Starting briefing from the research team (not from an earlier trader). Treat it as background, not as rules.

What this project is looking for: signs of informed buying before big moves. The original idea: when someone
knows good news is coming, they buy calls quietly, so call volume jumps and the put/call ratio collapses (say
from 0.8 to 0.08) while the stock itself is still calm. We collected options activity for hundreds of volatile
stocks to see whether that footprint shows up before 15%+ up days and can be traded.

What we have found so far:
- Call volume spikes on their own barely predict rallies: after 5x+ normal call volume, a 30%+ rally within 10
  sessions came about 1.1 to 1.3 times as often as on an average day, but big drops came about as often too.
- Call spikes right after a 10%+ week predicted big moves in BOTH directions (rallies 1.8x as often, drops
  1.6x). They flag volatility more than direction.
- "Quiet" call buying (a big call spike while share volume and price stay calm) was followed by FEWER big
  moves than average, the opposite of the original idea, at least in that simple form.
- A collapse in the put/call ratio on its own predicted nothing.
- Calls bought blindly on these stocks lose most of the time: after 10 sessions the typical (median) result
  ranged from about -20% (90-day calls) to -80% (14-day calls 20% above the price). An options edge has to
  beat that decay plus the 5% cost each way.
- An earlier committee, trading mostly shares, found price setups mattered more than the flow numbers in its
  training data: stocks more than 10% below their 50-day average but up on the day averaged +4.0% over 10
  sessions (219 trades, versus +1.1% for buying everything), and momentum after a 15%+ month looked good at
  first and then faded.

Nobody has found an options-flow pattern that works yet. The simple versions are exhausted; any edge is
likely in combinations: where the call buying lands (short versus long expiry, out of the money versus near
the money), calls versus puts together, flow combined with the price setup, or which calls are cheap versus
expensive. That is the frontier: be creative.
"""
OPS = {">": lambda a, b: a > b, ">=": lambda a, b: a >= b, "<": lambda a, b: a < b,
       "<=": lambda a, b: a <= b, "=": lambda a, b: a == b}


# ---------------------------------------------------------------- the pool
def month_of(date):
    return date[:7]


def split_months(months):
    """One random month in each 3-month block is a scoring month; the rest train."""
    rng = random.Random("committee-split-v1")
    train_months, y, mo = [], int(FIRST_MONTH[:4]), int(FIRST_MONTH[5:])
    while f"{y:04d}-{mo:02d}" < TEST_START[:7]:      # every calendar month, data or not
        train_months.append(f"{y:04d}-{mo:02d}")
        y, mo = (y + 1, 1) if mo == 12 else (y, mo + 1)
    split = {}
    for i in range(0, len(train_months), 3):
        block = train_months[i:i + 3]
        pick = rng.choice(block)
        for m in block:
            split[m] = "score" if m == pick else "train"
    for m in months:
        if m >= TEST_START[:7]:
            split[m] = "test"
        elif m < FIRST_MONTH:
            split[m] = "skip"
    return split


def split_of(date, month_split):
    m = month_of(date)
    s = month_split.get(m, "skip")
    ahead = (dt.date.fromisoformat(date) + dt.timedelta(days=BUFFER_DAYS)).isoformat()
    if s != "test" and month_split.get(month_of(ahead), s) != s:
        return "buffer"           # the 10-session outcome would run into the other kind of month
    return s


def deal_bundles(stats):
    """stats: ticker -> (big moves, volatility). Deal stocks into bundles in matched groups of 8."""
    order = sorted(stats, key=lambda t: (-stats[t][0], -stats[t][1], t))
    bundle = {}
    for i in range(0, len(order), N_BUNDLES):
        group = order[i:i + N_BUNDLES]
        slots = list(range(1, N_BUNDLES + 1))
        random.Random(f"deal-{i}").shuffle(slots)
        for t, b in zip(group, slots):
            bundle[t] = b
    return bundle


def ladder_files(st, archive):
    """Where priced option ladders live: the archive release file, plus any rows still in the
    database's ladder table (the wide-list ladder), exported once to a temporary file."""
    paths = []
    if archive:
        if not os.path.exists(archive):
            sys.exit(f"Archive file {archive} not found (download it from the ladder-trades-archive release).")
        paths.append(archive)
    if st.kind == "postgres":
        conn = st.backend.conn
        if conn.execute("select to_regclass('public.ladder_trades') is not null").fetchone()[0] and \
                conn.execute("select exists (select 1 from ladder_trades)").fetchone()[0]:
            tmp = os.path.join(C.DATA, "ladder_live.csv.gz")
            with gzip.open(tmp, "wb") as gz, conn.cursor() as cur:
                with cur.copy("COPY ladder_trades TO STDOUT WITH (FORMAT csv, HEADER true)") as copy:
                    for chunk in copy:
                        gz.write(chunk)
            paths.append(tmp)
    if not paths:
        sys.exit("No ladder data: pass --archive or run the ladder first.")
    return paths


def ladder_rows(paths):
    for path in paths:
        with gzip.open(path, "rt", newline="") as f:
            yield from csv.DictReader(f)


def market_closes():
    """Daily closes of the S&P 500 fund (SPY), for market context. Empty if Alpaca isn't set up."""
    try:
        bars = C.stock_bars(["SPY"], "2023-12-01", dt.date.today().isoformat())
        return {b["date"]: b["close"] for b in bars.get("SPY", [])}
    except (Exception, SystemExit) as ex:   # noqa: BLE001 - market context is a nice-to-have (or no keys)
        print(f"Market context unavailable ({str(ex)[:100]}); those columns will be blank.")
        return {}


LADDER_COST = 0.05          # what the ladder charged on each side
MIN_HALF_SPREAD = 0.05      # dollars per share: cheap contracts can't be bought or sold closer than this


def realistic_cell(entry, stock_close, ret_hold, ret_double):
    """Reprice one ladder contract with a more realistic cost. The ladder charged a flat 5% each way,
    which for a $0.20 option is a penny, while real quotes on cheap, thinly traded contracts are often
    5 to 30 cents wide. Here each side costs 5% or $0.05 a share, whichever is larger. Raw prices are
    recovered from what the ladder stored. (The take-profit point of double_or_10 is kept where the
    ladder found it, a close approximation.)"""
    raw_in = entry / (1 + LADDER_COST)
    new_in = raw_in + max(LADDER_COST * raw_in, MIN_HALF_SPREAD)

    def redo(ret):
        if ret is None:
            return None
        value = (ret / 100 + 1) * entry / (1 - LADDER_COST)      # the option's value at the exit
        out = max(0.0, value - max(LADDER_COST * value, MIN_HALF_SPREAD)) if value > 0 else 0.0
        return round((out / new_in - 1) * 100, 2)
    return [round(new_in / stock_close * 100, 2), redo(ret_hold), redo(ret_double)]


RATE = 0.045                 # risk-free rate for implied volatility (close enough for 2024-2026)
US_HOLIDAYS = ["2024-01-01", "2024-01-15", "2024-02-19", "2024-03-29", "2024-05-27", "2024-06-19", "2024-07-04",
               "2024-09-02", "2024-11-28", "2024-12-25", "2025-01-01", "2025-01-09", "2025-01-20", "2025-02-17",
               "2025-04-18", "2025-05-26", "2025-06-19", "2025-07-04", "2025-09-01", "2025-11-27", "2025-12-25",
               "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25", "2026-06-19", "2026-07-03",
               "2026-09-07", "2026-11-26", "2026-12-25"]


def sessions_until(start, end):
    """Trading sessions after `start` up to and including `end` (the expiration day)."""
    import numpy as np
    d0 = (dt.date.fromisoformat(start[:10]) + dt.timedelta(days=1)).isoformat()
    d1 = (dt.date.fromisoformat(end[:10]) + dt.timedelta(days=1)).isoformat()
    return int(np.busday_count(d0, d1, holidays=US_HOLIDAYS))


def call_price(S, K, T, vol, r=RATE):
    if T <= 0 or vol <= 0:
        return max(0.0, S - K)
    d1 = (math.log(S / K) + (r + vol * vol / 2) * T) / (vol * math.sqrt(T))
    d2 = d1 - vol * math.sqrt(T)
    n = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
    return S * n(d1) - K * math.exp(-r * T) * n(d2)


def implied_vol(price, S, K, T, r=RATE):
    """Annualized implied volatility (percent) from a call price, or None when the price is outside
    what any volatility could produce (stale or odd prints)."""
    if not (price and S and K and T and T > 0):
        return None
    lo, hi = 0.01, 6.0
    if price <= call_price(S, K, T, lo, r) or price >= call_price(S, K, T, hi, r):
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if call_price(S, K, T, mid, r) > price:
            hi = mid
        else:
            lo = mid
    return round((lo + hi) / 2 * 100, 1)


def option_detail(row):
    """Sessions from entry to expiration, and implied volatility at entry (from the raw traded price)."""
    try:
        entry_date, expiration = row["entry_date"], row["expiration"]
        sess = sessions_until(entry_date, expiration)
        raw = float(row["entry_price"]) / (1 + LADDER_COST)
        days = (dt.date.fromisoformat(expiration[:10]) - dt.date.fromisoformat(entry_date[:10])).days
        iv = implied_vol(raw, float(row["stock_close"]), float(row["strike"]), max(days, 0.5) / 365)
        return [sess, iv]
    except (KeyError, ValueError, TypeError):
        return [None, None]


def vwap_features(closes, vwaps, volumes, i, n=20):
    """Close versus the day's volume-weighted average price (buyers paying up into the close), and
    versus the 20-session volume-weighted average (where recent volume actually traded)."""
    out = {"close_vs_vwap_pct": None, "vs_vwap20_pct": None}
    c = closes[i]
    if c and vwaps[i]:
        out["close_vs_vwap_pct"] = round((c / vwaps[i] - 1) * 100, 2)
    pairs = [(w, v) for w, v in zip(vwaps[max(0, i - n + 1):i + 1], volumes[max(0, i - n + 1):i + 1]) if w and v]
    if c and len(pairs) >= n // 2:
        avg = sum(w * v for w, v in pairs) / sum(v for _, v in pairs)
        out["vs_vwap20_pct"] = round((c / avg - 1) * 100, 1)
    return out


def runway(values, i, recent=20, before=40):
    """Average over the last `recent` sessions ÷ the median of the `before` sessions ahead of them."""
    if i < recent + before - 1:
        return None
    now = [v for v in values[i - recent + 1:i + 1] if v is not None]
    base = [v for v in values[i - recent - before + 1:i - recent + 1] if v is not None]
    if len(now) < recent // 2 or len(base) < before // 2:
        return None
    med = statistics.median(base)
    return round(statistics.mean(now) / med, 2) if med > 0 else None


def build_pool(args):
    st = C.db()
    paths = ladder_files(st, args.archive)
    days = {}
    for r in ladder_rows(paths):
        if r.get("ret_hold10_pct") not in (None, ""):
            days[(r["ticker"], r["signal_date"])] = r["grp"]
    by_ticker = {}
    for (t, d), g in days.items():
        by_ticker.setdefault(t, {})[d] = g
    movers = set(C.mover_tickers())
    wide_only = set(C.wide_tickers()) - movers
    # Stocks on neither list (e.g. dropped from a re-chosen wide list) are left out of the pool.
    for t in [t for t in by_ticker if t not in movers and t not in wide_only]:
        del by_ticker[t]
    universe = {t: ("wide" if t in wide_only else "movers") for t in by_ticker}
    print(f"Ladder data: {len(days):,} stock-days across {len(by_ticker):,} stocks "
          f"({sum(1 for u in universe.values() if u == 'wide')} from the wide list).")
    spy = market_closes()
    spy_dates = sorted(spy)
    spy_idx = {d: i for i, d in enumerate(spy_dates)}

    def mkt(d, n):
        i = spy_idx.get(d)
        if i is None or i < n:
            return None
        return round((spy[d] / spy[spy_dates[i - n]] - 1) * 100, 1)

    moves = {}
    for e in st.events():
        moves[e["ticker"]] = moves.get(e["ticker"], 0) + 1
    feats, stats = {}, {}
    for n, t in enumerate(sorted(by_ticker), 1):
        rows = [r for r in st.daily(t) if r.get("put_call_alpaca") not in (None, "")]
        if not rows:
            continue
        scored_list = S.score_days({t: rows}, 30.0, 10)
        scored = {d["date"]: d for d in scored_list}
        s_pos = {d["date"]: k for k, d in enumerate(scored_list)}
        dates = [r["date"] for r in rows]
        closes = [C.to_float(r["stock_close"]) for r in rows]
        series = {k: [C.to_float(r.get(k)) for r in rows] for k in ("call_volume", "call_vol_long", "call_vol_otm", "put_volume",
                                                                 "stock_vwap", "stock_volume")}
        index = {d: i for i, d in enumerate(dates)}
        rets_all = [closes[k] / closes[k - 1] - 1 for k in range(1, len(closes)) if closes[k] and closes[k - 1]]
        stats[t] = (moves.get(t, 0), statistics.pstdev(rets_all) if len(rets_all) > 20 else 0.0)
        for d, g in by_ticker[t].items():
            i = index.get(d)
            if i is None or d not in scored or i + 11 >= len(dates) or not closes[i + 1] or not closes[i + 11]:
                continue
            rets = [closes[k] / closes[k - 1] - 1 for k in range(max(1, i - 19), i + 1) if closes[k] and closes[k - 1]]
            f = {k: scored[d].get(k) for k, _, _ in A.FEATURES if k in scored[d]}
            f["vol20_pct"] = round(statistics.pstdev(rets) * 100, 2) if len(rets) > 5 else None
            f.update(A.technicals(closes, i))
            f.update(vwap_features(closes, series["stock_vwap"], series["stock_volume"], i))
            # The last 5 sessions, so buildup over several days is visible, not just today.
            last5 = scored_list[max(0, s_pos[d] - 4):s_pos[d] + 1]

            def avg(key):
                v = [C.to_float(x.get(key)) for x in last5 if C.to_float(x.get(key)) is not None]
                return round(statistics.mean(v), 2) if v else None
            f["calls_5d_avg"] = avg("call_volume_spike")
            f["puts_5d_avg"] = avg("put_volume_spike")
            f["shares_5d_avg"] = avg("stock_volume_spike")
            f["call_days_2x"] = sum(1 for x in last5 if (C.to_float(x.get("call_volume_spike")) or 0) >= 2)
            # The last 20 sessions against the 40 before them: slow, sustained buying that a one-day
            # spike measure misses.
            for key, name in (("call_volume", "calls_20d"), ("call_vol_long", "long_calls_20d"),
                              ("call_vol_otm", "otm_calls_20d"), ("put_volume", "puts_20d")):
                f[name] = runway(series[key], i)
            last20 = scored_list[max(0, s_pos[d] - 19):s_pos[d] + 1]
            f["call_days_2x_20d"] = sum(1 for x in last20 if (C.to_float(x.get("call_volume_spike")) or 0) >= 2)
            back = scored_list[max(0, s_pos[d] - 60):s_pos[d] + 1][::-1]
            f["days_since_spike"] = next((k for k, x in enumerate(back)
                                          if (C.to_float(x.get("call_volume_spike")) or 0) >= 3), 60)
            f["mkt_5d_pct"], f["mkt_20d_pct"] = mkt(d, 5), mkt(d, 20)
            price = closes[i]
            f["price_band"] = "<$10" if price < 10 else "$10-50" if price <= 50 else ">$50"
            shares = (closes[i + 11] * (1 - A.SHARE_COST)) / (closes[i + 1] * (1 + A.SHARE_COST)) - 1
            feats[(t, d)] = (g, f, round(shares * 100, 2))
        if n % 100 == 0:
            print(f"  {n}/{len(by_ticker)} stocks")
    # Bundles are kept stable: a stock keeps its bundle across rebuilds (the first time, the
    # assignments are read from the existing pool), and only new stocks are dealt, each list on its own.
    bundle = {r["ticker"]: int(r["bundle"]) for r in st.backend.read("bundles")}
    if not bundle:
        bundle = {r["ticker"]: int(r["bundle"]) for r in st.backend.read("pool")}
    for u in ("movers", "wide"):
        fresh = {t: v for t, v in stats.items() if t not in bundle and universe[t] == u}
        if fresh:
            bundle.update(deal_bundles(fresh))
    st.backend.upsert("bundles", [{"ticker": t, "bundle": b, "universe": universe.get(t, "movers")}
                                  for t, b in bundle.items() if t in stats])
    month_split = split_months(sorted({month_of(d) for _, d in feats}))
    groups = {}
    for (t, d), (g, f, sh) in feats.items():
        b = bundle[t]
        s = "holdout" if b in HOLDOUT_BUNDLES and month_split.get(month_of(d)) != "test" else split_of(d, month_split)
        if s in ("skip", "buffer"):
            continue
        groups.setdefault((b, A.week_of(d), s, universe[t]), []).append((t, d))
    quota = {"movers": args.per_week_movers, "wide": args.per_week_wide}
    picked = []
    for key, items in groups.items():
        seen = set()
        for t, d in sorted(items, key=lambda x: A.rank("pool", x[0], x[1])):
            if t in seen:
                continue
            seen.add(t)
            picked.append((key, t, d))
            if len(seen) >= quota[key[3]]:
                break
    want = {(t, d) for _, t, d in picked}
    options = {}
    for r in ladder_rows(paths):
        k = (r["ticker"], r["signal_date"])
        if k not in want:
            continue
        ok = r["filled"] == "yes" and r["entry_price"] and r["stock_close"]
        cell = f"{int(float(r['target_dte']))}d+{float(r['target_otm_pct']):g}"
        options.setdefault(k, {})[cell] = realistic_cell(
            float(r["entry_price"]), float(r["stock_close"]), C.to_float(r["ret_hold10_pct"]),
            C.to_float(r["ret_double_or_10_pct"])) + option_detail(r) if ok else None
    import news as N
    nidx = N.Index(st, {t for _, t, _ in picked}) if st.backend.read("news_fetched") else None
    out = []
    for (b, wk, s, u), t, d in picked:
        g, f, sh = feats[(t, d)]
        if nidx:
            f.update(nidx.features(t, d, f.get("call_volume_spike")))
        out.append({"ticker": t, "signal_date": d, "bundle": b, "split": s, "week": wk, "month": month_of(d),
                    "grp": g, "universe": u, "features": json.dumps(f, separators=(",", ":")),
                    "options": json.dumps({k: v for k, v in options.get((t, d), {}).items() if v},
                                          separators=(",", ":")),
                    "shares_ret10": sh})
    # Sanity check before replacing anything: a much smaller pool, or a missing wide list, means
    # something upstream went wrong. Keep the old pool and say so.
    old_n = len(st.backend.read("pool"))
    n_wide = sum(1 for r in out if r["universe"] == "wide")
    problems = []
    if old_n and len(out) < 0.7 * old_n:
        problems.append(f"new pool has {len(out):,} candidates versus {old_n:,} before")
    if wide_only and n_wide == 0:
        problems.append(f"the wide list has {len(wide_only)} stocks but none made it into the pool")
    if problems and not getattr(args, "force", False):
        C.run_log("build-pool", "STOPPED, old pool kept: " + "; ".join(problems) + ". Rerun with --force if intended.")
        sys.exit("Pool not replaced: " + "; ".join(problems))
    st.backend.replace("pool", out)
    C.run_log("build-pool", f"pool rebuilt: {len(out):,} candidates ({n_wide:,} from the wide list).")
    counts = {}
    for r in out:
        key = f"{r['split']}/{r['universe']}"
        counts[key] = counts.get(key, 0) + 1
    print(f"Pool built: {len(out):,} candidates {dict(sorted(counts.items()))}; scoring months: "
          f"{sorted(m for m, s in month_split.items() if s == 'score')}")
    per_bundle = {b: sum(1 for r in out if r["bundle"] == b) for b in range(1, N_BUNDLES + 1)}
    print(f"Candidates per bundle: {per_bundle}")


def add_vol_columns(f, o):
    """Implied volatility of the ~30-day at-the-money call, realized volatility (both annualized), and
    their ratio: above 1 means options are priced for bigger moves than the stock has been making."""
    atm = o.get("30d+0") or o.get("90d+0") or {}
    iv = atm.get("iv")
    rv = f.get("vol20_pct")
    rv = round(float(rv) * math.sqrt(252), 1) if rv not in (None, "") else None
    f["iv30_atm"] = iv
    f["rv20_ann"] = rv
    f["iv_rv"] = round(iv / rv, 2) if iv and rv else None


def load_pool(st):
    pool = []
    for r in st.backend.read("pool"):
        o = {}
        for k, v in json.loads(r["options"]).items():
            if v:
                o[k] = {"cost_pct": v[0], "hold10": v[1], "double_or_10": v[2],
                        "sessions": v[3] if len(v) > 3 else None, "iv": v[4] if len(v) > 4 else None}
        f = json.loads(r["features"])
        add_vol_columns(f, o)
        pool.append({"ticker": r["ticker"], "date": r["signal_date"], "bundle": int(r["bundle"]),
                     "split": r["split"], "week": r["week"], "month": r["month"],
                     "f": f, "o": o, "shares": float(r["shares_ret10"]),
                     "universe": r.get("universe") or "movers"})
    return pool


# ---------------------------------------------------------------- rules and the scorebook
def clean_rules(raw):
    """Keep well-formed rules only; columns are the labels the agents see."""
    out = []
    for r in raw if isinstance(raw, list) else []:
        if not isinstance(r, dict):
            continue
        conds = []
        for c in r.get("when") or []:
            if not isinstance(c, dict):
                continue
            key, op, val = LABEL_TO_KEY.get(str(c.get("col", "")).strip()), str(c.get("op", "")).strip(), c.get("value")
            if not key or op not in OPS:
                continue
            if key == "price_band":
                if op != "=" or str(val) not in ("<$10", "$10-50", ">$50"):
                    continue
                conds.append({"col": c["col"], "op": op, "value": str(val)})
            else:
                try:
                    conds.append({"col": c["col"], "op": op, "value": float(val)})
                except (TypeError, ValueError):
                    continue
        if not conds or len(conds) > 5:
            continue
        rule = {"name": str(r.get("name") or "rule")[:80], "when": conds}
        if str(r.get("buy", "")).lower() == "stock" and CFG["options_only"]:
            continue
        if str(r.get("buy", "")).lower() == "stock":
            rule["buy"] = "stock"
        else:
            try:
                e, s = int(r.get("expiry")), float(r.get("strike"))
            except (TypeError, ValueError):
                continue
            if e not in A.EXPIRIES or s not in A.STRIKES:
                continue
            rule.update(buy="call", expiry=e, strike=s, exit=r.get("exit") if r.get("exit") in A.EXITS else "hold10")
        out.append(rule)
    return out[:8]


def rule_matches(rule, f):
    for c in rule["when"]:
        v = f.get(LABEL_TO_KEY[c["col"]])
        if v is None or v == "":
            return False
        if c["col"] != "price":
            v = float(v)
        if not OPS[c["op"]](v, c["value"]):
            return False
    return True


def rule_return(rule, cand):
    if rule["buy"] == "stock":
        return cand["shares"]
    return A.trade_return(cand, "call", rule["expiry"], rule["strike"], rule["exit"])


def boot_ci(pairs, reps=1000, seed=5):
    """95% range of the average return, resampling whole WEEKS rather than single trades.

    Stocks in the same week move together (a market-wide jump lifts many at once), so treating
    every trade as independent makes the range look narrower than it really is. pairs is a list
    of (week, return)."""
    if len(pairs) < 5:
        return None, None
    by_week = {}
    for w, r in pairs:
        by_week.setdefault(w, []).append(r)
    weeks = list(by_week.values())
    if len(weeks) < 3:
        return None, None
    rng = random.Random(seed)
    sims = []
    for _ in range(reps):
        pick = [rng.choice(weeks) for _ in weeks]
        total = sum(len(w) for w in pick)
        sims.append(sum(sum(w) for w in pick) / total)
    sims.sort()
    return round(sims[int(0.025 * reps)], 2), round(sims[int(0.975 * reps) - 1], 2)


def score_rule(rule, cands):
    rets, base, by_b, base_b, months = [], [], {}, {}, sorted({c["month"] for c in cands})
    half = months[len(months) // 2] if months else ""
    h1, h2, pairs = [], [], []
    for c in cands:
        r = rule_return(rule, c)
        if r is None:
            continue
        base.append(r)
        base_b.setdefault(c["bundle"], []).append(r)
        if rule_matches(rule, c["f"]):
            rets.append(r)
            pairs.append((c["week"], r))
            by_b.setdefault(c["bundle"], []).append(r)
            (h1 if c["month"] < half else h2).append(r)
    lo, hi = boot_ci(pairs)
    beat = [b for b, v in by_b.items() if len(v) >= 3]
    return {"trades": len(rets),
            "mean_ret": round(statistics.mean(rets), 2) if rets else None,
            "median_ret": round(statistics.median(rets), 2) if rets else None,
            "win_rate": round(100 * sum(r > 0 for r in rets) / len(rets), 1) if rets else None,
            "ci_low": lo, "ci_high": hi,
            "baseline_mean": round(statistics.mean(base), 2) if base else None,
            "bundles_beat": sum(1 for b in beat if statistics.mean(by_b[b]) > statistics.mean(base_b[b])),
            "bundles_total": len(beat),
            "half1_mean": round(statistics.mean(h1), 2) if h1 else None,
            "half2_mean": round(statistics.mean(h2), 2) if h2 else None}


def describe_rule(rule):
    def val(v):
        return v if isinstance(v, str) else f"{v:g}"
    cond = " and ".join(f"{c['col']} {c['op']} {val(c['value'])}" for c in rule["when"])
    what = "buy the stock" if rule["buy"] == "stock" else \
        f"buy the {rule['expiry']}-day call {rule['strike']:g}% above the price, exit {rule['exit']}"
    return f"when {cond}: {what}"


def scorebook_line(rule, s):
    if not s["trades"]:
        return f"- {rule['name']} ({describe_rule(rule)}): matched no tradable training candidates."
    rng = (f" (95% range {s['ci_low']:+.1f}% to {s['ci_high']:+.1f}%, resampling whole weeks)"
           if s["ci_low"] is not None else " (too few trades or weeks for a range)")
    halves = f"; first half of the months {s['half1_mean']:+.1f}%, second half {s['half2_mean']:+.1f}%" \
        if s["half1_mean"] is not None and s["half2_mean"] is not None else ""
    return (f"- {rule['name']} ({describe_rule(rule)}): {s['trades']} trades, average {s['mean_ret']:+.1f}%{rng}, "
            f"median {s['median_ret']:+.1f}%, {s['win_rate']:.0f}% winners. Buying every candidate the same way: "
            f"{s['baseline_mean']:+.1f}%. Beat that in {s['bundles_beat']} of {s['bundles_total']} bundles{halves}.")


# ---------------------------------------------------------------- the model, with a shared budget
class Pot:
    def __init__(self, max_usd, spent_before):
        self.max_usd, self.spent_before, self.members = max_usd, spent_before, []
        self.lock = threading.Lock()

    def total(self):
        return self.spent_before + sum(m.cost for m in self.members)

    def llm(self, model):
        m = A.LLM(model, self.max_usd, 0.0)

        def check():
            if self.total() >= self.max_usd:
                raise A.Budget(f"spending cap of ${self.max_usd:.2f} reached")
        m.check_budget = check
        with self.lock:
            self.members.append(m)
        return m


class TimeUp(Exception):
    pass


# ---------------------------------------------------------------- prompts
COLUMN_LIST = ", ".join(f'"{label}"' for _, label, _ in A.FEATURES)


def system_text(phase):
    feedback = ("Results of each trade are shown to you two weeks (10 trading sessions) after you make it."
                if phase == "train" else
                "This is a blind scoring run: you will NOT see any results. Rely on your notes.")
    defs = "\n".join(f"- {label}: {meaning}" for _, label, meaning in A.FEATURES)
    call = """one CALL option: expiry 14, 30 or 90 days; strike at the money (0) or 5, 10, 15, 20 percent above the
  price; exit "hold10" (sell after 10 sessions) or "double_or_10" (sell as soon as it is worth 2x,
  otherwise after 10 sessions). Calls marked "n/a" did not trade that day and cannot be bought."""
    if CFG["options_only"]:
        instruments = (f"Then you may buy up to {MAX_PICKS} of them. This committee trades OPTIONS ONLY: each pick is\n"
                       + call)
        example = ('{"id": "C3", "buy": "call", "expiry": 30, "strike": 5, "exit": "double_or_10"}, '
                   '{"id": "C7", "buy": "call", "expiry": 90, "strike": 0, "exit": "hold10"}')
    else:
        instruments = (f"Then you may buy up to {MAX_PICKS} of them. For each, either:\n"
                       f"- the STOCK (sold 10 trading sessions later), or\n- {call}")
        example = '{"id": "C3", "buy": "stock"}, {"id": "C7", "buy": "call", "expiry": 90, "strike": 0, "exit": "hold10"}'
    if phase == "train":
        explore = """TRAINING IS FOR LEARNING. Work like a strategist: hold a clear working strategy (the exact setup you
trade and why), trade it, and change it when the results say so. You must make at least one trade every
week: a week without a trade is a week without evidence, and your real score is the later blind run, where
you may pass whenever the odds look poor. Be inventive: besides the strategy in your notes, test at least
one idea of your own in every bundle (an unusual combination of columns, a different expiry or strike, a
contrarian take). Original ideas that the code later confirms are the most valuable thing you can pass on."""
    else:
        explore = "Follow the strategy in your notes. Trade when you believe the odds favor you and pass when they don't."
    return f"""You are one of four independent traders on a research committee, looking for a real, repeatable edge
in US stocks with unusual options activity (some very volatile, some ordinary). Each week you see up to
{PER_WEEK} candidate stock-days.

For EVERY candidate, give a rating: +2 strong buy, +1 lean buy, 0 no view, -1 lean avoid, -2 strong avoid
(you expect it to fall). Ratings are scored too: we check whether your higher-rated stocks did better
over the next 10 trading sessions.

{instruments}
Every trade is ${A.TRADE_USD:,}.
YOUR GOAL: MAKE AS MUCH MONEY AS POSSIBLE. Your score is your total profit in dollars. A pass earns $0; a
trade earns its return on ${A.TRADE_USD:,} (+50% = +$500, -100% = -${A.TRADE_USD:,}). You buy at the next session's
price; a 5% cost applies to each side of an option trade and 0.1% to each side of a stock trade.
{feedback}
{explore}

Stocks are anonymous codes and time is shown only as week numbers, on purpose: judge only from the
numbers. Columns:
{defs}
- option grid: the cost of each call as a percent of the stock price, and how many trading sessions
  until that expiration ("14d", "30d", "90d" are the nearest listed expirations, which can be shorter)

ANSWERS TO QUESTIONS EARLIER TRADERS RAISED:
- The -100% results on stocks that rose: those calls expired during the 10-session hold. An option that
  expires at or before session 10 is settled at its exercise value (zero if the stock is below the strike),
  even if it was worth a lot a few days earlier. The grid now shows sessions until expiration; check it.
- Trading costs ARE included everywhere, including the scorebook: each side of an option trade costs 5%
  or $0.05 a share, whichever is larger (much more than 5% on cheap options).
- Implied volatility is now provided (columns "iv %", "realized vol %", "iv/realized"), and each trade
  result shows what the option cost, its implied volatility, its expiry and the stock's own move.
- At each bundle review you now get the full-bundle tables: every column split into fifths, with how the
  stocks did, and how calls did by implied volatility.
- Puts and short selling are not available in this test. Data is daily closing data only.

Think it through silently, then reply with ONE compact JSON object and nothing else:
{{"ratings": {{"C1": 1, "C2": -2, "C3": 0}}, "picks": [{example}], "why": "under 25 words"}}
Rate every candidate.""" + ("" if phase == "train" else ' Use "picks": [] to buy nothing this week.')


def rules_prompt():
    extra = ("\nThis committee trades options only: every rule must buy a call (expiry, strike, exit)."
             if CFG["options_only"] else "")
    return RULES_PROMPT + extra


RULES_PROMPT = f"""Now turn your strongest ideas into testable rules. Code will test each rule on every training
candidate in all bundles, including stocks you never saw, and report the real numbers to the editor and
the next generation. A rule that only fit what you saw will be exposed, so state what you actually believe.

Reply with JSON only:
{{"rules": [{{"name": "short name", "when": [{{"col": "calls", "op": ">", "value": 3}}, {{"col": "vs ma20 %", "op": ">", "value": 0}}], "buy": "stock"}},
           {{"name": "short name", "when": [{{"col": "rsi", "op": "<", "value": 35}}], "buy": "call", "expiry": 90, "strike": 0, "exit": "hold10"}}]}}
Columns (exact names): {COLUMN_LIST}. Operators: >, >=, <, <=. The "price" column uses "=" with "<$10",
"$10-50" or ">$50". Up to 8 rules, each with 1 to 4 conditions. Rules can also say what to AVOID: describe
the bad setup and buy the stock, and the scorebook will show it losing."""


def parse_ratings(text, ids):
    out = {}
    data = A.parse_json(text)
    src = data.get("ratings") if isinstance(data, dict) and isinstance(data.get("ratings"), dict) else None
    pairs = src.items() if src else re.findall(r'"(C\d+)"\s*:\s*(-?\d)', text or "")
    for k, v in pairs:
        try:
            v = int(v)
        except (TypeError, ValueError):
            continue
        if k in ids and -2 <= v <= 2:
            out[k] = v
    return out


def rating_stats(ratings):
    """ratings: list of (rating, shares return, week). Rank correlation with a 95% range that
    resamples whole weeks."""
    pts_w = [(w, r, x) for r, x, w in ratings if x is not None]
    pts = [(r, x) for _, r, x in pts_w]
    if len(pts) < 20 or len({r for r, _ in pts}) < 2:
        return {}

    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0] * len(v)
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                rk[order[k]] = (i + j) / 2
            i = j + 1
        return rk

    def spearman(p):
        a, b = ranks([r for r, _ in p]), ranks([x for _, x in p])
        ma, mb = statistics.mean(a), statistics.mean(b)
        num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
        return num / den if den else 0.0

    rng = random.Random(9)
    by_week = {}
    for p_ in pts_w:
        by_week.setdefault(p_[0], []).append(p_[1:])
    weeks = list(by_week.values())
    sims = sorted(spearman([x for w in (rng.choice(weeks) for _ in weeks) for x in w]) for _ in range(300))
    top = [x for r, x in pts if r >= 1]
    bottom = [x for r, x in pts if r <= -1]
    return {"rated": len(pts), "rating_corr": round(spearman(pts), 3),
            "rating_corr_lo": round(sims[7], 3), "rating_corr_hi": round(sims[292], 3),
            "top_rated_ret": round(statistics.mean(top), 2) if top else None,
            "bottom_rated_ret": round(statistics.mean(bottom), 2) if bottom else None}


# ---------------------------------------------------------------- one agent's walk
class Walk:
    """One agent's run through one or more bundles. Collects trades, ratings, and weekly notes."""

    def __init__(self, run_id, llm, phase, deadline):
        self.run_id, self.llm, self.phase, self.deadline = run_id, llm, phase, deadline
        self.trades, self.ratings, self.weeks, self.week_rows = [], [], [], []
        self.replies = self.bad = self.cut = self.errors = 0
        self.sample = ""

    def bundle(self, cands_by_week, notes, scorebook, label):
        rng = random.Random(f"{self.run_id}-{label}")
        tickers = sorted({c["ticker"] for wk in cands_by_week.values() for c in wk})
        code = {t: f"S{n}" for t, n in zip(tickers, rng.sample(range(100, 10000), len(tickers)))}
        system = system_text(self.phase)
        start = len(self.trades)
        weeks = sorted(cands_by_week)
        for n, wk in enumerate(weeks, 1):
            if time.monotonic() > self.deadline:
                raise TimeUp()
            cands = [dict(c, id=f"C{i + 1}", code=code[c["ticker"]])
                     for i, c in enumerate(sorted(cands_by_week[wk], key=lambda c: A.rank(self.run_id, c["ticker"])))]
            wi = len(self.weeks)
            self.weeks.append(cands)
            parts = [f"Your notes:\n{notes.strip() or '(none yet: you are in the first generation)'}"]
            if scorebook:
                parts.append("Scorebook (rules from the last generation, tested by code on all training data):\n" + scorebook)
            mine = self.trades[start:]
            if self.phase == "train":
                shown = [t for t in mine if t["week"] <= (dt.date.fromisoformat(wk) - dt.timedelta(days=REVEAL_DAYS)).isoformat()]
                if shown:
                    rr = [t["ret_pct"] for t in shown]
                    parts.append(f"Your profit in this bundle so far: ${sum(rr) * A.TRADE_USD / 100:+,.0f} on {len(rr)} trades, "
                                 f"{100 * sum(r > 0 for r in rr) / len(rr):.0f}% winners. Most recent results "
                                 f"(what you saw -> result):\n" + "\n".join(
                                     f"- {t['code']} {A.describe_pick(t)}: calls {A.fmt(t['f'].get('call_volume_spike'))}x, "
                                     f"shares {A.fmt(t['f'].get('stock_volume_spike'))}x, 5d {A.fmt(t['f'].get('ret_5d_pct'), '{:+.1f}')}%, "
                                     f"vs ma20 {A.fmt(t['f'].get('vs_ma20_pct'), '{:+.1f}')}%, rsi {A.fmt(t['f'].get('rsi14'), '{:.0f}')} "
                                     f"-> {t['ret_pct']:+.1f}%{trade_detail(t)}" for t in shown[-10:]))
            parts.append(f"{label}, week {n} of {len(weeks)}. Candidates:\n{A.candidate_table(cands)}")
            try:
                reply = self.llm.chat([{"role": "system", "content": system},
                                       {"role": "user", "content": "\n\n".join(parts)}], max_tokens=2500)
            except RuntimeError as ex:       # the model API kept failing for this week: count it as a pass
                self.errors += 1
                self.week_rows.append({"run_id": self.run_id, "week_index": wi, "picks": 0, "finish": "error",
                                       "readable": "no", "why": f"[{label}] (model error) {str(ex)[:300]}"})
                if self.errors >= 10 and self.errors > 0.3 * (self.replies + self.errors):
                    raise
                continue
            self.replies += 1
            self.cut += self.llm.last_finish == "length"
            picks, why, ok = A.parse_picks(reply)
            by_id = {c["id"]: c for c in cands}
            rated = parse_ratings(reply, set(by_id))
            if not ok:
                self.bad += 1
                self.sample = self.sample or (reply or "(empty reply)")[:600]
                if self.replies >= 6 and self.bad > 0.6 * self.replies:
                    raise RuntimeError(f"model replies unreadable ({self.bad}/{self.replies}): {self.sample[:200]!r}")
            for cid, v in rated.items():
                c = by_id[cid]
                self.ratings.append({"run_id": self.run_id, "ticker": c["ticker"], "signal_date": c["date"],
                                     "rating": v, "shares_ret10": c["shares"]})
            used = set()
            for p in picks[:MAX_PICKS]:
                if not isinstance(p, dict):
                    continue
                c = by_id.get(str(p.get("id", "")).strip())
                if not c or c["id"] in used:
                    continue
                if str(p.get("buy", "")).lower() == "stock":
                    if CFG["options_only"]:
                        continue
                    spec = {"action": "stock", "expiry": None, "strike_pct": None, "exit_rule": None}
                else:
                    try:
                        e, s = int(p.get("expiry")), float(p.get("strike"))
                    except (TypeError, ValueError):
                        continue
                    if e not in A.EXPIRIES or s not in A.STRIKES:
                        continue
                    spec = {"action": "call", "expiry": e, "strike_pct": s,
                            "exit_rule": p.get("exit") if p.get("exit") in A.EXITS else "hold10"}
                r = A.trade_return(c, spec["action"], spec["expiry"], spec["strike_pct"], spec["exit_rule"])
                if r is None:
                    continue
                used.add(c["id"])
                cell = c["o"].get(f"{spec['expiry']}d+{spec['strike_pct']:g}") if spec["action"] == "call" else None
                self.trades.append(dict(spec, run_id=self.run_id, week_index=wi, week=wk, cand_id=c["id"],
                                        code=c["code"], ticker=c["ticker"], signal_date=c["date"],
                                        ret_pct=round(r, 2), f=c["f"], reason=why[:300], bundle=c["bundle"],
                                        stock_ret=c["shares"], opt=cell or {}))
            self.week_rows.append({"run_id": self.run_id, "week_index": wi, "picks": len(used),
                                   "finish": self.llm.last_finish, "readable": "yes" if ok else "no",
                                   "why": (f"[{label}] " + (why if ok else "(unreadable) " + (reply or "")))[:500]})
        return self.trades[start:]

    def summary(self, generation, agent):
        rets = [t["ret_pct"] for t in self.trades]
        bm, bmed, bw = A.random_baseline(self.weeks, self.trades) if self.trades else (None, None, None)
        s = {"run_id": self.run_id, "lineage": CFG["lineage"], "generation": generation, "phase": self.phase,
             "agent": agent, "model": self.llm.model, "weeks": len(self.weeks), "trades": len(rets),
             "mean_ret": round(statistics.mean(rets), 2) if rets else None,
             "median_ret": round(statistics.median(rets), 2) if rets else None,
             "win_rate": round(100 * sum(r > 0 for r in rets) / len(rets), 1) if rets else None,
             "baseline_mean": bm, "baseline_median": bmed, "baseline_win": bw,
             "profit_usd": round(sum(rets) * A.TRADE_USD / 100, 2),
             "baseline_profit_usd": round(bm * len(rets) * A.TRADE_USD / 100, 2) if bm is not None else None,
             "replies": self.replies, "bad_replies": self.bad, "cut_off": self.cut, "sample_reply": self.sample,
             "prompt_tokens": self.llm.prompt_tokens, "completion_tokens": self.llm.completion_tokens,
             "cost_usd": round(self.llm.cost, 4), "status": "complete",
             "finished": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        s.update(rating_stats([(r["rating"], r["shares_ret10"], A.week_of(str(r["signal_date"])))
                               for r in self.ratings]))
        return s


def feature_line(f):
    return ", ".join(f"{label} {A.fmt(f.get(k), '{:.1f}') if k != 'price_band' else f.get(k)}" for k, label, _ in A.FEATURES)


def trade_detail(t):
    """What the option cost and assumed, and what the stock itself did, for one trade."""
    o, bits = t.get("opt") or {}, []
    if o.get("cost_pct"):
        bits.append(f"paid {o['cost_pct']:.1f}% of the price")
    if o.get("iv"):
        bits.append(f"iv {o['iv']:.0f}%")
    if o.get("sessions") is not None:
        s = o["sessions"]
        bits.append(f"expired at session {s}, settled at exercise value" if s <= 10 else f"{s} sessions to expiry")
    if t.get("stock_ret") is not None:
        bits.append(f"stock {t['stock_ret']:+.1f}%")
    return f" ({'; '.join(bits)})" if bits else ""


def bundle_tables(cands):
    """The full-bundle view earlier traders asked for, computed by code: for each column, how the
    stocks in each fifth did over the next 10 sessions; and how 30-day at-the-money calls did by
    implied volatility and by implied/realized ratio."""
    if len(cands) < 50:
        return []
    out = [f"All {len(cands)} candidates in this bundle, split into fifths by each column (lowest to highest). "
           "Each cell: the column's range, then the stock's median 10-session return and % of stocks that rose:"]
    for key, label, _ in A.FEATURES:
        if key == "price_band":
            continue
        vals = [(float(c["f"][key]), c["shares"]) for c in cands if c["f"].get(key) not in (None, "")]
        if len(vals) < 50 or len({v for v, _ in vals}) < 5:
            continue
        vals.sort()
        cells = []
        for q in range(5):
            part = vals[q * len(vals) // 5:(q + 1) * len(vals) // 5]
            r = [x for _, x in part]
            cells.append(f"{part[0][0]:.4g} to {part[-1][0]:.4g}: {statistics.median(r):+.1f}%, {100 * sum(x > 0 for x in r) / len(r):.0f}% up")
        out.append(f"- {label}: " + " | ".join(cells))
    for key, label in (("iv30_atm", "implied volatility"), ("iv_rv", "implied/realized ratio")):
        pts = [(float(c["f"][key]), c["o"]["30d+0"]["hold10"]) for c in cands
               if c["f"].get(key) not in (None, "") and (c["o"].get("30d+0") or {}).get("hold10") is not None]
        if len(pts) < 50:
            continue
        pts.sort()
        cells = []
        for q in range(5):
            part = pts[q * len(pts) // 5:(q + 1) * len(pts) // 5]
            r = [x for _, x in part]
            cells.append(f"{part[0][0]:.3g} to {part[-1][0]:.3g}: avg {statistics.mean(r):+.0f}%, median {statistics.median(r):+.0f}%")
        out.append(f"30-day at-the-money call, held 10 sessions, by {label}: " + " | ".join(cells))
    return out


def bundle_review(trades, ratings, cands=()):
    rets = [t["ret_pct"] for t in trades]
    lines = []
    if rets:
        groups = {}
        for t in trades:
            groups.setdefault(A.describe_pick(t), []).append(t["ret_pct"])
        lines.append(f"Profit: ${sum(rets) * A.TRADE_USD / 100:+,.0f} on {len(rets)} trades, average {statistics.mean(rets):+.1f}%, "
                     f"median {statistics.median(rets):+.1f}%, {100 * sum(r > 0 for r in rets) / len(rets):.0f}% winners.")
        lines += [f"- {k}: {len(v)} trades, average {statistics.mean(v):+.1f}%, median {statistics.median(v):+.1f}%"
                  for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))]
    else:
        lines.append("You made no trades in this bundle.")
    by_r = {}
    for r in ratings:
        by_r.setdefault(r["rating"], []).append(r["shares_ret10"])
    if by_r:
        lines.append("How the stock did after each of your ratings (10 sessions, every candidate you rated):")
        lines += [f"- rated {k:+d}: {len(v)} stocks, average {statistics.mean(v):+.1f}%, median {statistics.median(v):+.1f}%"
                  for k, v in sorted(by_r.items(), reverse=True)]
    sample = sorted(trades, key=lambda t: t["ret_pct"])
    sample = sample[:10] + sample[-10:] if len(sample) > 20 else sample
    if sample:
        lines.append("Your worst and best trades (what you saw -> result):")
        for t in sample:
            f = t["f"]
            lines.append(f"- {A.describe_pick(t)}: {feature_line(f)} -> {t['ret_pct']:+.1f}%{trade_detail(t)}")
    # What the whole bundle looked like, traded or not: the biggest winners and losers among every
    # candidate shown, with the numbers seen beforehand and the rating given. This is the richest
    # evidence for finding a pattern, especially for a trader who made few trades.
    rated = {(r["ticker"], r["signal_date"]): r["rating"] for r in ratings}
    shown = sorted(cands, key=lambda c: c["shares"])
    if shown:
        base = [c["shares"] for c in shown]
        lines.append(f"All {len(shown)} candidates in this bundle: the stock averaged {statistics.mean(base):+.1f}% "
                     f"over the next 10 sessions (median {statistics.median(base):+.1f}%). The biggest losers and "
                     f"winners (what was visible beforehand, your rating -> stock return):")
        pick = shown[:12] + shown[-12:] if len(shown) > 24 else shown
        for c in pick:
            r = rated.get((c["ticker"], c["date"]))
            lines.append(f"- {feature_line(c['f'])}; you rated {'not rated' if r is None else f'{r:+d}'} "
                         f"-> stock {c['shares']:+.1f}%")
    lines += bundle_tables(list(cands))
    return "\n".join(lines)


def agent_train(gen, agent, llm, notes, scorebook, pool, order, fraction, deadline):
    run_id = f"committee-g{gen}-agent{agent}-train-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}"
    walk = Walk(run_id, llm, "train", deadline)
    working = notes
    for k, b in enumerate(order, 1):
        cands = [c for c in pool if c["bundle"] == b and c["split"] == "train"]
        weeks = sorted({c["week"] for c in cands})
        keep = set(random.Random(f"weeks-g{gen}-b{b}").sample(weeks, max(1, round(len(weeks) * fraction))))
        by_week = {}
        for c in cands:
            if c["week"] in keep:
                by_week.setdefault(c["week"], []).append(c)
        label = f"Bundle {k} of {len(order)}"
        before = len(walk.ratings)
        trades = walk.bundle(by_week, working, scorebook, label)
        review = bundle_review(trades, walk.ratings[before:], [c for wk in by_week.values() for c in wk])
        last = k == len(order)
        prompt = f"""You finished {label.lower()} (a fresh group of stocks you had not seen). Here is how you did.

{review}

Your working notes going into this bundle:
{working.strip() or '(none)'}

Rewrite your working notes{' as your final notes for the committee editor' if last else ' before the next bundle (new stocks)'}.
Your notes are your trading playbook, not a report. Structure them as:
1. MY CURRENT STRATEGY: the exact setup you trade (columns and thresholds, instrument, expiry, strike, exit)
   and the reasoning behind it.
2. WHAT I TESTED IN THIS BUNDLE and how it went, including the new idea you tried.
3. WHAT I WILL TRY NEXT: the change or new idea you will test on the next stocks.
4. Supporting evidence and ideas I have dropped (briefly).
Keep what held up, fix or drop what didn't, add what you learned. Write rules in terms of the columns
(thresholds, combinations, instrument, expiry, strike, exit), with the evidence behind each (how many trades,
returns, in how many bundles it held) and how confident you are. Be honest about small samples and about
ideas that worked in one bundle and failed in another. Put your rules and conclusions first and the supporting
detail after. Rewrite the notes as one up-to-date document (merge what each bundle taught you into the rules)
rather than appending a log per bundle, so they stay readable. The system already records every trade,
rating and result for you, so spend your words on what predicts returns, not on record-keeping.
No stock codes. No length limit: be as thorough as is useful, organized under headings. Reply with the notes only.

What the columns mean:
""" + "\n".join(f"- {label}: {meaning}" for _, label, meaning in A.FEATURES)
        working = llm.chat([{"role": "user", "content": prompt}], max_tokens=24000)
        if llm.last_finish == "length":
            working += "\n\n(The notes were cut off here by the reply limit.)"
    reply = llm.chat([{"role": "user", "content": f"Your final notes:\n{working}\n\n{rules_prompt()}"}], max_tokens=3000)
    data = A.parse_json(reply)
    rules = clean_rules(data.get("rules") if isinstance(data, dict) else None)
    return walk, working, rules


def blind_run(gen, llm_for, notes, scorebook, pool, bundles, split, phase, deadline, label):
    """One agent trades the given split with no feedback; one thread per bundle."""
    run_id = f"committee-g{gen}-{label}-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}"

    def one(b):
        w = Walk(f"{run_id}-b{b}", llm_for(), phase, deadline)
        by_week = {}
        for c in pool:
            if c["bundle"] == b and c["split"] in split:
                by_week.setdefault(c["week"], []).append(c)
        w.bundle(by_week, notes, scorebook, f"Bundle {b}")
        return w
    with cf.ThreadPoolExecutor(len(bundles)) as ex:
        walks = list(ex.map(one, bundles))
    merged = Walk(run_id, walks[0].llm, phase, deadline)
    for w in walks:
        offset = len(merged.weeks)
        merged.weeks += w.weeks
        merged.trades += [dict(t, run_id=run_id, week_index=t["week_index"] + offset) for t in w.trades]
        merged.ratings += [dict(r, run_id=run_id) for r in w.ratings]
        merged.week_rows += [dict(r, run_id=run_id, week_index=r["week_index"] + offset) for r in w.week_rows]
        merged.replies += w.replies
        merged.bad += w.bad
        merged.cut += w.cut
        merged.sample = merged.sample or w.sample
    merged.llm = type("Sum", (), {"model": walks[0].llm.model,
                                  "prompt_tokens": sum(w.llm.prompt_tokens for w in walks),
                                  "completion_tokens": sum(w.llm.completion_tokens for w in walks),
                                  "cost": sum(w.llm.cost for w in walks)})()
    return merged


# ---------------------------------------------------------------- one generation
def redesign(llm, gen, agent_outputs, ed_notes):
    """Ask the editor, with every trader's notes in view, how it would remake the test itself."""
    parts = [f"=== Agent {a}'s final notes ===\n{notes.strip()}" for a, (notes, _) in sorted(agent_outputs.items())]
    parts.append(f"=== Your playbook for the next generation ===\n{ed_notes.strip()}")
    prompt = "\n\n".join(parts) + """

Step outside the game. You and these traders have been working inside a test built by humans: anonymous
stocks, hidden dates, weekly batches of about 10 candidates, calls only (14, 30 or 90 days; at the money to
20% above), a fixed 10-session hold, daily data, the columns you were given, and a code scorebook.

The humans will run a few more generations with whatever changes you recommend. Write a redesign proposal:
1. WHAT BLOCKED YOU: the specific limits of this test that most stopped the traders from finding or
   proving an edge. Quote the traders' own complaints where they apply.
2. DATA TO ADD: columns or information you need, and exactly what each would let you test.
3. TOOLS AND INSTRUMENTS: trade types, exits, holding periods, or analysis tools you need.
4. CHANGES TO THE TEST ITSELF: how candidates are chosen, how much is shown, how results are fed back,
   how rules are scored.
5. THE FIRST THREE EXPERIMENTS you would run in the redesigned test, each stated as a testable rule.
Rank items by how much they would help. Be concrete and brief; say what is realistic from daily US stock
and options data. Plain prose and lists."""
    return llm.chat([{"role": "user", "content": prompt}], max_tokens=4000) or ""


def editor(llm, gen, prev_notes, agent_outputs, book_lines):
    parts = [f"Notes the committee started this generation with:\n{prev_notes.strip() or '(none: first generation)'}"]
    for a, (notes, rules) in sorted(agent_outputs.items()):
        parts.append(f"=== Agent {a}'s final notes ===\n{notes.strip()}\n\nAgent {a}'s rules, as tested by code on ALL "
                     f"training candidates in all six bundles:\n" + ("\n".join(book_lines[a]) or "(no testable rules)"))
    prompt = "\n\n".join(parts) + """

You are the committee editor. Four traders worked independently on the same stocks and weeks, each
developing its own strategy. Write the playbook the next generation will start from; it will see ONLY your notes and the code-tested scorebook of
the rules you state next, never these traders' notes or trades.
Weigh the evidence: trust rules the code confirmed across many trades and most bundles, and treat ideas
that only one trader saw, or that the code did not confirm, as weak. Say where the traders agreed and
where they disagreed. Keep useful ideas that still need testing, clearly marked as untested. No stock
codes. No length limit: be as thorough as is useful, organized under headings. Reply with the notes only.

How to organize them: start with the STRATEGY to trade (the setups worth trading, with their scorebook
numbers), then what to AVOID, then at least two promising NEW IDEAS for the next traders to test (give credit
to original ideas the code confirmed, and keep creative ones that are untested), then open questions. Spend your words on trading
ideas and evidence, not on bookkeeping. Things that are expected and need no comment: each trader's
trades and rating counts differ (they chose and rated independently), traders' notes are summaries
rather than full logs, and the scorebook's numbers supersede any figure a trader quoted.

What the columns mean:
""" + "\n".join(f"- {label}: {meaning}" for _, label, meaning in A.FEATURES)
    notes = llm.chat([{"role": "user", "content": prompt}], max_tokens=24000)
    if llm.last_finish == "length":
        notes += "\n\n(The notes were cut off here by the reply limit.)"
    reply = llm.chat([{"role": "user", "content": f"Your notes:\n{notes}\n\n{rules_prompt()}"}], max_tokens=3000)
    data = A.parse_json(reply)
    return notes, clean_rules(data.get("rules") if isinstance(data, dict) else None)


STAT_KEYS = ("trades", "mean_ret", "median_ret", "win_rate", "ci_low", "ci_high", "baseline_mean",
             "bundles_beat", "bundles_total", "half1_mean", "half2_mean")


def stats_of(row):
    out = {k: (C.to_float(row[k]) if row[k] not in (None, "") else None) for k in STAT_KEYS}
    for k in ("trades", "bundles_beat", "bundles_total"):
        out[k] = int(out[k] or 0)
    return out


def book_text(st, g):
    """The editor's rules for generation g with their TRAINING numbers only (what may be passed on)."""
    book = [r for r in st.backend.read("scorebook")
            if r["lineage"] == CFG["lineage"] and int(r["generation"]) == g and r["author"] == "editor"
            and r["period"] == "train"]
    return "\n".join(scorebook_line(json.loads(r["rule"]), stats_of(r)) for r in book)


def inherited(st):
    rows = [r for r in st.backend.read("committee_notes") if r["author"] == "editor" and r["lineage"] == CFG["lineage"]]
    if not rows:
        return 0, (SEED_NOTES if CFG["seed"] == "briefing" else ""), ""
    last = max(rows, key=lambda r: int(r["generation"]))
    g = int(last["generation"])
    return g, last["text"], book_text(st, g)


def book_rows(gen, author, period, rules, cands):
    rows, lines = [], []
    for r in rules:
        s = score_rule(r, cands)
        if s["trades"]:
            s["trades"] = int(s["trades"])
        rows.append(dict(s, lineage=CFG["lineage"], generation=gen, author=author, rule_name=r["name"], period=period, rule=json.dumps(r)))
        lines.append(scorebook_line(r, s))
    # Several rules can share a name; keep them apart in the table.
    seen = {}
    for row in rows:
        n = seen[row["rule_name"]] = seen.get(row["rule_name"], 0) + 1
        if n > 1:
            row["rule_name"] = f"{row['rule_name']} ({n})"
    return rows, lines


def run_generation(st, args, pool, deadline, pot):
    gen_before, notes, scorebook = inherited(st)
    gen = gen_before + 1
    order = list(TRAIN_BUNDLES)
    random.Random(f"order-g{gen}").shuffle(order)
    print(f"Generation {gen}: bundle order {order}, {N_AGENTS} agents, {args.weeks_fraction:.0%} of training weeks.")
    with cf.ThreadPoolExecutor(N_AGENTS) as ex:
        futs = {a: ex.submit(agent_train, gen, a, pot.llm(args.model), notes, scorebook, pool, order,
                             args.weeks_fraction, deadline) for a in range(1, N_AGENTS + 1)}
        results = {a: f.result() for a, f in futs.items()}
    train_cands = [c for c in pool if c["split"] == "train" and c["bundle"] in TRAIN_BUNDLES]
    score_cands = [c for c in pool if c["split"] == "score" and c["bundle"] in TRAIN_BUNDLES]
    agent_out, lines, book = {}, {}, []
    for a, (walk, working, rules) in results.items():
        rows, ls = book_rows(gen, f"agent{a}", "train", rules, train_cands)
        book += rows
        lines[a] = ls
        agent_out[a] = (working, rules)
        print(f"  agent {a}: {len(walk.trades)} trades, ${sum(t['ret_pct'] for t in walk.trades) * 10:+,.0f}, "
              f"{len(rules)} rules, {walk.bad}/{walk.replies} unreadable")
    ed = pot.llm(getattr(args, "editor_model", None) or args.model)   # the editor's judgment matters most
    ed_notes, ed_rules = editor(ed, gen, notes, agent_out, lines)
    try:
        proposal = redesign(ed, gen, agent_out, ed_notes)
    except Exception as ex:   # noqa: BLE001 - a nice-to-have; never lose a generation over it
        proposal = f"(redesign proposal failed: {type(ex).__name__}: {str(ex)[:200]})"
    rows, ed_lines = book_rows(gen, "editor", "train", ed_rules, train_cands)
    book += rows
    srows, s_lines = book_rows(gen, "editor", "score", ed_rules, score_cands)
    book += srows
    scoring = blind_run(gen, lambda: pot.llm(args.model), ed_notes, "\n".join(ed_lines), pool,
                        TRAIN_BUNDLES, ("score",), "score", deadline, "scoring")
    # Everything finished: write the generation in one go, on a fresh connection (the one opened at
    # the start may have been dropped while the agents worked; Neon closes idle connections).
    C._STORE = None
    st = C.db()
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    runs, trades, ratings, weeks = [], [], [], []
    for a, (walk, working, rules) in results.items():
        runs.append(dict(walk.summary(gen, f"agent{a}"), started=now))
        trades += walk.trades
        ratings += walk.ratings
        weeks += walk.week_rows
    sc = scoring.summary(gen, "scorer")
    sc["cost_usd"] = round(scoring.llm.cost + ed.cost, 4)   # the editor's calls are billed with the scoring run
    runs.append(dict(sc, started=now))
    trades += scoring.trades
    ratings += scoring.ratings
    weeks += scoring.week_rows
    keep = ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action", "expiry", "strike_pct",
            "exit_rule", "ret_pct", "reason")
    st.backend.upsert("agent_runs", runs)
    st.backend.upsert("agent_trades", [{k: t.get(k) for k in keep} for t in trades])
    st.backend.upsert("agent_ratings", ratings)
    st.backend.upsert("agent_weeks", weeks)
    st.backend.upsert("scorebook", book)
    notes_rows = [{"lineage": CFG["lineage"], "generation": gen, "author": f"agent{a}", "model": args.model, "text": w, "rules": json.dumps(r),
                   "created": now} for a, (w, r) in agent_out.items()]
    notes_rows.append({"lineage": CFG["lineage"], "generation": gen, "author": "editor",
                       "model": getattr(args, "editor_model", None) or args.model, "text": ed_notes,
                       "rules": json.dumps(ed_rules), "created": now})
    notes_rows.append({"lineage": CFG["lineage"], "generation": gen, "author": "redesign",
                       "model": getattr(args, "editor_model", None) or args.model, "text": proposal,
                       "rules": "[]", "created": now})
    st.backend.upsert("committee_notes", notes_rows)
    print(f"Generation {gen} done: scoring run {sc['trades']} trades, profit ${sc['profit_usd']:+,.0f} "
          f"(random ${sc['baseline_profit_usd'] or 0:+,.0f}), rating correlation {sc.get('rating_corr')} "
          f"({sc.get('rating_corr_lo')} to {sc.get('rating_corr_hi')}); generation cost ${pot.total() - pot.spent_before:.2f}")
    print("Editor rules on the blind scoring months:\n" + ("\n".join(s_lines) or "(none)"))
    return gen


def spent(st):
    return sum(C.to_float(r["cost_usd"]) or 0 for r in st.backend.read("agent_runs"))


def loop(args):
    st = C.db()
    pool = load_pool(st)
    if not pool:
        sys.exit("The candidate pool is empty: run `python committee.py build-pool --archive ...` first.")
    deadline = time.monotonic() + 60 * args.max_minutes
    started, done, stop = time.monotonic(), 0, None
    for _ in range(args.generations):
        per_gen = (time.monotonic() - started) / done if done else 60 * 35
        if time.monotonic() + 1.3 * per_gen > deadline:
            print("Not enough time left for another generation in this round; stopping cleanly.")
            break
        pot = None
        try:
            # Fresh connection for every generation; a database hiccup here gets a few retries.
            for attempt in range(4):
                try:
                    C._STORE = None
                    st = C.db()
                    pot = Pot(args.max_usd, spent(st))
                    break
                except Exception as ex:   # noqa: BLE001
                    if attempt == 3:
                        raise
                    print(f"Database connection failed ({type(ex).__name__}: {ex}); retrying in 30 seconds.")
                    time.sleep(30)
            run_generation(st, args, pool, deadline, pot)
            done += 1
            continue
        except A.Budget as b:
            stop = f"spending cap: {b}"
        except TimeUp:
            print("Ran out of time mid-generation; it will be redone from the start next round.")
        except Exception as ex:   # noqa: BLE001 - record any crash where the report can show it
            stop = f"error: {type(ex).__name__}: {ex}"
            tb = traceback.format_exc()
            print(tb)
            with open(os.path.join(C.ROOT, "committee_error.txt"), "w") as f:
                f.write(f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC\n{tb[-3000:]}")
            save_crash(stop)
        # The generation did not finish: still count what it spent, so the cap stays honest.
        cost = pot.total() - pot.spent_before if pot else 0
        if cost > 0 and _safe_db():
            C.db().backend.upsert("agent_runs", [{
                "run_id": f"committee-unfinished-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}",
                "lineage": CFG["lineage"], "generation": inherited(C.db())[0] + 1, "phase": "unfinished",
                "agent": "all", "model": args.model, "cost_usd": round(cost, 4), "status": stop or "time limit",
                "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}])
        break
    remaining = 0 if stop else max(0, args.generations - done)
    if done == 0 and remaining and not stop:
        # A generation that can't finish in one round would repeat forever.
        print("No generation finished this round, so not scheduling another.")
        remaining = 0
    with open(os.path.join(C.ROOT, "committee_status.txt"), "w") as f:
        f.write(str(remaining))
    print(f"This round: {done} generation(s). Remaining: {remaining}" + (f" ({stop})" if stop else ""))
    try:
        report(args)
    except Exception as ex:   # noqa: BLE001
        save_crash(f"report failed: {type(ex).__name__}: {ex}")


def _safe_db():
    try:
        C._STORE = None
        C.db()
        return True
    except Exception:   # noqa: BLE001
        return False


def save_crash(stop):
    """Write any crash to a file the workflow commits (logs aren't readable from outside)."""
    if not stop:
        return
    tb = traceback.format_exc()
    name = f"COMMITTEE-{CFG['lineage']}-ERROR.md"
    with open(os.path.join(C.ROOT, name), "w") as f:
        f.write(f"# Last crash ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)\n\n{stop}\n\n```\n{tb[-4000:]}\n```\n")


def final_test(args):
    """The one-time exam: the chosen generation's editor notes on held-back stocks and the test months."""
    st = C.db()
    pool = load_pool(st)
    rows = [r for r in st.backend.read("committee_notes")
            if r["author"] == "editor" and r["lineage"] == CFG["lineage"] and int(r["generation"]) == args.generation]
    if not rows:
        sys.exit(f"No editor notes for generation {args.generation}.")
    if any(r.get("phase") == "test" and r.get("lineage") == CFG["lineage"] and r["generation"] == str(args.generation)
           for r in st.backend.read("agent_runs")):
        print("Note: this generation already took the exam; a repeat is no longer a clean test.")
    rules = clean_rules(json.loads(rows[0]["rules"] or "[]"))
    book = book_text(st, args.generation)
    pot = Pot(args.max_usd, spent(st))
    deadline = time.monotonic() + 60 * args.max_minutes
    exam = [c for c in pool if c["split"] in ("test", "holdout")]
    w = blind_run(args.generation, lambda: pot.llm(args.model), rows[0]["text"], book, exam,
                  tuple(range(1, N_BUNDLES + 1)), ("test", "holdout"), "test", deadline, "final-exam")
    s = w.summary(args.generation, "exam")
    st.backend.upsert("agent_runs", [dict(s, started=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))])
    keep = ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action", "expiry", "strike_pct",
            "exit_rule", "ret_pct", "reason")
    st.backend.upsert("agent_trades", [{k: t.get(k) for k in keep} for t in w.trades])
    st.backend.upsert("agent_ratings", w.ratings)
    st.backend.upsert("agent_weeks", w.week_rows)
    rows_b, lines = book_rows(args.generation, "editor", "test", rules, exam)
    st.backend.upsert("scorebook", rows_b)
    print(f"Final exam: {s['trades']} trades, profit ${s['profit_usd']:+,.0f} (random ${s['baseline_profit_usd'] or 0:+,.0f}); "
          f"rating correlation {s.get('rating_corr')} ({s.get('rating_corr_lo')} to {s.get('rating_corr_hi')})")
    print("Editor rules on the exam:\n" + "\n".join(lines))
    report(args)


# ---------------------------------------------------------------- model bake-off
def openrouter_models():
    import urllib.request
    base = os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
    req = urllib.request.Request(f"{base}/models", headers={"Authorization": f"Bearer {os.environ.get('LLM_API_KEY', '')}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())["data"]


def resolve_model(want, catalog):
    """An exact OpenRouter id, or the best match for a short name like 'kimi-k2.6'."""
    ids = {m["id"]: m for m in catalog}
    if want in ids:
        return ids[want]
    w = want.lower()
    hits = [m for m in catalog if w in m["id"].lower() and ":" not in m["id"]]
    hits.sort(key=lambda m: len(m["id"]))
    return hits[0] if hits else None


def bakeoff(args):
    """The same blind scoring run (same notes, same months, same rules) with different models."""
    st = C.db()
    pool = load_pool(st)
    CFG.update(lineage=args.source_lineage, options_only=args.options_only)
    notes = [r for r in st.backend.read("committee_notes") if r["author"] == "editor"
             and r["lineage"] == args.source_lineage and int(r["generation"]) == args.generation]
    if not notes:
        sys.exit(f"No editor notes for {args.source_lineage} generation {args.generation}.")
    book = book_text(st, args.generation)
    catalog = openrouter_models()
    entries = []
    # The reference: the lineage's own scoring run for that generation (already paid for).
    ref = [r for r in st.backend.read("agent_runs") if r["lineage"] == args.source_lineage
           and int(r["generation"] or 0) == args.generation and r["phase"] == "score"]
    if ref:
        r = ref[-1]
        entries.append((r["model"] + " (from the lineage's own run)", r,
                        [t for t in st.backend.read("agent_trades") if t["run_id"] == r["run_id"]], None))
    done = {r["agent"]: r for r in st.backend.read("agent_runs") if r["lineage"] == "bakeoff"
            and r.get("model") and int(r["generation"] or 0) == args.generation}
    pot = Pot(args.max_usd, spent(st))
    deadline = time.monotonic() + 60 * args.max_minutes
    for want in [m.strip() for m in args.models.split(",") if m.strip()]:
        m = resolve_model(want, catalog)
        if not m:
            near = [x["id"] for x in catalog if want.split("-")[0].lower() in x["id"].lower()][:8]
            print(f"{want}: not found on OpenRouter. Close: {near}")
            entries.append((f"{want} (not found)", None, [], None))
            continue
        mid = m["id"]
        price = m.get("pricing") or {}
        price_txt = f"${float(price.get('prompt') or 0) * 1e6:.2f} / ${float(price.get('completion') or 0) * 1e6:.2f}"
        name = f"bakeoff-{args.source_lineage}-g{args.generation}-{mid}"
        if name in done and not args.redo:
            r = done[name]
            entries.append((mid, r, [t for t in st.backend.read("agent_trades") if t["run_id"] == r["run_id"]], price_txt))
            continue
        print(f"Running {mid} ({price_txt} per million tokens in / out)...")
        started = time.monotonic()
        model_deadline = min(deadline, started + 60 * args.per_model_minutes)
        CFG.update(lineage="bakeoff")
        try:
            w = blind_run(args.generation, lambda: pot.llm(mid), notes[0]["text"], book, pool, TRAIN_BUNDLES,
                          ("score",), "score", model_deadline, f"bakeoff-{mid.replace('/', '-')}")
        except (Exception, TimeUp) as ex:   # noqa: BLE001 - a model that can't finish is itself a result
            why = (f"too slow: not finished in {args.per_model_minutes:.0f} minutes" if isinstance(ex, TimeUp)
                   else f"failed: {type(ex).__name__}: {str(ex)[:120]}")
            print(f"{mid}: {why}")
            entries.append((f"{mid} ({why})", None, [], price_txt))
            CFG.update(lineage=args.source_lineage)
            continue
        CFG.update(lineage=args.source_lineage)
        s = dict(w.summary(args.generation, name), lineage="bakeoff",
                 started=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
        s["sample_reply"] = (s.get("sample_reply") or "")[:600]
        C._STORE = None
        st = C.db()
        st.backend.upsert("agent_runs", [s])
        keep = ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action", "expiry", "strike_pct",
                "exit_rule", "ret_pct", "reason")
        st.backend.upsert("agent_trades", [{k: t.get(k) for k in keep} for t in w.trades])
        print(f"{mid}: {s['trades']} trades, {s['bad_replies']}/{s['replies']} unreadable, ${s['cost_usd']}, "
              f"{(time.monotonic() - started) / 60:.0f} minutes")
        entries.append((mid, s, w.trades, price_txt))
    write_bakeoff(args, pool, entries)


def write_bakeoff(args, pool, entries):
    L = [f"# Model bake-off ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
         f"Every model traded the same blind scoring months with the same notes ({args.source_lineage}, generation "
         f"{args.generation}'s editor notes and scorebook), the same candidates and the same rules"
         f"{' (calls only)' if args.options_only else ''}. One run each, so the money results are noisy; the",
         "reliability columns (unreadable replies, replies cut off) are the most dependable comparison.", "",
         "| model | price per million tokens (in / out) | replies unreadable | cut off | cost $ | trades | average % | "
         "random same trades % | WIDE list: agent vs random % (range of the difference) | rating correlation |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for name, s, trades, price in entries:
        if not s:
            L.append(f"| {name} | {price or '-'} | | | | | | | | |")
            continue
        wd = list_stats(pool, trades).get("wide")
        if wd:
            rng_ = "no range" if wd["lo"] is None else f"{wd['lo']:+.1f} to {wd['hi']:+.1f}"
            wide = f"{wd['mean']:+.1f} vs {wd['random']:+.1f} ({wd['excess']:+.1f}; {rng_})"
        else:
            wide = "-"
        corr = f"{s.get('rating_corr')}" if s.get("rating_corr") not in (None, "") else "-"
        L.append(f"| {name} | {price or 'see OpenRouter'} | {s.get('bad_replies')}/{s.get('replies')} | {s.get('cut_off') or 0} | "
                 f"{s.get('cost_usd')} | {s.get('trades')} | {s.get('mean_ret')} | {s.get('baseline_mean')} | {wide} | {corr} |")
    with open(os.path.join(C.ROOT, "BAKEOFF.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))
    C.run_log("bakeoff", "; ".join(f"{n}: {s.get('bad_replies')}/{s.get('replies')} unreadable, ${s.get('cost_usd')}"
                                   for n, s, _, _ in entries if s))


# ---------------------------------------------------------------- playoff
def agent_strength(book_rows_, min_trades=30):
    """An agent's best rule, as tested by code on all training months: the bottom of its 95% range
    minus buying everything the same way. Comparable across generations and lineages."""
    best = None
    for b in book_rows_:
        if b["ci_low"] in (None, "") or b["baseline_mean"] in (None, "") or int(b["trades"] or 0) < min_trades:
            continue
        edge = float(b["ci_low"]) - float(b["baseline_mean"])
        if best is None or edge > best[0]:
            best = (edge, b)
    return best


def playoff(args):
    """Shortlist the strongest agents from every lineage by the code scorebook, run each through the
    blind months with only its own notes, and judge them on the wide list (no hindsight)."""
    st = C.db()
    pool = load_pool(st)
    book = [b for b in st.backend.read("scorebook") if b["period"] == "train" and str(b["author"]).startswith("agent")]
    by_agent = {}
    for b in book:
        by_agent.setdefault((b["lineage"], int(b["generation"]), b["author"]), []).append(b)
    notes = {(n["lineage"], int(n["generation"]), n["author"]): n for n in st.backend.read("committee_notes")
             if str(n["author"]).startswith("agent")}
    ranked = []
    for key, rows in by_agent.items():
        s = agent_strength(rows)
        if s and key in notes and (notes[key]["text"] or "").strip():
            ranked.append((s[0], key, s[1], rows))
    ranked.sort(key=lambda x: -x[0])
    print(f"{len(ranked)} agents with notes and a scorable rule; top {args.finalists}:")
    finalists = ranked[:args.finalists]
    for edge, key, b, _ in finalists:
        print(f"  {key}: best rule '{b['rule_name']}', edge {edge:+.2f} on {b['trades']} trades")
    CFG.update(lineage="playoff", options_only=False)
    done = {r["agent"]: r for r in st.backend.read("agent_runs") if r["lineage"] == "playoff" and r["phase"] == "score"}
    deadline = time.monotonic() + 60 * args.max_minutes
    pot = Pot(args.max_usd, spent(st))
    results = []
    for i, (edge, key, b, rows) in enumerate(finalists, 1):
        name = f"{key[0]}-g{key[1]}-{key[2]}"
        if name in done and not args.redo:
            print(f"{name}: already played; reusing its result.")
            run_id = done[name]["run_id"]
            trades = [t for t in st.backend.read("agent_trades") if t["run_id"] == run_id]
            results.append((edge, key, b, done[name], trades))
            continue
        text = notes[key]["text"]
        rules_text = "\n".join(scorebook_line(json.loads(r["rule"]), stats_of(r)) for r in rows)
        w = blind_run(i, lambda: pot.llm(args.model), text, rules_text, pool, TRAIN_BUNDLES, ("score",),
                      "score", deadline, f"playoff-{name}")
        s = dict(w.summary(i, name), started=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))
        C._STORE = None
        st = C.db()
        st.backend.upsert("agent_runs", [s])
        keep = ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action", "expiry", "strike_pct",
                "exit_rule", "ret_pct", "reason")
        st.backend.upsert("agent_trades", [{k: t.get(k) for k in keep} for t in w.trades])
        st.backend.upsert("agent_weeks", w.week_rows)
        print(f"{name}: {s['trades']} trades, mean {s['mean_ret']}%, cost ${s['cost_usd']}")
        results.append((edge, key, b, s, w.trades))
    write_playoff(pool, results)


def write_playoff(pool, results):
    def fmt(v, f="{:+.2f}"):
        return "-" if v is None else f.format(v)
    L = [f"# Playoff ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
         "Finalists: the agents (from every lineage) whose best rule held up best when code tested it on all",
         "training months. Each then traded the blind months with only its own final notes and rules, stock or",
         "calls allowed. Judged on the **wide list** (chosen January 2024, no hindsight): average return per trade",
         "minus the same kind of trade on random wide-list candidates in the same weeks, 95% range by week.", "",
         "| finalist | best training rule (edge) | blind trades | WIDE: trades, agent vs random % | WIDE excess (range) | "
         "big movers: agent vs random % | cost $ |", "|---|---|---|---|---|---|---|"]
    verdicts = []
    for edge, key, b, s, trades in results:
        name = f"{key[0]} gen {key[1]} {key[2]}"
        ls = list_stats(pool, trades)
        wd, mv = ls.get("wide"), ls.get("movers")
        wide = f"{wd['n']}: {wd['mean']:+.2f} vs {wd['random']:+.2f}" if wd else "-"
        rng_ = f"{wd['excess']:+.2f} ({fmt(wd['lo'])} to {fmt(wd['hi'])})" if wd else "-"
        mov = f"{mv['mean']:+.2f} vs {mv['random']:+.2f} ({mv['n']})" if mv else "-"
        L.append(f"| {name} | {b['rule_name']} ({edge:+.2f}) | {s.get('trades')} | {wide} | {rng_} | {mov} | {s.get('cost_usd')} |")
        verdicts.append((wd["excess"] if wd else -1e9, name, wd))
    verdicts.sort(reverse=True)
    L += ["", "## Verdict", ""]
    clear = [v for v in verdicts if v[2] and v[2]["lo"] is not None and v[2]["lo"] > 0]
    if clear:
        L.append(f"- **{clear[0][1]}** beat random on the wide list with its whole range above zero. It earns paper account 2.")
    elif verdicts and verdicts[0][2]:
        L.append(f"- Nobody beat random on the wide list clearly. Best showing: {verdicts[0][1]} "
                 f"({verdicts[0][2]['excess']:+.2f}% per trade versus random, range crossing zero). Treat that as luck;")
        L.append("  choose paper account 2 for the most interesting strategy rather than this result.")
    L += [f"- {len(results)} finalists were tested, so one passing narrowly could still be chance."]
    with open(os.path.join(C.ROOT, "PLAYOFF.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))
    C.run_log("playoff", "; ".join(f"{v[1]}: wide excess {v[2]['excess']:+.2f}" for v in verdicts if v[2]))


# ---------------------------------------------------------------- report
def report(args=None):
    st = C.db()
    runs = [r for r in st.backend.read("agent_runs") if r["lineage"] == CFG["lineage"]]
    notes = [n for n in st.backend.read("committee_notes") if n["lineage"] == CFG["lineage"]]
    book = [b for b in st.backend.read("scorebook") if b["lineage"] == CFG["lineage"]]
    pool_counts = {}
    for r in st.backend.read("pool"):
        pool_counts[r["split"]] = pool_counts.get(r["split"], 0) + 1
    L = [f"# Committee generations ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
         f"Total spent on all agent runs: ${spent(st):.2f}. Candidate pool: {pool_counts}.", "",
         "Four agents train independently on six stock bundles; code scores their rules; an editor writes the",
         "notes passed on. The scoring run trades blind months with the editor's notes. \"Random\" makes the same",
         "number and kind of trades on random candidates in the same weeks. Rating correlation: does a higher",
         "rating go with a better 10-session stock return (0 = no skill, ranges are 95%). Every trade is $1,000.", "",
         "## Runs", "",
         "| gen | who | phase | trades | profit $ | random profit $ | mean % | win % | rating corr (95% range) | top rated % | bottom rated % | unreadable | cost $ |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(runs, key=lambda r: (int(r["generation"] or 0), r["phase"] != "train", r["agent"] or "")):
        corr = f"{r['rating_corr']} ({r['rating_corr_lo']} to {r['rating_corr_hi']})" if r.get("rating_corr") else "-"
        L.append(f"| {r['generation']} | {r['agent']} | {r['phase']} | {r['trades']} | {r['profit_usd']} | "
                 f"{r['baseline_profit_usd'] or '-'} | {r['mean_ret'] or '-'} | {r['win_rate'] or '-'} | {corr} | "
                 f"{r.get('top_rated_ret') or '-'} | {r.get('bottom_rated_ret') or '-'} | "
                 f"{r.get('bad_replies') or 0}/{r.get('replies')} | {r['cost_usd']} |")
    # Luck check: every rule ever tested, and how many passed the blind months clearly (the bottom of
    # the 95% range above buying everything the same way). About 1 in 40 would do that by chance.
    tested = {b["rule"] for b in book if b["period"] == "train"}
    blind = [b for b in book if b["period"] == "score"]
    passed = [b for b in blind if b["ci_low"] not in (None, "") and b["baseline_mean"] not in (None, "")
              and float(b["ci_low"]) > float(b["baseline_mean"])]
    L += ["", "## Luck check", "",
          f"- Different rules tested on training data so far: {len(tested)} (by the agents and the editor).",
          f"- Editor rules checked on the blind months: {len(blind)}; passed clearly (whole 95% range above "
          f"buying everything the same way): {len(passed)}.",
          f"- Expected to pass by luck alone: about {len(blind) * 0.025:.1f}. Treat a pass as real only if it "
          f"clearly beats that count and the rule keeps passing in later generations."]
    if passed:
        L += [f"  - passed: {b['rule_name']} (generation {b['generation']}): blind average {b['mean_ret']}% "
              f"versus {b['baseline_mean']}% for buying everything" for b in passed]
    L += by_list_section(st, runs)
    gens = sorted({int(n["generation"]) for n in notes})
    for g in reversed(gens):
        L += ["", f"## Generation {g}", ""]
        for period, title in (("train", "Editor's rules, tested on all training months and bundles"),
                              ("score", "The same rules on the blind scoring months (never shown to agents)"),
                              ("test", "The same rules on the final exam")):
            rows = [b for b in book if int(b["generation"]) == g and b["author"] == "editor" and b["period"] == period]
            if rows:
                L += [f"### {title}", ""]
                L += [scorebook_line(json.loads(b["rule"]), stats_of(b)) for b in rows]
                L.append("")
        order = {"editor": 0, "redesign": 1}
        for n in sorted((n for n in notes if int(n["generation"]) == g),
                        key=lambda n: (order.get(n["author"], 2), n["author"])):
            who = {"editor": "Editor's notes (passed to the next generation)",
                   "redesign": "How the committee would remake the test (not passed on)"}.get(
                n["author"], f"Agent {n['author'][-1]}'s final notes (not passed on)")
            L += [f"### {who}", "", n["text"] or "(empty)", ""]
    err = os.path.join(C.ROOT, "committee_error.txt")
    if os.path.exists(err):
        L += ["", "## Last error", "", "```", open(err).read(), "```"]
    name = "COMMITTEE.md" if CFG["lineage"] == "committee" else f"COMMITTEE-{CFG['lineage']}.md"
    with open(os.path.join(C.ROOT, name), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:40]))


def list_stats(pool, trades, reps=60, seed=17):
    """Trades split by list ('wide' = honest, 'movers' = hindsight). For each trade, the expected
    return of the same kind of trade on a random candidate from the same list in the same week; the
    excess over that, with a 95% range resampling whole weeks."""
    by_key = {(c["ticker"], str(c["date"])[:10]): c for c in pool}
    by_week = {}
    for c in pool:
        by_week.setdefault((c["week"], c["universe"]), []).append(c)
    rng = random.Random(seed)
    out = {}
    for t in trades:
        c = by_key.get((t["ticker"], str(t["signal_date"])[:10]))
        if not c or t.get("ret_pct") in (None, ""):
            continue
        exp = int(t["expiry"]) if t.get("expiry") not in (None, "") else None
        strike = float(t["strike_pct"]) if t.get("strike_pct") not in (None, "") else None
        cands = by_week.get((c["week"], c["universe"]), [])
        sims = []
        for _ in range(reps):
            for _try in range(10):
                if not cands:
                    break
                v = A.trade_return(rng.choice(cands), t["action"], exp, strike, t.get("exit_rule") or None)
                if v is not None:
                    sims.append(v)
                    break
        if sims:
            r = float(t["ret_pct"])
            out.setdefault(c["universe"], []).append((c["week"], r, statistics.mean(sims)))
    res = {}
    for u, items in out.items():
        weeks = {}
        for w, r, m in items:
            weeks.setdefault(w, []).append(r - m)
        wl = list(weeks.values())
        lo = hi = None
        if len(wl) >= 5:
            sims = []
            for _ in range(1000):
                pick = [rng.choice(wl) for _ in wl]
                vals = [v for w in pick for v in w]
                sims.append(sum(vals) / len(vals))
            sims.sort()
            lo, hi = sims[25], sims[974]
        res[u] = {"n": len(items), "mean": statistics.mean(i[1] for i in items),
                  "random": statistics.mean(i[2] for i in items),
                  "excess": statistics.mean(i[1] - i[2] for i in items), "lo": lo, "hi": hi,
                  "weeks": len(wl)}
    return res


def by_list_section(st, runs):
    """Blind scoring trades split by list. The big-mover list was chosen for stocks that LATER had 3+ days
    up 15%, so a strategy can look good there through hindsight alone. The wide list (chosen from January
    2024 data only) is the honest test. Random = same number and kind of trades on random candidates
    from the same list in the same weeks."""
    score_runs = {r["run_id"]: r for r in runs if r["phase"] == "score"}
    if not score_runs:
        return []
    pool = load_pool(st)
    by_key = {(c["ticker"], str(c["date"])[:10]): c for c in pool}
    by_week = {}
    for c in pool:
        by_week.setdefault((c["week"], c["universe"]), []).append(c)
    trades = [t for t in st.backend.read("agent_trades") if t["run_id"] in score_runs]
    rng = random.Random(17)
    L = ["", "## Blind scoring trades by list (hindsight check)", "",
         "The big-mover list was chosen for stocks that later had 3+ days up 15%, so results there can come",
         "from hindsight alone. The wide list (chosen from January 2024 data only) is the honest test.",
         "Random = the same kind of trades on random candidates from the same list in the same weeks.", "",
         "| gen | list | trades | mean % | random mean % | profit $ | random profit $ |", "|---|---|---|---|---|---|---|"]
    rows = {}
    for t in trades:
        c = by_key.get((t["ticker"], str(t["signal_date"])[:10]))
        if not c or t.get("ret_pct") in (None, ""):
            continue
        g = int(score_runs[t["run_id"]]["generation"])
        rows.setdefault((g, c["universe"]), []).append((t, c))
    for (g, u), items in sorted(rows.items()):
        rets = [float(t["ret_pct"]) for t, _ in items]
        sims = []
        for _ in range(200):
            r_ = []
            for t, c in items:
                cands = by_week.get((c["week"], u), [])
                for _try in range(10):
                    if not cands:
                        break
                    x = rng.choice(cands)
                    exp = int(t["expiry"]) if t.get("expiry") not in (None, "") else None
                    strike = float(t["strike_pct"]) if t.get("strike_pct") not in (None, "") else None
                    v = A.trade_return(x, t["action"], exp, strike, t.get("exit_rule") or None)
                    if v is not None:
                        r_.append(v)
                        break
            if r_:
                sims.append(statistics.mean(r_))
        rm = statistics.mean(sims) if sims else None
        name = "wide (honest)" if u == "wide" else "big movers (hindsight)"
        L.append(f"| {g} | {name} | {len(rets)} | {statistics.mean(rets):+.2f} | "
                 f"{f'{rm:+.2f}' if rm is not None else '-'} | {sum(rets) * A.TRADE_USD / 100:+,.0f} | "
                 f"{f'{rm * len(rets) * A.TRADE_USD / 100:+,.0f}' if rm is not None else '-'} |")
    return L


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build-pool")
    b.add_argument("--archive", help="the ladder archive file (rows still in the database are added)")
    b.add_argument("--per-week-movers", type=int, default=6)
    b.add_argument("--per-week-wide", type=int, default=4)
    b.add_argument("--force", action="store_true", help="replace the pool even if the sanity checks object")
    for name in ("loop", "final-test"):
        a = sub.add_parser(name)
        a.add_argument("--model", default=os.environ.get("LLM_MODEL", "anthropic/claude-haiku-5.5"))
        a.add_argument("--max-usd", type=float, default=float(os.environ.get("MAX_USD", "25")))
        a.add_argument("--max-minutes", type=float, default=140)
        if name == "loop":
            a.add_argument("--generations", type=int, default=1)
            a.add_argument("--weeks-fraction", type=float, default=0.5)
            a.add_argument("--editor-model", default=os.environ.get("EDITOR_MODEL", "anthropic/claude-sonnet-5.5"),
                           help="a stronger model for the editor, who writes the notes every later generation inherits")
        else:
            a.add_argument("--generation", type=int, required=True)
    sub.add_parser("report")
    bo = sub.add_parser("bakeoff")
    bo.add_argument("--models", default="deepseek/deepseek-v4-pro,kimi-k2.6,glm-5.2")
    bo.add_argument("--source-lineage", default="gen10")
    bo.add_argument("--generation", type=int, default=5)
    bo.add_argument("--options-only", action="store_true")
    bo.add_argument("--max-usd", type=float, default=float(os.environ.get("MAX_USD", "25")))
    bo.add_argument("--max-minutes", type=float, default=140)
    bo.add_argument("--redo", action="store_true")
    bo.add_argument("--per-model-minutes", type=float, default=35)
    po = sub.add_parser("playoff")
    po.add_argument("--finalists", type=int, default=5)
    po.add_argument("--model", default=os.environ.get("LLM_MODEL", "anthropic/claude-haiku-5.5"))
    po.add_argument("--max-usd", type=float, default=float(os.environ.get("MAX_USD", "25")))
    po.add_argument("--max-minutes", type=float, default=140)
    po.add_argument("--redo", action="store_true", help="replay finalists that already played")
    for sp in sub.choices.values():
        if sp.prog.split()[-1] in ("loop", "final-test", "report"):
            sp.add_argument("--lineage", default="committee",
                            help="a separate line of generations with its own notes (e.g. options1)")
            sp.add_argument("--options-only", action="store_true", help="agents may only buy calls")
            sp.add_argument("--seed", choices=["none", "briefing"], default="none",
                            help="what a new lineage's first generation starts with")
    a = p.parse_args()
    if hasattr(a, "lineage"):
        if not re.fullmatch(r"[a-z0-9-]{1,30}", a.lineage):
            sys.exit("Lineage names use lowercase letters, digits and dashes only.")
        CFG.update(lineage=a.lineage, options_only=a.options_only, seed=a.seed)
    try:
        {"build-pool": build_pool, "loop": loop, "final-test": final_test, "report": report,
         "playoff": playoff, "bakeoff": bakeoff}[a.cmd](a)
    except SystemExit:
        raise
    except BaseException as ex:   # noqa: BLE001 - save it where it can be read, then fail the job
        save_crash(f"{a.cmd} crashed: {type(ex).__name__}: {ex}")
        raise


if __name__ == "__main__":
    main()
