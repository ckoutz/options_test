# LEAPS backtest crashed

```
Traceback (most recent call last):
  File "/home/runner/work/options_test/options_test/options-footprint/paper/leaps_backtest.py", line 263, in <module>
    main()
  File "/home/runner/work/options_test/options_test/options-footprint/paper/leaps_backtest.py", line 197, in main
    "spy": 100 * (spy_end / spy[d] - 1) if spy_end and spy.get(d) else None,
                  ~~~~~~~~^~~~~~~~
TypeError: unsupported operand type(s) for /: 'tuple' and 'tuple'

```
