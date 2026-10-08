# Status report FAILED (2026-10-08 19:56 UTC)
```
Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 930, in <module>
    main()
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 924, in main
    {"find-movers": find_movers, "collect": collect, "controls": controls, "features": features,
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 829, in status
    st = db()
         ^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/collector.py", line 331, in db
    _STORE = Store()
             ^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/store.py", line 261, in __init__
    self.backend = PostgresStore(url) if url else CsvStore()
                   ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/store.py", line 141, in __init__
    self.conn = psycopg.connect(url, autocommit=True)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/psycopg/connection.py", line 134, in connect
    raise new_ex.with_traceback(None)
psycopg.OperationalError: connection is bad: connection to server at "2600:1f16:729:b92b:fe3c:f60f:d694:464d", port 5432 failed: Network is unreachable
	Is the server running on that host and accepting TCP/IP connections?
Multiple connection attempts failed. All failures were:
- host: 'ep-solitary-shape-b5u0pnnh-pooler.c-7.us-east-2.aws.neon.tech', port: None, hostaddr: '3.141.122.14': connection failed: connection to server at "3.141.122.14", port 5432 failed: ERROR:  Your account or project has exceeded the quota. Upgrade your plan to increase limits.
- host: 'ep-solitary-shape-b5u0pnnh-pooler.c-7.us-east-2.aws.neon.tech', port: None, hostaddr: '18.189.49.143': connection failed: connection to server at "18.189.49.143", port 5432 failed: ERROR:  Your account or project has exceeded the quota. Upgrade your plan to increase limits.
- host: 'ep-solitary-shape-b5u0pnnh-pooler.c-7.us-east-2.aws.neon.tech', port: None, hostaddr: '3.18.239.121': connection failed: connection to server at "3.18.239.121", port 5432 failed: ERROR:  Your account or project has exceeded the quota. Upgrade your plan to increase limits.
- host: 'ep-solitary-shape-b5u0pnnh-pooler.c-7.us-east-2.aws.neon.tech', port: None, hostaddr: '2600:1f16:729:b915:bb3e:237c:b2ee:22a9': connection is bad: connection to server at "2600:1f16:729:b915:bb3e:237c:b2ee:22a9", port 5432 failed: Network is unreachable
	Is the server running on that host and accepting TCP/IP connections?
- host: 'ep-solitary-shape-b5u0pnnh-pooler.c-7.us-east-2.aws.neon.tech', port: None, hostaddr: '2600:1f16:729:b904:bb79:cee9:5022:3861': connection is bad: connection to server at "2600:1f16:729:b904:bb79:cee9:5022:3861", port 5432 failed: Network is unreachable
	Is the server running on that host and accepting TCP/IP connections?
- host: 'ep-solitary-shape-b5u0pnnh-pooler.c-7.us-east-2.aws.neon.tech', port: None, hostaddr: '2600:1f16:729:b92b:fe3c:f60f:d694:464d': connection is bad: connection to server at "2600:1f16:729:b92b:fe3c:f60f:d694:464d", port 5432 failed: Network is unreachable
	Is the server running on that host and accepting TCP/IP connections?
```
