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
import hashlib
import os
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
MIN_SECONDS_BETWEEN_REQUESTS = 2.0   # 30 a minute while the backfill is running (shared Alpaca key)
FAST_SECONDS_BETWEEN_REQUESTS = 0.4  # 150 a minute once the backfill has finished


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


def stable_rank(ticker, date):
    """A fixed pseudo-random number per stock and day, so control picks don't reshuffle when new
    stocks or days are added (Python's built-in hash changes between runs, so use sha1)."""
    return hashlib.sha1(f"{ticker}|{date}".encode()).hexdigest()


def choose_days(days):
    """Flag days (any shortlist rule fired), plus for each stock the same number of non-flag days
    from that same stock as controls. Matching stock by stock compares like with like."""
    flags, quiet = [], {}
    for d in days:
        fired = [name for name in S.FLAG_RULES if S.RULES[name](d)]
        if fired:
            flags.append((d, "flag", ", ".join(fired)))
        else:
            quiet.setdefault(d["ticker"], []).append(d)
    per_ticker = {}
    for d, _, _ in flags:
        per_ticker[d["ticker"]] = per_ticker.get(d["ticker"], 0) + 1
    controls = []
    for t, n in per_ticker.items():
        pool = sorted(quiet.get(t, []), key=lambda d: stable_rank(t, d["date"]))
        controls += [(d, "control", "") for d in pool[:n]]
    return flags + controls


def backfill_busy(st):
    """True while the main backfill is still pulling data (so the ladder should share the key)."""
    if st.kind != "postgres":
        return False
    q = lambda sql: st.backend.conn.execute(sql).fetchone()[0]
    return (q("select count(*) from events where coalesce(window_filled, '') <> 'yes'")
            + q("select count(*) from controls where coalesce(window_filled, '') <> 'yes'")
            + q("select count(*) from (select ticker from events group by ticker having count(*) >= 3) x "
                "where ticker not in (select ticker from history_done)")) > 0


def batches(items, max_symbols=100):
    """Group one stock's days so each Alpaca request carries up to 100 contracts."""
    out, cur, syms = [], [], set()
    for it in items:
        s = {p["contract"] for p in it["picked"]}
        if cur and len(syms | s) > max_symbols:
            out.append(cur)
            cur, syms = [], set()
        cur.append(it)
        syms |= s
    if cur:
        out.append(cur)
    return out


def run(args):
    st = C.db()
    busy = backfill_busy(st)
    C.MIN_SECONDS_BETWEEN_REQUESTS = MIN_SECONDS_BETWEEN_REQUESTS if busy else FAST_SECONDS_BETWEEN_REQUESTS
    print(f"Pacing: {C.MIN_SECONDS_BETWEEN_REQUESTS}s between requests "
          f"({'backfill still running' if busy else 'backfill finished'}).")
    deadline = time.monotonic() + 60 * args.max_minutes
    data = S.load(st)
    days = S.score_days(data, 30.0, HOLD_SESSIONS)
    plan = choose_days(days)
    done = {(r["grp"], r["ticker"], r["signal_date"]) for r in st.backend.read("ladder_trades")}
    todo = [p for p in plan if (p[1], p[0]["ticker"], p[0]["date"]) not in done]
    by_ticker = {}
    for p in todo:
        by_ticker.setdefault(p[0]["ticker"], []).append(p)
    print(f"Ladder: {len(plan)} days planned ({sum(1 for p in plan if p[1] == 'flag')} flags), "
          f"{len(plan) - len(todo)} done, {len(todo)} to go across {len(by_ticker)} stocks.")
    today = dt.date.today().isoformat()
    finished, n_done = True, 0
    for t, items in sorted(by_ticker.items()):
        if time.monotonic() > deadline:
            finished = False
            break
        rows = data[t]
        dates = [r["date"] for r in rows]
        index = {d: i for i, d in enumerate(dates)}
        closes = {r["date"]: C.to_float(r["stock_close"]) for r in rows}
        try:
            contracts = C.option_contracts(t, C.ALPACA_HISTORY_START, C.add_days(today, C.MAX_EXPIRY_DAYS))
        except Exception as ex:
            C.log_error({"ticker": t, "event_date": "ladder contracts"}, ex)
            print(f"  {t} contracts FAILED: {str(ex)[:150]}")
            continue
        work = []
        for d, grp, rules in sorted(items, key=lambda p: p[0]["date"]):
            i = index[d["date"]]
            if i + 1 >= len(dates):
                continue                               # no next session yet to buy in
            picked = pick_contracts(contracts, d["date"], d["close"])
            if picked:
                work.append({"d": d, "grp": grp, "rules": rules, "i": i, "picked": picked})
        for batch in batches(work):
            if time.monotonic() > deadline:
                finished = False
                break
            syms = sorted({p["contract"] for it in batch for p in it["picked"]})
            start = dates[batch[0]["i"] + 1]
            end = min(max(p["expiration"] for it in batch for p in it["picked"]), today)
            try:
                pages = C.alpaca_get("https://data.alpaca.markets", "/v1beta1/options/bars",
                                     {"symbols": ",".join(syms), "timeframe": "1Day", "start": start,
                                      "end": C.safe_end(end), "limit": 10000})
            except Exception as ex:
                C.log_error({"ticker": t, "event_date": f"ladder {start}"}, ex)
                print(f"  {t} from {start} FAILED: {str(ex)[:150]}")
                continue
            bars = {}
            for page in pages:
                for sym, bs in (page.get("bars") or {}).items():
                    bars.setdefault(sym, []).extend(bs)
            out = []
            for it in batch:
                d = it["d"]
                for p in it["picked"]:
                    tr = dict(p, grp=it["grp"], rules=it["rules"], ticker=t, signal_date=d["date"],
                              stock_close=d["close"])
                    out.append(simulate(tr, bars.get(p["contract"], []), dates, closes, it["i"] + 1))
            st.backend.upsert("ladder_trades", out)
            n_done += len(batch)
        if not finished:
            break
        print(f"  {t}: {len(work)} days ({n_done}/{len(todo)} overall)")
    with open(STATUS_FILE, "w") as f:
        f.write("done" if finished else "more")
    print("Ladder complete." if finished else "Ladder not finished; another round needed.")


