"""
Storage for the options footprint project.

If the DATABASE_URL environment variable is set (your Neon connection string), everything is
read from and written to Postgres. Otherwise it falls back to CSV files in data/, which is handy
for testing on a laptop.

Both backends hand rows back as dicts of strings ("" for empty), exactly like csv.DictReader,
so the rest of the code doesn't care which one is in use.
"""
import csv
import datetime as dt
import os
import sqlite3
import threading

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

T, F, I, D = "text", "double precision", "bigint", "date"

EVENT_COLS = {"ticker": T, "event_date": D, "event_type": T, "move_pct": F, "prior_close": F,
              "event_close": F, "catalyst": T, "label": T, "notes": T,
              "window_filled": T}   # "yes" once the pre-move window has options data
DAILY_COLS = {"ticker": T, "date": D, "put_call_ratio": F, "put_call_alpaca": F,
              "call_volume": I, "put_volume": I, "short_otm_call_volume": I,
              "call_vol_short": I, "call_vol_medium": I, "call_vol_long": I,
              "call_vol_otm": I, "call_vol_atm": I, "call_vol_itm": I,
              "stock_close": F, "stock_volume": I, "source_put_call": T, "source_price": T}
FEATURE_COLS = {"ticker": T, "event_date": D, "label": T, "move_pct": F, "days_with_put_call": I,
                "baseline_put_call_median": F, "recent_put_call_min": F, "put_call_drop_ratio": F,
                "window_put_call_min": F, "sessions_from_low_to_event": I,
                "call_volume_recent_vs_baseline": F, "short_otm_call_recent_max": I,
                "short_otm_call_recent_vs_baseline": F,
                "call_vol_short_spike": F, "call_vol_medium_spike": F, "call_vol_long_spike": F,
                "call_vol_otm_spike": F, "call_vol_atm_spike": F, "call_vol_itm_spike": F,
                "stock_volume_last_vs_avg": F, "price_change_in_window_pct": F,
                "max_daily_abs_move_pct": F}
HISTORY_COLS = {"ticker": T, "completed": D}
ERROR_COLS = {"logged_at": T, "ticker": T, "event_date": T, "error": T}
REPORT_COLS = {"run_date": D, "move_pct": F, "horizon_days": I, "rule": T, "days_fired": I,
               "episodes": I, "hit_rate_pct": F, "lift": F, "drop_lift": F,
               "avg_fwd_return_pct": F, "median_fwd_return_pct": F, "avg_fwd_max_gain_pct": F,
               "lift_half1": F, "fired_half1": I, "lift_half2": F, "fired_half2": I}
# The daily shortlist for the investigator agent. The verdict columns are left empty here and
# filled in later by the agent, so its calls can be scored against what actually happened.
FLAG_COLS = {"signal_date": D, "ticker": T, "rule": T, "close": F, "call_volume_spike": F,
             "call_vol_long_spike": F, "put_call_drop": F, "stock_volume_spike": F,
             "ret_5d_pct": F, "rule_lift": F, "rule_hit_rate_pct": F,
             "verdict": T, "verdict_notes": T, "reviewed_at": T,
             "fwd_return_pct": F, "fwd_max_gain_pct": F}

# The ladder backtest: hypothetical call purchases across strikes and expirations after each
# flag (and on random control days), with the result under several exit rules.
LADDER_COLS = {"grp": T, "rules": T, "ticker": T, "signal_date": D, "entry_date": D,
               "contract": T, "target_dte": I, "dte": I, "target_otm_pct": F, "strike": F,
               "expiration": D, "stock_close": F, "entry_price": F, "filled": T,
               "ret_hold10_pct": F, "ret_double_or_10_pct": F, "ret_expiry_pct": F,
               "peak_10_pct": F}
LADDER_REPORT_COLS = {"run_date": D, "grp": T, "target_dte": I, "target_otm_pct": F, "exit_rule": T,
                      "trades": I, "win_rate_pct": F, "mean_ret_pct": F, "median_ret_pct": F,
                      "mean_peak_pct": F}

