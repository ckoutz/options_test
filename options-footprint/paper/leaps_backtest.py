"""
Backtest: buy a stock when market volatility spikes, sell a long-dated (400+ day) out-of-the-money covered call
against it, and hold to the call's expiration. Real option prices (Alpaca's option history, from early 2024).

    python paper/leaps_backtest.py          # writes LEAPS.md

Rules
- Spike entries: the first close each episode where the VIX (CBOE's own daily history) closes at or above
  ENTRY_VIX after closing under CALM_VIX within the previous 20 sessions. Episodes are at least 30 sessions apart.
- Calm control entries: dates with the VIX under CALM_VIX, spread through the same period, so we can tell
  whether the timing matters or the trade simply worked in a rising market.
- Stocks: the 120 most-traded US stocks (60-session average dollar volume) as of each entry date, excluding
  exchange-traded funds. Only stocks listed today are available (delisted ones are missing).
- The call: first expiration at least 400 days out, strike nearest to 10%, 20% or 30% above the stock's close.
  Premium = the option's closing trade on the entry day (or within the next 3 sessions), minus 5% for selling
  at the bid. Stocks that split during the hold are dropped (their contracts change).
- Outcome per share, as a % of the stock price paid: at expiration, min(stock, strike) + premium. Calls not yet
  expired are marked at today's prices: stock - (call x 1.05 to buy it back) + premium. Dividends are ignored
  for every leg (the covered-call holder and the buy-and-hold holder would both get them).
- Compared with: holding the same stock with no call, and the S&P 500 fund (SPY), over the same dates.
"""
import csv
import datetime as dt
import io
import os
import random
import statistics
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from paper import alpaca as AP   # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START = dt.date(2024, 2, 15)
ENTRY_VIX, CALM_VIX = 28.0, 20.0
OTMS = (0.10, 0.20, 0.30)
MIN_DAYS = 400
TOP_N = 120
SELL_HAIRCUT, BUY_HAIRCUT = 0.95, 1.05
FUND_WORDS = ("ETF", " ETN", " Fund", "ProShares", "Direxion", "iShares", "SPDR", "Invesco QQQ", "Leveraged",
              " 2X", " 3X", "Daily Target", "YieldMax", "Bitcoin Trust", "Ether Trust")


def vix_history():
    url = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60) as r:
        text = r.read().decode()
    out = {}
    for row in csv.DictReader(io.StringIO(text)):
        m, d, y = row["DATE"].split("/")
        out[f"{y}-{int(m):02d}-{int(d):02d}"] = float(row["CLOSE"])
    return out


def bars(symbols, start, adjustment):
    keys = AP.data_keys()
    out = {}
    for i in range(0, len(symbols), 100):
        pages = AP.get_pages(f"{AP.DATA}/v2/stocks/bars", keys,
                             {"symbols": ",".join(symbols[i:i + 100]), "timeframe": "1Day", "start": start.isoformat(),
                              "end": AP.last_close_end(), "limit": 10000, "adjustment": adjustment, "feed": "sip"},
                             "bars")
        for page in pages:
            for s, bs in page.items():
                out.setdefault(s, {}).update({b["t"][:10]: (b["c"], b["v"]) for b in bs})
    return out


def entries(vix):
    days = sorted(d for d in vix if d >= START.isoformat())
    last_ok = (dt.date.today() - dt.timedelta(days=45)).isoformat()
    spikes, last = [], -999
    for i, d in enumerate(days):
        if d > last_ok:
            break
        if vix[d] >= ENTRY_VIX and any(vix[x] < CALM_VIX for x in days[max(0, i - 20):i]) and i - last >= 30:
            spikes.append(d)
            last = i
    calm = [d for d in days if vix[d] < CALM_VIX and d <= last_ok]
    rng = random.Random(7)
    picks = sorted(rng.sample(calm, min(len(calm), max(4, 2 * len(spikes)))))
    return spikes, picks


def contracts(symbol, entry, price, keys):
    e = dt.date.fromisoformat(entry)
    found = []
    for status in ("inactive", "active"):
        found += AP.get_pages(f"{AP.PAPER}/v2/options/contracts", keys,
                              {"underlying_symbols": symbol, "type": "call", "status": status, "limit": 10000,
                               "expiration_date_gte": (e + dt.timedelta(days=MIN_DAYS)).isoformat(),
                               "expiration_date_lte": (e + dt.timedelta(days=MIN_DAYS + 420)).isoformat(),
                               "strike_price_gte": round(price * 1.03, 2), "strike_price_lte": round(price * 1.45, 2)},
                              "option_contracts")
    if not found:
        return {}
    first = min(c["expiration_date"] for c in found)
    near = [c for c in found if c["expiration_date"] == first]
    out = {}
    for otm in OTMS:
        want = price * (1 + otm)
        c = min(near, key=lambda c: abs(float(c["strike_price"]) - want))
        if abs(float(c["strike_price"]) / want - 1) <= 0.04:
            out[otm] = (c["symbol"], float(c["strike_price"]), first)
    return out


