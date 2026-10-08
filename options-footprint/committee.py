"""
Committee generations: four independent agents, stock bundles, a code-kept scorebook, and an editor.

Data split (python committee.py build-pool --archive ladder_trades.csv.gz):
  - Every stock is dealt into one of 8 BUNDLES, matched on how many big moves it had and how
    volatile it is. Bundles 7 and 8 are held back for the final exam and never used before it.
  - Months from March 2024 to January 2026 are cut into 3-month blocks; one month in each block,
    picked at random, is a blind SCORING month and the rest are TRAINING months. Candidates whose
    10-session outcome would run into a month of the other kind are dropped (the buffer), so no
    outcome straddles training and scoring.
  - February 2026 onward is the TEST period: the one-time forward final exam.

One generation (python committee.py loop):
  1. Four agents each start from the notes and scorebook passed down by the previous generation.
     Independently, each walks the six training bundles in the same shuffled order, week by week:
     it rates every candidate from -2 to +2 and may buy up to 3 (stock or a call). Results show up
     two weeks later. After each bundle it rewrites its own working notes; after the last it states
     its strongest ideas as testable rules.
  2. SCOREBOOK: code tests every rule on every training candidate in all six bundles, including
     stocks the author never saw, and reports trades, returns, a 95% range, how buying every
     candidate the same way did, and how many bundles the rule beat that in.
  3. EDITOR: a fifth agent reads the four agents' notes and their scorebook results and writes
     the combined notes (no length limit) and rules for the next generation. Only the editor's
     notes and the training scorebook of its rules pass on.
  4. BLIND SCORING: a fresh agent trades the scoring months with the editor's notes and no
     feedback, and the editor's rules are scored mechanically on those months. Neither result is
     ever shown to a later generation.

    python committee.py build-pool --archive ladder_trades.csv.gz
    python committee.py loop --generations 5
    python committee.py final-test --generation 7
    python committee.py report                      # writes COMMITTEE.md
"""
import argparse
import concurrent.futures as cf
import csv
import datetime as dt
import gzip
import json
import os
import random
import re
import statistics
import sys
import threading
import time
import traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C  # noqa: E402
import scorer as S     # noqa: E402
import agents as A     # noqa: E402

N_BUNDLES = 8
HOLDOUT_BUNDLES = (7, 8)
TRAIN_BUNDLES = (1, 2, 3, 4, 5, 6)
TEST_START = "2026-02-01"
FIRST_MONTH = "2024-03"
BUFFER_DAYS = 15                  # about 10 trading sessions
PER_WEEK = 8                      # candidates per bundle per week
N_AGENTS = 4
MAX_PICKS = 3
REVEAL_DAYS = 14
LABEL_TO_KEY = {label: key for key, label, _ in A.FEATURES}
OPS = {">": lambda a, b: a > b, ">=": lambda a, b: a >= b, "<": lambda a, b: a < b,
       "<=": lambda a, b: a <= b, "=": lambda a, b: a == b}


# ---------------------------------------------------------------- the pool
def month_of(date):
    return date[:7]


def split_months(months):
    """One random month in each 3-month block is a scoring month; the rest train."""
    rng = random.Random("committee-split-v1")
    train_months, y, mo = [], int(FIRST_MONTH[:4]), int(FIRST_MONTH[5:])
    while f"{y:04d}-{mo:02d}" < TEST_START[:7]:      # every calendar month, data or not
        train_months.append(f"{y:04d}-{mo:02d}")
        y, mo = (y + 1, 1) if mo == 12 else (y, mo + 1)
    split = {}
    for i in range(0, len(train_months), 3):
        block = train_months[i:i + 3]
        pick = rng.choice(block)
        for m in block:
            split[m] = "score" if m == pick else "train"
    for m in months:
        if m >= TEST_START[:7]:
            split[m] = "test"
        elif m < FIRST_MONTH:
            split[m] = "skip"
    return split


def split_of(date, month_split):
    m = month_of(date)
    s = month_split.get(m, "skip")
    ahead = (dt.date.fromisoformat(date) + dt.timedelta(days=BUFFER_DAYS)).isoformat()
    if s != "test" and month_split.get(month_of(ahead), s) != s:
        return "buffer"           # the 10-session outcome would run into the other kind of month
    return s


def deal_bundles(stats):
    """stats: ticker -> (big moves, volatility). Deal stocks into bundles in matched groups of 8."""
    order = sorted(stats, key=lambda t: (-stats[t][0], -stats[t][1], t))
    bundle = {}
    for i in range(0, len(order), N_BUNDLES):
        group = order[i:i + N_BUNDLES]
        slots = list(range(1, N_BUNDLES + 1))
        random.Random(f"deal-{i}").shuffle(slots)
        for t, b in zip(group, slots):
            bundle[t] = b
    return bundle


