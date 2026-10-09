"""
A plain machine learning benchmark for the trader agents to beat.

    python benchmark.py                 # writes BENCHMARK.md

It sees exactly what the agents see: the same candidates, the same columns, the same training months.
It is judged exactly like them: on the blind scoring months, trading up to 3 picks per bundle per week,
with the same costs, against a random picker making the same number and kind of trades.

The model is a gradient-boosted tree ensemble (scikit-learn's HistGradientBoostingRegressor) with fixed,
ordinary settings: nothing is tuned on the blind months. Each row is one candidate paired with one way to
trade it (the stock, or one of the 30 call choices), and the model predicts that trade's 10-session
return from the columns plus the trade's expiry, strike, exit and cost. Each week it takes the trades it
expects to earn the most, at most one per stock, and only if it expects a profit.

If this model finds no edge in the blind months, the agents probably won't either. If it does, the
committee's job is to beat it.
"""
import argparse
import datetime as dt
import os
import random
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C  # noqa: E402
import agents as A     # noqa: E402
import committee as K  # noqa: E402

PRICE_BAND = {"<$10": 0, "$10-50": 1, ">$50": 2}
NUMERIC = [k for k, _, _ in A.FEATURES if k != "price_band"]


def instruments(options_only):
    out = [] if options_only else [("stock", None, None, None)]
    for e in A.EXPIRIES:
        for s in A.STRIKES:
            for x in A.EXITS:
                out.append(("call", e, s, x))
    return out


def row_features(c, inst):
    f = c["f"]
    vals = [C.to_float(f.get(k)) for k in NUMERIC]
    vals.append(PRICE_BAND.get(f.get("price_band")))
    kind, e, s, x = inst
    cost = None
    if kind == "call":
        o = c["o"].get(f"{e}d+{float(s):g}") or {}
        cost = o.get("cost_pct")
    vals += [0 if kind == "stock" else 1, e or 0, s or 0, 1 if x == "double_or_10" else 0, cost]
    return [float("nan") if v is None else float(v) for v in vals]


def target(c, inst):
    kind, e, s, x = inst
    return A.trade_return(c, kind, e, s, x)


def dataset(cands, insts):
    X, y, keys = [], [], []
    for c in cands:
        for inst in insts:
            r = target(c, inst)
            if r is None:
                continue
            X.append(row_features(c, inst))
            y.append(r)
            keys.append((c, inst))
    return X, y, keys


def trade_weeks(keys, preds, max_picks=3):
    """Per bundle-week: the best predicted trades, one per stock, only if predicted to profit."""
    groups = {}
    for (c, inst), p in zip(keys, preds):
        groups.setdefault((c["bundle"], c["week"]), []).append((p, c, inst))
    trades, weeks = [], []
    for (b, wk), items in sorted(groups.items()):
        cands = list({id(c): c for _, c, _ in items}.values())
        wi = len(weeks)
        weeks.append(cands)
        used = set()
        for p, c, inst in sorted(items, key=lambda t: -t[0]):
            if p <= 0 or len(used) >= max_picks:
                break
            if c["ticker"] in used:
                continue
            used.add(c["ticker"])
            kind, e, s, x = inst
            trades.append({"week_index": wi, "week": wk, "action": kind, "expiry": e, "strike_pct": s,
                           "exit_rule": x, "ret_pct": target(c, inst), "ticker": c["ticker"]})
    return trades, weeks


def summarize(name, trades, weeks):
    rets = [t["ret_pct"] for t in trades]
    if not rets:
        return {"name": name, "trades": 0}
    lo, hi = K.boot_ci([(t["week"], t["ret_pct"]) for t in trades])
    bm, _, bw = A.random_baseline(weeks, trades)
    kinds = {}
    for t in trades:
        kinds[A.describe_pick(t)] = kinds.get(A.describe_pick(t), 0) + 1
    return {"name": name, "trades": len(rets), "profit": round(sum(rets) * A.TRADE_USD / 100),
            "mean": round(statistics.mean(rets), 2), "median": round(statistics.median(rets), 2),
            "win": round(100 * sum(r > 0 for r in rets) / len(rets), 1), "ci": (lo, hi),
            "random_mean": bm, "random_profit": round(bm * len(rets) * A.TRADE_USD / 100) if bm is not None else None,
            "random_win": bw, "top_kinds": sorted(kinds.items(), key=lambda kv: -kv[1])[:4]}


def spearman(a, b):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        for pos, i in enumerate(order):
            r[i] = pos
        return r
    ra, rb = ranks(a), ranks(b)
    ma, mb = statistics.mean(ra), statistics.mean(rb)
    num = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    den = (sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb)) ** 0.5
    return num / den if den else 0.0


