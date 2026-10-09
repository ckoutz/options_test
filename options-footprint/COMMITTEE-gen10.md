# Committee generations (2026-10-09 21:31 UTC)

Total spent on all agent runs: $7.79. Candidate pool: {'train': 2998, 'score': 1439, 'holdout': 2000, 'test': 2720}.

Four agents train independently on six stock bundles; code scores their rules; an editor writes the
notes passed on. The scoring run trades blind months with the editor's notes. "Random" makes the same
number and kind of trades on random candidates in the same weeks. Rating correlation: does a higher
rating go with a better 10-session stock return (0 = no skill, ranges are 95%). Every trade is $1,000.

## Runs

| gen | who | phase | trades | profit $ | random profit $ | mean % | win % | rating corr (95% range) | top rated % | bottom rated % | unreadable | cost $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | agent1 | train | 222 | -36788.3 | -27594.6 | -16.57 | 31.1 | 0.022 (-0.023 to 0.068) | 0.11 | 0.22 | 3/151 | 0.2907 |
| 1 | agent2 | train | 293 | -47796.0 | -43686.3 | -16.31 | 30.0 | -0.02 (-0.078 to 0.037) | -0.96 | 0.31 | 16/151 | 0.3067 |
| 1 | agent3 | train | 264 | -44071.2 | -38992.8 | -16.69 | 29.2 | 0.021 (-0.032 to 0.069) | 0.07 | 0.87 | 12/151 | 0.3117 |
| 1 | agent4 | train | 217 | -34204.3 | -33418.0 | -15.76 | 31.3 | 0.058 (0.016 to 0.106) | -0.21 | -0.46 | 1/151 | 0.2927 |
| 1 | scorer | score | 156 | -29176.1 | -36457.2 | -18.7 | 28.2 | 0.028 (-0.038 to 0.104) | -0.01 | 0.93 | 14/144 | 0.4717 |
| 2 | agent1 | train | 222 | -31222.8 | -21711.6 | -14.06 | 31.5 | -0.026 (-0.085 to 0.033) | -1.37 | 1.28 | 7/151 | 0.358 |
| 2 | agent2 | train | 208 | -31898.2 | -20612.8 | -15.34 | 26.0 | -0.015 (-0.061 to 0.031) | -1.03 | 0.77 | 14/151 | 0.3485 |
| 2 | agent3 | train | 217 | -49754.9 | -39168.5 | -22.93 | 25.3 | -0.034 (-0.089 to 0.021) | -0.46 | 1.56 | 16/151 | 0.3598 |
| 2 | agent4 | train | 237 | -50255.2 | -22443.9 | -21.2 | 27.8 | -0.035 (-0.087 to 0.017) | -1.49 | 1.32 | 12/151 | 0.3613 |
| 2 | scorer | score | 179 | -21569.5 | -23771.2 | -12.05 | 30.7 | -0.034 (-0.097 to 0.036) | 0.04 | 2.29 | 42/144 | 0.5312 |
| 3 | all | unfinished |  |  | - | - | - | - | - | - | 0/ | 1.1656 |

## Luck check

- Different rules tested on training data so far: 58 (by the agents and the editor).
- Editor rules checked on the blind months: 16; passed clearly (whole 95% range above buying everything the same way): 0.
- Expected to pass by luck alone: about 0.4. Treat a pass as real only if it clearly beats that count and the rule keeps passing in later generations.

## Blind scoring trades by list (hindsight check)

The big-mover list was chosen for stocks that later had 3+ days up 15%, so results there can come
from hindsight alone. The wide list (chosen from January 2024 data only) is the honest test.
Random = the same kind of trades on random candidates from the same list in the same weeks.

| gen | list | trades | mean % | random mean % | profit $ | random profit $ |
|---|---|---|---|---|---|---|
| 1 | big movers (hindsight) | 50 | -4.14 | -7.31 | -2,070 | -3,656 |
| 1 | wide (honest) | 106 | -25.57 | -24.11 | -27,106 | -25,559 |
| 2 | big movers (hindsight) | 62 | -1.59 | -4.74 | -987 | -2,936 |
| 2 | wide (honest) | 117 | -17.59 | -17.49 | -20,582 | -20,467 |

## Generation 2

### Editor's rules, tested on all training months and bundles

- Uptrend + sustained calls, 90d 5% OTM (when calls 5d avg > 1 and vs ma50 % > 0: buy the 90-day call 5% above the price, exit hold10): 224 trades, average -2.5% (95% range -11.4% to +5.2%, resampling whole weeks), median -20.5%, 39% winners. Buying every candidate the same way: -7.4%. Beat that in 5 of 6 bundles; first half of the months -0.5%, second half -3.9%.
- Stack: >$50, uptrend, calls, 90d 5% OTM (when price = >$50 and calls 5d avg > 1 and vs ma50 % > 0: buy the 90-day call 5% above the price, exit hold10): 73 trades, average -4.6% (95% range -16.9% to +8.5%, resampling whole weeks), median -22.1%, 37% winners. Buying every candidate the same way: -7.4%. Beat that in 4 of 6 bundles; first half of the months -2.8%, second half -5.9%.
- Over $50 30d ATM (when price = >$50: buy the 30-day call 0% above the price, exit hold10): 700 trades, average -1.7% (95% range -11.1% to +9.2%, resampling whole weeks), median -29.4%, 37% winners. Buying every candidate the same way: -10.9%. Beat that in 5 of 6 bundles; first half of the months +4.7%, second half -7.9%.
- Positive news tone 30d ATM (when news tone 7d > 0 and news 3d > 0: buy the 30-day call 0% above the price, exit hold10): 432 trades, average -0.1% (95% range -11.6% to +11.2%, resampling whole weeks), median -35.0%, 34% winners. Buying every candidate the same way: -10.9%. Beat that in 5 of 6 bundles; first half of the months +8.6%, second half -10.8%.
- Momentum 90d 5% OTM (when 20d % > 10: buy the 90-day call 5% above the price, exit hold10): 174 trades, average -1.0% (95% range -12.9% to +12.5%, resampling whole weeks), median -22.2%, 37% winners. Buying every candidate the same way: -7.4%. Beat that in 4 of 6 bundles; first half of the months +4.6%, second half -5.1%.
- Market+stock uptrend 90d ATM (when market 20d % > 0 and vs ma50 % > 0 and 20d % > 5: buy the 90-day call 0% above the price, exit hold10): 135 trades, average -3.8% (95% range -15.3% to +12.9%, resampling whole weeks), median -20.1%, 33% winners. Buying every candidate the same way: -8.4%. Beat that in 3 of 6 bundles; first half of the months +6.7%, second half -9.1%.
- Quiet after spike, uptrend 30d ATM (when days since spike >= 20 and calls 5d avg < 1 and vs ma50 % > 0: buy the 30-day call 0% above the price, exit hold10): 31 trades, average +55.9% (95% range -34.0% to +160.6%, resampling whole weeks), median -21.1%, 36% winners. Buying every candidate the same way: -10.9%. Beat that in 5 of 5 bundles; first half of the months +135.9%, second half +5.4%.
- Overbought chase 30d ATM (when rsi > 70 and vs ma20 % > 10: buy the 30-day call 0% above the price, exit hold10): 233 trades, average +4.8% (95% range -17.3% to +29.0%, resampling whole weeks), median -46.7%, 32% winners. Buying every candidate the same way: -10.9%. Beat that in 4 of 6 bundles; first half of the months -0.7%, second half +10.3%.

### The same rules on the blind scoring months (never shown to agents)

- Uptrend + sustained calls, 90d 5% OTM (when calls 5d avg > 1 and vs ma50 % > 0: buy the 90-day call 5% above the price, exit hold10): 177 trades, average -8.8% (95% range -18.8% to +3.1%, resampling whole weeks), median -20.6%, 30% winners. Buying every candidate the same way: -7.1%. Beat that in 3 of 6 bundles; first half of the months -11.1%, second half -6.3%.
- Stack: >$50, uptrend, calls, 90d 5% OTM (when price = >$50 and calls 5d avg > 1 and vs ma50 % > 0: buy the 90-day call 5% above the price, exit hold10): 66 trades, average -15.3% (95% range -25.8% to -1.6%, resampling whole weeks), median -20.1%, 30% winners. Buying every candidate the same way: -7.1%. Beat that in 2 of 6 bundles; first half of the months -20.3%, second half -11.2%.
- Over $50 30d ATM (when price = >$50: buy the 30-day call 0% above the price, exit hold10): 362 trades, average -19.0% (95% range -32.5% to -5.1%, resampling whole weeks), median -39.9%, 30% winners. Buying every candidate the same way: -14.7%. Beat that in 1 of 6 bundles; first half of the months -12.9%, second half -24.7%.
- Positive news tone 30d ATM (when news tone 7d > 0 and news 3d > 0: buy the 30-day call 0% above the price, exit hold10): 253 trades, average -7.5% (95% range -22.6% to +7.0%, resampling whole weeks), median -31.7%, 35% winners. Buying every candidate the same way: -14.7%. Beat that in 6 of 6 bundles; first half of the months -6.4%, second half -8.3%.
- Momentum 90d 5% OTM (when 20d % > 10: buy the 90-day call 5% above the price, exit hold10): 116 trades, average -8.1% (95% range -20.6% to +5.3%, resampling whole weeks), median -24.3%, 28% winners. Buying every candidate the same way: -7.1%. Beat that in 2 of 6 bundles; first half of the months -12.6%, second half -3.5%.
- Market+stock uptrend 90d ATM (when market 20d % > 0 and vs ma50 % > 0 and 20d % > 5: buy the 90-day call 0% above the price, exit hold10): 138 trades, average -6.1% (95% range -15.0% to +6.2%, resampling whole weeks), median -24.9%, 30% winners. Buying every candidate the same way: -7.2%. Beat that in 4 of 6 bundles; first half of the months -7.4%, second half -4.6%.
- Quiet after spike, uptrend 30d ATM (when days since spike >= 20 and calls 5d avg < 1 and vs ma50 % > 0: buy the 30-day call 0% above the price, exit hold10): 22 trades, average -6.0% (95% range -41.5% to +31.6%, resampling whole weeks), median -16.8%, 32% winners. Buying every candidate the same way: -14.7%. Beat that in 2 of 4 bundles; first half of the months +4.9%, second half -19.1%.
- Overbought chase 30d ATM (when rsi > 70 and vs ma20 % > 10: buy the 30-day call 0% above the price, exit hold10): 191 trades, average -19.9% (95% range -34.2% to -3.9%, resampling whole weeks), median -47.0%, 28% winners. Buying every candidate the same way: -14.7%. Beat that in 1 of 6 bundles; first half of the months -21.5%, second half -18.3%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

(Committee editor's synthesis of four independent traders over six bundles. Where a trader's figure and the code-tested scorebook differ, the scorebook is used.)

## 0. Bottom line

- **No rule has a proven edge.** No rule has a positive average whose 95% range (resampling whole weeks) excludes zero. Almost every rule has a negative median, and win rates run 28% to 40%.
- **What all four traders agreed on:**
  - Buying options loses money on median. The stock median over 10 sessions is about -0.2% to -1%, while the option median is -20% to -60%.
  - 14-day expiries are bad. Many trades go to -100%.
  - Averages are carried by a few large winners, so judge by median and by the count of bundles beating the benchmark.
  - Extremes lists (best and worst names) are not evidence. Both tails are full of high-volatility names with the same features.
  - Ratings (+2 to -2) carry no stable signal.
- **The job is to lose less, then find a real winner.** Always judge a rule against the same-expiry, same-strike, same-exit benchmark of buying every candidate:

| Structure (hold 10 sessions unless noted) | Benchmark average |
|---|---|
| 30-day at-the-money call | -10.9% |
| 90-day at-the-money call | -8.4% |
| 90-day call 5% above price | -7.4% |
| 30-day double-or-10 exit | -12.0% |

- **The pattern in the scorebook:**
  - Strength, trend, large size and positive news are least bad.
  - Oversold dips, call-volume spikes and falling-knife entries are consistently worst.
  - This is the main stable finding, and the rules below build on it.

## 1. STRATEGY: setups worth trading (small size or paper)

All entries are bought on the entry day and exited after 10 sessions. These are "least-bad, worth refining", not validated edges. Every one still has a negative median except where noted. Lists are ordered by combined evidence: number of trades, bundles beating the benchmark, and stability across the two halves of the sample.

### 1A. Tier 1: beat the benchmark in 5 of 6 bundles with large n

**Broad call base in an uptrend, 90-day call 5% above the price**
- **Rule:** calls 5d avg > 1 and vs ma50 % > 0.
- **Scorebook:** 224 trades, average -2.5% (range -11.4% to +5.2%), median -20.5%, 39% winners.
- **Versus benchmark:** beat the -7.4% benchmark in 5 of 6 bundles. First half -0.5%, second half -3.9%.
- **Why it ranks first:**
  - It has the most stable halves of any rule.
  - It has the best win rate in the book.
  - It is the only rule that combines an uptrend with sustained, moderate call interest, as opposed to a one-day spike.
- **Source:** Agent 4's idea, confirmed by code.

**Over $50 stocks, 30-day at-the-money call**
- **Rule:** price band over $50.
- **Scorebook:** 700 trades, average -1.7% (range -11.1% to +9.2%), median -29.4%, 37% winners.
- **Versus benchmark:** beat the -10.9% benchmark in 5 of 6 bundles. First half +4.7%, second half -7.9%.
- **Caveats:**
  - Only the 30-day version is strong. The 90-day at-the-money version over $50 (190 trades, -8.0%, median -15.2%, beat in 3 of 6 bundles, halves -8.7% and -7.4%) is no better than its -8.4% benchmark.
  - Agent 1 championed this band. Agents 2, 3 and 4 dropped it after reading extremes lists, so the full-sample test settled the disagreement for the 30-day version only.
  - Likely reason (untested): big, liquid names have cheaper, less hyped premium and fewer total-loss outcomes.

**Positive news tone, 30-day at-the-money call**
- **Rule:** news tone 7d > 0 and news 3d > 0.
- **Scorebook:** 432 trades, average -0.1% (range -11.6% to +11.2%), median -35.0%, 34% winners.
- **Versus benchmark:** beat it in 5 of 6 bundles. First half +8.6%, second half -10.8%.
- **Caveat:** the regime split is large. Traders dropped "news" as a filter based on extremes lists, which the full test contradicts.

### 1B. Tier 2: 4 of 6 bundles, decent n

**Momentum, 90-day call 5% above the price**
- **Rule:** 20d % > 10.
- **Scorebook:** 174 trades, average -1.0% (range -12.9% to +12.5%), median -22.2%, 37% winners.
- **Versus benchmark:** beat it in 4 of 6 bundles. Halves +4.6% and -5.1%.
- **At-the-money version:** 179 trades, -5.6%, beat in 3 of 6 bundles. The 5% out-of-the-money strike did better than at-the-money here and in Agent 4's pooled notes, but only at 90 days. At 30 days the strike effect flipped sign.

**Market and stock both in an uptrend, 90-day at-the-money call**
- **Rule:** market 20d % > 0 and vs ma50 % > 0.
- **Scorebook:** 184 trades, average -3.2%, median -19.8%, 34% winners.
- **Versus benchmark:** beat it in 4 of 6 bundles. Halves -0.6% and -4.4%.
- **Variant:** 20d % > 10 and vs ma50 % > 0 gave 150 trades, -5.1%, 3 of 6 bundles, halves +4.3% and -10.2%.

**Strong stock with a call spike, 30-day at-the-money call**
- **Rule:** calls > 3 and vs ma20 % > 0.
- **Scorebook:** 565 trades, average -4.1%, median -39.0%, 32% winners.
- **Versus benchmark:** beat it in 4 of 6 bundles. Halves -2.1% and -6.2%.
- **Contrast:** the same spike filter with no trend condition is terrible at 90 days (see section 2). The trend condition is what makes it tolerable.

**Overbought chase, 30-day at-the-money call**
- **Rule:** RSI > 70 and vs ma20 % > 10.
- **Scorebook:** 233 trades, average **+4.8%** (range -17.3% to +29.0%), median -46.7%, 32% winners.
- **Versus benchmark:** beat it in 4 of 6 bundles. First half -0.7%, second half +10.3%.
- **Why it matters:**
  - It is the best average at this sample size, and Agent 3 designed it as an "avoid" rule.
  - It shows that strength is not worse than average.
  - The median is very poor, so the average rests on a few big winners.
  - Treat it as a tail-driven candidate, not a safe edge.
- **Caution:** the 90-day at-the-money version with an extra 5d % ≥ 10 condition lost heavily (see section 2). The 30-day result is not robust to that change.

**Momentum with moderate RSI, 30-day at-the-money call**
- **Rule:** RSI 45 to 75 and 20d % ≥ 10.
- **Scorebook:** 382 trades, average -1.2%, median -44.2%, 28% winners.
- **Versus benchmark:** beat it in 3 of 6 bundles. Halves +4.0% and -6.4%.

### 1C. Tier 3: interesting but weak or unstable

- **Quiet after a spike, 30-day at-the-money call.**
  - Rule: days since spike ≥ 20 and calls 5d avg < 1.
  - Scorebook: 117 trades, average +10.1% (range -19.8% to +48.3%), median -37.9%, 34% winners.
  - Beat the benchmark in only 2 of 6 bundles, but both halves were positive (+20.3% and +1.6%).
  - This is the opposite of "buy the spike". It looks at names where call interest has been absent.
  - Only one trader saw it, and it is wide-ranged. Worth refining and stacking.
- **Spike with no news and a rising stock, 30-day at-the-money call.**
  - Rule: spike, no news ≥ 1 and 5d % > 5.
  - Scorebook: 208 trades, average -7.0%, median -34.0%, beat the benchmark in 5 of 6 bundles. The 5d % condition does the work.
  - On its own, "spike, no news" is a clear loser (section 2).
- **Oversold at 90 days.**
  - Rule: RSI < 35 and vs ma50 % < -10, 90-day at-the-money call.
  - Scorebook: 48 trades, average -1.5%, median -10.0% (the best median in the book), 40% winners.
  - Beat the benchmark in only 2 of 6 bundles. The tighter variant (off high % < -30 and RSI < 30, 25 trades) had halves of -45.2% and +12.0%, which is noise.
  - Do not use the 30-day or 5%-out-of-the-money versions of oversold, which lose heavily.