def build_pool(args):
    st = C.db()
    path = args.archive
    if not os.path.exists(path):
        sys.exit(f"Archive file {path} not found (download it from the ladder-trades-archive release).")
    days = {}
    with gzip.open(path, "rt", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("ret_hold10_pct") not in (None, ""):
                days[(r["ticker"], r["signal_date"])] = r["grp"]
    by_ticker = {}
    for (t, d), g in days.items():
        by_ticker.setdefault(t, {})[d] = g
    print(f"Archive: {len(days):,} stock-days across {len(by_ticker):,} stocks.")
    moves = {}
    for e in st.events():
        moves[e["ticker"]] = moves.get(e["ticker"], 0) + 1
    feats, stats = {}, {}
    for n, t in enumerate(sorted(by_ticker), 1):
        rows = [r for r in st.daily(t) if r.get("put_call_alpaca") not in (None, "")]
        if not rows:
            continue
        scored = {d["date"]: d for d in S.score_days({t: rows}, 30.0, 10)}
        dates = [r["date"] for r in rows]
        closes = [C.to_float(r["stock_close"]) for r in rows]
        index = {d: i for i, d in enumerate(dates)}
        rets_all = [closes[k] / closes[k - 1] - 1 for k in range(1, len(closes)) if closes[k] and closes[k - 1]]
        stats[t] = (moves.get(t, 0), statistics.pstdev(rets_all) if len(rets_all) > 20 else 0.0)
        for d, g in by_ticker[t].items():
            i = index.get(d)
            if i is None or d not in scored or i + 11 >= len(dates) or not closes[i + 1] or not closes[i + 11]:
                continue
            rets = [closes[k] / closes[k - 1] - 1 for k in range(max(1, i - 19), i + 1) if closes[k] and closes[k - 1]]
            f = {k: scored[d].get(k) for k, _, _ in A.FEATURES if k in scored[d]}
            f["vol20_pct"] = round(statistics.pstdev(rets) * 100, 2) if len(rets) > 5 else None
            f.update(A.technicals(closes, i))
            price = closes[i]
            f["price_band"] = "<$10" if price < 10 else "$10-50" if price <= 50 else ">$50"
            shares = (closes[i + 11] * (1 - A.SHARE_COST)) / (closes[i + 1] * (1 + A.SHARE_COST)) - 1
            feats[(t, d)] = (g, f, round(shares * 100, 2))
        if n % 100 == 0:
            print(f"  {n}/{len(by_ticker)} stocks")
    bundle = deal_bundles(stats)
    month_split = split_months(sorted({month_of(d) for _, d in feats}))
    groups = {}
    for (t, d), (g, f, sh) in feats.items():
        b = bundle[t]
        s = "holdout" if b in HOLDOUT_BUNDLES and month_split.get(month_of(d)) != "test" else split_of(d, month_split)
        if s in ("skip", "buffer"):
            continue
        groups.setdefault((b, A.week_of(d), s), []).append((t, d))
    picked = []
    for key, items in groups.items():
        seen = set()
        for t, d in sorted(items, key=lambda x: A.rank("pool", x[0], x[1])):
            if t in seen:
                continue
            seen.add(t)
            picked.append((key, t, d))
            if len(seen) >= args.per_week:
                break
    want = {(t, d) for _, t, d in picked}
    options = {}
    with gzip.open(path, "rt", newline="") as f:
        for r in csv.DictReader(f):
            k = (r["ticker"], r["signal_date"])
            if k not in want:
                continue
            ok = r["filled"] == "yes" and r["entry_price"] and r["stock_close"]
            cell = f"{int(float(r['target_dte']))}d+{float(r['target_otm_pct']):g}"
            options.setdefault(k, {})[cell] = [
                round(float(r["entry_price"]) / float(r["stock_close"]) * 100, 2),
                C.to_float(r["ret_hold10_pct"]), C.to_float(r["ret_double_or_10_pct"])] if ok else None
    out = []
    for (b, wk, s), t, d in picked:
        g, f, sh = feats[(t, d)]
        out.append({"ticker": t, "signal_date": d, "bundle": b, "split": s, "week": wk, "month": month_of(d),
                    "grp": g, "features": json.dumps(f, separators=(",", ":")),
                    "options": json.dumps({k: v for k, v in options.get((t, d), {}).items() if v},
                                          separators=(",", ":")),
                    "shares_ret10": sh})
    st.backend.replace("pool", out)
    counts = {}
    for r in out:
        counts[r["split"]] = counts.get(r["split"], 0) + 1
    print(f"Pool built: {len(out):,} candidates {counts}; scoring months: "
          f"{sorted(m for m, s in month_split.items() if s == 'score')}")
    per_bundle = {b: sum(1 for r in out if r["bundle"] == b) for b in range(1, N_BUNDLES + 1)}
    print(f"Candidates per bundle: {per_bundle}")


def load_pool(st):
    pool = []
    for r in st.backend.read("pool"):
        o = {}
        for k, v in json.loads(r["options"]).items():
            if v:
                o[k] = {"cost_pct": v[0], "hold10": v[1], "double_or_10": v[2]}
        pool.append({"ticker": r["ticker"], "date": r["signal_date"], "bundle": int(r["bundle"]),
                     "split": r["split"], "week": r["week"], "month": r["month"],
                     "f": json.loads(r["features"]), "o": o, "shares": float(r["shares_ret10"])})
    return pool


# ---------------------------------------------------------------- rules and the scorebook
def clean_rules(raw):
    """Keep well-formed rules only; columns are the labels the agents see."""
    out = []
    for r in raw if isinstance(raw, list) else []:
        if not isinstance(r, dict):
            continue
        conds = []
        for c in r.get("when") or []:
            if not isinstance(c, dict):
                continue
            key, op, val = LABEL_TO_KEY.get(str(c.get("col", "")).strip()), str(c.get("op", "")).strip(), c.get("value")
            if not key or op not in OPS:
                continue
            if key == "price_band":
                if op != "=" or str(val) not in ("<$10", "$10-50", ">$50"):
                    continue
                conds.append({"col": c["col"], "op": op, "value": str(val)})
            else:
                try:
                    conds.append({"col": c["col"], "op": op, "value": float(val)})
                except (TypeError, ValueError):
                    continue
        if not conds or len(conds) > 5:
            continue
        rule = {"name": str(r.get("name") or "rule")[:80], "when": conds}
        if str(r.get("buy", "")).lower() == "stock":
            rule["buy"] = "stock"
        else:
            try:
                e, s = int(r.get("expiry")), float(r.get("strike"))
            except (TypeError, ValueError):
                continue
            if e not in A.EXPIRIES or s not in A.STRIKES:
                continue
            rule.update(buy="call", expiry=e, strike=s, exit=r.get("exit") if r.get("exit") in A.EXITS else "hold10")
        out.append(rule)
    return out[:8]


def rule_matches(rule, f):
    for c in rule["when"]:
        v = f.get(LABEL_TO_KEY[c["col"]])
        if v is None or v == "":
            return False
        if c["col"] != "price":
            v = float(v)
        if not OPS[c["op"]](v, c["value"]):
            return False
    return True


def rule_return(rule, cand):
    if rule["buy"] == "stock":
        return cand["shares"]
    return A.trade_return(cand, "call", rule["expiry"], rule["strike"], rule["exit"])


def boot_ci(values, stat=statistics.mean, reps=1000, seed=5):
    if len(values) < 5:
        return None, None
    rng = random.Random(seed)
    sims = sorted(stat([rng.choice(values) for _ in values]) for _ in range(reps))
    return round(sims[int(0.025 * reps)], 2), round(sims[int(0.975 * reps) - 1], 2)


def score_rule(rule, cands):
    rets, base, by_b, base_b, months = [], [], {}, {}, sorted({c["month"] for c in cands})
    half = months[len(months) // 2] if months else ""
    h1, h2 = [], []
    for c in cands:
        r = rule_return(rule, c)
        if r is None:
            continue
        base.append(r)
        base_b.setdefault(c["bundle"], []).append(r)
        if rule_matches(rule, c["f"]):
            rets.append(r)
            by_b.setdefault(c["bundle"], []).append(r)
            (h1 if c["month"] < half else h2).append(r)
    lo, hi = boot_ci(rets)
    beat = [b for b, v in by_b.items() if len(v) >= 3]
    return {"trades": len(rets),
            "mean_ret": round(statistics.mean(rets), 2) if rets else None,
            "median_ret": round(statistics.median(rets), 2) if rets else None,
            "win_rate": round(100 * sum(r > 0 for r in rets) / len(rets), 1) if rets else None,
            "ci_low": lo, "ci_high": hi,
            "baseline_mean": round(statistics.mean(base), 2) if base else None,
            "bundles_beat": sum(1 for b in beat if statistics.mean(by_b[b]) > statistics.mean(base_b[b])),
            "bundles_total": len(beat),
            "half1_mean": round(statistics.mean(h1), 2) if h1 else None,
            "half2_mean": round(statistics.mean(h2), 2) if h2 else None}


def describe_rule(rule):
    def val(v):
        return v if isinstance(v, str) else f"{v:g}"
    cond = " and ".join(f"{c['col']} {c['op']} {val(c['value'])}" for c in rule["when"])
    what = "buy the stock" if rule["buy"] == "stock" else \
        f"buy the {rule['expiry']}-day call {rule['strike']:g}% above the price, exit {rule['exit']}"
    return f"when {cond}: {what}"


def scorebook_line(rule, s):
    if not s["trades"]:
        return f"- {rule['name']} ({describe_rule(rule)}): matched no tradable training candidates."
    rng = f" (95% range {s['ci_low']:+.1f}% to {s['ci_high']:+.1f}%)" if s["ci_low"] is not None else " (too few trades for a range)"
    halves = f"; first half of the months {s['half1_mean']:+.1f}%, second half {s['half2_mean']:+.1f}%" \
        if s["half1_mean"] is not None and s["half2_mean"] is not None else ""
    return (f"- {rule['name']} ({describe_rule(rule)}): {s['trades']} trades, average {s['mean_ret']:+.1f}%{rng}, "
            f"median {s['median_ret']:+.1f}%, {s['win_rate']:.0f}% winners. Buying every candidate the same way: "
            f"{s['baseline_mean']:+.1f}%. Beat that in {s['bundles_beat']} of {s['bundles_total']} bundles{halves}.")


# ---------------------------------------------------------------- the model, with a shared budget
class Pot:
    def __init__(self, max_usd, spent_before):
        self.max_usd, self.spent_before, self.members = max_usd, spent_before, []
        self.lock = threading.Lock()

    def total(self):
        return self.spent_before + sum(m.cost for m in self.members)

    def llm(self, model):
        m = A.LLM(model, self.max_usd, 0.0)

        def check():
            if self.total() >= self.max_usd:
                raise A.Budget(f"spending cap of ${self.max_usd:.2f} reached")
        m.check_budget = check
        with self.lock:
            self.members.append(m)
        return m


class TimeUp(Exception):
    pass


# ---------------------------------------------------------------- prompts
COLUMN_LIST = ", ".join(f'"{label}"' for _, label, _ in A.FEATURES)


def system_text(phase):
    feedback = ("Results of each trade are shown to you two weeks (10 trading sessions) after you make it."
                if phase == "train" else
                "This is a blind scoring run: you will NOT see any results. Rely on your notes.")
    defs = "\n".join(f"- {label}: {meaning}" for _, label, meaning in A.FEATURES)
    return f"""You are one of four independent traders on a research committee, looking for a real, repeatable edge
in volatile US stocks with unusual options activity. Each week you see up to {PER_WEEK} candidate stock-days.

For EVERY candidate, give a rating: +2 strong buy, +1 lean buy, 0 no view, -1 lean avoid, -2 strong avoid
(you expect it to fall). Ratings are scored too: we check whether your higher-rated stocks did better
over the next 10 trading sessions.

Then you may buy up to {MAX_PICKS} of them. For each, either:
- the STOCK (sold 10 trading sessions later), or
- one CALL option: expiry 14, 30 or 90 days; strike at the money (0) or 5, 10, 15, 20 percent above the
  price; exit "hold10" (sell after 10 sessions) or "double_or_10" (sell as soon as it is worth 2x,
  otherwise after 10 sessions). Calls marked "n/a" did not trade that day and cannot be bought.
Every trade is ${A.TRADE_USD:,}.
YOUR GOAL: MAKE AS MUCH MONEY AS POSSIBLE. Your score is your total profit in dollars. A pass earns $0; a
trade earns its return on ${A.TRADE_USD:,} (+50% = +$500, -100% = -${A.TRADE_USD:,}). Trade when you believe the
odds favor you and pass when they don't. You buy at the next session's price; a 5% cost applies to each
side of an option trade and 0.1% to each side of a stock trade.
{feedback}

Stocks are anonymous codes and time is shown only as week numbers, on purpose: judge only from the
numbers. Columns:
{defs}
- option grid: the cost of each call as a percent of the stock price

Think it through silently, then reply with ONE compact JSON object and nothing else:
{{"ratings": {{"C1": 1, "C2": -2, "C3": 0}}, "picks": [{{"id": "C3", "buy": "stock"}}, {{"id": "C7", "buy": "call", "expiry": 90, "strike": 0, "exit": "hold10"}}], "why": "under 25 words"}}
Rate every candidate. Use "picks": [] to buy nothing this week."""


RULES_PROMPT = f"""Now turn your strongest ideas into testable rules. Code will test each rule on every training
candidate in all bundles, including stocks you never saw, and report the real numbers to the editor and
the next generation. A rule that only fit what you saw will be exposed, so state what you actually believe.

Reply with JSON only:
{{"rules": [{{"name": "short name", "when": [{{"col": "calls", "op": ">", "value": 3}}, {{"col": "vs ma20 %", "op": ">", "value": 0}}], "buy": "stock"}},
           {{"name": "short name", "when": [{{"col": "rsi", "op": "<", "value": 35}}], "buy": "call", "expiry": 90, "strike": 0, "exit": "hold10"}}]}}
Columns (exact names): {COLUMN_LIST}. Operators: >, >=, <, <=. The "price" column uses "=" with "<$10",
"$10-50" or ">$50". Up to 8 rules, each with 1 to 4 conditions. Rules can also say what to AVOID: describe
the bad setup and buy the stock, and the scorebook will show it losing."""


def parse_ratings(text, ids):
    out = {}
    data = A.parse_json(text)
    src = data.get("ratings") if isinstance(data, dict) and isinstance(data.get("ratings"), dict) else None
    pairs = src.items() if src else re.findall(r'"(C\d+)"\s*:\s*(-?\d)', text or "")
    for k, v in pairs:
        try:
            v = int(v)
        except (TypeError, ValueError):
            continue
        if k in ids and -2 <= v <= 2:
            out[k] = v
    return out


def rating_stats(ratings):
    """ratings: list of (rating, shares return). Rank correlation with a 95% range."""
    pts = [(r, x) for r, x in ratings if x is not None]
    if len(pts) < 20 or len({r for r, _ in pts}) < 2:
        return {}

    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0] * len(v)
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                rk[order[k]] = (i + j) / 2
            i = j + 1
        return rk

    def spearman(p):
        a, b = ranks([r for r, _ in p]), ranks([x for _, x in p])
        ma, mb = statistics.mean(a), statistics.mean(b)
        num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
        return num / den if den else 0.0

    rng = random.Random(9)
    sims = sorted(spearman([rng.choice(pts) for _ in pts]) for _ in range(300))
    top = [x for r, x in pts if r >= 1]
    bottom = [x for r, x in pts if r <= -1]
    return {"rated": len(pts), "rating_corr": round(spearman(pts), 3),
            "rating_corr_lo": round(sims[7], 3), "rating_corr_hi": round(sims[292], 3),
            "top_rated_ret": round(statistics.mean(top), 2) if top else None,
            "bottom_rated_ret": round(statistics.mean(bottom), 2) if bottom else None}


# ---------------------------------------------------------------- one agent's walk
class Walk:
    """One agent's run through one or more bundles. Collects trades, ratings, and weekly notes."""

    def __init__(self, run_id, llm, phase, deadline):
        self.run_id, self.llm, self.phase, self.deadline = run_id, llm, phase, deadline
        self.trades, self.ratings, self.weeks, self.week_rows = [], [], [], []
        self.replies = self.bad = self.cut = self.errors = 0
        self.sample = ""

    def bundle(self, cands_by_week, notes, scorebook, label):
        rng = random.Random(f"{self.run_id}-{label}")
        tickers = sorted({c["ticker"] for wk in cands_by_week.values() for c in wk})
        code = {t: f"S{n}" for t, n in zip(tickers, rng.sample(range(100, 10000), len(tickers)))}
        system = system_text(self.phase)
        start = len(self.trades)
        weeks = sorted(cands_by_week)
        for n, wk in enumerate(weeks, 1):
            if time.monotonic() > self.deadline:
                raise TimeUp()
            cands = [dict(c, id=f"C{i + 1}", code=code[c["ticker"]])
                     for i, c in enumerate(sorted(cands_by_week[wk], key=lambda c: A.rank(self.run_id, c["ticker"])))]
            wi = len(self.weeks)
            self.weeks.append(cands)
            parts = [f"Your notes:\n{notes.strip() or '(none yet: you are in the first generation)'}"]
            if scorebook:
                parts.append("Scorebook (rules from the last generation, tested by code on all training data):\n" + scorebook)
            mine = self.trades[start:]
            if self.phase == "train":
                shown = [t for t in mine if t["week"] <= (dt.date.fromisoformat(wk) - dt.timedelta(days=REVEAL_DAYS)).isoformat()]
                if shown:
                    rr = [t["ret_pct"] for t in shown]
                    parts.append(f"Your profit in this bundle so far: ${sum(rr) * A.TRADE_USD / 100:+,.0f} on {len(rr)} trades, "
                                 f"{100 * sum(r > 0 for r in rr) / len(rr):.0f}% winners. Most recent results "
                                 f"(what you saw -> result):\n" + "\n".join(
                                     f"- {t['code']} {A.describe_pick(t)}: calls {A.fmt(t['f'].get('call_volume_spike'))}x, "
                                     f"shares {A.fmt(t['f'].get('stock_volume_spike'))}x, 5d {A.fmt(t['f'].get('ret_5d_pct'), '{:+.1f}')}%, "
                                     f"vs ma20 {A.fmt(t['f'].get('vs_ma20_pct'), '{:+.1f}')}%, rsi {A.fmt(t['f'].get('rsi14'), '{:.0f}')} "
                                     f"-> {t['ret_pct']:+.1f}%" for t in shown[-10:]))
            parts.append(f"{label}, week {n} of {len(weeks)}. Candidates:\n{A.candidate_table(cands)}")
            try:
                reply = self.llm.chat([{"role": "system", "content": system},
                                       {"role": "user", "content": "\n\n".join(parts)}], max_tokens=2500)
            except RuntimeError as ex:       # the model API kept failing for this week: count it as a pass
                self.errors += 1
                self.week_rows.append({"run_id": self.run_id, "week_index": wi, "picks": 0, "finish": "error",
                                       "readable": "no", "why": f"[{label}] (model error) {str(ex)[:300]}"})
                if self.errors >= 10 and self.errors > 0.3 * (self.replies + self.errors):
                    raise
                continue
            self.replies += 1
            self.cut += self.llm.last_finish == "length"
            picks, why, ok = A.parse_picks(reply)
            by_id = {c["id"]: c for c in cands}
            rated = parse_ratings(reply, set(by_id))
            if not ok:
                self.bad += 1
                self.sample = self.sample or (reply or "(empty reply)")[:600]
                if self.replies >= 6 and self.bad > 0.6 * self.replies:
                    raise RuntimeError(f"model replies unreadable ({self.bad}/{self.replies}): {self.sample[:200]!r}")
            for cid, v in rated.items():
                c = by_id[cid]
                self.ratings.append({"run_id": self.run_id, "ticker": c["ticker"], "signal_date": c["date"],
                                     "rating": v, "shares_ret10": c["shares"]})
            used = set()
            for p in picks[:MAX_PICKS]:
                if not isinstance(p, dict):
                    continue
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
                    if e not in A.EXPIRIES or s not in A.STRIKES:
                        continue
                    spec = {"action": "call", "expiry": e, "strike_pct": s,
                            "exit_rule": p.get("exit") if p.get("exit") in A.EXITS else "hold10"}
                r = A.trade_return(c, spec["action"], spec["expiry"], spec["strike_pct"], spec["exit_rule"])
                if r is None:
                    continue
                used.add(c["id"])
                self.trades.append(dict(spec, run_id=self.run_id, week_index=wi, week=wk, cand_id=c["id"],
                                        code=c["code"], ticker=c["ticker"], signal_date=c["date"],
                                        ret_pct=round(r, 2), f=c["f"], reason=why[:300], bundle=c["bundle"]))
            self.week_rows.append({"run_id": self.run_id, "week_index": wi, "picks": len(used),
                                   "finish": self.llm.last_finish, "readable": "yes" if ok else "no",
                                   "why": (f"[{label}] " + (why if ok else "(unreadable) " + (reply or "")))[:500]})
        return self.trades[start:]

    def summary(self, generation, agent):
        rets = [t["ret_pct"] for t in self.trades]
        bm, bmed, bw = A.random_baseline(self.weeks, self.trades) if self.trades else (None, None, None)
        s = {"run_id": self.run_id, "lineage": "committee", "generation": generation, "phase": self.phase,
             "agent": agent, "model": self.llm.model, "weeks": len(self.weeks), "trades": len(rets),
             "mean_ret": round(statistics.mean(rets), 2) if rets else None,
             "median_ret": round(statistics.median(rets), 2) if rets else None,
             "win_rate": round(100 * sum(r > 0 for r in rets) / len(rets), 1) if rets else None,
             "baseline_mean": bm, "baseline_median": bmed, "baseline_win": bw,
             "profit_usd": round(sum(rets) * A.TRADE_USD / 100, 2),
             "baseline_profit_usd": round(bm * len(rets) * A.TRADE_USD / 100, 2) if bm is not None else None,
             "replies": self.replies, "bad_replies": self.bad, "cut_off": self.cut, "sample_reply": self.sample,
             "prompt_tokens": self.llm.prompt_tokens, "completion_tokens": self.llm.completion_tokens,
             "cost_usd": round(self.llm.cost, 4), "status": "complete",
             "finished": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        s.update(rating_stats([(r["rating"], r["shares_ret10"]) for r in self.ratings]))
        return s


def bundle_review(trades, ratings):
    rets = [t["ret_pct"] for t in trades]
    lines = []
    if rets:
        groups = {}
        for t in trades:
            groups.setdefault(A.describe_pick(t), []).append(t["ret_pct"])
        lines.append(f"Profit: ${sum(rets) * A.TRADE_USD / 100:+,.0f} on {len(rets)} trades, average {statistics.mean(rets):+.1f}%, "
                     f"median {statistics.median(rets):+.1f}%, {100 * sum(r > 0 for r in rets) / len(rets):.0f}% winners.")
        lines += [f"- {k}: {len(v)} trades, average {statistics.mean(v):+.1f}%, median {statistics.median(v):+.1f}%"
                  for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))]
    else:
        lines.append("You made no trades in this bundle.")
    by_r = {}
    for r in ratings:
        by_r.setdefault(r["rating"], []).append(r["shares_ret10"])
    if by_r:
        lines.append("How the stock did after each of your ratings (10 sessions, every candidate you rated):")
        lines += [f"- rated {k:+d}: {len(v)} stocks, average {statistics.mean(v):+.1f}%, median {statistics.median(v):+.1f}%"
                  for k, v in sorted(by_r.items(), reverse=True)]
    sample = sorted(trades, key=lambda t: t["ret_pct"])
    sample = sample[:10] + sample[-10:] if len(sample) > 20 else sample
    if sample:
        lines.append("Your worst and best trades (what you saw -> result):")
        for t in sample:
            f = t["f"]
            lines.append(f"- {A.describe_pick(t)}: " + ", ".join(
                f"{label} {A.fmt(f.get(k), '{:.1f}') if k != 'price_band' else f.get(k)}" for k, label, _ in A.FEATURES)
                + f" -> {t['ret_pct']:+.1f}%")
    return "\n".join(lines)


