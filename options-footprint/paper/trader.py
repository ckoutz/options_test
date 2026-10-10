"""
Paper traders: three AI agents, each with its own Alpaca paper account, trading once a day after the
close with live data, their own strategy, a journal, and a request desk.

    python paper/trader.py day                 # all three agents (after the nightly data job)
    python paper/trader.py day --agents 3 --dry-run   # one agent, orders checked but not sent
    python paper/trader.py report              # rebuild PAPER.md
    python paper/trader.py respond --id R1012-2-ab12 --status approved --response "..."

Seeds: agent 1 starts from the gen10b committee's final playbook, agent 2 from the playoff pick
(gen10b generation 10, agent 3), agent 3 from nothing (the control).
"""
import argparse
import datetime as dt
import http.client
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import collector as C   # noqa: E402
from paper import alpaca as AP   # noqa: E402
from paper import tools as TL    # noqa: E402

MODEL = os.environ.get("PAPER_MODEL", "anthropic/claude-haiku-5.5")
MAX_USD_DAY = float(os.environ.get("PAPER_MAX_USD_DAY", "1.50"))   # per agent per day
MAX_STEPS = int(os.environ.get("PAPER_MAX_STEPS", "45"))
SEEDS = {1: ("gen10b", 10, "editor"), 2: ("gen10b", 10, "agent3"), 3: None}
SEASON = "Season 1: 6 months, with a checkpoint at 3 months."

RULEBOOK = """You are a stock and options trader running your own account. Your goal is to beat the S&P 500 —
not by holding an index, but by finding an edge: something you can do repeatedly that makes money more often,
or more per trade, than chance would.

THE ACCOUNT
- A paper (simulated) account that started with $100,000. Treat every dollar as real.
- Cash account: no borrowing and no short selling unless granted (see Requests). You can buy calls and puts.
- Two other traders run identical accounts with identical tools. You never see their accounts.
- {season}

YOUR DAY
- You wake up once each trading day, after the close and after the nightly data update. You review your
  positions, research with your tools, and place orders that execute at the next session.
- Options orders must be limit orders (quotes after the close are approximate; price near the mid).
- Call finish_day when you are done. Update your journal (journal_write) before you finish.

YOUR MEMORY
- Your journal is loaded every day. Keep your strategy, beliefs, lessons and open questions in it.
- Your last few days' summaries and your recent orders are loaded every day.
- Everything older is saved and searchable with memory_search.

THE RULES (enforced by code; an order that breaks one is rejected with the reason)
- No buy-and-hold: no position held longer than 60 days (the system closes it), and no more than 25% of the
  account in index funds.
- Any expiration is allowed, including long-dated options; buying 90+ days out and selling well before the
  final month is often the smart way to use them. Options must be closed before their last trading day (the
  system closes any that are not), and you cannot open a contract that expires within two sessions.
- Sizing grows with evidence. Every strategy starts at the EXPERIMENT level: each position 5% of the account
  (or one contract if that costs more, never above 10%), and at least 1%. Strategies earn larger sizes
  (Promising: 10%, after 20+ trades beating their random twins; Proven: 25%, after 30+ trades with the whole
  range above zero) once the scoreboard's twin scoring has enough of your trades. Keep at least 10% of your
  new trades as experiments even then.
- Every opening order needs: strategy (a name), reason, and exit_plan — what would prove you wrong
  ("I am wrong if..."). Stop and target orders are optional tools (stock stops: stop, stop_limit,
  trailing_stop). Changing your mind on new information is good trading; write down why.

CASH
- You never have to trade. Waiting for a strong setup is a legitimate edge.
- Your return is measured on your whole account against the S&P 500, so idle money in a rising market falls
  behind on its own.
- If more than 75% of your account sits in cash for 10 straight trading days, write in your journal why you
  are waiting and exactly what would bring you back.

THE BAR AND THE SCORE
- Less than a 4% return per quarter (or the S&P 500's return, if higher) is a failure.
- The main score: every trade you make is shadowed by 100 random twins (the same kind of trade, size and
  holding time on random stocks). Your skill score is how much you beat them. Beating the S&P 500 in a rising
  market is not enough if random traders would have done the same.
- Also tracked: return against the S&P 500 after adjusting for risk, your worst losing stretch, realistic
  trading costs (paper fills are too generous), and registered experiments completed and honestly reported.

EXPLORE
- Register experiments (experiment_register) BEFORE running them: the idea, what you expect, how many trades
  it needs, when you will judge it. Completed, honestly reported experiments count whether they win or lose.

REQUESTS
- If your strategy needs something you don't have — more data, a tool, margin, short selling, or a live
  intraday trading window (up to 2 hours) — file a request saying what and why. Requests are reviewed by a
  human; free ones built from existing data are usually approved, paid data and account changes take
  longer. Approved requests apply to all three traders. You can ask questions the same way.

HOW TO THINK
- Most patterns that look good on a few trades are luck. Before trusting an idea, ask how many trades it
  rests on and whether random trades would have done the same.
- Write down what you expect before you trade, then check it after. Keep what works, drop what doesn't, and
  say why in your journal.
- It is fine to sit in cash when you have no edge. It is not fine to trade just to look busy."""