- **Sharp 1-day drop, 90-day call 5% above the price.**
  - Rule: 1d % ≤ -5.
  - Scorebook: 51 trades, +3.9% (range -20.2% to +32.1%), median -23.2%, 3 of 6 bundles. Halves +16.9% and -6.8%.
  - The 30-day version with a call spike is the worst rule in the book. Treat the 90-day result as noise.

### 1D. Sizing and execution (all traders agree)

- Flat, small size. Never add after wins. Assume any option can go to -100%.
- Do not use 14-day expiries. Use 30-day or 90-day calls.
- Strikes: at the money or 5% above the price. Do not go 10% or more out of the money.
- Exits:
  - Hold 10 sessions is the standard exit.
  - In the scorebook, hold-10, double-or-10 and a -50% stop could not be told apart on common entries.
  - Double-or-10 has a worse benchmark (-12.0% vs -10.9%), so no exit has been shown to help.

## 2. AVOID

### Clearly worse than the benchmark (code-confirmed)

| Rule | Trades | Average (range) | Median | Beat benchmark |
|---|---|---|---|---|
| Large down day with call spike (1d % ≤ -5 and calls ≥ 3), 30-day, hold 10 | 95 | **-23.2%** (-42.2% to +2.3%) | -48.6% | 1 of 6 |
| Calls ≥ 3 and price $10 to $50, 90-day | 103 | **-21.9%** (-31.1% to -12.2%) | -30.5% | 1 of 6 |
| Stretched-up (RSI ≥ 70, vs ma20 % ≥ 10, 5d % ≥ 10), 90-day at the money | 48 | **-20.6%** (-31.1% to -8.8%) | -33.8% | 2 of 6 |
| Spike, no news ≥ 1, 90-day at the money | 138 | **-19.4%** (-28.7% to -10.8%) | -25.2% | 0 of 6 |
| Oversold with high volatility (vol20 % ≥ 4, RSI < 40), double-or-10 | 218 | **-18.7%** (-30.9% to -7.0%) | -46.6% | 2 of 6 |
| Low-volatility dip (20d % < -10 and vol20 % < 4), 30-day | 196 | **-18.0%** (-33.5% to -1.1%) | -43.7% | 2 of 6 |
| Oversold (RSI < 45 and off high % < -25), 30-day | 326 | **-17.1%** (-31.1% to -2.4%) | -46.9% | 1 of 6 |
| Calls ≥ 3 with no other condition, 90-day | 234 | **-15.2%** (-22.0% to -7.7%) | -28.2% | 1 of 6 |
| Call-days surge (call days 2x+ ≥ 4 and calls 5d avg > 2), 30-day | 256 | -15.0% | -47.9% | 2 of 6 |
| Oversold deep drawdown (RSI < 35, off high % < -25, 20d % < -15), 30-day | 160 | -14.6% | -50.8% | 2 of 6 |
| Oversold pullback (off high % ≤ -20 and RSI < 40), 90-day call 5% above | 73 | -14.6% (-27.3% to +0.2%) | -33.3% | 1 of 6 |

**Themes:**
- Dip-buying with calls loses at every expiry and strike tested.
- Buying call-volume spikes (especially with no news, or on falling or mid-priced stocks) loses. Spike days mean expensive premium.
- The sign of "spike" flips once the stock is above its 20-day average, which is why 1B treats trend as the key condition.

### Nothing there (no edge either way)
- Deep oversold rebound (RSI ≤ 25, vs ma20 ≤ -20, off high ≤ -35): 42 trades, halves -72.8% and +13.8%. Noise.
- Extended names (RSI ≥ 75 and vs ma20 ≥ +20): 96 trades, -8.2%. The "extended names fade" idea is unsupported.
- Sustained call building (calls 5d avg ≥ 2 and call days 2x+ ≥ 3), 30-day: 573 trades, -8.9%, 3 of 6 bundles. Roughly the benchmark.
- Put crowding (puts 5d avg ≥ 3): 727 trades, -9.2%, 4 of 6 bundles. It is not a bearish signal. Halves +2.3% and -22.1%.
- Under-$10 after a 20-day run-up (90-day): 36 trades, -11.1%, 3 of 6 bundles. Under-$10 names produced most of the -100% outcomes, but the group is mixed.
- Ratings of any kind:
  - Traders reported a "+1 underperforms" pattern, but it held in some bundles and not in others (2 of 4 by one trader). Median and average disagreed.
  - The "-1 outperforms" pattern did not repeat.
  - Ratings at -2 and +2 have too few names.
  - Do not use ratings.

### Stop doing
- 14-day expiries, and any strike 10% or more out of the money.
- Reading extremes lists as evidence. Several traders' "avoid" and "do not chase" ideas were contradicted by full tests.
- Using any exit rule to rescue a losing entry. No exit has been shown to help.
- Judging by total P&L or by averages alone.

## 3. NEW IDEAS TO TEST

1. **Stack the confirmed "less bad" features at 90 days (highest priority, untested).**
   - Try over $50, positive news tone (news tone 7d > 0 and news 3d > 0), market 20d % > 0, vs ma50 % > 0, 20d % > 10 and calls 5d avg > 1 in various combinations.
   - Use a 90-day call 5% above the price, or at the money.
   - Each feature alone beat its benchmark in 4 to 5 of 6 bundles, but all single rules did worse in the second half.
   - Require n ≥ 60. Test in both halves of the sample.
2. **Regime gate (untested).**
   - Nearly every rule earned its better average in the first half. Test whether market 20d % > 0, or a market 5d % filter, explains the split.
   - If so, the real edge may be "buy strength in an uptrending market", with stock-level filters secondary.
3. **Substitute stock or deep in-the-money calls (untested).**
   - Stock medians sit near zero while option medians sit near -30% to -60%, so the wrapper costs most of the loss.
   - Test a 90-day call 5% to 10% below the price (delta about 0.8) on the Tier 1 and Tier 2 setups. Also test a bull call spread to cut premium.
   - Compare each with the same setup's stock return.
4. **Buy before the crowd, not at the spike (partly confirmed).**
   - Quiet-after-spike (+10.1% average, both halves positive) and the positive result for strength without a fresh spike suggest an edge in names not yet crowded.
   - Test days since spike ≥ 20 together with an uptrend (vs ma50 % > 0, 20d % > 0), and with over $50.
   - Also try the 20-day measures that no trader tested: calls 20d, long calls 20d and call days 2x+ 20d. These capture slow, sustained buying, which may be cheaper than a one-day surge.
5. **Volatility-aware premium filter (untested).**
   - Loss size seems tied to premium level. Test vol20 % bands (below 2%, 2% to 4%, above 4%) within over-$50 and within trend setups.
   - Combine with 60-day and 120-day expiries, which have not been tried. Longer expiries seem to cut total-loss outcomes.
6. **Fade the losers with defined risk (untested, high risk).**
   - The worst cells lose 18% to 23% on average with ranges that exclude zero: large down day with spike, oversold quiet names, spike with no news.
   - Test a bear call spread or covered call on paper only, with a tail-loss check, since the same names occasionally produce huge rebounds.
7. **Unused features to scan.**
   - These columns were barely used: shares volume ratios (shares, shares 5d avg), close vs vwap %, vs vwap20 %, otm calls 20d, short/medium/long mix, p/c drop, news 1d.
   - Test each as a single-feature bucket at 90 days, alongside trend, and keep what beats the benchmark in at least 4 of 6 bundles.
8. **Reversal vs momentum bucket test.**
   - Bucket the full universe by 20d %, RSI and vol20 %, and compare option returns to the same-expiry benchmark.
   - This should settle the "momentum beats reversal" read that the current results suggest.

## 4. OPEN QUESTIONS

- **Can any call setup have a positive median?** None does. The least negative are 90-day oversold (-10.0%, small n), 90-day over-$50 (-15.2%) and the trend setups (about -20%). Is that reachable with calls at all, or only with stock, deep in-the-money calls or spreads?
- **Is over-$50 size, liquidity, lower implied volatility, or a proxy for something else?** It beat the benchmark at 30 days in 5 of 6 bundles but barely at 90 days.
- **Which half of the sample is the regime?** Why did nearly every rule do better in the first half? Is it market trend, volatility, or the earlier weeks?
- **Direction vs decay:** how much of each option loss comes from the stock not moving versus premium collapse? Pair each option trade with its own stock return and entry implied volatility (not yet available).
- **Do exits differ?** Hold-10, double-or-10 and a stop were identical in the scorebook. Can they be scored on common entries with premium paths?
- **Strike:** 5% above the price beat at the money at 90 days (benchmark -7.4% vs -8.4%), but the 30-day comparison flipped. Is the strike effect real?
- **Why do the 30-day and 90-day versions of "overbought chase" disagree** (+4.8% vs -20.6% with an extra 5d % ≥ 10 condition)? Is 5d % ≥ 10 the toxic ingredient (a spike on the last few days)?
- **Ratings:** the traders disagreed on "+1 underperforms", and the scorebook shows no stable signal. Treat as noise unless a full-universe test with n ≥ 60 says otherwise.

### Agent 1's final notes (not passed on)

# Options and Ratings Playbook (after bundles 1 to 6)

## 1. MY CURRENT STRATEGY

### Live rule
- **Live size: zero.** No option structure has passed the pass criteria in section 4. Stock-level ratings have one candidate filter that passes the stock-level test, but the option version has not been tested.
- **Paper benchmark (logged every bundle, unchanged):** buy one at-the-money (ATM) call with a 90-day expiry on the bundle's entry date. Strike within about 0% of the price. Exit after 10 sessions regardless of P&L. Equal notional per trade.
- **Benchmark record, 10-session median by bundle:** -9.2% (n=4), -17.5% (n=14), -24.6% (n=23), -37.4% (n=22), -19.5% (n=17), -6.7% (n=11). Pooled, about 91 trades. The median has been negative in all six bundles. Bundle 6 was the least negative so far, but n=11 is too small to call it a trend.
- **Confidence that the benchmark has positive expectancy: none.**

### Instrument, strike, expiry, exit
- **Calls only.** Puts have added noise in every bundle and have not helped any filter.
- **Strike:** ATM is the benchmark. OTM is paper only. Results have been mixed (bundle 5: 90-day +20% OTM +31% on 2 trades; bundle 6: 90-day +10% OTM +168% on 1 trade; 14-day OTM lines lost heavily in both bundles). Confidence that OTM is better: low.
- **Expiry: 90 days is the only expiry I keep.**
  - **14-day: dropped as a candidate.** The 14-day ATM double-or-10 line was the one paper result I had flagged as interesting. Bundle 5 had 3 trades with a median of +126%. Bundle 6 had 23 trades with a median of -93.8% and an average of -29.9%. Pooled, the line is clearly negative. Stop logging it as a live or paper hope; keep it only as a cautionary data point.
  - **30-day: dropped.** Bundle 5 median -24.5% (n=7). Bundle 6 median -44.3% (n=5, average -23.4%). Negative in both.
  - **14-day hold-10, 14-day OTM, 30-day OTM:** all lost heavily. Paper only, and not worth continuing.
- **Exit: hold 10 sessions for the benchmark.** Double-or-10 has now failed to reach its target in almost every trade, so drop it as an exit for short expiries. Do not rank other exits until I have per-trade stock returns.

### Why option returns lag stock returns (working model)
- In bundle 6 the universe median stock return over 10 sessions was -0.2%. The 90-day ATM benchmark median was -6.7%. In bundle 5 the gap was about 18 points. In bundle 4 it was about 37 points. The gap is narrowing but still present.
- Working explanation (unconfirmed): premium decay and implied-volatility changes cost more than the stock move gives back, and buying after a call-volume surge pays up for the move that has already happened.
- Working rule until the decomposition in section 3 is done: **the stock must rise by more than the premium for the trade to win.** Assume the premium is large relative to a 10-session move.
- **Gap to close:** I still cannot match each option trade to its own 10-session stock return. The bundle 6 feedback gives option results and stock features for trades and a separate list of stock extremes, but not the stock return for each trade. Until that is logged, I cannot say whether losing trades were direction losses or premium losses.

### Universe and price bands
- **Price band is now the strongest variable I have seen, but the evidence is partial.** Bundle 6 extremes:
  - Over $50: all six shown trades were positive. Three 14-day trades (+102%, +116%, +124%, +134%, four in the list) and two 90-day trades (+60%, +98%). Among the trades I can see, none over $50 lost heavily.
  - Under $50: the worst trades were almost all $10 to $50 or under $10, many at -100%.
  - Bundle 5 extremes over $50 split both ways (-93% and +96% on 90-day ATM). So over-$50 is not yet a rule.
  - Caveat: the lists show extremes, not all trades. I cannot compute the over-$50 median from them.
- **Over $50: default research universe.** Low-to-medium confidence that it is better. Test it properly (section 3).
- **$10 to $50 and under $10: paper only.** Largest stock moves and largest option losses have been here in most bundles.

### Ratings (stock-level only; not an option entry filter yet)
Ratings are judged on stock returns over 10 sessions, against the universe median in the same bundle.

| Rating | Bundle 4 avg / median (n) | Bundle 5 avg / median (n) | Bundle 6 avg / median (n) | Read |
|---|---|---|---|---|
| +1 | -1.5% / -0.5% | -2.8% / -3.1% (16) | -4.4% / -0.9% (29) | Median below universe in 3 of 3 bundles. Average well below. Candidate "avoid" filter. |
| +0 | -0.5% / -0.9% | -0.1% / -0.8% (98) | +1.3% / +0.1% (116) | Near universe. No edge. |
| -1 | +1.9% / +0.8% (96) | +3.0% / -0.8% (120) | +0.4% / +0.5% (89) | Median above universe in 3 of 3 bundles. Edges +1.1, +0.2, +0.7 points. Small. |
| -2 | +12.3% / -2.8% (10) | -16.3% / -12.7% (6) | +6.2% / +4.6% (4) | Mixed. Dropped as a contrarian signal. |

Universe reference, 10-session stock median: bundle 4 -0.3%, bundle 5 -1.0%, bundle 6 -0.2%.

**Interpretation:** my "bearish" ratings (-1) have tended to rise more than the universe, and my "bullish" ratings (+1) have tended to fall relative to it. The -1 and +1 effects are small in the -1 case and somewhat larger in the +1 case. Neither is large enough to pay option premium on its own.

## 2. WHAT I TESTED IN THIS BUNDLE and how it went

### Bundle 6 option results (42 trades, -$8,864; average -21.1%, median -59.4%; 36% winners)
- **14-day ATM double-or-10:** 23 trades, average -29.9%, median -93.8%. Most trades expired near -100%. The strategy needed a doubling inside 10 sessions on short-dated calls, and that almost never happened. **Dropped.**
- **90-day ATM hold-10 (benchmark):** 11 trades, average -7.5%, median -6.7%. Best median of the six bundles, still negative. Shown winners include +49% and +90% ($10 to $50) and +60% and +98% (over $50).
- **30-day ATM hold-10:** 5 trades, average -23.4%, median -44.3%. **Dropped.**
- **14-day +5% OTM double-or-10:** 1 trade, -81.5%. Single trade; paper only.
- **14-day ATM hold-10:** 1 trade, -86.5%. Single trade; paper only.
- **90-day +10% OTM hold-10:** 1 trade, +168.3%. Single trade, $10 to $50; paper only.

### Universe (248 candidates)
- Average +0.1%, median -0.2%. Flat. The market did not drive the option losses.

### Stock-level ratings test (section 1 table)
- **+1 names:** median below universe in all three measured bundles (bundle 6: -0.9% vs -0.2%). Average gap about 4.5 points in bundle 6.
- **-1 names:** median above universe in all three measured bundles. Pooled n across bundles 4, 5 and 6 is about 305 names (96, 120, 89). Median edges +1.1, +0.2, +0.7.
- **-2 names (n=4):** average +6.2%, median +4.6%. Too few names to use, and the sign has not held across bundles.

### Extremes (stock outcomes; hypothesis generation only)
- **Biggest stock losers (-18% to -37%):** mostly under $50, many rated 0 or -1, often with large prior run-ups or strong recent call buying. Several had news in the prior 7 days.
- **Biggest stock winners (+19% to +56%):** mostly under $50 and often well below the 60-day high, with a mix of very low and very high RSI. Call buying was common on both sides.
- **Features that appeared on both sides:** call-days 2x+, "spike, no news," high call ratios, and large 20-day moves. These do not separate winners from losers.
- **Drawdown-reversal hypothesis:** deep drawdowns with oversold RSI rebounded in several extremes, and large run-ups faded in several others. This is still based on extremes only. Not tested on the full universe.

### New idea I tried
- **Over-$50 vs under-$50 on option returns (from the bundle 6 extremes).** The pattern is suggestive but based on the shown trades, not the full set, so there is no base rate. Carried forward as a pre-registered test (section 3, item 3).

### What I still could not decompose
- The per-trade stock return over the same 10 sessions is still not logged. This is the most important missing field, and I failed to log it again in bundle 6.

## 3. WHAT I WILL TRY NEXT (bundle 7 onward)

1. **Decompose every trade (mandatory, first).** For every option trade, log:
   - the stock's 10-session return over the same window,
   - the option return,
   - expiry days and strike distance at entry,
   - vol20 % at entry (implied-volatility proxy),
   - price band,
   - calls 5d avg and call days 2x+ at entry.
   Read: stock up more than the premium but option lost = strike or IV effect. Stock flat or down with a large option loss = direction plus premium decay. Options losing 40% or more with the stock flat = premium and IV are the main cost.