def agent_train(gen, agent, llm, notes, scorebook, pool, order, fraction, deadline):
    run_id = f"committee-g{gen}-agent{agent}-train-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}"
    walk = Walk(run_id, llm, "train", deadline)
    working = notes
    for k, b in enumerate(order, 1):
        cands = [c for c in pool if c["bundle"] == b and c["split"] == "train"]
        weeks = sorted({c["week"] for c in cands})
        keep = set(random.Random(f"weeks-g{gen}-b{b}").sample(weeks, max(1, round(len(weeks) * fraction))))
        by_week = {}
        for c in cands:
            if c["week"] in keep:
                by_week.setdefault(c["week"], []).append(c)
        label = f"Bundle {k} of {len(order)}"
        before = len(walk.ratings)
        trades = walk.bundle(by_week, working, scorebook, label)
        review = bundle_review(trades, walk.ratings[before:])
        last = k == len(order)
        prompt = f"""You finished {label.lower()} (a fresh group of stocks you had not seen). Here is how you did.

{review}

Your working notes going into this bundle:
{working.strip() or '(none)'}

Rewrite your working notes{' as your final notes for the committee editor' if last else ' before the next bundle (new stocks)'}.
Keep what held up, fix or drop what didn't, add what you learned. Write rules in terms of the columns
(thresholds, combinations, instrument, expiry, strike, exit), with the evidence behind each (how many trades,
returns, in how many bundles it held) and how confident you are. Be honest about small samples and about
ideas that worked in one bundle and failed in another. No stock codes. No length limit: be as thorough as
is useful, organized under headings. Reply with the notes only."""
        working = llm.chat([{"role": "user", "content": prompt}], max_tokens=12000)
        if llm.last_finish == "length":
            working += "\n\n(The notes were cut off here by the reply limit.)"
    reply = llm.chat([{"role": "user", "content": f"Your final notes:\n{working}\n\n{RULES_PROMPT}"}], max_tokens=3000)
    data = A.parse_json(reply)
    rules = clean_rules(data.get("rules") if isinstance(data, dict) else None)
    return walk, working, rules


