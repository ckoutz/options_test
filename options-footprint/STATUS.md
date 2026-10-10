# Status (2026-10-10 01:11 UTC, storage: postgres)

## Backfill
- Big moves logged: 5,384 across 1,650 stocks
- Pre-move windows filled: 5,384 of 5,384
- Stocks eligible for full history (3+ moves): 650; done: 920
- Control days: 10,758 (filled 10,758)
- Daily rows: 1,174,576; database size: 490 MB

## Table sizes
- daily: 272 MB, about 1,174,576 rows
- ladder_trades: 141 MB, about 564,225 rows
- news: 47 MB, about 225,612 rows
- pool: 21 MB, about 9,157 rows
- arena: 5 MB, about 1,613 rows
- agent_ratings: 5 MB, about 25,590 rows
- event_features: 3 MB, about 16,142 rows
- flags: 2 MB, about 3,918 rows
- agent_trades: 2 MB, about 4,257 rows
- controls: 1 MB, about 10,758 rows
- events: 1 MB, about 5,384 rows
- agent_weeks: 1 MB, about 2,992 rows
- oi_daily: 1 MB, about 3,653 rows
- committee_notes: 0 MB, about 20 rows
- bundles: 0 MB, about 766 rows
- history_done: 0 MB, about 920 rows
- scorebook: 0 MB, about 146 rows
- news_fetched: 0 MB, about 742 rows
- ladder_report: 0 MB, about 90 rows
- wide_universe: 0 MB, about 300 rows
- errors: 0 MB, about 151 rows
- signal_report: 0 MB, about 36 rows
- agent_runs: 0 MB, about 33 rows
- run_log: 0 MB, about 36 rows
- agent_lessons: 0 MB, about 4 rows

## Labels
- unknown: 4,600
- sector_day: 772
- check_corporate_action: 11
- news_catalyst: 1

## Ladder backtest
- control: 18,781 days, 281,715 contracts (114,306 could be bought)
- flag: 18,778 days, 281,670 contracts (125,867 could be bought)