# The agent loop ("trader generations"): a fixed, anonymized sample of candidate days; each
# generation's runs, trades, and the lessons document it passes on.
ARENA_COLS = {"ticker": T, "signal_date": D, "period": T, "week": D, "grp": T, "features": T,
              "options": T, "shares_ret10": F}
AGENT_RUN_COLS = {"run_id": T, "lineage": T, "generation": I, "phase": T, "model": T, "started": T,
                  "finished": T, "weeks": I, "trades": I, "mean_ret": F, "median_ret": F,
                  "win_rate": F, "baseline_mean": F, "baseline_median": F, "baseline_win": F,
                  "prompt_tokens": I, "completion_tokens": I, "cost_usd": F, "status": T,
                  "profit_usd": F, "baseline_profit_usd": F, "replies": I, "bad_replies": I, "cut_off": I,
                  "sample_reply": T, "agent": T, "rating_corr": F, "rating_corr_lo": F, "rating_corr_hi": F,
                  "top_rated_ret": F, "bottom_rated_ret": F, "rated": I}
AGENT_TRADE_COLS = {"run_id": T, "week_index": I, "cand_id": T, "ticker": T, "signal_date": D,
                    "action": T, "expiry": I, "strike_pct": F, "exit_rule": T, "ret_pct": F,
                    "reason": T}
AGENT_WEEK_COLS = {"run_id": T, "week_index": I, "picks": I, "why": T, "finish": T, "readable": T}
# Committee version: a larger candidate pool split into stock bundles and month blocks, notes per
# generation and author, a code-kept scorebook of every rule, and every rating an agent gives.
POOL_COLS = {"ticker": T, "signal_date": D, "bundle": I, "split": T, "week": D, "month": T, "grp": T,
             "features": T, "options": T, "shares_ret10": F, "universe": T}
# Stocks chosen without hindsight: liquid, optionable stocks picked using only January 2024 data
# (before any of the history the agents study), whether or not they later had big moves.
WIDE_COLS = {"ticker": T, "status": T, "avg_price": F, "avg_volume": F, "selected": T}
BUNDLE_COLS = {"ticker": T, "bundle": I, "universe": T}
COMMITTEE_NOTE_COLS = {"lineage": T, "generation": I, "author": T, "model": T, "text": T, "rules": T, "created": T}
SCOREBOOK_COLS = {"lineage": T, "generation": I, "author": T, "rule_name": T, "period": T, "rule": T, "trades": I,
                  "mean_ret": F, "median_ret": F, "win_rate": F, "ci_low": F, "ci_high": F,
                  "baseline_mean": F, "bundles_beat": I, "bundles_total": I, "half1_mean": F, "half2_mean": F}
RATING_COLS = {"run_id": T, "ticker": T, "signal_date": D, "rating": I, "shares_ret10": F}
LESSON_COLS = {"lineage": T, "generation": I, "run_id": T, "model": T, "text": T, "created": T}

