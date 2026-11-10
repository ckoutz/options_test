# Paper traders crashed (2026-11-10 11:07 UTC)

```
Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 57, in request
    with urllib.request.urlopen(req, timeout=60) as r:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/urllib/request.py", line 215, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/urllib/request.py", line 521, in open
    response = meth(req, response)
               ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/urllib/request.py", line 630, in http_response
    response = self.parent.error(
               ^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/urllib/request.py", line 559, in error
    return self._call_chain(*args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.16/x64/lib/python3.12/urllib/request.py", line 639, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 400: Bad Request

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/paper/trader.py", line 640, in <module>
    main()
  File "/home/runner/work/options_test/options_test/options-footprint/paper/trader.py", line 595, in main
    snap = AP.market_snapshot()
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 128, in market_snapshot
    recent = daily_bars(syms, days=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 103, in daily_bars
    pages = get_pages(f"{DATA}/v2/stocks/bars", keys,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 80, in get_pages
    page = request("GET", url, keys, p)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 65, in request
    raise AlpacaError(f"HTTP {e.code}: {msg}")
paper.alpaca.AlpacaError: HTTP 400: {"message":"invalid symbol: 037ESC019"}


```
