"""
Focused test: give a model a fair chance. Lots of data, one simple question, column groups tested
separately, and tuning that only ever looks at training months.

    python focused.py              # writes FOCUSED.md

The question: will this stock beat the other stocks over the next 10 sessions? (Its return, bought at
the next session's close and sold 10 sessions later, minus the average of every stock on the same day,
so a market-wide move doesn't count.) No options yet: if the data can't predict the stock, it can't
predict its calls.

The data: EVERY stock-day with options data for the stocks in bundles 1 to 6 (big movers and the wide
list), not the agents' small sample. Training months train; blind months judge. Held-back bundles 7 and
8 and the final-exam months (February 2026 on) are never touched. Days whose 10-session outcome would
cross into the other kind of month are dropped (the buffer).

The test, per column group (options flow, technical analysis, market, news, flow plus technical, all):
  1. Choose model settings using the latest fifth of the training weeks as a check set (training data
     only), then retrain on all training months.
  2. On the blind months, every day: rank all stocks by the model's prediction and measure how well
     that ranking matches what actually happened (rank correlation, 0 = no skill), and how the top
     tenth did versus the average stock.
  3. 95% ranges resample whole weeks.
"""
import argparse
import datetime as dt
import math
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C  # noqa: E402
import scorer as S     # noqa: E402
import agents as A     # noqa: E402
import committee as K  # noqa: E402

FLOW = ["call_volume_spike", "put_volume_spike", "put_call", "put_call_drop", "call_vol_short_spike",
        "call_vol_medium_spike", "call_vol_long_spike", "call_vol_otm_spike", "call_vol_atm_spike",
        "call_vol_itm_spike", "short_otm_call_volume_spike", "calls_vs_shares", "calls_5d_avg", "puts_5d_avg",
        "call_days_2x", "calls_20d", "long_calls_20d", "otm_calls_20d", "puts_20d", "call_days_2x_20d",
        "days_since_spike"]
TECH = ["ret_1d_pct", "ret_5d_pct", "ret_20d_pct", "vs_ma20_pct", "vs_ma50_pct", "from_high60_pct", "rsi14",
        "vol20_pct", "close_vs_vwap_pct", "vs_vwap20_pct", "stock_volume_spike", "shares_5d_avg", "log_price"]
MARKET = ["mkt_5d_pct", "mkt_20d_pct"]
NEWS = ["news_1d", "news_3d", "news_7d", "news_sent_7d", "quiet_spike"]
GROUPS = [("Options flow", FLOW), ("Technical analysis", TECH), ("Market", MARKET), ("News", NEWS),
          ("Flow + technical", FLOW + TECH), ("Everything", FLOW + TECH + MARKET + NEWS)]
SETTINGS = [(7, 100), (7, 300), (15, 100), (15, 300), (31, 100), (31, 300)]   # (leaves per tree, trees)