TABLES = {
    "events": (EVENT_COLS, ["ticker", "event_date"]),
    "controls": (EVENT_COLS, ["ticker", "event_date"]),
    "daily": (DAILY_COLS, ["ticker", "date"]),
    "event_features": (FEATURE_COLS, ["ticker", "event_date"]),
    "history_done": (HISTORY_COLS, ["ticker"]),
    "errors": (ERROR_COLS, None),
    "signal_report": (REPORT_COLS, ["move_pct", "horizon_days", "rule"]),
    "flags": (FLAG_COLS, ["signal_date", "ticker", "rule"]),
    "ladder_trades": (LADDER_COLS, ["grp", "ticker", "signal_date", "target_dte", "target_otm_pct"]),
    "ladder_report": (LADDER_REPORT_COLS, ["grp", "target_dte", "target_otm_pct", "exit_rule"]),
    "arena": (ARENA_COLS, ["ticker", "signal_date"]),
    "agent_runs": (AGENT_RUN_COLS, ["run_id"]),
    "agent_trades": (AGENT_TRADE_COLS, ["run_id", "ticker", "signal_date"]),
    "agent_weeks": (AGENT_WEEK_COLS, ["run_id", "week_index"]),
    "pool": (POOL_COLS, ["ticker", "signal_date"]),
    "wide_universe": (WIDE_COLS, ["ticker"]),
    "bundles": (BUNDLE_COLS, ["ticker"]),
    "committee_notes": (COMMITTEE_NOTE_COLS, ["lineage", "generation", "author"]),
    "scorebook": (SCOREBOOK_COLS, ["lineage", "generation", "author", "rule_name", "period"]),
    "agent_ratings": (RATING_COLS, ["run_id", "ticker", "signal_date"]),
    "agent_lessons": (LESSON_COLS, ["lineage", "generation"]),
}
CSV_FILES = {"events": "events.csv", "controls": "controls.csv", "daily": "daily_features.csv",
             "event_features": "event_features.csv", "history_done": "history_done.csv",
             "errors": "errors.csv", "signal_report": "signal_report.csv", "flags": "flags.csv",
             "ladder_trades": "ladder_trades.csv", "ladder_report": "ladder_report.csv",
             "arena": "arena.csv", "agent_runs": "agent_runs.csv", "agent_trades": "agent_trades.csv",
             "agent_lessons": "agent_lessons.csv", "agent_weeks": "agent_weeks.csv", "pool": "pool.csv", "committee_notes": "committee_notes.csv",
             "scorebook": "scorebook.csv", "agent_ratings": "agent_ratings.csv",
             "wide_universe": "wide_universe.csv", "bundles": "bundles.csv"}


def _to_db(value, kind):
    if value is None or value == "":
        return None
    if kind == F:
        return float(value)
    if kind == I:
        return int(float(value))
    if kind == D:
        return dt.date.fromisoformat(str(value)[:10])
    return str(value)


def _from_db(value):
    if value is None:
        return ""
    if isinstance(value, float):
        return repr(value) if value != int(value) or abs(value) >= 1e15 else str(value)
    return str(value)


