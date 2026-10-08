"""
Ladder backtest: would buying calls after a flag actually have made money, and which ones?

For every historical flag day (and an equal number of random non-flag "control" days on the
same stocks), pretend to buy the same grid of call options the next trading day:
    5 strikes:     at the money, then 5%, 10%, 15%, 20% above the stock price
    3 expirations: the listed expirations nearest to 14, 30 and 90 days out
Each contract is then followed day by day using Alpaca's daily option prices, and scored under
three exit rules:
    hold10        sell after 10 trading sessions (or at expiration if sooner)
    double_or_10  sell the first day it is worth 2x what you paid, otherwise after 10 sessions
    expiry        hold to expiration, worth whatever the stock is above the strike
Costs: you pay SPREAD_COST above the price you see when buying and get SPREAD_COST below it when
selling, because past data has trade prices, not the bid and ask.

Comparing flag ladders with control ladders shows whether any profit comes from the signal or
would have happened buying calls on any random day.

    python ladder.py                   # run (resumable), then print and save the report
    python ladder.py --report-only     # just rebuild the report from trades already recorded

Results go to the ladder_trades and ladder_report tables.
"""
import argparse
import datetime as dt
import os
import random
import statistics
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # find the modules next to this file
import collector as C  # noqa: E402
import scorer as S     # noqa: E402

TARGET_DTES = (14, 30, 90)
TARGET_OTM = (0.0, 5.0, 10.0, 15.0, 20.0)
SPREAD_COST = 0.05        # 5% worse than the printed price on each side of the trade
HOLD_SESSIONS = 10
TAKE_PROFIT = 2.0
MIN_DTE = 7
STATUS_FILE = os.path.join(C.ROOT, "ladder_status.txt")
MIN_SECONDS_BETWEEN_REQUESTS = 2.0   # 30 a minute, so it fits beside the backfill on one Alpaca key


def pick_contracts(contracts, signal_date, stock_close):
    """The 15 calls in the grid: nearest listed expiration to each target, nearest strike to each target."""
    d0 = dt.date.fromisoformat(signal_date)
    calls = [c for c in contracts.values() if c["type"] == "call"
             and C.STANDARD_OPTION_SYMBOL.match(c["symbol"])]
    expiries = sorted({c["expiration_date"] for c in calls
                       if (dt.date.fromisoformat(c["expiration_date"]) - d0).days >= MIN_DTE})
    picked = []
    for target in TARGET_DTES:
        if not expiries:
            break
        exp = min(expiries, key=lambda e: abs((dt.date.fromisoformat(e) - d0).days - target))
        strikes = sorted({float(c["strike_price"]) for c in calls if c["expiration_date"] == exp})
        for otm in TARGET_OTM:
            want = stock_close * (1 + otm / 100)
            k = min(strikes, key=lambda s: abs(s - want))
            sym = next(c["symbol"] for c in calls
                       if c["expiration_date"] == exp and float(c["strike_price"]) == k)
            picked.append({"contract": sym, "target_dte": target, "target_otm_pct": otm, "strike": k,
                           "expiration": exp, "dte": (dt.date.fromisoformat(exp) - d0).days})
    return picked