## Signal report (run 2026-10-09): rally within 10 sessions
| big move | rule | fired | hit % | lift | 1st half | 2nd half | drop lift | median 10-day return % |
|---|---|---|---|---|---|---|---|---|
| 15% | Momentum: calls 3x+ after 10%+ week | 13,430 | 28.9 | 1.7 | 1.77 | 1.63 | 1.53 | -0.23 |
| 15% | Call volume 5x+ | 26,881 | 18.7 | 1.1 | 1.13 | 1.07 | 1.07 | -0.11 |
| 15% | Short out-of-the-money calls 3x+ | 47,863 | 18.7 | 1.09 | 1.16 | 1.04 | 1.05 | 0.18 |
| 15% | Call volume 3x+ | 50,834 | 18.6 | 1.09 | 1.11 | 1.07 | 1.06 | -0.08 |
| 15% | Medium-dated calls 3x+ | 66,561 | 18.1 | 1.06 | 1.1 | 1.04 | 1.05 | -0.08 |
| 15% | Long-dated calls 3x+ | 62,050 | 17.7 | 1.04 | 1.04 | 1.04 | 1.0 | 0.08 |
| 15% | Long-dated calls 5x+ | 35,304 | 17.7 | 1.04 | 1.04 | 1.04 | 1.0 | 0.12 |
| 15% | Short-dated calls 3x+ | 56,848 | 17.7 | 1.04 | 1.11 | 0.98 | 0.97 | 0.3 |
| 15% | Out-of-the-money calls 3x+ | 59,464 | 17.6 | 1.03 | 1.05 | 1.02 | 1.0 | 0.0 |
| 15% | Any day (baseline) | 372,279 | 17.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |
| 15% | Calls outpacing shares 2x+ | 55,108 | 15.9 | 0.93 | 0.93 | 0.94 | 0.95 | -0.11 |
| 15% | Put/call drop 3x+ | 56,112 | 15.6 | 0.92 | 0.94 | 0.9 | 0.91 | 0.08 |
| 15% | Calls outpacing shares 3x+ | 30,184 | 15.3 | 0.9 | 0.89 | 0.91 | 0.92 | -0.08 |
| 15% | Put/call drop 5x+ | 32,702 | 15.2 | 0.89 | 0.93 | 0.86 | 0.9 | 0.11 |
| 15% | Calls 3x+ and puts flat (put/call drop 3x+) | 19,334 | 14.9 | 0.88 | 0.87 | 0.89 | 0.89 | 0.0 |
| 15% | Calls 3x+ while price quiet | 14,899 | 9.2 | 0.54 | 0.53 | 0.56 | 0.62 | -0.11 |
| 15% | Long-dated 3x+ while price quiet | 19,130 | 8.8 | 0.52 | 0.49 | 0.55 | 0.6 | -0.03 |
| 15% | Stealth: calls 3x+, shares normal, price quiet | 11,258 | 8.4 | 0.49 | 0.47 | 0.53 | 0.58 | -0.14 |
| 30% | Momentum: calls 3x+ after 10%+ week | 13,430 | 12.7 | 2.37 | 2.58 | 2.16 | 2.04 | -0.23 |
| 30% | Call volume 5x+ | 26,881 | 7.2 | 1.33 | 1.42 | 1.25 | 1.18 | -0.11 |
| 30% | Call volume 3x+ | 50,834 | 6.9 | 1.29 | 1.35 | 1.23 | 1.16 | -0.08 |
| 30% | Medium-dated calls 3x+ | 66,561 | 6.5 | 1.2 | 1.25 | 1.16 | 1.13 | -0.08 |
| 30% | Out-of-the-money calls 3x+ | 59,464 | 6.3 | 1.18 | 1.24 | 1.11 | 1.07 | 0.0 |
| 30% | Short out-of-the-money calls 3x+ | 47,863 | 6.3 | 1.17 | 1.25 | 1.09 | 1.12 | 0.18 |
| 30% | Long-dated calls 5x+ | 35,304 | 6.3 | 1.17 | 1.22 | 1.12 | 1.01 | 0.12 |
| 30% | Short-dated calls 3x+ | 56,848 | 6.1 | 1.13 | 1.21 | 1.05 | 1.0 | 0.3 |
| 30% | Long-dated calls 3x+ | 62,050 | 6.1 | 1.13 | 1.18 | 1.09 | 1.02 | 0.08 |
| 30% | Any day (baseline) | 372,279 | 5.4 | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 |
| 30% | Calls outpacing shares 2x+ | 55,108 | 5.3 | 0.98 | 1.0 | 0.97 | 0.93 | -0.11 |
| 30% | Calls outpacing shares 3x+ | 30,184 | 5.0 | 0.94 | 0.95 | 0.93 | 0.88 | -0.08 |
| 30% | Put/call drop 3x+ | 56,112 | 4.8 | 0.9 | 0.91 | 0.89 | 0.8 | 0.08 |
| 30% | Calls 3x+ and puts flat (put/call drop 3x+) | 19,334 | 4.7 | 0.88 | 0.88 | 0.89 | 0.79 | 0.0 |
| 30% | Put/call drop 5x+ | 32,702 | 4.4 | 0.82 | 0.87 | 0.77 | 0.76 | 0.11 |
| 30% | Calls 3x+ while price quiet | 14,899 | 2.4 | 0.46 | 0.46 | 0.46 | 0.5 | -0.11 |
| 30% | Long-dated 3x+ while price quiet | 19,130 | 2.3 | 0.43 | 0.43 | 0.45 | 0.45 | -0.03 |
| 30% | Stealth: calls 3x+, shares normal, price quiet | 11,258 | 2.2 | 0.4 | 0.38 | 0.44 | 0.45 | -0.14 |