def blind_run(gen, llm_for, notes, scorebook, pool, bundles, split, phase, deadline, label):
    """One agent trades the given split with no feedback; one thread per bundle."""
    run_id = f"committee-g{gen}-{label}-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}"

    def one(b):
        w = Walk(f"{run_id}-b{b}", llm_for(), phase, deadline)
        by_week = {}
        for c in pool:
            if c["bundle"] == b and c["split"] in split:
                by_week.setdefault(c["week"], []).append(c)
        w.bundle(by_week, notes, scorebook, f"Bundle {b}")
        return w
    with cf.ThreadPoolExecutor(len(bundles)) as ex:
        walks = list(ex.map(one, bundles))
    merged = Walk(run_id, walks[0].llm, phase, deadline)
    for w in walks:
        offset = len(merged.weeks)
        merged.weeks += w.weeks
        merged.trades += [dict(t, run_id=run_id, week_index=t["week_index"] + offset) for t in w.trades]
        merged.ratings += [dict(r, run_id=run_id) for r in w.ratings]
        merged.week_rows += [dict(r, run_id=run_id, week_index=r["week_index"] + offset) for r in w.week_rows]
        merged.replies += w.replies
        merged.bad += w.bad
        merged.cut += w.cut
        merged.sample = merged.sample or w.sample
    merged.llm = type("Sum", (), {"model": walks[0].llm.model,
                                  "prompt_tokens": sum(w.llm.prompt_tokens for w in walks),
                                  "completion_tokens": sum(w.llm.completion_tokens for w in walks),
                                  "cost": sum(w.llm.cost for w in walks)})()
    return merged


