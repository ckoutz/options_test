# Status (2026-10-08 18:18 UTC, storage: postgres)

## Backfill
- Big moves logged: 5,382 across 1,649 stocks
- Pre-move windows filled: 5,382 of 5,382
- Stocks eligible for full history (3+ moves): 649; done: 649
- Control days: 10,754 (filled 10,754)
- Daily rows: 1,049,473; database size: 445 MB

## Table sizes
- ladder_trades: 274 MB, about 1,006,755 rows
- daily: 175 MB, about 1,049,473 rows
- event_features: 3 MB, about 16,136 rows
- arena: 3 MB, about 1,613 rows
- controls: 1 MB, about 10,754 rows
- events: 1 MB, about 5,382 rows
- flags: 1 MB, about 2,689 rows
- history_done: 0 MB, about 649 rows
- want: 0 MB, about 1,613 rows
- ladder_report: 0 MB, about 90 rows
- signal_report: 0 MB, about 36 rows
- agent_runs: 0 MB, about 3 rows
- agent_lessons: 0 MB, about 1 rows
- errors: 0 MB, about 0 rows
- agent_trades: 0 MB, about 0 rows

## Labels
- unknown: 4,598
- sector_day: 772
- check_corporate_action: 11
- news_catalyst: 1

## Ladder backtest
- control: 33,553 days, 503,295 contracts (262,234 could be bought)
- flag: 33,564 days, 503,460 contracts (282,137 could be bought)

## Signal report (run 2026-10-08): rally within 10 sessions
| big move | rule | fired | hit % | lift | 1st half | 2nd half | drop lift | median 10-day return % |
|---|---|---|---|---|---|---|---|---|
| 15% | Momentum: calls 3x+ after 10%+ week | 11,761 | 31.2 | 1.34 | 1.33 | 1.35 | 1.25 | -0.29 |
| 15% | Call volume 5x+ | 17,412 | 25.7 | 1.1 | 1.12 | 1.09 | 1.05 | -0.2 |
| 15% | Call volume 3x+ | 33,253 | 25.4 | 1.09 | 1.1 | 1.08 | 1.06 | -0.31 |
| 15% | Short out-of-the-money calls 3x+ | 32,511 | 25.1 | 1.08 | 1.12 | 1.03 | 1.04 | -0.16 |
| 15% | Out-of-the-money calls 3x+ | 37,289 | 24.9 | 1.07 | 1.09 | 1.05 | 1.03 | -0.28 |
| 15% | Medium-dated calls 3x+ | 43,537 | 24.7 | 1.06 | 1.08 | 1.04 | 1.04 | -0.23 |
| 15% | Short-dated calls 3x+ | 37,041 | 24.7 | 1.06 | 1.13 | 0.99 | 0.99 | 0.0 |
| 15% | Long-dated calls 3x+ | 40,933 | 24.0 | 1.03 | 1.03 | 1.04 | 0.99 | -0.03 |
| 15% | Long-dated calls 5x+ | 23,294 | 23.8 | 1.02 | 1.02 | 1.02 | 0.98 | 0.0 |
| 15% | Any day (baseline) | 246,437 | 23.3 | 1.0 | 1.0 | 1.0 | 1.0 | -0.22 |
| 15% | Calls outpacing shares 2x+ | 33,766 | 22.7 | 0.97 | 0.97 | 0.98 | 0.97 | -0.33 |
| 15% | Calls outpacing shares 3x+ | 17,805 | 22.3 | 0.96 | 0.94 | 0.97 | 0.95 | -0.32 |
| 15% | Calls 3x+ and puts flat (put/call drop 3x+) | 11,388 | 21.9 | 0.94 | 0.93 | 0.94 | 0.95 | -0.23 |
| 15% | Put/call drop 3x+ | 35,698 | 21.7 | 0.93 | 0.95 | 0.91 | 0.92 | -0.1 |
| 15% | Put/call drop 5x+ | 20,650 | 21.1 | 0.9 | 0.94 | 0.87 | 0.9 | 0.0 |
| 15% | Calls 3x+ while price quiet | 5,687 | 18.7 | 0.8 | 0.84 | 0.77 | 0.83 | -0.6 |
| 15% | Stealth: calls 3x+, shares normal, price quiet | 4,220 | 17.4 | 0.75 | 0.74 | 0.75 | 0.8 | -0.66 |
| 15% | Long-dated 3x+ while price quiet | 7,938 | 16.8 | 0.72 | 0.71 | 0.73 | 0.78 | -0.4 |
| 30% | Momentum: calls 3x+ after 10%+ week | 11,761 | 14.1 | 1.81 | 1.85 | 1.76 | 1.59 | -0.29 |
| 30% | Call volume 5x+ | 17,412 | 10.4 | 1.34 | 1.39 | 1.28 | 1.16 | -0.2 |
| 30% | Call volume 3x+ | 33,253 | 10.0 | 1.28 | 1.32 | 1.24 | 1.15 | -0.31 |
| 30% | Out-of-the-money calls 3x+ | 37,289 | 9.5 | 1.22 | 1.27 | 1.15 | 1.1 | -0.28 |
| 30% | Medium-dated calls 3x+ | 43,537 | 9.3 | 1.2 | 1.22 | 1.17 | 1.12 | -0.23 |
| 30% | Short out-of-the-money calls 3x+ | 32,511 | 8.9 | 1.15 | 1.2 | 1.08 | 1.11 | -0.16 |
| 30% | Short-dated calls 3x+ | 37,041 | 8.9 | 1.15 | 1.22 | 1.06 | 1.02 | 0.0 |
| 30% | Long-dated calls 5x+ | 23,294 | 8.9 | 1.14 | 1.19 | 1.09 | 0.99 | 0.0 |
| 30% | Long-dated calls 3x+ | 40,933 | 8.8 | 1.13 | 1.16 | 1.08 | 1.01 | -0.03 |
| 30% | Calls outpacing shares 2x+ | 33,766 | 8.1 | 1.04 | 1.05 | 1.02 | 0.96 | -0.33 |
| 30% | Calls outpacing shares 3x+ | 17,805 | 7.8 | 1.01 | 1.02 | 0.99 | 0.94 | -0.32 |
| 30% | Any day (baseline) | 246,437 | 7.8 | 1.0 | 1.0 | 1.0 | 1.0 | -0.22 |
| 30% | Calls 3x+ and puts flat (put/call drop 3x+) | 11,388 | 7.4 | 0.96 | 0.96 | 0.95 | 0.86 | -0.23 |
| 30% | Put/call drop 3x+ | 35,698 | 7.1 | 0.92 | 0.93 | 0.91 | 0.81 | -0.1 |
| 30% | Put/call drop 5x+ | 20,650 | 6.6 | 0.84 | 0.89 | 0.79 | 0.76 | 0.0 |
| 30% | Calls 3x+ while price quiet | 5,687 | 5.6 | 0.73 | 0.77 | 0.67 | 0.73 | -0.6 |
| 30% | Long-dated 3x+ while price quiet | 7,938 | 5.1 | 0.66 | 0.66 | 0.65 | 0.63 | -0.4 |
| 30% | Stealth: calls 3x+, shares normal, price quiet | 4,220 | 5.0 | 0.65 | 0.65 | 0.64 | 0.66 | -0.66 |

## Flags (daily shortlist)
- 2,689 flags; latest signal date: 2026-10-07

## Errors (0 total, latest 8)
- none
