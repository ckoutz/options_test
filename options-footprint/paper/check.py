"""Check that each paper account's keys work: balance, options level, shorting. Writes PAPER_CHECK.md.
Never prints the keys."""
import datetime as dt
import json
import os
import urllib.error
import urllib.request

BASE = "https://paper-api.alpaca.markets"


def get(path, key, secret):
    req = urllib.request.Request(BASE + path, headers={"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    lines = [f"# Paper account check ({dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC)", "",
             "| account | keys | status | equity $ | buying power $ | options level (approved / trading) | shorting | pattern day trader |",
             "|---|---|---|---|---|---|---|---|"]
    for n in (1, 2, 3):
        key, secret = os.environ.get(f"PAPER{n}_KEY_ID", ""), os.environ.get(f"PAPER{n}_SECRET", "")
        if not key or not secret:
            lines.append(f"| {n} | missing secret(s) | | | | | | |")
            continue
        kind = "paper key" if key.startswith("PK") else "key does not start with PK (live key?)"
        try:
            a = get("/v2/account", key, secret)
        except urllib.error.HTTPError as e:
            lines.append(f"| {n} | {kind}; login failed (HTTP {e.code}) | | | | | | |")
            continue
        except Exception as e:  # noqa: BLE001
            lines.append(f"| {n} | {kind}; error {type(e).__name__} | | | | | | |")
            continue
        lines.append(f"| {n} | {kind}, works | {a.get('status')} | {float(a.get('equity') or 0):,.0f} | "
                     f"{float(a.get('buying_power') or 0):,.0f} | {a.get('options_approved_level')} / "
                     f"{a.get('options_trading_level')} | {a.get('shorting_enabled')} | {a.get('pattern_day_trader')} |")
    lines += ["", "Options levels: 1 = covered calls, 2 = buy calls and puts, 3 = spreads and other multi-leg trades."]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "PAPER_CHECK.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
