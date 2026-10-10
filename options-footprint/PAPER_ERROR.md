# Paper traders crashed (2026-10-10 21:34 UTC)

```
Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 57, in request
    with urllib.request.urlopen(req, timeout=60) as r:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/request.py", line 215, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/request.py", line 521, in open
    response = meth(req, response)
               ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/request.py", line 630, in http_response
    response = self.parent.error(
               ^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/request.py", line 559, in error
    return self._call_chain(*args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/urllib/request.py", line 639, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 403: Forbidden

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/paper/trader.py", line 480, in <module>
    main()
  File "/home/runner/work/options_test/options_test/options-footprint/paper/trader.py", line 473, in main
    smoke(a.agent)
  File "/home/runner/work/options_test/options_test/options-footprint/paper/trader.py", line 404, in smoke
    snap = AP.market_snapshot()
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 129, in market_snapshot
    snap = request("GET", f"{DATA}/v2/stocks/snapshots", keys,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 65, in request
    raise AlpacaError(f"HTTP {e.code}: {msg}")
paper.alpaca.AlpacaError: HTTP 403: {"message":"subscription does not permit querying recent SIP data"}


```
