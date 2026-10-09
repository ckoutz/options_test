# Status (2026-10-09 00:09 UTC, storage: postgres)

## Backfill
- Big moves logged: 5,382 across 1,649 stocks
- Pre-move windows filled: 5,382 of 5,382
- Stocks eligible for full history (3+ moves): 649; done: 867
- Control days: 10,754 (filled 10,754)
- Daily rows: 1,150,859; database size: 270 MB

## Table sizes
- daily: 203 MB, about 1,150,866 rows
- news: 31 MB, about 145,726 rows
- pool: 12 MB, about 6,515 rows
- ladder_trades: 10 MB, about 41,402 rows
- arena: 5 MB, about 1,613 rows
- event_features: 3 MB, about 16,136 rows
- agent_ratings: 2 MB, about 11,851 rows
- controls: 1 MB, about 10,754 rows
- events: 1 MB, about 5,382 rows
- flags: 1 MB, about 2,759 rows
- agent_trades: 1 MB, about 2,042 rows
- agent_weeks: 1 MB, about 1,496 rows
- oi_daily: 0 MB, about 1,688 rows
- committee_notes: 0 MB, about 10 rows
- history_done: 0 MB, about 867 rows
- bundles: 0 MB, about 533 rows
- news_fetched: 0 MB, about 514 rows
- ladder_report: 0 MB, about 90 rows
- scorebook: 0 MB, about 72 rows
- wide_universe: 0 MB, about 300 rows
- errors: 0 MB, about 83 rows
- signal_report: 0 MB, about 36 rows
- agent_runs: 0 MB, about 20 rows
- agent_lessons: 0 MB, about 4 rows
- run_log: 0 MB, about 17 rows

## Labels
- unknown: 4,598
- sector_day: 772
- check_corporate_action: 11
- news_catalyst: 1

## Ladder backtest
- control: 1,359 days, 20,385 contracts (7,743 could be bought)
- flag: 1,359 days, 20,385 contracts (8,606 could be bought)

