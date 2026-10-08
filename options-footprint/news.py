"""
News for the agents: how much news each candidate stock had, its tone, and whether heavy call buying
came with NO news (the footprint the project is looking for).

    python news.py update --max-minutes 120      # fetch, score, and add the news columns to the pool

1. FETCH: every headline Alpaca (Benzinga) has for each pool stock since February 2024. Articles about
   more than 3 stocks (market roundups) are kept but not counted, since they aren't about the company.
2. SCORE: a cheap model rates each needed headline's tone for the stock from -1 to +1. Only headlines
   within 7 days before some candidate day are scored. The cost counts toward the spending cap.
3. APPLY: each pool candidate gets news counts for the 1, 3 and 7 days before that day's close, the
   average tone over 7 days, and a "call spike with no news" flag.

The trading agents NEVER see headline text: it would name the company and hint at the date, so a model
could recognize the story and remember what happened next. They see only the numbers.
Resumable: fetching is done stock by stock, scoring headline by headline. Writes 'done' or 'more' to
news_status.txt so the workflow can launch another round.
"""
import argparse
import bisect
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collector as C  # noqa: E402
import agents as A     # noqa: E402

START = "2024-02-01T00:00:00Z"
CLOSE_UTC = "20:00:00"          # 4 PM New York in summer; in winter this cuts off an hour early (safe side)
MAX_SYMBOLS = 3                 # articles naming more stocks than this are roundups, not company news
QUIET_SPIKE = 3.0               # "heavy call buying": call volume at least this many times normal
SCORE_BATCH = 40
WINDOW_DAYS = 7
STATUS_FILE = os.path.join(C.ROOT, "news_status.txt")


# ---------------------------------------------------------------- fetch
def fetch(st, tickers, deadline):
    done = {r["ticker"] for r in st.backend.read("news_fetched")}
    todo = [t for t in tickers if t not in done]
    print(f"News: {len(done)} stocks fetched, {len(todo)} to go.")
    end = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for n, t in enumerate(todo, 1):
        if time.monotonic() > deadline:
            return False
        try:
            pages = C.alpaca_get("https://data.alpaca.markets", "/v1beta1/news",
                                 {"symbols": t, "start": START, "end": end, "limit": 50, "sort": "asc",
                                  "include_content": "false"})
        except Exception as ex:   # noqa: BLE001 - one stock's news failing shouldn't stop the rest
            C.log_error({"ticker": t, "event_date": "news"}, ex)
            print(f"  {t}: FAILED {str(ex)[:150]}")
            continue
        rows = {}
        for page in pages:
            for a in (page.get("news") or []) if isinstance(page, dict) else []:
                syms = a.get("symbols") or []
                rows[str(a["id"])] = {"id": str(a["id"]), "ticker": t, "created_at": a.get("created_at", ""),
                                      "headline": (a.get("headline") or "")[:300], "n_symbols": len(syms)}
        st.backend.upsert("news", list(rows.values()))
        st.backend.upsert("news_fetched", [{"ticker": t, "through": end, "articles": len(rows)}])
        if n % 50 == 0:
            print(f"  {n}/{len(todo)} stocks")
    return True