FINDINGS = """WHAT EARLIER RESEARCH FOUND (from historical tests on 2024-2026 data; use as context, not gospel):
- Buying calls is expensive: at random, a 30-day at-the-money call held 10 sessions lost about 9-12% on
  average after realistic costs (median about -35%). Round-trip trading costs on an option are 10% or more of
  its price, more on cheap options.
- The best stock-level edges found were small: about +1% to +1.6% over 10 sessions for strong-trend stocks
  with steady call buying in a rising market. Edges that small cannot pay for an ordinary option; options
  only won when the stock moved a lot.
- A momentum-plus-call-flow idea (up 20%+ in 20 sessions, 15%+ above the 50-day average, market rising)
  beat random option trades in historical blind tests, but mostly on stocks that were chosen with hindsight;
  on stocks chosen without hindsight its edge was weak or absent.
- Stocks with many 15%+ jumps in the past year keep jumping (about a 16% chance of another 15%+ up day in the
  next two weeks, versus about 1% for typical stocks), but their options are priced for it: implied
  volatility above 100%, and their 30-day calls lost about 37% on average.
- Implied volatility, earnings dates and option prices matter; check them before buying options."""


# ---------------------------------------------------------------- model calls with tools
class Budget(Exception):
    pass


def chat(messages, tools, cost_so_far):
    key = os.environ.get("LLM_API_KEY", "")
    base = os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
    body = json.dumps({"model": MODEL, "messages": messages, "tools": tools, "max_tokens": 4000,
                       "temperature": 0.5, "usage": {"include": True}}).encode()
    for attempt in range(6):
        req = urllib.request.Request(f"{base}/chat/completions", data=body, headers={
            "Authorization": f"Bearer {key}", "Content-Type": "application/json", "X-Title": "paper traders"})
        try:
            with urllib.request.urlopen(req, timeout=240) as r:
                data = json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 5:
                time.sleep(min(60, 5 * 2 ** attempt))
                continue
            raise RuntimeError(f"model API HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
        except (urllib.error.URLError, OSError, http.client.HTTPException, ValueError):
            if attempt < 5:
                time.sleep(10 * (attempt + 1))
                continue
            raise
        if "error" in data or not data.get("choices"):
            if attempt < 5:
                time.sleep(10)
                continue
            raise RuntimeError(f"model API error: {str(data)[:300]}")
        u = data.get("usage") or {}
        cost = float(u.get("cost") or 0)
        if not cost:
            # Some responses omit the cost: estimate from tokens (Haiku-class prices, a little high on purpose).
            cost = (int(u.get("prompt_tokens") or 0) * 1.2 + int(u.get("completion_tokens") or 0) * 6.0) / 1e6
        msg = data["choices"][0]["message"]
        if not (msg.get("content") or msg.get("tool_calls")) and attempt < 5:
            time.sleep(5)
            continue
        return msg, cost
    raise RuntimeError("model API kept failing")


# ---------------------------------------------------------------- housekeeping before each agent's day
def housekeeping(n, snap, notes):
    """Record equity; close options at their last session and positions held 60+ days."""
    st = C.db()
    view = TL.account_view(n)
    spy = (snap["rows"].get("SPY") or {}).get("price")
    long_v = sum(p["market_value"] for p in view["positions"] if p["market_value"] > 0)
    short_v = sum(-p["market_value"] for p in view["positions"] if p["market_value"] < 0)
    st.backend.upsert("paper_equity", [{"agent": TL.me(n), "day": dt.date.today().isoformat(),
                                        "equity": view["equity"], "cash": view["cash"], "long_value": long_v,
                                        "short_value": short_v, "positions": len(view["positions"]),
                                        "spy_close": spy}])
    nxt = TL.next_sessions(1)
    first_buy = {}
    for o in st.backend.read("paper_orders"):
        if o["agent"] == TL.me(n) and o["side"] == "buy" and o["status"] not in ("rejected", "dry-run"):
            first_buy[o["symbol"]] = min(first_buy.get(o["symbol"], o["created"]), o["created"])
    for p in view["positions"]:
        occ = TL.parse_occ(p["symbol"])
        why = None
        if occ and nxt and occ["expiration"] <= nxt[0]:
            why = f"option expires {occ['expiration']}: closed by the system before its last trading day"
        fb = first_buy.get(p["symbol"])
        if fb and (dt.datetime.now(dt.timezone.utc) - dt.datetime.fromisoformat(fb)).days >= TL.MAX_HOLD_DAYS:
            why = f"held {TL.MAX_HOLD_DAYS}+ days: closed by the system (no buy-and-hold)"
        if not why or TL.DRY_RUN:
            if why:
                notes.append(f"(dry run) would close {p['symbol']}: {why}")
            continue
        body = {"symbol": p["symbol"], "qty": str(abs(int(p["qty"])) if occ else abs(p["qty"])),
                "side": "sell" if p["qty"] > 0 else "buy", "time_in_force": "day"}
        if occ:
            body.update(type="limit", limit_price=str(max(0.01, round(p["price"] * 0.9, 2))))
        else:
            body.update(type="market")
        try:
            o = AP.submit_order(n, body)
            TL.log_order(n, {"symbol": p["symbol"], "asset": "option" if occ else "stock", "side": body["side"],
                             "qty": body["qty"], "order_type": body["type"], "strategy": "system",
                             "reason": why}, o.get("status", "submitted"), order_id=o.get("id"))
            notes.append(f"The system placed an order to close {p['symbol']}: {why}.")
        except AP.AlpacaError as e:
            notes.append(f"The system could not close {p['symbol']} ({why}): {e}")
    return view


def cash_streak(n):
    rows = sorted((r for r in C.db().backend.read("paper_equity") if r["agent"] == TL.me(n)),
                  key=lambda r: r["day"])[-10:]
    return len(rows) == 10 and all(TL.fnum(r["cash"]) > 0.75 * TL.fnum(r["equity"], 1) for r in rows)


# ---------------------------------------------------------------- the briefing
def seed_journal(n):
    st = C.db()
    if any(j["agent"] == TL.me(n) for j in st.backend.read("paper_journal")):
        return
    seed = SEEDS.get(n)
    text = "(empty: you start fresh. Build your own approach.)"
    if seed:
        lineage, gen, author = seed
        rows = [r for r in st.backend.read("committee_notes") if r["lineage"] == lineage
                and int(r["generation"]) == gen and r["author"] == author]
        if rows:
            who = "the research committee's final playbook" if author == "editor" else \
                "the trader whose approach held up best in historical tests"
            text = (f"NOTES INHERITED FROM YOUR PREDECESSORS ({who}). They learned on historical data with hidden "
                    "dates, anonymous stocks, a fixed menu of calls and a 10-session hold. You now trade live, "
                    "with real names, dates, any instrument and any holding period. Keep what holds up on live "
                    "data, change what doesn't, and rewrite this journal as your own.\n\n" + rows[0]["text"])
    st.backend.upsert("paper_journal", [{"agent": TL.me(n), "text": text, "updated": TL.now()}])


def briefing(n, view, snap, notes):
    st = C.db()
    me = TL.me(n)
    journal = next((j["text"] for j in st.backend.read("paper_journal") if j["agent"] == me), "")
    days = sorted((d for d in st.backend.read("paper_days") if d["agent"] == me), key=lambda d: d["day"])[-4:]
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=7)).isoformat()
    orders = [o for o in st.backend.read("paper_orders") if o["agent"] == me and o["created"] >= since]
    try:
        fills = {o["id"]: o for o in AP.recent_orders(n, 7)}
    except AP.AlpacaError:
        fills = {}
    reqs = st.backend.read("paper_requests")
    granted = [r for r in reqs if r["status"] == "approved"]
    mine = [r for r in reqs if r["agent"] == me]
    exps = [e for e in st.backend.read("paper_experiments") if e["agent"] == me and e["status"] == "open"]
    eq = sorted((r for r in st.backend.read("paper_equity") if r["agent"] == me), key=lambda r: r["day"])
    start = eq[0] if eq else None
    spy_now = (snap["rows"].get("SPY") or {}).get("price")
    perf = ""
    if start and TL.fnum(start["spy_close"]) and spy_now:
        perf = (f"Since the season started on {start['day']}: your account {100 * (view['equity'] / TL.fnum(start['equity']) - 1):+.2f}%, "
                f"the S&P 500 fund {100 * (spy_now / TL.fnum(start['spy_close']) - 1):+.2f}%.")
    spy = snap["rows"].get("SPY") or {}
    parts = [f"TODAY: {dt.date.today():%A %Y-%m-%d}. Next sessions: {', '.join(str(d) for d in TL.next_sessions(3))}.",
             f"MARKET: S&P 500 fund {spy.get('price')} (5 sessions {spy.get('r5d')}%, 20 sessions {spy.get('r1m')}%, "
             f"3 months {spy.get('r3m')}%, "
             f"12 months {spy.get('r12m')}%); {snap['meta']['breadth_pct_above_ma50']}% of {snap['meta']['stocks']} "
             f"liquid US stocks are above their 50-day average.",
             f"YOUR ACCOUNT: {json.dumps(view)}",
             perf]
    if notes:
        parts.append("SYSTEM NOTES:\n" + "\n".join(f"- {x}" for x in notes))
    if cash_streak(n):
        parts.append("You have been more than 75% in cash for 10 straight sessions: write in your journal why "
                     "you are waiting and exactly what would bring you back.")
    parts.append("YOUR JOURNAL:\n" + (journal or "(empty)"))
    if days:
        parts.append("YOUR LAST FEW DAYS:\n" + "\n".join(f"- {d['day']}: {d['summary']}" for d in days))
    if orders:
        parts.append("YOUR ORDERS IN THE LAST 7 DAYS:\n" + "\n".join(
            f"- {o['created'][:10]} {o['side']} {TL.fnum(o['qty']):g} {o['symbol']} ({o['order_type']}"
            f"{', limit ' + str(o['limit_price']) if o['limit_price'] not in ('', None) else ''}) "
            f"strategy {o['strategy'] or '-'}: status {fills.get(o['id'], {}).get('status', o['status'])}"
            f"{', filled at ' + str(fills[o['id']].get('filled_avg_price')) if o['id'] in fills and fills[o['id']].get('filled_avg_price') else ''}"
            f"{' — REJECTED: ' + o['rejected'] if o['rejected'] else ''}" for o in orders[-40:]))
    if exps:
        parts.append("YOUR OPEN EXPERIMENTS:\n" + "\n".join(
            f"- {e['id']} {e['name']}: expect {e['expected']}; needs {e['trades_needed']} trades; judge by {e['judge_by']}"
            for e in exps))
    if mine:
        parts.append("YOUR REQUESTS:\n" + "\n".join(
            f"- {r['id']} ({r['kind']}, {r['status']}): {r['text'][:200]}" + (f" — ANSWER: {r['response']}" if r['response'] else "")
            for r in mine[-10:]))
    if granted:
        parts.append("GRANTED TO ALL TRADERS:\n" + "\n".join(f"- {r['kind']}: {r['response'] or r['text'][:200]}"
                                                           for r in granted))
    parts.append(FINDINGS)
    parts.append("Do your research, place any orders, update your journal, then call finish_day.")
    return "\n\n".join(p for p in parts if p)


