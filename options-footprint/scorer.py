"""
Signal scorer: does unusual options activity actually come before big moves?

Uses every trading day for tickers with full options history (data/history_done.csv).
For each day it computes signals from that day and earlier ONLY, then looks at what the
stock did over the following days. A signal is useful if big moves follow it noticeably
more often than they follow an ordinary day, consistently in both halves of the data.

    python scorer.py                         # "big move" = up 15%+ and 30%+ within 10 sessions
    python scorer.py --moves 20 --days 5     # different threshold and horizon

Writes data/signal_days.csv (every scored day) and data/signal_report.csv (one row per rule),
and prints a summary. Standard library only.
"""
import argparse
import csv
import datetime as dt
import os
import statistics

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
DAILY = os.path.join(DATA, "daily_features.csv")
HISTORY_DONE = os.path.join(DATA, "history_done.csv")
DAYS_OUT = os.path.join(DATA, "signal_days.csv")
REPORT_OUT = os.path.join(DATA, "signal_report.csv")

BASELINE_DAYS = 20          # "normal" = median of the previous 20 sessions
MIN_BASELINE_CALLS = 50     # skip days when the stock's options normally barely trade
SPLIT_ARTIFACT_UP = 2.0     # a raw close jumping 200%+ or falling 66%+ in one day is almost
SPLIT_ARTIFACT_DOWN = -0.66 # always a split or share reissue; skip windows that cross one

SERIES = ["call_volume", "put_volume", "call_vol_short", "call_vol_medium", "call_vol_long",
          "call_vol_otm", "call_vol_atm", "call_vol_itm", "short_otm_call_volume", "stock_volume"]


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def spike(values, i):
    """Today's value versus the median of the previous BASELINE_DAYS sessions."""
    prior = [v for v in values[max(0, i - BASELINE_DAYS):i] if v is not None]
    if len(prior) < BASELINE_DAYS // 2 or values[i] is None:
        return None
    base = statistics.median(prior)
    return values[i] / base if base > 0 else None


def score_days(move, horizon):
    done = {r["ticker"] for r in csv.DictReader(open(HISTORY_DONE))}
    by_ticker = {}
    with open(DAILY, newline="") as f:
        for r in csv.DictReader(f):
            if r["ticker"] in done and r.get("put_call_alpaca") not in (None, ""):
                by_ticker.setdefault(r["ticker"], []).append(r)
    out = []
    for t, rows in sorted(by_ticker.items()):
        rows.sort(key=lambda r: r["date"])
        close = [num(r["stock_close"]) for r in rows]
        series = {k: [num(r.get(k)) for r in rows] for k in SERIES}
        pcr = [num(r["put_call_alpaca"]) for r in rows]
        daily_ret = [None] + [(close[i] / close[i - 1] - 1) if close[i] and close[i - 1] else None
                              for i in range(1, len(rows))]
        for i in range(BASELINE_DAYS, len(rows) - horizon):
            c0 = close[i]
            if not c0:
                continue
            # Skip windows that cross a split or reissue (raw prices would fake a move).
            window = daily_ret[i - 5:i + horizon + 1]
            if any(x is not None and (x > SPLIT_ARTIFACT_UP or x < SPLIT_ARTIFACT_DOWN) for x in window):
                continue
            base_calls = statistics.median(v for v in series["call_volume"][i - BASELINE_DAYS:i] if v is not None)
            if base_calls < MIN_BASELINE_CALLS:
                continue
            future = [c for c in close[i + 1:i + horizon + 1] if c]
            if len(future) < horizon:
                continue
            prior_pcr = [p for p in pcr[i - BASELINE_DAYS:i] if p is not None]
            d = {"ticker": t, "date": rows[i]["date"], "close": c0,
                 # What happened next (the outcome being predicted).
                 "fwd_max_gain_pct": round((max(future) / c0 - 1) * 100, 2),
                 "fwd_max_drop_pct": round((min(future) / c0 - 1) * 100, 2),
                 "fwd_return_pct": round((future[-1] / c0 - 1) * 100, 2),
                 # What the stock had already done (to separate stealth from momentum).
                 "ret_5d_pct": round((c0 / close[i - 5] - 1) * 100, 2) if close[i - 5] else None,
                 "ret_1d_pct": round(daily_ret[i] * 100, 2) if daily_ret[i] is not None else None,
                 "put_call": pcr[i],
                 "put_call_drop": round(statistics.median(prior_pcr) / max(pcr[i], 0.01), 2)
                                  if prior_pcr and pcr[i] is not None else None}
            for k in SERIES:
                s = spike(series[k], i)
                d[f"{k}_spike"] = round(s, 2) if s is not None else None
            # Options activity running ahead of stock activity: the classic "someone knows" shape.
            cs, ss = d["call_volume_spike"], d["stock_volume_spike"]
            d["calls_vs_shares"] = round(cs / ss, 2) if cs and ss else None
            d["hit"] = 1 if d["fwd_max_gain_pct"] >= move else 0
            # The mirror image: a big DROP in the same window. If a signal predicts drops as
            # often as rallies, it is predicting volatility, not direction.
            d["drop_hit"] = 1 if d["fwd_max_drop_pct"] <= -move * 0.67 else 0
            out.append(d)
    return out


