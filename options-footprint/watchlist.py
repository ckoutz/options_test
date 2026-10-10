"""
Watchlist test: would a list of "past big movers", built only from what was known at the time, have
helped? (The live agents will build lists like this, so this tests the idea without hindsight.)

    python watchlist.py --archive ladder_trades.csv.gz     # writes WATCHLIST.md

Honest by construction:
- Stocks: the WIDE list only (chosen from January 2024 price and volume, before any outcome). The
  big-mover list is excluded because it was chosen using the future.
- Each stock-day is labeled by how many days the stock rose 15%+ in the PREVIOUS 252 sessions
  (about a year), known at that moment. Days in 2025 and 2026 are tested (2024 is the look-back).
- Outcomes: the stock over the next 10 sessions (bought at the next close), the chance of a 15%+ up
  day or a 15%+ down day in those 10 sessions, and, where the options backtest has the contract, a
  30-day at-the-money call held 10 sessions with realistic costs, plus its implied volatility.
- Ranges are 95%, resampling whole weeks, for each group's difference from the "no big moves" group.
"""
import argparse
import datetime as dt
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C   # noqa: E402
import committee as K   # noqa: E402
import agents as A      # noqa: E402

BIG = 0.15
LOOKBACK = 252
GROUPS = [("none in the past year", 0, 0), ("1 to 2", 1, 2), ("3 to 5", 3, 5), ("6 or more", 6, 10 ** 6)]


def group_of(n):
    return next(name for name, lo, hi in GROUPS if lo <= n <= hi)