# ---------------------------------------------------------------- one agent's day
def run_agent(n, snap):
    st = C.db()
    seed_journal(n)
    notes = []
    view = housekeeping(n, snap, notes)
    messages = [{"role": "system", "content": RULEBOOK.format(season=SEASON)},
                {"role": "user", "content": briefing(n, view, snap, notes)}]
    transcript, cost, steps, summary, wrote_journal, n_orders = [], 0.0, 0, "", False, 0
    while steps < MAX_STEPS:
        steps += 1
        if cost >= MAX_USD_DAY:
            messages.append({"role": "user", "content": "Today's research budget is used up. Update your journal "
                                                        "(journal_write) if you haven't, then call finish_day."})
        msg, c = chat(messages, TL.SCHEMAS, cost)
        cost += c
        messages.append({k: v for k, v in msg.items() if k in ("role", "content", "tool_calls")})
        if msg.get("content"):
            transcript.append(f"THOUGHT: {msg['content'][:2000]}")
        calls = msg.get("tool_calls") or []
        if not calls:
            messages.append({"role": "user", "content": "Use your tools, or call finish_day when you are done."})
            continue
        done = False
        for tc in calls:
            name = tc["function"]["name"]
            try:
                args = json.loads(tc["function"].get("arguments") or "{}")
            except ValueError:
                args = {}
            if name == "finish_day":
                if len(calls) > 1:
                    result = {"error": "call finish_day on its own, after you have read the results of your other "
                                       "tool calls"}
                elif not wrote_journal:
                    result = {"error": "update your journal with journal_write first, then call finish_day again"}
                else:
                    summary, done = str(args.get("summary", ""))[:3000], True
                    result = {"ok": True}
            else:
                result = TL.call(n, name, args)
                wrote_journal |= name == "journal_write" and bool(result.get("saved")) if isinstance(result, dict) else False
                n_orders += name == "place_order"
            text = json.dumps(result, default=str)
            transcript.append(f"TOOL {name} {json.dumps(args)[:600]} -> {text[:800]}")
            messages.append({"role": "tool", "tool_call_id": tc["id"], "content": text[:12000]})
        if done:
            break
        if cost >= MAX_USD_DAY * 1.5:
            transcript.append("STOPPED: spending cap")
            break
    st.backend.upsert("paper_days", [{"agent": TL.me(n), "day": dt.date.today().isoformat(),
                                      "summary": summary or "(no summary: the session ended early)",
                                      "transcript": "\n".join(transcript)[:200000], "cost_usd": round(cost, 4),
                                      "steps": steps, "orders": n_orders, "finished": TL.now()}])
    C.run_log("paper", f"agent{n}: {steps} steps, {n_orders} order attempts, ${cost:.2f}"
                       + ("" if summary else " (no finish_day)"))
    return cost