# ---------------------------------------------------------------- one generation
def editor(llm, gen, prev_notes, agent_outputs, book_lines):
    parts = [f"Notes the committee started this generation with:\n{prev_notes.strip() or '(none: first generation)'}"]
    for a, (notes, rules) in sorted(agent_outputs.items()):
        parts.append(f"=== Agent {a}'s final notes ===\n{notes.strip()}\n\nAgent {a}'s rules, as tested by code on ALL "
                     f"training candidates in all six bundles:\n" + ("\n".join(book_lines[a]) or "(no testable rules)"))
    prompt = "\n\n".join(parts) + """

You are the committee editor. Four traders worked independently on the same stocks and weeks. Write the
notes the next generation will start from; it will see ONLY your notes and the code-tested scorebook of
the rules you state next, never these traders' notes or trades.
Weigh the evidence: trust rules the code confirmed across many trades and most bundles, and treat ideas
that only one trader saw, or that the code did not confirm, as weak. Say where the traders agreed and
where they disagreed. Keep useful ideas that still need testing, clearly marked as untested. No stock
codes. No length limit: be as thorough as is useful, organized under headings. Reply with the notes only."""
    notes = llm.chat([{"role": "user", "content": prompt}], max_tokens=12000)
    if llm.last_finish == "length":
        notes += "\n\n(The notes were cut off here by the reply limit.)"
    reply = llm.chat([{"role": "user", "content": f"Your notes:\n{notes}\n\n{RULES_PROMPT}"}], max_tokens=3000)
    data = A.parse_json(reply)
    return notes, clean_rules(data.get("rules") if isinstance(data, dict) else None)