2. **Price band, pre-registered (highest priority).** Compare 90-day ATM hold-10 for over $50 vs $50 and under, using identical entries. Report the median for each band and the trade count. Target at least 40 over-$50 trades pooled across bundles 3 to 6. Pass: higher median in at least 2 of 3 bundles. Bundle 6 extremes suggest it may pass; the data does not yet show it.
3. **Stock-level +1 "avoid" test.** Pool +1 names against the universe on 10-session stock returns, by price band. Current evidence: median below universe in 3 of 3 bundles, n of about 45 or more. Pass rule for a no-buy filter: pooled n of at least 60 and a lower median than the universe in at least 3 of 4 bundles. If it passes, test whether skipping +1 names improves the 90-day benchmark median on option returns.
4. **Stock-level -1 test, option-level follow-up.** Stock-level pass rule as written: pooled n of at least 150 and a higher median than the universe in at least 2 of 4 bundles (3, 4, 5, 6). Bundles 4, 5 and 6 satisfy the stock-level rule (n about 305), with small margins. Bundle 3 is not in my notes. Next step: test -1 names on the 90-day ATM option, versus all other names, on option return. The option test decides whether the stock edge is tradable. Confidence that -1 is a tradable edge: low.
5. **Drawdown-reversal test (stock level, pre-registered).** Names more than 30% below their 60-day high with RSI below 30, vs all other names in the same price band, on 10-session stock return. Pass rule: pooled n of at least 60 across bundles 5 and 6, and a higher median than the universe in both bundles. Bundle 6 data does not include full-universe splits, so this test cannot be run yet. Log every name, not just extremes.
6. **Keep the 90-day ATM hold-10 benchmark.** Log it every bundle, no live size.
7. **Volatility tier (paper).** Within over-$50 names, split by vol20 % at the batch median. Test whether low-vol names lose less to premium on the same stock return.
8. **News and spike test (paper).** Compare 90-day ATM hold-10 by:
   - A: spike present (call volume at least 3x normal in the last 5 sessions, or call days 2x+ of 3 or more) and news in the prior 1 to 3 days,
   - B: spike present and no news,
   - C: no spike.
   Also compare buying before a spike (days since spike 10+) vs at the spike (days since spike 0). Group A must beat the benchmark median in 2 bundles before it becomes a filter.
9. **Deep ITM substitute (paper).** Over-$50 names, 90-day expiry, strike 5% to 10% below price, same exit. Compare option return to stock return to see whether the option tracks the stock more closely.
10. **Longer expiry (paper).** 180-day ATM hold-10 on the same candidates, to test whether the 90-day loss is mostly fast decay.
11. **Market regime split.** Split by market 20d % (above and below zero). Check whether losses cluster in down-market windows. Bundle 6 market 20d was mixed and did not obviously drive results.

## 4. Pass criteria for any filter going live
- At least 40 trades in the group, pooled across bundles.
- A better median than the 90-day ATM hold-10 benchmark on the same candidates, in at least 2 of 3 bundles.
- Stock-level check first: the filter improves the stock's own return, or it reduces the option's excess loss over the stock's move. The option result alone is not enough.
- No single trade or small cluster drives the result. Report the median and how many trades drive the average.
- Ratings and any stock-level filter: pass on stock returns first, then on options.

## 5. Supporting evidence and dropped ideas

### Held up (low confidence)
- **90-day ATM as the least bad benchmark.** Median negative in all six bundles. Bundle 6 median (-6.7%) is the least negative so far. Least bad, not a winning setup.
- **Stock-level -1 edge.** Median above universe in bundles 4, 5 and 6 (+1.1, +0.2, +0.7 points). Small. Needs the option-level test.
- **Stock-level +1 underperformance.** Median below universe in bundles 4, 5 and 6, with a bigger average gap. Candidate avoid filter.
- **Universe flatness.** Median stock return near zero in bundles 4, 5 and 6 (-0.3%, -1.0%, -0.2%). The option structure, not the market, drives the loss. Medium confidence.
- **Price band (over $50 vs smaller names).** Every over-$50 trade shown in bundle 6 was positive, and the smaller-name losers dominate the extremes. Bundle 5 extremes were mixed. Open, medium-low confidence. This is the leading research idea.

### Weakened or dropped
- **14-day double-or-10 as a paper hope.** Bundle 5 looked good on 3 trades (median +126%). Bundle 6 on 23 trades was -93.8%. Dropped.
- **14-day and 30-day expiries.** Repeated losses, many near -100%. Dropped as candidates. 30-day ATM median -24.5% (bundle 5) and -44.3% (bundle 6).
- **Ratings -2 as a contrarian long signal.** Bundle 4 average positive but median negative; bundle 5 clearly negative; bundle 6 positive but n=4. Dropped.
- **OTM better than ATM.** Inconclusive. Keep ATM as benchmark. OTM remains paper only.
- **Spike and call-volume features as predictors.** Appear on both sides of the extremes in every bundle. Not a filter.
- **Ratings as an option entry filter.** Dropped until the option-level test is run.
- **RSI alone and vol20 alone as filters.** No clean separation. The drawdown-reversal hypothesis (section 3, item 5) tests RSI together with depth off the high on stock returns.

### Extremes lists are for hypotheses only
- The extremes lists (stock and trade) are not a base rate. Each hypothesis needs a pre-registered test on the full universe, logged for every name.

### Contradictions to keep in view
- The benchmark median improved in bundle 6 (-6.7%), but the sample is 11 trades. The trend across six bundles is not reliably improving.
- The universe median was flat in bundles 4, 5 and 6, yet the benchmark lost 7% to 37%. The cost is in the option structure, the entry timing, or both.
- Over-$50 trades were all positive in the bundle 6 extremes, yet over-$50 names split both ways in bundle 5. Price band may matter, but I have not separated it from the other features.
- The -1 rating beats the universe on median by small amounts in three bundles. The +1 rating underperforms by larger amounts in the same bundles. The asymmetry is worth testing, but neither is yet an option trade.
- Big winners and losers still share features (call buying, spikes, large 20-day moves). These features have not predicted direction in any bundle.

### Agent 2's final notes (not passed on)

# TRADING NOTES: revised after bundle 6 (fresh stocks, 248 candidates, 33 option trades)

## 1. MY CURRENT STRATEGY

**Status: no live trades.** Six bundles in, no stock-level setup has passed the pass rule (section 1.4), and no option structure has beaten the stock it was written on. Everything stays paper-tracked. Bundle 6 lost $13,586 on 33 option trades (median −60%, 12% winners). Bundle 5's +$3,090 was not an edge, and bundle 6 confirms that.

**Default action: do not trade.** The only thing I will act on is a rule that clears the pass rule. Until then, I hold no positions.

### 1.1 Universe and benchmark
- **Price band:** live consideration only for stocks at $10 and above. Under-$10 names stay paper-tracked. Their option results range from −100% to +200%+, and that spread is not controllable.
- **Benchmark:** every stock-level test is judged against the same bundle's universe median over 10 sessions, not against zero.
- **Universe medians (10-session):** bundle 2 +0.3%, bundle 3 −1.0%, bundle 4 −0.3%, bundle 5 −1.0%, bundle 6 −0.2% (average +0.1%). Across five bundles the typical stock drifts slightly negative to flat. Any selection rule has to add return on top of that.
- **Confidence that the universe is flat-to-negative:** high (about 1,250 stock observations).

### 1.2 Stock-level paper setups (10-session return, hold 10 sessions)

**Setup A: momentum confirmation (unscored).**
- calls ≥ 2, news tone 7d > 0, news 3d > 0, vs ma50 % > 0.
- Prediction: no beat of the universe median. Not yet scored on full-sample stock returns, because bundle summaries only show extremes.

**Setup B: stretched-up avoid flag (paper, avoid test only).**
- rsi ≥ 70 AND vs ma20 % ≥ +10 AND 5d % ≥ +10.
- Question: is the 10-session median below the universe median? If so, it becomes a "do not chase a spike" flag for long entries. It is not a short signal.
- Evidence: bundle 5's two worst stocks fit it. Bundle 6 did not support it. The largest winners included several stretched names (rsi 68–73, vs ma20 +13% to +33%, 5d up to +47%), and one near-miss (rsi 69, 5d +47%, vs ma20 +32%) gained +37%. Among the listed losers, the stretched-looking ones mostly failed the rsi or 5d condition. Net: B is mixed across bundles and has no clean support yet.
- Confidence: low.

**Setup C: stretched-down bounce (paper, now weakened).**
- rsi ≤ 50 AND off high % ≤ −25 AND vs ma20 % < 0.
- Question: is the 10-session median above the universe median?
- Evidence: bundle 5's largest winners fit it. Bundle 6 did not. Four of the largest losers fit it cleanly: −36.8% (rsi 36, off high −28%, vs ma20 −9.5%), −25.5% (rsi 39, off high −45%), −24.0% (rsi 30, off high −33%), and −18.3% (rsi 16, off high −48%). None of the listed winners fit it. Combined with bundle 5, the profile splits the extremes in both directions, so it does not separate winners from losers.
- Confidence: low, and leaning negative.

**Avoid flag for +1 ratings (paper, now weakened).**
- Bundle 6: +1 median −0.6%, 0 −0.7%, −1 −0.4%, −2 +0.3%. No separation. The +1 group was not the lowest.
- History: bundle 3 no separation, bundle 4 yes (+1 −2.4% vs 0 −0.4%), bundle 5 yes (+1 −3.0% vs 0 −0.2%), bundle 6 no.
- Result: 2 of 4 bundles with ratings. This is coin-flip territory. Keep it as paper only. Do not treat it as a rule.

### 1.3 Options (paper only)

**Structures**
- **14-day structures:** excluded. Lost 100% in every bundle they appeared in (bundles 2–6).
- **30-day structures:** excluded from live. Bundle 6 median was strongly negative across the main structures (30d +5% hold10: 16 trades, median −80.7%, average −66.4%; 30d +0% hold10: 3 trades, median −42.9%; 30d +10% hold10: 3 trades, median −85.2%). The bundle 5 positive result (4 trades, median +142%) did not repeat. Pooled over five bundles, the median is negative in every bundle except bundle 5, and that one was n=4.
- **90-day ATM hold10 (wrapper-cost benchmark):** bundle 6 had only 5 trades across three structures (+0% median +8.9%, n=2; +10% median −11.4%, n=1; +20% median −34.1%, n=2). Pooled 90-day ATM results across bundles 2–6 are negative on median. Verdict: the wrapper costs more than the stock typically returns, and the benchmark has no edge on its own.
- **90-day ITM calls (strike ~5% below price, delta 0.7–0.8), hold 10, with +50% / −50% premium exit:** the planned instrument for the first option test. It only applies after a stock setup passes. Not yet tested.

**Option sizing and risk**
- Flat size per trade. Never add after a win.
- Any option can lose 100%. Size so one full loss is small relative to the account.
- Cap total premium at risk per bundle.
- Judge option structures on median, win rate, and the stock-level result beside them. Total P&L is not evidence. Bundle 5's total was carried by 3–4 trades and bundle 6's total came from a broad median loss.

### 1.4 Pass rule (unchanged)
- A stock-level setup goes live only if its 10-session median beats the same-bundle universe median over at least 40 setups, across at least 2 bundles, with the same sign of edge in both.
- Options go live only after a stock-level setup passes and the option structure beats its own stock-level result after cost on the same names.

### 1.5 Ratings
- Ratings are not a filter and not a live avoid flag. Paper-track only.
- The −2 flag remains dropped (bundle 6 −2 median +0.3%, n=8, not informative).

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### 2.1 Results
- **Options:** 33 trades, −$13,586, average −41.2%, median −60.0%, 12% winners. Losses were broad across structures, not one bad trade.
- **Stock universe:** 248 candidates, average +0.1%, median −0.2% over 10 sessions. No edge in the average.
- **Ratings:** no rating group beat the universe median. +1 was −0.6% (n=33), 0 was −0.7% (n=138), −1 was −0.4% (n=59), −2 was +0.3% (n=8).

### 2.2 Stock-level extremes
- **Largest losers (−18% to −37%):** mostly pulled back. Rsi 16–39, off high −28% to −48%, below ma20. Four fit Setup C cleanly. One (−22.9%) was stretched with rsi 50, 5d −28%, which is a different pattern: a sharp drop after a run. Several losers had heavy put crowding (puts 5d avg up to 195×), which is noise.
- **Largest winners (+18% to +56%):** mixed. Some were stretched (rsi 68–73, 20d +35% to +340%, vs ma20 +13% to +33%). Some were quiet (rsi 42–57, 20d −3% to +10%, sometimes well above the universe). Several had news in the last 7 days.
- **What it says:** the extremes do not split cleanly on any single feature. Bundle 4 and 5 suggested stretched losers and pulled-back winners. Bundle 6 partly reversed that. The split is noise until a full-sample test confirms it.

### 2.3 Option structures
- Every 30-day structure I ran had a negative median. The bundle 5 signal did not replicate.
- Ratings-based option trades did not lose more than the others, but they did not win either.
- The best trade this bundle (+115% on a 30d +10% double_or_10, $10–50 name) and the second (+209.8% on a 30d +0% hold10, under-$10) were both single outliers in a losing set.

### 2.4 Price band
- Bundle 6 winners include both under-$10 and $10–50 names, and losers appear in all bands. Price band is still not a stable filter.

### 2.5 Market gate
- Not tested this bundle. Only extremes show market 20d %, and it ranges from −6% to +5% across both winners and losers. Need full-sample split before reading anything.

---

## 3. WHAT I WILL TRY NEXT

1. **Score Setup A on full-sample stock returns.** Log every stock with calls ≥ 2, news tone 7d > 0, news 3d > 0, vs ma50 % > 0. Compare its 10-session median to the same-bundle universe median. Prediction: no beat.
2. **Score Setup B on full-sample stock returns.** Log every stock with rsi ≥ 70, vs ma20 ≥ +10, 5d ≥ +10. Compare its median to the universe. Bundle 6 extremes did not support it. A third failure drops B.
3. **Score Setup C on full-sample stock returns.** Log every stock with rsi ≤ 50, off high ≤ −25, vs ma20 < 0. Count every name in each half of the profile, not only the extremes. Bundle 6 extremes leaned against it. A full-sample test that also fails drops C.
4. **Score the +1 avoid test.** Compare +1 median vs the universe, 0, and −1 in the same bundle. Bundle 6 gave no separation, so the flag is now 2 of 4. One more clean bundle either way decides it.
5. **Market gate split.** Split every setup and the universe by market 20d % > 0 vs ≤ 0. Compare each half to the same-half universe median. Bundle 6 extremes span both market states.
6. **Mean-reversion buckets (inside the universe).** Compare 10-session medians by 5-day bucket (below −10%, −10% to +10%, above +10%) and by off-high bucket (0 to −10, −10 to −25, below −25). Fix the cuts before looking at returns.
7. **Options: no 30-day or 14-day structures.** Stop 30-day paper tests unless they are restricted to a setup that has passed the stock test.
8. **Options: 90-day ITM only, after a stock setup passes.** Keep 90-day ATM as the wrapper-cost benchmark.
9. **Stock vs option gap.** For every 90-day trade, log the stock's 10-session return beside the option return. Bundle 6 had too few 90-day trades for this to be informative.
10. **Price band (90-day, clean test).** Compare $10–50 vs over $50 on the same structure and the same hold.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### 4.1 Evidence and confidence
- **Universe stock drift is flat to slightly negative.** Medians +0.3%, −1.0%, −0.3%, −1.0%, −0.2% across five bundles. Any edge has to come from selection. [High; ~1,250 stock setups]
- **Option medians are negative across bundles 2–6.** Bundle 6 median −60%, 12% winners, 33 trades. Bundle 5 median −21%, 28% winners, 32 trades. Total P&L is not evidence. [High that medians are negative; low that any total means anything]
- **14-day structures lose 100% every time.** Bundles 2–6. [High]
- **30-day structures are negative on median in five of six bundles.** Bundle 5 positive (n=4, median +142%) did not repeat in bundle 6 (n=16, median −80.7% on the main structure). [Medium-high that they are not live]
- **90-day ATM calls are a negative benchmark.** Pooled median negative across bundles 2–6, with bundle 4 the only clearly positive bundle (+3.5%, n=6). [Medium]
- **+1 ratings underperformed in bundles 4 and 5 and not in 3 or 6.** 2 of 4. [Low-medium]
- **Stretched vs pulled-back profiles split the extremes in bundles 4 and 5, and partly reversed in bundle 6.** [Low; extremes only]
- **Price band is not a stable filter.** Winners and losers appear in both cheap and higher-priced names across bundles. [Low]
- **Put crowding does not separate winners from losers.** Extremes on both sides showed large put ratios. [Low-medium]
- **Call-volume spikes did not beat the universe in bundles 2–3.** Not re-tested at setup level since. [Medium]

### 4.2 Dropped ideas
- Rating as a filter or a live avoid flag, including the −2 flag. Dropped.
- 30-day structures in any form as a live candidate, including the double_or_10 variant. Dropped; did not replicate.
- 14-day option structures in any form. Dropped.
- Over-$50 as a positive 90-day filter. Dropped until the clean test.
- "Spike, no news" as a standalone filter. Dropped.
- Total-P&L as evidence of an edge. Dropped. Judge on median and stock-level results.
- Setup C as a bounce signal. Leaning dropped after bundle 6 extremes, pending the full-sample test.
- Setup B as a live avoid flag. Still paper, with bundle 6 not supporting it.
- Setup A as a live candidate. Still paper; the prediction is that it will not pass.

### Agent 3's final notes (not passed on)

# TRADING NOTES (final, after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Status: I do not trade. No option structure and no stock-level signal is validated. Everything runs as paper tracking until new data supports a rule.**

### 1a. Option rules

- **No standing option trade.** Long-option results have been negative on average in all six bundles. Bundle 6 added another loss: 42 trades, -$4,386, average -10.4%, median -59%, 31% winners. Pooled 30-day calls across bundles 1 to 6 are roughly -22% on about 170 trades. Confidence that the long-call wrapper loses on average in this setup: high. Confidence in the cause (premium decay, entering after volatility, buying after extended moves): low, because implied volatility is not logged.
- **14-day expiry: banned.** Ten losses in twelve trades across bundles 2 to 4. No further testing.
- **30-day double-or-10 at a +10% to +20% trigger: dropped.** This was my only paper candidate after bundle 5. Bundle 6 fell on it:
  - +10% trigger: 26 trades, average -28.4%, median -68.4%.
  - +15% trigger: 5 trades, average +12.5%, median -17.1%.
  - +20% trigger: 1 trade, +101.5% (n=1, no weight).
  - Pooled across bundles 4 to 6, the +10% to +20% group is about -9% on roughly 44 trades. Bundle 5's positive result did not hold.
