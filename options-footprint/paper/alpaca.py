"""
Alpaca access for the paper traders.

Market data uses the project's data keys (ALPACA_KEY_ID / ALPACA_SECRET_KEY). Trading uses each agent's
own paper keys (PAPERn_KEY_ID / PAPERn_SECRET), and refuses to run with anything but paper keys.
"""
import bisect
import datetime as dt
import json
import math
import os
import statistics
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
DATA = "https://data.alpaca.markets"
PAPER = "https://paper-api.alpaca.markets"
MAJOR_EXCHANGES = {"NYSE", "NASDAQ", "AMEX", "ARCA", "BATS"}


class AlpacaError(Exception):
    pass


def data_keys():
    kid, sec = os.environ.get("ALPACA_KEY_ID", ""), os.environ.get("ALPACA_SECRET_KEY", "")
    if not (kid and sec):
        raise AlpacaError("ALPACA_KEY_ID / ALPACA_SECRET_KEY are not set")
    return kid, sec


def agent_keys(n):
    kid, sec = os.environ.get(f"PAPER{n}_KEY_ID", ""), os.environ.get(f"PAPER{n}_SECRET", "")
    if not (kid and sec):
        raise AlpacaError(f"PAPER{n}_KEY_ID / PAPER{n}_SECRET are not set")
    if not kid.startswith("PK"):
        # Paper key IDs start with PK. Anything else could be a live account: never trade with it.
        sys.exit(f"Refusing to run: PAPER{n}_KEY_ID does not look like a paper key.")
    return kid, sec


def request(method, url, keys, params=None, body=None, tries=4):
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    headers = {"APCA-API-KEY-ID": keys[0], "APCA-API-SECRET-KEY": keys[1], "Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    for attempt in range(tries):
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read().decode()
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:400]
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            raise AlpacaError(f"HTTP {e.code}: {msg}")
        except (urllib.error.URLError, OSError) as e:
            if attempt < tries - 1:
                time.sleep(3 * (attempt + 1))
                continue
            raise AlpacaError(f"network: {e}")
    raise AlpacaError("request kept failing")


def get_pages(url, keys, params, key):
    out, token = [], None
    while True:
        p = dict(params)
        if token:
            p["page_token"] = token
        page = request("GET", url, keys, p)
        items = page.get(key)
        if isinstance(items, dict):
            out.append(items)
        elif items:
            out.extend(items)
        token = page.get("next_page_token")
        if not token:
            return out


