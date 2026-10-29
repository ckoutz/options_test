# LEAPS backtest crashed

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
  File "/home/runner/work/options_test/options_test/options-footprint/paper/leaps_backtest.py", line 263, in <module>
    main()
  File "/home/runner/work/options_test/options_test/options-footprint/paper/leaps_backtest.py", line 204, in main
    now_px = option_closes(sorted({p[2] for p in pend}), (dt.date.fromisoformat(today) - dt.timedelta(days=10)).isoformat(),
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/leaps_backtest.py", line 113, in option_closes
    pages = AP.get_pages(f"{AP.DATA}/v1beta1/options/bars", keys,
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 80, in get_pages
    page = request("GET", url, keys, p)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/paper/alpaca.py", line 65, in request
    raise AlpacaError(f"HTTP {e.code}: {msg}")
paper.alpaca.AlpacaError: HTTP 403: {"message":"OPRA agreement is not signed"}


```
