"""
Open interest test with Databento (US options, OPRA): does a build-up of NEW option positions before a
day predict what happens next? Daily volume can't tell opening from closing trades; open interest can.

    python oi_test.py estimate          # free: checks the key and prices the plan, spends nothing

Needs the DATABENTO_API_KEY secret. New Databento accounts get $125 of free credit; every paid step
checks the price first and refuses to go over --max-cost.
"""
import argparse
import os
import sys

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


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("estimate")
    e.add_argument("--stocks", type=int, default=60)
    e.add_argument("--probe", type=int, default=6, help="how many stocks to price individually")
    a = p.parse_args()
    {"estimate": estimate}[a.cmd](a)


if __name__ == "__main__":
    main()
