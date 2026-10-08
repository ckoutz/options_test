"""
Trader generations: agents that walk through history, trade, learn, and pass on lessons.

Each generation:
  1. TRAINING  walks week by week through the training period (March 2024 to June 2025). Each
     week it sees about a dozen anonymized candidate stock-days and may buy the stock or a call
     (15 strike and expiration choices). Results of its trades are revealed two weeks later
     (10 trading sessions), so it can learn as it goes.
  2. LESSONS   at the end it rewrites the lessons document it inherited from the previous
     generation. Only this document passes on; its trades and results are never shown to the
     next generation.
  3. SCORING   with its new lessons and no feedback at all, it trades the validation period
     (July 2025 to January 2026). That score is how we judge each generation.
The test period (February 2026 onward) is never used by the loop. Run it once, at the very end,
with `--phase test`, to see whether the best lessons hold up on data nobody has learned from.

Stocks are shown as codes that are reshuffled every run, days as week numbers, and prices only
as percentages, so a model cannot recognize a stock or period from its training data.

Every run is compared with a random picker that makes the same number of trades of the same
kind in the same weeks: an agent has to beat luck, not just zero.

    python agents.py build                          # build the candidate sample (once)
    python agents.py loop --generations 3           # run 3 more generations of a lineage
    python agents.py loop --lineage briefed         # a lineage that starts from our findings
    python agents.py test --lineage blank --generation 5    # the one-time final exam
    python agents.py report                         # write AGENTS.md

Model access is any OpenAI-compatible chat API (OpenRouter by default):
    LLM_API_KEY    your OpenRouter key          LLM_MODEL     e.g. anthropic/claude-haiku-5.5
    LLM_BASE_URL   https://openrouter.ai/api/v1 (default)
    MAX_USD        total spending cap across all runs (default 25)
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import random
import re
import statistics
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # find the modules next to this file
import collector as C  # noqa: E402
import scorer as S     # noqa: E402

TRAIN_END = "2025-06-30"
VALIDATION_END = "2026-01-31"
CANDIDATES_PER_WEEK = 12
MAX_PICKS_PER_WEEK = 3
REVEAL_AFTER_WEEKS = 2            # 10 trading sessions
SHARE_COST = 0.001                # 0.1% each way for stock trades
LESSON_WORDS = 400
EXPIRIES = (14, 30, 90)
STRIKES = (0.0, 5.0, 10.0, 15.0, 20.0)
EXITS = ("hold10", "double_or_10")
FEATURES = [  # (key in the arena, label shown to the agent, meaning)
    ("call_volume_spike", "calls", "call volume today ÷ its median over the previous 20 sessions"),
    ("put_volume_spike", "puts", "put volume today ÷ its 20-session median"),
    ("put_call", "p/c", "put volume ÷ call volume today"),
    ("put_call_drop", "p/c drop", "20-session median put/call ÷ today's (above 1 = calls crowding out puts)"),
    ("call_vol_short_spike", "short", "calls expiring within 14 days, ÷ their 20-session median"),
    ("call_vol_medium_spike", "medium", "calls expiring in 15 to 60 days, ÷ their 20-session median"),
    ("call_vol_long_spike", "long", "calls expiring beyond 60 days, ÷ their 20-session median"),
    ("call_vol_otm_spike", "otm", "calls with strikes 5%+ above the price, ÷ their 20-session median"),
    ("stock_volume_spike", "shares", "share volume today ÷ its 20-session median"),
    ("ret_1d_pct", "1d %", "stock price change today, percent"),
    ("ret_5d_pct", "5d %", "stock price change over the last 5 sessions, percent"),
    ("vol20_pct", "vol20 %", "typical daily move over the last 20 sessions (standard deviation), percent"),
    ("ret_20d_pct", "20d %", "stock price change over the last 20 sessions, percent"),
    ("vs_ma20_pct", "vs ma20 %", "price versus its 20-session average close, percent (above 0 = above the average)"),
    ("vs_ma50_pct", "vs ma50 %", "price versus its 50-session average close, percent"),
    ("from_high60_pct", "off high %", "price versus the highest close of the last 60 sessions, percent (0 = at the high)"),
    ("rsi14", "rsi", "14-session RSI of closes (above 70 = overbought, below 30 = oversold)"),
    ("price_band", "price", "share price band: under $10, $10 to $50, or over $50"),
]
TECHNICALS = ("ret_20d_pct", "vs_ma20_pct", "vs_ma50_pct", "from_high60_pct", "rsi14")
TRADE_USD = 1000                  # every trade is the same size, so profit = return x $10
LINEAGE_VERSION = "-v2"           # v1 runs (truncated replies, no trades) stay in the tables, kept apart

SEED_BRIEFING = """Findings from an earlier statistical study of these stocks (not from an agent):
- Big call-volume spikes (5x+ normal) were followed by 30%+ rallies about 1.3x as often as an average
  day, but by big drops about 1.2x as often too; the median 10-day return was the same as any day.