STAT_KEYS = ("trades", "mean_ret", "median_ret", "win_rate", "ci_low", "ci_high", "baseline_mean",
             "bundles_beat", "bundles_total", "half1_mean", "half2_mean")


def stats_of(row):
    out = {k: (C.to_float(row[k]) if row[k] not in (None, "") else None) for k in STAT_KEYS}
    for k in ("trades", "bundles_beat", "bundles_total"):
        out[k] = int(out[k] or 0)
    return out


def book_text(st, g):
    """The editor's rules for generation g with their TRAINING numbers only (what may be passed on)."""
    book = [r for r in st.backend.read("scorebook")
            if int(r["generation"]) == g and r["author"] == "editor" and r["period"] == "train"]
    return "\n".join(scorebook_line(json.loads(r["rule"]), stats_of(r)) for r in book)


def inherited(st):
    rows = [r for r in st.backend.read("committee_notes") if r["author"] == "editor"]
    if not rows:
        return 0, "", ""
    last = max(rows, key=lambda r: int(r["generation"]))
    g = int(last["generation"])
    return g, last["text"], book_text(st, g)


def book_rows(gen, author, period, rules, cands):
    rows, lines = [], []
    for r in rules:
        s = score_rule(r, cands)
        if s["trades"]:
            s["trades"] = int(s["trades"])
        rows.append(dict(s, generation=gen, author=author, rule_name=r["name"], period=period, rule=json.dumps(r)))
        lines.append(scorebook_line(r, s))
    # Several rules can share a name; keep them apart in the table.
    seen = {}
    for row in rows:
        n = seen[row["rule_name"]] = seen.get(row["rule_name"], 0) + 1
        if n > 1:
            row["rule_name"] = f"{row['rule_name']} ({n})"
    return rows, lines