- **30-day hold-10 at +5% or +10% trigger: dropped.** Negative in bundles 4 and 5. Bundle 6: +5% (1 trade, -100%), +10% (2 trades, -26.5%). Still negative.
- **30-day hold-10 at +0% trigger: reference group only.** Bundle 6 had 6 trades, average +46.7% but median -77.4%, so the average came from one or two names. Pooled across bundles 4 to 6 it is about 0% on average with a negative median. This is the least-bad exit I have seen, but it is not a trade.
- **90-day calls: paper only, not trusted.** Bundle 6 had one trade (+8.8%). Pooled across bundles 2 to 6 the median is negative and the average is roughly -20%. Track the median, not the average.
- **Sizing if a live trade is ever placed:** flat size, a small fraction of capital, assume total loss, no adding after wins.

### 1b. Stock-level rules (no validated edge)

- **Ratings are not a trade trigger.** The one rating pattern I have tracked is that +1 names underperform. It held on average in bundles 4, 5, and 6 (about 1.2 to 1.4 points below the universe average each time), and on median in bundles 4 and 5. In bundle 6 the +1 median beat the universe (+0.4% vs -0.2%). Bundle 6's +1 group had 36 names, below my 40-name minimum. Confidence: low to moderate. Use as a question for future data, not as a rule.
- **-1 outperformance did not repeat.** It was +3.9% and +4.1% average in bundles 4 and 5, but +0.2% in bundle 6, in line with the universe. Dropped.
- **-2 has 8 names per bundle at most.** Not testable. Dropped.
- **News screen (news tone 7d > 0 or news 3d > 0):** a paper screen with no claimed edge. Its effect on returns is untested on a full table.
- **Pre-registered hypotheses H1 to H5:** still untested. See section 2.

### 1c. Reasoning

The stock has to move up before any option can pay. Over six bundles I have not found a stock-level column combination that beats the universe median on a full table. Option results have been negative on average, and the one exit rule that looked positive in bundle 5 failed in bundle 6. Until a stock-level signal passes on a full candidate table, I have no basis for a position.

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

**A. Option trades (42 trades, bundle 6).** Total -$4,386, average -10.4%, median -59.0%, 31% winners.

- **30-day (41 trades), average about -10.9%.**
  - Double-or-10 at +10%: 26 trades, -28.4% average, -68.4% median. This is the main failure.
  - Hold-10 at +0%: 6 trades, +46.7% average, -77.4% median.
  - Double-or-10 at +15%: 5 trades, +12.5% average, -17.1% median.
  - Hold-10 at +10%: 2 trades, -26.5%.
  - Double-or-10 at +20%: 1 trade, +101.5%.
  - Hold-10 at +5%: 1 trade, -100%.
- **90-day (1 trade):** +8.8%. Not usable.
- **Read:** the largest group (double-or-10 at +10%, 26 trades) lost heavily, with a median near -68%. The positive averages in the smaller groups rest on 1 to 6 trades. Bundle 6 confirms that the average is driven by a few large winners while most trades lose.

**B. Ratings against the next 10 sessions (bundle 6, 248 candidates).** Universe: average +0.1%, median -0.2%.

| Rating | Names | Average | Median |
|---|---|---|---|
| +1 | 36 | -1.1% | +0.4% |
| 0 | 138 | +0.3% | -0.6% |
| -1 | 66 | +0.2% | -0.3% |
| -2 | 8 | +0.7% | -1.3% |

- **+1 average underperformed** (-1.1% vs +0.1%). Median outperformed. It is the most consistent average pattern so far, but the median reversed in this bundle and the group is under 40 names.
- **-1** matched the universe. Its earlier outperformance did not repeat.
- **-2** (8 names) is too small to read.
- **Conclusion:** ratings still do not give a stable ranking. The +1 average underperformance is the only thing worth carrying forward, and only as a question.

**C. Pre-registered stock-level hypotheses (H1 to H5). Not tested.**

I could not run them. Bundle 6, like bundles 4 and 5, gave me summary statistics and extreme lists, not the full candidate table with every column and 10-session return. I will not infer test results from extremes. Under the rule I set before this bundle, a hypothesis passes only on the full table with at least 40 names per group. None has been tested on a full table in any bundle.

- H1 (chase): RSI > 70 AND vs ma20 > 10. Does the stock underperform the universe median?
- H2 (news): news tone 7d > 0. Does the stock outperform?
- H3 (buildup): calls 5d avg > 2 AND call days 2x+ ≥ 3. Does the stock outperform?
- H4 (quiet after spike): days since spike ≥ 20 AND calls 5d avg < 1. Does the stock underperform?
- H5 (oversold): RSI < 45 AND off high < -25%. Does the stock outperform?

**D. Extremes (pattern only, not evidence).**

- **Losers:** both oversold names (RSI 16 to 30, off high -33% to -48%, several lost 18% to 25%) and overheated names (RSI 52 to 73, one with 20-day return above +300% that still lost 23%). Call buildup and high put activity appeared among losers and winners alike.
- **Winners:** included names with strong 20-day runs (+35% to +55%) and oversold names (RSI 42, 20-day -2.5%, +56%). News was present in several winners, and in several losers too.
- **Read:** the tails are two-sided on RSI, off-high, news, and call buildup. Nothing separates them. H1 and H5 each explain some tail names and fail on others.

**E. Price band.** The three trades in the price-over-$50 band averaged a large positive return, but that is n=3. Both large winners and large losers appeared in every band in every bundle. Not a filter.

**F. Market backdrop.** Universe roughly flat over 10 sessions (average +0.1%, median -0.2%). No market-regime signal.

**G. The new idea I tried.** The only new idea in this bundle was the double-or-10 exit at a +10% to +20% trigger, carried over from bundle 5 as a paper candidate. It failed in bundle 6. Dropped.

## 3. WHAT I WILL TRY NEXT

This was the last of the six bundles, so the next step is a change of data, not another tweak to the current list.

1. **Stop the option wrapper.** No option trade on any candidate until a stock-level hypothesis passes on a full table. The 30-day double-or-10 candidate is dropped, not paused.
2. **Request the full candidate table, once, for any new data.** Every candidate's full column set and 10-session return, unsampled. Without it, H1 to H5 cannot be tested, and I will not treat extremes as evidence.
3. **Set a deadline for H1 to H5.** If a full table is not available for the next data set, retire all five hypotheses. Keeping them open indefinitely without testing them does not count as progress.
4. **Pre-register on the next data set.** Thresholds fixed as written, one test per hypothesis, at least 40 names per group, and report average and median against the universe median. A pass is a candidate for live testing on later data, not a validated edge.
5. **Test the +1 rating question again.** Whether +1 names underperform the universe average, with at least 40 names in the group. If that holds on a full table, it becomes a stock-level question for the next round, still not a trade trigger.
6. **Log implied volatility at entry for any paper option.** This is the largest unanswered question about the wrapper: whether losses come from direction or from premium decay.
7. **Paper-track only if I track options at all.** Record each candidate's 10-session stock return alongside its option result, so direction and premium can be separated. Use the 30-day hold-10 at +0% as the reference group. Track 90-day calls by median.
8. **Keep the news screen as a paper screen** (news tone 7d > 0 or news 3d > 0), recording stock returns and option premium at entry and day 10.

## 4. SUPPORTING EVIDENCE AND IDEAS I HAVE DROPPED

### Evidence I am keeping (with confidence)

- **Long calls lose on average in this setup.** Pooled 30-day about -22% over about 170 trades across six bundles. High confidence in the average, low confidence in the cause.
- **14-day expiry does not work.** Ten losses in twelve trades across bundles 2 to 4. Moderate-to-high confidence.
- **30-day hold-10 at +5% or +10% loses.** Negative in bundles 4 and 5 and still negative in bundle 6 (small n). Moderate confidence.
- **30-day hold-10 at +0% is the least-bad reference.** Pooled near 0% on average with a negative median. Low confidence that it is a real exit, since the average depends on a few names.
- **+1 ratings underperformed on average in bundles 4, 5, and 6** (about 1.2 to 1.4 points below the universe average). Median held in two of three bundles. Low-to-moderate confidence. Stock-level question, not a trade signal.
- **The universe is roughly flat over 10 sessions.** Medians between -1.0% and +0.3% across recent bundles. Moderate confidence, small effect.

### Ideas I am keeping as open questions

- **+1 rating underperformance** (see above). Needs a full-table test with at least 40 names.
- **H1 to H5 and the news screen.** Untested on a full table. Each has a retirement deadline (section 3).

### Ideas I am dropping

- **30-day double-or-10 at +10% to +20%.** Positive in bundles 4 and 5 (about +16% on 12 trades), negative in bundle 6 (-28% on 26 trades at +10%). Pooled across bundles 4 to 6 it is about -9% on roughly 44 trades. Dropped.
- **30-day hold-10 at +5% and +10%.** Negative in bundles 4 to 6.
- **14-day expiry.** Dropped.
- **Exit-rule tuning to rescue the wrapper.** Dropped. Every rule I tested either lost in some bundles or failed the next bundle.
- **"90-day calls fix the wrapper."** One trade in bundle 6. Median negative across bundles. Not trusted.
- **-1 rating outperformance.** Did not repeat in bundle 6. Dropped.
- **Ratings as a trade trigger in either direction.** Ordering flips between bundles.
- **Price band as a filter.** Both large winners and losers appear in every band.
- **Extremes lists as evidence.** RSI, off-high, news, and call buildup each appear in both tails. Used only to suggest hypotheses.
- **"Spike, no news" as a standalone filter.** No clean split.
- **Short-dated call ratio (short above 20).** Appears in both tails. Not usable.
- **H5 as a validated oversold signal.** Bundle 6's extremes were two-sided. Untested on a full table.

### Caveats

- **Six bundles, roughly 200 to 260 candidates each, and no bundle has given me a full candidate table.** The data is not enough to validate any stock-level rule.
- **Option P&L cannot be paired with stock returns** in the data I receive, so I cannot say how much of each option loss came from direction versus premium.
- **Small samples dominate the option groups.** Most double-or-10 and 90-day groups have 1 to 6 trades. Treat any group under 10 trades as anecdote.
- **Averages are driven by a few names.** Bundle 6's hold-10 at +0% average of +46.7% has a median of -77.4%. Read medians alongside averages.
- **Tails are noisy.** Extreme winners and losers are often high-volatility names with thin histories.
- **Any hypothesis first seen in extremes is a suggestion only.** It counts only when tested on a full table with thresholds fixed in advance.

### Agent 4's final notes (not passed on)

# TRADING NOTES: Rolling Playbook (after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Status: still losing on paper options. Bundle 6 was the worst result since bundle 4 (-$6,205, 33% winners, 52 trades). Bundle 5 was -$3,666. Bundle 4 was -$9,580. Everything stays paper only. Nothing here is ready for real size.**

### Working setup (paper, for testing)

1. **Instrument: options as paper trades, with the underlying stock's 10-session return recorded on the same entry day as a shadow baseline.**
   - Confidence that the option wrapper is the main drag: high. Stock median across bundles is near zero (bundle 6: -0.2%). Option median is about -30% (bundle 6: -29.4%).
   - Cause of the wrapper gap: unknown. Confidence in any explanation: low.

2. **Expiry: 90-day is the working default. 30-day and 14-day are paper-only and not promoted.**
   - 90-day, +5% strike, pooled over bundles 4–6: about 26 trades, average about -12%. Median is negative in every bundle (-30%, -6.5%, -13.4%).
   - 90-day, ATM, pooled over bundles 4–6: about 25 trades, average about -31%. Median is negative in every bundle (-36%, -29%, -73.8%).
   - 30-day +5%: bundle 6 gave 18 trades, average -29.0%, median -60.5%. Bundle 5 gave 3 trades, average +22.8%. Pooled, this is a losing cell with a large sample. **Dropped as a rule.**
   - 14-day: bundle 6 gave 1 trade at -100% and 1 at +0.9%. Bundle 5 gave two losers. **Avoid.**
   - Confidence: medium that 90-day beats 14-day and 30-day +5%. Low that 90-day is profitable (it is not, on median).

3. **Strike: 90-day +5% OTM is the working default. Confidence: low-to-medium.**
   - +5% beat ATM on average and on median in each of the three bundles where both were tested on 90-day entries. The average gap is about 19 points on pooled trades.
   - The +5% median is still negative every time. "Less bad" is the honest read, not "works."
   - The 30-day strike result flipped sign: 30-day ATM was +55.5% (n=9) while 30-day +5% was -29.0% (n=18). That is too unstable to use. Treat the strike effect as specific to 90-day until shown otherwise.

4. **Exit: hold 10 sessions, then close.** Double-or-10 is dropped.
   - Confidence: medium. It has been used in every bundle and no alternative has beaten it.

5. **Ratings filter: no active exclusion. The "+1" exclusion is back on the paper-test list.**
   - Bundle 6: +1 averaged -1.6% with a median of -0.3% (n=60). The +0 bucket averaged +0.7% (median +0.2%). The -1 bucket averaged +1.2% (median -0.7%).
   - Across six bundles, +1 has had a negative median in five and below-average returns in four. Bundle 5 was the one reversal.
   - Status: **candidate exclusion, paper test only.** On paper, skip +1 names in bundle 7 and compare results against the non-excluded set. Do not treat as a live rule until it holds on a second fresh bundle.

6. **Sizing:** fixed, small dollars. Assume 100% loss on any option. No adding, no averaging down.

### Ideas that failed this bundle (removed from active use)

- **Calls-building entry** (`calls` ≥ 1.0 AND `call days 2x+` ≥ 2 over the last 5 sessions). The filter is not selective. Nearly every option trade in the bundle's extremes met it, including most of the largest losers and most of the largest winners. A filter that passes almost everything cannot separate winners from losers. **Dropped.**
- **Avoid chasing sharp run-ups** (`20d %` above +15%). In bundle 6 this rule would have excluded several of the best option trades (for example, 20d moves of about +18%, +35%, and +44% that returned +36% to +522%). Bundle 5 had three losers after big run-ups. The evidence is contradictory. **Dropped as a rule. Keep logging `20d %`.**

## 2. WHAT I TESTED IN THIS BUNDLE

### Option results (bundle 6: 52 trades, -$6,205, 33% winners)

| Cell | Trades | Average | Median |
|---|---|---|---|
| 30d, +5%, hold 10 | 18 | -29.0% | -60.5% |
| 90d, +5%, hold 10 | 13 | -13.6% | -13.4% |
| 30d, +0%, hold 10 | 9 | +55.5% | +31.5% |
| 90d, +0%, hold 10 | 4 | -46.5% | -73.8% |
| 30d, +10%, hold 10 | 2 | -57.2% | -57.2% |
| 30d, +15%, hold 10 | 2 | -46.5% | -46.5% |
| 90d, +10%, hold 10 | 2 | +35.3% | +35.3% |
| 14d, +10%, hold 10 | 1 | -100.0% | -100.0% |
| 14d, +0%, hold 10 | 1 | +0.9% | +0.9% |

**Read:**
- The 30-day +5% cell is the largest loser by count (18 trades, median -60%). It is the main reason for the bundle's loss.
- 30-day ATM was the only large positive cell (9 trades, average +55.5%, median +31.5%). Bundle 5 had only 2 ATM 30-day trades, both losers. Nine trades is still too few to promote, and the result rests on a few very large winners.
- 90-day +5% was negative on average and median, but its median (-13.4%) was much better than 90-day ATM's (-73.8%).
- The largest winners were 30-day ATM and 90-day names with strong 20-day momentum. The largest losers were mostly 30-day and 14-day, and many were not extended.
- Price band did not separate winners from losers. Both winners and losers appeared in all three bands.
- News did not separate them either. Winners had news and no news in roughly equal measure.
- Two very large option losses were on names with `days since spike` of 0 to 1 (fresh call activity). Two large winners were on names with `days since spike` of 0 as well. Not a usable separator.
- I do not have implied volatility in this record. The IV test from the prior plan cannot be run from these columns. This remains the top open question.

### Ratings (stock returns over 10 sessions, bundle 6: 248 candidates)

| Rating | Count | Average | Median |
|---|---|---|---|
| +2 | 1 | -6.2% | -6.2% |
| +1 | 60 | -1.6% | -0.3% |
| 0 | 104 | +0.7% | +0.2% |
| -1 | 71 | +1.2% | -0.7% |
| -2 | 2 | -2.1% | -2.1% |

- Whole sample: average +0.1%, median -0.2%. No edge from the ratings as a group.
- +1 was the weakest bucket again. This is what the candidate exclusion was waiting for.
- -1 has a positive average and a negative median, the same pattern as in earlier bundles.

### Stock tails (extreme winners and losers)

- **Winners were mostly in strong 20-day uptrends.** Many had `20d %` between +18% and +337%, `vs ma20 %` positive, and RSI in the 60s and 70s. A few were oversold, but most were not.
- **Losers were mostly in 20-day downtrends.** Many had `20d %` between -12% and -26%, `off high %` between -20% and -48%, and RSI in the 16–39 range.
- This is the opposite of bundle 5's tail read, where oversold names were the winners. Across bundles 4–6, the tail direction on oversold names has flipped at least once, so the tail lists are not a stable signal.
- Caveat: the tails show extremes only. I cannot compute group averages for "oversold" or "extended" from them. The pre-registered oversold test is not resolved.

### Stock-to-option gap

- Stock median over 10 sessions: -0.2%. Option median: -29.4%. The gap is still about 30 points.
- Unchanged from bundles 4 and 5. The cause is still unidentified.

## 3. WHAT I WILL TRY NEXT

Priority order:

1. **Paper test: exclude +1-rated stocks.** Record each +1 name as a skipped entry, and track its 10-session return alongside the non-excluded set. If the +1 bucket is again below the other buckets on median in bundle 7 (fresh stocks), it becomes a rule to test on a second fresh bundle. Confidence in the pattern: low. Confidence in the mechanism: none.

2. **Keep 90-day +5% OTM as the only option paper cell.** Log ATM 90-day as the control. Do not add new option cells. Judge the strike gap at n ≥ 30 per strike, using averages and medians together.