def week_range(diffs, reps=1000, seed=9):
    """diffs: list of (week, value). 95% range of the mean, resampling weeks."""
    by = {}
    for w, v in diffs:
        by.setdefault(w, []).append(v)
    weeks = list(by.values())
    if len(weeks) < 10:
        return None, None
    rng = random.Random(seed)
    sims = []
    for _ in range(reps):
        pick = [rng.choice(weeks) for _ in weeks]
        vals = [v for w in pick for v in w]
        sims.append(sum(vals) / len(vals))
    sims.sort()
    return sims[int(0.025 * reps)], sims[int(0.975 * reps) - 1]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--archive", default=None)
    p.add_argument("--start", default="2025-01-01")
    args = p.parse_args()
    st = C.db()
    wide = set(C.wide_tickers()) - set(C.mover_tickers())
    rows = []          # (ticker, date, week, group, ret10, up15, down15)
    for n, t in enumerate(sorted(wide), 1):
        daily = [r for r in st.daily(t) if C.to_float(r.get("stock_close"))]
        dates = [r["date"] for r in daily]
        closes = [C.to_float(r["stock_close"]) for r in daily]
        day_ret = [None] + [closes[k] / closes[k - 1] - 1 for k in range(1, len(closes))]
        for i in range(LOOKBACK, len(dates) - 11):
            if dates[i] < args.start:
                continue
            past = sum(1 for k in range(i - LOOKBACK + 1, i + 1) if day_ret[k] is not None and day_ret[k] >= BIG)
            nxt = [day_ret[k] for k in range(i + 2, i + 12) if day_ret[k] is not None]
            ret10 = ((closes[i + 11] * (1 - A.SHARE_COST)) / (closes[i + 1] * (1 + A.SHARE_COST)) - 1) * 100
            rows.append((t, dates[i], A.week_of(dates[i]), group_of(past), ret10,
                         any(r >= BIG for r in nxt), any(r <= -BIG for r in nxt)))
        if n % 50 == 0:
            print(f"  {n}/{len(wide)} stocks, {len(rows):,} stock-days")
    if not rows:
        sys.exit("No stock-days to test.")
    # Excess over the average wide stock the same day, so market moves cancel out.
    by_day = {}
    for r in rows:
        by_day.setdefault(r[1], []).append(r[4])
    day_mean = {d: statistics.mean(v) for d, v in by_day.items()}
    label = {(r[0], r[1]): r[3] for r in rows}

    # Options: the 30-day at-the-money call, held 10 sessions, realistic costs, from the options backtest.
    calls = {}
    if True:
        for r in K.ladder_rows(K.ladder_files(st, args.archive)):
            key = (r["ticker"], r["signal_date"])
            if key not in label or r.get("filled") != "yes" or r.get("target_dte") not in ("30", "30.0"):
                continue
            if float(r.get("target_otm_pct") or -1) != 0.0 or r.get("ret_hold10_pct") in (None, ""):
                continue
            sess, iv = K.option_detail(r)
            if sess is not None and sess <= A.HOLD_SESSIONS:
                continue
            cell = K.realistic_cell(float(r["entry_price"]), float(r["stock_close"]),
                                    C.to_float(r["ret_hold10_pct"]), C.to_float(r["ret_double_or_10_pct"]))
            calls[key] = (cell[1], iv)

    L = [f"# Watchlist test: do past big movers make good trades? ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
         f"Wide-list stocks only (chosen from January 2024 data, no hindsight), days from {args.start} on. Each "
         "stock-day is labeled by how many 15%+ up days the stock had in the previous year (known at the time). "
         "Returns are over the next 10 sessions, bought at the next close.", "",
         "| days with a 15%+ jump in the past year | stock-days | stocks | 10-session return: average / median | "
         "vs the average wide stock that day (range) | % that rose | chance of a 15%+ up day next 10 sessions | "
         "chance of a 15%+ down day |", "|---|---|---|---|---|---|---|---|"]
    base = None
    for name, _, _ in GROUPS:
        g = [r for r in rows if r[3] == name]
        if not g:
            continue
        ex = [(r[2], r[4] - day_mean[r[1]]) for r in g]
        lo, hi = week_range(ex)
        rng_ = f"{statistics.mean(v for _, v in ex):+.2f} ({lo:+.2f} to {hi:+.2f})" if lo is not None else \
            f"{statistics.mean(v for _, v in ex):+.2f}"
        L.append(f"| {name} | {len(g):,} | {len({r[0] for r in g})} | {statistics.mean(r[4] for r in g):+.2f}% / "
                 f"{statistics.median(r[4] for r in g):+.2f}% | {rng_} | {100 * sum(r[4] > 0 for r in g) / len(g):.0f}% | "
                 f"{100 * sum(r[5] for r in g) / len(g):.1f}% | {100 * sum(r[6] for r in g) / len(g):.1f}% |")
    L += ["", "## The 30-day at-the-money call on the same stock-days", "",
          "Where the options backtest has the contract (it covers selected days, not every day). Realistic costs; "
          "contracts expiring during the hold excluded.", "",
          "| days with a 15%+ jump in the past year | calls | average | median | % winners | median implied volatility |",
          "|---|---|---|---|---|---|"]
    for name, _, _ in GROUPS:
        g = [v for k, v in calls.items() if label[k] == name and v[0] is not None]
        if not g:
            L.append(f"| {name} | 0 | | | | |")
            continue
        r = [x[0] for x in g]
        ivs = [x[1] for x in g if x[1]]
        L.append(f"| {name} | {len(g):,} | {statistics.mean(r):+.1f}% | {statistics.median(r):+.1f}% | "
                 f"{100 * sum(x > 0 for x in r) / len(r):.0f}% | {statistics.median(ivs):.0f}% |" if ivs else
                 f"| {name} | {len(g):,} | {statistics.mean(r):+.1f}% | {statistics.median(r):+.1f}% | "
                 f"{100 * sum(x > 0 for x in r) / len(r):.0f}% | - |")
    L += ["", "## How to read it", "",
          "- If past big movers are a useful watchlist, the groups with more past jumps should beat the average "
          "wide stock (second column of the first table, range above zero), not just jump more often in both directions.",
          "- If they only show higher chances of BOTH a 15%+ up day and a 15%+ down day, the list catches volatility, "
          "not direction; whether that pays depends on the option's price (second table)."]
    with open(os.path.join(C.ROOT, "WATCHLIST.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))
    C.run_log("watchlist", f"{len(rows):,} wide-list stock-days tested; {len(calls):,} with a 30-day call")


if __name__ == "__main__":
    main()