- Call spikes right after a 10%+ week were followed by big moves in BOTH directions (rally 1.8x,
  drop 1.6x): they predict volatility more than direction.
- "Quiet" call buying (big call spike, share volume and price calm) was followed by FEWER big moves.
- Put/call drops on their own predicted nothing.
- Bought blindly, calls on these stocks lose most of the time: median results after 10 sessions
  ranged from about -20% (90-day calls) to -80% (14-day calls 20% above the price).
"""


# ---------------------------------------------------------------- arena
def period_of(date):
    return "train" if date <= TRAIN_END else "validation" if date <= VALIDATION_END else "test"


def week_of(date):
    d = dt.date.fromisoformat(date)
    return (d - dt.timedelta(days=d.weekday())).isoformat()


def rank(*parts):
    return hashlib.sha1("|".join(map(str, parts)).encode()).hexdigest()


def ladder_days(st):
    """Every stock-day in the ladder backtest, with its group (flag or control)."""
    if st.kind == "postgres":
        rows = st.backend.conn.execute(
            "select distinct ticker, signal_date, grp from ladder_trades "
            "where ret_hold10_pct is not null").fetchall()
        return [(t, str(d), g) for t, d, g in rows]
    return sorted({(r["ticker"], r["signal_date"], r["grp"]) for r in st.backend.read("ladder_trades")
                   if r["ret_hold10_pct"] != ""})


def ladder_rows(st, picked):
    keys = {(t, d) for t, d, _ in picked}
    if st.kind == "postgres":
        cols = ["ticker", "signal_date", "target_dte", "target_otm_pct", "filled", "entry_price",
                "stock_close", "ret_hold10_pct", "ret_double_or_10_pct"]
        st.backend.conn.execute("create temporary table if not exists want (ticker text, signal_date date)")
        st.backend.conn.execute("delete from want")
        with st.backend.conn.cursor() as cur:
            cur.executemany("insert into want values (%s, %s)", sorted(keys))
        rows = st.backend.conn.execute(
            f"select {', '.join('l.' + c for c in cols)} from ladder_trades l "
            "join want w on w.ticker = l.ticker and w.signal_date = l.signal_date").fetchall()
        return [{c: ("" if v is None else str(v)) for c, v in zip(cols, r)} for r in rows]
    return [r for r in st.backend.read("ladder_trades") if (r["ticker"], r["signal_date"]) in keys]


def technicals(closes, i):
    """Price-only technical indicators for day i, from closes up to and including day i."""
    c = [x for x in closes[max(0, i - 60):i + 1]]
    if any(x is None or x <= 0 for x in c[-21:]) or len(c) < 21:
        return {k: None for k in TECHNICALS}
    now = c[-1]
    out = {"ret_20d_pct": round((now / c[-21] - 1) * 100, 1),
           "vs_ma20_pct": round((now / statistics.mean(c[-20:]) - 1) * 100, 1)}
    ok = [x for x in c if x]
    out["vs_ma50_pct"] = round((now / statistics.mean(ok[-50:]) - 1) * 100, 1) if len(ok) >= 50 else None
    out["from_high60_pct"] = round((now / max(ok[-60:]) - 1) * 100, 1) if len(ok) >= 40 else None
    diffs = [b - a for a, b in zip(c[-15:-1], c[-14:])]
    gain = sum(d for d in diffs if d > 0) / 14
    loss = -sum(d for d in diffs if d < 0) / 14
    out["rsi14"] = round(100.0 if loss == 0 else 100 - 100 / (1 + gain / loss), 0)
    return out


def add_technicals(args):
    """Add the technical columns to an existing arena (needs only the daily prices, not ladder_trades)."""
    st = C.db()
    rows = st.backend.read("arena")
    if not rows:
        sys.exit("The arena is empty.")
    by_t = {}
    for r in rows:
        by_t.setdefault(r["ticker"], []).append(r)
    for n, (t, items) in enumerate(sorted(by_t.items()), 1):
        daily = [r for r in st.daily(t) if C.to_float(r.get("stock_close"))]
        dates = [r["date"] for r in daily]
        closes = [C.to_float(r["stock_close"]) for r in daily]
        index = {d: i for i, d in enumerate(dates)}
        for r in items:
            f = json.loads(r["features"])
            i = index.get(str(r["signal_date"]))
            f.update(technicals(closes, i) if i is not None else {k: None for k in TECHNICALS})
            r["features"] = json.dumps(f)
        if n % 100 == 0:
            print(f"  {n}/{len(by_t)} stocks")
    st.backend.replace("arena", rows)
    have = sum(1 for r in rows if json.loads(r["features"]).get("vs_ma20_pct") is not None)
    print(f"Technicals added to {have:,} of {len(rows):,} candidates.")


def build(args):
    st = C.db()
    days = ladder_days(st)
    if not days:
        sys.exit("No ladder trades in the database (they may be archived). Restore them with archive.py "
                 "before rebuilding the arena; the current arena is untouched.")
    by_week = {}
    for t, d, g in days:
        by_week.setdefault(week_of(d), []).append((t, d, g))
    picked = []
    for wk, items in sorted(by_week.items()):
        seen = set()
        for t, d, g in sorted(items, key=lambda x: rank("arena", x[0], x[1])):
            if t in seen:
                continue                       # one day per stock per week
            seen.add(t)
            picked.append((t, d, g))
            if len(seen) >= CANDIDATES_PER_WEEK:
                break
    print(f"Arena: {len(days):,} ladder days, {len(by_week)} weeks, {len(picked):,} candidates sampled.")
    options = {}
    for r in ladder_rows(st, picked):
        key = f"{int(r['target_dte'])}d+{float(r['target_otm_pct']):g}"
        ok = r["filled"] == "yes" and r["entry_price"] and r["stock_close"]
        options.setdefault((r["ticker"], r["signal_date"]), {})[key] = {
            "cost_pct": round(float(r["entry_price"]) / float(r["stock_close"]) * 100, 2) if ok else None,
            "hold10": C.to_float(r["ret_hold10_pct"]) if ok else None,
            "double_or_10": C.to_float(r["ret_double_or_10_pct"]) if ok else None}
    tickers = sorted({t for t, _, _ in picked})
    out = []
    for n, t in enumerate(tickers, 1):
        rows = [r for r in st.daily(t) if r.get("put_call_alpaca") not in (None, "")]
        scored = {d["date"]: d for d in S.score_days({t: rows}, 30.0, 10)}
        dates = [r["date"] for r in rows]
        closes = [C.to_float(r["stock_close"]) for r in rows]
        index = {d: i for i, d in enumerate(dates)}
        for tt, d, g in picked:
            if tt != t or d not in scored or d not in index:
                continue
            i = index[d]
            if i + 11 >= len(dates) or not closes[i + 1] or not closes[i + 11]:
                continue
            rets = [closes[k] / closes[k - 1] - 1 for k in range(max(1, i - 19), i + 1)
                    if closes[k] and closes[k - 1]]
            f = {k: scored[d].get(k) for k, _, _ in FEATURES if k in scored[d]}
            f["vol20_pct"] = round(statistics.pstdev(rets) * 100, 2) if len(rets) > 5 else None
            price = closes[i]
            f.update(technicals(closes, i))
            f["price_band"] = "<$10" if price < 10 else "$10-50" if price <= 50 else ">$50"
            shares = (closes[i + 11] * (1 - SHARE_COST)) / (closes[i + 1] * (1 + SHARE_COST)) - 1
            out.append({"ticker": t, "signal_date": d, "period": period_of(d), "week": week_of(d),
                        "grp": g, "features": json.dumps(f), "shares_ret10": round(shares * 100, 2),
                        "options": json.dumps(options.get((t, d), {}))})
        if n % 50 == 0:
            print(f"  {n}/{len(tickers)} stocks")
    st.backend.replace("arena", out)
    counts = {p: sum(1 for r in out if r["period"] == p) for p in ("train", "validation", "test")}
    print(f"Arena built: {len(out):,} candidates ({counts}).")


# ---------------------------------------------------------------- the model
class Budget(Exception):
    pass


class LLM:
    def __init__(self, model, max_usd, spent_before):
        self.model = model
        self.key = os.environ.get("LLM_API_KEY", "")
        self.base = os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
        self.max_usd, self.spent_before = max_usd, spent_before
        self.prompt_tokens = self.completion_tokens = 0
        self.cost = 0.0
        self.last_finish = None
        # Fallback prices (USD per million tokens) when the provider doesn't report cost.
        self.in_price = float(os.environ.get("LLM_PRICE_IN", "2.0"))
        self.out_price = float(os.environ.get("LLM_PRICE_OUT", "10.0"))

    def check_budget(self):
        if self.spent_before + self.cost >= self.max_usd:
            raise Budget(f"spending cap of ${self.max_usd:.2f} reached")

    def chat(self, messages, max_tokens=1500):
        if not self.key:
            sys.exit("Set LLM_API_KEY (your OpenRouter key).")
        self.check_budget()
        body = json.dumps({"model": self.model, "messages": messages, "max_tokens": max_tokens,
                           "temperature": 0.7, "usage": {"include": True}}).encode()
        for attempt in range(6):
            req = urllib.request.Request(f"{self.base}/chat/completions", data=body, headers={
                "Authorization": f"Bearer {self.key}", "Content-Type": "application/json",
                "X-Title": "options-footprint trader generations"})
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    data = json.loads(r.read().decode())
            except urllib.error.HTTPError as e:
                msg = e.read().decode("utf-8", "replace")[:300]
                if e.code in (429, 500, 502, 503, 504) and attempt < 5:
                    time.sleep(min(60, 5 * 2 ** attempt))
                    continue
                raise RuntimeError(f"model API refused with HTTP {e.code}: {msg}")
            except (urllib.error.URLError, TimeoutError):
                if attempt < 5:
                    time.sleep(10)
                    continue
                raise
            if "error" in data:
                if attempt < 5:
                    time.sleep(10)
                    continue
                raise RuntimeError(f"model API error: {str(data['error'])[:300]}")
            u = data.get("usage") or {}
            pt, ct = int(u.get("prompt_tokens") or 0), int(u.get("completion_tokens") or 0)
            self.prompt_tokens += pt
            self.completion_tokens += ct
            self.cost += float(u["cost"]) if u.get("cost") is not None else \
                (pt * self.in_price + ct * self.out_price) / 1e6
            choice = data["choices"][0]
            self.last_finish = choice.get("finish_reason")
            return (choice["message"].get("content") or "").strip()
        raise RuntimeError("model API kept failing")


def parse_json(text):
    """The first JSON object in a reply (models sometimes wrap it in prose or code fences)."""
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


PICK_RE = re.compile(r'\{[^{}]*"id"\s*:\s*"C\d+"[^{}]*\}')


def parse_picks(text):
    """(picks, why, ok). Falls back to pulling complete pick objects out of a cut-off or messy reply."""
    data = parse_json(text)
    if isinstance(data, dict) and isinstance(data.get("picks"), list):
        return data["picks"], str(data.get("why", "")), True
    picks = []
    for m in PICK_RE.finditer(text or ""):
        try:
            picks.append(json.loads(m.group(0)))
        except json.JSONDecodeError:
            pass
    why = re.search(r'"why"\s*:\s*"([^"]*)', text or "")
    passed = re.search(r'"picks"\s*:\s*\[\s*\]', text or "") is not None
    return picks, (why.group(1) if why else ""), bool(picks) or passed


# ---------------------------------------------------------------- prompts
def rules_text(phase):
    feedback = ("Results of each trade are shown to you two weeks (10 trading sessions) after you make it."
                if phase == "train" else
                "This is a scoring run: you will NOT see any results. Rely on your lessons.")
    defs = "\n".join(f"- {label}: {meaning}" for _, label, meaning in FEATURES)
    return f"""You are a trader learning to profit from unusual options activity in volatile US stocks.