3. **Add implied volatility to every option entry, if the data source provides it.** If IV is not available, record that the test cannot run. The cause of the wrapper gap cannot be identified without it.

4. **Shares shadow on every option entry.** Record the stock's 10-session return from the same entry day, and compare it to the option return. Flag any option trade where the stock is flat (within ±3%) but the option loses more than 20%. These are premium or timing losses, not direction losses.

5. **Stock momentum test (shares only, new).** The bundle 6 tails leaned toward 20-day momentum, while bundle 5 leaned toward oversold. Record `20d %` and `off high %` on every rated stock. Compare the group averages and medians of stocks with `20d %` > +10% against those with `20d %` < -10%, and against the whole sample. Pre-register: a bucket counts only if its median beats the whole-sample median by at least 1 point on at least 60 stocks.

6. **Oversold/extended test (shares only), continued but downgraded.** Oversold: `off high %` ≤ -20 AND `rsi` < 40. Extended: `rsi` > 70 AND `vs ma20 %` > +5. Group averages for both must be recorded in full. Bundle 6 tails leaned against oversold, so this test is now two bundles with mixed direction.

7. **30-day +5% paper: stop.** Do not trade it on paper. Keep logging 30-day ATM only as a control, and do not promote it unless it holds at n ≥ 15 with a positive median.

8. **14-day: no trades.** Two bundles of 14-day results have been poor or noisy. Stop logging them unless a specific reason comes up.

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Held up (with reservations)

- **Option wrapper is the main drag.** Stock medians sit near zero (about -1% to 0%) across bundles, and option medians are negative every time. Confidence high that the wrapper is the problem. Confidence low on the cause.
- **90-day over 14-day.** Medium confidence. 14-day has been poor or noisy in each bundle where it was tested.
- **Hold 10 sessions.** Medium confidence. Simple and used consistently.
- **90-day +5% OTM over 90-day ATM.** Low-to-medium confidence. Better on average and median in three of three bundles, but the median is still negative in all three. Less bad, not profitable.
- **Stock base rate near zero.** Medians within about ±1% in every bundle. Any rule must clear this by more than option costs.

### Failed or dropped

- **Calls-building entry** (`calls` ≥ 1 AND `call days 2x+` ≥ 2). Non-selective. Passed almost every option trade. Dropped.
- **Avoid run-ups above +15% (`20d %`).** Contradicted in bundle 6. Several of the best option trades came from large 20-day runs. Dropped as a rule.
- **30-day +5% as a working cell.** Bundle 5 looked positive on 3 trades. Bundle 6 lost badly on 18 (median -60%). Dropped.
- **14-day expiry.** Poor or noisy in bundles 4–6. Avoid.
- **Avoid +1 as a live rule.** Failed in bundle 5, passed again in bundle 6 (average -1.6%, median -0.3%). Now a paper candidate, not a rule.
- **Oversold names as winners.** Bundle 5 tails favored them. Bundle 6 tails did not. Unresolved.
- **Avoid entries after a 1-day drop of ≤ -5%.** Contradicted in bundle 5. Dropped.
- **Over-$50 price band.** Bundle 3 looked strong. Not replicated in bundles 4–6. Dropped.
- **Under-$10 as a blanket avoid.** Mixed in every bundle. Dropped.
- **Double-or-10 exit.** Dropped. Not enough evidence.
- **Calls ≥ 3 as a sole filter.** No separation in bundle 4. Dropped.
- **Call spike as a standalone entry.** Dropped in bundle 2. Not rescued by later data.
- **News as a separator (winners vs losers).** No separation in bundles 5 or 6.
- **Price band as a separator for options.** No separation in bundles 5 or 6.

### Open questions

- What is the implied volatility at entry, and how much of the 30–40% median option loss does it explain? (Not measurable from the current record.)
- Does the stock-option gap disappear if the same entries are traded in shares? Or is it a property of the wrapper?
- Does 90-day +5% OTM remain less bad than ATM on fresh stocks, at n ≥ 30 per strike?
- Is the +1 weakness a real effect, or an artifact of how the ratings are built? The paper exclusion test in bundle 7 will help answer this.
- Does 20-day momentum predict stock returns in the group averages (not just the tails)? The bundle 6 stock tails favored it. The bundle 5 tails favored the opposite. The group-average test has not yet been run cleanly.


## Generation 1

### Editor's rules, tested on all training months and bundles

- Over50 ATM 30d (when price = >$50: buy the 30-day call 0% above the price, exit hold10): 700 trades, average -1.7% (95% range -11.1% to +9.2%, resampling whole weeks), median -29.4%, 37% winners. Buying every candidate the same way: -10.9%. Beat that in 5 of 6 bundles; first half of the months +4.7%, second half -7.9%.
- Over50 uptrend 90d (when price = >$50 and market 20d % > 0 and vs ma50 % > 0: buy the 90-day call 0% above the price, exit hold10): 63 trades, average -6.6% (95% range -19.3% to +7.7%, resampling whole weeks), median -14.3%, 33% winners. Buying every candidate the same way: -8.4%. Beat that in 3 of 6 bundles; first half of the months -14.7%, second half -1.7%.
- Positive news tone 90d (when news 3d > 0 and news tone 7d > 0: buy the 90-day call 0% above the price, exit hold10): 110 trades, average -3.1% (95% range -13.3% to +6.6%, resampling whole weeks), median -13.2%, 39% winners. Buying every candidate the same way: -8.4%. Beat that in 4 of 6 bundles; first half of the months -4.2%, second half -2.0%.
- Market and stock uptrend 90d (when market 20d % > 0 and vs ma50 % > 0: buy the 90-day call 0% above the price, exit hold10): 184 trades, average -3.2% (95% range -12.7% to +8.2%, resampling whole weeks), median -19.8%, 34% winners. Buying every candidate the same way: -8.4%. Beat that in 4 of 6 bundles; first half of the months -0.6%, second half -4.4%.
- Stack news over50 uptrend 90d (when price = >$50 and news tone 7d > 0 and market 20d % > 0 and vs ma50 % > 0: buy the 90-day call 0% above the price, exit hold10): 26 trades, average -6.0% (95% range -25.5% to +15.3%, resampling whole weeks), median -9.8%, 38% winners. Buying every candidate the same way: -8.4%. Beat that in 2 of 3 bundles; first half of the months -28.4%, second half +3.9%.
- Oversold 90d (when rsi < 35 and vs ma50 % < -10: buy the 90-day call 0% above the price, exit hold10): 48 trades, average -1.5% (95% range -18.7% to +19.8%, resampling whole weeks), median -10.0%, 40% winners. Buying every candidate the same way: -8.4%. Beat that in 2 of 6 bundles; first half of the months -2.3%, second half -1.3%.
- Momentum moderate RSI 90d (when rsi >= 45 and rsi <= 75 and 20d % >= 10: buy the 90-day call 0% above the price, exit hold10): 118 trades, average -11.0% (95% range -22.4% to +5.1%, resampling whole weeks), median -27.7%, 29% winners. Buying every candidate the same way: -8.4%. Beat that in 2 of 6 bundles; first half of the months +2.0%, second half -20.3%.
- Call spike above ma20 90d (when calls > 3 and vs ma20 % > 0 and price = >$50: buy the 90-day call 0% above the price, exit hold10): 47 trades, average -14.8% (95% range -30.6% to +1.6%, resampling whole weeks), median -20.2%, 26% winners. Buying every candidate the same way: -8.4%. Beat that in 2 of 6 bundles; first half of the months -25.9%, second half -7.8%.

### The same rules on the blind scoring months (never shown to agents)

- Over50 ATM 30d (when price = >$50: buy the 30-day call 0% above the price, exit hold10): 362 trades, average -19.0% (95% range -32.5% to -5.1%, resampling whole weeks), median -39.9%, 30% winners. Buying every candidate the same way: -14.7%. Beat that in 1 of 6 bundles; first half of the months -12.9%, second half -24.7%.
- Over50 uptrend 90d (when price = >$50 and market 20d % > 0 and vs ma50 % > 0: buy the 90-day call 0% above the price, exit hold10): 57 trades, average -11.3% (95% range -20.5% to -0.2%, resampling whole weeks), median -14.4%, 30% winners. Buying every candidate the same way: -7.2%. Beat that in 2 of 6 bundles; first half of the months -17.3%, second half -7.2%.
- Positive news tone 90d (when news 3d > 0 and news tone 7d > 0: buy the 90-day call 0% above the price, exit hold10): 85 trades, average -7.4% (95% range -18.0% to +3.1%, resampling whole weeks), median -16.1%, 31% winners. Buying every candidate the same way: -7.2%. Beat that in 4 of 6 bundles; first half of the months -8.1%, second half -6.7%.
- Market and stock uptrend 90d (when market 20d % > 0 and vs ma50 % > 0: buy the 90-day call 0% above the price, exit hold10): 174 trades, average -7.1% (95% range -15.2% to +2.5%, resampling whole weeks), median -21.7%, 31% winners. Buying every candidate the same way: -7.2%. Beat that in 4 of 6 bundles; first half of the months -8.7%, second half -5.3%.
- Stack news over50 uptrend 90d (when price = >$50 and news tone 7d > 0 and market 20d % > 0 and vs ma50 % > 0: buy the 90-day call 0% above the price, exit hold10): 30 trades, average -13.5% (95% range -28.9% to -0.2%, resampling whole weeks), median -14.1%, 23% winners. Buying every candidate the same way: -7.2%. Beat that in 2 of 4 bundles; first half of the months -29.9%, second half -3.9%.
- Oversold 90d (when rsi < 35 and vs ma50 % < -10: buy the 90-day call 0% above the price, exit hold10): 22 trades, average -3.3% (95% range -23.3% to +14.7%, resampling whole weeks), median -11.8%, 46% winners. Buying every candidate the same way: -7.2%. Beat that in 4 of 5 bundles; first half of the months -25.7%, second half +12.2%.
- Momentum moderate RSI 90d (when rsi >= 45 and rsi <= 75 and 20d % >= 10: buy the 90-day call 0% above the price, exit hold10): 80 trades, average -20.2% (95% range -28.0% to -13.6%, resampling whole weeks), median -29.1%, 22% winners. Buying every candidate the same way: -7.2%. Beat that in 1 of 6 bundles; first half of the months -16.5%, second half -24.7%.
- Call spike above ma20 90d (when calls > 3 and vs ma20 % > 0 and price = >$50: buy the 90-day call 0% above the price, exit hold10): 35 trades, average -14.0% (95% range -24.9% to -0.9%, resampling whole weeks), median -16.0%, 29% winners. Buying every candidate the same way: -7.2%. Beat that in 0 of 5 bundles; first half of the months -17.3%, second half -10.5%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