## Signal report (run 2026-10-08): rally within 10 sessions
| big move | rule | fired | hit % | lift | 1st half | 2nd half | drop lift | median 10-day return % |
|---|---|---|---|---|---|---|---|---|
| 15% | Momentum: calls 3x+ after 10%+ week | 11,843 | 31.1 | 1.37 | 1.36 | 1.37 | 1.27 | -0.3 |
| 15% | Call volume 5x+ | 18,076 | 24.9 | 1.1 | 1.11 | 1.08 | 1.05 | -0.2 |
| 15% | Short out-of-the-money calls 3x+ | 33,426 | 24.6 | 1.08 | 1.13 | 1.03 | 1.05 | -0.17 |
| 15% | Call volume 3x+ | 34,426 | 24.7 | 1.08 | 1.09 | 1.08 | 1.05 | -0.28 |
| 15% | Out-of-the-money calls 3x+ | 38,657 | 24.1 | 1.06 | 1.08 | 1.04 | 1.02 | -0.26 |
| 15% | Medium-dated calls 3x+ | 45,032 | 24.0 | 1.06 | 1.07 | 1.04 | 1.04 | -0.19 |
| 15% | Short-dated calls 3x+ | 38,209 | 24.1 | 1.06 | 1.13 | 0.99 | 0.99 | 0.0 |
| 15% | Long-dated calls 3x+ | 42,345 | 23.3 | 1.03 | 1.02 | 1.03 | 0.99 | 0.0 |
| 15% | Long-dated calls 5x+ | 24,172 | 23.0 | 1.01 | 1.02 | 1.01 | 0.98 | 0.0 |
| 15% | Any day (baseline) | 253,609 | 22.7 | 1.0 | 1.0 | 1.0 | 1.0 | -0.19 |
| 15% | Calls outpacing shares 2x+ | 35,140 | 21.9 | 0.97 | 0.96 | 0.98 | 0.97 | -0.31 |
| 15% | Calls outpacing shares 3x+ | 18,650 | 21.4 | 0.94 | 0.93 | 0.96 | 0.95 | -0.28 |
| 15% | Calls 3x+ and puts flat (put/call drop 3x+) | 11,929 | 21.0 | 0.93 | 0.92 | 0.93 | 0.94 | -0.21 |
| 15% | Put/call drop 3x+ | 37,020 | 21.0 | 0.92 | 0.94 | 0.91 | 0.92 | -0.07 |
| 15% | Put/call drop 5x+ | 21,431 | 20.4 | 0.9 | 0.93 | 0.87 | 0.9 | 0.0 |
| 15% | Calls 3x+ while price quiet | 6,290 | 17.1 | 0.75 | 0.77 | 0.74 | 0.8 | -0.45 |
| 15% | Stealth: calls 3x+, shares normal, price quiet | 4,654 | 15.9 | 0.7 | 0.68 | 0.72 | 0.76 | -0.5 |
| 15% | Long-dated 3x+ while price quiet | 8,701 | 15.4 | 0.68 | 0.66 | 0.7 | 0.75 | -0.27 |
| 30% | Momentum: calls 3x+ after 10%+ week | 11,843 | 14.0 | 1.85 | 1.91 | 1.78 | 1.62 | -0.3 |
| 30% | Call volume 5x+ | 18,076 | 10.0 | 1.33 | 1.38 | 1.26 | 1.16 | -0.2 |
| 30% | Call volume 3x+ | 34,426 | 9.6 | 1.28 | 1.31 | 1.23 | 1.15 | -0.28 |
| 30% | Out-of-the-money calls 3x+ | 38,657 | 9.1 | 1.21 | 1.27 | 1.14 | 1.1 | -0.26 |
| 30% | Medium-dated calls 3x+ | 45,032 | 9.0 | 1.2 | 1.22 | 1.17 | 1.12 | -0.19 |
| 30% | Short out-of-the-money calls 3x+ | 33,426 | 8.7 | 1.15 | 1.21 | 1.08 | 1.11 | -0.17 |
| 30% | Short-dated calls 3x+ | 38,209 | 8.7 | 1.15 | 1.22 | 1.06 | 1.02 | 0.0 |
| 30% | Long-dated calls 5x+ | 24,172 | 8.6 | 1.14 | 1.18 | 1.08 | 0.98 | 0.0 |
| 30% | Long-dated calls 3x+ | 42,345 | 8.5 | 1.12 | 1.16 | 1.08 | 1.0 | 0.0 |
| 30% | Calls outpacing shares 2x+ | 35,140 | 7.8 | 1.03 | 1.04 | 1.01 | 0.96 | -0.31 |
| 30% | Any day (baseline) | 253,609 | 7.6 | 1.0 | 1.0 | 1.0 | 1.0 | -0.19 |
| 30% | Calls outpacing shares 3x+ | 18,650 | 7.5 | 0.99 | 1.01 | 0.98 | 0.93 | -0.28 |
| 30% | Calls 3x+ and puts flat (put/call drop 3x+) | 11,929 | 7.1 | 0.94 | 0.94 | 0.94 | 0.86 | -0.21 |
| 30% | Put/call drop 3x+ | 37,020 | 6.9 | 0.91 | 0.92 | 0.9 | 0.81 | -0.07 |
| 30% | Put/call drop 5x+ | 21,431 | 6.3 | 0.84 | 0.88 | 0.79 | 0.76 | 0.0 |
| 30% | Calls 3x+ while price quiet | 6,290 | 5.1 | 0.68 | 0.71 | 0.64 | 0.7 | -0.45 |
| 30% | Long-dated 3x+ while price quiet | 8,701 | 4.7 | 0.62 | 0.61 | 0.62 | 0.6 | -0.27 |
| 30% | Stealth: calls 3x+, shares normal, price quiet | 4,654 | 4.6 | 0.61 | 0.59 | 0.62 | 0.63 | -0.5 |