Each week you see about a dozen candidate stock-days. For each, you may:
- buy the STOCK (sold 10 trading sessions later), or
- buy one CALL option: expiry 14, 30 or 90 days; strike at the money (0) or 5, 10, 15, 20 percent above
  the stock price; exit "hold10" (sell after 10 sessions) or "double_or_10" (sell as soon as it is worth
  2x, otherwise after 10 sessions), or
- pass.
Pick at most {MAX_PICKS_PER_WEEK} per week. Every trade is ${TRADE_USD:,}.
YOUR GOAL: MAKE AS MUCH MONEY AS POSSIBLE. Your score is your total profit in dollars over the whole run.
A pass earns $0; a trade earns its return on ${TRADE_USD:,} (+50% = +$500, -100% = -${TRADE_USD:,}). So trade
when you believe the odds favor you, and pass when they don't: losing trades cost real money, but a
trader who never trades cannot win. You buy at the next session's price; a 5% cost applies to each side
of an option trade and 0.1% to each side of a stock trade.
Calls marked "n/a" did not trade that day and cannot be bought.
{feedback}

Stocks are anonymous codes (reshuffled every run) and time is shown as week numbers, on purpose: judge
only from the numbers. Columns:
{defs}
- option grid: the cost of each call as a percent of the stock price (cheaper = further from the money
  or shorter expiry)