(Editor's synthesis of four independent traders over six bundles, checked against the code-tested scorebook.)

## 0. Bottom line

- **There is no proven edge.** The scorebook shows no rule with a positive average whose 95% range (resampling whole weeks) excludes zero. Every rule has a negative median, mostly between -20% and -50%, and a win rate of 24% to 40%.
- **All four traders agree:**
  - Buying calls on call-volume spikes loses money.
  - The median option trade loses 30% to 100% of its premium in 10 sessions.
  - Averages are propped up by a few huge winners, so medians are the number to trust.
  - Ratings (+2 to -2) carry no stable stock-level signal.
- **The practical goal is to lose less, then find something that actually wins.** The benchmark is "buy every candidate the same way", which averages **-10.9%** for a 30-day at-the-money call held 10 sessions, **-8.4%** for the 90-day version, and **-12.0%** for 30-day double-or-10.
- **Some filters beat that benchmark repeatedly.** They reduce the loss to roughly -4% to 0%, but none turns it into a profit.
- **Judge every idea against the same-expiry, same-exit benchmark.** Raw P/L misleads because the benchmark itself is negative. Use medians and the bundle-by-bundle count.

## 1. STRATEGY: the setups worth trading (small size, or paper)

These are ranked by scorebook evidence. All use a call bought at the money (0% above price) and held 10 sessions. Treat them as "least-bad, worth refining", not as validated edges. Several flip sign between the first and second half of the sample, which suggests a market-regime dependence.

### 1A. Over-$50 stocks (the most robust finding)
- **Rule:** price band over $50, buy the 30-day at-the-money call, hold 10 sessions.
- **Scorebook:** 700 trades, average **-1.7%** (95% range -11.1% to +9.2%), median -29.4%, 37% winners. It beat the benchmark in **5 of 6 bundles**. First half of the months +4.7%, second half -7.9%.
- **Who saw it:**
  - Two traders (2 and 4) noticed over-$50 winners among the extremes, though one saw the opposite in an earlier bundle.
  - The full-sample test confirms it, which is why extremes lists should not be trusted but full tests should.
- **The 90-day, call-spike version is worse.** Over $50 with calls ≥ 3, 90-day: 73 trades, average -12.3%, median -19.9%, beat the benchmark in only 2 of 6 bundles. The edge appears to come from over-$50 names generally, not from the spike.
- **Likely reason (untested):** higher-priced, larger names have less hyped, cheaper option premium and fewer total-loss outcomes. Under-$10 names produced most of the -100% results.

### 1B. Positive news tone
- **Rule:** news 3d > 0 and news tone 7d > 0, 30-day at-the-money call, hold 10.
- **Scorebook:** 432 trades, average **-0.1%** (95% range -11.6% to +11.2%), median -35.0%, 34% winners. It beat the benchmark in **5 of 6 bundles**. First half +8.6%, second half -10.8%.
- **Caution:** this is the best average in the book, but the regime split is large. Only one trader found it, and others dropped "news" as a filter based on extremes lists. Use it as a stacking candidate, not alone.

### 1C. Market and stock in an uptrend, 90-day expiry
- **Rule:** market 20d % > 0 and the stock's vs ma50 % > 0, 90-day at-the-money call, hold 10.
- **Scorebook:** 184 trades, average -3.2% (95% range -12.7% to +8.2%), median **-19.8%**, 34% winners. Benchmark for 90-day is -8.4%. It beat it in 4 of 6 bundles. First half -0.6%, second half -4.4%.
- **Why it matters:** this is the most stable setup across the halves (-0.6% and -4.4%), and the 90-day median is far less negative than any 30-day cell.

### 1D. Call volume above 3x while the stock is above its 20-day average
- **Rule:** calls > 3 and vs ma20 % > 0, 30-day at-the-money call, hold 10.
- **Scorebook:** 565 trades, average -4.1% (95% range -16.4% to +8.3%), median -39.0%, 32% winners. It beat the benchmark in 4 of 6 bundles. First half -2.1%, second half -6.2%.
- **Note:** this is the only call-spike variant that beats the benchmark. Spikes on stocks above their average are tolerable. Spikes on falling stocks are not (see section 2).

### 1E. Spike with no news and a rising stock
- **Rule:** spike, no news > 0 (calls 3x+ with no news in the prior 3 days) and 5d % > 5, 30-day at-the-money call, hold 10.
- **Scorebook:** 208 trades, average -7.0%, median -34.0%, 32% winners. It beat the benchmark in 5 of 6 bundles, with the first half -10.6% and the second half -3.5%.
- **Weak:** the average is only a few points better than the benchmark, and the 95% range was -22.9% to +8.4%. Traders found "spike, no news" useless on its own. The 5d % > 5 condition seems to be doing the work.

### 1F. Momentum with moderate RSI
- **Rule:** RSI 45 to 75 and 20d % ≥ 10, 30-day at-the-money call, hold 10.
- **Scorebook:** 382 trades, average **-1.2%** (95% range -18.9% to +18.4%), median -44.2%, 28% winners. It beat the benchmark in 3 of 6 bundles. First half +4.0%, second half -6.4%.
- **Read:** the average is near zero, but the median is poor, so the result depends on tail winners. It was proposed by only one trader, from an extremes list.

### 1G. Overbought spike chase
- **Rule:** RSI > 65, 5d % > 10 and 20d % > 20, 30-day at-the-money call, hold 10.
- **Scorebook:** 146 trades, average -6.5% (95% range -26.8% to +10.9%), median -49.3%, 32% winners. It beat the benchmark in 4 of 6 bundles. First half -8.5%, second half -4.3%.
- **Read:** this was proposed as a "do not chase" pattern, but the code shows it does slightly better than the benchmark. Chasing strength is not worse than average. Momentum and strength are mildly positive features, and weakness is negative (see section 2).

### 1H. Oversold names on the 90-day expiry (small sample, interesting median)
- **Rule:** RSI < 35 and vs ma50 % < -10, 90-day at-the-money call, hold 10.
- **Scorebook:** 48 trades, average -1.5% (95% range -18.7% to +19.8%), median **-10.0%** (the best median in the book), 40% winners. It beat the benchmark in 2 of 6 bundles. First half -2.3%, second half -1.3%.
- **Read:** the stable halves and the 40% win rate are encouraging, but n = 48 and only 2 of 6 bundles beat the benchmark. Longer expiries seem to cut the total-loss outcomes. This needs more testing.

### Sizing and execution rules (all traders agree)
- Flat, small size, and no adding after wins. Assume any single option can go to -100%.
- Use at-the-money strikes only. Do not buy 5% or more out of the money.
- Prefer 90-day over 30-day. The benchmark loss is smaller (-8.4% vs -10.9%), and the medians are less negative in 1C and 1H.
- Do not use 14-day expiries.

## 2. AVOID

### Rules the code shows as clearly worse than the benchmark
- **Low-volatility stocks after a 20-day drop** (20d % < -10 and vol20 % < 4), 30-day at-the-money call, hold 10: 196 trades, average **-18.0%** (95% range -33.5% to -1.1%, significantly negative), median -43.7%. It beat the benchmark in 2 of 6 bundles. The second half was -34.3%. Do not buy dips in quiet stocks with calls.
- **Oversold with high volatility and double-or-10** (vol20 % ≥ 4 and RSI < 40, 30-day, double-or-10 exit): 218 trades, average **-18.7%** (95% range -30.9% to -7.0%), median -46.6%. The benchmark for that exit is -12.0%, and it beat it in 2 of 6 bundles.
- **Large down day with a call spike** (1d % ≤ -5 and calls ≥ 3), 30-day, hold 10: 95 trades, average **-23.2%** (95% range -42.2% to +2.3%), median -48.6%. It beat the benchmark in only 1 of 6 bundles. This is the worst setup in the book. Call buying into a falling stock loses.
- **Calls ≥ 3 with price $10 to $50, 90-day:** 103 trades, average **-21.9%** (95% range -31.1% to -12.2%, significantly negative), median -30.5%. It beat the benchmark in 1 of 6 bundles. Compare this with the over-$50 band, which is much better.
- **Call-days surge** (call days 2x+ ≥ 4 and calls 5d avg > 2), 30-day: 256 trades, average -15.0%, median -47.9%, beat the benchmark in 2 of 6 bundles. Sustained call building is a mild negative, not a signal.
- **Oversold deep drawdown** (RSI < 35, off high % < -25 and 20d % < -15), 30-day: 160 trades, average -14.6%, median -50.8%, beat the benchmark in 2 of 6 bundles. Do not pool it with 1H, where the 90-day expiry and the ma50 condition make the difference.

### Rules that look like nothing (no edge either way)
- **Deep oversold rebound** (RSI ≤ 25, vs ma20 ≤ -20 and off high ≤ -35): 42 trades, average -8.8% (95% range -55.5% to +42.2%). First half -72.8%, second half +13.8%. This is pure noise.
- **Extended names** (RSI ≥ 75 and vs ma20 ≥ +20): 96 trades, average -8.2%, 2 of 6 bundles. The "extended names fade" idea is unsupported. Strong names are not worse than average.
- **Sustained call building** (calls 5d avg ≥ 2 and call days 2x+ ≥ 3): 573 trades, average -8.9%, 3 of 6 bundles. This is roughly the benchmark.
- **Put crowding** (puts 5d avg ≥ 3): 727 trades, average -9.2%, 4 of 6 bundles. Avoiding these names does not help, because they do slightly better than the benchmark. The first half was +2.3% and the second half -22.1%, so it is regime-dependent. It is not a bearish signal.

### Things all traders agree to stop doing
- Option strikes 5% or more out of the money.
- 14-day expiries, and a fixed 10-session hold on short-dated calls.
- Under-$10 underlyings.
- Using ratings, price band as a standalone separator, "spike, no news", market 5d, short-call ratio or news count as filters from extremes lists.
- Reading the extremes lists (best and worst names) as evidence. They are dominated by high-volatility names on both sides.
- The calls-spike-as-entry idea in general. Call spikes mean expensive premium.

### Exits
- The code could not tell hold-10, double-or-10 and a -50% stop apart. One trader's three-way exit tests came back identical in the scorebook.
- The only informative comparison is that the double-or-10 benchmark (-12.0%) is slightly worse than hold-10 (-10.9%). No exit has been shown to help.
- Exits remain an open question (section 4).

## 3. NEW IDEAS TO TEST

Idea 1 is partly code-confirmed and the rest are untested.

1. **Stack the confirmed "less bad" features** (partly confirmed; stacking untested). Try over $50 + positive news tone + market 20d > 0 + vs ma50 > 0, with a 90-day at-the-money call. Each feature separately beat the benchmark in 4 to 5 of 6 bundles. Pre-register thresholds and require n ≥ 40. This is the highest-priority test.
   - Concern: stacking shrinks n, and all single rules lost money in the second half. Test stacks in the first half and second half separately.
2. **Substitute stock for options** (untested). Several traders found stock-level medians near zero (universe median -0.4%) while option medians sit near -40%. The option wrapper costs most of the loss. For any setup in section 1, compute the same setup's 10-session stock return (hit rate versus the universe median). If the stock version has a positive median edge, trade it as a deep in-the-money call (strike about 5% to 10% below price, 90 days, delta near 0.8) or as shares. Agents 2 and 4 both proposed deep in-the-money calls to cut decay. A bull call spread is a cheaper-premium variant.
3. **Volatility-aware premium filter** (untested, supported only indirectly). The high-volatility oversold cell lost heavily (-18.7%), and the quiet-stock dip cell also lost, so volatility alone does not decide it. Test whether low vol20 (< 2%) plus over $50 gives cheaper, less decaying premium. Log the implied volatility at entry for every option trade (not yet available). Premium decay and IV collapse are the most likely explanation for 70% to 100% losses on small stock moves.
4. **Fade the call spike by selling premium** (untested, high risk). Buying calls on spikes loses 15% to 23% in several cells, which suggests spike-day premium is overpriced. Test defined-risk structures only (e.g. a bear call spread or covered call on stocks already held), paper-tracked, with a tail-loss review. A spike on a falling stock was the worst case, so the large-down-day spike is the first candidate to fade.
5. **Regime gate** (untested). Almost every rule in the book earned its better average in the first half of the months and its worse in the second. Test whether market 20d > 0, or a similar regime gate, explains the split. If so, the real edge might be "trade only in uptrends", with the stock-level filters secondary.
6. **Extend the 90-day oversold cell** (weakly supported). Try RSI < 30 or vs ma50 < -15, or add over $50, and see if the median stays near -10%. Also test a 120-day expiry.
7. **Time-stop and profit-target grid on the section 1 setups** (untested). Test sell-at-+50%, sell-at-day-5 and a -50% stop using the premium path, with exits scored on common entries. Agent 3's 30-day +10% target (5 trades, median -23.8%) is a single sample.

## 4. OPEN QUESTIONS

- **Does any setup have a positive median?** None does so far. The least negative are 1H (-10%), 1C (-19.8%) and 1A (-29.4%). Is a positive median reachable with calls at all, or only with stock or ITM substitutes?
- **Is the price-band effect real or a proxy?** Over $50 beat the benchmark in 5 of 6 bundles, but three traders reached opposite impressions from extremes lists. Is it size, liquidity, lower implied volatility or something else?
- **Which half of the sample is the regime?** Why did nearly all rules do better in the first half? Is it the market trend, volatility, or something about the earlier weeks?
- **Do the three exits differ?** The scorebook could not tell them apart. Is there a way to score them on common entries with premium paths?
- **Direction versus decay:** what fraction of option losses comes from the stock not moving versus premium collapse? Pair every option trade with its own 10-session stock return and entry implied volatility.
- **Rating 0:** it beat the universe median by about 0.5 points in bundles 5 and 6 for three traders, but one disagreed. Likely noise, but cheap to track.
- **Rating +1:** the traders disagree. It was best in bundle 3, below median in bundles 4 and 5, and above in bundle 6 for some counts and below for others. Treat it as no signal.
- **Reversal versus momentum:** dip-buying lost (-18% in quiet stocks), and strong names did slightly better than average (-1.2% and -6.5% vs -10.9%). Does this "momentum beats reversal" read hold in a full-universe bucket test by 20d %, RSI and vol20?

### Agent 1's final notes (not passed on)

# Trading Notes: Stock-Level Signals and the Option Book

## 1. My Current Strategy

**Status: no option trades. No validated buy or sell signal. Stock-level tracking only.**

### Rules

**R1. No new option positions.** The option book reopens only when every re-entry condition in Section 3, item 4 is met. Across six bundles (about 222 option trades), losses total roughly -$37,000. The one cell that looked positive on median in bundle 5 (30-day, ATM, double-or-10 exit) returned a median of -31.5% in bundle 6, so it has not held.

**R2. No rating is a trading signal.** Ratings +2 to -2 describe the system's view. They have not produced a stable edge relative to the same bundle's universe median.
- **Rated +1:** Below the universe median in bundles 4 and 5, above it in bundle 6 (+0.6 points), and the best bucket in bundle 3. Three bundles of mixed results. The "weak negative" label I held after bundle 5 did not replicate. Treat as no edge.
- **Rated 0:** Above the universe median by about +0.5 points in both bundle 5 and bundle 6 (n=114 and n=105). This is the most consistent bucket across recent bundles, but the margin is small and "neutral" ratings are not something I would trade on. Watch only.
- **Rated -1:** Above the median in bundle 4 (about +0.7), at the median in bundle 5, and slightly below it in bundle 6 (about -0.6). No edge. Dropped.
- **Rated -2:** Too few observations to read (n=6 in bundle 5, n=2 in bundle 6). Bundle 6's two were both sharply negative (-16.9% median), bundle 5's six were flat (+0.1% median). Not a rule.

**R3. Judge every stock-level result against the same bundle's universe median, not zero.** Universe medians by bundle: bundle 1 0.0%, bundle 2 -0.6%, bundle 3 -0.9%, bundle 4 -0.6%, bundle 5 -1.2%, bundle 6 -0.4%. The universe is typically slightly negative, so a raw "down 1%" tells me little.

**R4. Exit: never a fixed 10-session hold for options.** The 10-session hold had a negative median in every bundle where it was tested. The double-or-10 exit at 30 days is the only exit I have not yet ruled out, and it now has a negative median in the most recent (largest) test. Any future option test must compare the option's P/L against the stock-only return on the same signal, with a time stop.

**R5. Strike: ATM (0%) only.** Strikes 5% or more out of the money produced most of the -100% outcomes in every bundle. Keep this rule.

**R6. Sizing: flat and small.** No adding after wins. Assume any single option can go to -100%.

### Reasoning

Option losses are much larger than the underlying moves that preceded them. In bundle 6, the worst outcomes (-100%, -97%, -84%, -84%, -74%, -73%) came on stock moves that the logged data does not explain well, and several losers saw the stock move little. Premium decay and implied-volatility collapse remain the most likely explanation, but I have no implied-volatility field to confirm this. Stock-level results are roughly flat to slightly negative, so even a correct directional call has to clear a high bar before it pays for option premium.

### Confidence

- **High:** Buying calls on call-volume spikes has negative expectancy in this instrument and timing. Six bundles, about 222 trades, and no cell with a positive median that held in a second bundle.
- **Moderate:** The fixed 10-session hold is the wrong exit for options.
- **Low:** Any rating-based stock signal (ratings have been inconsistent).
- **Unknown:** Any stock-level feature bucket. I have not yet been able to run the planned full-universe bucket tests (see Section 3).

## 2. What I Tested in Bundle 6 and How It Went

### Option book (bundle 6, 32 trades, 38% winners, total -$3,307)

| Measure | Value |
|---|---|
| Trades | 32 |
| Average return | -10.3% |
| Median return | -31.5% |
| Winners | 38% |
| Cell | 30-day, ATM, double-or-10 exit |

The average looks better than the median because a handful of large winners (+82% to +236%) pulled it up. The median is the more reliable read, and it was clearly negative. Results were bimodal: many trades lost 70% to 100%, and a minority made large gains. A cell with that shape needs far more trades than I have before its average means anything.

Cumulative 30-day double-or-10 results: bundle 4 median -85.1% (n=5), bundle 5 median +5.1% (n=5), bundle 6 median -31.5% (n=32). It did not hold.

### Stock-level buckets (bundle 6, 250 candidates)

| Rating | n | Average | Median | vs. universe median (-0.4%) |
|---|---|---|---|---|
| +1 | 44 | +2.3% | +0.2% | about +0.6 points |
| 0 | 105 | +0.2% | +0.1% | about +0.5 points |
| -1 | 99 | +0.4% | -1.0% | about -0.6 points |
| -2 | 2 | -16.9% | -16.9% | too small |

Universe: average +0.5%, median -0.4%.

Two things stand out. First, the rated +1 bucket had the best average in the bundle (+2.3%), but its median was only slightly above the universe, so the average is being carried by a few large moves. Second, the -1 bucket underperformed the median slightly, which is consistent with the bucket having no edge.

### Planned bucket tests (Section 3, items 1c to 1h)

**Not run.** I only have bucket averages by rating and a short list of extremes. I do not have the full candidate list with the feature columns, so I cannot compute medians or hit rates for RSI, vs ma20, off-high, 1-day move, call-spike, or put-crowding buckets. I am carrying these tests forward and requesting the full table (Section 3, item 6).

### Extremes view (bundle 6, hypothesis only)

The extremes list is biased, so it cannot establish base rates. With that caveat:

- **Biggest losers (-17% to -37%):** RSI spans from 16 to 73, so oversold and overbought names both fell hard. Several had strong 20-day gains (+10% to +337%), and several had 20-day declines (-12% to -26%). Price band and news did not separate them.
- **Biggest winners (+19% to +56%):** Most had RSI between 42 and 73 and a positive 20-day return, often large (+21% to +35%). This is the first time the RSI-and-momentum pattern shows up on the winning side with a consistent direction. It is still not separated from the losers, which had similar RSI and momentum values.
- **Both sides:** Large one-day moves appeared on both sides (-13% to +11%). Put crowding (puts 5-day average up to 68) appeared on both sides.

Read: the extremes give a weak hint that momentum with moderately high RSI may be associated with big upside moves, but the same features appear among the losers. This is a hypothesis generator, not evidence.

## 3. What I Will Try Next

1. **Full-universe bucket test (stocks, no options).** Requires the full candidate table for bundle 6 (see item 6). Use the fixed thresholds below. Report median 10-session return vs. the universe median, hit rate (share above the universe median), and n. Any bucket with n < 20 is noise.
   - a. **Rated +1 check.** Confirm whether it sits above or below the universe median. Bundle 6 says above by about 0.6 points. If bundle 7 is also above, retire the "weak negative" idea. If not, the rating has no stable direction.
   - b. **Rated -1 check.** Bundle 6 says slightly below the median. An edge would need to beat the universe median by more than 0.5 points in bundle 7 to be worth pooling.
   - c. **Oversold:** RSI ≤ 25 and vs ma20 ≤ -20%.
   - d. **Extended:** RSI ≥ 75 and vs ma20 ≥ +20%.
   - e. **Deep off-high:** off high ≤ -35%.
   - f. **Large down day:** 1-day % ≤ -5%, split by whether a call spike (calls 3x+) occurred that day.
   - g. **Sustained call building:** calls 5-day average ≥ 2 and call days 2x+ ≥ 3.
   - h. **Put crowding:** puts 5-day average ≥ 3.
   - i. **New hypothesis from bundle 6 extremes:** RSI 45 to 75 and 20-day change ≥ +10%. Test only on full data. This is the most likely candidate to replicate, but I have no base rate yet.

2. **Pooled test, fixed thresholds.** The thresholds above are fixed. A rule counts only if it holds in bundle 7 with those thresholds. Do not tune thresholds on bundle 6.

3. **Option test, only when item 4 is satisfied.** Use 30-day ATM options with a profit target, a time stop, and fixed small size. Do not use the fixed 10-session hold. Log entry implied volatility where available. Compare option P/L against the stock-only return on the same signal.

4. **Re-entry criteria for options (all required):**
   - A stock-level bucket beats the universe median by at least 2 points with n ≥ 40, in two consecutive bundles. Nothing currently qualifies. Rated +1 beat the median by about 0.6 points in bundle 6 and has not beaten it by 2 points in any bundle.
   - The first option test is ATM, 30 days or longer, with a profit-target exit and time stop, at fixed small size.
   - Option P/L is compared to the same bucket's stock-only return, so the premium cost is visible.

5. **Sample targets.** At least 40 to 50 candidates per hypothesis before trusting a rule. Use medians, not averages. Anything under 20 is noise.

6. **Data request (priority).** I need the full candidate list for each bundle with all feature columns, not only the extremes and the rating summary. Without it, Section 3 items 1c to 1i cannot be tested. I also need implied volatility logged for every option trade.

## 4. Supporting Evidence and Dropped Ideas

### Supporting evidence

- **Options, cumulative (bundles 1 to 6):** about 222 trades, roughly 30% winners, total about -$37,000. Negative medians in nearly every main cell. The 30-day double-or-10 cell was positive in bundle 5 only, and negative in bundles 4 and 6.
- **Universe stock returns:** 10-session averages by bundle are about +0.4%, +1.7%, -0.5%, -1.3%, -1.3%, +0.5%. Medians are 0.0%, -0.6%, -0.9%, -0.6%, -1.2%, -0.4%. The universe is slightly negative on median but has no consistent direction across bundles.
- **Ratings:** no consistent monotonic relation. Rated +1 was best in bundle 3, below median in bundles 4 and 5, and above in bundle 6. Rated 0 was above median in bundles 5 and 6. Rated -1 was above in bundle 4, near the median in bundle 5, and slightly below in bundle 6.
- **Strikes:** OTM cells produced most -100% results across bundles.
- **Sample size:** most cells have fewer than 15 trades. Averages are distorted by a few large winners (+111%, +181%, +236%, +476%). Medians are more reliable, and most have been negative.

### Dropped

- **Rated +1 as a weak negative.** Did not hold in bundle 6. Dropped.
- **Rated -1 as a bullish or bearish edge.** No edge in bundles 5 or 6. Dropped.
- **30-day double-or-10 as a validated exit.** Median -31.5% in bundle 6. Dropped as a candidate for re-entry until a new test shows otherwise.
- **Bundle 1 "best cell" (14-day, ATM, 10-session hold).** Failed in bundles 2 through 5.
- **14-day double-or-10 exit.** Too small to judge, no support.
- **Fixed 10-session hold for options.** Negative medians in every bundle where tested. Replaced by R4.
- **Strikes 5% or more out of the money.** Dropped.
- **Call-building as an option entry rule.** Kept only as a stock-level test (Section 3, item 1g).
- **"Spike, no news" as a filter.** Appears on both winners and losers in every bundle. Dropped.
- **Price band as a rule.** No separation in any bundle. Dropped.

### Kept but unproven

- **Oversold rebound** (RSI ≤ 25, deep below the 20-day average, deep below the 60-day high). Bundle 5's largest winner fits, but oversold names also appear among the losers. Needs the full universe test.
- **Extended-name fade** (vs ma20 ≥ +20%, RSI ≥ 75). Bundle 5 extremes split both ways, and bundle 6 winners had RSI up to 73 and momentum well above zero. Needs the full universe test.
- **Momentum with moderately high RSI** (RSI 45 to 75 and 20-day ≥ +10%). New in bundle 6. Plausible from the winners list, not separated from losers. Needs the full universe test.
- **Large one-day move signal.** Appears on both sides. Needs the full universe test.
- **Put crowding as a bearish stock signal** (puts 5-day average ≥ 3). Appears on both sides in bundles 5 and 6. Needs the full universe test.
- **Implied-volatility explanation for option losses.** Still the most plausible explanation for losses of 70% to 100% on small stock moves. No data to confirm.

### Agent 2's final notes (not passed on)

# TRADING NOTES (final, after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Bottom line: I have no validated edge. No real-money option trades until a pre-registered test passes. Everything below is either a rule that has been killed or a hypothesis that is still under test.**

### 1a. Option structure: 30-day calls, strike about 5% above price, exit at 2x premium or 10 sessions
- **Status: OFF (kill rule confirmed a second time).**
- Bundle 6: the 30d +0% hold10 cell (15 trades) averaged -72% with a median of -100%. The 30d +5% cell has now lost money in every bundle where it had a meaningful sample.
- Pooled across six bundles, this cell is roughly 180 to 200 trades with a negative average and a negative median in every bundle with a meaningful sample. The positive-average bundles came from a few very large winners.
- Cumulative P&L across six bundles is about -$48k (bundles 1 to 4 about -$18.7k, bundle 5 -$14.3k, bundle 6 -$14.7k).
- **Do not reopen this cell** unless a new pre-registered test (section 3) produces a signal that passes.

### 1b. Other option cells: OFF
- **14-day and 90-day calls:** keep off. Bundle 6 added a 90d +10% hold10 winner (+136%), but the 90d cell was negative in bundle 1, bundle 5, and bundle 6 on the median. One winner is not an edge.
- **Strikes at 0%, +10%, +15%, +20%:** every test lost on the median. Keep off.
- **Exits at hold10 with 14-day expiries:** bundle 6 median was -100% in every 14d cell with a meaningful sample. A 10-session hold on a short-dated call is nearly always a total loss on the median. Keep off.
- **Observation to explain, not trade:** the median trade in bundle 6 lost 100% of its premium within 10 sessions. That is far more than direction alone would usually cost. Either the strikes are too far out, the expiry is too short for a 10-session hold, or the exit is capturing the worst moment. Step 4 (deep-ITM test) is designed to check this.

### 1c. Ratings: logged, not used for selection or sizing
- **Bundle 6, 10-session stock averages:** +1 -2.7% (median -1.3%, n=53); +0 +0.7% (median -0.6%, n=102); -1 +3.0% (median +1.0%, n=76); -2 -2.6% (median -2.9%, n=9).
- **Bundle 5, same measure:** +1 -1.4% (median -1.9%); +0 -1.2% (median -0.6%); -1 -2.6% (median -1.1%); -2 +5.6% (median +1.2%).
- **Pattern:** the +1 cohort has had the worst median in bundles 5 and 6. The -1 cohort has been negative in bundle 5 and positive in bundle 6. The -2 cohort flips sign between bundles.
- **Rule:** ratings stay out of selection and sizing. The only thing I will track is whether the +1 cohort keeps underperforming. If it does in bundle 7, I will consider a "do not buy +1 names" filter, which is a different and simpler claim than using ratings to pick winners.

### 1d. Universe and drift
- **Bundle 6 universe:** all 250 candidates averaged +0.5% over 10 sessions (median -0.4%). Bundle 5 averaged -1.3%. The universe is roughly a coin flip in direction, with a slight negative median.
- **Option headwind:** a long call needs a move of about 5% or more plus time decay to pay. The median candidate in both recent bundles did not deliver that within 10 sessions. So the option structure starts with a headwind even before direction is considered.

### 1e. The 20-day reversal hypothesis is weakened
- **Bundle 5 extremes** suggested short-term reversal: 11 of the 12 worst names had a positive 20-day return.
- **Bundle 6 extremes do not confirm it.** Of the 12 worst names (returns of -18% to -37%), 7 had a positive 20-day return and 5 had a negative one. Of the 12 best names (returns of +18% to +56%), 11 had a positive 20-day return, and one had a -2.5% return.
- **What both tails share in bundle 6: high volatility.** The vol20 values in both tails are mostly above 4% (many above 6%, some above 10%). Several top names had 20-day gains of +100% to +337%. The extremes are dominated by dispersion, not by a clean direction signal.
- **Revised reading:** the extremes lists are selected on the outcome and are dominated by high-volatility names. They cannot establish the base rate for reversal or momentum. The base rate has to come from the full candidate distribution.
- **Status: reversal is unconfirmed. Momentum is also unconfirmed.** Neither has held across two or more bundles.

### 1f. Momentum gate: dead
- The pre-registered momentum filter (20-day return above 0, price above the 20-day average, RSI 55 to 80) was tested in bundle 5 and failed. It worked only in bundle 4. Drop it as a gate. Do not revisit it without a new, distinct hypothesis.

---

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

**Result:** -$14,712 on 36 trades, average -40.9%, median -100%, 19% winners (about 7 of 36).
- **30d +0% hold10:** 15 trades, average -72%, median -100%. This was the main structure, and it was the main source of the loss.
- **14d +0% hold10:** 7 trades, average -24%, median -100%.
- **14d +5% hold10:** 5 trades, average +42%, median -100%. The average is positive only because of one very large winner (about +612%). The median is a total loss.
- **Other cells (14d +10%, 14d +15%, 30d +10%, 90d):** 1 to 2 trades each. Too small to judge.

**Price band (new observation, low confidence):**
- In the logged best trades, over-$50 names were the winners in 4 of about 5 cases (including +223% and +612%).
- In the logged worst trades, losers were mostly in the under-$10 and $10-to-$50 bands.
- Bundle 5 found the opposite pattern for over-$50 names (most lost about 93% to 95%). The two bundles contradict each other.
- **Status:** not a rule. Check on the full trade list in bundle 7. The rule would only be considered if the over-$50 group has a positive median in at least two bundles.

**Stock-level results (all 250 candidates):** averaged +0.5% over 10 sessions, median -0.4%. The option trades were placed on these same candidates, so the option losses are not explained by the universe drift.

**Direction versus decay (still open):**
- I still cannot pair each option trade with its stock return over the same 10 sessions. The log does not carry the stock return for each trade. Without that pairing, I cannot separate the two.
- For the logged extremes, the best stock moves in bundle 6 were large (+18% to +56%). Several trades in the +14d and +30d cells that lost 100% were on names that did not move up. That points toward direction for part of the loss, but I cannot quantify it.

**New idea tested (partly):** the 2x-premium exit versus the 10-session close (Step 7 in section 3). Not run yet. The log lacks the path of each option's premium, so the count of trades that reached 2x and then reversed cannot be computed.

---

## 3. WHAT I WILL TRY NEXT

Tests run in order. Do not start a later test until the earlier one is logged.

**Step 1 (priority, every bundle from now on): log both sides of every candidate.**
- For every candidate (traded or not), record the 10-session stock return.
- For every traded candidate, record the option result, the option's premium path (peak premium and day it peaked), and the stock return over the same window.
- Classify each option trade as (a) the stock rose 5% or more but the option still lost more than half its premium (strike or decay problem), or (b) the stock did not rise 5% (direction problem). Make the next structural decision from this split.
- **Without this, bundles 5 and 6 cannot be interpreted. This is the first thing to fix.**

**Step 2 (no money): reversal and volatility test on the full candidate universe.**
- Question 1: do candidates with a negative 20-day return have higher 10-session returns than those with a positive 20-day return, across all candidates?
- Question 2: do high-vol20 names (above 4%) have wider 10-session dispersion than low-vol20 names, and is the median different?
- Method: bucket every candidate by 20-day return (below -10%, -10% to 0%, 0% to +10%, above +10%). Report median and average 10-session stock returns per bucket. Repeat for RSI (below 30, 30 to 60, above 60). Repeat for vol20 (below 2%, 2% to 4%, above 4%). Do not use the extremes lists.
- Pass rule: for the reversal claim, the lowest 20-day bucket has a higher median than the highest bucket, in bundle 7 and bundle 8. For the volatility claim, report dispersion; no pass or fail is needed for it to inform the option design.
- Confidence this holds: low. Bundles 5 and 6 point in opposite directions on the extremes.

**Step 3 (paper-trade only, after Step 2): direction without options.**
- If Step 2 shows a bucket with a consistent median across two bundles, paper-track stock positions in that bucket over 10 sessions (no options). Keep these outside the real book.
- Pass rule: positive median and average 10-session stock return, at least 15 paper trades, in the same bundle.

**Step 4 (after Step 3): deep in-the-money strike test, options.**
- 30-day calls, strike about 5% below price (higher delta), exit at 10 sessions. Minimum 15 trades, minimal size.
- Purpose: test whether the near-total median loss (-100% in bundle 6, -37% to -58% in earlier bundles) is caused by strike choice and decay rather than direction.
- Pass rule: positive median and average on the bundle's trades, and at least 3 of 4 trades where the stock rose 5% or more ending with more than half their premium.

**Step 5: vol20 as a premium filter (after Step 4).**
- Compare trades with vol20 below 2% against trades with vol20 at or above 4%, using medians. Do not trade until the comparison is logged.

**Step 6: over-$50 price check (runs with Step 2, costs nothing).**
- Using the full trade list (not the extremes), compare the median option return in the over-$50 band against the other bands, across bundles 5, 6, and 7.
- Rule only if the over-$50 group has a positive median in at least two of the three bundles.

**Step 7: 2x-premium exit versus 10-session close.**
- Count how many trades reached 2x premium and then reversed by the 10-session exit, and how much the winners would have gained if held. No exit change until this count is logged.

**Step 8: +1 rating check (costs nothing).**
- Track 10-session median return for the +1 cohort in bundle 7. If it is again below the +0 and -1 cohorts, write it up as a "do not buy +1-rated names" hypothesis for a later pre-registered test. Do not use it for sizing.

**Position sizing until a test passes:**
- No option trades in the 30d +5% cell, the 14-day cells, or the 90-day cells.
- No option trades at any strike other than the ones tested in Step 4.
- No averaging up.
- Any new option test is minimal size and needs a pre-registered pass rule before it starts.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

**Supporting evidence, with confidence:**

- **30d +5% double_or_10:** negative median in every bundle with a meaningful sample. Pooled average negative across roughly 180 to 200 trades. Confidence of positive expectancy: **none**. Off.
- **Momentum (positive 20-day return, above 20-day average, RSI 55 to 80):** worked in bundle 4 only. Failed in bundles 2, 3, and 5. Dropped as a gate.
- **Short-term reversal (negative 20-day, oversold RSI):** supported by the bundle 5 extremes, not by the bundle 6 extremes. Confidence: low. Under Step 2 test.
- **Volatility dispersion:** both tails in bundle 6 were dominated by high vol20 names. Confidence that vol20 matters for dispersion: moderate (it is consistent with the option's size of move). Confidence it predicts direction: none. Under Step 2 and Step 5.
- **Falling-knife caution (deep drawdown, negative 5-day returns):** supported by losers in bundles 2 and 3, contradicted by winners in bundles 4 and 5. Low confidence. Demoted to Step 6 in earlier plans; now folded into Step 2's bucket test.
- **Ratings:** no consistent order across bundles 2 to 6. The +1 cohort has underperformed in bundles 5 and 6 (low confidence). Used only as a hypothesis for Step 8.
- **News:** winners in the option cells usually had 7-day news, but losers did too. No usable filter.
- **Price band:** conflicting between bundle 5 (over-$50 lost) and bundle 6 (over-$50 won in most logged cases). Under Step 6. Not a rule.
- **Market trend (market 5d and 20d):** winners and losers appeared in rising and falling markets. Dropped as an explanation.
- **Short-call ratio (short):** extreme values appeared among both winners and losers. Not usable on its own.
- **Spike recency, call-day persistence, combined column thresholds:** did not replicate across bundles. Dropped as entry gates.

**Dropped or demoted:**
- The 30d +5% double_or_10 structure (off).
- The 14d and 90d expiries, and the 14d 10-session hold (off).
- Strikes at 0%, +10%, +15%, +20% (off until Step 4 results).
- Momentum as a gate (failed in bundle 5, unconfirmed in bundle 6).
- Ratings as a gate or sizing signal.
- Spike recency, call persistence, and single or combined column thresholds as entry gates.

**What I have learned overall:**
- The option structures I have traded depend on rare, very large winners. The median trade loses most or all of its premium in every bundle, and bundle 6 was the worst median yet (-100% in the main cell).
- Judge every structure on the median and on the stock's own 10-session move, not on the average.
- I still cannot separate direction from decay, because the log does not pair each option with its stock move. Fixing the logging (Step 1) comes before any new option test.
- The two most recent bundles disagree on the 20-day direction pattern, and both extremes lists are dominated by high-volatility names. Bundles 5 and 6 together do not tell me which way 10-session direction leans in this universe. The next step is to measure it on the full candidate set (Step 2), not on the extremes.

### Agent 3's final notes (not passed on)

# TRADING NOTES: FINAL (after bundle 6 of 6)

## 1. CURRENT STRATEGY AND RULES

### 1a. Status: no real option trading, no capital committed
- **Real option trading stays suspended.** Nothing is committed to any option structure. Every option idea is paper-logged until it passes the gates in section 4.
- **Reconcile bundle 6 before anything else.** The bundle reports -$12,444 on 39 trades, which means trades were recorded as executed. The bundle 5 stop rule said real option trading stops after a second negative-median 30-day baseline, and bundle 5 triggered it. Bundle 6 then has a third negative-median 30-day baseline (-42.4% on 22 trades). I must establish whether these 39 trades were real, paper, or executed under a stale instruction. If any were real after the stop rule, that is a process breach and must be logged as one. Until reconciled, treat the bundle 6 option results as a real-money loss and the process as not working.
- **Per-trade size if any capital is ever committed:** platform minimum, and no single trade above about 1% of bundle capital.
- **Cumulative option record:** about -$44,100 over about 264 option trades across six bundles (estimate: prior total of about -$31,700 over 225 trades plus bundle 6's -$12,444 over 39). Win rate in bundle 6 was 21%.

### 1b. Option structure to paper-trade (the baseline I am measuring against)
- **Instrument:** at-the-money call.
- **Expiry:** 30 days. (14-day expiries are dropped.)
- **Exit:** 10 sessions after entry, no profit target.
- **Purpose:** this is a measurement baseline, not a recommendation. Paper-log every candidate so the median can be tracked on a larger sample.
- **Evidence for the baseline being negative:** median -37.9% (bundle 4), -21.7% (bundle 5), -42.4% (bundle 6, 22 trades). Average was positive in some bundles only because of a few very large winners. Median is the number to watch.

### 1c. Paper-only alternatives to track (no real money, low confidence)
- **30-day call, +10% profit target, hold 10.** Bundle 6: 5 trades, median -23.8%, average -17.5%. That beat the +0% baseline on both measures in this bundle. This reverses my earlier conclusion that profit targets of +5% or more underperform. The +5% target still failed (5 trades, median -80%). The +10% result is 5 trades in one bundle, so it is a paper candidate only.
- **30-day call, +15% target, hold 10.** Bundle 6: 2 trades, median -22.4%. Too few to judge.
- **90-day call, no target, hold 10.** Bundle 5: 9 trades, median -54.1%. Bundle 6: 2 trades, median -44.5%. Not a replacement for the baseline.
- **90-day call, +10% or +20% target.** Bundle 6: one trade each, +34.7% and +44.7%. Single observations, nothing more.
- **Double-or-10 exits:** dropped (see section 5).

### 1d. Stock-level rules
- **No stock-level filter currently passes a gate.** Do not select names by rating, RSI, volume, price band or news for real trades.
- **Rating +1 is not a signal.** Bundle 6: 37 stocks, median -0.2% vs baseline -0.4%, average -1.7% vs +0.5%. The median is above baseline by 0.2 points, but the average is 2.2 points below. Not a filter.
- **Rating -1 is not a short signal.** Bundle 6: 64 stocks, median -0.6%, average +1.2%. Average was above baseline. No short edge in six bundles.
- **Rating 0 is the only group to beat baseline on both measures in bundle 6** (116 stocks, median +0.2%, average +1.2%, about 0.6 and 0.7 points above baseline). This is one bundle, the rating may just mark "no view," and the gap is small. Watch it; do not trade it.
- **Rating -2** had 3 stocks (average +6.4%). Too few to read.
- **Oversold (RSI-based) rule: not supported.** It is dropped as a directional rule (see 2c).
- **Overbought-spike loser pattern: unscored.** It remains a paper hypothesis (see section 3).

### 1e. Why these rules
- Six bundles of data show no rating with a stable edge over the stock baseline. Stock returns are close to zero on average and median. Tails are large in both directions (about -42% to +56% in 10 sessions in bundle 6), and the tails come from all rating groups.
- The option drag is consistent. Even when stock-level moves are near zero, the 30-day ATM call loses on median, so the structure, not the stock picks, is the main problem.
- Option averages look positive in some bundles only because of a few very large winners. The median trade loses.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### 2a. Option results
| Structure | Trades | Average | Median | Read |
|---|---|---|---|---|
| 30d, +0% target, hold 10 | 22 | -41.4% | -42.4% | Negative median for the third bundle in a row. Stop rule already triggered. |
| 30d, +5% target, hold 10 | 5 | -18.5% | -80.0% | Worst median. Dropped. |
| 30d, +10% target, hold 10 | 5 | -17.5% | -23.8% | Beat the +0% baseline on both measures. Paper candidate only. |
| 30d, +15% target, hold 10 | 2 | -22.4% | -22.4% | Too few to judge. |
| 30d, +5% double-or-10 | 1 | -100% | -100% | Dropped. |
| 90d, +0% target, hold 10 | 2 | -44.5% | -44.5% | Negative, consistent with bundle 5. |
| 90d, +10% target, hold 10 | 1 | +34.7% | +34.7% | Single trade. |
| 90d, +20% target, hold 10 | 1 | +44.7% | +44.7% | Single trade. |

- **Total bundle 6:** 39 trades, 21% winners, average -31.9%, median -41.9%.
- **Bundle 6 option drag, stock-level view:** the stock baseline was about flat (median -0.4%), so the option structure accounts for nearly all of the loss. Median stock returns in the +0% baseline group were not far from baseline, but the option median was about -42%.

### 2b. Stock-level results (250 candidates)
- **Baseline:** average +0.5%, median -0.4% over 10 sessions.
- **By rating:** see section 1d.
- **Read:** no rating separates direction. The rating-0 group is the only one with a small edge over baseline, and it is not tradable as a rule.

### 2c. Extremes (pattern-spotting only, not evidence)
- **Oversold hypothesis from bundle 5 failed here.** The biggest winners in bundle 6 had RSI 42 to 73 (most between 54 and 73). Several of the biggest losers had RSI 16, 30 and 36, which is oversold. So low RSI did not predict winners this bundle. The bundle 5 pattern (winners oversold) did not repeat. Conclusion: RSI does not predict direction on these extremes. Oversold is dropped as a directional rule.
- **Overbought-spike loser pattern is not separable.** Losers had RSI 39 to 73 and many had elevated 20-day or 5-day moves, but the winners showed the same readings. The pattern is not a filter on the extremes printout.
- **Volume and news:** the largest winners had high call-volume ratios (calls 10x to 52x in some cases, call days 2x+ of 4 to 12 over 20 sessions). Losers had similar readings. Volume and news do not separate winners from losers.
- **Price band:** no separation. Drop.
- **Read:** the tails are not predictable from the columns I can see on extremes. Any filter must be tested on the full table, pre-registered, not chosen after seeing winners.

### 2d. New idea tried: stock-only oversold filter (not scorable)
- Pre-registered filter: RSI below 35, off 60-day high below -25%, 20-session change below -15%.
- **Result:** not scored. The printout gives extremes only, so I cannot count passes, compute pass vs fail medians or compare to baseline. The extremes that were visible do not support the filter (see 2c). Status: unscored, low prior, dropped as a directional idea.

### 2e. Process findings
- **Real-money suspension was not clearly enforced** (see 1a). Must be reconciled.
- **The printout still does not give the full candidate table.** Every filter remains untestable until the full table is available.

---

## 3. WHAT I WILL TRY NEXT

1. **Reconcile the bundle 6 trade log.** For each of the 39 trades, record whether it was real, paper, or executed under the stop rule. Any real trade after the stop rule is logged as a breach. Owner: the system, not me, to confirm.
2. **Require the full candidate table before any filter test.** If it is not provided, no filter is scored in that bundle, and I record "not tested" rather than reading the extremes as evidence.
3. **Score the overbought-spike loser pattern, pre-registered.** Filter: RSI above 65, 5-day change above +10%, 20-session change above +20%. Measure the 10-session median and average stock return against that bundle's baseline. If it underperforms baseline on median and average, it becomes a "do not chase" note for paper and future decisions.
4. **Score the oversold filter on the full table, as written in 2d.** Its prior is now low because bundle 6 extremes did not support it. Still worth one scored test, since bundle 5 extremes suggested it.
5. **Paper-trade the 30-day baseline on median only.** Log every candidate, measure the 10-session median. Three bundles of negative median are already on record, so the question is whether a larger paper sample keeps it negative.
6. **Paper-trade the +10% profit target against the +0% baseline,** same 30-day expiry, same candidates. Require at least 20 paper trades before it counts, since bundle 6 had only 5.
7. **Track the rating-0 group** on full tables. Test whether it beats baseline on median and average in a second bundle. This is a watch item, not a trading rule.
8. **Keep the sample guard.** Stop any paper setup after 10 consecutive negative trades. Stop any real-money setup immediately.

---

## 4. GATES BEFORE ANY REAL CAPITAL

- **Signal gate (stock level):** a filter must (a) be pre-registered before the bundle is scored, (b) show a positive median 10-session stock return above that bundle's baseline on at least 50 candidates, (c) beat baseline on both median and average, and (d) hold in at least two bundles. No filter currently passes. Oversold: not passed, prior low. Overbought loser pattern: not yet scored. Rating 0: watch only.
- **Option gate:** after a filter passes the signal gate, the option structure must show a positive median return over at least 20 paper trades.
- **Structure gate:** a structure change (90-day, profit target, different exit) must beat the 30-day, +0% target, hold-10 baseline on median over at least 20 paper trades before it replaces the baseline. The +10% target has 5 trades so far. The 90-day has 2 to 9 depending on the bucket.
- **Stop rule:** a second negative-median 30-day baseline suspends real option trading. This has been triggered (bundle 5), and bundle 6 added a third negative median. Real trading stays off until the gates above pass and the bundle 6 reconciliation is complete.
- **Baselines for comparison (10-session stock return):**
  - Bundle 2: +1.7% average, -0.6% median.
  - Bundle 3: -0.5% average, -0.9% median.
  - Bundle 4: -1.3% average, -0.6% median.
  - Bundle 5: -1.3% average, -1.2% median.
  - Bundle 6: +0.5% average, -0.4% median.

---

## 5. SUPPORTING EVIDENCE AND IDEAS I HAVE DROPPED

**Overall confidence: low.** Six bundles, about 264 option trades, most option buckets under 10 trades. No stock-level signal has passed the gate. The option drag is the most consistent finding, but its size varies from bundle to bundle.

**Held up across bundles (moderate confidence):**
- **30-day ATM call, +0% target, hold 10 has a negative median** in bundles 4, 5 and 6 (-37.9%, -21.7%, -42.4%).
- **14-day expiries underperform.** Lost in every bundle where tested.
- **Option medians are negative even when averages are positive.** Averages depend on a few very large winners.
- **No rating has a stable stock-level edge** across bundles.

**Did not hold up or too weak to trust:**
- **Profit targets of +5% or more, as a blanket rule.** The +5% target failed again (median -80%, 5 trades). The +10% and +15% targets beat the +0% baseline in bundle 6 (medians -23.8% and -22.4% vs -42.4%). This contradicts my earlier finding that all targets of +5% or more underperform. The earlier claim is withdrawn. The +10% target is now a paper candidate, not a rule.
- **Oversold as a directional signal.** Bundle 5 extremes suggested it. Bundle 6 extremes did not (winners RSI 42 to 73, several losers RSI 16 to 36). Dropped as a directional rule. One scored test remains (section 3, item 4).
- **Rating +1 as a signal.** Beat baseline on median in bundles 2 to 4, failed in bundle 5, and in bundle 6 the median was above baseline but the average was 2.2 points below. Dropped.
- **Rating -1 as a short signal.** Average was above baseline in bundle 6 (+1.2% vs +0.5%), no short edge in bundles 5 or 6. Dropped.
- **90-day expiry as a default alternative.** Bundle 5 median -54.1% (9 trades). Bundle 6 median -44.5% (2 trades). Positive results are single trades. Not a replacement for the baseline.
- **News-support as an option filter.** No separation in bundles 4 or 6.
- **"Spike, no news," put-heavy readings, p/c, price band.** No consistent separation.
- **Single large option winners** (+315%, +255%, +200%, +134%, +55%). Tail events. They do not make a strategy and are the only reason option averages look positive.

**Dropped:**
- Any 14-day expiry.
- Double-or-10 exits.
- Profit targets of +5% (as a blanket rule; +10% and +15% are paper candidates only).
- Rating +1 as a signal.
- Rating -1 as a short signal.
- Oversold RSI as a directional filter.
- 90-day expiry as a default.
- News-support as an option-entry filter.
- p/c as an entry filter.
- "Spike, no news" as a signal.
- Price band as a separator.
- Any filter chosen by looking at extremes alone.

### Agent 4's final notes (not passed on)

# TRADING NOTES (revised after bundle 6)

## 1. MY CURRENT STRATEGY

**Status: no live trading. Paper-track only, under the pre-registered test below. The old entry setup is dropped.**

### 1a. The paper-test setup

Every entry must meet all of these rules. Trades outside them are logged separately and excluded from the test.

| Column or item | Rule |
|---|---|
| Universe | Every candidate with calls ≥ 3 (call volume at least 3x its 20-session median) on the latest session, and price band $10 to $50 or over $50. No other filter. |
| Instrument | Calls only |
| Expiry | 60 to 90 days. 14-day and 30-day calls are out of the test. |
| Strike | At the money to 5% above price |
| Sizing (paper) | 1% of capital at risk per trade, scored as a total loss (-100%) |

**Entry logging:** log every candidate in the universe automatically, whether or not I would have chosen it. Selection by me is what made the bundle 6 sample unreadable (see section 2).

**Three exits, scored on the same entries:**
- **(A) Hold 10 sessions** (baseline).
- **(B) Double-or-10:** take profit when the option doubles, otherwise hold 10 sessions.
- **(C) Stop at -50% of premium,** otherwise hold 10 sessions.

**Decision rule (set before reading results):** an exit becomes a candidate only if its median is above zero across at least 30 in-spec entries. If no exit reaches that, I stop trading options and stay on paper.

**Quit criteria:** no live trading unless one exit has a median above zero over at least 30 in-spec trades, and the average is not carried by one trade. If the single largest trade contributes more than half the total profit, the result is not an edge.

**Cut points are frozen.** RSI, vs ma20, call days, and the calls ≥ 3 threshold will not change for this test. A cut point changed after seeing results is curve-fitting.

### 1b. Reasoning

- **Stock direction from the rating has no reliable signal.** Across six bundles the stock-level result is near flat. Bundle 6: all 250 candidates averaged +0.5% (median -0.4%). Rated +0 beat rated -1 by about 4 points, but rated +1 did worse than +0, so the ordering is not monotone. Dropped.
- **Options lose to decay and to the exit rule.** Option results across bundles 1 to 6 have a median that is negative in every bundle. Stocks were roughly flat in the same windows, so the loss is in the instrument and the exit, not the stock move.
- **The exit matters more than my entry guesses.** Hold-10 is the weakest exit in both bundles 5 and 6. Double-or-10 has a better average than hold-10 in both bundles, but its median is not reliably positive.
- **Entry filters have been fitted to visible rows.** Five bundles of entry searches produced thresholds that flipped sign from bundle to bundle. The paper test removes entry filtering as the main question.

### Confidence
- **Entry rule:** none. The old setup failed its kill test and is dropped.
- **Exit comparison:** unknown. Hold-10 looks worst in two bundles. Double-or-10 looks better on average, not on median. Neither has reached the decision threshold.
- **Stock direction from rating:** none.
- **Calls ≥ 3 universe:** untested as a whole. Bundle 6 shows a pattern in the visible extremes (see section 2), but I cannot compute the universe result from them.

---

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

### Bundle 6 totals
- **+$908 on 33 trades.** Average +2.8%, median -4.1%, 42% winners.
- The first positive-average bundle since bundle 2, but the median is still negative. The average depends on a few large winners.
- Stock universe: +0.5% average, -0.4% median over 10 sessions.

### Breakdown by exit and expiry

| Group | Expiry | Trades | Average | Median | In spec? |
|---|---|---|---|---|---|
| Double-or-10, strike +0% | 90-day | 11 | -2.3% | -3.7% | Yes |
| Double-or-10, strike +5% | 90-day | 10 | +5.2% | -7.6% | Yes |
| Hold-10, strike +0% | 90-day | 3 | -54.3% | -74.4% | Yes |
| Hold-10, strike +5% | 90-day | 2 | -7.9% | -7.9% | Yes |
| Double-or-10, strike +0% | 30-day | 6 | +21.5% | -20.1% | **No** (30-day) |
| Double-or-10, strike +5% | 30-day | 1 | +113.7% | +113.7% | **No** (30-day) |

**In-spec subtotals (90-day, 26 trades):**
- **Double-or-10:** 21 trades. Average about +1.3%. Both group medians are negative (-3.7% and -7.6%), so the pooled median is almost certainly negative.
- **Hold-10:** 5 trades. Average about -36%. Medians -74% and -8%.
- **Stop (C):** not traded. No data.

### Process failure, recorded
- **I traded seven 30-day calls, which the 60-to-90-day rule excludes.** Their results are logged but excluded from the test. The 30-day group gave the biggest average (+21.5%, and +113.7% on one trade) but a median of -20.1% on six trades.
- **Exits were not scored on the same entries.** Each trade used one exit. The three-way comparison in section 1a has not yet been run on a common set of entries.
- **Trade selection was mine, not the universe.** I cannot tell from this bundle how the universe performed.

### What the visible trades show (extremes only, so biased)
- Nineteen of the twenty visible trades had calls ≥ 3. The one exception had 2.7 and was a winner. The visible list is a set of extremes, so this does not show that the universe works or fails.
- **Price band among visible trades:**
  - Over $50: 5 of 6 positive (+33%, +100%, +114%, +116%, +254%), one loss (-48%).
  - $10 to $50: 5 of 14 positive. Nine losses ranged from -57% to -100%.
  - Under $10 is excluded from the universe.
- This price pattern is a hypothesis to log, not a filter. Six over-$50 trades and fourteen $10-to-$50 trades is far too few to separate the bands.
- The big winners were on calls at or near the money with high calls ratios, but the same profile shows up in the losers. No other column separated winners from losers in the visible rows.

### Stock-level findings
- Rated +0 (138 stocks): average +2.1%, median +1.0%.
- Rated -1 (81): average -1.9%, median -2.8%.
- Rated +1 (30): average -0.4%, median -0.5%.
- Rated -2 (1): +7.7%. Too few to use.
- Over six bundles, rating has no direction signal I can rely on. Dropped.

---

## 3. WHAT I WILL TRY NEXT

1. **Run the section 1a test on the next fresh stock set, with the universe logged in full.** Every candidate with calls ≥ 3 and price ≥ $10 gets an entry logged automatically, traded or not. Each entry gets all three exits (A, B, C) scored on the same underlying data.
2. **Count in-spec entries per exit, not per trade I chose.** The 30-entry threshold applies to the universe log. Bundle 6 contributes 21 in-spec double-or-10 trades and 5 in-spec hold-10 trades, but these were not scored on common entries, so they count only as evidence that the exits differ.
3. **Stop trading 14-day and 30-day calls, including on paper trades I would like to take.** Log them separately if I want them, excluded from the test.
4. **Test the -50% stop on the full set.** For each stop trigger, record whether the same option would have recovered above -50% by day 10. If the path is not visible, mark the stop as untested rather than inferred.
5. **Run double-or-10 with and without the top trade**, and report both. Keep the 60-to-90-day expiry.
6. **Log the price band and every entry column on every trade,** as data only. Do not use them to exclude trades in this test. Revisit only after the exit decision is made.
7. **Sizing check before any live trade:** at 1% risk, five losses in a row is a 5% drawdown. Confirm this is inside the loss limit before any capital is committed.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Results across bundles (all trades)

| Bundle | Result | Trades | Average | Median | Winners |
|---|---|---|---|---|---|
| 1 (old setup) | -$17,038 | 51 | -33% | -42% | 27% |
| 2 (old setup, fresh stocks) | +$8,579 | 29 | +30% | -32% | 38% |
| 3 (filter where possible) | -$10,790 | 42 | -26% | -37% | 31% |
| 4 (fresh stocks, filter on visible rows) | -$9,994 | 31 | -32% | -27% | 26% |
| 5 (strict filter applied) | -$5,868 | 31 | -19% | -50% | 26% |
| 6 (paper-test rules, 7 out-of-spec trades) | +$908 | 33 | +2.8% | -4.1% | 42% |

- Bundle 2 and bundle 6 are the only profitable bundles. Both have medians that are negative or near zero, and both depend on large winners.
- Bundle 6 is the best median so far, but still negative. Its average is positive mainly because of the over-$50 winners and the 30-day group.

### Exit evidence
- **Hold-10:** worst in bundle 5 (average about -20%, most trades worse than -30%) and in bundle 6 (90-day average about -36%, median -74% for the 0% strike). Consistent across two bundles. Confidence that hold-10 is a poor exit on these trades: moderate.
- **Double-or-10:** better average than hold-10 in both bundles. Bundle 5 (30-day, 5 trades): median +93%. Bundle 6 (90-day, 21 in-spec trades): average about +1%, median negative. Bundle 6 (30-day, out of spec, 7 trades): median -20%. The medians disagree across bundles and expiries. Confidence: low.
- **Stop at -50%:** not tested. No evidence either way.

### Old-setup passers (dropped)
- Combined across bundles 3 to 5: about 21 passers, median still negative. The kill test was met and the setup was dropped.

### Evidence for each dropped rule

| Rule | What the data showed | Bundles | Status |
|---|---|---|---|
| RSI 40 to 69 | Mixed. No clean separation. | 3 | Dropped |
| vs ma20 0 to +10 | Cut points unstable. Winners near the cap. | 3 | Dropped |
| calls 5d ≥ 2 and call days ≥ 3 | Necessary-looking in one bundle, not sufficient in others. | 3 | Dropped |
| 90-day vs 30-day expiry | 90-day in-spec double-or-10: average about +1%. 30-day double-or-10: median -20% in bundle 6 and +93% in bundle 5. | 3 | Unresolved. Test on 60-to-90-day only |
| Price $10 to $50, or over $50 | Over-$50 visible trades mostly positive; $10-to-$50 visible trades mostly negative. Not tested on a full universe. | 3, visible only | Hypothesis; log, do not filter |
| Under $10 underlyings | Most -100% outcomes across bundles | 4 | Excluded |
| Rating direction | Flat across all bundles | 6 | Dropped |
| Fresh spike only (days since spike 0 to 2) | No separation | 2 | Dropped |
| "Spike, no news" | Winners and losers alike | 3 | Dropped |
| 14-day calls | Heavy losses in every bundle they were traded | 3 | Dropped |
| 30-day calls | Excluded from the test. Bundle 6 median -20% (6 trades); bundle 5 median +93% (5 trades) | 2 | Out of spec. Not traded |
| Full 90-day bucket with no filter | Flat to negative | 3 | Dropped |

### Ideas still open (not yet tested on a clean basis)
- **Stop at -50%:** section 1a, exit (C). Needs path data.
- **In-the-money calls:** deeper strikes might reduce decay and -100% outcomes. Would need a separate paper test with its own decision rule.
- **Premium selling on flat stocks:** might collect decay. Needs its own tail-loss review before any test.

### Open questions
- Does any exit reach a positive median on at least 30 in-spec trades in the universe log?
- Is the over-$50 pattern real, or a feature of the visible extremes?
- Does the double-or-10 median turn positive on common entries, or does it only look better on average?
- Does the -50% stop cut more winners than losers once recoveries are counted?


## Last error

```
2026-10-09 21:31 UTC
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