def run_generation(st, args, pool, deadline, pot):
    gen_before, notes, scorebook = inherited(st)
    gen = gen_before + 1
    order = list(TRAIN_BUNDLES)
    random.Random(f"order-g{gen}").shuffle(order)
    print(f"Generation {gen}: bundle order {order}, {N_AGENTS} agents, {args.weeks_fraction:.0%} of training weeks.")
    with cf.ThreadPoolExecutor(N_AGENTS) as ex:
        futs = {a: ex.submit(agent_train, gen, a, pot.llm(args.model), notes, scorebook, pool, order,
                             args.weeks_fraction, deadline) for a in range(1, N_AGENTS + 1)}
        results = {a: f.result() for a, f in futs.items()}
    train_cands = [c for c in pool if c["split"] == "train" and c["bundle"] in TRAIN_BUNDLES]
    score_cands = [c for c in pool if c["split"] == "score" and c["bundle"] in TRAIN_BUNDLES]
    agent_out, lines, book = {}, {}, []
    for a, (walk, working, rules) in results.items():
        rows, ls = book_rows(gen, f"agent{a}", "train", rules, train_cands)
        book += rows
        lines[a] = ls
        agent_out[a] = (working, rules)
        print(f"  agent {a}: {len(walk.trades)} trades, ${sum(t['ret_pct'] for t in walk.trades) * 10:+,.0f}, "
              f"{len(rules)} rules, {walk.bad}/{walk.replies} unreadable")
    ed = pot.llm(args.model)
    ed_notes, ed_rules = editor(ed, gen, notes, agent_out, lines)
    rows, ed_lines = book_rows(gen, "editor", "train", ed_rules, train_cands)
    book += rows
    srows, s_lines = book_rows(gen, "editor", "score", ed_rules, score_cands)
    book += srows
    scoring = blind_run(gen, lambda: pot.llm(args.model), ed_notes, "\n".join(ed_lines), pool,
                        TRAIN_BUNDLES, ("score",), "score", deadline, "scoring")
    # Everything finished: write the generation in one go, on a fresh connection (the one opened at
    # the start may have been dropped while the agents worked; Neon closes idle connections).
    C._STORE = None
    st = C.db()
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    runs, trades, ratings, weeks = [], [], [], []
    for a, (walk, working, rules) in results.items():
        runs.append(dict(walk.summary(gen, f"agent{a}"), started=now))
        trades += walk.trades
        ratings += walk.ratings
        weeks += walk.week_rows
    sc = scoring.summary(gen, "scorer")
    sc["cost_usd"] = round(scoring.llm.cost + ed.cost, 4)   # the editor's calls are billed with the scoring run
    runs.append(dict(sc, started=now))
    trades += scoring.trades
    ratings += scoring.ratings
    weeks += scoring.week_rows
    keep = ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action", "expiry", "strike_pct",
            "exit_rule", "ret_pct", "reason")
    st.backend.upsert("agent_runs", runs)
    st.backend.upsert("agent_trades", [{k: t.get(k) for k in keep} for t in trades])
    st.backend.upsert("agent_ratings", ratings)
    st.backend.upsert("agent_weeks", weeks)
    st.backend.upsert("scorebook", book)
    notes_rows = [{"generation": gen, "author": f"agent{a}", "model": args.model, "text": w, "rules": json.dumps(r),
                   "created": now} for a, (w, r) in agent_out.items()]
    notes_rows.append({"generation": gen, "author": "editor", "model": args.model, "text": ed_notes,
                       "rules": json.dumps(ed_rules), "created": now})
    st.backend.upsert("committee_notes", notes_rows)
    print(f"Generation {gen} done: scoring run {sc['trades']} trades, profit ${sc['profit_usd']:+,.0f} "
          f"(random ${sc['baseline_profit_usd'] or 0:+,.0f}), rating correlation {sc.get('rating_corr')} "
          f"({sc.get('rating_corr_lo')} to {sc.get('rating_corr_hi')}); generation cost ${pot.total() - pot.spent_before:.2f}")
    print("Editor rules on the blind scoring months:\n" + ("\n".join(s_lines) or "(none)"))
    return gen


def spent(st):
    return sum(C.to_float(r["cost_usd"]) or 0 for r in st.backend.read("agent_runs"))