class PostgresStore:
    def __init__(self, url):
        import psycopg   # only needed when a database is configured
        self.conn = psycopg.connect(url, autocommit=True)
        for name, (cols, key) in TABLES.items():
            col_sql = ", ".join(f"{c} {k}" for c, k in cols.items())
            if key:
                col_sql += f", primary key ({', '.join(key)})"
            else:
                col_sql = "id bigserial primary key, " + col_sql
            self.conn.execute(f"create table if not exists {name} ({col_sql})")
            # New columns added in later versions of this file get added to existing tables.
            for c, k in cols.items():
                self.conn.execute(f"alter table {name} add column if not exists {c} {k}")
        self.conn.execute("create index if not exists flags_date on flags (signal_date)")
        # Committee tables gained a lineage column in their key; older rows belong to "committee".
        for t in ("committee_notes", "scorebook"):
            self.conn.execute(f"update {t} set lineage = 'committee' where lineage is null")
            key = TABLES[t][1]
            have = [r[0] for r in self.conn.execute(
                "select a.attname from pg_index i join pg_attribute a on a.attrelid = i.indrelid "
                "and a.attnum = any(i.indkey) where i.indrelid = %s::regclass and i.indisprimary", (t,)).fetchall()]
            if set(have) != set(key):
                self.conn.execute(f"alter table {t} drop constraint if exists {t}_pkey")
                self.conn.execute(f"alter table {t} add primary key ({', '.join(key)})")
        # Every write to the big daily table is time-stamped, so a local copy can fetch only what
        # changed since it last synced instead of downloading the whole table again.
        for t in STAMPED:
            self.conn.execute(f"alter table {t} add column if not exists updated_at timestamptz")
            self.conn.execute(f"create index if not exists {t}_updated on {t} (updated_at)")

    def read(self, table, where=None, params=()):
        cols = list(TABLES[table][0])
        sql = f"select {', '.join(cols)} from {table}"
        if where:
            sql += f" where {where}"
        rows = self.conn.execute(sql, params).fetchall()
        return [{c: _from_db(v) for c, v in zip(cols, r)} for r in rows]

    def upsert(self, table, rows):
        """Insert rows, or update existing ones. Only the columns a row actually carries are
        written, so a partial row (say, just a cost) never blanks out the rest."""
        if not rows:
            return
        cols, key = TABLES[table]
        groups = {}
        for r in rows:
            names = tuple(c for c in cols if c in r)
            groups.setdefault(names, []).append(r)
        for names, group in groups.items():
            values = [[_to_db(r.get(c), cols[c]) for c in names] for r in group]
            stamp = table in STAMPED
            sql = (f"insert into {table} ({', '.join(names)}{', updated_at' if stamp else ''}) "
                   f"values ({', '.join(['%s'] * len(names))}{', now()' if stamp else ''})")
            if key:
                updates = [f"{c} = excluded.{c}" for c in names if c not in key]
                if stamp:
                    updates.append("updated_at = now()")
                sql += f" on conflict ({', '.join(key)}) do " + (
                    "update set " + ", ".join(updates) if updates else "nothing")
            with self.conn.cursor() as cur:
                cur.executemany(sql, values)

    def replace(self, table, rows):
        with self.conn.transaction():
            self.conn.execute(f"delete from {table}")
            self.upsert(table, rows)

    def tickers_with_daily(self):
        return {r[0] for r in self.conn.execute("select distinct ticker from daily").fetchall()}


class CsvStore:
    def __init__(self):
        os.makedirs(DATA, exist_ok=True)
        self._cache = {}

    def _path(self, table):
        return os.path.join(DATA, CSV_FILES[table])

    def _all(self, table):
        if table not in self._cache:
            p = self._path(table)
            self._cache[table] = list(csv.DictReader(open(p, newline="", encoding="utf-8"))) \
                if os.path.exists(p) else []
        return self._cache[table]

    def _write(self, table):
        cols, key = TABLES[table]
        rows = self._all(table)
        if key:
            rows.sort(key=lambda r: tuple(str(r.get(k, "")) for k in key))
        with open(self._path(table), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(cols), extrasaction="ignore", restval="")
            w.writeheader()
            w.writerows(rows)

    def read(self, table, where=None, params=()):
        rows = self._all(table)
        if where:   # the CSV backend understands the few filters this project uses
            w = where.strip()
            if w == "ticker = %s":
                rows = [r for r in rows if r.get("ticker") == params[0]]
            elif w == "ticker = %s and date >= %s":
                rows = [r for r in rows if r.get("ticker") == params[0] and r.get("date", "") >= str(params[1])]
            elif w == "date >= %s":
                rows = [r for r in rows if r.get("date", "") >= str(params[0])]
            else:
                raise ValueError(f"CSV backend can't filter on: {where}")
        return [{c: ("" if r.get(c) is None else str(r.get(c))) for c in TABLES[table][0]} for r in rows]

    def upsert(self, table, rows):
        cols, key = TABLES[table]
        existing = self._all(table)
        if key:
            index = {tuple(str(r.get(k, ""))[:10] if cols[k] == D else str(r.get(k, ""))
                           for k in key): i for i, r in enumerate(existing)}
            for r in rows:
                k = tuple(str(r.get(c, ""))[:10] if cols[c] == D else str(r.get(c, "")) for c in key)
                given = {c: ("" if r.get(c) is None else r.get(c)) for c in cols if c in r}
                if k in index:
                    existing[index[k]].update(given)      # partial rows only touch their own columns
                else:
                    index[k] = len(existing)
                    existing.append({c: given.get(c, "") for c in cols})
        else:
            existing.extend(rows)
        self._write(table)

    def replace(self, table, rows):
        self._cache[table] = []
        self.upsert(table, rows)

    def tickers_with_daily(self):
        return {r["ticker"] for r in self._all("daily")}


