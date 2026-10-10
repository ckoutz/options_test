# Watchlist test: do past big movers make good trades? (2026-10-10 21:20 UTC)

Wide-list stocks only (chosen from January 2024 data, no hindsight), days from 2025-01-01 on. Each stock-day is labeled by how many 15%+ up days the stock had in the previous year (known at the time). Returns are over the next 10 sessions, bought at the next close.

| days with a 15%+ jump in the past year | stock-days | stocks | 10-session return: average / median | vs the average wide stock that day (range) | % that rose | chance of a 15%+ up day next 10 sessions | chance of a 15%+ down day |
|---|---|---|---|---|---|---|---|
| none in the past year | 84,974 | 250 | +0.08% / -0.00% | -0.11 (-0.27 to +0.02) | 50% | 0.8% | 0.7% |
| 1 to 2 | 18,416 | 93 | +0.27% / +0.08% | -0.01 (-0.42 to +0.40) | 50% | 1.9% | 2.0% |
| 3 to 5 | 1,562 | 13 | +1.62% / -0.95% | +1.36 (-0.42 to +3.27) | 47% | 15.7% | 6.0% |
| 6 or more | 981 | 6 | +8.12% / -0.69% | +7.68 (+0.73 to +16.79) | 48% | 15.6% | 5.1% |

## The 30-day at-the-money call on the same stock-days

Where the options backtest has the contract (it covers selected days, not every day). Realistic costs; contracts expiring during the hold excluded.

| days with a 15%+ jump in the past year | calls | average | median | % winners | median implied volatility |
|---|---|---|---|---|---|
| none in the past year | 12,025 | -9.2% | -35.1% | 34% | 32% |
| 1 to 2 | 2,746 | -8.2% | -34.7% | 35% | 50% |
| 3 to 5 | 282 | -22.8% | -52.3% | 27% | 100% |
| 6 or more | 249 | -36.7% | -63.4% | 19% | 113% |

## How to read it

- If past big movers are a useful watchlist, the groups with more past jumps should beat the average wide stock (second column of the first table, range above zero), not just jump more often in both directions.
- If they only show higher chances of BOTH a 15%+ up day and a 15%+ down day, the list catches volatility, not direction; whether that pays depends on the option's price (second table).