# ---------------------------------------------------------------- the index used for features
class Index:
    """Per stock: company-specific articles sorted by time, with their tone where scored."""

    def __init__(self, st, tickers=None):
        want = set(tickers) if tickers else None
        self.by = {}
        for r in st.backend.read("news"):
            if (want and r["ticker"] not in want) or int(float(r["n_symbols"] or 0)) > MAX_SYMBOLS:
                continue
            s = C.to_float(r.get("sentiment"))
            self.by.setdefault(r["ticker"], []).append((r["created_at"], s, r["id"], r["headline"]))
        for v in self.by.values():
            v.sort()
        self.keys = {t: [x[0] for x in v] for t, v in self.by.items()}
        self.fetched = {r["ticker"] for r in st.backend.read("news_fetched")}

    def window(self, ticker, date, days):
        """Articles in the `days` days before `date`'s close (only what was public by then)."""
        end = f"{date}T{CLOSE_UTC}"
        start = (dt.datetime.fromisoformat(end) - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S")
        keys = self.keys.get(ticker, [])
        return self.by.get(ticker, [])[bisect.bisect_right(keys, start):bisect.bisect_right(keys, end + "Z")]

    def features(self, ticker, date, call_spike):
        if ticker not in self.fetched:
            return {k: None for k in ("news_1d", "news_3d", "news_7d", "news_sent_7d", "quiet_spike")}
        n1, n3, n7 = (len(self.window(ticker, date, d)) for d in (1, 3, 7))
        tones = [s for _, s, _, _ in self.window(ticker, date, 7) if s is not None]
        spike = C.to_float(call_spike)
        return {"news_1d": n1, "news_3d": n3, "news_7d": n7,
                "news_sent_7d": round(sum(tones) / len(tones), 2) if tones else None,
                "quiet_spike": None if spike is None else int(spike >= QUIET_SPIKE and n3 == 0)}


# ---------------------------------------------------------------- score
PROMPT = """Rate each headline's likely effect on the named company's stock price over the next two weeks,
from -1 (clearly bad) through 0 (neutral or unclear) to +1 (clearly good). Judge only the headline itself.
Reply with JSON only, mapping each number to a score, for example {"1": 0.5, "2": -1, "3": 0}.

"""


def score(st, pool, model, max_usd, deadline):
    import committee as K   # the shared spending cap
    idx = Index(st, {c["ticker"] for c in pool})
    need = {}
    for c in pool:
        for _, s, aid, head in idx.window(c["ticker"], c["date"], WINDOW_DAYS):
            if s is None and head:
                need[aid] = (c["ticker"], head)
    items = sorted(need.items())
    print(f"News tone: {len(items):,} headlines to score.")
    if not items:
        return True
    pot = K.Pot(max_usd, K.spent(st))
    batches = [items[i:i + SCORE_BATCH] for i in range(0, len(items), SCORE_BATCH)]
    lock = __import__("threading").Lock()
    out = []

    def one(batch):
        if time.monotonic() > deadline:
            return []
        llm = pot.llm(model)
        text = PROMPT + "\n".join(f"{i}. [{t}] {h}" for i, (_, (t, h)) in enumerate(batch, 1))
        try:
            reply = llm.chat([{"role": "user", "content": text}], max_tokens=1500)
        except RuntimeError as ex:
            print(f"  batch failed: {str(ex)[:120]}")
            return []
        data = A.parse_json(reply) or {}
        if not data:
            data = dict(re.findall(r'"(\d+)"\s*:\s*(-?[\d.]+)', reply or ""))
        rows = []
        for i, (aid, (t, _)) in enumerate(batch, 1):
            try:
                v = max(-1.0, min(1.0, float(data.get(str(i)))))
            except (TypeError, ValueError):
                continue
            rows.append({"id": aid, "ticker": t, "sentiment": round(v, 2)})
        return rows
    with cf.ThreadPoolExecutor(6) as ex:
        for rows in ex.map(one, batches):
            with lock:
                out += rows
            if len(out) >= 2000:
                save_scores(st, out)
                out = []
    save_scores(st, out)
    cost = pot.total() - pot.spent_before
    st.backend.upsert("agent_runs", [{"run_id": f"news-tone-{dt.datetime.now(dt.timezone.utc):%Y%m%d%H%M%S}",
                                      "lineage": "news", "phase": "scoring", "model": model,
                                      "cost_usd": round(cost, 4), "status": "complete",
                                      "started": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}])
    finished = time.monotonic() <= deadline   # every batch was tried; any the model fumbled stay blank
    left = sum(1 for aid, _ in items if aid not in scored_ids(st))
    print(f"News tone: ${cost:.2f} spent; {len(items) - left:,} of {len(items):,} headlines scored.")
    return finished


def save_scores(st, rows):
    # The same article can be filed under several stocks: give every copy the score.
    if not rows:
        return
    if st.kind == "postgres":
        with st.backend.conn.cursor() as cur:
            cur.executemany("update news set sentiment = %s where id = %s", [(r["sentiment"], r["id"]) for r in rows])
    else:
        st.backend.upsert("news", rows)


def scored_ids(st):
    return {r["id"] for r in st.backend.read("news") if r.get("sentiment") not in (None, "")}


# ---------------------------------------------------------------- apply to the pool
def apply(st):
    rows = st.backend.read("pool")
    idx = Index(st, {r["ticker"] for r in rows})
    upd = []
    for r in rows:
        f = json.loads(r["features"])
        f.update(idx.features(r["ticker"], r["signal_date"], f.get("call_volume_spike")))
        upd.append({"ticker": r["ticker"], "signal_date": r["signal_date"], "features": json.dumps(f, separators=(",", ":"))})
    for i in range(0, len(upd), 2000):
        st.backend.upsert("pool", upd[i:i + 2000])
    with_news = sum(1 for u in upd if json.loads(u["features"]).get("news_7d"))
    quiet = sum(1 for u in upd if json.loads(u["features"]).get("quiet_spike") == 1)
    print(f"News columns added to {len(upd):,} candidates: {with_news:,} had news in the prior week; "
          f"{quiet:,} were call spikes with no news in the prior 3 days.")


def update(args):
    import committee as K
    st = C.db()
    deadline = time.monotonic() + 60 * args.max_minutes
    pool = K.load_pool(st)
    if not pool:
        sys.exit("The pool is empty: build it first (committee.py build-pool).")
    finished = fetch(st, sorted({c["ticker"] for c in pool}), deadline)
    if finished:
        finished = score(st, pool, args.model, args.max_usd, deadline)
    apply(st)
    with open(STATUS_FILE, "w") as f:
        f.write("done" if finished else "more")
    print("News complete." if finished else "News not finished; another round needed.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("update")
    u.add_argument("--max-minutes", type=float, default=120)
    u.add_argument("--model", default=os.environ.get("LLM_MODEL", "anthropic/claude-haiku-5.5"))
    u.add_argument("--max-usd", type=float, default=float(os.environ.get("MAX_USD", "25")))
    a = p.parse_args()
    {"update": update}[a.cmd](a)


if __name__ == "__main__":
    main()
