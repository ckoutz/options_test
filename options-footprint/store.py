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

TABLES = {
    "events": (EVENT_COLS, ["ticker", "event_date"]),
    "controls": (EVENT_COLS, ["ticker", "event_date"]),
    "daily": (DAILY_COLS, ["ticker", "date"]),
    "event_features": (FEATURE_COLS, ["ticker", "event_date"]),
    "history_done": (HISTORY_COLS, ["ticker"]),
    "errors": (ERROR_COLS, None),
    "signal_report": (REPORT_COLS, ["move_pct", "horizon_days", "rule"]),
    "flags": (FLAG_COLS, ["signal_date", "ticker", "rule"]),
}
CSV_FILES = {"events": "events.csv", "controls": "controls.csv", "daily": "daily_features.csv",
             "event_features": "event_features.csv", "history_done": "history_done.csv",
             "errors": "errors.csv", "signal_report": "signal_report.csv", "flags": "flags.csv"}


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

    def read(self, table, where=None, params=()):
        cols = list(TABLES[table][0])
        sql = f"select {', '.join(cols)} from {table}"
        if where:
            sql += f" where {where}"
        rows = self.conn.execute(sql, params).fetchall()
        return [{c: _from_db(v) for c, v in zip(cols, r)} for r in rows]

    def upsert(self, table, rows):
        if not rows:
            return
        cols, key = TABLES[table]
        names = list(cols)
        values = [[_to_db(r.get(c), cols[c]) for c in names] for r in rows]
        sql = f"insert into {table} ({', '.join(names)}) values ({', '.join(['%s'] * len(names))})"
        if key:
            updates = [c for c in names if c not in key]
            sql += f" on conflict ({', '.join(key)}) do update set " + \
                   ", ".join(f"{c} = excluded.{c}" for c in updates)
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
                clean = {c: ("" if r.get(c) is None else r.get(c)) for c in cols}
                if k in index:
                    existing[index[k]] = clean
                else:
                    index[k] = len(existing)
                    existing.append(clean)
        else:
            existing.extend(rows)
        self._write(table)

    def replace(self, table, rows):
        self._cache[table] = []
        self.upsert(table, rows)

    def tickers_with_daily(self):
        return {r["ticker"] for r in self._all("daily")}


class Store:
    """The one object the rest of the code talks to."""

    def __init__(self, url=None):
        url = url if url is not None else os.environ.get("DATABASE_URL", "")
        self.backend = PostgresStore(url) if url else CsvStore()
        self.kind = "postgres" if url else "csv"

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
        if since:
            rows = self.backend.read("daily", "ticker = %s and date >= %s", (ticker, since))
        else:
            rows = self.backend.read("daily", "ticker = %s", (ticker,))
        rows.sort(key=lambda r: r["date"])
        return rows

    def daily_by_ticker(self, tickers=None, since=None):
        """Many tickers in one query (for the scorer). Returns {ticker: rows sorted by date}."""
        rows = self.backend.read("daily", "date >= %s", (since,)) if since else self.backend.read("daily")
        out = {}
        for r in rows:
            if tickers is None or r["ticker"] in tickers:
                out.setdefault(r["ticker"], []).append(r)
        for v in out.values():
            v.sort(key=lambda r: r["date"])
        return out

    def save_daily(self, ticker, rows):
        self.backend.upsert("daily", [r for r in rows if r.get("ticker") == ticker])

    def daily_tickers(self):
        return self.backend.tickers_with_daily()