def option_closes(symbols, start, end):
    keys = AP.data_keys()
    out = {}
    for i in range(0, len(symbols), 100):
        pages = AP.get_pages(f"{AP.DATA}/v1beta1/options/bars", keys,
                             {"symbols": ",".join(symbols[i:i + 100]), "timeframe": "1Day",
                              "start": start, "end": end, "limit": 10000}, "bars")
        for page in pages:
            for s, bs in page.items():
                out.setdefault(s, []).extend((b["t"][:10], b["c"]) for b in bs)
    return {s: sorted(v) for s, v in out.items()}


def summarize(rows, key):
    v = [r[key] for r in rows if r.get(key) is not None]
    if not v:
        return "-"
    return f"{statistics.mean(v):+.1f}% / {statistics.median(v):+.1f}%"


def main():
    print("fetching VIX history", flush=True)
    vix = vix_history()
    print(f"VIX history: {len(vix)} days", flush=True)
    spikes, calm = entries(vix)
    print(f"spike entries: {spikes}\ncalm entries: {calm}")
    try:
        tkeys = AP.agent_keys(1)
    except Exception:   # noqa: BLE001
        tkeys = AP.data_keys()
    assets = AP.request("GET", f"{AP.PAPER}/v2/assets", AP.data_keys(), {"status": "active", "asset_class": "us_equity"})
    names = {a["symbol"]: a.get("name", "") for a in assets
             if a.get("tradable") and a.get("options_enabled", True) and a.get("exchange") in AP.MAJOR_EXCHANGES
             and "." not in a["symbol"] and "/" not in a["symbol"]}
    stocks = sorted(s for s, n in names.items() if not any(w.lower() in n.lower() for w in FUND_WORDS))
    # Liquidity screen first (recent bars), then full raw and split-adjusted history for the survivors.
    recent = bars(stocks, dt.date.today() - dt.timedelta(days=15), "raw")
    pool = sorted(s for s, b in recent.items() if b and statistics.mean(c * v for c, v in b.values()) >= 50e6)
    raw = bars(pool + ["SPY"], START - dt.timedelta(days=120), "raw")
    split = bars(pool, START - dt.timedelta(days=120), "split")
    spy = raw.get("SPY", {})
    today = max(spy)
    results = []
    for kind, dates in (("spike", spikes), ("calm", calm)):
        for d in dates:
            ranked = []
            for s in pool:
                b = raw.get(s, {})
                ds = sorted(x for x in b if x <= d)[-60:]
                if len(ds) < 40 or ds[-1] != d:
                    continue
                ranked.append((statistics.mean(b[x][0] * b[x][1] for x in ds), s))
            top = [s for _, s in sorted(ranked, reverse=True)[:TOP_N]]
            picks = {}
            for s in top:
                try:
                    cs = contracts(s, d, raw[s][d][0], tkeys)
                except Exception as ex:   # noqa: BLE001
                    print(f"  {s} {d}: contracts failed {ex}")
                    continue
                for otm, c in cs.items():
                    picks[(s, otm)] = c
            end = (dt.date.fromisoformat(d) + dt.timedelta(days=6)).isoformat()
            entry_px = option_closes(sorted({c[0] for c in picks.values()}), d, end)
            n_before = len(results)
            for (s, otm), (occ, strike, exp) in picks.items():
                px = entry_px.get(occ)
                if not px:
                    continue
                prem = px[0][1] * SELL_HAIRCUT
                S0 = raw[s][d][0]
                expired = exp <= today
                end_day = max(x for x in raw[s] if x <= (exp if expired else today))
                r0 = raw[s][d][0] / split[s][d][0] if split.get(s, {}).get(d) else 1
                r1 = raw[s][end_day][0] / split[s][end_day][0] if split.get(s, {}).get(end_day) else 1
                if abs(r1 / r0 - 1) > 0.01:
                    continue                                    # split during the hold
                S1 = raw[s][end_day][0]
                if expired:
                    value = min(S1, strike) + prem
                    status = "assigned" if S1 > strike else "expired"
                else:
                    results.append({"pending": (s, otm, occ, kind, d, S0, S1, strike, prem, exp, end_day)})
                    continue
                spy_end = spy.get(end_day)
                results.append({"kind": kind, "date": d, "stock": s, "otm": otm, "contract": occ, "exp": exp,
                                "status": status, "premium_pct": 100 * prem / S0,
                                "cc": 100 * (value / S0 - 1), "hold": 100 * (S1 / S0 - 1),
                                "spy": 100 * (spy_end / spy[d] - 1) if spy_end and spy.get(d) else None,
                                "days": (dt.date.fromisoformat(end_day) - dt.date.fromisoformat(d)).days})
            print(f"{kind} {d}: {len(top)} stocks, {len(picks)} contracts, {len(results) - n_before} trades")
    # Mark the unexpired ones at today's option prices.
    pend = [r["pending"] for r in results if "pending" in r]
    results = [r for r in results if "pending" not in r]
    if pend:
        now_px = option_closes(sorted({p[2] for p in pend}), (dt.date.fromisoformat(today) - dt.timedelta(days=10)).isoformat(),
                               (dt.date.fromisoformat(today) + dt.timedelta(days=1)).isoformat())
        for s, otm, occ, kind, d, S0, S1, strike, prem, exp, end_day in pend:
            px = now_px.get(occ)
            if not px:
                continue
            value = S1 - px[-1][1] * BUY_HAIRCUT + prem
            spy_end = spy.get(end_day)
            results.append({"kind": kind, "date": d, "stock": s, "otm": otm, "contract": occ, "exp": exp,
                            "status": "open (marked today)", "premium_pct": 100 * prem / S0,
                            "cc": 100 * (value / S0 - 1), "hold": 100 * (S1 / S0 - 1),
                            "spy": 100 * (spy_end / spy[d] - 1) if spy_end and spy.get(d) else None,
                            "days": (dt.date.fromisoformat(end_day) - dt.date.fromisoformat(d)).days})
    write(results, spikes, calm, vix)