def loop(args):
    st = C.db()
    pool = load_pool(st)
    if not pool:
        sys.exit("The candidate pool is empty: run `python committee.py build-pool --archive ...` first.")
    deadline = time.monotonic() + 60 * args.max_minutes
    started, done, stop = time.monotonic(), 0, None
    for _ in range(args.generations):
        per_gen = (time.monotonic() - started) / done if done else 60 * 35
        if time.monotonic() + 1.3 * per_gen > deadline:
            print("Not enough time left for another generation in this round; stopping cleanly.")
            break
        C._STORE = None              # fresh connection for every generation
        st = C.db()
        pot = Pot(args.max_usd, spent(st))
        try:
            run_generation(st, args, pool, deadline, pot)
            done += 1
            continue
        except A.Budget as b:
            stop = f"spending cap: {b}"
        except TimeUp:
            print("Ran out of time mid-generation; it will be redone from the start next round.")
        except Exception as ex:   # noqa: BLE001 - record any crash where the report can show it
            stop = f"error: {type(ex).__name__}: {ex}"
            tb = traceback.format_exc()
            print(tb)
            with open(os.path.join(C.ROOT, "committee_error.txt"), "w") as f:
                f.write(f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC\n{tb[-3000:]}")
        # The generation did not finish: still count what it spent, so the cap stays honest.
        cost = pot.total() - pot.spent_before
        if cost > 0:
            st.backend.upsert("agent_runs", [{
                "run_id": f"committee-unfinished-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}",
                "lineage": "committee", "generation": inherited(st)[0] + 1, "phase": "unfinished",
                "agent": "all", "model": args.model, "cost_usd": round(cost, 4), "status": stop or "time limit",
                "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}])
        break
    remaining = 0 if stop else max(0, args.generations - done)
    if done == 0 and remaining and not stop:
        # A generation that can't finish in one round would repeat forever.
        print("No generation finished this round, so not scheduling another.")
        remaining = 0
    with open(os.path.join(C.ROOT, "committee_status.txt"), "w") as f:
        f.write(str(remaining))
    print(f"This round: {done} generation(s). Remaining: {remaining}" + (f" ({stop})" if stop else ""))
    report(args)


def final_test(args):
    """The one-time exam: the chosen generation's editor notes on held-back stocks and the test months."""
    st = C.db()
    pool = load_pool(st)
    rows = [r for r in st.backend.read("committee_notes")
            if r["author"] == "editor" and int(r["generation"]) == args.generation]
    if not rows:
        sys.exit(f"No editor notes for generation {args.generation}.")
    if any(r.get("phase") == "test" and r.get("lineage") == "committee" and r["generation"] == str(args.generation)
           for r in st.backend.read("agent_runs")):
        print("Note: this generation already took the exam; a repeat is no longer a clean test.")
    rules = clean_rules(json.loads(rows[0]["rules"] or "[]"))
    book = book_text(st, args.generation)
    pot = Pot(args.max_usd, spent(st))
    deadline = time.monotonic() + 60 * args.max_minutes
    exam = [c for c in pool if c["split"] in ("test", "holdout")]
    w = blind_run(args.generation, lambda: pot.llm(args.model), rows[0]["text"], book, exam,
                  tuple(range(1, N_BUNDLES + 1)), ("test", "holdout"), "test", deadline, "final-exam")
    s = w.summary(args.generation, "exam")
    st.backend.upsert("agent_runs", [dict(s, started=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))])
    keep = ("run_id", "week_index", "cand_id", "ticker", "signal_date", "action", "expiry", "strike_pct",
            "exit_rule", "ret_pct", "reason")
    st.backend.upsert("agent_trades", [{k: t.get(k) for k in keep} for t in w.trades])
    st.backend.upsert("agent_ratings", w.ratings)
    st.backend.upsert("agent_weeks", w.week_rows)
    rows_b, lines = book_rows(args.generation, "editor", "test", rules, exam)
    st.backend.upsert("scorebook", rows_b)
    print(f"Final exam: {s['trades']} trades, profit ${s['profit_usd']:+,.0f} (random ${s['baseline_profit_usd'] or 0:+,.0f}); "
          f"rating correlation {s.get('rating_corr')} ({s.get('rating_corr_lo')} to {s.get('rating_corr_hi')})")
    print("Editor rules on the exam:\n" + "\n".join(lines))
    report(args)


# ---------------------------------------------------------------- report
def report(args=None):
    st = C.db()
    runs = [r for r in st.backend.read("agent_runs") if r["lineage"] == "committee"]
    notes = st.backend.read("committee_notes")
    book = st.backend.read("scorebook")
    pool_counts = {}
    for r in st.backend.read("pool"):
        pool_counts[r["split"]] = pool_counts.get(r["split"], 0) + 1
    L = [f"# Committee generations ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
         f"Total spent on all agent runs: ${spent(st):.2f}. Candidate pool: {pool_counts}.", "",
         "Four agents train independently on six stock bundles; code scores their rules; an editor writes the",
         "notes passed on. The scoring run trades blind months with the editor's notes. \"Random\" makes the same",
         "number and kind of trades on random candidates in the same weeks. Rating correlation: does a higher",
         "rating go with a better 10-session stock return (0 = no skill, ranges are 95%). Every trade is $1,000.", "",
         "## Runs", "",
         "| gen | who | phase | trades | profit $ | random profit $ | mean % | win % | rating corr (95% range) | top rated % | bottom rated % | unreadable | cost $ |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(runs, key=lambda r: (int(r["generation"] or 0), r["phase"] != "train", r["agent"] or "")):
        corr = f"{r['rating_corr']} ({r['rating_corr_lo']} to {r['rating_corr_hi']})" if r.get("rating_corr") else "-"
        L.append(f"| {r['generation']} | {r['agent']} | {r['phase']} | {r['trades']} | {r['profit_usd']} | "
                 f"{r['baseline_profit_usd'] or '-'} | {r['mean_ret'] or '-'} | {r['win_rate'] or '-'} | {corr} | "
                 f"{r.get('top_rated_ret') or '-'} | {r.get('bottom_rated_ret') or '-'} | "
                 f"{r.get('bad_replies') or 0}/{r.get('replies')} | {r['cost_usd']} |")
    gens = sorted({int(n["generation"]) for n in notes})
    for g in reversed(gens):
        L += ["", f"## Generation {g}", ""]
        for period, title in (("train", "Editor's rules, tested on all training months and bundles"),
                              ("score", "The same rules on the blind scoring months (never shown to agents)"),
                              ("test", "The same rules on the final exam")):
            rows = [b for b in book if int(b["generation"]) == g and b["author"] == "editor" and b["period"] == period]
            if rows:
                L += [f"### {title}", ""]
                L += [scorebook_line(json.loads(b["rule"]), stats_of(b)) for b in rows]
                L.append("")
        for n in sorted((n for n in notes if int(n["generation"]) == g),
                        key=lambda n: (n["author"] != "editor", n["author"])):
            who = "Editor's notes (passed to the next generation)" if n["author"] == "editor" else \
                f"Agent {n['author'][-1]}'s final notes (not passed on)"
            L += [f"### {who}", "", n["text"] or "(empty)", ""]
    err = os.path.join(C.ROOT, "committee_error.txt")
    if os.path.exists(err):
        L += ["", "## Last error", "", "```", open(err).read(), "```"]
    with open(os.path.join(C.ROOT, "COMMITTEE.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[:40]))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build-pool")
    b.add_argument("--archive", required=True)
    b.add_argument("--per-week", type=int, default=PER_WEEK)
    for name in ("loop", "final-test"):
        a = sub.add_parser(name)
        a.add_argument("--model", default=os.environ.get("LLM_MODEL", "anthropic/claude-haiku-5.5"))
        a.add_argument("--max-usd", type=float, default=float(os.environ.get("MAX_USD", "25")))
        a.add_argument("--max-minutes", type=float, default=140)
        if name == "loop":
            a.add_argument("--generations", type=int, default=1)
            a.add_argument("--weeks-fraction", type=float, default=0.5)
        else:
            a.add_argument("--generation", type=int, required=True)
    sub.add_parser("report")
    a = p.parse_args()
    {"build-pool": build_pool, "loop": loop, "final-test": final_test, "report": report}[a.cmd](a)


if __name__ == "__main__":
    main()
