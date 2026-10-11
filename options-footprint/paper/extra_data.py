"""
Data the traders asked for on their research day (requests R1010-1, R1010-2, R1010-3):

- Earnings calendar and earnings history (Finnhub, free plan; key in FINNHUB_API_KEY).
- Shares outstanding and share turnover (Finnhub company profiles + Alpaca daily volume).
- Past daily prices for any option contract, expired ones included (Alpaca), with implied volatility worked
  out from each day's close.
"""
import datetime as dt
import json
import math
import os
import time
import urllib.error
import urllib.parse
import urllib.request

from paper import alpaca as AP

FINNHUB = "https://finnhub.io/api/v1"
RATE = 0.045
_last_call = [0.0]


class DataError(Exception):
    pass


# ---------------------------------------------------------------- Finnhub
def finnhub(path, params, tries=3):
    key = os.environ.get("FINNHUB_API_KEY", "")
    if not key:
        raise DataError("FINNHUB_API_KEY is not set")
    url = f"{FINNHUB}{path}?" + urllib.parse.urlencode({**params, "token": key})
    for attempt in range(tries):
        wait = 1.05 - (time.time() - _last_call[0])      # free plan: 60 calls a minute
        if wait > 0:
            time.sleep(wait)
        _last_call[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/json"}),
                                        timeout=30) as r:
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < tries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise DataError(f"Finnhub HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:200]}")
        except (urllib.error.URLError, OSError) as e:
            if attempt < tries - 1:
                time.sleep(3)
                continue
            raise DataError(f"Finnhub network: {e}")
    raise DataError("Finnhub kept failing")


def _cache(name):
    return os.path.join(AP.DATA_DIR, name)


def _load(name):
    try:
        with open(_cache(name)) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _save(name, obj):
    os.makedirs(AP.DATA_DIR, exist_ok=True)
    with open(_cache(name), "w") as f:
        json.dump(obj, f)


def _surprise(actual, est):
    if actual is None or est in (None, 0):
        return None
    return round((actual - est) / abs(est) * 100, 1)


def earnings_calendar(symbol=None, days_ahead=30, days_back=0, universe=None):
    """Upcoming (and optionally recent) earnings reports. Without a symbol, limited to `universe`."""
    today = dt.date.today()
    params = {"from": (today - dt.timedelta(days=days_back)).isoformat(),
              "to": (today + dt.timedelta(days=days_ahead)).isoformat()}
    if symbol:
        params["symbol"] = symbol
    rows = finnhub("/calendar/earnings", params).get("earningsCalendar") or []
    out = []
    for r in rows:
        sym = r.get("symbol")
        if universe is not None and sym not in universe:
            continue
        out.append({"symbol": sym, "date": r.get("date"),
                    "time": {"bmo": "before open", "amc": "after close", "dmh": "during hours"}.get(r.get("hour"), "unknown"),
                    "eps_estimate": r.get("epsEstimate"), "eps_actual": r.get("epsActual"),
                    "eps_surprise_pct": _surprise(r.get("epsActual"), r.get("epsEstimate")),
                    "revenue_estimate_m": round(r["revenueEstimate"] / 1e6, 1) if r.get("revenueEstimate") else None,
                    "revenue_actual_m": round(r["revenueActual"] / 1e6, 1) if r.get("revenueActual") else None})
    out.sort(key=lambda x: (x["date"] or "", x["symbol"] or ""))
    return out


def earnings_history(symbol):
    """The last few reported quarters: actual vs estimate (Finnhub free plan gives about 4)."""
    rows = finnhub("/stock/earnings", {"symbol": symbol}) or []
    return [{"period": r.get("period"), "eps_actual": r.get("actual"), "eps_estimate": r.get("estimate"),
             "eps_surprise_pct": r.get("surprisePercent") if r.get("surprisePercent") is not None
             else _surprise(r.get("actual"), r.get("estimate"))} for r in rows if isinstance(r, dict)]


