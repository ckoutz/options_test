# Last crash (2026-10-09 21:31 UTC)

error: RuntimeError: model replies unreadable (4/6): '(empty reply)'

```
Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/committee.py", line 1118, in loop
    run_generation(st, args, pool, deadline, pot)
  File "/home/runner/work/options_test/options_test/options-footprint/committee.py", line 1032, in run_generation
    results = {a: f.result() for a, f in futs.items()}
                  ^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/concurrent/futures/_base.py", line 449, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/concurrent/futures/thread.py", line 59, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/committee.py", line 876, in agent_train
    trades = walk.bundle(by_week, working, scorebook, label)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/options_test/options_test/options-footprint/committee.py", line 756, in bundle
    raise RuntimeError(f"model replies unreadable ({self.bad}/{self.replies}): {self.sample[:200]!r}")
RuntimeError: model replies unreadable (4/6): '(empty reply)'

```