STAMPED = ("daily",)
MIRROR_PATH = os.path.join(DATA, "daily_mirror.sqlite")
MIRROR_OVERLAP = dt.timedelta(hours=2)   # re-fetch a little, in case another job's write landed late


class DailyMirror:
    """A local SQLite copy of the daily table (about a million rows).

    The GitHub workflows keep this file in the Actions cache. On first use in a job it asks the
    database only for rows written since the copy was last synced (plus a small overlap), so a
    normal job downloads megabytes instead of the whole table. Every daily write goes to both the
    database and the copy. Reads come from the copy and match what the database would return."""

    def __init__(self, pg, path=MIRROR_PATH):
        self.pg, self.path = pg, path
        self.cols = list(DAILY_COLS)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.lock = threading.Lock()
        self.db.execute(f"create table if not exists daily ({', '.join(c + ' text' for c in self.cols)}, "
                        "primary key (ticker, date))")
        self.db.execute("create table if not exists meta (k text primary key, v text)")
        self.sync()

    def _norm(self, value, kind):
        """The same string the database read path would give for this value."""
        if value is None or value == "":
            return None
        return _from_db(_to_db(value, kind))

    def sync(self):
        # A copy made from a different database (or one restored since) is thrown away and rebuilt.
        ident = "|".join(str(v) for v in self.pg.conn.execute(
            "select current_database(), (select oid from pg_class where relname = 'daily')").fetchone())
        known = self.db.execute("select v from meta where k = 'source'").fetchone()
        if known and known[0] != ident:
            self.db.execute("delete from daily")
            self.db.execute("delete from meta")
        self.db.execute("insert or replace into meta values ('source', ?)", (ident,))
        row = self.db.execute("select v from meta where k = 'watermark'").fetchone()
        server_now = self.pg.conn.execute("select now()").fetchone()[0]
        sel = ", ".join(self.cols)
        if row:
            since = dt.datetime.fromisoformat(row[0]) - MIRROR_OVERLAP
            sql = f"copy (select {sel} from daily where updated_at > '{since.isoformat()}') to stdout"
        else:
            sql = f"copy (select {sel} from daily) to stdout"
        kinds = [DAILY_COLS[c] for c in self.cols]
        batch, n = [], 0
        put = (f"insert or replace into daily ({sel}) values ({', '.join('?' * len(self.cols))})")
        with self.pg.conn.cursor() as cur, cur.copy(sql) as copy:
            for rec in copy.rows():
                batch.append([self._norm(v, k) for v, k in zip(rec, kinds)])
                if len(batch) >= 20000:
                    self.db.executemany(put, batch)
                    n += len(batch)
                    batch = []
        if batch:
            self.db.executemany(put, batch)
            n += len(batch)
        self.db.execute("insert or replace into meta values ('watermark', ?)", (server_now.isoformat(),))
        self.db.commit()
        self.synced = n
        print(f"Daily data: local copy {'updated with' if row else 'built from'} {n:,} rows from the database.")

    def upsert(self, rows):
        with self.lock:
            for r in rows:
                names = [c for c in self.cols if c in r]
                vals = [self._norm(r.get(c), DAILY_COLS[c]) for c in names]
                upd = [f"{c} = excluded.{c}" for c in names if c not in ("ticker", "date")]
                self.db.execute(f"insert into daily ({', '.join(names)}) values ({', '.join('?' * len(names))}) "
                                f"on conflict (ticker, date) do " + ("update set " + ", ".join(upd) if upd else "nothing"),
                                vals)
            self.db.commit()

    def read(self, where="", params=()):
        sql = f"select {', '.join(self.cols)} from daily" + (f" where {where}" if where else "")
        with self.lock:
            rows = self.db.execute(sql, params).fetchall()
        return [{c: ("" if v is None else v) for c, v in zip(self.cols, r)} for r in rows]

    def tickers(self):
        with self.lock:
            return {r[0] for r in self.db.execute("select distinct ticker from daily")}