def write(results, spikes, calm, vix):
    L = [f"# Selling long-dated covered calls after volatility spikes ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d} UTC)", "",
         __doc__.split("Rules")[1].strip(), "",
         f"Spike entry dates (VIX close): {', '.join(f'{d} ({vix[d]:.0f})' for d in spikes) or 'none'}",
         f"Calm control dates: {', '.join(calm) or 'none'}", "",
         "## Results (average / median, % of the stock price paid; not annualized)", "",
         "| entries | strike above price | trades | premium collected | covered call | stock held, no call | "
         "S&P 500 fund | covered call beat holding the stock | finished above the strike | covered call lost money | worst |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for kind in ("spike", "calm"):
        for otm in OTMS:
            g = [r for r in results if r["kind"] == kind and r["otm"] == otm]
            if not g:
                continue
            L.append(f"| {kind} | {otm:.0%} | {len(g)} | {summarize(g, 'premium_pct')} | {summarize(g, 'cc')} | "
                     f"{summarize(g, 'hold')} | {summarize(g, 'spy')} | "
                     f"{100 * sum(r['cc'] > r['hold'] for r in g) / len(g):.0f}% | "
                     f"{100 * sum(r['status'] == 'assigned' or (r['status'].startswith('open') and r['hold'] > r['otm'] * 100) for r in g) / len(g):.0f}% | "
                     f"{100 * sum(r['cc'] < 0 for r in g) / len(g):.0f}% | {min(r['cc'] for r in g):+.0f}% |")
    L += ["", "## By entry date (20% above the price)", "",
          "| date | kind | trades | status | premium | covered call | stock held | S&P 500 fund | days held |",
          "|---|---|---|---|---|---|---|---|---|"]
    for d in sorted({r["date"] for r in results}):
        g = [r for r in results if r["date"] == d and r["otm"] == 0.20]
        if g:
            st = ", ".join(sorted({r["status"] for r in g}))
            L.append(f"| {d} | {g[0]['kind']} | {len(g)} | {st} | {summarize(g, 'premium_pct')} | {summarize(g, 'cc')} | "
                     f"{summarize(g, 'hold')} | {summarize(g, 'spy')} | {statistics.median(r['days'] for r in g):.0f} |")
    big = [r for r in results if r["kind"] == "spike" and r["premium_pct"] >= 20]
    L += ["", f"Trades where the premium was 20% or more of the stock price: {len(big)} of "
              f"{sum(r['kind'] == 'spike' for r in results)} spike trades; covered call {summarize(big, 'cc')}, "
              f"stock held {summarize(big, 'hold')}.", "",
          "## Every trade", "", "| kind | date | stock | contract | status | premium | covered call | stock held |",
          "|---|---|---|---|---|---|---|---|"]
    L += [f"| {r['kind']} | {r['date']} | {r['stock']} | {r['contract']} | {r['status']} | {r['premium_pct']:.1f}% | "
          f"{r['cc']:+.1f}% | {r['hold']:+.1f}% |" for r in sorted(results, key=lambda r: (r['date'], r['otm'], -r['premium_pct']))]
    with open(os.path.join(ROOT, "LEAPS.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:40]))


if __name__ == "__main__":
    try:
        main()
    except Exception:   # noqa: BLE001 - logs are not readable from the chat, so the error goes in the report
        import traceback
        with open(os.path.join(ROOT, "LEAPS.md"), "w") as f:
            f.write("# LEAPS backtest crashed\n\n```\n" + traceback.format_exc() + "\n```\n")
        raise