def last_close_end():
    """A safe end time for daily data: 20 minutes ago (the free plan refuses very recent data)."""
    return (dt.datetime.now(dt.timezone.utc) - dt.timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%SZ")


def daily_bars(symbols, days=400):
    """{symbol: [{"date", "close", "volume", "high", "low"}]} for up to `days` calendar days back."""
    keys = data_keys()
    start = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    out = {}
    for i in range(0, len(symbols), 100):
        chunk = symbols[i:i + 100]
        pages = get_pages(f"{DATA}/v2/stocks/bars", keys,
                          {"symbols": ",".join(chunk), "timeframe": "1Day", "start": start,
                           "end": last_close_end(), "limit": 10000, "adjustment": "all", "feed": "sip"}, "bars")
        for page in pages:
            for sym, bars in page.items():
                out.setdefault(sym, []).extend({"date": b["t"][:10], "close": b["c"], "volume": b["v"],
                                                "high": b["h"], "low": b["l"], "vwap": b.get("vw")} for b in bars)
    return out


# ---------------------------------------------------------------- the market snapshot (shared by all agents)
def market_snapshot(force=False):
    """Every liquid US stock ($5+, 500,000+ shares a day) with its 1/3/6/12-month returns, rank, trend,
    volatility, beta and dollar volume. Built once per day and cached (all three agents share it)."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"market_snapshot_{dt.date.today().isoformat()}.json")
    if os.path.exists(path) and not force:
        with open(path) as f:
            return json.load(f)
    keys = data_keys()
    assets = request("GET", f"{PAPER}/v2/assets", keys, {"status": "active", "asset_class": "us_equity"})
    syms = sorted(a["symbol"] for a in assets if a.get("tradable") and a.get("exchange") in MAJOR_EXCHANGES
                  and "." not in a["symbol"] and "/" not in a["symbol"])
    # Liquidity screen from the last week of daily bars ($5+ and 500,000+ shares a day on average).
    # (The free plan refuses consolidated "snapshots", but historical daily bars are fine.)
    recent = daily_bars(syms, days=10)
    liquid = [s for s, b in recent.items()
              if b and b[-1]["close"] >= 5 and statistics.mean(x["volume"] for x in b[-5:]) >= 500_000]
    bars = daily_bars(sorted(set(liquid) | {"SPY"}), days=400)
    spy = {b["date"]: b["close"] for b in bars.get("SPY", [])}
    rows = {}
    for s, b in bars.items():
        if len(b) < 60:
            continue
        closes = [x["close"] for x in b]
        dates = [x["date"] for x in b]
        c = closes[-1]

        def ret(n):
            return round((c / closes[-1 - n] - 1) * 100, 1) if len(closes) > n and closes[-1 - n] else None
        rets = [closes[k] / closes[k - 1] - 1 for k in range(max(1, len(closes) - 20), len(closes))]
        pairs = [(closes[k] / closes[k - 1] - 1, spy[dates[k]] / spy[dates[k - 1]] - 1)
                 for k in range(max(1, len(closes) - 60), len(closes)) if dates[k] in spy and dates[k - 1] in spy]
        beta = None
        if len(pairs) >= 40:
            ms = statistics.mean(p[1] for p in pairs)
            mv = statistics.mean((p[1] - ms) ** 2 for p in pairs)
            if mv > 0:
                ss = statistics.mean(p[0] for p in pairs)
                beta = round(statistics.mean((p[0] - ss) * (p[1] - ms) for p in pairs) / mv, 2)
        ma50 = statistics.mean(closes[-50:]) if len(closes) >= 50 else None
        hi52 = max(closes[-252:])
        ma20 = statistics.mean(closes[-20:])
        vw = b[-1].get("vwap")
        rows[s] = {"price": round(c, 2), "r1d": ret(1), "r5d": ret(5), "r1m": ret(21), "r3m": ret(63), "r6m": ret(126), "r12m": ret(252),
                   "vs_ma20": round((c / ma20 - 1) * 100, 1),
                   "vs_ma50": round((c / ma50 - 1) * 100, 1) if ma50 else None,
                   "close_vs_vwap": round((c / vw - 1) * 100, 2) if vw else None,
                   "off_52w_high": round((c / hi52 - 1) * 100, 1),
                   "vol20_ann": round(statistics.pstdev(rets) * math.sqrt(252) * 100, 1) if len(rets) > 10 else None,
                   "beta": beta,
                   "dollar_vol_m": round(statistics.mean(x["close"] * x["volume"] for x in b[-20:]) / 1e6, 1),
                   "last_date": dates[-1]}
    # Percentile ranks across the whole liquid market.
    for k in ("r1m", "r3m", "r6m", "r12m"):
        vals = sorted(v[k] for v in rows.values() if v[k] is not None)
        for v in rows.values():
            if v[k] is not None and vals:
                v[k + "_rank"] = round(100 * bisect.bisect_left(vals, v[k]) / len(vals))
    above = [v["vs_ma50"] > 0 for v in rows.values() if v["vs_ma50"] is not None]
    meta = {"built": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "stocks": len(rows),
            "breadth_pct_above_ma50": round(100 * sum(above) / len(above), 1) if above else None}
    snap = {"meta": meta, "rows": rows}
    with open(path, "w") as f:
        json.dump(snap, f)
    return snap


# ---------------------------------------------------------------- options and news
def option_chain(symbol, kind="call", min_days=7, max_days=120, strike_pct=20.0, price=None):
    keys = data_keys()
    today = dt.date.today()
    params = {"feed": "indicative", "type": kind, "limit": 1000,
              "expiration_date_gte": (today + dt.timedelta(days=min_days)).isoformat(),
              "expiration_date_lte": (today + dt.timedelta(days=max_days)).isoformat()}
    if price:
        params["strike_price_gte"] = round(price * (1 - strike_pct / 100), 2)
        params["strike_price_lte"] = round(price * (1 + strike_pct / 100), 2)
    snaps = get_pages(f"{DATA}/v1beta1/options/snapshots/{symbol}", keys, params, "snapshots")
    out = []
    for page in snaps:
        for occ, v in page.items():
            q = v.get("latestQuote") or {}
            g = v.get("greeks") or {}
            exp = dt.date(2000 + int(occ[-15:-13]), int(occ[-13:-11]), int(occ[-11:-9]))
            strike = int(occ[-8:]) / 1000
            bid, ask = q.get("bp"), q.get("ap")
            out.append({"contract": occ, "expiration": exp.isoformat(), "days": (exp - today).days,
                        "strike": strike, "bid": bid, "ask": ask,
                        "mid": round((bid + ask) / 2, 2) if bid is not None and ask else None,
                        "iv_pct": round(v["impliedVolatility"] * 100, 1) if v.get("impliedVolatility") else None,
                        "delta": round(g["delta"], 3) if g.get("delta") is not None else None,
                        "theta": round(g["theta"], 3) if g.get("theta") is not None else None})
    out.sort(key=lambda x: (x["expiration"], x["strike"]))
    return out


def news(symbol, days=7, limit=15):
    keys = data_keys()
    start = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = request("GET", f"{DATA}/v1beta1/news", keys,
                   {"symbols": symbol, "start": start, "limit": min(limit, 50), "sort": "desc"})
    return [{"time": n.get("created_at", "")[:16], "headline": n.get("headline", ""),
             "summary": (n.get("summary") or "")[:300], "symbols": len(n.get("symbols") or [])}
            for n in data.get("news", [])]


# ---------------------------------------------------------------- trading (the agent's own paper account)
def account(n):
    keys = agent_keys(n)
    acct = request("GET", f"{PAPER}/v2/account", keys)
    positions = request("GET", f"{PAPER}/v2/positions", keys)
    orders = request("GET", f"{PAPER}/v2/orders", keys, {"status": "open", "limit": 100})
    return acct, positions, orders


def submit_order(n, body):
    return request("POST", f"{PAPER}/v2/orders", agent_keys(n), body=body, tries=1)


def cancel_order(n, order_id):
    return request("DELETE", f"{PAPER}/v2/orders/{order_id}", agent_keys(n), tries=2)


def recent_orders(n, days=5):
    after = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return request("GET", f"{PAPER}/v2/orders", agent_keys(n), {"status": "all", "after": after, "limit": 200})


def clock():
    return request("GET", f"{PAPER}/v2/clock", data_keys())


def calendar(days=10):
    start = dt.date.today().isoformat()
    end = (dt.date.today() + dt.timedelta(days=days)).isoformat()
    return request("GET", f"{PAPER}/v2/calendar", data_keys(), {"start": start, "end": end})