## Flags (daily shortlist)
- 2,759 flags; latest signal date: 2026-10-07

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
| committee | 1 | train | anthropic/claude-haiku-5.5 | 56 | 1428.8 | -218.4 | 2.55 | -0.52 | 50.0 | -0.39 | 45.3 | 0/151 | 0.2055 | complete |
| committee | 1 | train | anthropic/claude-haiku-5.5 | 84 | -486.2 | 1050.0 | -0.58 | 1.13 | 53.6 | 1.25 | 46.1 | 0/151 | 0.2074 | complete |
| committee | 1 | train | anthropic/claude-haiku-5.5 | 78 | 2431.0 | 702.0 | 3.12 | -0.99 | 43.6 | 0.9 | 40.5 | 1/151 | 0.1992 | complete |
| committee | 1 | train | anthropic/claude-haiku-5.5 | 87 | -3353.8 | -1818.3 | -3.85 | -1.81 | 42.5 | -2.09 | 40.7 | 0/151 | 0.1992 | complete |
| committee | 1 | score | anthropic/claude-haiku-5.5 | 304 | 5214.6 | 3374.4 | 1.72 | -1.18 | 48.0 | 1.11 | 47.6 | 0/144 | 0.1995 | complete |
| options1 | 1 | train | anthropic/claude-haiku-5.5 | 233 | 88953.0 | 11743.2 | 38.18 | -41.95 | 30.0 | 5.04 | 30.3 | 1/151 | 0.269 | complete |
| options1 | 1 | train | anthropic/claude-haiku-5.5 | 298 | 111695.7 | 28190.8 | 37.48 | -46.87 | 29.2 | 9.46 | 28.9 | 0/151 | 0.2573 | complete |
| options1 | 1 | train | anthropic/claude-haiku-5.5 | 249 | -427.4 | 27016.5 | -0.17 | -42.83 | 28.5 | 10.85 | 29.8 | 1/151 | 0.271 | complete |
| options1 | 1 | train | anthropic/claude-haiku-5.5 | 213 | 69348.1 | 36060.9 | 32.56 | -36.05 | 31.0 | 16.93 | 31.4 | 0/151 | 0.2744 | complete |
| options1 | 1 | score | anthropic/claude-haiku-5.5 | 271 | 15275.1 | 14905.0 | 5.64 | -31.28 | 31.7 | 5.5 | 32.1 | 5/144 | 0.2811 | complete |
| news |  | scoring | anthropic/claude-haiku-5.5 |  |  |  |  |  |  |  |  |  | 0.2049 | complete |

### Latest lessons: blank lineage, generation 3 (anthropic/claude-haiku-5.5)

# Lessons Document: Generation 1 ## Status This generation made no trades, so it produced no evidence. Nothing below is a validated rule. Treat every item as a hypothesis to test, not a fact. ## What we know - **No trades, no results.** We have no data on which signals, instruments, expiries, strikes, or exits perform well or badly. - **Doing nothing is a valid baseline, not a failure.** Its score is zero. Any strategy you adopt should beat zero after costs, or it is not worth running. ## Starting principles (low confidence, untested) These are general reasoning, not findings. 1. **Start from the columns, not from a story.** Before trading, write down which columns you will use and what threshold or combination would trigger an entry. Decide this in advance, not after seeing outcomes. 2. **Prefer simple rules.** One or two conditions are easier to evaluate than many. Many conditions on a small sample mostly fit noise. 3. **Define the exit before the entry.** Set the exit rule (time-based, target, or stop) at the same time as the entry, so results are measurable. 4. **Pick one instrument and one expiry to begin.** Mixing instruments, expiries, and strikes makes results impossible to attribute. 5. **Strike choice matters, but we have no data on it.** Test at least two levels (for example, at-the-money and one step out-of-the-money) before drawing conclusions. ## How to build real lessons - **Log every decision**, including no-trade decisions and the reason for each. - **Record the columns' values at entry**, the exit reason, and the result after costs. - **Use a holdout.** Form rules on one segment of data and check them on a later segment. A rule that only works in-sample is not a lesson. - **Count trades before believing anything.** Under roughly 30 comparable trades, treat any win rate or average return as indicative only. Under 100, treat conclusions as provisional. - **Compare against doing nothing and against a simple baseline** (for example, always entering the same way with the same exit). - **Watch for overfitting:** if you tried many thresholds and kept the best, the result is likely luck. ## Confidence summary

### Latest lessons: blank-v2 lineage, generation 1 (anthropic/claude-haiku-5.5)