def make_model(kind, seed):
    from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
    from sklearn.impute import SimpleImputer
    from sklearn.linear_model import Ridge
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    if kind == "gradient boosting":
        return HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=15, min_samples_leaf=50,
                                             l2_regularization=1.0, max_features=0.7, random_state=seed)
    if kind == "random forest":
        return RandomForestRegressor(n_estimators=100, max_depth=8, min_samples_leaf=50, max_features=0.5,
                                     n_jobs=-1, random_state=seed)
    return make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), Ridge(alpha=10.0))


def multi_runs(train, blind, runs):
    """Many versions of each model: each trained on a different random resample of the training WEEKS
    (and, for the tree models, a different random subset of columns per split). A real edge should show
    up in most versions; luck shows up as a wide spread around the random picker."""
    import numpy as np
    out = ["", f"## Multiple runs ({runs} per model)", "",
           "Each run trains on a different random resample of the training weeks (whole weeks, with repeats).",
           "The blind months and the random comparison are the same for every run.", "",
           "| model | instruments | runs | median average % | lowest to highest | beat random same-trades | made money | median stock ranking |",
           "|---|---|---|---|---|---|---|---|"]
    total_beat = total_runs = 0
    for label, options_only in (("stock or calls", False), ("calls only", True)):
        insts = instruments(options_only)
        X, y, keys = dataset(train, insts)
        keep = [j for j in range(len(X[0])) if any(row[j] == row[j] for row in X)]
        X = np.array([[row[j] for j in keep] for row in X], dtype=float)
        y = np.clip(np.array(y, dtype=float), -100.0, 300.0)
        week_rows = {}
        for i, (c, _) in enumerate(keys):
            week_rows.setdefault(c["week"], []).append(i)
        weeks = sorted(week_rows)
        Xb, _, bkeys = dataset(blind, insts)
        Xb = np.array([[row[j] for j in keep] for row in Xb], dtype=float)
        for kind in ("gradient boosting", "random forest", "linear"):
            avgs, beats, profits, ranks = [], 0, 0, []
            for r in range(runs):
                rng = random.Random(f"run-{r}")
                idx = [i for w in (rng.choice(weeks) for _ in weeks) for i in week_rows[w]]
                model = make_model(kind, r)
                model.fit(X[idx], y[idx])
                preds = model.predict(Xb)
                trades, wks = trade_weeks(bkeys, preds)
                s = summarize("", trades, wks)
                if not s["trades"]:
                    avgs.append(0.0)
                    continue
                avgs.append(s["mean"])
                beats += s["random_mean"] is not None and s["mean"] > s["random_mean"]
                profits += s["mean"] > 0
                if not options_only:
                    sk = [(c, p) for (c, inst), p in zip(bkeys, preds) if inst[0] == "stock"]
                    if sk:
                        ranks.append(spearman([p for _, p in sk], [c["shares"] for c, _ in sk]))
            total_beat += beats
            total_runs += runs
            med_rank = f"{statistics.median(ranks):+.3f}" if ranks else "-"
            out.append(f"| {kind} | {label} | {runs} | {statistics.median(avgs):+.1f} | {min(avgs):+.1f} to "
                       f"{max(avgs):+.1f} | {beats} of {runs} | {profits} of {runs} | {med_rank} |")
            print(out[-1])
    out += ["", f"Across all {total_runs} runs, {total_beat} beat the random picker making the same trades. With no edge",
            "at all, about half would by chance. A real edge would show most runs of every model beating random AND",
            "making money, with stock rankings clearly above zero."]
    C.run_log("benchmark-runs", f"{total_beat} of {total_runs} model runs beat the random same-trades picker.")
    return out


