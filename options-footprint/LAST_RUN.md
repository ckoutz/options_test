# Last run: nightly (2026-10-09 02:29 UTC)
```
Warning: Alpaca did not flag any assets as options-enabled; scanning all major-exchange stocks.
Storage: postgres
Scanned 6926 tickers: 19 moves of 15%+, 0 new events added (0 over 200% kept but flagged for review).
events: 5384 already filled, 0 to fill.
Daily data: local copy updated with 150,800 rows from the database.
[nightly FAILED] ls = option_daily_volume(ticker, todo, closes)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 296, in option_daily_volume
    pages = alpaca_get("https://data.alpaca.markets", "/v1beta1/options/bars",
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 180, in alpaca_get
    data = http_json(f"{base}{path}?{urllib.parse.urlencode(p)}", headers)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 159, in http_json
    sys.exit(message)
SystemExit: Alpaca refused https://data.alpaca.markets/v1beta1/options/bars with HTTP 403: {"message":"OPRA agreement is not signed"}


Alpaca refused https://data.alpaca.markets/v1beta1/options/bars with HTTP 403: {"message":"OPRA agreement is not signed"}

```