# Lessons for the Next Trader **Baseline:** Over 136 trades of $1,000 each, the overall result was -4.1% average and -5.5k total, with 45% winners. Trading shares was roughly flat (+0.4% average, -1.1% median, 92 trades). Most option variants lost money. Treat everything below as hypotheses, not established edges. ## Rules, with confidence 1. **Default to shares unless an option setup clearly beats them. Confidence: moderate.** Shares were the only large group near breakeven. Options lost on most variants, and their losses were often total (-100%), so one bad option trade costs far more than one bad share trade. 2. **Avoid 30-day calls struck above the money with a 10-day hold. Confidence: moderate.** The 30d +5%, +10%, and +15% hold10 groups averaged roughly -50% to -65%. Short expiry leaves too little time for the move to arrive. 3. **Avoid the "double_or_10" exit as a default. Confidence: moderate.** It produced the largest single gains and many of the largest losses. Its median outcome was poor, so it behaves like a lottery ticket, not a plan. 4. **Longer expiry (90 days) with a 10-day hold is the least bad option structure. Confidence: low.** The 90d +20% hold10 group averaged +13.6% over 3 trades, and the 90d +0% hold10 group had a positive median (+4.5%) but a negative average. Both samples are too small to trust. 5. **Do not trust the ratio columns (calls, puts, long, short, shares) as predictors. Confidence: moderate that they were not useful here.** Large and small values showed up in both winners and losers. I found no threshold that separated them. 6. **Short-term price moves (1d, 5d) and volatility (vol20) did not separate winners from losers in this data. Confidence: low.** Several large losses followed positive 1d and 5d moves, and some winners had weak early moves. ## What failed - Far-OTM short-dated calls: nearly every variant lost most of its premium. - Averaging across all option types hid the few winners. Medians were often worse than averages, meaning results depended on a handful of outliers. - Sizing every trade at $1,000 regardless of instrument risk. ## Sample caveats - Most groups have 1 to 11 trades. A single trade drives several results (the +258% and +123% gains each come from one or two trades). - Groups were chosen after seeing results, which inflates apparent edges. - Results cover one period. Regime changes may invalidate everything above. ## Next steps - Collect more trades in the 90-day hold10 structures before sizing up. - Test shares against 90-day options at equal dollar risk. - Record whether the exit rule fired and why, to separate strategy from luck.

## Wide list (chosen without hindsight)
- 300 stocks chosen; full options history done for 247

## Job notes (latest 8)
- 2026-10-08T23:23:24+00:00 oi-pull: plan: 134 stocks, 3,804 stock-days, estimated $53.31 (cap $100).
- 2026-10-08T23:22:41+00:00 oi-pull: cost check failed for SPCE: 504 The remote gateway timed out.
- 2026-10-08T23:21:14+00:00 oi-pull: cost check failed for DPRO: 504 The remote gateway timed out.
- 2026-10-08T23:20:14+00:00 oi-pull: cost check failed for CLMT: 504 The remote gateway timed out.
- 2026-10-08T23:18:34+00:00 oi-pull: cost check failed for PTGX: 504 The remote gateway timed out.
- 2026-10-08T23:17:13+00:00 oi-pull: cost check failed for ALMU: 504 The remote gateway timed out.
- 2026-10-08T23:16:06+00:00 oi-pull: cost check failed for EWTX: 504 The remote gateway timed out.
- 2026-10-08T23:14:30+00:00 oi-pull: cost check failed for SATL: 504 The remote gateway timed out.

## Errors (83 total, latest 8)
- 2026-10-09 00:09 RUM oi 2025-01-06: 504 The remote gateway timed out.
- 2026-10-09 00:07 NVTS oi 2024-09-26: 504 The remote gateway timed out.
- 2026-10-09 00:07 PLCE oi 2024-03-21: 504 The remote gateway timed out.
- 2026-10-09 00:05 CLPT oi 2025-07-02: 504 The remote gateway timed out.
- 2026-10-09 00:04 PACS oi 2025-01-14: 504 The remote gateway timed out.
- 2026-10-09 00:04 CGC oi 2025-07-03: 504 The remote gateway timed out.
- 2026-10-09 00:03 RIVN oi 2025-02-28: 504 The remote gateway timed out.
- 2026-10-09 00:02 CGC oi 2025-01-27: 504 The remote gateway timed out.
