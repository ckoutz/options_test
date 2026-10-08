# Status (2026-10-08 20:52 UTC, storage: postgres)

## Backfill
- Big moves logged: 5,382 across 1,649 stocks
- Pre-move windows filled: 5,382 of 5,382
- Stocks eligible for full history (3+ moves): 649; done: 649
- Control days: 10,754 (filled 10,754)
- Daily rows: 1,049,473; database size: 200 MB

## Table sizes
- daily: 182 MB, about 1,049,473 rows
- pool: 6 MB, about 7,320 rows
- arena: 5 MB, about 1,613 rows
- event_features: 3 MB, about 16,136 rows
- controls: 1 MB, about 10,754 rows
- events: 1 MB, about 5,382 rows
- flags: 1 MB, about 2,689 rows
- history_done: 0 MB, about 649 rows
- agent_trades: 0 MB, about 169 rows
- ladder_report: 0 MB, about 90 rows
- signal_report: 0 MB, about 36 rows
- agent_lessons: 0 MB, about 4 rows
- agent_runs: 0 MB, about 9 rows
- scorebook: 0 MB, about 0 rows
- agent_weeks: 0 MB, about 0 rows
- errors: 0 MB, about 0 rows
- ladder_trades: 0 MB, about 0 rows
- agent_ratings: 0 MB, about 0 rows
- committee_notes: 0 MB, about 0 rows

## Labels
- unknown: 4,598
- sector_day: 772
- check_corporate_action: 11
- news_catalyst: 1

## Ladder backtest
- raw trades archived to a GitHub Release; summary kept in ladder_report

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

## Trader generations
| lineage | gen | phase | model | trades | profit $ | random profit $ | mean % | median % | win % | random mean % | random win % | unreadable | cost $ | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| blank | 1 | train | anthropic/claude-haiku-5.5 | 0 |  |  |  |  |  |  |  |  | 0.0469 | complete |
| blank | 1 | validation | anthropic/claude-haiku-5.5 | 0 |  |  |  |  |  |  |  |  | 0.0203 | complete |
| blank | 2 | train | anthropic/claude-haiku-5.5 | 0 |  |  |  |  |  |  |  |  | 0.0469 | complete |
| blank | 2 | validation | anthropic/claude-haiku-5.5 | 0 |  |  |  |  |  |  |  |  | 0.0203 | complete |
| blank | 3 | train | anthropic/claude-haiku-5.5 | 0 |  |  |  |  |  |  |  |  | 0.0469 | complete |
| blank | 3 | validation | anthropic/claude-haiku-5.5 | 2 |  |  | 1.71 | 1.71 | 50.0 | -0.09 | 39.5 |  | 0.022 | complete |
| blank | 4 | train | anthropic/claude-haiku-5.5 |  |  |  |  |  |  |  |  |  |  | running |
| blank-v2 | 1 | train | anthropic/claude-haiku-5.5 | 136 | -5543.2 | -3100.8 | -4.08 | -2.73 | 44.9 | -2.28 | 40.3 | 0/71 | 0.067 | complete |
| blank-v2 | 1 | validation | anthropic/claude-haiku-5.5 | 31 | -290.5 | 564.2 | -0.94 | 0.82 | 51.6 | 1.82 | 52.3 | 0/31 | 0.0253 | complete |

### Latest lessons: blank lineage, generation 3 (anthropic/claude-haiku-5.5)

# Lessons Document: Generation 1 ## Status This generation made no trades, so it produced no evidence. Nothing below is a validated rule. Treat every item as a hypothesis to test, not a fact. ## What we know - **No trades, no results.** We have no data on which signals, instruments, expiries, strikes, or exits perform well or badly. - **Doing nothing is a valid baseline, not a failure.** Its score is zero. Any strategy you adopt should beat zero after costs, or it is not worth running. ## Starting principles (low confidence, untested) These are general reasoning, not findings. 1. **Start from the columns, not from a story.** Before trading, write down which columns you will use and what threshold or combination would trigger an entry. Decide this in advance, not after seeing outcomes. 2. **Prefer simple rules.** One or two conditions are easier to evaluate than many. Many conditions on a small sample mostly fit noise. 3. **Define the exit before the entry.** Set the exit rule (time-based, target, or stop) at the same time as the entry, so results are measurable. 4. **Pick one instrument and one expiry to begin.** Mixing instruments, expiries, and strikes makes results impossible to attribute. 5. **Strike choice matters, but we have no data on it.** Test at least two levels (for example, at-the-money and one step out-of-the-money) before drawing conclusions. ## How to build real lessons - **Log every decision**, including no-trade decisions and the reason for each. - **Record the columns' values at entry**, the exit reason, and the result after costs. - **Use a holdout.** Form rules on one segment of data and check them on a later segment. A rule that only works in-sample is not a lesson. - **Count trades before believing anything.** Under roughly 30 comparable trades, treat any win rate or average return as indicative only. Under 100, treat conclusions as provisional. - **Compare against doing nothing and against a simple baseline** (for example, always entering the same way with the same exit). - **Watch for overfitting:** if you tried many thresholds and kept the best, the result is likely luck. ## Confidence summary

### Latest lessons: blank-v2 lineage, generation 1 (anthropic/claude-haiku-5.5)

# Lessons for the Next Trader **Baseline:** Over 136 trades of $1,000 each, the overall result was -4.1% average and -5.5k total, with 45% winners. Trading shares was roughly flat (+0.4% average, -1.1% median, 92 trades). Most option variants lost money. Treat everything below as hypotheses, not established edges. ## Rules, with confidence 1. **Default to shares unless an option setup clearly beats them. Confidence: moderate.** Shares were the only large group near breakeven. Options lost on most variants, and their losses were often total (-100%), so one bad option trade costs far more than one bad share trade. 2. **Avoid 30-day calls struck above the money with a 10-day hold. Confidence: moderate.** The 30d +5%, +10%, and +15% hold10 groups averaged roughly -50% to -65%. Short expiry leaves too little time for the move to arrive. 3. **Avoid the "double_or_10" exit as a default. Confidence: moderate.** It produced the largest single gains and many of the largest losses. Its median outcome was poor, so it behaves like a lottery ticket, not a plan. 4. **Longer expiry (90 days) with a 10-day hold is the least bad option structure. Confidence: low.** The 90d +20% hold10 group averaged +13.6% over 3 trades, and the 90d +0% hold10 group had a positive median (+4.5%) but a negative average. Both samples are too small to trust. 5. **Do not trust the ratio columns (calls, puts, long, short, shares) as predictors. Confidence: moderate that they were not useful here.** Large and small values showed up in both winners and losers. I found no threshold that separated them. 6. **Short-term price moves (1d, 5d) and volatility (vol20) did not separate winners from losers in this data. Confidence: low.** Several large losses followed positive 1d and 5d moves, and some winners had weak early moves. ## What failed - Far-OTM short-dated calls: nearly every variant lost most of its premium. - Averaging across all option types hid the few winners. Medians were often worse than averages, meaning results depended on a handful of outliers. - Sizing every trade at $1,000 regardless of instrument risk. ## Sample caveats - Most groups have 1 to 11 trades. A single trade drives several results (the +258% and +123% gains each come from one or two trades). - Groups were chosen after seeing results, which inflates apparent edges. - Results cover one period. Regime changes may invalidate everything above. ## Next steps - Collect more trades in the 90-day hold10 structures before sizing up. - Test shares against 90-day options at equal dollar risk. - Record whether the exit rule fired and why, to separate strategy from luck.

## Errors (0 total, latest 8)
- none