class Store:
    """The one object the rest of the code talks to."""

    def __init__(self, url=None):
        url = url if url is not None else os.environ.get("DATABASE_URL", "")
        self.backend = PostgresStore(url) if url else CsvStore()
        self.kind = "postgres" if url else "csv"
        self._mirror = None

    def mirror(self):
        """The local copy of the daily table (Postgres only; set DAILY_MIRROR=off to read directly)."""
        if self.kind != "postgres" or os.environ.get("DAILY_MIRROR", "on") == "off":
            return None
        if self._mirror is None:
            self._mirror = DailyMirror(self.backend, os.environ.get("DAILY_MIRROR_PATH", MIRROR_PATH))
        return self._mirror

    # events, controls, features, history marks, errors, report, flags
    def events(self):
        return self.backend.read("events")

    def save_events(self, rows):
        self.backend.upsert("events", rows)

    def controls(self):
        return self.backend.read("controls")

    def save_controls(self, rows):
        self.backend.upsert("controls", rows)

    def history_done(self):
        return self.backend.read("history_done")

    def mark_history(self, ticker, date):
        self.backend.upsert("history_done", [{"ticker": ticker, "completed": date}])

    def log_error(self, row):
        self.backend.upsert("errors", [row])

    def errors(self):
        return self.backend.read("errors")

    def save_features(self, rows):
        self.backend.upsert("event_features", rows)

    def features(self):
        return self.backend.read("event_features")

    def save_report(self, rows):
        self.backend.replace("signal_report", rows)

    def save_flags(self, rows):
        # Never overwrite an agent's verdict when the scorer re-flags the same day.
        existing = {(r["signal_date"], r["ticker"], r["rule"]): r for r in self.backend.read("flags")}
        for r in rows:
            old = existing.get((str(r["signal_date"]), r["ticker"], r["rule"]))
            if old:
                for c in ("verdict", "verdict_notes", "reviewed_at"):
                    r[c] = old.get(c, "")
        self.backend.upsert("flags", rows)

    def flags(self):
        return self.backend.read("flags")

    # per-ticker daily options and price history
    def daily(self, ticker, since=None):
        m = self.mirror()
        if m:
            rows = m.read("ticker = ? and date >= ?", (ticker, since)) if since else m.read("ticker = ?", (ticker,))
            rows.sort(key=lambda r: r["date"])
            return rows
        if since:
            rows = self.backend.read("daily", "ticker = %s and date >= %s", (ticker, since))
        else:
            rows = self.backend.read("daily", "ticker = %s", (ticker,))
        rows.sort(key=lambda r: r["date"])
        return rows

    def daily_by_ticker(self, tickers=None, since=None):
        """Many tickers in one query (for the scorer). Returns {ticker: rows sorted by date}."""
        m = self.mirror()
        if m:
            rows = m.read("date >= ?", (since,)) if since else m.read()
        else:
            rows = self.backend.read("daily", "date >= %s", (since,)) if since else self.backend.read("daily")
        out = {}
        for r in rows:
            if tickers is None or r["ticker"] in tickers:
                out.setdefault(r["ticker"], []).append(r)
        for v in out.values():
            v.sort(key=lambda r: r["date"])
        return out

    def save_daily(self, ticker, rows):
        rows = [r for r in rows if r.get("ticker") == ticker]
        self.backend.upsert("daily", rows)
        m = self.mirror()
        if m:
            m.upsert(rows)

    def daily_tickers(self):
        m = self.mirror()
        return m.tickers() if m else self.backend.tickers_with_daily()