def simulate(trade, bars, dates, closes, entry_idx):
    """Fill in entry, the three exit-rule returns and the 10-session peak for one contract."""
    entry_date = dates[entry_idx]
    by_day = {b["t"][:10]: b for b in bars}
    eb = by_day.get(entry_date)
    trade["entry_date"] = entry_date
    if not eb or not eb.get("v"):
        trade["filled"] = "no"          # nothing traded that day: you couldn't have bought it
        return trade
    entry = (eb.get("vw") or eb["c"]) * (1 + SPREAD_COST)
    trade.update(filled="yes", entry_price=round(entry, 4))
    k, exp = trade["strike"], trade["expiration"]
    last, values = eb["c"], []
    expired = dates[-1] >= exp                   # the data runs past expiration
    last_session = max(x for x in dates if x <= exp) if any(x <= exp for x in dates) else None
    for j in range(entry_idx, len(dates)):
        d = dates[j]
        if d > exp:
            break
        b = by_day.get(d)
        if b and b.get("v"):
            last = b["c"]
        intrinsic = max(0.0, (closes.get(d) or 0) - k)
        if expired and d == last_session:
            values.append((d, intrinsic))          # at expiration it's worth exactly its intrinsic value
        else:
            values.append((d, max(last, intrinsic)))   # never worth less than intrinsic before then
    sell = lambda v: v * (1 - SPREAD_COST)
    pct = lambda v: round((sell(v) / entry - 1) * 100, 2)
    window = values[1:HOLD_SESSIONS + 1]
    if len(window) >= HOLD_SESSIONS or expired:
        hold_value = window[-1][1] if window else values[-1][1]
        trade["ret_hold10_pct"] = pct(hold_value)
        hit = next((v for _, v in window if sell(v) >= TAKE_PROFIT * entry), None)
        trade["ret_double_or_10_pct"] = pct(hit) if hit is not None else pct(hold_value)
        trade["peak_10_pct"] = pct(max(v for _, v in window)) if window else pct(hold_value)
    exp_close = [closes.get(d) for d in dates if d <= exp and closes.get(d)]
    if expired and exp_close:               # expiration has passed: settle at intrinsic value
        payoff = max(0.0, exp_close[-1] - k)
        trade["ret_expiry_pct"] = round((payoff / entry - 1) * 100, 2)
    return trade


def choose_days(days, seed=7):
    """Flag days (any shortlist rule fired) and the same number of random non-flag days."""
    flags, quiet = [], []
    for d in days:
        fired = [name for name in S.FLAG_RULES if S.RULES[name](d)]
        (flags if fired else quiet).append((d, fired))
    rng = random.Random(seed)
    controls = rng.sample(quiet, min(len(flags), len(quiet)))
    return [(d, "flag", ", ".join(f)) for d, f in flags] + [(d, "control", "") for d, _ in controls]


def run(args):
    C.MIN_SECONDS_BETWEEN_REQUESTS = MIN_SECONDS_BETWEEN_REQUESTS
    st = C.db()
    deadline = time.monotonic() + 60 * args.max_minutes
    data = S.load(st)
    days = S.score_days(data, 30.0, HOLD_SESSIONS)
    plan = choose_days(days)
    done = {(r["grp"], r["ticker"], r["signal_date"]) for r in st.backend.read("ladder_trades")}
    todo = [p for p in plan if (p[1], p[0]["ticker"], p[0]["date"]) not in done]
    todo.sort(key=lambda p: (p[0]["ticker"], p[0]["date"]))   # one stock at a time: contracts load once
    print(f"Ladder: {len(plan)} days planned ({sum(1 for p in plan if p[1] == 'flag')} flags), "
          f"{len(plan) - len(todo)} done, {len(todo)} to go.")
    contracts_cache = {}
    today = dt.date.today().isoformat()
    finished = True
    for n, (d, grp, rules) in enumerate(todo, 1):
        if time.monotonic() > deadline:
            finished = False
            break
        t = d["ticker"]
        rows = data[t]
        dates = [r["date"] for r in rows]
        closes = {r["date"]: C.to_float(r["stock_close"]) for r in rows}
        i = dates.index(d["date"])
        if i + 1 >= len(dates):
            continue                               # no next session yet to buy in
        try:
            if t not in contracts_cache:
                contracts_cache = {t: C.option_contracts(t, C.ALPACA_HISTORY_START,
                                                         C.add_days(today, C.MAX_EXPIRY_DAYS))}
            picked = pick_contracts(contracts_cache[t], d["date"], d["close"])
            if not picked:
                continue
            last_exp = max(p["expiration"] for p in picked)
            pages = C.alpaca_get("https://data.alpaca.markets", "/v1beta1/options/bars",
                                 {"symbols": ",".join(sorted({p["contract"] for p in picked})),
                                  "timeframe": "1Day", "start": dates[i + 1],
                                  "end": C.safe_end(min(last_exp, today)), "limit": 10000})
            bars = {}
            for page in pages:
                for sym, bs in (page.get("bars") or {}).items():
                    bars.setdefault(sym, []).extend(bs)
            out = []
            for p in picked:
                tr = dict(p, grp=grp, rules=rules, ticker=t, signal_date=d["date"], stock_close=d["close"])
                out.append(simulate(tr, bars.get(p["contract"], []), dates, closes, i + 1))
            st.backend.upsert("ladder_trades", out)
        except Exception as ex:
            C.log_error({"ticker": t, "event_date": f"ladder {d['date']}"}, ex)
            print(f"  {t} {d['date']} FAILED: {str(ex)[:150]}")
            continue
        if n % 25 == 0:
            print(f"  {n}/{len(todo)} days done")
    with open(STATUS_FILE, "w") as f:
        f.write("done" if finished else "more")
    print("Ladder complete." if finished else "Ladder not finished; another round needed.")