## Flags (daily shortlist)
- 3,918 flags; latest signal date: 2026-10-08

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
| news |  | scoring | anthropic/claude-haiku-5.5 |  |  |  |  |  |  |  |  |  | 0.1216 | complete |
| news |  | scoring | anthropic/claude-haiku-5.5 |  |  |  |  |  |  |  |  |  | 0.0022 | complete |
| gen10 | 1 | train | anthropic/claude-haiku-5.5 | 222 | -36788.3 | -27594.6 | -16.57 | -46.42 | 31.1 | -12.43 | 31.1 | 3/151 | 0.2907 | complete |
| gen10 | 1 | train | anthropic/claude-haiku-5.5 | 293 | -47796.0 | -43686.3 | -16.31 | -58.77 | 30.0 | -14.91 | 29.6 | 16/151 | 0.3067 | complete |
| gen10 | 1 | train | anthropic/claude-haiku-5.5 | 264 | -44071.2 | -38992.8 | -16.69 | -37.88 | 29.2 | -14.77 | 30.1 | 12/151 | 0.3117 | complete |
| gen10 | 1 | train | anthropic/claude-haiku-5.5 | 217 | -34204.3 | -33418.0 | -15.76 | -35.08 | 31.3 | -15.4 | 29.8 | 1/151 | 0.2927 | complete |
| gen10 | 1 | score | anthropic/claude-haiku-5.5 | 156 | -29176.1 | -36457.2 | -18.7 | -34.74 | 28.2 | -23.37 | 27.1 | 14/144 | 0.4717 | complete |
| gen10 | 2 | train | anthropic/claude-haiku-5.5 | 222 | -31222.8 | -21711.6 | -14.06 | -30.35 | 31.5 | -9.78 | 35.6 | 7/151 | 0.358 | complete |
| gen10 | 2 | train | anthropic/claude-haiku-5.5 | 208 | -31898.2 | -20612.8 | -15.34 | -32.62 | 26.0 | -9.91 | 32.6 | 14/151 | 0.3485 | complete |
| gen10 | 2 | train | anthropic/claude-haiku-5.5 | 217 | -49754.9 | -39168.5 | -22.93 | -41.66 | 25.3 | -18.05 | 28.4 | 16/151 | 0.3598 | complete |
| gen10 | 2 | train | anthropic/claude-haiku-5.5 | 237 | -50255.2 | -22443.9 | -21.2 | -36.32 | 27.8 | -9.47 | 33.7 | 12/151 | 0.3613 | complete |
| gen10 | 2 | score | anthropic/claude-haiku-5.5 | 179 | -21569.5 | -23771.2 | -12.05 | -24.75 | 30.7 | -13.28 | 29.9 | 42/144 | 0.5312 | complete |
| gen10 | 3 | unfinished | anthropic/claude-haiku-5.5 |  |  |  |  |  |  |  |  |  | 1.1656 | error: RuntimeError: model replies unreadable (4/6): '(empty reply)' |

### Latest lessons: blank lineage, generation 3 (anthropic/claude-haiku-5.5)

# Lessons Document: Generation 1 ## Status This generation made no trades, so it produced no evidence. Nothing below is a validated rule. Treat every item as a hypothesis to test, not a fact. ## What we know - **No trades, no results.** We have no data on which signals, instruments, expiries, strikes, or exits perform well or badly. - **Doing nothing is a valid baseline, not a failure.** Its score is zero. Any strategy you adopt should beat zero after costs, or it is not worth running. ## Starting principles (low confidence, untested) These are general reasoning, not findings. 1. **Start from the columns, not from a story.** Before trading, write down which columns you will use and what threshold or combination would trigger an entry. Decide this in advance, not after seeing outcomes. 2. **Prefer simple rules.** One or two conditions are easier to evaluate than many. Many conditions on a small sample mostly fit noise. 3. **Define the exit before the entry.** Set the exit rule (time-based, target, or stop) at the same time as the entry, so results are measurable. 4. **Pick one instrument and one expiry to begin.** Mixing instruments, expiries, and strikes makes results impossible to attribute. 5. **Strike choice matters, but we have no data on it.** Test at least two levels (for example, at-the-money and one step out-of-the-money) before drawing conclusions. ## How to build real lessons - **Log every decision**, including no-trade decisions and the reason for each. - **Record the columns' values at entry**, the exit reason, and the result after costs. - **Use a holdout.** Form rules on one segment of data and check them on a later segment. A rule that only works in-sample is not a lesson. - **Count trades before believing anything.** Under roughly 30 comparable trades, treat any win rate or average return as indicative only. Under 100, treat conclusions as provisional. - **Compare against doing nothing and against a simple baseline** (for example, always entering the same way with the same exit). - **Watch for overfitting:** if you tried many thresholds and kept the best, the result is likely luck. ## Confidence summary

### Latest lessons: blank-v2 lineage, generation 1 (anthropic/claude-haiku-5.5)