def g(d, k):
    v = d.get(k)
    return v if v is not None else 0.0


def quiet(d):
    return d["ret_5d_pct"] is not None and abs(d["ret_5d_pct"]) < 5 and abs(g(d, "ret_1d_pct")) < 3


RULES = {
    "Any day (baseline)": lambda d: True,
    "Put/call drop 3x+": lambda d: g(d, "put_call_drop") >= 3,
    "Put/call drop 5x+": lambda d: g(d, "put_call_drop") >= 5,
    "Call volume 3x+": lambda d: g(d, "call_volume_spike") >= 3,
    "Call volume 5x+": lambda d: g(d, "call_volume_spike") >= 5,
    "Long-dated calls 3x+": lambda d: g(d, "call_vol_long_spike") >= 3,
    "Long-dated calls 5x+": lambda d: g(d, "call_vol_long_spike") >= 5,
    "Medium-dated calls 3x+": lambda d: g(d, "call_vol_medium_spike") >= 3,
    "Short-dated calls 3x+": lambda d: g(d, "call_vol_short_spike") >= 3,
    "Out-of-the-money calls 3x+": lambda d: g(d, "call_vol_otm_spike") >= 3,
    "Short out-of-the-money calls 3x+": lambda d: g(d, "short_otm_call_volume_spike") >= 3,
    "Calls 3x+ while price quiet": lambda d: g(d, "call_volume_spike") >= 3 and quiet(d),
    "Long-dated 3x+ while price quiet": lambda d: g(d, "call_vol_long_spike") >= 3 and quiet(d),
    "Calls outpacing shares 2x+": lambda d: g(d, "calls_vs_shares") >= 2 and g(d, "call_volume_spike") >= 2,
    "Calls outpacing shares 3x+": lambda d: g(d, "calls_vs_shares") >= 3 and g(d, "call_volume_spike") >= 3,
    "Stealth: calls 3x+, shares normal, price quiet":
        lambda d: g(d, "call_volume_spike") >= 3 and g(d, "stock_volume_spike") < 1.5 and quiet(d),
    "Calls 3x+ and puts flat (put/call drop 3x+)":
        lambda d: g(d, "call_volume_spike") >= 3 and g(d, "put_call_drop") >= 3,
    "Momentum: calls 3x+ after 10%+ week": lambda d: g(d, "call_volume_spike") >= 3 and g(d, "ret_5d_pct") >= 10,
}


def episodes(days):
    """Count distinct signal episodes: fires on the same ticker within 5 sessions count once."""
    n, last = 0, {}
    for d in days:
        prev = last.get(d["ticker"])
        if prev is None or (dt.date.fromisoformat(d["date"]) - dt.date.fromisoformat(prev)).days > 7:
            n += 1
        last[d["ticker"]] = d["date"]
    return n