def shares_outstanding(symbols):
    """{symbol: shares in millions}, from Finnhub company profiles, cached for 7 days."""
    cache = _load("finnhub_profiles.json")
    fresh = (dt.date.today() - dt.timedelta(days=7)).isoformat()
    out = {}
    for s in symbols:
        c = cache.get(s)
        if c and c.get("as_of", "") >= fresh:
            out[s] = c.get("shares_m")
            continue
        prof = finnhub("/stock/profile2", {"symbol": s}) or {}
        shares = prof.get("shareOutstanding")
        cache[s] = {"as_of": dt.date.today().isoformat(), "shares_m": shares,
                    "industry": prof.get("finnhubIndustry"), "market_cap_m": prof.get("marketCapitalization")}
        out[s] = shares
    _save("finnhub_profiles.json", cache)
    return out, cache


def turnover(symbols):
    """Daily share turnover (volume / shares outstanding) over 20 and 120 sessions."""
    shares, cache = shares_outstanding(symbols)
    bars = AP.daily_bars(symbols, days=200)
    out = {}
    for s in symbols:
        b = bars.get(s) or []
        sh = shares.get(s)
        if not b or not sh:
            out[s] = {"error": "no shares outstanding or no price history"}
            continue
        v20 = sum(x["volume"] for x in b[-20:]) / len(b[-20:])
        v120 = sum(x["volume"] for x in b[-120:]) / len(b[-120:])
        out[s] = {"shares_outstanding_m": round(sh, 1),
                  "turnover_20d_pct_per_day": round(v20 / (sh * 1e6) * 100, 3),
                  "turnover_120d_pct_per_day": round(v120 / (sh * 1e6) * 100, 3),
                  "turnover_20d_vs_120d": round(v20 / v120, 2) if v120 else None,
                  "industry": cache.get(s, {}).get("industry"),
                  "market_cap_m": cache.get(s, {}).get("market_cap_m")}
    return out


