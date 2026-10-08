"""
Open interest test with Databento (US options, OPRA): does a build-up of NEW option positions before a
day predict what happens next? Daily volume can't tell opening from closing trades; open interest can.

    python oi_test.py estimate          # free: checks the key and prices the plan, spends nothing
    python oi_test.py pull --max-cost 100
    python oi_test.py analyze           # writes OI_TEST.md
    python oi_test.py trades-check      # a few cents: does Databento mark which side started each trade?

Timing: OPRA publishes open interest before each session's open, and it reflects the previous close. So
the record published on the morning of the session AFTER a candidate day already counts that day's new
positions, and it is public before we would buy (we buy at the next session's price).

Needs the DATABENTO_API_KEY secret. New Databento accounts get $125 of free credit; every paid step
checks the price first and refuses to go over --max-cost.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import os
import statistics
import sys
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C  # noqa: E402
import committee as K  # noqa: E402
import agents as A     # noqa: E402

DATASET = "OPRA.PILLAR"
WINDOW = ("2024-02-01", "2026-02-01")     # training and blind months (the final-exam months stay untouched)


def client():
    import databento as db
    key = os.environ.get("DATABENTO_API_KEY", "")
    if not key:
        sys.exit("Set the DATABENTO_API_KEY secret first.")
    return db.Historical(key=key)


def sample(st, n):
    """A fixed random sample of pool stocks from the six training bundles, half from each list."""
    pool = K.load_pool(st)
    uni = {}
    for c in pool:
        if c["bundle"] in K.TRAIN_BUNDLES:
            uni.setdefault(c["ticker"], {"movers": 0, "wide": 0})
    for r in st.backend.read("pool"):
        if r["ticker"] in uni:
            uni[r["ticker"]][r.get("universe") or "movers"] += 1
    ranked = sorted(uni, key=lambda t: A.rank("oi-sample", t))
    movers = [t for t in ranked if uni[t]["movers"]][: n // 2]
    wide = [t for t in ranked if uni[t]["wide"]][: n - len(movers)]
    return movers + wide


def estimate(args):
    cl = client()
    st = C.db()
    try:
        rng = cl.metadata.get_dataset_range(dataset=DATASET)
    except Exception as ex:   # noqa: BLE001 - report the exact problem (bad key, no access)
        C.run_log("oi-estimate", f"Databento refused the request: {str(ex)[:300]}")
        sys.exit(1)
    tickers = sample(st, args.stocks)
    if not tickers:
        sys.exit("No pool stocks to sample.")
    probe = tickers[:args.probe]
    costs = {}
    for t in probe:
        try:
            costs[t] = cl.metadata.get_cost(dataset=DATASET, schema="statistics", symbols=[f"{t}.OPT"],
                                            stype_in="parent", start=WINDOW[0], end=WINDOW[1])
        except Exception as ex:   # noqa: BLE001
            C.run_log("oi-estimate", f"cost check failed for {t}: {str(ex)[:200]}")
    trades_month = {}
    for t in probe[:3]:
        try:
            trades_month[t] = cl.metadata.get_cost(dataset=DATASET, schema="trades", symbols=[f"{t}.OPT"],
                                                   stype_in="parent", start="2024-06-01", end="2024-07-01")
        except Exception as ex:   # noqa: BLE001
            C.run_log("oi-estimate", f"trades cost check failed for {t}: {str(ex)[:200]}")
    if not costs:
        sys.exit("No cost estimates came back.")
    per = sum(costs.values()) / len(costs)
    span = (f"{str(rng.get('start', '?'))[:10]} to {str(rng.get('end', '?'))[:10]}"
            if isinstance(rng, dict) else str(rng)[:80])
    msg = (f"key works; OPRA history {span}. "
           f"Open interest for {WINDOW[0]} to {WINDOW[1]}: "
           + ", ".join(f"{t} ${c:.2f}" for t, c in costs.items())
           + f"; about ${per:.2f} a stock, so ${per * len(tickers):.2f} for the {len(tickers)}-stock sample. "
           + ("Trades for one month (June 2024): " + ", ".join(f"{t} ${c:.2f}" for t, c in trades_month.items())
              if trades_month else ""))
    C.run_log("oi-estimate", msg)


OCC_TAIL = 15                              # YYMMDD + C/P + strike x 1000 (8 digits)
GAPS = (5, 20)                             # open interest compared with 5 and 20 sessions earlier
MAX_STOCK_COST = 3.0                       # skip stocks with huge chains; more stocks fit the budget


def parse_occ(sym):
    """'PRCT  240315C00050000' -> ('C', date(2024, 3, 15), 50.0)."""
    tail = (sym or "").strip()[-OCC_TAIL:]
    try:
        return tail[6], dt.date(2000 + int(tail[:2]), int(tail[2:4]), int(tail[4:6])), int(tail[7:]) / 1000
    except (ValueError, IndexError):
        return None


def needed_dates(st, tickers):
    """Per stock: for every training or blind candidate day, the session after it (its open interest
    covers the candidate day) and the sessions 5 and 20 before that."""
    pool = [c for c in K.load_pool(st) if c["split"] in ("train", "score") and c["bundle"] in K.TRAIN_BUNDLES]
    want = {}
    for t in tickers:
        days = sorted({c["date"] for c in pool if c["ticker"] == t})
        sessions = [r["date"] for r in st.daily(t) if C.to_float(r.get("stock_close"))]
        idx = {d: i for i, d in enumerate(sessions)}
        dates = set()
        for d in days:
            i = idx.get(d)
            if i is None or i + 1 >= len(sessions):
                continue
            for back in (0,) + GAPS:
                if i + 1 - back >= 0:
                    dates.add(sessions[i + 1 - back])
        want[t] = sorted(dates)
    return want


def pull(args):
    st = C.db()
    cl = client()
    tickers = sample(st, args.stocks)
    have = {(r["ticker"], str(r["date"])) for r in st.backend.read("oi_daily")}
    want = needed_dates(st, tickers)
    plan, total = [], 0.0
    full_days = 500   # trading days in the cost-check window
    for t in tickers:
        dates = [d for d in want.get(t, []) if (t, d) not in have]
        if not dates:
            continue
        try:
            full = cl.metadata.get_cost(dataset=DATASET, schema="statistics", symbols=[f"{t}.OPT"],
                                        stype_in="parent", start=WINDOW[0], end=WINDOW[1])
        except Exception as ex:   # noqa: BLE001
            C.run_log("oi-pull", f"cost check failed for {t}: {str(ex)[:150]}")
            continue
        est = full / full_days * len(dates)
        if est > MAX_STOCK_COST:
            continue
        if total + est > args.max_cost:
            break
        plan.append((t, dates, est))
        total += est
    C.run_log("oi-pull", f"plan: {len(plan)} stocks, {sum(len(d) for _, d, _ in plan):,} stock-days, "
                         f"estimated ${total:.2f} (cap ${args.max_cost:.0f}).")
    if args.dry_run:
        return
    lock, done, spent = threading.Lock(), [0], [0.0]
    # Read everything from the database up front: the download threads must not share its connection.
    closes = {t: {r["date"]: C.to_float(r.get("stock_close")) for r in st.daily(t)} for t, _, _ in plan}

    def one(item):
        t, dates, est = item
        c2 = client()
        rows = []
        for d in dates:
            nxt = (dt.date.fromisoformat(d) + dt.timedelta(days=1)).isoformat()
            try:
                df = c2.timeseries.get_range(dataset=DATASET, schema="statistics", symbols=[f"{t}.OPT"],
                                             stype_in="parent", start=d, end=nxt).to_df()
            except Exception as ex:   # noqa: BLE001
                with lock:
                    C.log_error({"ticker": t, "event_date": f"oi {d}"}, ex)
                continue
            if df is None or df.empty:
                continue
            df = df[df["stat_type"] == 9]                     # open interest records
            # The record published this morning is as of the PREVIOUS session's close.
            sess = sorted(x for x in closes[t] if x < d)
            asof = sess[-1] if sess else d
            close = closes[t].get(asof)
            agg = {"call_oi": 0, "put_oi": 0, "call_oi_otm": 0, "call_oi_long": 0, "call_oi_short": 0}
            seen = set()
            for sym, q in zip(df["symbol"], df["quantity"]):
                if sym in seen:
                    continue                                    # one figure per contract per day
                seen.add(sym)
                occ = parse_occ(sym)
                if not occ or q is None:
                    continue
                kind, exp, strike = occ
                q = int(q)
                if kind == "P":
                    agg["put_oi"] += q
                    continue
                agg["call_oi"] += q
                days_left = (exp - dt.date.fromisoformat(asof)).days
                if close and strike >= close * 1.05:
                    agg["call_oi_otm"] += q
                if days_left > 60:
                    agg["call_oi_long"] += q
                elif days_left <= 14:
                    agg["call_oi_short"] += q
            rows.append(dict(agg, ticker=t, date=asof, contracts=len(seen)))
        with lock:
            st.backend.upsert("oi_daily", rows)
            done[0] += 1
            spent[0] += est
            if done[0] % 10 == 0:
                print(f"  {done[0]}/{len(plan)} stocks, about ${spent[0]:.2f}")
    with cf.ThreadPoolExecutor(6) as ex:
        list(ex.map(one, plan))
    C.run_log("oi-pull", f"done: {done[0]} stocks, about ${spent[0]:.2f} of credit used.")


def analyze(args):
    """For candidate days of the sampled stocks: does open interest growth before the day predict
    what the stock (and a 30-day call) did next? Training and blind months reported separately."""
    st = C.db()
    oi = {}
    for r in st.backend.read("oi_daily"):
        oi.setdefault(r["ticker"], {})[str(r["date"])] = r
    pool = [c for c in K.load_pool(st) if c["ticker"] in oi and c["split"] in ("train", "score")
            and c["bundle"] in K.TRAIN_BUNDLES]
    if not pool:
        sys.exit("No open interest yet: run pull first.")
    feats = []
    sessions_of = {t: [r["date"] for r in st.daily(t)] for t in {c["ticker"] for c in pool}}
    index_of = {t: {d: i for i, d in enumerate(v)} for t, v in sessions_of.items()}
    for c in pool:
        if c["date"] not in oi[c["ticker"]]:
            continue
        cur = oi[c["ticker"]][c["date"]]
        row = {"c": c}
        for gap in GAPS:
            prev = None
            j = index_of[c["ticker"]].get(c["date"], -1) - gap
            if j >= 0:
                prev = oi[c["ticker"]].get(sessions_of[c["ticker"]][j])
            for k in ("call_oi", "call_oi_otm", "call_oi_long", "call_oi_short", "put_oi"):
                a_, b_ = C.to_float(cur.get(k)), C.to_float(prev.get(k)) if prev else None
                row[f"{k}_chg{gap}"] = (a_ / b_ - 1) * 100 if a_ is not None and b_ else None
        po, co = C.to_float(cur.get("put_oi")), C.to_float(cur.get("call_oi"))
        row["put_call_oi"] = po / co if po is not None and co else None
        feats.append(row)
    lines = [f"# Open interest test ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
             f"{len(oi)} stocks with Databento open interest; {len(feats):,} candidate days with it. "
             "Open interest after the candidate day versus 5 and 20 sessions earlier (new positions opened). "
             "Each row splits candidate days into fifths by that measure and shows the top fifth against all "
             "days: the stock's next-10-session return and a 30-day at-the-money call held 10 sessions "
             "(realistic costs). Ranges are 95%, resampling whole weeks.", ""]
    measures = [k for k in feats[0] if k != "c"] if feats else []
    for split in ("train", "score"):
        rows = [f for f in feats if f["c"]["split"] == split]
        lines += [f"## {'Training months' if split == 'train' else 'Blind months (never used to choose anything)'}"
                  f" ({len(rows):,} days)", "",
                  "| measure | top fifth threshold | stock: top fifth % (range) | stock: all % | call: top fifth % | call: all % | days |",
                  "|---|---|---|---|---|---|---|"]
        for m in measures:
            vals = [(f[m], f["c"]) for f in rows if f[m] is not None]
            if len(vals) < 50:
                continue
            vals.sort(key=lambda x: x[0])
            cut = vals[int(len(vals) * 0.8)][0]
            top = [c for v, c in vals if v >= cut]
            allc = [c for _, c in vals]
            sh_t = [(c["week"], c["shares"]) for c in top]
            lo, hi = K.boot_ci(sh_t)
            call = lambda cs: [A.trade_return(c, "call", 30, 0.0, "hold10") for c in cs]
            ct = [x for x in call(top) if x is not None]
            ca = [x for x in call(allc) if x is not None]
            rng = f" ({lo:+.1f} to {hi:+.1f})" if lo is not None else ""
            lines.append(f"| {m} | {cut:.2f} | {statistics.mean([x for _, x in sh_t]):+.2f}{rng} | "
                         f"{statistics.mean(c['shares'] for c in allc):+.2f} | "
                         f"{statistics.mean(ct):+.1f} | {statistics.mean(ca):+.1f} | {len(top)} |"
                         if ct and ca else f"| {m} | {cut:.2f} | - | - | - | - | {len(top)} |")
        lines.append("")
    lines += ["Read it this way: a measure matters only if its top fifth beats 'all' in the training months AND",
              "again in the blind months, with the range clear of the 'all' figure. Many measures are tested here, so",
              "one or two will look good by chance."]
    with open(os.path.join(C.ROOT, "OI_TEST.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))
    C.run_log("oi-analyze", f"OI_TEST.md written: {len(feats):,} candidate days from {len(oi)} stocks.")


def trades_check(args):
    """One month of individual option trades for a few stocks: which 'side' values appear?"""
    cl = client()
    st = C.db()
    out = []
    for t in sample(st, 60)[:3]:
        try:
            df = cl.timeseries.get_range(dataset=DATASET, schema="trades", symbols=[f"{t}.OPT"], stype_in="parent",
                                         start="2024-06-03", end="2024-06-08").to_df()
        except Exception as ex:   # noqa: BLE001
            out.append(f"{t}: failed {str(ex)[:120]}")
            continue
        sides = df["side"].value_counts().to_dict() if "side" in df else {}
        out.append(f"{t}: {len(df):,} trades, side values {sides}")
    C.run_log("oi-trades-check", "; ".join(out))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("estimate")
    e.add_argument("--stocks", type=int, default=60)
    e.add_argument("--probe", type=int, default=6, help="how many stocks to price individually")
    pl = sub.add_parser("pull")
    pl.add_argument("--stocks", type=int, default=300)
    pl.add_argument("--max-cost", type=float, default=100)
    pl.add_argument("--dry-run", action="store_true")
    sub.add_parser("analyze")
    sub.add_parser("trades-check")
    a = p.parse_args()
    {"estimate": estimate, "pull": pull, "analyze": analyze, "trades-check": trades_check}[a.cmd](a)


if __name__ == "__main__":
    main()