# Lessons for the Next Trader **Baseline:** Over 136 trades of $1,000 each, the overall result was -4.1% average and -5.5k total, with 45% winners. Trading shares was roughly flat (+0.4% average, -1.1% median, 92 trades). Most option variants lost money. Treat everything below as hypotheses, not established edges. ## Rules, with confidence 1. **Default to shares unless an option setup clearly beats them. Confidence: moderate.** Shares were the only large group near breakeven. Options lost on most variants, and their losses were often total (-100%), so one bad option trade costs far more than one bad share trade. 2. **Avoid 30-day calls struck above the money with a 10-day hold. Confidence: moderate.** The 30d +5%, +10%, and +15% hold10 groups averaged roughly -50% to -65%. Short expiry leaves too little time for the move to arrive. 3. **Avoid the "double_or_10" exit as a default. Confidence: moderate.** It produced the largest single gains and many of the largest losses. Its median outcome was poor, so it behaves like a lottery ticket, not a plan. 4. **Longer expiry (90 days) with a 10-day hold is the least bad option structure. Confidence: low.** The 90d +20% hold10 group averaged +13.6% over 3 trades, and the 90d +0% hold10 group had a positive median (+4.5%) but a negative average. Both samples are too small to trust. 5. **Do not trust the ratio columns (calls, puts, long, short, shares) as predictors. Confidence: moderate that they were not useful here.** Large and small values showed up in both winners and losers. I found no threshold that separated them. 6. **Short-term price moves (1d, 5d) and volatility (vol20) did not separate winners from losers in this data. Confidence: low.** Several large losses followed positive 1d and 5d moves, and some winners had weak early moves. ## What failed - Far-OTM short-dated calls: nearly every variant lost most of its premium. - Averaging across all option types hid the few winners. Medians were often worse than averages, meaning results depended on a handful of outliers. - Sizing every trade at $1,000 regardless of instrument risk. ## Sample caveats - Most groups have 1 to 11 trades. A single trade drives several results (the +258% and +123% gains each come from one or two trades). - Groups were chosen after seeing results, which inflates apparent edges. - Results cover one period. Regime changes may invalidate everything above. ## Next steps - Collect more trades in the 90-day hold10 structures before sizing up. - Test shares against 90-day options at equal dollar risk. - Record whether the exit rule fired and why, to separate strategy from luck.

## Wide list (chosen without hindsight)
- 300 stocks chosen; full options history done for 300

## Job notes (latest 8)
- 2026-10-09T13:47:23+00:00 focused: Options flow: blind rank correlation +0.009, top tenth +2.67%; Technical analysis: blind rank correlation +0.028, top tenth +2.91%; Market: blind rank correlation +0.015, top tenth -0.23%; News: blind rank correlation +0.017, top tenth -0.21%; Flow + technical: blind rank correlation +0.021, top tenth +2.64%; Everything: blind rank correlation +0.021, top tenth +2.91%
- 2026-10-09T13:47:23+00:00 focused-hindsight: wide-list passed: none
- 2026-10-09T13:47:10+00:00 focused-volatility: passed: Options flow, Technical analysis, Flow + technical, Everything; volatility-only top tenth +3.01%
- 2026-10-09T13:42:50+00:00 focused: Options flow: blind rank correlation +0.009, top tenth +2.67%; Technical analysis: blind rank correlation +0.028, top tenth +2.91%; Market: blind rank correlation +0.015, top tenth -0.23%; News: blind rank correlation +0.017, top tenth -0.21%; Flow + technical: blind rank correlation +0.021, top tenth +2.64%; Everything: blind rank correlation +0.021, top tenth +2.91%
- 2026-10-09T13:42:50+00:00 focused-volatility: passed: Options flow, Technical analysis, Flow + technical, Everything; volatility-only top tenth +3.01%
- 2026-10-09T05:33:11+00:00 focused: Options flow: blind rank correlation +0.009, top tenth +2.67%; Technical analysis: blind rank correlation +0.028, top tenth +2.91%; Market: blind rank correlation +0.015, top tenth -0.23%; News: blind rank correlation +0.018, top tenth -0.21%; Flow + technical: blind rank correlation +0.021, top tenth +2.64%; Everything: blind rank correlation +0.021, top tenth +2.91%
- 2026-10-09T05:30:45+00:00 benchmark: model (stock or calls) on blind months: 401 trades, average -4.35%, range (-9.13, -0.26), random same-trades -2.13%.
- 2026-10-09T05:30:45+00:00 benchmark-runs: 74 of 120 model runs beat the random same-trades picker.

## Errors (151 total, latest 8)
- 2026-10-09 01:03 IAC oi 2026-01-13: 504 The remote gateway timed out.
- 2026-10-09 00:59 FRSH oi 2025-07-07: 504 The remote gateway timed out.
- 2026-10-09 00:58 IAC oi 2025-06-26: 504 The remote gateway timed out.
- 2026-10-09 00:55 FRSH oi 2025-03-24: 504 The remote gateway timed out.
- 2026-10-09 00:55 IR oi 2025-07-10: 504 The remote gateway timed out.
- 2026-10-09 00:52 IAC oi 2024-10-28: 504 The remote gateway timed out.
- 2026-10-09 00:52 FRSH oi 2025-01-15: 504 The remote gateway timed out.
- 2026-10-09 00:51 IR oi 2025-04-07: 504 The remote gateway timed out.