# ---------------------------------------------------------------- past option prices
def _ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs_price(S, K, T, sigma, kind, r=RATE):
    if T <= 0 or sigma <= 0:
        return max(0.0, S - K) if kind == "call" else max(0.0, K - S)
    d1 = (math.log(S / K) + (r + sigma * sigma / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if kind == "call":
        return S * _ncdf(d1) - K * math.exp(-r * T) * _ncdf(d2)
    return K * math.exp(-r * T) * _ncdf(-d2) - S * _ncdf(-d1)


def implied_vol(price, S, K, T, kind):
    if not price or not S or T <= 0:
        return None
    intrinsic = max(0.0, S - K) if kind == "call" else max(0.0, K - S)
    if price <= intrinsic + 1e-6:
        return None
    lo, hi = 0.01, 5.0
    if bs_price(S, K, T, hi, kind) < price:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if bs_price(S, K, T, mid, kind) < price:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2 * 100, 1)


def occ(symbol, expiration, kind, strike):
    e = dt.date.fromisoformat(expiration)
    return f"{symbol.upper()}{e:%y%m%d}{'C' if kind == 'call' else 'P'}{int(round(strike * 1000)):08d}"


def parse_occ(contract):
    c = contract.upper()
    return {"symbol": c[:-15], "expiration": f"20{c[-15:-13]}-{c[-13:-11]}-{c[-11:-9]}",
            "type": "call" if c[-9] == "C" else "put", "strike": int(c[-8:]) / 1000}


def find_contract(n, symbol, as_of, days_to_expiry, strike_pct, kind):
    """The listed contract closest to the target expiry and strike, as of a past date (expired ones too)."""
    keys = AP.agent_keys(n)
    day = dt.date.fromisoformat(as_of)
    target = day + dt.timedelta(days=days_to_expiry)
    stock = AP.daily_bars([symbol], days=(dt.date.today() - day).days + 10).get(symbol) or []
    close = next((b["close"] for b in stock if b["date"] >= as_of), None)
    if not close:
        raise DataError(f"no stock price for {symbol} on or after {as_of}")
    want = close * (1 + strike_pct / 100) if kind == "call" else close * (1 - strike_pct / 100)
    found = []
    for status in ("inactive", "active"):
        found += AP.get_pages(f"{AP.PAPER}/v2/options/contracts", keys,
                              {"underlying_symbols": symbol, "type": kind, "status": status, "limit": 10000,
                               "expiration_date_gte": (target - dt.timedelta(days=12)).isoformat(),
                               "expiration_date_lte": (target + dt.timedelta(days=12)).isoformat(),
                               "strike_price_gte": round(want * 0.85, 2), "strike_price_lte": round(want * 1.15, 2)},
                              "option_contracts")
    if not found:
        raise DataError(f"no listed {kind} contracts for {symbol} near {target} (Alpaca's option history starts "
                        "in early 2024)")
    best = min(found, key=lambda c: (abs((dt.date.fromisoformat(c["expiration_date"]) - target).days) * 0.5
                                     + abs(float(c["strike_price"]) - want) / want * 100))
    return best["symbol"], close


def option_history(n, contract=None, symbol=None, as_of=None, days_to_expiry=30, strike_pct=0.0, kind="call",
                   sessions=30):
    """Daily bars for one contract from `as_of`, with the stock's close and the implied volatility."""
    if not contract:
        if not (symbol and as_of):
            raise DataError("give a contract (OCC symbol) or symbol + as_of date")
        contract, _ = find_contract(n, symbol.upper(), as_of, int(days_to_expiry), float(strike_pct), kind)
    meta = parse_occ(contract)
    start = as_of or (dt.date.fromisoformat(meta["expiration"]) - dt.timedelta(days=60)).isoformat()
    end_day = min(dt.date.fromisoformat(meta["expiration"]), dt.date.today())
    bars = AP.get_pages(f"{AP.DATA}/v1beta1/options/bars", AP.data_keys(),
                        {"symbols": contract, "timeframe": "1Day", "start": start, "end": AP.last_close_end()
                         if end_day >= dt.date.today() else (end_day + dt.timedelta(days=1)).isoformat(),
                         "limit": 10000}, "bars")
    rows = []
    for page in bars:
        rows.extend(page.get(contract, []) if isinstance(page, dict) else [])
    if not rows:
        raise DataError(f"no trades on record for {contract} from {start} (thinly traded contracts can have days "
                        "with no trades; try a strike closer to the money)")
    stock = {b["date"]: b["close"] for b in AP.daily_bars([meta["symbol"]],
                                                          days=(dt.date.today() - dt.date.fromisoformat(start)).days + 10)
             .get(meta["symbol"], [])}
    exp = dt.date.fromisoformat(meta["expiration"])
    out = []
    for b in sorted(rows, key=lambda x: x["t"])[:int(sessions)]:
        d = b["t"][:10]
        s = stock.get(d)
        T = max((exp - dt.date.fromisoformat(d)).days, 0.5) / 365
        out.append([d, s, b["c"], b.get("v"), implied_vol(b["c"], s, meta["strike"], T, meta["type"]) if s else None])
    first, last = out[0][2], out[-1][2]
    late = as_of and out[0][0] > as_of
    return {"contract": contract, **meta,
            **({"warning": f"first trade on record is {out[0][0]}, after {as_of}: weekly contracts are often listed "
                           "only a few weeks before expiry, so try days_to_expiry near a monthly expiry (third "
                           "Friday) or a contract that already existed"} if late else {}),
            "columns": ["date", "stock_close", "option_close", "option_volume", "implied_vol_pct"],
            "rows": out, "change_pct_first_to_last": round((last / first - 1) * 100, 1) if first else None,
            "note": "Option closes are the last trade of the day, not the bid/ask; thin contracts can be stale. "
                    "Real buys and sells cost about half the bid-ask spread each way (often 2-10% of the price "
                    "for short-dated contracts), so subtract that when judging a strategy."}