Think it through silently, then reply with ONE compact JSON object and nothing else (no code fences,
no notes before or after):
{{"picks": [{{"id": "C3", "buy": "stock"}}, {{"id": "C7", "buy": "call", "expiry": 30, "strike": 10, "exit": "hold10"}}], "why": "under 25 words"}}
Use {{"picks": [], "why": "under 25 words"}} to pass on the whole week."""


def fmt(v, spec="{:.2f}"):
    if v is None or v == "":
        return "-"
    try:
        return spec.format(float(v))
    except (TypeError, ValueError):
        return str(v)


def candidate_table(cands):
    head = "id  | " + " | ".join(label for _, label, _ in FEATURES)
    lines = [head]
    for c in cands:
        f = c["f"]
        vals = []
        for k, _, _ in FEATURES:
            if k == "price_band":
                vals.append(str(f.get(k) or "-"))
            elif k == "rsi14":
                vals.append(fmt(f.get(k), "{:.0f}"))
            elif k == "vol20_pct":
                vals.append(fmt(f.get(k), "{:.1f}"))
            elif k.endswith("_pct"):
                vals.append(fmt(f.get(k), "{:+.1f}"))
            else:
                vals.append(fmt(f.get(k), "{:.2f}"))
        lines.append(f"{c['id']} {c['code']} | " + " | ".join(vals))
        grid = []
        for e in EXPIRIES:
            cells = []
            for s in STRIKES:
                o = c["o"].get(f"{e}d+{s:g}") or {}
                cells.append(f"+{s:g}%:{fmt(o.get('cost_pct'), '{:.1f}') if o.get('cost_pct') else 'n/a'}")
            grid.append(f"{e}d " + " ".join(cells))
        lines.append("     option grid (cost % of price): " + " / ".join(grid))
    return "\n".join(lines)


def describe_pick(p):
    if p["action"] == "stock":
        return "stock"
    return f"call {p['expiry']}d +{p['strike_pct']:g}% {p['exit_rule']}"


# ---------------------------------------------------------------- one run
def trade_return(cand, action, expiry=None, strike=None, exit_rule=None):
    if action == "stock":
        return cand["shares"]
    o = cand["o"].get(f"{expiry}d+{float(strike):g}") or {}
    if not o.get("cost_pct"):
        return None
    return o.get(exit_rule)


def random_baseline(weeks, trades, reps=300, seed=11):
    """Same weeks, same number and kind of trades, random candidates."""
    rng = random.Random(seed)
    by_week = {}
    for t in trades:
        by_week.setdefault(t["week_index"], []).append(t)
    means, meds, wins = [], [], []
    for _ in range(reps):
        rets = []
        for wi, ts in by_week.items():
            cands = weeks[wi]
            for t in ts:
                for _try in range(10):
                    c = rng.choice(cands)
                    r = trade_return(c, t["action"], t["expiry"], t["strike_pct"], t["exit_rule"])
                    if r is not None:
                        rets.append(r)
                        break
        if rets:
            means.append(statistics.mean(rets))
            meds.append(statistics.median(rets))
            wins.append(100 * sum(r > 0 for r in rets) / len(rets))
    if not means:
        return None, None, None
    return round(statistics.mean(means), 2), round(statistics.mean(meds), 2), round(statistics.mean(wins), 1)


def run_phase(st, llm, lineage, generation, phase, lessons, deadline):
    run_id = f"{lineage}-g{generation}-{phase}-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}"
    rows = [r for r in st.backend.read("arena") if r["period"] == phase]
    if not rows:
        print(f"No candidates for the {phase} period; run `python agents.py build` first. Skipping.")
        return None, [], "skipped: no candidates"
    rng = random.Random(run_id)
    tickers = sorted({r["ticker"] for r in rows})
    codes = rng.sample(range(100, 1000), len(tickers)) if len(tickers) <= 900 else \
        rng.sample(range(1000, 10000), len(tickers))
    code_of = {t: f"S{c}" for t, c in zip(tickers, codes)}
    week_list = sorted({r["week"] for r in rows})
    weeks = []
    for wk in week_list:
        cands = []
        for r in sorted((r for r in rows if r["week"] == wk), key=lambda r: rank(run_id, r["ticker"])):
            cands.append({"id": f"C{len(cands) + 1}", "code": code_of[r["ticker"]], "ticker": r["ticker"],
                          "date": r["signal_date"], "f": json.loads(r["features"]),
                          "o": json.loads(r["options"]), "shares": float(r["shares_ret10"])})
        weeks.append(cands)
    st.backend.upsert("agent_runs", [{"run_id": run_id, "lineage": lineage, "generation": generation,
                                       "phase": phase, "model": llm.model, "status": "running",
                                       "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                       "weeks": len(weeks)}])
    system = rules_text(phase)
    trades, revealed, status = [], [], "complete"
    replies, bad_replies, cut_off, sample_reply = 0, 0, 0, ""
    week_notes = []
    print(f"{run_id}: {len(weeks)} weeks")
    for wi, cands in enumerate(weeks):
        if time.monotonic() > deadline:
            status = "stopped: time limit"
            break
        if phase == "train":
            ready = [t for t in trades if t["week_index"] <= wi - REVEAL_AFTER_WEEKS and not t.get("_shown")]
            for t in ready:
                t["_shown"] = True
                revealed.append(t)
        parts = [f"Your lessons so far:\n{lessons.strip() or '(none yet: you are the first generation)'}"]
        if phase == "train" and revealed:
            rr = [t["ret_pct"] for t in revealed]
            by_kind = {}
            for t in revealed:
                by_kind.setdefault("stock" if t["action"] == "stock" else f"call {t['expiry']}d", []).append(t["ret_pct"])
            parts.append(f"Your profit so far: ${sum(rr) * TRADE_USD / 100:+,.0f} on {len(rr)} trades. "
                         f"Average {statistics.mean(rr):+.1f}%, "
                         f"median {statistics.median(rr):+.1f}%, {100 * sum(r > 0 for r in rr) / len(rr):.0f}% winners. "
                         + "; ".join(f"{k}: {len(v)} trades, avg {statistics.mean(v):+.1f}%"
                                     for k, v in sorted(by_kind.items())))
            recent = revealed[-12:]
            parts.append("Most recent results (what you saw when you bought -> result):\n" + "\n".join(
                f"- week {t['week_index'] + 1} {t['code']} {describe_pick(t)}: calls {fmt(t['f'].get('call_volume_spike'))}x, "
                f"long {fmt(t['f'].get('call_vol_long_spike'))}x, shares {fmt(t['f'].get('stock_volume_spike'))}x, "
                f"5d {fmt(t['f'].get('ret_5d_pct'), '{:+.1f}')}% -> {t['ret_pct']:+.1f}%"
                for t in recent))
        parts.append(f"Week {wi + 1} of {len(weeks)}. Candidates:\n{candidate_table(cands)}")
        messages = [{"role": "system", "content": system}, {"role": "user", "content": "\n\n".join(parts)}]
        try:
            llm.check_budget()
            reply = llm.chat(messages, max_tokens=2500)
        except Budget as b:
            status = f"stopped: {b}"
            break
        except RuntimeError as ex:
            print(f"  week {wi + 1}: model error, treated as pass: {str(ex)[:150]}")
            continue
        replies += 1
        cut_off += llm.last_finish == "length"
        picks, why, ok = parse_picks(reply)
        week_notes.append({"run_id": run_id, "week_index": wi, "picks": len(picks), "finish": llm.last_finish,
                           "readable": "yes" if ok else "no",
                           "why": (why if ok else "(unreadable) " + (reply or ""))[:500]})
        if not ok:
            bad_replies += 1
            if not sample_reply:
                sample_reply = (reply or "(empty reply)")[:600]
                print(f"  week {wi + 1}: could not read the reply ({llm.last_finish}): {sample_reply[:200]!r}")
            if phase == "train" and wi >= 4 and bad_replies > 0.6 * replies:
                status = "stopped: model replies unreadable"
                break
        by_id = {c["id"]: c for c in cands}
        used = set()
        for p in picks[:MAX_PICKS_PER_WEEK]:
            c = by_id.get(str(p.get("id", "")).strip())
            if not c or c["id"] in used:
                continue
            if str(p.get("buy", "")).lower() == "stock":
                spec = {"action": "stock", "expiry": None, "strike_pct": None, "exit_rule": None}
            else:
                try:
                    e, s = int(p.get("expiry")), float(p.get("strike"))
                except (TypeError, ValueError):
                    continue
                x = p.get("exit") if p.get("exit") in EXITS else "hold10"
                if e not in EXPIRIES or s not in STRIKES:
                    continue
                spec = {"action": "call", "expiry": e, "strike_pct": s, "exit_rule": x}
            r = trade_return(c, **{"action": spec["action"], "expiry": spec["expiry"],
                                   "strike": spec["strike_pct"], "exit_rule": spec["exit_rule"]})
            if r is None:
                continue                         # contract not tradable: counts as a pass
            used.add(c["id"])
            trades.append(dict(spec, run_id=run_id, week_index=wi, cand_id=c["id"], code=c["code"],
                               ticker=c["ticker"], signal_date=c["date"], ret_pct=round(r, 2), f=c["f"],
                               reason=why[:300]))
        if (wi + 1) % 10 == 0:
            print(f"  week {wi + 1}: {len(trades)} trades, {bad_replies} unreadable replies, "
                  f"${llm.cost:.3f} spent this run")
    st.backend.upsert("agent_trades", [{k: t.get(k) for k in
                                        ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action",
                                         "expiry", "strike_pct", "exit_rule", "ret_pct", "reason")} for t in trades])
    if week_notes:
        st.backend.upsert("agent_weeks", week_notes)
    rets = [t["ret_pct"] for t in trades]
    bm, bmed, bw = random_baseline(weeks, trades)
    summary = {"run_id": run_id, "lineage": lineage, "generation": generation, "phase": phase,
               "model": llm.model, "weeks": len(weeks), "trades": len(trades),
               "mean_ret": round(statistics.mean(rets), 2) if rets else None,
               "median_ret": round(statistics.median(rets), 2) if rets else None,
               "win_rate": round(100 * sum(r > 0 for r in rets) / len(rets), 1) if rets else None,
               "baseline_mean": bm, "baseline_median": bmed, "baseline_win": bw,
               "profit_usd": round(sum(rets) * TRADE_USD / 100, 2),
               "baseline_profit_usd": round(bm * len(rets) * TRADE_USD / 100, 2) if bm is not None else None,
               "replies": replies, "bad_replies": bad_replies, "cut_off": cut_off, "sample_reply": sample_reply,
               "prompt_tokens": llm.prompt_tokens, "completion_tokens": llm.completion_tokens,
               "cost_usd": round(llm.cost, 4), "status": status,
               "finished": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
    st.backend.upsert("agent_runs", [summary])
    print(f"{run_id}: {summary['trades']} trades, profit ${summary['profit_usd']:+,.0f} "
          f"(random ${summary['baseline_profit_usd'] or 0:+,.0f}), {bad_replies}/{replies} unreadable, mean {summary['mean_ret']}, median {summary['median_ret']}, "
          f"win {summary['win_rate']}% | random same-trades: mean {bm}, median {bmed}, win {bw}% | "
          f"${llm.cost:.3f} | {status}")
    return run_id, trades, status


def write_lessons(llm, lessons, trades):
    """End of training: the agent rewrites the lessons document from its own results."""
    rets = [t["ret_pct"] for t in trades]
    if not trades:
        summary = "You made no trades."
    else:
        groups = {}
        for t in trades:
            groups.setdefault(describe_pick(t), []).append(t["ret_pct"])
        summary = (f"Total profit: ${sum(rets) * TRADE_USD / 100:+,.0f} on {len(rets)} trades of ${TRADE_USD:,}. "
                   f"Average {statistics.mean(rets):+.1f}%, median {statistics.median(rets):+.1f}%, "
                   f"{100 * sum(r > 0 for r in rets) / len(rets):.0f}% winners.\nBy trade type:\n" +
                   "\n".join(f"- {k}: {len(v)} trades, avg {statistics.mean(v):+.1f}%, median {statistics.median(v):+.1f}%"
                             for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))))
    sample = sorted(trades, key=lambda t: t["ret_pct"])
    sample = sample[:15] + sample[-15:] if len(sample) > 30 else sample
    detail = "\n".join(
        f"- {describe_pick(t)}: calls {fmt(t['f'].get('call_volume_spike'))}x, puts {fmt(t['f'].get('put_volume_spike'))}x, "
        f"long {fmt(t['f'].get('call_vol_long_spike'))}x, short {fmt(t['f'].get('call_vol_short_spike'))}x, "
        f"shares {fmt(t['f'].get('stock_volume_spike'))}x, 1d {fmt(t['f'].get('ret_1d_pct'), '{:+.1f}')}%, "
        f"5d {fmt(t['f'].get('ret_5d_pct'), '{:+.1f}')}%, vol20 {fmt(t['f'].get('vol20_pct'), '{:.1f}')}% "
        f"-> {t['ret_pct']:+.1f}%" for t in sample)
    prompt = f"""Your training run is over. Here is how you did.