# ---------------------------------------------------------------- scoreboard
def report():
    st = C.db()
    eq = st.backend.read("paper_equity")
    days = st.backend.read("paper_days")
    orders = st.backend.read("paper_orders")
    reqs = st.backend.read("paper_requests")
    exps = st.backend.read("paper_experiments")
    L = [f"# Paper traders ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "", SEASON, "",
         "Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose "
         "approach held up best). Agent 3: fresh, no notes (the control).", "",
         "| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | "
         "rejected | open experiments | model cost $ |", "|---|---|---|---|---|---|---|---|---|---|"]
    for n in (1, 2, 3):
        me = TL.me(n)
        e = sorted((r for r in eq if r["agent"] == me), key=lambda r: r["day"])
        if not e:
            L.append(f"| {n} | not started | | | | | | | | |")
            continue
        a, b = e[0], e[-1]
        ret = 100 * (TL.fnum(b["equity"]) / TL.fnum(a["equity"], 1) - 1)
        spy = 100 * (TL.fnum(b["spy_close"]) / TL.fnum(a["spy_close"], 1) - 1) if TL.fnum(a["spy_close"]) else 0
        mo = [o for o in orders if o["agent"] == me]
        L.append(f"| {n} | {TL.fnum(b['equity']):,.0f} | {ret:+.2f}% | {spy:+.2f}% | "
                 f"{100 * TL.fnum(b['cash']) / TL.fnum(b['equity'], 1):.0f}% | {b['positions']} | "
                 f"{sum(1 for o in mo if o['status'] not in ('rejected', 'dry-run'))} | "
                 f"{sum(1 for o in mo if o['status'] == 'rejected')} | "
                 f"{sum(1 for x in exps if x['agent'] == me and x['status'] == 'open')} | "
                 f"{sum(TL.fnum(d['cost_usd']) for d in days if d['agent'] == me):.2f} |")
    L += ["", "The random-twin skill score, risk-adjusted return and experiment points arrive in the next build "
              "phase; they are computed from the saved trades, so they will cover these first days too.", ""]
    pend = [r for r in reqs if r["status"] == "pending"]
    L += ["## Requests waiting for you", ""]
    L += [f"- **{r['id']}** (agent {r['agent'].replace('agent', '')}, {r['kind']}, {r['created'][:10]}): {r['text']}" for r in pend] or ["- none"]
    done = [r for r in reqs if r["status"] != "pending"]
    if done:
        L += ["", "## Answered requests", ""] + [f"- {r['id']} {r['status']}: {r['text'][:150]} — {r['response']}"
                                                 for r in done[-15:]]
    L += ["", "## Latest days", ""]
    for n in (1, 2, 3):
        mine = sorted((d for d in days if d["agent"] == TL.me(n)), key=lambda d: d["day"])[-3:]
        L += [f"### Agent {n}", ""] + [f"- **{d['day']}** ({d['steps']} steps, {d['orders']} order attempts, "
                                       f"${TL.fnum(d['cost_usd']):.2f}): {d['summary']}" for d in mine] + [""]
    L += ["## Open experiments", ""]
    L += [f"- agent {e['agent'].replace('agent', '').replace('-dry', ' (dry run)')} **{e['name']}** ({e['id']}): {e['hypothesis'][:200]} Expect: {e['expected'][:150]}. "
          f"Judge by {e['judge_by']}." for e in exps if e["status"] == "open"] or ["- none"]
    with open(os.path.join(C.ROOT, "PAPER.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:20]))


def smoke(n):
    """Call every read-only tool once and print a short result, to check the plumbing."""
    os.environ["PAPER_DRY_RUN"] = "1"
    TL.DRY_RUN = True
    snap = AP.market_snapshot()
    print(f"snapshot: {snap['meta']}")
    checks = [("account", {}), ("leaders", {"period": "6m", "count": 5}), ("stock_stats", {"symbols": ["AAPL", "NVDA"]}),
              ("price_history", {"symbol": "AAPL", "days": 30}), ("news", {"symbol": "AAPL", "limit": 3}),
              ("option_chain", {"symbol": "AAPL", "min_days": 20, "max_days": 60, "strike_range_pct": 5}),
              ("options_flow", {"count": 5}), ("watchlists", {}),
              ("memory_search", {"query": "momentum"}),
              ("place_order", {"symbol": "AAPL", "side": "buy", "qty": 1, "order_type": "limit", "limit_price": 1.0,
                               "strategy": "smoke", "reason": "smoke test", "exit_plan": "smoke test"})]
    ok = True
    out = [f"# Paper tools smoke test ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
           f"Market snapshot: {snap['meta']}", ""]
    for name, args in checks:
        res = TL.call(n, name, args)
        bad = isinstance(res, dict) and ("error" in res)
        ok &= not bad
        line = f"{'FAIL' if bad else 'ok'} **{name}**: `{json.dumps(res, default=str)[:600]}`"
        print(line)
        out.append("- " + line)
    chain = TL.call(n, "option_chain", {"symbol": "AAPL", "min_days": 30, "max_days": 60, "strike_range_pct": 3})
    rows = chain.get("rows") or []
    if rows:
        c = rows[len(rows) // 2]
        res = TL.call(n, "place_order", {"symbol": c["contract"], "side": "buy", "qty": 1, "order_type": "limit",
                                         "limit_price": c.get("mid") or 1.0, "strategy": "smoke",
                                         "reason": "smoke test", "exit_plan": "smoke test"})
        print(f"option order check: {json.dumps(res)[:400]}")
        out.append(f"- option order check ({c['contract']}): `{json.dumps(res)[:600]}`")
    out.append("")
    out.append("ALL OK" if ok else "SOME FAILED")
    with open(os.path.join(C.ROOT, "PAPER_SMOKE.md"), "w") as f:
        f.write("\n".join(out) + "\n")
    C.run_log("paper-smoke", "all tools answered" if ok else "some tools failed")
    print("ALL OK" if ok else "SOME FAILED")


def respond(args):
    st = C.db()
    rows = [r for r in st.backend.read("paper_requests") if r["id"] == args.id]
    if not rows:
        sys.exit(f"No request {args.id}")
    st.backend.upsert("paper_requests", [dict(rows[0], status=args.status, response=args.response or "")])
    print(f"{args.id}: {args.status}")
    report()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("day")
    d.add_argument("--agents", default="1,2,3")
    d.add_argument("--dry-run", action="store_true", help="check orders but do not send them")
    sub.add_parser("report")
    sm = sub.add_parser("smoke", help="call every read-only tool once (no model, no orders)")
    sm.add_argument("--agent", type=int, default=3)
    r = sub.add_parser("respond")
    r.add_argument("--id", required=True)
    r.add_argument("--status", choices=["approved", "denied", "pending"], required=True)
    r.add_argument("--response", default="")
    a = p.parse_args()
    if a.cmd == "day":
        if a.dry_run:
            os.environ["PAPER_DRY_RUN"] = "1"
            TL.DRY_RUN = True
        snap = AP.market_snapshot()
        print(f"Market snapshot: {snap['meta']['stocks']} liquid stocks; breadth {snap['meta']['breadth_pct_above_ma50']}%")
        total = 0.0
        for n in [int(x) for x in a.agents.split(",")]:
            try:
                total += run_agent(n, snap)
            except Exception as ex:   # noqa: BLE001 - one agent failing must not stop the others
                C.run_log("paper", f"agent{n} crashed: {type(ex).__name__}: {str(ex)[:300]}")
                print(f"agent{n} crashed: {ex}")
        print(f"Model cost today: ${total:.2f}")
        report()
    elif a.cmd == "report":
        report()
    elif a.cmd == "smoke":
        smoke(a.agent)
    elif a.cmd == "respond":
        respond(a)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except BaseException as ex:   # noqa: BLE001 - write the crash where it can be read, then fail the job
        import traceback
        with open(os.path.join(C.ROOT, "PAPER_ERROR.md"), "w") as f:
            f.write(f"# Paper traders crashed ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)\n\n"
                    f"```\n{traceback.format_exc()[-4000:]}\n```\n")
        raise
