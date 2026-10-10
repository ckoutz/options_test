"""
Unusual options activity for the paper traders: the project's own scanner, on the latest session in
the database (the nightly data job fills it after each close). Cached per day.
"""
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import collector as C   # noqa: E402
import scorer as S      # noqa: E402


def runway(series, i, recent=20, base=40):
    rec = [x for x in series[max(0, i - recent + 1):i + 1] if x is not None]
    old = [x for x in series[max(0, i - recent - base + 1):max(0, i - recent + 1)] if x is not None]
    if len(rec) < recent // 2 or len(old) < base // 2:
        return None
    a, b = sum(rec) / len(rec), sum(old) / len(old)
    return round(a / b, 2) if b > 0 else None


def scan():
    path = os.path.join(C.DATA, f"flow_scan_{dt.date.today().isoformat()}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    st = C.db()
    rows = []
    for t in C.history_tickers():
        daily = [r for r in st.daily(t) if r.get("put_call_alpaca") not in (None, "")][-90:]
        if len(daily) < 30:
            continue
        scored = S.score_days({t: daily}, 30.0, 10)
        if not scored:
            continue
        last = scored[-1]
        closes = [C.to_float(r["stock_close"]) for r in daily]
        calls = [C.to_float(r.get("call_volume")) for r in daily]
        puts = [C.to_float(r.get("put_volume")) for r in daily]
        i = len(daily) - 1

        def ret(k):
            return round((closes[i] / closes[i - k] - 1) * 100, 1) if i >= k and closes[i] and closes[i - k] else None
        spikes = [C.to_float(x.get("call_volume_spike")) or 0 for x in scored[-20:]]
        back = [C.to_float(x.get("call_volume_spike")) or 0 for x in scored[-61:]][::-1]
        rows.append({"symbol": t, "date": last["date"], "close": closes[i],
                     "call_spike": C.to_float(last.get("call_volume_spike")),
                     "put_spike": C.to_float(last.get("put_volume_spike")),
                     "put_call": C.to_float(last.get("put_call")),
                     "calls_20d": runway(calls, i), "puts_20d": runway(puts, i),
                     "call_days_2x_20d": sum(1 for x in spikes if x >= 2),
                     "days_since_spike": next((k for k, x in enumerate(back) if x >= 3), 60),
                     "ret_1d": ret(1), "ret_5d": ret(5), "ret_20d": ret(20)})
    latest = max((r["date"] for r in rows), default=None)
    rows = [r for r in rows if r["date"] == latest]       # only stocks with data from the latest session
    with open(path, "w") as f:
        json.dump(rows, f)
    return rows