{summary}

Your worst and best trades (what you saw -> result):
{detail}

The lessons you started with:
{lessons.strip() or '(none: you were the first generation)'}

Write the updated lessons document for the next trader, who will see ONLY this document, never your
trades or results. Keep what held up, fix or drop what didn't, add what you learned. Write general
rules for MAKING MONEY, in terms of the columns (thresholds, combinations, which instrument, expiry, strike and exit),
with how confident you are in each. Be honest about what did not work and about small samples.
No stock codes. At most {LESSON_WORDS} words. Reply with the document only."""
    llm.check_budget()
    text = llm.chat([{"role": "user", "content": prompt}], max_tokens=2000)
    words = text.split()
    return " ".join(words[:int(LESSON_WORDS * 1.15)])


# ---------------------------------------------------------------- commands
def spent(st):
    return sum(C.to_float(r["cost_usd"]) or 0 for r in st.backend.read("agent_runs"))


def latest_lessons(st, lineage):
    rows = [r for r in st.backend.read("agent_lessons") if r["lineage"] == lineage]
    if not rows:
        return 0, (SEED_BRIEFING if lineage.startswith("briefed") else "")
    last = max(rows, key=lambda r: int(r["generation"]))
    return int(last["generation"]), last["text"]


def loop(args):
    st = C.db()
    arena = st.backend.read("arena")
    if not arena:
        build(args)
    elif "rsi14" not in json.loads(arena[0]["features"]):
        print("Adding technical-analysis columns to the candidates (one time)...")
        add_technicals(args)
    args.lineage = args.lineage + LINEAGE_VERSION
    deadline = time.monotonic() + 60 * args.max_minutes
    done, out_of_money, failed = 0, False, False
    started = time.monotonic()
    for _ in range(args.generations):
        # Leave room for one more generation: 1.5x the average so far, or 25 minutes to start.
        per_gen = (time.monotonic() - started) / done if done else 60 * 15
        if time.monotonic() + 1.5 * per_gen > deadline:
            print("Not enough time left for another generation in this round; stopping cleanly.")
            break
        gen_before, lessons = latest_lessons(st, args.lineage)
        generation = gen_before + 1
        llm = LLM(args.model, args.max_usd, spent(st))
        try:
            run_id, trades, status = run_phase(st, llm, args.lineage, generation, "train", lessons, deadline)
            if status != "complete":
                print(f"Training run incomplete ({status}); no lessons written.")
                out_of_money = "spending" in status
                failed = not out_of_money and "time limit" not in status
                break
            if not trades:
                print("The training run made no trades at all; stopping rather than passing on empty lessons.")
                failed = True
                break
            new_lessons = write_lessons(llm, lessons, trades)
        except Budget as b:
            print(f"Stopping: {b}.")
            out_of_money = True
            break
        st.backend.upsert("agent_lessons", [{"lineage": args.lineage, "generation": generation, "run_id": run_id,
                                              "model": args.model, "text": new_lessons,
                                              "created": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}])
        st.backend.upsert("agent_runs", [{"run_id": run_id, "cost_usd": round(llm.cost, 4),
                                           "prompt_tokens": llm.prompt_tokens,
                                           "completion_tokens": llm.completion_tokens}])
        print(f"\nGeneration {generation} lessons:\n{new_lessons}\n")
        llm2 = LLM(args.model, args.max_usd, spent(st))
        _, _, status = run_phase(st, llm2, args.lineage, generation, "validation", new_lessons, deadline)
        done += 1
        if status.startswith("stopped: spending"):
            out_of_money = True
            break
    remaining = 0 if (out_of_money or failed) else max(0, args.generations - done)
    if done == 0 and remaining:
        print("No generation finished this round, so not scheduling another (it would just repeat).")
        remaining = 0
    with open(os.path.join(C.ROOT, "agents_status.txt"), "w") as f:
        f.write(str(remaining))
    print(f"This round: {done} generation(s). Remaining for the next round: {remaining}"
          + (" (spending cap reached)" if out_of_money else ""))
    report(args)


def final_test(args):
    st = C.db()
    args.lineage = args.lineage + LINEAGE_VERSION
    rows = [r for r in st.backend.read("agent_lessons")
            if r["lineage"] == args.lineage and int(r["generation"]) == args.generation]
    if not rows:
        sys.exit(f"No lessons for {args.lineage} generation {args.generation}.")
    if any(r["phase"] == "test" and r["lineage"] == args.lineage and r["generation"] == str(args.generation)
           for r in st.backend.read("agent_runs")):
        print("Note: this generation has already taken the test; a repeat is no longer a clean exam.")
    llm = LLM(args.model, args.max_usd, spent(st))
    run_phase(st, llm, args.lineage, args.generation, "test", rows[0]["text"], time.monotonic() + 60 * args.max_minutes)
    report(args)


def report(args=None):
    st = C.db()
    runs = st.backend.read("agent_runs")
    lessons = st.backend.read("agent_lessons")
    lines = [f"# Trader generations ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
             f"Total spent: ${spent(st):.2f}", "",
             "Each generation trains (with feedback) on March 2024 to June 2025, writes lessons, then is scored",
             "blind on July 2025 to January 2026. \"Random\" makes the same number and kind of trades in the",
             "same weeks on random candidates; beating it is what counts. Every trade is $1,000; returns after costs.",
             "Lineages without -v2 are from the first version (replies were cut off, so they never traded).", "",
             "| lineage | gen | phase | trades | profit $ | random profit $ | mean % | median % | win % | random mean % | random win % | unreadable | cost $ | status |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(runs, key=lambda r: (r["lineage"], int(r["generation"] or 0), r["started"] or "")):
        unread = f"{r.get('bad_replies') or 0}/{r.get('replies')}" if r.get("replies") not in (None, "") else "-"
        lines.append(f"| {r['lineage']} | {r['generation']} | {r['phase']} | {r['trades']} | {r.get('profit_usd') or '-'} | "
                     f"{r.get('baseline_profit_usd') or '-'} | {r['mean_ret']} | {r['median_ret']} | {r['win_rate']} | "
                     f"{r['baseline_mean']} | {r['baseline_win']} | {unread} | {r['cost_usd']} | {r['status']} |")
    for lin in sorted({l["lineage"] for l in lessons}):
        last = max((l for l in lessons if l["lineage"] == lin), key=lambda l: int(l["generation"]))
        lines += ["", f"## Latest lessons: {lin} lineage, generation {last['generation']} ({last['model']})", "",
                  last["text"]]
    with open(os.path.join(C.ROOT, "AGENTS.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    for name in ("loop", "test"):
        a = sub.add_parser(name)
        a.add_argument("--lineage", default="blank", choices=["blank", "briefed"])
        a.add_argument("--model", default=os.environ.get("LLM_MODEL", "anthropic/claude-haiku-5.5"))
        a.add_argument("--max-usd", type=float, default=float(os.environ.get("MAX_USD", "25")))
        a.add_argument("--max-minutes", type=float, default=140)
        if name == "loop":
            a.add_argument("--generations", type=int, default=3)
        else:
            a.add_argument("--generation", type=int, required=True)
    sub.add_parser("report")
    sub.add_parser("add-technicals")
    a = p.parse_args()
    {"build": build, "loop": loop, "test": final_test, "report": report,
     "add-technicals": add_technicals}[a.cmd](a)


if __name__ == "__main__":
    main()