def report(args):
    st = C.db()
    trades = [r for r in st.backend.read("ladder_trades") if r["filled"] == "yes"]
    allt = st.backend.read("ladder_trades")
    if not allt:
        print("No ladder trades yet.")
        return
    fill = {g: (sum(1 for r in allt if r["grp"] == g and r["filled"] == "yes"),
                sum(1 for r in allt if r["grp"] == g)) for g in ("flag", "control")}
    print(f"Fill rate (contract actually traded on the entry day): "
          + ", ".join(f"{g} {a}/{b}" for g, (a, b) in fill.items()))
    rows = []
    run_date = dt.date.today().isoformat()
    for rule, col in (("hold10", "ret_hold10_pct"), ("double_or_10", "ret_double_or_10_pct"),
                      ("expiry", "ret_expiry_pct")):
        for grp in ("flag", "control"):
            for dte in TARGET_DTES:
                for otm in TARGET_OTM:
                    vals = [float(r[col]) for r in trades if r["grp"] == grp and r[col] != ""
                            and int(r["target_dte"]) == dte and float(r["target_otm_pct"]) == otm]
                    peaks = [float(r["peak_10_pct"]) for r in trades if r["grp"] == grp
                             and r["peak_10_pct"] != "" and int(r["target_dte"]) == dte
                             and float(r["target_otm_pct"]) == otm]
                    if len(vals) < 5:
                        continue
                    rows.append({"run_date": run_date, "grp": grp, "target_dte": dte,
                                 "target_otm_pct": otm, "exit_rule": rule, "trades": len(vals),
                                 "win_rate_pct": round(100 * sum(v > 0 for v in vals) / len(vals), 1),
                                 "mean_ret_pct": round(statistics.mean(vals), 1),
                                 "median_ret_pct": round(statistics.median(vals), 1),
                                 "mean_peak_pct": round(statistics.mean(peaks), 1) if peaks else None})
    st.backend.replace("ladder_report", rows)
    for rule in ("hold10", "double_or_10", "expiry"):
        print(f"\n=== Exit rule: {rule}  (mean return %, win rate %; flags vs random control days) ===")
        print(f"{'expiry':<8}{'strike':<10}{'flag mean':>10}{'win':>6}{'control mean':>14}{'win':>6}{'trades':>8}")
        for dte in TARGET_DTES:
            for otm in TARGET_OTM:
                f = next((r for r in rows if r["grp"] == "flag" and r["exit_rule"] == rule
                          and r["target_dte"] == dte and r["target_otm_pct"] == otm), None)
                c = next((r for r in rows if r["grp"] == "control" and r["exit_rule"] == rule
                          and r["target_dte"] == dte and r["target_otm_pct"] == otm), None)
                if not f:
                    continue
                print(f"{dte:>3} days  {('ATM' if otm == 0 else f'+{otm:g}%'):<10}"
                      f"{f['mean_ret_pct']:>+10.1f}{f['win_rate_pct']:>6.0f}"
                      f"{(c['mean_ret_pct'] if c else float('nan')):>+14.1f}"
                      f"{(c['win_rate_pct'] if c else float('nan')):>6.0f}{f['trades']:>8}")
    print("\nMean returns include a 5% cost on each side of the trade. A useful pattern beats the")
    print("control days by a clear margin, not just zero; buying calls on random days usually loses.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--max-minutes", type=float, default=100)
    p.add_argument("--report-only", action="store_true")
    a = p.parse_args()
    if not a.report_only:
        run(a)
    report(a)


if __name__ == "__main__":
    main()