def run(args):
    from sklearn.ensemble import HistGradientBoostingRegressor
    st = C.db()
    pool = K.load_pool(st)
    train = [c for c in pool if c["split"] == "train" and c["bundle"] in K.TRAIN_BUNDLES]
    blind = [c for c in pool if c["split"] == "score" and c["bundle"] in K.TRAIN_BUNDLES]
    if not train or not blind:
        sys.exit("The pool has no training or scoring candidates; build it first.")
    lines = [f"# Machine learning benchmark ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
             f"Training candidates: {len(train):,}. Blind scoring candidates: {len(blind):,}. "
             "Same columns, months, costs and pick limits as the agents; nothing tuned on the blind months.",
             "Ranges are 95%, resampling whole weeks. Every trade is $1,000.", ""]
    results = []
    for label, options_only in (("Stock or calls", False), ("Calls only", True)):
        insts = instruments(options_only)
        X, y, _ = dataset(train, insts)
        model = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=15,
                                              min_samples_leaf=50, l2_regularization=1.0, random_state=0)
        # Option returns have huge outliers (+1,000%); clip the target so a few lottery wins don't
        # dominate what the model learns. Profits below are still measured unclipped.
        # Columns that are blank for every training row (e.g. data added after these months) carry
        # nothing to learn from; drop them, the same way for training and blind rows.
        keep = [j for j in range(len(X[0])) if any(row[j] == row[j] for row in X)]
        X = [[row[j] for j in keep] for row in X]
        model.fit(X, [max(-100.0, min(300.0, v)) for v in y])
        Xb, yb, keys = dataset(blind, insts)
        preds = model.predict([[row[j] for j in keep] for row in Xb])
        trades, weeks = trade_weeks(keys, preds)
        s = summarize(f"Model, {label.lower()}", trades, weeks)
        results.append(s)
        # Does the model at least rank stocks sensibly? Predicted vs actual 10-session stock return.
        if not options_only:
            sk = [(c, p) for (c, inst), p in zip(keys, preds) if inst[0] == "stock"]
            rho = spearman([p for _, p in sk], [c["shares"] for c, _ in sk]) if sk else None
            s["stock_rank_corr"] = round(rho, 3) if rho is not None else None
        # Simple yardsticks on the same blind weeks.
        if not options_only:
            every = [{"week_index": 0, "week": c["week"], "action": "stock", "expiry": None, "strike_pct": None,
                      "exit_rule": None, "ret_pct": c["shares"], "ticker": c["ticker"]} for c in blind]
            results.append(summarize("Buy every candidate's stock", every, [blind]))
        rng = random.Random(1)
        rand = []
        groups = {}
        for c in blind:
            groups.setdefault((c["bundle"], c["week"]), []).append(c)
        rweeks = []
        for key in sorted(groups):
            cs = groups[key]
            wi = len(rweeks)
            rweeks.append(cs)
            for c in rng.sample(cs, min(3, len(cs))):
                inst = rng.choice(insts)
                r = target(c, inst)
                if r is not None:
                    rand.append({"week_index": wi, "week": c["week"], "action": inst[0], "expiry": inst[1],
                                 "strike_pct": inst[2], "exit_rule": inst[3], "ret_pct": r, "ticker": c["ticker"]})
        results.append(summarize(f"Random picks, {label.lower()}", rand, rweeks))
    lines += ["| strategy | trades | profit $ | average % (95% range) | median % | win % | random same-trades profit $ |",
              "|---|---|---|---|---|---|---|"]
    for s in results:
        if not s["trades"]:
            lines.append(f"| {s['name']} | 0 | - | - | - | - | - |")
            continue
        ci = f"{s['mean']:+.1f} ({s['ci'][0]:+.1f} to {s['ci'][1]:+.1f})" if s["ci"][0] is not None else f"{s['mean']:+.1f}"
        lines.append(f"| {s['name']} | {s['trades']} | {s['profit']:+,} | {ci} | {s['median']:+.1f} | {s['win']} | "
                     f"{s['random_profit']:+,} |" if s.get("random_profit") is not None else
                     f"| {s['name']} | {s['trades']} | {s['profit']:+,} | {ci} | {s['median']:+.1f} | {s['win']} | - |")
    lines.append("")
    for s in results:
        if s.get("stock_rank_corr") is not None:
            lines.append(f"- How well the model ranks stocks (predicted vs actual 10-session return, 0 = no skill): "
                         f"{s['stock_rank_corr']}")
        if s["name"].startswith("Model") and s.get("top_kinds"):
            lines.append(f"- {s['name']} mostly traded: " + ", ".join(f"{k} ({n})" for k, n in s["top_kinds"]))
    lines += ["", "Read it this way: the model has an edge only if its average beats the random same-trades",
              "picker AND the bottom of its 95% range is above that. The agents' blind runs should be compared",
              "with the model's line for the same instruments."]
    if getattr(args, "runs", 0):
        lines += multi_runs(train, blind, args.runs)
    with open(os.path.join(C.ROOT, "BENCHMARK.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    m = next(s for s in results if s["name"].startswith("Model"))
    C.run_log("benchmark", f"model (stock or calls) on blind months: {m['trades']} trades, average "
                           f"{m.get('mean')}%, range {m.get('ci')}, random same-trades {m.get('random_mean')}%.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--runs", type=int, default=20, help="versions of each model to train (0 = the single run only)")
    run(p.parse_args())


if __name__ == "__main__":
    main()