def evaluate(days):
    days = sorted(days, key=lambda d: (d["ticker"], d["date"]))
    dates = sorted(d["date"] for d in days)
    mid = dates[len(dates) // 2]
    base_rate = sum(d["hit"] for d in days) / len(days)
    base_drop = sum(d["drop_hit"] for d in days) / len(days)
    base_ret = statistics.mean(d["fwd_return_pct"] for d in days)
    halves = {h: [d for d in days if (d["date"] < mid) == (h == 1)] for h in (1, 2)}
    half_base = {h: sum(d["hit"] for d in v) / len(v) for h, v in halves.items()}
    report = []
    for name, rule in RULES.items():
        fired = [d for d in days if rule(d)]
        if not fired:
            continue
        hit = sum(d["hit"] for d in fired) / len(fired)
        row = {"rule": name, "days_fired": len(fired), "episodes": episodes(fired),
               "hit_rate_pct": round(100 * hit, 1),
               "lift": round(hit / base_rate, 2) if base_rate else None,
               "drop_lift": round((sum(d["drop_hit"] for d in fired) / len(fired)) / base_drop, 2)
                            if base_drop else None,
               "avg_fwd_return_pct": round(statistics.mean(d["fwd_return_pct"] for d in fired), 2),
               "median_fwd_return_pct": round(statistics.median(d["fwd_return_pct"] for d in fired), 2),
               "avg_fwd_max_gain_pct": round(statistics.mean(d["fwd_max_gain_pct"] for d in fired), 2)}
        for h in (1, 2):
            f = [d for d in halves[h] if rule(d)]
            row[f"lift_half{h}"] = (round((sum(d["hit"] for d in f) / len(f)) / half_base[h], 2)
                                    if f and half_base[h] else None)
            row[f"fired_half{h}"] = len(f)
        report.append(row)
    return report, base_rate, base_ret, mid


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--moves", default="15,30", help="comma-separated percent gains that count as a big move")
    p.add_argument("--days", type=int, default=10, help="sessions after the signal to look for it")
    a = p.parse_args()
    all_rows, saved_days = [], False
    for move in [float(x) for x in a.moves.split(",")]:
        days = score_days(move, a.days)
        if not days:
            raise SystemExit("No full-history tickers yet; run the backfill first.")
        if not saved_days:   # the per-day file is the same for every threshold except the hit flags
            with open(DAYS_OUT, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=list(days[0].keys())); w.writeheader(); w.writerows(days)
            saved_days = True
        report, base, base_ret, mid = evaluate(days)
        base_med = statistics.median(d["fwd_return_pct"] for d in days)
        for r in report:
            all_rows.append({"move_pct": move, "horizon_days": a.days, **r})
        tickers = len({d["ticker"] for d in days})
        print(f"\n=== Big move = up {move:g}%+ within {a.days} sessions "
              f"({len(days):,} ticker-days, {tickers} tickers) ===")
        print(f"Baseline: {100 * base:.1f}% of all days are followed by a big move; "
              f"median {a.days}-session return {base_med:+.2f}%. Halves split at {mid}.\n")
        print(f"{'rule':<48}{'fired':>7}{'hit %':>7}{'lift':>6}{'1st':>6}{'2nd':>6}{'drop':>6}{'median ret':>11}")
        for r in report:
            print(f"{r['rule']:<48}{r['days_fired']:>7}{r['hit_rate_pct']:>7}{r['lift']:>6}"
                  f"{str(r['lift_half1']):>6}{str(r['lift_half2']):>6}{str(r['drop_lift']):>6}"
                  f"{r['median_fwd_return_pct']:>+11.2f}")
    with open(REPORT_OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys())); w.writeheader(); w.writerows(all_rows)
    print("\nlift = how many times more often a big rally follows the signal than an average day;")
    print("1st/2nd = the same lift in each half of the data; drop = lift for a big DROP instead.")
    print("A real directional signal has rally lift above 1 in both halves AND drop lift near or below 1.")


if __name__ == "__main__":
    main()