def build_rows(st):
    """One row per stock-day: the columns, the 10-session return, and where it belongs."""
    import news as N
    bundle = {r["ticker"]: int(r["bundle"]) for r in st.backend.read("bundles")}
    tickers = sorted(t for t, b in bundle.items() if b in K.TRAIN_BUNDLES)
    # Every calendar month through the end of 2026, so the final-exam months are marked as such and
    # the buffer keeps January 2026 outcomes from reaching into them.
    months = [f"{y}-{m:02d}" for y in (2024, 2025, 2026) for m in range(1, 13)]
    month_split = K.split_months(months)
    spy = K.market_closes()
    spy_dates = sorted(spy)
    spy_idx = {d: i for i, d in enumerate(spy_dates)}

    def mkt(d, n):
        i = spy_idx.get(d)
        return round((spy[d] / spy[spy_dates[i - n]] - 1) * 100, 2) if i is not None and i >= n else None

    nidx = N.Index(st, set(tickers)) if st.backend.read("news_fetched") else None
    rows = []
    for n, t in enumerate(tickers, 1):
        daily = [r for r in st.daily(t) if r.get("put_call_alpaca") not in (None, "")]
        if len(daily) < 60:
            continue
        scored = S.score_days({t: daily}, 30.0, 10)
        pos = {d["date"]: k for k, d in enumerate(scored)}
        dates = [r["date"] for r in daily]
        closes = [C.to_float(r["stock_close"]) for r in daily]
        series = {k: [C.to_float(r.get(k)) for r in daily] for k in
                  ("call_volume", "call_vol_long", "call_vol_otm", "put_volume", "stock_vwap", "stock_volume")}
        index = {d: i for i, d in enumerate(dates)}
        for d in scored:
            day = d["date"]
            split = K.split_of(day, month_split)
            if split not in ("train", "score"):
                continue
            i = index[day]
            if i + 11 >= len(dates) or not closes[i + 1] or not closes[i + 11]:
                continue
            f = {k: C.to_float(d.get(k)) for k in FLOW + TECH if k in d}
            f.update(A.technicals(closes, i))
            rets = [closes[k] / closes[k - 1] - 1 for k in range(max(1, i - 19), i + 1) if closes[k] and closes[k - 1]]
            f["vol20_pct"] = statistics.pstdev(rets) * 100 if len(rets) > 5 else None
            f.update(K.vwap_features(closes, series["stock_vwap"], series["stock_volume"], i))
            p = pos[day]
            last5, last20 = scored[max(0, p - 4):p + 1], scored[max(0, p - 19):p + 1]

            def avg(rows_, key):
                v = [C.to_float(x.get(key)) for x in rows_ if C.to_float(x.get(key)) is not None]
                return statistics.mean(v) if v else None
            f["calls_5d_avg"], f["puts_5d_avg"] = avg(last5, "call_volume_spike"), avg(last5, "put_volume_spike")
            f["shares_5d_avg"] = avg(last5, "stock_volume_spike")
            f["call_days_2x"] = sum(1 for x in last5 if (C.to_float(x.get("call_volume_spike")) or 0) >= 2)
            f["call_days_2x_20d"] = sum(1 for x in last20 if (C.to_float(x.get("call_volume_spike")) or 0) >= 2)
            back = scored[max(0, p - 60):p + 1][::-1]
            f["days_since_spike"] = next((k for k, x in enumerate(back)
                                          if (C.to_float(x.get("call_volume_spike")) or 0) >= 3), 60)
            for key, name in (("call_volume", "calls_20d"), ("call_vol_long", "long_calls_20d"),
                              ("call_vol_otm", "otm_calls_20d"), ("put_volume", "puts_20d")):
                f[name] = K.runway(series[key], i)
            f["mkt_5d_pct"], f["mkt_20d_pct"] = mkt(day, 5), mkt(day, 20)
            f["log_price"] = math.log(closes[i]) if closes[i] else None
            if nidx:
                f.update(nidx.features(t, day, d.get("call_volume_spike")))
            ret = (closes[i + 11] / closes[i + 1] - 1) * 100
            # Market sensitivity (beta) over the previous 60 sessions, and the market's return over the
            # same 10 sessions the stock is held.
            pairs = [(closes[k] / closes[k - 1] - 1, spy[dates[k]] / spy[dates[k - 1]] - 1)
                     for k in range(max(1, i - 59), i + 1)
                     if closes[k] and closes[k - 1] and dates[k] in spy and dates[k - 1] in spy]
            beta = 1.0
            if len(pairs) >= 30:
                ms = statistics.mean(p[1] for p in pairs)
                mv = statistics.mean((p[1] - ms) ** 2 for p in pairs)
                if mv > 0:
                    ss = statistics.mean(p[0] for p in pairs)
                    beta = statistics.mean((p[0] - ss) * (p[1] - ms) for p in pairs) / mv
                    beta = max(-1.0, min(4.0, beta))
            m0, m1 = spy.get(dates[i + 1]), spy.get(dates[i + 11])
            mret = (m1 / m0 - 1) * 100 if m0 and m1 else None
            rows.append({"ticker": t, "date": day, "week": A.week_of(day), "split": split, "ret": ret, "f": f,
                         "beta": beta, "mret": mret})
        if n % 100 == 0:
            print(f"  {n}/{len(tickers)} stocks, {len(rows):,} stock-days")
    # The outcome: the stock's return minus the average stock's return the same day.
    by_day = {}
    for r in rows:
        by_day.setdefault(r["date"], []).append(r["ret"])
    mean_day = {d: statistics.mean(v) for d, v in by_day.items()}
    for r in rows:
        r["excess"] = r["ret"] - mean_day[r["date"]]
    add_yardsticks(rows)
    return rows