def report(args):
    st = C.db()
    allt = st.backend.read("ladder_trades")
    trades = [r for r in allt if r["filled"] == "yes"]
    if not allt:
        stored = st.backend.read("ladder_report")
        if not stored:
            print("No ladder trades yet.")
            return
        print("The raw ladder trades are archived (GitHub Release); showing the saved summary from "
              f"{stored[0]['run_date']}.")
        rows = [{"grp": r["grp"], "target_dte": int(r["target_dte"]), "target_otm_pct": float(r["target_otm_pct"]),
                 "exit_rule": r["exit_rule"], "trades": int(r["trades"]), "win_rate_pct": float(r["win_rate_pct"]),
                 "mean_ret_pct": float(r["mean_ret_pct"]), "median_ret_pct": float(r["median_ret_pct"])}
                for r in stored]
        print_tables(rows)
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
    print_tables(rows)


def print_tables(rows):
    for rule in ("hold10", "double_or_10", "expiry"):
        print(f"\n=== Exit rule: {rule}  (return %, flags vs control days on the same stocks) ===")
        print(f"{'expiry':<9}{'strike':<9}{'FLAG mean':>10}{'median':>8}{'win%':>6}"
              f"{'CONTROL mean':>14}{'median':>8}{'win%':>6}{'trades':>8}")
        for dte in TARGET_DTES:
            for otm in TARGET_OTM:
                f = next((r for r in rows if r["grp"] == "flag" and r["exit_rule"] == rule
                          and r["target_dte"] == dte and r["target_otm_pct"] == otm), None)
                c = next((r for r in rows if r["grp"] == "control" and r["exit_rule"] == rule
                          and r["target_dte"] == dte and r["target_otm_pct"] == otm), None)
                if not f:
                    continue
                cv = lambda k: f"{c[k]:+.1f}" if c else "-"
                cw = f"{c['win_rate_pct']:.0f}" if c else "-"
                print(f"{dte:>3} days  {('at money' if otm == 0 else f'+{otm:g}%'):<9}"
                      f"{f['mean_ret_pct']:>+10.1f}{f['median_ret_pct']:>+8.1f}{f['win_rate_pct']:>6.0f}"
                      f"{cv('mean_ret_pct'):>14}{cv('median_ret_pct'):>8}"
                      f"{cw:>6}{f['trades']:>8}")
    print("\nReturns include a 5% cost on each side of the trade. Control days are non-flag days on the")
    print("same stocks. A useful pattern beats its controls by a clear margin, in the median too, since")
    print("a few huge winners can lift a mean on their own.")


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