def add_yardsticks(rows):
    """Two stricter yardsticks than 'beat the average stock':
    vol_excess: return minus the average stock of the SAME volatility (same tenth by 20-day volatility,
                same day). Picking jumpy stocks in a rising market earns nothing here.
    beta_excess: return minus what the stock's market sensitivity (beta) predicts from the market's move,
                 then minus the same-day average of that."""
    by_day = {}
    for r in rows:
        by_day.setdefault(r["date"], []).append(r)
    for items in by_day.values():
        have = sorted((r for r in items if r["f"].get("vol20_pct") is not None), key=lambda r: r["f"]["vol20_pct"])
        groups = {}
        for k, r in enumerate(have):
            groups.setdefault(min(9, k * 10 // len(have)), []).append(r)
        missing = [r for r in items if r["f"].get("vol20_pct") is None]
        if missing:
            groups[-1] = missing
        for g in groups.values():
            m = statistics.mean(r["ret"] for r in g)
            for r in g:
                r["vol_excess"] = r["ret"] - m
        b = [r["ret"] - r["beta"] * (r["mret"] if r["mret"] is not None else 0) for r in items]
        mb = statistics.mean(b)
        for r, v in zip(items, b):
            r["beta_excess"] = v - mb


def rank_corr(a, b):
    import numpy as np
    if len(a) < 3:
        return None
    ra = np.argsort(np.argsort(a))
    rb = np.argsort(np.argsort(b))
    c = np.corrcoef(ra, rb)[0, 1]
    return None if c != c else float(c)


def daily_scores(rows, preds, target="excess"):
    """Per day: rank correlation of prediction vs excess return; top tenth's excess and raw return."""
    by_day = {}
    for r, p in zip(rows, preds):
        by_day.setdefault(r["date"], []).append((p, r[target], r["ret"], r["week"], r["vol_excess"],
                                                 r["beta_excess"], r["f"].get("vol20_pct"), r["beta"]))
    out = []
    for d, items in sorted(by_day.items()):
        if len(items) < 20:
            continue
        items.sort(key=lambda x: -x[0])
        top = items[:max(2, len(items) // 10)]
        out.append({"date": d, "week": items[0][3],
                    "top_vol_excess": statistics.mean(x[4] for x in top),
                    "top_beta_excess": statistics.mean(x[5] for x in top),
                    "top_vol": statistics.mean(x[6] for x in top if x[6] is not None) if any(x[6] is not None for x in top) else None,
                    "all_vol": statistics.mean(x[6] for x in items if x[6] is not None) if any(x[6] is not None for x in items) else None,
                    "top_beta": statistics.mean(x[7] for x in top),
                    "ic": rank_corr([x[0] for x in items], [x[1] for x in items]),
                    "top_excess": statistics.mean(x[1] for x in top),
                    "top_ret": statistics.mean(x[2] for x in top),
                    "all_ret": statistics.mean(x[2] for x in items)})
    return [o for o in out if o["ic"] is not None]


def week_ci(days, key, reps=1000, seed=3):
    by_week = {}
    for o in days:
        by_week.setdefault(o["week"], []).append(o[key])
    weeks = list(by_week.values())
    if len(weeks) < 5:
        return None, None
    rng = random.Random(seed)
    sims = []
    for _ in range(reps):
        pick = [rng.choice(weeks) for _ in weeks]
        vals = [v for w in pick for v in w]
        sims.append(sum(vals) / len(vals))
    sims.sort()
    return sims[int(0.025 * reps)], sims[int(0.975 * reps) - 1]


def matrix(rows, cols):
    import numpy as np
    return np.array([[r["f"].get(c) if r["f"].get(c) is not None else float("nan") for c in cols] for r in rows],
                    dtype=float)


def fit(X, y, leaves, trees, seed=0):
    from sklearn.ensemble import HistGradientBoostingRegressor
    m = HistGradientBoostingRegressor(max_iter=trees, learning_rate=0.05, max_leaf_nodes=leaves,
                                      min_samples_leaf=200, l2_regularization=1.0, random_state=seed)
    m.fit(X, y)
    return m


def run(args):
    import numpy as np
    st = C.db()
    rows = build_rows(st)
    train = [r for r in rows if r["split"] == "train"]
    blind = [r for r in rows if r["split"] == "score"]
    if len(train) < args.min_rows or len(blind) < args.min_rows:
        sys.exit(f"Too little data: {len(train)} training and {len(blind)} blind stock-days.")
    # The check set for choosing settings: the latest fifth of the training weeks (training data only).
    tweeks = sorted({r["week"] for r in train})
    cut = tweeks[int(len(tweeks) * 0.8)]
    fit_part = [r for r in train if r["week"] < cut]
    check_part = [r for r in train if r["week"] >= cut]
    clip = lambda v: max(-50.0, min(50.0, v))   # a few 300% moves shouldn't dominate what is learned
    lines = [f"# Focused test ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
             f"Every stock-day with options data for bundles 1 to 6: **{len(train):,} training** and "
             f"**{len(blind):,} blind** stock-days, {len({r['ticker'] for r in rows}):,} stocks. The question: will "
             "the stock beat the average stock over the next 10 sessions (bought at the next session's close)?",
             "Settings were chosen on the latest fifth of the training weeks only; blind months were used once, "
             "to judge. Ranges are 95%, resampling whole weeks.", "",
             "Rank correlation compares the model's daily ranking of all stocks with what actually happened "
             "(0 = no skill; in professional stock selection, a steady 0.02 to 0.05 is considered valuable). "
             "Top tenth = the stocks the model liked most each day.", "",
             "| columns | settings chosen | check-set rank correlation | BLIND rank correlation (range) | "
             "blind days it was positive | top tenth vs average stock, % per 10 sessions (range) | top tenth raw return % |",
             "|---|---|---|---|---|---|---|"]
    summary = []
    kept = {}
    for name, cols in GROUPS:
        cols = [c for c in cols if any(r["f"].get(c) is not None for r in fit_part[:5000])]
        if not cols:
            continue
        Xf, yf = matrix(fit_part, cols), np.array([clip(r["excess"]) for r in fit_part])
        Xc = matrix(check_part, cols)
        best = None
        for leaves, trees in SETTINGS:
            preds = fit(Xf, yf, leaves, trees).predict(Xc)
            days = daily_scores(check_part, preds)
            ic = statistics.mean(o["ic"] for o in days) if days else -1
            if best is None or ic > best[0]:
                best = (ic, leaves, trees)
        ic_check, leaves, trees = best
        model = fit(matrix(train, cols), np.array([clip(r["excess"]) for r in train]), leaves, trees)
        days = daily_scores(blind, model.predict(matrix(blind, cols)))
        ic = statistics.mean(o["ic"] for o in days)
        lo, hi = week_ci(days, "ic")
        top = statistics.mean(o["top_excess"] for o in days)
        tlo, thi = week_ci(days, "top_excess")
        raw = statistics.mean(o["top_ret"] for o in days)
        pos = sum(1 for o in days if o["ic"] > 0)
        lines.append(f"| {name} ({len(cols)}) | {leaves} leaves, {trees} trees | {ic_check:+.3f} | {ic:+.3f} "
                     f"({lo:+.3f} to {hi:+.3f}) | {pos} of {len(days)} | {top:+.2f} ({tlo:+.2f} to {thi:+.2f}) | {raw:+.2f} |")
        summary.append((name, ic, lo, hi, top, tlo))
        kept[name] = (cols, leaves, trees, days)
        print(lines[-1])
    allr = statistics.mean(o["all_ret"] for o in days)
    real = [s for s in summary if s[2] is not None and s[2] > 0 and s[5] is not None and s[5] > 0]
    lines += ["", f"The average stock returned {allr:+.2f}% per 10 sessions in the blind months.", "",
              "## Verdict", "",
              f"({len(summary)} column groups were tested, so one passing narrowly could still be chance; a real signal",
              "should pass clearly and make sense alongside the others, e.g. 'Everything' should not be worse than its parts.)", ""]
    if real:
        lines += [f"- Signal found: {', '.join(s[0] for s in real)}: blind rank correlation and top-tenth excess "
                  "return both have their whole 95% range above zero. Worth testing with options next."]
    else:
        lines += ["- No column group's blind ranking skill was clearly above zero (whole 95% range above zero for both",
                  "  the rank correlation and the top tenth's excess return). With this much data, that is a strong",
                  "  sign these columns don't predict which stocks beat others over 10 sessions."]
    lines += volatility_check(train, blind, kept, clip)
    with open(os.path.join(C.ROOT, "FOCUSED.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    C.run_log("focused", "; ".join(f"{s[0]}: blind rank correlation {s[1]:+.3f}, top tenth {s[4]:+.2f}%"
                                   for s in summary))


def volatility_check(train, blind, kept, clip):
    """Is the top tenth's advantage just 'buy the jumpiest stocks in a rising market'?"""
    import numpy as np

    def rng(days, key):
        v = statistics.mean(o[key] for o in days)
        lo, hi = week_ci(days, key)
        if lo is None:
            return f"{v:+.2f}", v, None
        return f"{v:+.2f} ({lo:+.2f} to {hi:+.2f})", v, lo

    def vol_of(days, key):
        v = [o[key] for o in days if o[key] is not None]
        return f"{statistics.mean(v):.2f}" if v else "?"

    vol_only = daily_scores(blind, np.array([r["f"].get("vol20_pct") if r["f"].get("vol20_pct") is not None
                                             else -1.0 for r in blind]))
    out = ["", "## Is it just volatility?", "",
           "A model can beat the average stock in a rising market just by picking jumpy stocks. Three checks:",
           "",
           "1. **Volatility only:** each day, buy the tenth of stocks with the highest 20-day volatility. No model.",
           "2. **Same-volatility yardstick:** compare each pick with the average stock of the *same* volatility "
           "(same tenth by 20-day volatility, same day). Picking jumpy stocks earns nothing here.",
           "3. **Market-sensitivity yardstick:** subtract what the stock's market sensitivity (beta, from the "
           "previous 60 sessions) predicts from the market's move over the same 10 sessions.", "",
           "| top tenth chosen by | its 20-day volatility, % a day (all stocks) | its beta | vs average stock | "
           "vs same-volatility stocks | after market sensitivity |", "|---|---|---|---|---|---|"]
    rows_ = [("Volatility only (no model)", vol_only)] + [(n, k[3]) for n, k in kept.items()]
    for name, days in rows_:
        out.append(f"| {name} | {vol_of(days, 'top_vol')} ({vol_of(days, 'all_vol')}) | "
                   f"{statistics.mean(o['top_beta'] for o in days):.2f} | {rng(days, 'top_excess')[0]} | "
                   f"{rng(days, 'top_vol_excess')[0]} | {rng(days, 'top_beta_excess')[0]} |")
    out += ["", "All figures are % per 10 sessions, with 95% ranges resampling whole weeks.", "",
            "### Retrained to ignore volatility", "",
            "The same models trained on the same-volatility yardstick, so they get no credit for picking jumpy "
            "stocks and have to find something else. Same settings as above.", "",
            "| columns | BLIND rank correlation (range) | blind days positive | top tenth vs same-volatility stocks (range) |",
            "|---|---|---|---|"]
    passed = []
    for name in ("Options flow", "Technical analysis", "Flow + technical", "Everything"):
        if name not in kept:
            continue
        cols, leaves, trees, _ = kept[name]
        model = fit(matrix(train, cols), np.array([clip(r["vol_excess"]) for r in train]), leaves, trees)
        days = daily_scores(blind, model.predict(matrix(blind, cols)), target="vol_excess")
        ic = statistics.mean(o["ic"] for o in days)
        lo, hi = week_ci(days, "ic")
        top, tv, tlo = rng(days, "top_excess")
        pos = sum(1 for o in days if o["ic"] > 0)
        out.append(f"| {name} | {ic:+.3f} ({lo:+.3f} to {hi:+.3f}) | {pos} of {len(days)} | {top} |")
        print(out[-1])
        if lo is not None and tlo is not None and lo > 0 and tlo > 0:
            passed.append(name)
    out += ["", "### What this means", ""]
    base = rng(vol_only, "top_excess")[1]
    out.append(f"- Buying the most volatile tenth with no model beat the average stock by {base:+.2f}% per 10 sessions.")
    if passed:
        out.append(f"- After removing volatility, {', '.join(passed)} still ranked stocks better than chance with the "
                   "whole range above zero. That leftover is a real lead worth testing with options.")
    else:
        out.append("- After removing volatility, no column group could rank stocks with its whole range above zero. "
                   "The top tenth's advantage was volatility, not information.")
    C.run_log("focused-volatility", "passed: " + (", ".join(passed) or "none") + f"; volatility-only top tenth {base:+.2f}%")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--min-rows", type=int, default=1000)
    run(p.parse_args())


if __name__ == "__main__":
    main()
