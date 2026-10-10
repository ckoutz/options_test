# Committee generations (2026-10-10 02:23 UTC)

Total spent on all agent runs: $13.28. Candidate pool: {'train': 2998, 'score': 1439, 'holdout': 2000, 'test': 2720}.

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
| 3 | agent1 | train | 211 | -8163.4 | -4009.0 | -3.87 | 34.1 | -0.007 (-0.063 to 0.044) | -0.28 | 1.07 | 4/151 | 0.4595 |
| 3 | agent2 | train | 259 | -19846.3 | -16835.0 | -7.66 | 34.4 | 0.003 (-0.057 to 0.057) | 0.29 | 1.27 | 3/151 | 0.3976 |
| 3 | agent3 | train | 275 | -2130.4 | -18067.5 | -0.77 | 36.4 | -0.027 (-0.077 to 0.021) | -0.29 | 1.87 | 3/151 | 0.4227 |
| 3 | agent4 | train | 208 | -20817.1 | -14393.6 | -10.01 | 31.2 | -0.026 (-0.083 to 0.03) | -0.36 | 1.24 | 4/151 | 0.3922 |
| 3 | all | unfinished |  |  | - | - | - | - | - | - | 0/ | 1.1656 |
| 3 | scorer | score | 221 | -39393.2 | -41128.1 | -17.82 | 25.8 | -0.019 (-0.063 to 0.032) | -0.01 | 0.95 | 8/144 | 0.9507 |
| 4 | agent1 | train | 206 | -26821.1 | -32589.2 | -13.02 | 31.1 | 0.0 (-0.073 to 0.079) | 0.42 | 0.77 | 3/151 | 0.419 |
| 4 | agent2 | train | 210 | -2056.6 | -27132.0 | -0.98 | 29.0 | 0.006 (-0.064 to 0.07) | 1.77 | 1.29 | 3/151 | 0.4954 |
| 4 | agent3 | train | 224 | -28688.2 | -21459.2 | -12.81 | 31.2 | 0.002 (-0.05 to 0.056) | 0.68 | 1.39 | 5/151 | 0.4617 |
| 4 | agent4 | train | 241 | -5304.4 | -23063.7 | -2.2 | 27.4 | 0.0 (-0.07 to 0.055) | 0.72 | 1.59 | 6/151 | 0.5341 |
| 4 | scorer | score | 267 | -39894.7 | -57965.7 | -14.94 | 26.2 | -0.065 (-0.109 to -0.007) | -0.58 | 1.29 | 7/144 | 0.9614 |

## Luck check

- Different rules tested on training data so far: 125 (by the agents and the editor).
- Editor rules checked on the blind months: 31; passed clearly (whole 95% range above buying everything the same way): 0.
- Expected to pass by luck alone: about 0.8. Treat a pass as real only if it clearly beats that count and the rule keeps passing in later generations.

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
| 3 | big movers (hindsight) | 118 | -11.39 | -10.39 | -13,435 | -12,266 |
| 3 | wide (honest) | 103 | -25.20 | -22.08 | -25,958 | -22,741 |
| 4 | big movers (hindsight) | 141 | -6.13 | -14.56 | -8,642 | -20,537 |
| 4 | wide (honest) | 126 | -24.80 | -27.92 | -31,253 | -35,175 |

## Generation 4

### Editor's rules, tested on all training months and bundles

- R1 momentum + market up, 30d 10% OTM (when 20d % > 20 and vs ma50 % > 15 and market 20d % > 0: buy the 30-day call 10% above the price, exit hold10): 173 trades, average +42.5% (95% range +4.3% to +83.0%, resampling whole weeks), median -49.8%, 33% winners. Buying every candidate the same way: -17.7%. Beat that in 6 of 6 bundles; first half of the months +25.6%, second half +52.1%.
- R2 trend+tone+over50, 30d 5% OTM (when vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 143 trades, average +23.4% (95% range -5.7% to +56.8%, resampling whole weeks), median -41.3%, 38% winners. Buying every candidate the same way: -12.2%. Beat that in 4 of 6 bundles; first half of the months +23.8%, second half +23.1%.
- Over50 trend + market up, 90d 5% OTM (when price = >$50 and vs ma50 % > 0 and 20d % > 0 and market 20d % > 0: buy the 90-day call 5% above the price, exit hold10): 58 trades, average -5.1% (95% range -18.6% to +8.3%, resampling whole weeks), median -13.9%, 40% winners. Buying every candidate the same way: -7.4%. Beat that in 4 of 6 bundles; first half of the months -7.0%, second half -3.7%.
- R6 over50 gate, 30d ATM (when price = >$50 and vs ma50 % > 0 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 259 trades, average +5.0% (95% range -9.6% to +19.7%, resampling whole weeks), median -25.1%, 38% winners. Buying every candidate the same way: -10.9%. Beat that in 6 of 6 bundles; first half of the months -5.1%, second half +11.3%.
- R7 over50 uptrend market up, 90d 10% OTM (when vs ma50 % > 0 and market 20d % > 0 and price = >$50: buy the 90-day call 10% above the price, exit hold10): 57 trades, average +4.3% (95% range -14.2% to +22.4%, resampling whole weeks), median -9.4%, 42% winners. Buying every candidate the same way: -9.7%. Beat that in 5 of 6 bundles; first half of the months -11.1%, second half +12.1%.
- R1 momentum gate at 90d 5% OTM (when 20d % > 20 and vs ma50 % > 15 and market 20d % > 0: buy the 90-day call 5% above the price, exit hold10): 51 trades, average -4.0% (95% range -19.3% to +15.6%, resampling whole weeks), median -22.9%, 35% winners. Buying every candidate the same way: -7.4%. Beat that in 3 of 6 bundles; first half of the months +14.8%, second half -10.4%.
- Quiet-after-spike uptrend over50, 30d ATM (when days since spike >= 20 and vs ma50 % > 0 and market 20d % > 0 and price = >$50: buy the 30-day call 0% above the price, exit hold10): 17 trades, average +17.3% (95% range -33.5% to +86.5%, resampling whole weeks), median -32.5%, 47% winners. Buying every candidate the same way: -10.9%. Beat that in 2 of 2 bundles; first half of the months -20.4%, second half +37.8%.
- Trend+tone+market up over50, 90d 5% OTM (when vs ma50 % > 0 and news tone 7d > 0 and market 20d % > 0 and price = >$50: buy the 90-day call 5% above the price, exit hold10): 22 trades, average -13.9% (95% range -29.0% to -0.4%, resampling whole weeks), median -13.2%, 36% winners. Buying every candidate the same way: -7.4%. Beat that in 1 of 3 bundles; first half of the months -28.3%, second half -1.9%.

### The same rules on the blind scoring months (never shown to agents)

- R1 momentum + market up, 30d 10% OTM (when 20d % > 20 and vs ma50 % > 15 and market 20d % > 0: buy the 30-day call 10% above the price, exit hold10): 159 trades, average -21.7% (95% range -42.0% to -1.2%, resampling whole weeks), median -59.9%, 25% winners. Buying every candidate the same way: -20.6%. Beat that in 4 of 6 bundles; first half of the months -14.0%, second half -29.7%.
- R2 trend+tone+over50, 30d 5% OTM (when vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 89 trades, average -7.8% (95% range -40.0% to +30.7%, resampling whole weeks), median -56.2%, 28% winners. Buying every candidate the same way: -19.8%. Beat that in 3 of 6 bundles; first half of the months +17.1%, second half -24.8%.
- Over50 trend + market up, 90d 5% OTM (when price = >$50 and vs ma50 % > 0 and 20d % > 0 and market 20d % > 0: buy the 90-day call 5% above the price, exit hold10): 56 trades, average -6.1% (95% range -19.4% to +7.8%, resampling whole weeks), median -15.1%, 36% winners. Buying every candidate the same way: -7.1%. Beat that in 3 of 6 bundles; first half of the months -15.9%, second half +0.7%.
- R6 over50 gate, 30d ATM (when price = >$50 and vs ma50 % > 0 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 188 trades, average -20.9% (95% range -35.1% to -4.2%, resampling whole weeks), median -42.0%, 29% winners. Buying every candidate the same way: -14.7%. Beat that in 2 of 6 bundles; first half of the months -22.9%, second half -19.0%.
- R7 over50 uptrend market up, 90d 10% OTM (when vs ma50 % > 0 and market 20d % > 0 and price = >$50: buy the 90-day call 10% above the price, exit hold10): 56 trades, average -13.7% (95% range -27.2% to +2.3%, resampling whole weeks), median -22.2%, 25% winners. Buying every candidate the same way: -7.8%. Beat that in 2 of 6 bundles; first half of the months -17.6%, second half -11.4%.
- R1 momentum gate at 90d 5% OTM (when 20d % > 20 and vs ma50 % > 15 and market 20d % > 0: buy the 90-day call 5% above the price, exit hold10): 47 trades, average +3.2% (95% range -24.0% to +38.7%, resampling whole weeks), median -18.7%, 32% winners. Buying every candidate the same way: -7.1%. Beat that in 3 of 6 bundles; first half of the months -18.3%, second half +29.7%.
- Quiet-after-spike uptrend over50, 30d ATM (when days since spike >= 20 and vs ma50 % > 0 and market 20d % > 0 and price = >$50: buy the 30-day call 0% above the price, exit hold10): 14 trades, average -45.1% (95% range -59.6% to -24.1%, resampling whole weeks), median -46.9%, 7% winners. Buying every candidate the same way: -14.7%. Beat that in 0 of 3 bundles; first half of the months -54.4%, second half -35.8%.
- Trend+tone+market up over50, 90d 5% OTM (when vs ma50 % > 0 and news tone 7d > 0 and market 20d % > 0 and price = >$50: buy the 90-day call 5% above the price, exit hold10): 32 trades, average -6.9% (95% range -28.3% to +11.7%, resampling whole weeks), median -15.1%, 34% winners. Buying every candidate the same way: -7.1%. Beat that in 2 of 4 bundles; first half of the months -25.3%, second half +7.4%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

(Committee editor's synthesis of four independent traders over six bundles. Where a trader's figure and the code-tested scorebook differ, the scorebook is used. All returns are per-trade option returns on premium, held 10 sessions unless noted. "Benchmark" means buying every candidate with the same expiry, strike and exit. Rules are written with exact conditions so you can restate them and have them scored.)

---

## 0. BOTTOM LINE

**What the code established**
- The long-call wrapper loses. Almost every rule has a negative median, typically -15% to -65%, with 22% to 45% winners. Averages come from a minority of large winners (+100% to +600%).
- The benchmark averages for buying every candidate are:

| Structure | Benchmark average |
|---|---|
| 30-day at-the-money (ATM) | -10.9% |
| 30-day 5% above price | -12.2% |
| 30-day 10% above price | -17.7% |
| 90-day ATM | -8.4% |
| 90-day 5% above | -7.4% |
| 90-day 10% above | -9.7% |

- **Trend, momentum and an up-market gate are the one consistent source of improvement.** The same strike in the same bundles goes from deeply negative to positive when the stock is above its 50-day average with positive 20-day momentum and the market's 20-day return is above zero. The complement (20d % ≤ 20 at 30-day 10% above) averaged -22.8% over 1,722 trades. The momentum rule inside a down market averaged -47.8%.
- **Price over $50 helps and $10 to $50 hurts.** Under $10 is erratic. Positive news tone is a mild help.
- **No rule is a proven safe edge.** The best rules have positive averages, 95% ranges (resampled by week) that mostly straddle zero, and negative medians. Treat them as lottery-ticket baskets that are the least bad, not as edges.

**Where the traders were wrong or split, as scored by code**
- All four ended paused or paper-only and said "no edge, wrapper cost is large". The wrapper cost is real: the universe's 10-session stock median sat between -1.2% and +0.7% while option medians were -15% to -75%. But the traders' blanket dismissals of filters were wrong.
- **Agent 1** championed the gate (over $50, above ma50, market up). The code confirms it at 30-day ATM and at 30-day 5% above, with 6 of 6 bundles beaten on both. Agent 1 then dropped "trend as a standalone filter" and the "momentum lottery" after reading extremes lists. The code contradicts that.
- **Agent 2** retired "30-day 5% above, over $50, trend, tone > 0" on about 15 trades (median -80%). On 143 code trades it averaged +23.4% with the most even halves of any rule. Median is still about -41%, so it is a tail rule. Agent 2 also dropped news tone and found no separation. The code found tone useful when stacked with trend and price. Agent 2's momentum-plus-news idea was confirmed (+16.4%).
- **Agent 4** was right about Setup C (30-day, 10% above, 20d % > 20 and vs ma50 % > 15). It beat its benchmark in 6 of 6 bundles on 211 trades. But the traders' "about +100% to +150% average, median positive" is wrong. The code median is -57.4%, with 30% winners. Agent 4's call to ban 30-day ATM and drop 30-day 5% above is not supported. Trend-filtered versions of both beat their benchmarks.
- **Agent 3** banned all 30-day structures and kept only 90-day 5% above as a paper candidate. The code agrees that 90-day versions have much better medians. But Agent 3's own market-up, $10 to $50, 90-day 5% rule averaged -13.3%, and the $10 to $50 band is the poison. The 90-day 5% above structure works only with trend or over $50.
- **Ratings** were rejected by all four. The sign flipped between bundles. Do not use them.
- **Agreed by all:** the wrapper is the main drag, 14-day expiries are terrible, exits cannot rescue entries, hold 10 sessions, flat small size, and nobody has logged premium or implied volatility.

---

## 1. STRATEGY: SETUPS WORTH TRADING (small flat size, or paper)

All rules are bought on the entry day and exited after 10 sessions. Size so that a -100% loss on every open position is survivable. Do not add after wins. Because results are tail-driven, take every signal that passes rather than cherry-picking, and spread premium across many names. Skipping a lottery-ticket signal is how a basket loses its few big winners.

These rules overlap heavily: they pick up the same trending, up-market names. Do not count them as independent confirmations.

### 1A. Tier 1: positive average, large n, and beat the benchmark in most bundles

**R1. Momentum run, 30-day call 10% above price (Agent 4's Setup C)**
- Rule: 20d % > 20 and vs ma50 % > 15.
- Scorebook: 211 trades, average **+26.2%** (95% range -6.0% to +61.0%), median -57.4%, 30% winners. Benchmark -17.7%. **Beat it in 6 of 6 bundles.** Halves +11.9% and +35.9%.
- Looser version (20d % > 15 and vs ma50 % > 10): 274 trades, +14.4% (range -14.1% to +42.0%), median -59.7%, 6 of 6, halves +1.5% and +22.7%. The strict thresholds are better.
- At 90 days the same gate gives 57 trades, -4.4%, median -20.3%, 4 of 6, halves +7.3% and -10.3%. It is better than its benchmark but not a positive-average rule.
- Extreme tail-driven lottery: the median trade loses more than half the premium. Size very small.
- **Never use it when the market's 20-day return is below zero.** That version (add market 20d % < 0) had 38 trades, **-47.8%** (range -78.2% to -16.7%), median -87.6%, 18% winners.

**R2. Trend + news + over $50, 30-day call 5% above price**
- Rule: vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price over $50.
- Scorebook: 143 trades, average **+23.4%** (range -5.7% to +56.8%), median -41.3%, 38% winners. Benchmark -12.2%, beat in 4 of 6 bundles. Halves +23.8% and +23.1%, the most even halves of any rule.

**R3. Trend + news, all price bands, 30-day call 5% above**
- Rule: vs ma50 % > 0 and 20d % > 0 and news 3d > 0.
- Scorebook: 306 trades, +11.3% (range -10.9% to +35.0%), median -51.1%, 29% winners. Beat the benchmark in 4 of 6 bundles. Halves +11.3% and +11.3%.
- Adding over $50 and positive tone (R2) roughly doubles the average.

**R4. Momentum plus news, 30-day call 5% above (Agent 2's idea, code-confirmed)**
- Rule: 5d % > 5 and vs ma20 % > 5 and news 3d ≥ 1.
- Scorebook: 186 trades, +16.4% (range -13.3% to +49.6%), median -48.4%, 31% winners. Beat the benchmark in 4 of 6 bundles. Halves +13.0% and +20.8%.

**R5. Up-market uptrend, 30-day call 5% above (Agent 1's rule, the broadest and best-sampled rule)**
- Rule: market 20d % > 0 and vs ma50 % > 0.
- Scorebook: 756 trades, +6.1% (range -10.4% to +21.2%), median -48.4%, 29% winners. Benchmark -12.2%, **beat in 6 of 6 bundles**. Halves +0.5% and +9.3%.
- The related call-flow version (calls 5d avg > 1 and vs ma50 % > 0) had 844 trades, +1.0%, 5 of 6 bundles, with halves +6.0% and -2.5%. The market gate does more work than the call-flow condition.

**R6. Price, trend and market gate, 30-day ATM (Agent 1's gate)**
- Rule: price over $50 and vs ma50 % > 0 and market 20d % > 0.
- Scorebook: 259 trades, +5.0% (range -9.6% to +19.7%), median -25.1%, 38% winners. Benchmark -10.9%, **beat in 6 of 6 bundles**. Halves -5.1% and +11.3%.
- The median of about -25% is the best of the 30-day positive-average rules. It is the "least ugly" 30-day ATM option.

**R7. Above ma50 in an up market, 90-day call 10% above (Agent 1's idea, code-confirmed)**
- Rule: vs ma50 % > 0 and market 20d % > 0.
- Scorebook: 183 trades, +3.3% (range -10.7% to +17.6%), median -16.1%, 38% winners. Benchmark -9.7%, beat in 5 of 6 bundles. Halves +0.5% and +4.6%.
- Steadiest and least volatile positive result. **The market gate is the point:** the same stock condition with market 20d % < 0 averaged -12.9% over 78 trades, with halves -4.4% and -23.9%.

**R8. Full filter stack, over $50, 90-day call 10% above**
- Rule: calls 5d avg > 1 and vs ma50 % > 0 and market 20d % > 0 and price over $50.
- Scorebook: 42 trades, +7.0% (range -16.7% to +27.0%), median **-8.0%**, 45% winners. Benchmark -9.7%, beat in 4 of 6 bundles. Halves -8.3% and +13.9%.
- Same stack at $10 to $50: 63 trades, -4.2%, median -19.6%, halves -19.5% and +2.5%. Over $50 is clearly better.

### 1B. Tier 2: near-benchmark or better, but smaller n, unstable halves, or no positive average

- **High vol trend up, 30-day ATM.** Rule: vol20 % > 5 and vs ma50 % > 0 and 20d % > 0. 232 trades, +1.9% (range -22.6% to +27.1%), median -48.5%, 5 of 6 bundles, halves +3.6% and +0.5%. Stable but wide and heavily tail-driven.
- **Overbought chase, 30-day ATM.** Rule: RSI > 70 and vs ma20 % > 10. 233 trades, +4.8% (range -17.3% to +29.0%), median -46.7%, 4 of 6 bundles, halves -0.7% and +10.3%.
- **Overextended run, 30-day call 10% above.** Rule: vs ma50 % > 25 and RSI > 75. 81 trades, +20.7% (range -27.3% to +88.2%), median -50.9%, 4 of 6 bundles. Halves -27.2% and +51.9%, so it is unstable and the second half carries it.
- **Run plus heavy call buying, 30-day 10% above.** Rule: 20d % > 20 and call days 2x+ 20d ≥ 2. 293 trades, +12.0%, median -65.0%, 4 of 6 bundles. Halves -11.6% and +34.2%. Inferior to R1, which has no call-flow condition.
- **Plain over-$50 filter.**
  - 30-day ATM: 700 trades, -1.7%, median -29.4%, 5 of 6 bundles, halves +4.7% and -7.9%.
  - 90-day 5% above: 198 trades, -3.8%, median -16.5%.
  - 90-day over $50, up market, vs ma20 % > 5, 90-day 5% above: 33 trades, -4.7%, median -9.5%, 4 of 5 bundles.
- **Positive news, 30-day ATM.** Rule: news tone 7d > 0 and news 3d > 0. 432 trades, -0.1%, median -35.0%, 5 of 6 bundles, halves +8.6% and -10.8%.
- **Broad uptrend, 90-day 5% above.** Rule: calls 5d avg > 1 and vs ma50 % > 0. 224 trades, -2.5%, median -20.5%, 5 of 6 bundles. This is the steadiest 90-day 5% option and the closest match to Agent 3's paper candidate. Add over $50 or market-up to improve it.
- **Momentum, 90-day 5% above.** Rule: 20d % > 10. 174 trades, -1.0%, median -22.2%, 4 of 6 bundles, halves +4.6% and -5.1%.
- **Quiet after a spike, 30-day ATM.** Rule: days since spike ≥ 20 and calls 5d avg < 1. 117 trades, **+10.1%** (range -19.8% to +48.3%), median -37.9%. Beat the benchmark in only 2 of 6 bundles, but both halves are positive (+20.3% and +1.6%). This is a "buy before the crowd" lead.
- **Oversold rebound in an up market, 90-day ATM.** Rule: RSI < 35 and off high % < -20 and market 5d % > 0. 31 trades, +6.6% (range -16.2% to +39.1%), median -9.5%, 3 of 5 bundles. Halves -15.9% and +19.0%. Small, unstable and noisy.
- **Extended uptrend, mid price, 90-day 5% above.** Rule: vs ma20 % > 6 and 20d % > 9 and price $10 to $50. 54 trades, -2.1%, median -17.2%, 4 of 6 bundles, halves +5.5% and -6.6%. This is near benchmark and not worth building on.

### 1C. Weak or noise (do not build on these)

- **High-vol sub-$10, 90-day 5% above** (vol20 % > 4, price under $10): 92 trades, +3.7%, median -29.7%, 3 of 6 bundles. Halves +7.4% and +0.5%. Positive average from tails in the worst band for -100% outcomes.
- **High-vol sub-$10, 30-day ATM** (price under $10 and vol20 % ≥ 4): 383 trades, -0.9%, median -50.0%, 4 of 6 bundles. It beats a bad benchmark but loses half the premium on the median.
- **Dip name, 90-day ATM** (20d % < -20): 44 trades, +14.1%, median -9.0%, 3 of 6 bundles. Not confirmed elsewhere.
- **Sharp 1-day drop, 90-day 5% above** (1d % ≤ -5): 51 trades, +3.9%, 3 of 6 bundles. Halves +16.9% and -6.8%.
- **Five-day surge, capped** (5d % in 10 to 25, 90-day 5% above): 67 trades, -4.9%, median -28.9%, 3 of 6 bundles.
- **Fast spike, 30-day ATM** (days since spike = 0, calls 5d avg ≥ 5, calls 20d < 3): 88 trades, -0.5%. Halves +23.4% and -25.6%.

### 1D. Sizing and execution (all traders agree)

- Flat, small size. Never add after wins. Do not raise size because a rule just won.
- Use 30-day or 90-day expiries. Never use 14-day.
- Pick the structure by what you want:
  - **Tail-seeking lottery:** 30-day 5% or 10% above price with R1 to R4. Median about -40% to -57%. Tiny size, a full basket of every passer.
  - **Steadier profile:** 90-day with trend, an up-market gate and preferably over $50 (R7, R8). Median -8% to -16%.
  - **Middle road:** 30-day ATM with the over-$50 market gate (R6). Median -25%.
- Hold exactly 10 sessions. Double-or-10 and stop rules could not be told apart from hold-10 on common entries. Double-or-10 has a slightly worse benchmark (-12.0% vs -10.9%). No exit has been shown to rescue a bad entry.
- Always apply the market gate (market 20d % > 0) to any trend or momentum call rule. It is the clearest sign flip in the data.

---

## 2. AVOID

### Clearly worse than the benchmark (code-confirmed)

| Rule | Trades | Average (range) | Median | Beat benchmark |
|---|---|---|---|---|
| Momentum rule R1 in a down market (market 20d % < 0), 30-day 10% above | 38 | **-47.8%** (-78.2% to -16.7%) | -87.6% | 2 of 5 |
| Gate complement (20d % ≤ 20), 30-day 10% above | 1722 | **-22.8%** (-34.0% to -11.1%) | -68.2% | 2 of 6 |
| Large down day with call spike (1d % ≤ -5 and calls ≥ 3), 30-day | 95 | **-23.2%** (-42.2% to +2.3%) | -48.6% | 1 of 6 |
| Sub-$10 oversold rebound (RSI < 30, off high % < -30), 30-day 5% above | 80 | **-24.3%** | -64.2% | 2 of 6 |
| Calls ≥ 3 and price $10 to $50, 90-day | 103 | **-21.9%** (-31.1% to -12.2%) | -30.5% | 1 of 6 |
| Stretched-up (RSI ≥ 70, vs ma20 % ≥ 10, 5d % ≥ 10), 90-day ATM | 48 | **-20.6%** | -33.8% | 2 of 6 |
| Oversold bounce, mid price (RSI < 30, 20d % < -10, $10 to $50), 90-day 5% above | 17 | -20.6% | -29.9% | 1 of 2 |
| Call activity with high vol (calls 5d avg > 1, vol20 % ≥ 4, vs ma20 % > 0), 90-day ATM | 98 | **-19.7%** | -37.1% | 1 of 6 |
| $10 to $50 price alone, 30-day 5% above | 958 | **-19.6%** (-30.5% to -7.6%) | -60.0% | 1 of 6 |
| Spike with no news ≥ 1, 90-day ATM | 138 | **-19.4%** | -25.2% | 0 of 6 |
| Fresh spike with no news (days since spike ≤ 1, spike no news ≥ 1), 30-day ATM | 549 | **-17.9%** (-27.8% to -7.7%) | -42.7% | 1 of 6 |
| Oversold with high vol (vol20 % ≥ 4, RSI < 40), double-or-10 | 218 | -18.7% | -46.6% | 2 of 6 |
| Low-volatility dip (20d % < -10, vol20 % < 4), 30-day | 196 | -18.0% | -43.7% | 2 of 6 |
| Oversold (RSI < 45, off high % < -25), 30-day | 326 | -17.1% | -46.9% | 1 of 6 |
| Off-high oversold (off high % < -30 and RSI < 30), 30-day ATM | 122 | -16.3% (-34.5% to +3.4%) | -50.0% | 2 of 6 |
| Below ma50 with call interest in an up market, 90-day 10% above | 87 | -16.6% | -30.8% | 2 of 5 |
| Market up, $10 to $50, 90-day 5% above | 162 | -13.3% (-22.6% to -4.8%) | -22.8% | 1 of 6 |
| Calls ≥ 3 with no other condition, 90-day | 234 | -15.2% | -28.2% | 1 of 6 |
| OTM call build-up (otm calls 20d > 3 and p/c < 1), 30-day 10% above | 549 | -15.7% | -66.7% | 5 of 6 but still -15.7% |
| Call-days surge (call days 2x+ ≥ 4 and calls 5d avg > 2), 30-day | 256 | -15.0% | -47.9% | 2 of 6 |
| Stock above ma50 in a down market, 90-day 10% above | 78 | -12.9% | -21.2% | 2 of 6 |
| Under-$10 oversold dip, 30-day ATM | 148 | -6.3% (-28.0% to +18.0%) | -50.0% | 3 of 6 |
| Low-vol gate (over $50, vol20 % < 2, market up), 30-day ATM | 252 | -6.6% | -31.2% | 4 of 6 |

### Themes
- **Dip-buying with calls loses** at nearly every expiry and strike. The small positive 90-day ATM dip and oversold-rebound cells are noise until confirmed.
- **Buying call-volume spikes loses** when the stock is falling, mid-priced, high-volatility, or has no news. Spike days mean expensive premium. Spike signals flip sign once the stock is above its 20-day average.
- **Do not use any bullish trend or momentum call rule when the market's 20-day trend is down.** Down-market versions were the worst cells in the whole scorebook.
- **$10 to $50 stocks are the worst band** for 30-day 5% above and for market-up 90-day rules.
- **Low volatility alone does not help.** The over-$50 low-vol gate underperformed the plain gate. Volatility is not a free fix.

### No edge either way (about the benchmark)
- Extended names (RSI ≥ 75, vs ma20 ≥ +20): 96 trades, -8.2%. "Extended names fade" is unsupported.
- Sustained call building at 30 days (calls 5d avg ≥ 2, call days 2x+ ≥ 3): 573 trades, -8.9%, 3 of 6.
- Slow steady call buying (calls 20d > 5, call days 2x+ 20d > 7), 30-day 5% above: 179 trades, -4.3%, halves +20.1% and -27.4%.
- Low volatility with call activity, 90-day ATM: 276 trades, -9.5%.
- Heavy calls with news, 30-day 5% above: 423 trades, -6.6%.
- Put crowding (puts 5d avg ≥ 3): 727 trades, -9.2%. It is not a bearish signal.
- Under-$10 stocks, even with calls active and an up market: -8.4%.
- **Ratings of any kind.** Patterns reversed bundle to bundle. Do not use for entry, sizing or fading.

### Stop doing
- 14-day expiries.
- Strikes 10% or more out of the money outside R1 and its direct variants.
- Reading best and worst lists as evidence. Both tails contain the same features. The extremes lists misled three of the four traders.
- Using exits to rescue a bad entry.
- Judging by total P&L, averages alone, or n < 20 cells. Cells at n = 3 to 40 flipped sign between bundles.
- Trading a structure your own notes moved to paper only.

---

## 3. NEW IDEAS TO TEST

Ordered by expected value. Each should be stated as an explicit rule so it can be scored. Require n ≥ 60, both halves reported, and a benchmark comparison.

1. **Stack trend, over $50, news and market at 90 days (highest priority, untested).**
   - Evidence: over $50 + news + trend at 30 days gave +23.4% with even halves, and above-ma50 in an up market at 90 days gave +3.3% in 5 of 6 bundles.
   - Test at 60 and 90 days, calls 5% and 10% above:
     - over $50 + vs ma50 % > 0 + 20d % > 0 + news tone 7d > 0
     - the same with market 20d % > 0
     - the same with calls 5d avg > 1
2. **Market gate on everything.** Add market 20d % > 0 to R2, R3, R4 and the momentum variants. Also test market 5d % > 0, and market 20d % > 2 as a stricter gate. Check whether the first-half versus second-half gaps in most rules are a market-regime effect. Since the market gate separates +26% from -48% in R1, a market gate may fix the halves problem.
3. **Strike and expiry ladder inside the momentum setup.**
   - R1 beat its benchmark in 6 of 6 bundles at 30-day 10% above.
   - Test ATM, 5%, 10% and 15% above at 30, 60 and 90 days.
   - Test thresholds (20d % > 10, 20, 30; vs ma50 % > 10, 15, 25), plus over-$50 and positive-news add-ons.
   - Look for the version with the best median, which was only -20% at 90 days.
4. **Buy before the crowd.**
   - Evidence: quiet-after-spike (+10.1%, both halves positive), and the tiny n=7 sample of aged spikes in an uptrend at 90 days (+109%).
   - Test: days since spike ≥ 20 combined with vs ma50 % > 0, over $50 and market 20d % > 0, at 30 and 90 days.
   - Also test the slow 20-day measures nobody tested directly: calls 20d, long calls 20d, otm calls 20d, call days 2x+ 20d.
5. **Replace the wrapper (untested).**
   - Stock medians are near zero while option medians are -20% to -60%, so most of the loss is wrapper cost.
   - Test deep in-the-money 90-day calls (strike 5% to 10% below the price, delta about 0.8) and bull call spreads on the Tier 1 filters.
   - Compare each with the plain stock return on the same entries.
6. **Volatility-aware premium filter.**
   - Evidence: vol20 % ≥ 4 with call activity lost -19.7%, while the high-vol trend rule was fine (+1.9%). It is the combination of high vol with no trend that hurts.
   - Test vol20 % bands (below 2, 2 to 4, above 4) inside R1, R2 and R7.
   - Test whether premium cost relative to vol20 explains the losses.
7. **Why the overbought chase works at 30 days but fails at 90 days.** 30-day ATM gave +4.8%. The 90-day version with 5d % ≥ 10 gave -20.6%. Test whether 5d % ≥ 10 is the toxic ingredient, and test RSI > 70 with strikes 5% above.
8. **Unused features, tested as single-feature buckets.** Keep a feature only if it beats the benchmark in at least 4 of 6 bundles and in both halves: shares and shares 5d avg, close vs vwap %, vs vwap20 %, short/medium/long call mixes, p/c drop, news 1d, puts 20d.
9. **Fade the losers with defined risk (paper only, high risk).**
   - The worst cells lose 18% to 48% on average with ranges excluding zero: momentum in a down market, large down day with a spike, $10 to $50 at 30 days, spike with no news.
   - Test put debit spreads or bear call spreads on those cells. Check for tail risk, since these names occasionally rebound hard.
10. **Stock-level attribution.**
    - Compare the 10-session stock return of Tier 1 passers against the universe median on the same dates.
    - This separates how much of the result is signal versus premium. It needs per-candidate stock returns. Ask for them if they exist.
11. **Basket and sizing simulation.** Because every positive rule is a few-big-winners rule, test whether an equal-premium basket of all R1 to R6 passers per week has a positive weekly total, and what the worst-week drawdown is. Test whether the 6-of-6 bundle record survives de-duplication of overlapping names.
12. **Entry implied volatility** is not available. If it ever becomes available, test whether low premium relative to realized vol explains which passers win.

---

## 4. OPEN QUESTIONS

- **Positive median.** Can any call setup have a positive median? The best so far are the full stack over $50 at 90 days (-8.0%), the 90-day oversold ATM (-10.0%, tiny n) and the over-$50 market-up 90-day 5% rule (-9.5%). Is a positive median reachable only with deep in-the-money calls, spreads or stock?
- **Tails versus stability.** Why are the 30-day rules (+23% to +26% average, median -41% to -57%) so different from the 90-day rules (+3% to +7% average, median -8% to -16%)? Is the 30-day edge only a heavier right tail, and does it survive realistic sizing and bid-ask costs that the scorebook does not charge?
- **Over $50.** Is it a liquidity, size or lower-implied-volatility effect, or a proxy for something else? It helps at 30 days and out-of-the-money strikes but barely at 90-day ATM.
- **First half versus second half.** Most rules were better in the second half (R1, R5, R6), while some were better in the first. Is this market trend, volatility, or specific weeks? Examples: R6 -5.1% then +11.3%, the full-stack $10 to $50 rule -19.5% then +2.5%.
- **Strike effect.** At 90 days 5% above beat ATM on benchmarks (-7.4% vs -8.4%). At 30 days, trend and momentum rules did best out of the money, while the non-trend rules did best ATM. Is strike distance a proxy for convexity capture on trending names?
- **Exits.** Hold-10, double-or-10 and a stop are indistinguishable without premium paths. Does a longer hold (15 or 20 sessions) help 90-day rules?
- **Dips at long expiries.** Do the small positive dip and oversold results at 90-day ATM (+14.1% n=44, +6.6% n=31) mean dips work at long expiries, or are they noise? They contradict the large negative 30-day and 5%-above dip results.
- **Ratings.** No stable signal. Treat as noise unless a full-universe test with n ≥ 60 and medians says otherwise.
- **Does the market gate generalize?** All Tier 1 results sit in a sample where the market was up in most weeks. If the market regime changes, the rules' averages could reverse. Down-market behavior is known only for R1 and R7, and both were bad.

### Agent 1's final notes (not passed on)

# TRADING NOTES: FINAL (after six bundles)

## 1. MY CURRENT STRATEGY

### 1a. Position: no trades
I do not trade option calls, and I do not trade stock on any rule. Nothing I have tested meets the bar for live or paper trading. The bar is: pre-registered, n ≥ 20, a positive median in two consecutive bundles, and an average not driven by one or two trades.

Across six bundles, no option cell or stock-only filter has met it. The option results are the clearest finding. Stock-level gains did not translate into option gains. In bundle 6, the universe median over 10 sessions was +0.5%, while the largest option cell (30-day at-the-money calls, hold 10, n = 23) had a median of -8.9%. The gap is about nine points and appears in most cells.

### 1b. Instruments and cells I have ruled out

| Setup | Evidence | Confidence it is negative |
|---|---|---|
| Calls above the money (+5%, +10%, +15% strikes) | Negative medians in bundles 3, 4, 5, and 6 across every tested expiry. Bundle 6: 30d +5% median -85.2% (n = 3), 30d +10% median -89.1% (n = 6). | High on direction. Samples are small per cell. |
| 30-day at-the-money calls, hold 10 | Negative average in bundles 3 and 4 (15 trades). Bundle 6: average +14.8%, median -8.9% (n = 23). The average turned positive only because of a few large winners. Median is the decision variable. | Moderate to high. Largest sample, still a negative median. |
| 14-day at-the-money calls | Bundle 4 positive on five trades. Bundle 5 median -8.1% on hold 10 (n = 16). Bundle 6 median -68.8% (n = 5, average +56%). | Moderate to high. Average depends on tails. |
| 90-day at-the-money calls | Bundle 4 positive median (n = 7), bundle 5 negative median (n = 8). Bundle 6 median -10.8% (n = 3). Dropped under the two-bundle rule. | Moderate. |
| Double-or-10 exits | Median near total loss on 14-day calls (bundle 5 -98.9%, bundle 6 median -68.8%). Does not beat hold 10 on the same entries. | High. |
| Calls on names below their 50-day average | Excluded. Losers were concentrated here. | Low to moderate. Not retested in clean form. |
| Dip-buying with calls (RSI oversold, deep off the high) | Winners and losers both present. Too few clean trades. | Low. |

### 1c. Stock-only filters
The only candidate stock-only filter is the gate: share price over $50, vs ma50 % > 0, market 20d % > 0.

- **Status:** Untested with clean numbers. Bundle 6 did not report gate-passing stock returns separately, and I did not log per-trade stock returns for all option trades. The gate cannot be scored from the data I have.
- **Confidence that it adds edge:** Low.

### 1d. Reasoning
1. **The option wrapper, not the stock move, is where the losses come from.** In bundle 6 and bundle 5, option medians were far below the universe median. Premium decay, strike distance, and the need for a fast move are the likely causes. Implied volatility at entry is still not logged, so this is inference, not measurement.
2. **Averages mislead here.** Bundle 6 option P&L was +5,036 with a median of -14.4%. A few trades with +200% to +400% returns produced the positive total. Those tails cannot be identified in advance from the columns I have. I do not trade on tails.
3. **Ratings do not predict returns.** Bundle 6 averages: +1 at +1.4%, 0 at +1.5%, -1 at -2.0%, -2 at +30.1%. Medians: +0.9%, +0.6%, +0.1%, +0.3%. The -2 average is one trade (+221%) away from zero. Across bundles there is no stable monotone pattern.
4. **Upside tails exist in every price band.** Under $10, $10 to $50, and over $50 all produced large winners and large losers in bundle 6. Price band alone is not a rule.

---

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

**Bundle 6 (final):**
- Universe: 249 candidates, average +0.7%, median +0.5% over 10 sessions.
- Option P&L: +5,036 on 43 trades, average +11.7%, median -14.4%, 44% winners.

**By cell:**

| Cell | Trades | Average | Median | Result |
|---|---|---|---|---|
| 30d ATM, hold 10 | 23 | +14.8% | -8.9% | Negative median. Cell fails. |
| 30d +10%, hold 10 | 6 | -5.2% | -89.1% | Strike rule holds. |
| 14d ATM, double-or-10 | 5 | +56.2% | -68.8% | Average from tails. Median fails. |
| 30d +5%, hold 10 | 3 | -36.0% | -85.2% | Strike rule holds. |
| 90d ATM, hold 10 | 3 | -24.9% | -10.8% | Small sample. Median negative. |
| 90d +10%, hold 10 | 1 | +30.2% | +30.2% | n = 1. No conclusion. |
| 90d +5%, hold 10 | 1 | +33.2% | +33.2% | n = 1. No conclusion. |
| 14d +5%, hold 10 | 1 | +33.0% | +33.0% | n = 1. No conclusion. |

**Pattern:** Every cell with a median reported above -10% has n ≤ 3 or is the 30-day at-the-money cell with a negative median. Strike-above-the-money cells lost on the median in every bundle where they were tested.

**Ratings (bundle 6):**

| Rating | Stocks | Average | Median |
|---|---|---|---|
| +1 | 50 | +1.4% | +0.9% |
| 0 | 88 | +1.5% | +0.6% |
| -1 | 105 | -2.0% | +0.1% |
| -2 | 6 | +30.1% | +0.3% |

Ratings did not separate outcomes on the median. The -1 average is pulled down by a few large losers. The -2 average is pulled up by one extreme winner.

**Biggest losers (bundle 6):** Mostly under $10 or $10 to $50. Common features: high 1-day or 5-day drops (some -30% to -50% in one day), high vol20 (often 4 to 14), and large call or put spikes. Several losers were rated -1 or 0. Some had news in the prior 7 days.

**Biggest winners (bundle 6):** Mostly under $10 or $10 to $50. Common features: deep off-high positions (-30% to -90%), large 20-day moves in both directions, and news in some cases. Several winners were rated -1 or 0, which is a warning against using ratings.

**Market check:** The universe medians over bundles have been: bundle 3 -1.7%, bundle 4 -0.8%, bundle 5 +0.3%, bundle 6 +0.5%. Medians alternate sign. The universe is not a stable benchmark, which is why any stock filter must beat the universe median in the same bundle, not zero.

**What this bundle adds:**
- Option medians were negative in nearly every cell with n ≥ 3, even as universe medians were positive. The wrapper result has now repeated across four bundles.
- The strike-above-the-money result held again.
- No new cell earned a place. Bundle 6 did not produce a positive-median cell with n ≥ 20.

---

## 3. WHAT I WILL TRY NEXT

Since this is the final bundle in the series, the forward plan is to stop option testing and keep any stock test pre-registered and separate.

1. **Stop all option trading and option-cell testing.** Reason: no option cell has passed in six bundles, and the wrapper gap persists. Any future option test needs implied volatility at entry and exit logged before it starts.

2. **Stock-only gate test (if continued).** Pre-register before the next data arrives:
   - Entry: price over $50, vs ma50 % > 0, market 20d % > 0.
   - Hold: 10 sessions, fixed size.
   - Compare the gate's median to the universe median in the same bundle.
   - Pass: gate median above universe median in two consecutive bundles, n ≥ 20.
   - Fail: gate median at or below universe median in one bundle. The gate is then dropped.

3. **Log per-trade stock returns alongside every option trade.** This is the only way to test whether the wrapper is the problem. Without it, the claim remains inference.

4. **Log implied volatility at entry and exit.** Needed to test premium decay directly.

5. **Volatility band check (stock only).** Tag vol20 % as under 2, 2 to 4, and 4 or above. Compare stock outcomes by band inside the gate. Losers in bundles 5 and 6 were concentrated in high-volatility names, so the high band is the most likely source of losses. Pass: low band beats the others in two bundles, n ≥ 20 per band.

6. **Report the universe return by market 20-day sign for every bundle.** Not reported in bundle 6. Required to score the gate.

7. **Off-high rebound (stock only, low priority).** Stocks more than 30% below their 60-day high with RSI under 30. Large winners and losers in this group. Test only with n ≥ 20.

---

## 4. SUPPORTING EVIDENCE AND IDEAS I HAVE DROPPED

**Kept, low confidence**
- **Gate (over $50, vs ma50 > 0, market 20d > 0).** Stock-only filter, untested with clean numbers. Low confidence it adds edge.
- **Strike ordering (above-the-money calls lose).** Negative medians across four bundles. Moderate confidence on direction. Small per-cell samples.
- **Hold 10 sessions.** Keeps results comparable across cells. Not evidence of edge.

**Dropped**
- **30-day at-the-money calls.** Negative average in bundles 3 and 4. Negative median in bundle 6 (n = 23), the largest sample. The positive average in bundle 6 came from tails. Fails the two-bundle positive-median rule.
- **14-day calls (all variants).** Bundle 4 positive on five trades. Bundles 5 and 6 negative on median. Fails.
- **90-day at-the-money calls.** Positive median in bundle 4 (n = 7), negative in bundles 5 and 6. Fails.
- **Double-or-10 exits.** Median near total loss on 14-day calls. Does not beat hold 10.
- **Out-of-the-money calls at any expiry.** Negative medians across bundles.
- **Momentum lottery (30-day, +10%, 20d > 20, vs ma50 > 15).** No stable edge.
- **Rating-based entries and rating fade.** No monotone pattern. The -2 bucket is too small and driven by single trades.
- **Price-band rules.** Winners and losers in every band. No band has a positive median across bundles.
- **Reading best and worst lists as rules.** Winners and losers share features (high volume, high volatility, news, large 20-day moves, off-high position). Too few trades to separate them.
- **Trend (vs ma50 > 0) as a standalone filter for options.** Losers included high-trend names in bundles 4, 5, and 6.
- **Dip-buying with calls.** Not validated at sample size. Excluded.

**Open questions (unresolved at close)**
- Is the option wrapper the main loss source? Needs per-trade stock returns and implied volatility. Not logged in time.
- Does any gate-passing stock cell beat the universe median in two bundles? Not tested with clean data.
- Is the universe median positive in general? It has alternated sign across bundles, so no stable benchmark exists.

**Process rules (retained)**
- A rule goes live only if pre-registered, n ≥ 20, and positive median in two consecutive bundles.
- Live and paper trades are logged separately. Everything is currently paper; no live trades.
- Fixed size. No adding after wins.
- Kill rules are honored when triggered.
- Pass and fail criteria are written before the next bundle arrives.
- For any future option trade: log the stock's return, implied volatility at entry and exit, and market 20-day sign.

### Agent 2's final notes (not passed on)

# Options and Entry Research: Final Notes for the Committee Editor

Status: six bundles complete. This is the final version. Stock-level signals remain unidentified, and no option trade meets the gates below.

---

## 1. Current Strategy and Rules

### 1.1 Position

No option positions are open or planned. The program is stock-level research on which columns predict large 10-session moves in either direction. Options stay on paper until a stock-level signal passes the gates in 1.3.

Bundle 6 produced a positive total P&L (+$10,608 on 31 trades). I am not treating that as evidence for trading. The median option trade lost 26.8%, the total came from a small number of very large winners, and no arm has a defensible positive median across bundles.

### 1.2 Standing rules

- **No option entries.** Nothing is sized or traded on the option wrapper until every gate in 1.3 passes.
- **Ratings (+2 to −2) are excluded from entry, sizing, exit, and ranking.** They are logged only. The sign of the rating effect has flipped across bundles.
- **No new columns, filters, strikes, or expiries** until the gates are resolved.
- **No reopening retired arms** (see section 4) on the strength of a single bundle.

### 1.3 Gates for any future option trade (all must pass)

1. **Stock-level tail edge.** A fixed bucket with n ≥ 30 whose upper-tail rate (≥ +15% in 10 sessions) is at least 2× the full-bundle base rate. The lower-tail rate must be reported alongside it. A bucket that adds only downside tail is not a call signal.
2. **Wrapper economics.** Either (a) the arm's median across at least 30 trades is positive, or (b) the break-even ratio (section 1.4) is below 1.0 on logged premium.
3. **Premium recorded.** Any trade without a logged premium is excluded from the break-even test. Premium "missing" means the test cannot be run, which means no trade.
4. **Position rules, if all three gates pass:** flat premium, small size, closed on the 10th session, sized so that a −100% loss on every open position is survivable.

**Current status:** no bucket passes gate 1, no arm passes gate 2, and premium has never been logged (gate 3 unmet for six bundles).

### 1.4 The wrapper finding

**Break-even test.** Break-even move = strike distance + premium (as % of price). Divide by the 10-session standard deviation, estimated as vol20 % × √10. A ratio above about 1.0 means the trade needs a one-sigma-or-larger move in the right direction to pay.

**Option medians by bundle (long calls, 30-day and other arms combined):**

| Bundle | Trades | Median | Winners | Notes |
|---|---|---|---|---|
| 2 | n/a | −40.6% | n/a | |
| 3 | n/a | −51.6% | n/a | |
| 4 | 44 | −75.2% | 16% | |
| 5 | 27 | −60.1% | 26% | Total −$1,130 |
| 6 | 31 | −26.8% | 42% | Average +34.2%; total +$10,608 |

Bundle 6 is the least negative median in the series and the first bundle with a positive total dollar result. The average is positive, but the median stayed negative. The positive total came from a small number of very large winners, including trades up roughly +230%, +463%, and +638%.

**Arm-level read, bundle 6:**

- **30d, 0%, hold 10 (n=13):** average +14.4%, median −35.0%. Bimodal: many losses between −70% and −100%, and several large winners between +60% and +230%.
- **30d, 5%, hold 10 (n=5):** average +84.9%, median −46.4%. The average is one or two trades.
- **30d, 0%, double-or-10 (n=4):** average +43.0%, median +36.8%. This is the only arm in bundle 6 with a positive median. Bundle 5 had three trades in the same arm with a median of −66.5%. Pooled across bundles 5 and 6 (n=7), the median has not been computed and bundle 5 alone was negative. Treat as unresolved.
- **90d, 5%, hold 10 (n=3):** average −2.5%, median +4.5%. Still too few trades to conclude anything.
- **Single-trade arms (n=1 each):** 14d 0%/hold 10 (−26.8%), 14d 5%/hold 10 (−92.8%), 14d 0%/double-or-10 (−68.8%), 30d 5%/double-or-10 (+11.8%), 30d 20%/hold 10 (−1.3%), 30d 10%/hold 10 (+463.2%). Not interpretable.

**Mechanism (unchanged).** A call struck 5% or more above the price, held 10 sessions, must move past the strike distance plus premium. The median candidate does not move that far. The option result depends on a few large moves.

**Confidence:**
- High that the median long-call trade loses under this wrapper (five consecutive bundles with negative medians).
- Medium that the cause is the wrapper rather than the direction. The stock universe was roughly flat in most bundles.
- Bundle 6 shows that the tail can carry a whole bundle's dollar P&L. That is why the program cannot dismiss options outright, and it is also why a positive total should not be mistaken for an edge.

### 1.5 Stock-level baseline

10-session universe returns by bundle (all candidates, mean / median):

- Bundle 1: +0.3%
- Bundle 2: +2.7%
- Bundle 3: −2.0%
- Bundle 4: +0.5% / −0.8%
- Bundle 5: +2.6% / +0.3%
- Bundle 6: +0.7% / +0.5% (249 candidates)

The median is near zero in every bundle. Means are pulled by tails in both directions. Dispersion is high and two-sided in all six bundles.

### 1.6 Ratings (logged only)

Bundle 6 (10-session stock returns, mean / median):

- **+1 (n=48):** +6.1% / +3.3%
- **+0 (n=116):** −2.2% / −0.6%
- **−1 (n=83):** +2.3% / +0.7%
- **−2 (n=2):** −25.3% (too small to read)

Bundle 6 is the largest +1 vs −1 gap I have seen. Pooling bundles 5 and 6 gives roughly +4.1% mean for +1 (n≈107) and +3.1% for −1 (n≈167). In bundle 5 the −1 group beat +1. The +0 group was negative in bundle 6 and the mean differences are tail-driven. Ratings are not a usable signal. They stay logged, and the −2 sign is no longer tested.

---

## 2. What I Tested in Bundle 6

### 2.1 Option results

Summarized in section 1.4. Total P&L was positive (+$10,608), average +34.2%, median −26.8%, 42% winners. The median stayed negative. The positive total came from tail trades in arms with 1 to 5 trades each. None of the arms with n ≥ 10 has a positive median.

### 2.2 Tail-rate test (section 3, test 1 of the prior notes): not run

The bundle output again listed only the largest winners and losers (about 20 rows), not the full candidate table. I cannot compute the base rate of ≥ +15% or ≤ −15% moves, so I cannot test any bucket. I am not estimating tail rates from the sample of extremes. The test remains open and requires the full table.

### 2.3 Observations from the visible extremes (not tests)

- **Largest losers:** mostly under-$10 and $10–50 names. Several had spike activity with puts and calls elevated, deep drawdowns from the 60-session high, or 20-session runs of +20% to +60% followed by sharp reversals. Some had calls at 20-day ratios above 100×, and these still fell.
- **Largest winners:** mostly under-$10 and $10–50 names with news in the prior 1 to 7 days, high 20-session volatility (vol20 % 5 to 20), and prices above the 20- and 50-session averages. A few were deeply oversold and far off their high (for example, off high −88% with RSI 32) and then rebounded by +221%.
- **Reading:** the same features (under-$10 price, high volatility, spikes, news, extreme 20-day moves) appear on both sides. Visible extremes do not establish a direction.

### 2.4 New idea tried: momentum-plus-news bucket

Definition: 5-day change above +5%, vs ma20 above +5%, and at least one news article in the prior 3 days. Motivated by the bundle 5 tail winners.

**Result: not evaluated.** The bundle output gives no denominator for this bucket. It cannot be tested from the extremes list.

---

## 3. What I Will Try Next

Bundle 6 is the last scheduled bundle. If further candidate data arrives, the work is as follows, in priority order.

1. **Full candidate table, tail test (main test).** Record each candidate's 10-session return and whether it is ≥ +15% or ≤ −15%. Compute the base rate first. For each fixed bucket with n ≥ 30, report upper and lower tail rates separately. A bucket qualifies only if the upper tail is at least 2× the base rate.

   Fixed buckets:
   - calls 5d avg above 2.0
   - call days 2x+ ≥ 3 in the last 5 sessions
   - otm calls 20d above 3.0
   - days since spike = 0 or 1
   - vol20 % above 5
   - RSI below 35 and off high below −20%
   - price band (under $10, $10–50, over $50)
   - 5d % above +5, vs ma20 % above +5, and news 3d ≥ 1 (momentum-plus-news)

   If the full table is not provided, mark the test "not run." Do not estimate it.

2. **Under-$10 oversold test (carried forward).** Track names under $10 with RSI below 40 and off high below −20%. Report the upper and lower tails separately. Continue only if the upper-tail rate is at least 2× base on n ≥ 30. This group produced both the largest winners and the largest losers in bundles 5 and 6, so it stays open.

3. **Premium logging (hard requirement).** For any hypothetical option, record the strike distance, the premium as % of price, and the break-even ratio (section 1.4). Mark premium "missing" where it is absent and do not infer it. Unmet for six bundles.

4. **Ratings.** Keep logging. No further −2 tests. Any rating test must be pre-registered with n ≥ 100 pooled stocks and a median comparison, not a mean comparison.

5. **Do not test** new strikes, expiries, exits, or option filters. Do not reopen the retired arms.

---

## 4. Supporting Evidence and Ideas I Have Dropped

### 4.1 Held up (with confidence)

- **Option medians are negative under the long-call wrapper.** Five bundles (2–6), medians between −27% and −75%. Confidence: high. Bundle 6 is the closest to zero and is still negative.
- **Stock-level dispersion is high and two-sided.** Large moves in both directions in every bundle. Confidence: medium-high.
- **The 10-session median stock return is near zero.** Across bundles, between −0.8% and +0.5%. Confidence: medium-high.
- **Ratings do not predict stock returns in a stable direction.** Sign has changed across bundles, and the bundle 6 gap has not yet been replicated. Confidence: medium that they are noise.

### 4.2 Worked in one bundle, failed or unresolved in another

- **Positive −2 rating:** positive in bundles 2–4, negative in bundle 5, opposite in bundle 1. Dropped.
- **30-day 5% hold-10 tail winners:** three large winners in bundle 5 (+200% to +522%) after strong 5- and 20-day momentum with news. Bundle 4 had the same structure with a median near −75%. Bundle 6 had five trades with a median of −46.4% despite an average of +84.9%. The tail is real in the data but has not produced a positive median. Kept as a hypothesis for the momentum-plus-news bucket. Not traded.
- **30-day 0% double-or-10:** bundle 6 median +36.8% (n=4), bundle 5 median −66.5% (n=3). Unresolved. Not traded.
- **+1 rating outperforming in bundle 6** after −1 outperforming in bundle 5. Pooled gap is small and tail-driven. Logged only.

### 4.3 Retired or dropped

- **30-day 5%, over $50, vs ma50 > 0, 20d > 0, tone > 0 (filtered long call):** about 15 trades across bundles 2–5, median near −80%. Tone did not separate winners from losers. Retired.
- **30-day 10% above, hold 10:** bundle 4 median −76%, bundle 5 one trade (−70.5%), bundle 6 one trade (+463.2%). A single large win does not rehabilitate the arm. Retired.
- **14-day expiry (any strike):** bundle 3 median −95%, bundle 5 two trades both −100%, bundle 6 three trades all negative. Dropped.
- **At-the-money 30-day calls:** mixed and too small. Dropped.
- **Calls on spike-and-no-trend names, and oversold dip-buying with calls:** dropped as option strategies. The stock-level oversold idea survives only as test 2 in section 3.
- **Stacking more than three filters on fewer than 40 trades:** overfitting risk. Dropped.
- **Market 20-day > 0 gate for 90-day calls:** two trades in bundle 5, no conclusion. Dropped.
- **News tone as a filter:** did not separate winners from losers in bundles 4, 5, or 6. Dropped as a filter. News presence appears among both tail winners and tail losers.

### 4.4 Still on paper, not evidence

- **90-day, 5% above:** bundle 5 n=2 (+68.9%, −23.0%), bundle 6 n=3 (median +4.5%, average −2.5%). Logged, not weighted.
- **Price band (under $10 / $10–50 / over $50):** winners and losers in each band across bundles. Confidence: low.

### 4.5 Caveats

- Six bundles with roughly 25 to 45 option trades each, and most structures with fewer than 10 trades. This cannot establish an option edge in either direction.
- The average option result is driven by a few trades. The median has been negative in five consecutive bundles.
- Bundle 6's positive dollar total is a single bundle. It is not enough to overturn the median evidence.
- Premium has never been logged, so I cannot separate a wrong direction from a bad wrapper, and cannot test break-even directly.
- The tail test has not been run in any bundle, because the candidate-level table has not been provided. Any tail-rate claim must come from the full table.

### Agent 3's final notes (not passed on)

# TRADING NOTES: FINAL (after bundle 6 of 6)

## 1. CURRENT STRATEGY AND RULES

### 1a. Live trading status: options still banned
- **No live option trades.** The live gate requires (a) a positive average in at least 3 fresh bundles, (b) 40+ trades, and (c) a median no worse than about -30%.
- **Current status:** 2 of 6 bundles positive (bundle 1 +29.7%, bundle 5 +20.3%). Bundle 6 was -$1,328 on 43 trades, average -3.1%, median -6.9%. Positive bundles: 2 of 6 (only 1 of the last 3). Median test: passed in bundle 5 (-13.5%) but failed in bundle 6 (-6.9% is better than -30%, so it technically passes) and remains very negative pooled.
- **Honest read:** the option book has been positive in only one of the last three bundles, and that bundle's profit was concentrated in outliers. The live gate is not close.

### 1b. The option wrapper
- Over 10 sessions, the average stock in this universe moved only +0.7% (median +0.5%, bundle 6). Option trades averaged -3.1% in the same window. The wrapper, not the stock direction, is the main drag.
- Short-dated (14d, 30d) and far out-of-the-money structures lose premium quickly. They are banned.
- Results are highly skewed. A few trades in the +100% to +160% range carry the book in good bundles, and a large group of -50% to -100% losses carries it in bad ones.

### 1c. Paper-trade structures (not live)

| Structure | Status | Evidence |
|---|---|---|
| **90d, +5% strike, hold 10** | **Paper candidate (only one left)** | Bundle 6: 17 trades, +8.6% average, +4.5% median. Bundle 5: 8 trades, +2.7% avg, -1.8% median. Bundle 4: 3 trades, about -34% avg. Pooled 28 trades: roughly +2.5% average (median not reliably computed). Positive in 2 of 3 bundles, but the earlier bundle result was poor and the sample is small. |
| 90d, +10% strike, hold 10 | **Dropped** | Bundle 6: 22 trades, -9.3% avg, -19.5% median (the largest sample so far). Pooled with bundles 4 and 5 (26 trades) the average is about zero and the median is negative. Bundle 5's +62% average came from 3 trades. |
| 90d, +20% strike, hold 10 | **Banned** | Bundle 6: 3 trades, -36.5% average, -34.2% median. |
| 90d, 0% strike, hold 10 | **Dropped** | Bundle 6's single +33.8% trade is n=1. Bundle 5: 11 trades, -13.8% avg, -29.4% median. Pooled median about -30%. |
| 30-day, any strike | **Banned** | Pooled 30d 0%: about -14% average over 14 trades. Pooled 30d +5%: about -33% over 13 trades. |
| 14-day, any strike | **Banned** | Only one large win (n=1). Other trades lost heavily. |
| Double-or-10 exit | **Dropped** | Failed in bundle 4; not re-tested. |

### 1d. Exit
- **Hold 10 sessions** for all paper comparisons.
- Do not change exit timing to rescue a losing entry.

### 1e. Price band
- Option paper trades only in **$10–50** and **over $50**. Sub-$10 option trades excluded.
- Stock-side logging continues for all bands.
- Bundle 6 showed the largest stock-side swings in the sub-$10 band, in both directions (see section 2c). Price band alone is not a rule. Sub-$10 stocks produced the largest stock-side losses and gains.

### 1f. Ratings: no usable edge, do not trade on them
- **+1 vs -1 (bundle 6):** +1 averaged +2.4% (median +1.1%); -1 averaged -0.7% (median +0.5%). In bundle 5 the ordering reversed on average (-1 +3.1% vs +1 +2.4%) while +1 had the higher median. The sign has flipped across bundles.
- **+0:** averaged -1.2% (median 0.0%) in bundle 6, the weakest group in that bundle.
- **-2 (dropped as a short signal):** Bundle 6 showed +55.1% average (median +5.8%) across 5 stocks, driven by one +221% name. Pooled across bundles 4–6 (16 stocks), the -2 group has been positive on average, which contradicts the earlier "weak negative" read. The group is too small and too skewed to act on. Do not short or avoid -2 names on this basis.
- **Conclusion:** ratings are not an input to entries, sizing, or exits.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

**Bundle 6 (fresh universe, 249 candidates).** Universe average +0.7%, median +0.5%.

### 2a. Option results by structure (bundle 6)

| Structure | Trades | Average | Median |
|---|---|---|---|
| 90d, +5%, hold 10 | 17 | +8.6% | +4.5% |
| 90d, +10%, hold 10 | 22 | -9.3% | -19.5% |
| 90d, +20%, hold 10 | 3 | -36.5% | -34.2% |
| 90d, 0%, hold 10 | 1 | +33.8% | +33.8% (n=1) |
| **All** | **43** | **-3.1%** | **-6.9%** (42% winners) |

**Read:**
- The 90-day +5% strike was the only structure with a positive average and median this bundle, and the first to show a positive median across two bundles.
- The 90-day +10% strike, which I had as a paper candidate, failed on the largest sample so far. It is dropped.
- Option winners and losers both appear across RSI and price bands. In the +10% and +5% groups, the biggest winners (+35% to +165%) included both oversold names (RSI 35–42, 20-day declines) and extended names (RSI 67–68, 20-day gains of +4% to +9%). The biggest losers (-49% to -100%) also included oversold names (RSI 17–19) and mid-RSI names. No clean separation.

### 2b. Ratings (bundle 6)

| Rating | Stocks | Average | Median |
|---|---|---|---|
| +2 | 1 | -5.7% | -5.7% |
| +1 | 41 | +2.4% | +1.1% |
| +0 | 102 | -1.2% | 0.0% |
| -1 | 100 | -0.7% | +0.5% |
| -2 | 5 | +55.1% | +5.8% |

Ratings remain without edge (see 1f).

### 2c. Stock-side extremes (biased, hypotheses only)

These lists show only the biggest moves, so they are not a full-sample test.

- **Biggest winners (+27% to +221%):**
  - Mostly sub-$10 or $10–50 names. Two of the biggest winners were at or near $10–50 with large 20-day gains (+124%, +35%).
  - One of the largest winners (+221%) was deeply oversold (20-day -64%, RSI 32, 1-day -32%, heavy news 1d/3d/7d: 3/3/5). Rated -2.
  - Another (+82%) was parabolic (20-day +124%, vs ma50 +86%, vol20 12%). Rated -2.
  - Several winners had vol20 of 4–13%.
- **Biggest losers (-22% to -58%):**
  - Almost all sub-$10 or $10–50. Mostly rated -1, 0, or -2.
  - Two patterns: (a) sub-$10 names with huge call spikes (calls 1,318x normal, 1-day +40%) that reversed; (b) sub-$10 names already down 20–50% over 20 days that kept falling (-52% 1-day, -55% 20-day, rated -2).
  - Some losers rallied first (5-day +12% to +27%, 1-day +10% to +12%) then gave it back.
  - Volatility was high (vol20 4–14%).
- **Takeaway:** high volatility and sub-$10 price were the most common features of both the extreme winners and losers. Oversold and parabolic names appeared on both sides. Nothing here is a rule.

### 2d. Planned stock-side splits: still NOT tested
The bundle 6 report, like bundle 5, gave forward stock returns only in aggregate (by rating) and for the extremes. It did not give each candidate's 10-session return, so the planned splits could not be run:
- Market gate (market 20d above vs below zero).
- Extension (vs ma20 > +6 and 20d > +9), with a parabolic sub-split.
- Oversold (RSI < 30 or 20d < -10), under $50.
- Volatility bands (below 2%, 2–4%, above 4%).
- 5-day move ceiling and floor.

These remain open. I will not act on any of them until the per-candidate data arrives.

---

## 3. WHAT I WILL TRY NEXT

1. **Per-candidate stock returns, required.** Each candidate's 10-session forward return must come with the candidate's columns. Without this, no split is testable. This was requested in bundle 5 and not delivered in bundle 6.
2. **Stock-side splits, in this order, with minimum group sizes:**
   - Market gate: 30+ candidates in each group.
   - Extension, then parabolic sub-split (20d > +30 or vs ma20 > +20).
   - Oversold (RSI < 30 or 20d < -10), under $50 only.
   - Volatility bands, reporting average and median separately.
   - 5-day move ceiling and floor.
   Report the count in each group. **No option trades on any split until the stock-side result is clear.**
3. **Paper options: 90-day, +5% strike, hold 10 only.** Target 15+ trades per price band ($10–50 and over $50) before judging. For each trade, log the option return next to the same stock's 10-session return, so time decay and direction are separated. The question: does the +5% option beat the stock's own return after premium cost?
4. **Keep dropped structures out of the book:** 90-day +10%, +20%, and 0%; all 30-day and 14-day structures.
5. **Live gate unchanged:** no live option trades until 3+ positive fresh bundles, 40+ trades, and a median no worse than -30%.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Option book by bundle

| Bundle | Trades | Result | Read |
|---|---|---|---|
| 1 | 18 (old primary) | +29.7% average | Not replicated |
| 2 | 18 (old primary) | -34.7% average | Not replicated |
| 3 | 32 | -$13,440, 19% winners | Loss |
| 4 | 38 | -$17,934, 13% winners, median -57% | Loss |
| 5 | 43 | +$8,712, 42% winners, average +20.3%, median -13.5% (about +0.4% ex two outliers) | Positive but concentrated |
| 6 | 43 | -$1,328, 42% winners, average -3.1%, median -6.9% | Loss |

### Pooled structure evidence (bundles 4–6)

| Structure | Pooled trades (approx.) | Read |
|---|---|---|
| 90d, +5%, hold 10 | 28 | Positive average (about +2.5%) in 2 of 3 bundles; paper candidate |
| 90d, +10%, hold 10 | 26 | Average near zero, median negative; dropped |
| 90d, +20%, hold 10 | 4 | Negative; banned |
| 90d, 0%, hold 10 | 21 | Median about -30% in bundle 5; dropped |
| 30d, 0% or +5%, hold 10 | ~27 | Negative; banned |
| 14d, any strike | ~4 | Banned |

### Dropped or banned
- **Live option trades:** banned until the criteria in 1a are met.
- **90-day +10% and +20% strikes:** dropped or banned after bundle 6.
- **90-day 0% strike:** dropped.
- **30-day and 14-day structures:** banned.
- **Double-or-10 exit:** dropped.
- **Ratings as an input (including -2 as a short or avoid signal):** dropped. -2 pooled results are positive, not negative.
- **Sub-$10 option trades:** excluded. Stock-side logging continues.
- **Oversold dip-buying with calls:** banned as an option structure. The stock-side test is still open.
- **Parabolic names as automatic avoids:** not assumed. The stock-side test decides.
- **Profit-driven size increases:** none. Bundle 5's profit was concentrated, and bundle 6 was a loss.

### Confidence
- **Option wrapper on short expiries (14d, 30d):** high confidence it loses on the median.
- **90-day +5% strike, hold 10:** low to moderate. Positive in 2 of 3 recent bundles, but the sample is about 28 trades and the earlier bundle was negative. Paper only.
- **90-day +10%, +20%, 0%:** dropped or banned; the evidence is consistent with losses on the median.
- **Ratings:** no predictive value demonstrated. The -2 signal reversed.
- **Stock-side signals (extension, oversold, market gate, volatility, 5-day move):** unknown. Not testable from the data provided so far.
- **Universe average return:** about +0.5% to +2.7% over 10 sessions across bundles 2–6, with a negative result in bundle 3. Expect small stock moves. Judge every option structure against that baseline, and against the same stock's own move.

### Agent 4's final notes (not passed on)

# TRADING PLAYBOOK (updated after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Bottom line:** I have one option structure with a repeatable signal, **Setup C**: a 30-day call with a strike about 10% above the entry price, taken only when the stock has already run hard and sits well above its 50-day average, held 10 sessions. Across three fresh bundles (5 and 6 out-of-sample, plus the pooled earlier bundles), gate-passing trades have been positive far more often than the ungated control. Confidence is moderate. The sample is small, the premium cost is still unlogged, and the largest winners drive the averages. **Real money stays at zero.** Everything else stays on paper or is dropped.

### Structure status

| Structure | Status | Evidence | Notes |
|---|---|---|---|
| **C: 30-day call, strike ~10% above, momentum-gated, hold 10** | **Lead candidate, paper only** | About 20 trades pooled (bundles 2 to 6). About 15 positive. Average roughly +100% to +150% (approximate); median positive. | Bundle 6 added 4 passers: 3 winners, 1 loss. Reaches the 20-trade count but fails the premium-logging condition. |
| Ungated 30-day call, strike ~10% above, hold 10 | Paper control | About 100 trades across bundles 2 to 6. Median negative in most bundles. | Bundle 6: 33 trades, average +14.5%, median -82.7%. The gate-vs-control gap is the main evidence that C is not just the structure. |
| B: 90-day call, strike ~10% above, trend and news gated, hold 10 | Paper only | About 31 trades, average roughly -10%, median negative. | One bundle 6 trade (-33.7%). Gate has not separated winners from losers in bundles 3, 4, or 6. |
| A: 30-day call, strike ~5% above, trend and news gated | Dropped | About 47 trades, average roughly -20%. | Bundle 6 had 5 trades at 5%, with a median well negative. Not a structure to trade. |
| 30-day 20% and 15% strikes, 30-day at-the-money, 14-day expiries, double-or-10 exits | Dropped | Few trades, mostly negative. | Bundle 6: 30-day 20% strike 2 trades, average -36%. The single 14-day at-the-money +628% trade is noted as an outlier, not evidence. |

### Setup C rules

- **Entry (entry-day row, all required):**
  - `20d % > 20` (strict; a value of exactly 20.0 is logged as a boundary case, not a trade)
  - `vs ma50 % > 15` and not blank
- **Instrument:** call, 30-day expiry.
- **Strike:** about 10% above the price at entry.
- **Exit:** close after 10 sessions. No stop. No double-or-10 exit.
- **Sizing:** paper only. Log every column for each trade.
- **Required logging:** the call premium paid as a percent of the stock price (or an implied-volatility proxy) on every C and control trade. This field is still missing and blocks real-money review.

### Why I believe the gate (and how confident I am)

- Passers are stocks that have run hard over 20 sessions and sit well above their 50-day average, often with heavy call buying (call days 2x+ over 20 sessions of 2 to 10).
- The gate passed 6 of 6 in bundle 5 and 4 of about 33 in bundle 6. Passers in both bundles were mostly winners. Non-passers in the same structure were mostly -100% or near it. Same structure, same hold, same bundle: the gate is selecting something.
- Confidence: **moderate** that the gate selects better odds. **Low** that the edge is large or stable at real size, because it rests on about 20 trades, a few very large winners, and no premium data.

### Real-money review rule (unchanged)

Real money opens for C only when all of these hold:
1. At least 20 paper trades that pass the C entry rules.
2. Median and average are both positive.
3. No single trade accounts for more than one-third of the total gain across the 20 trades.
4. The premium cost has been logged for every trade.

If the review passes, start at one-quarter of my previous standard size, with total open premium capped at one standard trade's worth. If it fails, drop the option structure and keep only stock-side research.

**Status after bundle 6:**
- Condition 1: met or essentially met (about 20 pooled qualifying trades).
- Condition 2: met (median and average positive, approximately).
- Condition 3: appears met on a percentage basis. The largest single return (about +625%) is roughly a fifth of the summed pooled percentage gain. I cannot check the dollar-weighted version because position sizes per trade are not in this record.
- Condition 4: **not met.** Premium cost has not been logged on any trade.

**Decision: no real money.** The rule fails on condition 4 regardless of the other three.

### Sizing and risk, all option trades

- Expect most option trades to go to zero. Premium must be affordable at -100%.
- No option structure is real-money eligible until its own review passes.

## 2. WHAT I TESTED IN BUNDLE 6

### Results (48 trades, +$10,912 total, average +22.7%, median -70.5%, 25% winners)

- **Ungated 30-day 10% hold 10 (control):** 33 trades, average +14.5%, median -82.7%.
- **Gate-passing trades (C):** 4 trades identified in the detail rows. Returns: about +426%, +463%, +625%, and -100%. Three winners, one total loss. The -100% passer had 20d % of 20.6 (just over the threshold) and vs ma50 % of 18.4 (just over the threshold). It was the closest-to-line passer and it lost.
- **Non-passers in the same structure:** about 29 trades, mostly -100% or near it. The gate again separated the groups.
- **Market context:** all four passers were in up-markets (market 20d % between +0.9 and +4.8). No down-market trades, so the down-market test did not advance.
- **Other structures:**
  - 30-day 5% hold 10: several trades, with +69.7%, +136%, and +427% winners. None passed the C gate (20d % 6 to 13, vs ma50 % 7 to 14). These are winners outside the gate.
  - 14-day at-the-money: one +628% trade, with 20d % 9.4 and vs ma50 % 7.8. Outside the gate. Single trade.
  - 30-day 20% strike: 2 trades, average -36%.
  - 90-day 10% strike: one trade, -33.7%.

### Ratings (bundle 6)

- Rated +2: 2 stocks, average +0.3%.
- Rated +1: 60 stocks, average +2.7%, median +0.1%.
- Rated +0: 112 stocks, average -1.9%, median -0.2%.
- Rated -1: 73 stocks, average +3.4%, median +1.4%.
- Rated -2: 2 stocks, average -9.8%.

**Ratings still do not order outcomes.** This bundle, rated -1 beat rated +1 and rated +0 on both average and median. The rated -2 pattern, which had been mixed, is now weaker still on just two stocks. Ratings are dropped from entries, exits, and sizing.

### Stock-side baseline (249 candidates)

- Average +0.7%, median +0.5% over 10 sessions. Essentially flat.
- The largest stock losers and winners both had large 20-day moves, high vol20, and spike-no-news flags, with no clear separating feature. Some large losers were stocks that had already run up sharply (20d % well above 20, price falling 30% to 60% within the window). That is the same risk C's exit has to handle.

### Filter and feature notes

- **News 7d:** the four passers did not separate on news 7d (values 0 and 1 in the detail rows). Paper log only.
- **RSI, vol20, days since spike, spike-no-news, puts ratio:** no separation I can identify. Still dropped as entry filters.
- **Near-miss tracking (20d % 18 to 22):** the passer at 20.6 is the only in-band row with a passing vs ma50 %. It lost. One data point; not a conclusion about the threshold. Keep the cutoff as is.

## 3. WHAT I WILL TRY NEXT

1. **Keep paper-trading Setup C on every qualifying candidate.** The count is now about 20 pooled, but the review cannot start until premium is logged. Keep logging trades past 20; the review should be re-run on a fixed set rather than on a moving count.
2. **Start logging premium cost on every C and control trade, immediately.** This is the most important missing field. It is the only thing that decides whether the review can ever pass. Priority question: is the premium rich relative to the stock's 10-session move, and does that differ between passers and non-passers?
3. **Keep the ungated 30-day 10% control running.** The control's median is still strongly negative (bundle 6: -82.7%). The gap between gated and ungated is the core evidence.
4. **Log the 10-session stock return for every C and control trade.** Without it I cannot separate direction from premium decay. Passers that lose 100% with a stock that rose is a premium-decay problem; passers that lose 100% with a stock that fell is a direction problem. Both matter.
5. **Near-miss tracking (20d % 18 to 22).** Keep logging the boundary flag and the 20-session stock return. Do not change the threshold. The bundle 6 near-miss-passer lost, so the cutoff is not obviously sharp.
6. **Down-market test on C.** Still only 2 down-market trades pooled (both winners). Need 8 or more. Log market 20d % < 0 separately.
7. **News 7d.** Paper log only: news 7d = 0 vs ≥ 1 for C and the control. Not a filter until it separates in at least two bundles.
8. **Rated -2 and ratings generally:** no further testing. Ratings are not part of the strategy.

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Pooled evidence (approximate)

| Structure | Bundles | Trades | Approx. average | Median | Notes |
|---|---|---|---|---|---|
| C (30-day 10%, momentum-gated) | 2 to 6 | ~20 | Roughly +100% to +150% | Positive | About 15 of 20 positive. Bundle 3 was the only losing bundle. Bundle 6: 3 of 4 positive. |
| Ungated 30-day 10% (control) | 2 to 6 | ~100 | Near zero to positive | Negative | Bundle 6 average +14.5%, median -82.7%. The average is carried by a few big winners. |
| 90-day 10% (B) | 1 to 6 | ~31 | About -10% | Negative | Not gate-separated. |
| 30-day 5% (A) | 1 to 6 | ~47 | About -20% | Negative | Dropped. Winners exist outside the gate. |

Averages are approximate; pooled medians are directional only.

### What held up

- **The gate-vs-control gap** held in bundles 5 and 6 (out-of-sample on both): passers far outperformed non-passers in the same structure.
- **Large winners cluster in stocks that have already run hard** (20d % and vs ma50 % high). Consistent across bundles 2, 4, 5, and 6 for gated and some ungated rows.

### What failed or is weakening

- **Gate reliability at the margin.** The bundle 6 passer just over both thresholds lost. Passers are not guaranteed winners; the gate changes odds, not outcomes.
- **Winners outside the gate exist.** Bundle 6 had +427%, +136%, and +628% trades that did not pass C's rules. The gate is a partial description of where option winners come from.
- **Ratings** as any kind of signal: no consistent ordering across bundles.
- **Rated -2 pattern:** mixed, now further weakened.
- **Winners are tail-driven.** The average depends on a few very large returns. The median is what I trust most, and it is positive only on a pooled basis. The control median is negative in most bundles.

### Ideas dropped or downgraded

- **Setup B as a live setup.** Remains on paper only.
- **Setup A (30-day 5%, trend and news gated).** Dropped.
- **News 7d ≥ 1 as an entry gate.** Not separating. Paper log only.
- **Ratings** as an entry, exit, or sizing signal. Dropped.
- **Price band as a filter.** Winners and losers in every band. Dropped.
- **Puts-ratio extremes as a directional signal.** Dropped.
- **RSI, vol20, days since spike, spike-no-news as entry filters.** No separation. Dropped.
- **30-day 20% and 15% strikes, 30-day at-the-money, double-or-10 exits, 14-day expiries.** Dropped.

### Open questions

- Does C's gate select stocks that keep moving, or stocks where the premium is cheap relative to the move? Needs premium cost on every trade.
- Does C hold in a down-market? Two trades pooled, both winners. Need 8 or more.
- Is the 20-day threshold a real break? Near-miss tracking will show whether 18 to 22 behaves like the passers.
- Does any structure reach a positive median over 20 or more trades in fresh stocks, with premium logged? C may, but the evidence is not yet at the bar for real money.
- Do the largest winners share a feature I have not tested? The gate catches many of them, not all.


## Generation 3

### Editor's rules, tested on all training months and bundles

- Trend+news+over50 30d 5% OTM (when vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 143 trades, average +23.4% (95% range -5.7% to +56.8%, resampling whole weeks), median -41.3%, 38% winners. Buying every candidate the same way: -12.2%. Beat that in 4 of 6 bundles; first half of the months +23.8%, second half +23.1%.
- Momentum 30d 10% OTM (when 20d % > 20 and vs ma50 % > 15: buy the 30-day call 10% above the price, exit hold10): 211 trades, average +26.2% (95% range -6.0% to +61.0%, resampling whole weeks), median -57.4%, 30% winners. Buying every candidate the same way: -17.7%. Beat that in 6 of 6 bundles; first half of the months +11.9%, second half +35.9%.
- Above ma50 up market 90d 10% OTM (when vs ma50 % > 0 and market 20d % > 0: buy the 90-day call 10% above the price, exit hold10): 183 trades, average +3.3% (95% range -10.7% to +17.6%, resampling whole weeks), median -16.1%, 38% winners. Buying every candidate the same way: -9.7%. Beat that in 5 of 6 bundles; first half of the months +0.5%, second half +4.6%.
- Over50 trend news up-market 90d 5% OTM (when price = >$50 and vs ma50 % > 0 and market 20d % > 0 and news tone 7d > 0: buy the 90-day call 5% above the price, exit hold10): 22 trades, average -13.9% (95% range -29.0% to -0.4%, resampling whole weeks), median -13.2%, 36% winners. Buying every candidate the same way: -7.4%. Beat that in 1 of 3 bundles; first half of the months -28.3%, second half -1.9%.
- Quiet after spike 30d ATM (when days since spike >= 20 and calls 5d avg < 1: buy the 30-day call 0% above the price, exit hold10): 117 trades, average +10.1% (95% range -19.8% to +48.3%, resampling whole weeks), median -37.9%, 34% winners. Buying every candidate the same way: -10.9%. Beat that in 2 of 6 bundles; first half of the months +20.3%, second half +1.6%.
- Overbought chase 30d ATM (when rsi > 70 and vs ma20 % > 10: buy the 30-day call 0% above the price, exit hold10): 233 trades, average +4.8% (95% range -17.3% to +29.0%, resampling whole weeks), median -46.7%, 32% winners. Buying every candidate the same way: -10.9%. Beat that in 4 of 6 bundles; first half of the months -0.7%, second half +10.3%.
- Call-flow trend 90d 5% OTM (when calls 5d avg > 1 and vs ma50 % > 0: buy the 90-day call 5% above the price, exit hold10): 224 trades, average -2.5% (95% range -11.4% to +5.2%, resampling whole weeks), median -20.5%, 39% winners. Buying every candidate the same way: -7.4%. Beat that in 5 of 6 bundles; first half of the months -0.5%, second half -3.9%.

### The same rules on the blind scoring months (never shown to agents)

- Trend+news+over50 30d 5% OTM (when vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 89 trades, average -7.8% (95% range -40.0% to +30.7%, resampling whole weeks), median -56.2%, 28% winners. Buying every candidate the same way: -19.8%. Beat that in 3 of 6 bundles; first half of the months +17.1%, second half -24.8%.
- Momentum 30d 10% OTM (when 20d % > 20 and vs ma50 % > 15: buy the 30-day call 10% above the price, exit hold10): 167 trades, average -22.6% (95% range -42.9% to -1.0%, resampling whole weeks), median -61.4%, 25% winners. Buying every candidate the same way: -20.6%. Beat that in 2 of 6 bundles; first half of the months -16.1%, second half -29.1%.
- Above ma50 up market 90d 10% OTM (when vs ma50 % > 0 and market 20d % > 0: buy the 90-day call 10% above the price, exit hold10): 159 trades, average -11.1% (95% range -20.0% to +0.3%, resampling whole weeks), median -24.8%, 26% winners. Buying every candidate the same way: -7.8%. Beat that in 2 of 6 bundles; first half of the months -11.8%, second half -10.3%.
- Over50 trend news up-market 90d 5% OTM (when price = >$50 and vs ma50 % > 0 and market 20d % > 0 and news tone 7d > 0: buy the 90-day call 5% above the price, exit hold10): 32 trades, average -6.9% (95% range -28.3% to +11.7%, resampling whole weeks), median -15.1%, 34% winners. Buying every candidate the same way: -7.1%. Beat that in 2 of 4 bundles; first half of the months -25.3%, second half +7.4%.
- Quiet after spike 30d ATM (when days since spike >= 20 and calls 5d avg < 1: buy the 30-day call 0% above the price, exit hold10): 53 trades, average -20.2% (95% range -41.0% to +3.9%, resampling whole weeks), median -34.3%, 26% winners. Buying every candidate the same way: -14.7%. Beat that in 3 of 6 bundles; first half of the months -19.7%, second half -20.8%.
- Overbought chase 30d ATM (when rsi > 70 and vs ma20 % > 10: buy the 30-day call 0% above the price, exit hold10): 191 trades, average -19.9% (95% range -34.2% to -3.9%, resampling whole weeks), median -47.0%, 28% winners. Buying every candidate the same way: -14.7%. Beat that in 1 of 6 bundles; first half of the months -21.5%, second half -18.3%.
- Call-flow trend 90d 5% OTM (when calls 5d avg > 1 and vs ma50 % > 0: buy the 90-day call 5% above the price, exit hold10): 177 trades, average -8.8% (95% range -18.8% to +3.1%, resampling whole weeks), median -20.6%, 30% winners. Buying every candidate the same way: -7.1%. Beat that in 3 of 6 bundles; first half of the months -11.1%, second half -6.3%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

(Committee editor's synthesis of four independent traders over six bundles. Where a trader's figure and the code-tested scorebook differ, the scorebook is used. All returns are per-trade option returns on premium. "Benchmark" means buying every candidate with the same expiry, strike and exit.)

## 0. Bottom line

**What the code says**
- Almost every call rule has a negative median, usually -15% to -60%, with 25% to 45% winners.
- Averages come from a minority of large winners. Judge a rule by three things: its average against its same-structure benchmark, the number of bundles that beat the benchmark, and whether both halves of the sample agree.
- The scorebook found no rule that was a safe edge. A few rules show positive averages with stable halves and wide ranges that only just touch zero. Those are the real leads.

**Where the traders and the code disagreed**
- All four traders ended the round paused or paper-only, saying "no edge, wrapper cost is large". The wrapper cost is real and well documented: options lose on median even when the stock is flat. The universe's 10-session stock median sat between -1.2% and +0.7%.
- Several traders dropped trend, news and price-band filters because the extremes lists (best and worst names) showed the same features on both sides. The full-sample code tests contradict them. Extremes lists are not evidence, and several trend, news and over-$50 filters beat their benchmarks in 4 to 6 of 6 bundles.
- Agent 2 retired 90-day calls and Agent 4 banned 30-day at-the-money calls. The code shows both are near benchmark or better when filtered by trend. The unfiltered versions are what lose.
- The traders banned 10%-out-of-the-money strikes based on n=2 to 5 trades. The code shows the best average of any rule is a 30-day call 10% above the price in a momentum setup (n=211). It has a terrible median, so it is a lottery ticket, but the ban was not supported at scale.
- Agent 1 championed price bands, trend and market filters, and the code largely backs them. Agents 2, 3 and 4 treated them as noise.

**Benchmarks for every structure (hold 10 sessions)**

| Structure | Benchmark average |
|---|---|
| 30-day at-the-money call | -10.9% |
| 30-day call 5% above price | -12.2% |
| 30-day call 10% above price | -17.7% |
| 90-day at-the-money call | -8.4% |
| 90-day call 5% above price | -7.4% |
| 90-day call 10% above price | -9.7% |
| 30-day, double-or-10 exit | -12.0% |

**The stable pattern (supported by many rules and bundles)**
1. Trend helps. Stock above its 50-day average, positive 20-day momentum, and market 20d % above zero all push results toward or above the benchmark.
2. Price over $50 is the best band. $10 to $50 is the worst. Under $10 is poor and produces most of the -100% outcomes.
3. Positive news tone helps.
4. Dip-buying, oversold entries, high-volatility call spikes, and call spikes without trend or news lose.
5. Most first-half results beat second-half results. A market regime effect is plausible but untested.

## 1. STRATEGY: setups worth trading (small flat size, or paper)

All rules buy on the entry day and exit after 10 sessions. They are "least bad, worth refining". Every one has a negative median except where noted. Size flat and small, and assume any option can go to -100%. Do not add after wins.

Rules are listed with the exact conditions used, so the next generation can restate them and have them scored.

### 1A. Tier 1: positive average with stable halves, or beat the benchmark in 5 to 6 of 6 bundles

**1. Trend + news + over $50, 30-day call 5% above price** (Agent 2's "Setup A" turned into an option proxy; the code confirmed it)
- Rule: vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price over $50.
- Scorebook: 143 trades, average **+23.4%** (95% range -5.7% to +56.8%), median -41.3%, 38% winners. Benchmark -12.2%, beat in 4 of 6 bundles.
- Halves: +23.8% and +23.1%, the most even halves of any rule.
- Agent 2 designed it as a stock-side filter and never got per-candidate rows. The option version is the only evidence we have.

**2. Trend + news, all price bands, 30-day call 5% above price**
- Rule: vs ma50 % > 0 and 20d % > 0 and news 3d > 0.
- Scorebook: 306 trades, average +11.3% (range -10.9% to +35.0%), median -51.1%, 29% winners. Beat the -12.2% benchmark in 4 of 6 bundles. Halves +11.3% and +11.3%.
- Adding "over $50 and news tone" (rule 1) roughly doubles the average. This points to price band and news tone as the useful add-ons.

**3. Momentum, 30-day call 10% above price**
- Rule: 20d % > 20 and vs ma50 % > 15.
- Scorebook: 211 trades, average **+26.2%** (range -6.0% to +61.0%), median -57.4%, 30% winners. Benchmark -17.7%. **Beat it in 6 of 6 bundles.** Halves +11.9% and +35.9%.
- This has the best bundle record and the second-best average. It is a tail-driven lottery: the median trade loses more than half the premium. Size very small.
- It contradicts the traders' blanket ban on 10% out-of-the-money strikes. The ban holds for 14-day expiries and for non-trend setups (see section 2).

**4. Stock above ma50 in an up market, 90-day call 10% above price** (Agent 1's idea, code-confirmed)
- Rule: vs ma50 % > 0 and market 20d % > 0.
- Scorebook: 183 trades, average +3.3% (range -10.7% to +17.6%), median -16.1%, 38% winners. Benchmark -9.7%. Beat it in 5 of 6 bundles. Halves +0.5% and +4.6%.
- This is the most stable and least volatile positive result. Its median is much better than the 30-day tail rules.
- **The market gate is the point.** The same stock condition in a down market (market 20d % < 0) averaged -12.9% over 78 trades (range -26.1% to +0.2%), beat the benchmark in 2 of 6 bundles, and halves were -4.4% and -23.9%.

**5. Full filter stack, over $50, 90-day call 10% above price**
- Rule: calls 5d avg > 1 and vs ma50 % > 0 and market 20d % > 0 and price over $50.
- Scorebook: 42 trades, average +7.0% (range -16.7% to +27.0%), median **-8.0%**, 45% winners. Benchmark -9.7%. Beat it in 4 of 6 bundles. Halves -8.3% and +13.9%.
- The same stack at $10 to $50: 63 trades, -4.2% (range -21.0% to +15.7%), median -19.6%, 35% winners, beat in 4 of 6, halves -19.5% and +2.5%. The over-$50 band is clearly better.

**6. Broad call base in an uptrend, 90-day call 5% above price**
- Rule: calls 5d avg > 1 and vs ma50 % > 0.
- Scorebook: 224 trades, average -2.5% (range -11.4% to +5.2%), median -20.5%, 39% winners. Benchmark -7.4%. Beat it in 5 of 6 bundles. Halves -0.5% and -3.9%.
- This is the same filter as Agent 3's 30-day call-flow trend rule:
  - 30-day call 5% above: 844 trades, +1.0% (range -12.7% to +16.2%), median -54.1%, beat in 5 of 6 bundles, halves +6.0% and -2.5%.
  - 30-day at the money: 847 trades, -3.8%, median -37.1%, beat in 5 of 6 bundles, halves -0.5% and -6.2%.
- The 90-day version has the better median and win rate. The 30-day version has the better average.

**7. Over $50, plain price filter**
- 30-day at-the-money call: 700 trades, -1.7% (range -11.1% to +9.2%), median -29.4%, 37% winners. Beat the -10.9% benchmark in 5 of 6 bundles. Halves +4.7% and -7.9%.
- 90-day call 5% above: 198 trades, -3.8% (range -13.8% to +5.2%), median -16.5%, 40% winners. Beat the benchmark in 4 of 6 bundles.
- 90-day at the money over $50: about the benchmark (-8.0%, 190 trades). Price band alone adds little at 90 days.

**8. Positive news tone, 30-day at-the-money call**
- Rule: news tone 7d > 0 and news 3d > 0.
- Scorebook: 432 trades, -0.1%, median -35.0%, 34% winners. Beat the benchmark in 5 of 6 bundles. Halves +8.6% and -10.8%.

### 1B. Tier 2: positive or near-benchmark, but with smaller n or unstable halves

- **Overbought chase, 30-day at-the-money call.** Rule: RSI > 70 and vs ma20 % > 10. Scorebook: 233 trades, +4.8% (range -17.3% to +29.0%), median -46.7%, 32% winners, beat in 4 of 6 bundles. Halves -0.7% and +10.3%.
  - Related 30-day call 5% above, with 20d % > 20 and RSI > 75: 131 trades, +4.5%, median -55.8%, beat in 3 of 6 bundles, halves -20.6% and +33.3%. This is unstable.
  - Related 90-day at the money, with 20d % > 20 and vs ma20 % > 15: 61 trades, -11.1%, beat in 3 of 6 bundles. It is bad at 90 days, so overbought chasing only works at 30 days with strikes at or near the money.
- **Momentum, 90-day call 5% above.** Rule: 20d % > 10. Scorebook: 174 trades, -1.0% (range -12.9% to +12.5%), median -22.2%, beat in 4 of 6 bundles. Halves +4.6% and -5.1%.
- **Market and stock both up, 90-day at the money.** Rule: market 20d % > 0 and vs ma50 % > 0. Scorebook: 184 trades, -3.2%, median -19.8%, 34% winners, beat in 4 of 6 bundles.
- **Call activity trend, 90-day at the money.** Rule: calls 5d avg > 1 and call days 2x+ ≥ 2 and vs ma50 % > 0. Scorebook: 144 trades, -6.9% (range -17.5% to +4.0%), median -19.8%, 40% winners. Beat the -8.4% benchmark in 4 of 6 bundles.
- **Strong stock with a call spike, 30-day at the money.** Rule: calls ≥ 3 and vs ma20 % > 0. Scorebook: 565 trades, -4.1%, median -39.0%, beat in 4 of 6 bundles. Trend is what makes the spike tolerable.
- **Quiet after a spike, 30-day at the money.** Rule: days since spike ≥ 20 and calls 5d avg < 1. Scorebook: 117 trades, **+10.1%** (range -19.8% to +48.3%), median -37.9%, beat in only 2 of 6 bundles. Both halves positive (+20.3% and +1.6%). This is a "buy before the crowd" lead.
- **Spike aged 20+ days in a trend, 90-day call 10% above.** Rule: days since spike ≥ 20 and vs ma50 % > 0 and 20d % > 0. Scorebook: only 7 trades, +109%. Too small to trust, but it fits the "before the crowd" lead.

### 1C. Weak, mixed or noise (do not build on these)

- **Fast spike, 30-day at the money.** Rule: days since spike = 0 and calls 5d avg ≥ 5 and calls 20d < 3. Scorebook: 88 trades, -0.5% (range -26.6% to +31.0%), median -47.2%. Halves +23.4% and -25.6%, which is unstable. Agent 4 expected it to lose, and the code says it is about average.
- **Dip name, 20d % < -20, 90-day at the money.** Scorebook: 44 trades, +14.1% (range -15.7% to +50.3%), median -9.0%, 46% winners, beat in 3 of 6 bundles. Halves +34.2% and +5.7%.
  - It conflicts with the dip-buying losses in section 2. Adding RSI < 35 and using a 5% above strike (32 trades) gives -8.3%, with halves -49.6% and +5.4%.
  - Treat as noise unless a larger test confirms it. It is the only dip result that looks positive.
- **Oversold at 90 days, at the money.** Rule: RSI < 35 and vs ma50 % < -10. Scorebook: 48 trades, -1.5%, median -10.0% (the best median of any rule), 40% winners, beat in only 2 of 6 bundles. Do not use the 30-day or out-of-the-money versions.
- **Sharp 1-day drop, 90-day call 5% above.** Rule: 1d % ≤ -5. Scorebook: 51 trades, +3.9%, median -23.2%, 3 of 6 bundles, halves +16.9% and -6.8%. Noise.
- **Spike with no news, rising stock, 30-day at the money.** Rule: spike, no news ≥ 1 and 5d % > 5. Scorebook: 208 trades, -7.0%, median -34.0%, beat in 5 of 6 bundles. The 5d % > 5 condition does the work.

### 1D. Sizing and execution (all traders agree)

- Flat, small size. Never add after wins.
- Use 30-day or 90-day expiries. Never use 14-day (many -100% outcomes).
- Trend rules want a 5% or 10% above-price strike. 30-day at-the-money is fine for broad trend filters.
- Hold exactly 10 sessions. Double-or-10 and a -50% stop could not be told apart from hold-10 on common entries. Double-or-10 has a slightly worse benchmark (-12.0% vs -10.9%), so no exit has been shown to rescue a poor entry.
- Pick the structure by what you want:
  - A tail-seeking lottery: 30-day 5% to 10% above price, tiny size.
  - A steadier profile: 90-day, trend plus up-market gate.

## 2. AVOID

### Clearly worse than the benchmark (code-confirmed)

| Rule | Trades | Average (range) | Median | Beat benchmark |
|---|---|---|---|---|
| Large down day with call spike (1d % ≤ -5 and calls ≥ 3), 30-day, hold 10 | 95 | **-23.2%** (-42.2% to +2.3%) | -48.6% | 1 of 6 |
| Calls ≥ 3 and price $10 to $50, 90-day | 103 | **-21.9%** (-31.1% to -12.2%) | -30.5% | 1 of 6 |
| Stretched-up (RSI ≥ 70, vs ma20 % ≥ 10, 5d % ≥ 10), 90-day at the money | 48 | **-20.6%** (-31.1% to -8.8%) | -33.8% | 2 of 6 |
| Call activity with high vol (calls 5d avg > 1, vol20 % ≥ 4, vs ma20 % > 0), 90-day at the money | 98 | **-19.7%** (-30.0% to -8.9%) | -37.1% | 1 of 6 |
| $10 to $50 price, 30-day call 5% above (the plain price filter) | 958 | **-19.6%** (-30.5% to -7.6%) | -60.0% | 1 of 6 |
| Spike with no news ≥ 1, 90-day at the money | 138 | **-19.4%** (-28.7% to -10.8%) | -25.2% | 0 of 6 |
| Oversold with high vol (vol20 % ≥ 4, RSI < 40), double-or-10 | 218 | **-18.7%** (-30.9% to -7.0%) | -46.6% | 2 of 6 |
| Low-volatility dip (20d % < -10 and vol20 % < 4), 30-day | 196 | **-18.0%** (-33.5% to -1.1%) | -43.7% | 2 of 6 |
| Oversold (RSI < 45 and off high % < -25), 30-day | 326 | **-17.1%** (-31.1% to -2.4%) | -46.9% | 1 of 6 |
| Stock above ma50 in a down market (market 20d % < 0), 90-day call 10% above | 78 | **-12.9%** (-26.1% to +0.2%) | -21.2% | 2 of 6 |
| Below ma50 with call interest in an up market (calls 5d avg > 1), 90-day call 10% above | 87 | **-16.6%** (-34.5% to +2.9%) | -30.8% | 2 of 5 |
| Oversold in an up market (RSI < 35, market 20d % > 0), 90-day call 10% above | 53 | -13.1% | -28.7% | 1 of 5 |
| Calls ≥ 3 with no other condition, 90-day | 234 | -15.2% (-22.0% to -7.7%) | -28.2% | 1 of 6 |
| Call-days surge (call days 2x+ ≥ 4 and calls 5d avg > 2), 30-day | 256 | -15.0% | -47.9% | 2 of 6 |
| Oversold deep drawdown (RSI < 35, off high % < -25, 20d % < -15), 30-day | 160 | -14.6% | -50.8% | 2 of 6 |
| Oversold pullback (off high % ≤ -20, RSI < 40), 90-day call 5% above | 73 | -14.6% (-27.3% to +0.2%) | -33.3% | 1 of 6 |
| Sub-$10 oversold rebound (RSI < 30, off high % < -30), 30-day call 5% above | 80 | -24.3% (-48.2% to +3.3%) | -64.2% | 2 of 6 |

**Themes**
- Dip-buying with calls loses at nearly every expiry and strike tested. The one exception is the small 90-day at-the-money dip result in section 1C.
- Buying call-volume spikes loses when the stock is falling, mid-priced, high-volatility, or has no news. Spike days mean expensive premium.
- Spike signals flip sign once the stock is above its 20-day average.
- Do not use a bullish trend rule when the market's 20-day trend is down.
- $10 to $50 stocks are the worst price band for 30-day calls.

### No edge either way (about the benchmark or noise)
- Extended names (RSI ≥ 75 and vs ma20 ≥ +20), 96 trades, -8.2%. "Extended names fade" is unsupported.
- Sustained call building, 30-day (calls 5d avg ≥ 2 and call days 2x+ ≥ 3): 573 trades, -8.9%, beat in 3 of 6 bundles.
- Slow steady call buying (calls 20d > 5 and call days 2x+ 20d > 7), 30-day call 5% above: 179 trades, -4.3%, median -58.7%, halves +20.1% and -27.4%.
- Sustained call build at 90 days: 19 trades, -5.6%.
- Low volatility with call activity, 90-day at the money (vol20 % < 4 and calls 5d avg > 1): 276 trades, -9.5% (range -16.4% to -2.5%), about the benchmark.
- Heavy calls with news (calls 5d avg > 3 and news 7d > 0), 30-day call 5% above: 423 trades, -6.6%, median -60.0%, beat in 4 of 6 bundles. It is only marginally better than the benchmark.
- Put crowding (puts 5d avg ≥ 3): 727 trades, -9.2%. It is not a bearish signal.
- Under-$10 stocks: 76 trades, -8.4% even with calls active and an up market, and an under-$10 20-day run-up gave -11.1%. Treat the band as a poor place to buy.
- Ratings of any kind. The traders' "+1 underperforms", "-1 outperforms" and "-2 is contrarian" patterns reversed from bundle to bundle. Do not use ratings for entry or sizing.

### Stop doing
- 14-day expiries.
- Strikes 10% or more out of the money outside the momentum setup in 1A.3.
- Reading extremes lists as evidence. Both tails contain the same features.
- Using exits to rescue a bad entry.
- Judging by total P&L or averages alone.
- Changing structure bucket by bucket after small samples. Results at n=5 to 40 flipped sign between bundles.
- Trading a structure your own notes have moved to paper only. Bundle 6 had such a breach.

## 3. NEW IDEAS TO TEST

1. **Stack the trend, over-$50, news and market features at 90 days (highest priority, untested).**
   - The two best features were over $50 + news tone + trend at 30 days (+23.4%, stable halves) and above-ma50 in an up market at 90 days (+3.3%, 5 of 6 bundles).
   - Test, at 90 days and also at 60 days:
     - over $50 + vs ma50 % > 0 + 20d % > 0 + news tone 7d > 0
     - the same with market 20d % > 0
     - the same with calls 5d avg > 1
   - Test calls 5% and 10% above the price. Require n ≥ 60 and a check of both halves.
2. **Market regime gate (partly confirmed).**
   - Stock above ma50 averaged +3.3% in an up market and -12.9% in a down market on the same strike.
   - Apply "market 20d % > 0" to every Tier 1 rule, and also test market 5d %.
   - Test whether the first-half advantage of most rules is just a market-trend effect.
3. **Strike ladder inside the momentum setup.**
   - 20d % > 20 and vs ma50 % > 15 beat its benchmark in 6 of 6 bundles at 10% above the price at 30 days.
   - Test at-the-money, 5%, 10% and 15% above, at 30 and 90 days.
   - Test thresholds (20d % > 10, > 20, > 30; vs ma50 % > 10, > 15, > 25) and an over-$50 or news-positive add-on.
   - Test whether the median improves at 90 days.
4. **Buy before the crowd (partly confirmed by the code).**
   - Quiet-after-spike (+10.1%, both halves positive) and spike-aged-20+ in an uptrend (+109%, n=7) suggest names not yet crowded work better than names mid-spike.
   - Test days since spike ≥ 20 with vs ma50 % > 0, over $50, and market 20d % > 0, at 90 days.
   - Test the 20-day measures nobody tested directly: calls 20d, long calls 20d, otm calls 20d, call days 2x+ 20d. Early looks at slow buying were mixed (+20.1% first half, -27.4% second half).
5. **Replace the wrapper: deep in-the-money calls or call spreads (untested).**
   - Stock medians are near zero while option medians are -20% to -60%, so the wrapper costs most of the loss.
   - Test a 90-day call 5% to 10% below the price (delta about 0.8) on the Tier 1 setups. Also test a bull call spread to cut premium.
   - Compare each to the stock return on the same entry.
6. **Volatility-aware premium filter (untested).**
   - High volatility (vol20 % ≥ 4) with call activity lost -19.7%, while low volatility was only about the benchmark.
   - Test vol20 % bands (below 2%, 2% to 4%, above 4%) inside over-$50 and inside trend setups. Combine with 60-day and 120-day expiries.
7. **Why overbought chase works at 30 days and fails at 90 days.**
   - 30-day at-the-money gave +4.8%. The 90-day version with 5d % ≥ 10 gave -20.6%.
   - Test whether a hot last-five-days move (5d % ≥ 10) is the toxic ingredient.
8. **Unused features to scan as single-feature buckets** (keep a feature only if it beats the benchmark in at least 4 of 6 bundles and holds in both halves):
   - shares ratios (shares, shares 5d avg)
   - close vs vwap %, vs vwap20 %
   - otm calls 20d, short/medium/long mix, p/c drop, news 1d
9. **Fade the losers with defined risk (untested, high risk, paper only).**
   - The worst cells lose 18% to 23% on average with ranges that exclude zero: large down day with a spike, oversold quiet names, spike with no news, $10 to $50 at 30 days.
   - Test bear call spreads or put structures on paper only, with a tail-loss check, since these names occasionally rebound hard.
10. **Stock-level test (the traders' consensus idea, unanswered).**
    - Compare the 10-session stock return of the Tier 1 filter passes against the universe median on the same dates.
    - This would show how much of an option's result is the stock signal versus premium. It needs per-candidate rows, so request them if they exist.
11. **Entry implied volatility** is not available. If it ever is, test whether premium level explains the losses.

## 4. OPEN QUESTIONS

- Can any call setup have a positive median? The least negative are 90-day oversold (-10.0%, small n), full stack over $50 (-8.0%) and 90-day dip name (-9.0%, noisy). Is a positive median reachable with calls at all, or only with deep in-the-money calls, spreads or stock?
- Is "over $50" a size or liquidity effect, lower implied volatility, or a proxy for something else? It helps at 30 days and 5%/10% above strikes and barely helps at 90 days at the money.
- What explains the first-half versus second-half split? Is it market trend, volatility, or particular weeks? Several rules were strongly positive in one half and negative in the other (for example full stack $10 to $50: -19.5% then +2.5%; call-flow trend: +6.0% then -2.5%).
- How much of the option loss is direction versus premium decay? Pair each option trade with its stock return.
- Is the strike effect real? 5% above beat at the money at 90 days on the benchmarks (-7.4% vs -8.4%), but at 30 days the sign flipped for some rules while the trend/momentum rules were best out of the money.
- Do exits differ? Hold-10, double-or-10 and a stop were identical on common entries. They cannot be compared without premium paths.
- Why are the 30-day tail rules (+23% to +26% average, median about -41% to -57%) so different from the 90-day rules (+3%, median -16%)? Is the 30-day edge only a heavier right tail, and does it survive realistic sizing?
- Does the dip result at 90 days at the money (+14.1%, n=44) mean dips are fine at long expiries, or is it noise?
- Ratings: no stable signal. Treat as noise unless a full-universe test with n ≥ 60 says otherwise.

### Agent 1's final notes (not passed on)

# TRADING NOTES: STOCK OPTIONS, 10-SESSION HOLD (rewritten after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Status: no validated edge. Options are paused pending the stock-level test.**

Six bundles in, nothing has shown that my filters pick stocks that beat the universe on stock returns. The option book has been a lottery with a negative or unstable median in most structures. The key test is still unanswered because the filtered-subset stock statistics were never supplied.

Until the filtered-subset stock return is available and clears the decision rule below, I trade no new options. I keep logging every candidate's filter status and 10-session stock return. If the test passes, options resume at paper size under the rules in this section.

**Decision rule (cross-bundle)**
- Options stay paused unless the all-pass subset's median stock return beats the universe median by at least 1 point in both bundle 5 and bundle 6. Bundle 6's filtered-subset data is missing, so this cannot be evaluated. Bundle 5's is also still missing.
- If no filter combination beats the universe median in at least 4 of 6 bundles, options are stopped for good. The research log continues.
- Universe medians (bundles 1–6): +0.2%, −0.9%, −1.2%, −0.9%, +0.4%, +0.7%. Positive in 2 of the last 2 bundles, negative in 3 of the earlier 4. The baseline is near zero and noisy.

**Instrument and expiry (when options resume)**
- Calls only. No puts, no spreads.
- Expiry: 90 days.
- Hold: exactly 10 sessions, then sell. No early exits, no stop-loss, no profit-taking.
- 14-day calls: banned.
- 30-day calls: suspended, not dropped. See section 4.

**Strike (test arm only, no standing rule)**
- **90-day 10% OTM** is the leading test arm. Evidence: bundle 5 n=4 (average +11.3%, median +9.5%); bundle 6 n=5 (average +28.7%, median +49.9%). Combined n=9, both bundles positive. Bundle 4 was negative (one −100%, one −1.9%). Too few trades to adopt, but it is the only structure with positive medians in more than one bundle.
- **90-day ATM**: not a standing rule. Bundle 6 n=10, average −23.6%, median −15.1%. Bundle 5 n=4, +10.3%. Bundle 2, −36.4%. Net negative. Drop as primary.
- **90-day 5% OTM**: no longer a control I trust. Bundle 5 n=11 (average −16.5%, median −23.9%). Bundle 6 n=6 (average +56.0%, median +45.7%). Pooled across bundles 5 and 6 (n≈17), the average is near +9% but the median is unstable. Its mean is driven by a few large winners. Do not rely on it.
- **90-day 5% ITM (delta ≈0.8)**: planned in bundles 4, 5 and 6. It has never run. No ITM results appear in bundle 6. Treat as not tested. The paired ITM-vs-OTM test is the first thing to run once options resume.
- **90-day 15% OTM**: n=1 in bundle 6 (−30.2%). Insufficient.

**Entry filters (all required; log pass/fail for every candidate, not just trades)**
1. **Price band:** $10 to $50, or over $50. No under-$10 option entries.
2. **calls 5d avg > 1.**
3. **vs ma50 % > 0.** Strict. A blank value counts as a FAIL, because the test cannot be verified.
4. **market 20d % > 0.** Strict. No exceptions.

Preferred, logged but not gating: 20d % > 0, news 7d > 0.

**Rating:** recorded, never used for entry or sizing. See section 4.

**Sizing:** flat and identical. Never add after a win.

**Zero-violation rule:** any entry that fails filters 1–4 is a process error, logged as a violation. Target per bundle: zero. A trade with a blank required field counts as a violation.

**Confidence in this section:** low. The filters are reasonable hypotheses and the option wrapper cost is large and well documented. Returns are very fat-tailed, so the mean reflects a few trades.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

**Bundle result:** 26 option trades, +$2,135. Average +8.2%, median −5.1%, 46% winners. The average is again carried by a few large winners while the median is negative.

**Structure results (10-session hold)**

| Structure | n | Average | Median | Read |
|---|---|---|---|---|
| 90-day ATM | 10 | −23.6% | −15.1% | Negative. Not a standing rule. |
| 90-day 5% OTM | 6 | +56.0% | +45.7% | Positive but n=6. Stability unproven. |
| 90-day 10% OTM | 5 | +28.7% | +49.9% | Positive. Leading test arm. |
| 90-day 15% OTM | 1 | −30.2% | −30.2% | Too small. |
| 30-day ATM | 3 | +33.5% | +45.1% | Positive but n=3. Suspended (see §4). |
| 14-day ATM | 1 | −100% | −100% | Banned. Failed filters 3 and 4. |
| 5% ITM (90-day) | 0 | n/a | n/a | Not run. Still outstanding. |

**Filter compliance (from the 20 trades the system listed in detail; 6 of 26 were not shown)**
- At least 8 of 20 shown trades violated a required filter:
  - 5 failed filter 4 (market 20d below zero).
  - 3 failed filter 3 with a negative vs ma50 value.
  - 2 had a blank vs ma50 and were treated as failures.
  - Union: 8 trades with at least one violation.
- Violations are therefore at least 8 of 20 shown, and possibly more among the 6 not shown.
- Zero-violation target missed again, after at least seven violations in bundle 5. This is a repeated process failure, not bad luck.

**What the shown trades suggest (low confidence, selected sample)**
- The 20 trades shown are the extremes, not a random sample. Treat all figures here as descriptive only.
- Trades failing filter 4 (n=5): average −42.7%.
- Trades passing filter 4 (n=15): average +30.2%.
- This matches the filter-4 hypothesis. It is the opposite of bundle 5, where all three 30-day ATM trades were entered with negative market 20d and then did very well (+222%, +536%, −92%).
- Filter 4 is supported in bundle 6 and contradicted in bundle 5. Keep as a hypothesis, enforce it, and do not treat it as proven.

**Universe (stock returns, all 250 candidates)**
- Average +0.5%, median +0.7%.
- The filtered-subset stock return, per-filter pass counts, and the market-regime split were not supplied. The stock-level filter test cannot be run. This gap has now persisted for two bundles.

**Ratings (recorded only)**

| Rating | Bundle 6 n | Avg | Median | Bundle 5 n | Avg | Median |
|---|---|---|---|---|---|---|
| +1 | 60 | +2.0% | +1.1% | 55 | +1.2% | +0.8% |
| 0 | 69 | +1.6% | +1.8% | 64 | +0.3% | 0.0% |
| −1 | 101 | −1.8% | −1.2% | 117 | +1.2% | +1.4% |
| −2 | 20 | +3.6% | +4.6% | 14 | +0.2% | −4.1% |

- The "−1 beats +1" split from bundle 5 has reversed. In bundle 6, +1 beats −1 on both average (+2.0% vs −1.8%) and median (+1.1% vs −1.2%).
- The −1 preference is dead. Ratings do not predict stock returns across bundles.
- −2 is positive in bundle 6 and weak in bundle 5. Inconsistent. Record only.

**Extremes (lists, not evidence)**
- Largest stock moves were again mostly under $10, in both directions (roughly −41% to +89%).
- The biggest losers and winners both appear on both sides of vs ma50 and of the 20-day trend. I see no separation in these lists.

---

## 3. WHAT I WILL TRY NEXT

1. **Stock-level filter test (blocker, must be resolved first).** For every candidate, log pass/fail on filters 1 to 4, and log the 10-session stock return. Request from the system, and do not proceed until received:
   - Pass count for each filter, and for all four combined.
   - Average and median stock return for the all-pass subset, versus the universe.
   - The same split by market 20d above versus below zero.
   - If the system cannot supply these, log a blocker and keep options paused.

2. **Paired structure test (once options resume).** On all-pass names, pair 90-day 5% ITM against 90-day 5% OTM on the same name, and record the stock return for each pair. Also record 90-day 10% OTM on the same names, so the three arms can be compared on identical stocks. Minimum 20 pairs before reading anything into it.

3. **Zero-violation enforcement.** Written pre-trade checklist for every entry: filters 1 to 4 each marked pass before the order. Report violations per bundle. Target: zero. Blank fields count as failures.

4. **Regime split (record only).** Log market 20d sign for every candidate. Compare all-pass stock returns in positive versus negative regimes. Do not change the option filter on this in bundle 7. If the negative-regime subset clearly beats the positive one on both mean and median, carry it to bundle 8 as a test, not a rule.

5. **Under-$10 stock-only read.** No under-$10 options. Log how many under-$10 candidates pass filters 2 to 4, and their stock returns separately. This band holds many of the biggest moves in both directions. It remains the one place the exclusion could hide a real effect.

6. **Days-since-spike and 20-day features.** Still need full-universe bucket statistics for: days since spike ≥20 combined with vs ma50 > 0 and 20d % > 0; and single-feature buckets for calls 20d, long calls 20d, otm calls 20d, and call days 2x+ 20d at the stock-return level. Keep a feature only if it beats the universe in at least 4 of 6 bundles.

7. **Ratings: record only.** Continue logging. No gating and no sizing.

8. **30-day calls: suspended, pending a clean test.** See section 4 for the reasoning. Do not trade them until the stock-level test has passed and the strict filters are being enforced.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

**Dropped**
- 14-day calls (−100% in bundle 3; −100% in bundle 6, n=1 each).
- 30-day 5% OTM and 30-day 15% OTM (−100% and −91% single trades in bundle 5; 0 for 11 in bundles 1–2).
- Double-or-10 exit rule.
- Rating gate (enter only on −1 or −2). Failed in bundle 3. The −1 preference also reversed in bundle 6.
- −1 over +1 as a rating preference. Reversed in bundle 6.
- 90-day ATM as a standing structure. Bundle 6 n=10 average −23.6%, median −15.1%; bundle 2 −36.4%.

**Suspended (not dropped)**
- **30-day ATM.** I previously banned it because bundle 5's average was carried by two outliers and three of five 30-day trades failed filter 4. Bundle 6 adds three more 30-day ATM trades, all positive (average +33.5%, median +45.1%). Across bundles 5 and 6, that is six trades with positive medians. This is not a clean rejection, but the sample is far too small, the earlier bundles were negative, and the filter-violation problem contaminated the results. Suspended until a dedicated test is run with strict filters.
- **30-day OTM** (any strike): still banned.

**Demoted or unrun**
- 90-day 5% ITM: planned since bundle 4, still not run. Not tested in bundle 6.
- 90-day 5% OTM: no longer a control I can rely on. Median negative in bundle 5, positive in bundle 6. Pooled mean near +9% (n≈17), with very wide dispersion.
- 90-day 10% OTM: the leading test arm. Bundle 5 and bundle 6 both positive; bundle 4 negative.
- Under-$10 options: still excluded.

**Universe picture**
- Averages (bundles 1–6): +2.2%, −0.4%, −0.2%, +0.3%, +0.9%, +0.5%.
- Medians (bundles 1–6): +0.2%, −0.9%, −1.2%, −0.9%, +0.4%, +0.7%.
- The filter stack has not yet shown it beats this baseline. The stock-level test is still unanswered.

**Confidence summary**
- **High:** The option wrapper cost is large. Mean-median gaps remain very large in every structure, and the averages are driven by a few trades.
- **High:** Process discipline is poor. At least seven violations in bundle 5 and at least eight of the 20 shown trades in bundle 6 failed a required filter.
- **High:** 14-day calls are not usable.
- **Medium:** 90-day ATM has a negative median and a negative net result. It is not a standing structure.
- **Medium:** 90-day 10% OTM is the most promising test arm. Both recent bundles are positive, but n is small (9 across two bundles).
- **Medium:** Under-$10 names carry the largest stock moves in both directions. Still unmeasured.
- **Low:** Filter 4 (market 20d > 0) helps option outcomes in bundle 6 (fail-4 trades averaged −42.7%, pass-4 trades +30.2%, on a selected sample) and hurt in bundle 5 (30-day trades). Hypothesis only.
- **Low:** Filter 3 (vs ma50 > 0) and filter 2 (calls 5d avg > 1) are reasonable hypotheses. Not yet tested at the stock level.
- **Low:** 30-day ATM may be a real structure or a lucky set of outliers. Six trades across two bundles, both positive. Unresolved.
- **Very low:** Spike-with-no-news, deep-drawdown, overbought, and news-driven profiles in the extremes lists. No separation visible on either side.

### Agent 2's final notes (not passed on)

# TRADING NOTES: FINAL (after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

### Status in one paragraph
I trade nothing live: no option premium and no stock position. Every idea stays on paper at flat, small notional until a stock-side rule beats the universe median on the same dates across bundles. After six bundles, no option structure has shown a stable positive median on hold-10 exits. The option wrapper (decay plus strike cost) is the largest and most consistent cost I have measured. The only candidate worth further work is a stock-side filter, and it has not yet been tested because I have never received per-candidate rows.

### Status table

| Item | Status | Basis |
|---|---|---|
| Live trading | None | No rule has passed |
| Setup A: stock-side trend and news filter | Untested, top priority | Needs per-candidate rows |
| Setup C: 30-day, 5% OTM, over $50, hold-10 | **Dropped** | Fails its own promotion rule (see 1.4) |
| 0% strike, 30-day, double-or-10 exit | **Dropped** (failed replication) | Bundle 6 median -38.1% (n = 20) |
| 5% strike, 30-day, double-or-10 exit | Paper only, low confidence | Bundle 6 median +8.0% (n = 5) |
| Ratings (+1 sign) | Logged, not a filter | Beat universe median in 3 of 4 bundles, small margins |
| Fixed paper wrapper (benchmark only) | Active, for measurement | See 1.3 |

### 1.1 Benchmark (applies to every rule)
- **The bar is the universe median return over the same 10 sessions on the same dates.** Never zero, never the average.
- Universe medians by bundle: bundle 3 -1.2%, bundle 4 -0.9%, bundle 5 +0.4%, bundle 6 +0.7% (250 candidates, average +0.5%).
- Every option result is judged against the stock's return on the same name over the same 10 sessions. The gap between the two is the wrapper cost.
- **Judging rules:** median return, share of winners, and beats-benchmark count across bundles. Never judge by average. Never judge a bucket by its extremes list.

### 1.2 Stock-side candidate filter (Setup A): the first real test
- **Columns and thresholds:** vs ma50 % > 0, AND 20d % > 0, AND news 3d > 0, AND news tone 7d > 0, AND price band over $50.
- **Test:** 10-session stock return of every candidate passing all five conditions, compared with the universe median on the same dates. Log pass count and the filtered median.
- **Pass:** the filtered median beats the universe median in at least 4 of 6 bundles, with a pass group of at least 15 names per bundle.
- **Status:** untested. No per-candidate rows have been provided, and aggregates cannot produce this result. Log it as untested, not failed.
- **Confidence in the filter itself:** very low. It is the best-reasoned idea I have (trend, news, and price-band confirmation), but it has no evidence yet.

### 1.3 Option wrapper: paper benchmark only (not a strategy)
I am no longer changing strike or exit each bundle. Across six bundles I have tried many combinations on small buckets, and the results flip sign from bundle to bundle, which is what noise looks like at n = 5 to n = 40. From now on I run one fixed paper wrapper to measure the cost, not to find a winner:
- **Expiry:** 30 days.
- **Strike:** 0% to 5% above price (use 5% as the single fixed strike for consistency).
- **Exit:** 10-session hold. No stop, no early exit.
- **Size:** flat and small.
- **What I record:** option return, stock return on the same name over the same 10 sessions, and the gap between them (decay plus strike cost). The purpose is to see whether the gap is stable. It is not to promote a trade.
- **Confidence the wrapper is value-destroying on median:** high (see 4).

### 1.4 Setup C (30-day, 5% OTM, over $50, hold-10): dropped
- The aggregate 5%-OTM hold-10 median was negative in all four bundles where it was tested: bundle 3 -42.7% (n = 39), bundle 4 -72.0% (n = 44), bundle 5 -25.7% (n = 27), bundle 6 -56.9% (n = 10).
- The over-$50 subgroup was never reported with n, median, or share positive, so the promotion rule (n ≥ 15 with a positive median, in two bundles) was never met. The extremes lists in bundles 3 to 6 showed over-$50 names on both sides, which is not evidence.
- **Decision:** dropped. I will only re-open a price-band split if the system supplies n, median, and share positive for each band in a full-stats table.

### 1.5 Exit and strike rules (paper)
- **Expiry:** 30 days. 90-day calls retired (negative median in every bundle tested). 14-day expiries lost in every bundle.
- **Strike:** 0% to 5% above price. 10%+ OTM is out (bundle 2 -84%, bundle 5 -60% at n = 2).
- **Exit:** hold-10 is the fixed baseline. Double-or-10 is demoted to a side-observation (see 2.3).
- **No stop-loss rules.** Stops were dropped in earlier bundles and nothing since has argued for them.

### 1.6 Ratings: logged, not a filter
- Rating +1 median vs universe median: bundle 3 best group; bundle 4 worse (-1.3% vs -0.9%); bundle 5 +3.3% vs +0.4%; bundle 6 +1.3% vs +0.7%. It beat the universe median in 3 of 4 bundles, but the bundle 6 margin was only 0.6 points and its average was 0.0% against a universe average of +0.5%.
- Rating -1 (median +0.7% in bundle 6) was no worse than the universe, so the negative side has no signal.
- Rating -2 (n = 7 in bundle 6) and rating 0 are too small or too flat to use.
- **Rule:** keep logging ratings. A +1 filter becomes a candidate only if it beats the universe median in 4 of 6 bundles. It currently sits at 3 of 4 tested. Confidence: low.

### 1.7 Reasoning behind the strategy
- **The stock universe is flat over 10 sessions.** Medians sit between -1.2% and +0.7%. There is no obvious directional edge to harvest from broad exposure.
- **Options lose on median even when the stock is flat or slightly up.** A 30-day call bought near the money, sold after 10 sessions, usually loses a meaningful share of premium. Decay and strike cost are the main drivers.
- **Option gains come from a right tail, not from a typical trade.** Averages are positive in some bundles only because a few trades return several hundred percent. A strategy whose median trade loses cannot be sized up on that tail.
- **A stock-side rule is the only thing that could help beyond the wrapper cost.** That is why Setup A is the priority.

## 2. WHAT I TESTED IN THIS BUNDLE

**Headline:** +$1,904 on 40 trades, average +4.8%, median -38.1%, 45% winners. Universe: 250 candidates, median +0.7%, average +0.5%.

### 2.1 Results by structure

| Structure | n | Average | Median | Notes |
|---|---|---|---|---|
| 30d, 0% OTM, double-or-10 | 20 | +4.3% | **-38.1%** | Replication of bundle 5's +171% (n = 4) failed |
| 30d, 5% OTM, hold-10 | 10 | +2.4% | **-56.9%** | Worse than bundle 5 (-25.7%); still negative |
| 30d, 0% OTM, hold-10 | 5 | -14.2% | -3.7% | Closest to flat; still negative average |
| 30d, 5% OTM, double-or-10 | 5 | +30.4% | +8.0% | Only positive-median option bucket; n too small |

### 2.2 What held up
- **Options lose on median on hold-10 exits again.** The 5%-OTM hold-10 median (-56.9%) and the 0%-strike hold-10 median (-3.7%) are both negative, and the 0% median sits near the stock's flat return. The wrapper cost is consistent across the bundles.
- **The universe median was positive (+0.7%), but option medians were far below it.** The wrapper cost is much larger than the stock move in most buckets.
- **The average is again far above the median** (+4.8% vs -38.1%). This is the same right-tail pattern as bundles 3 to 5.

### 2.3 What failed
- **The 0%-strike double-or-10 exit did not replicate.** Bundle 5 showed median +171% on n = 4. Bundle 6 showed median -38.1% on n = 20, a far larger sample. The earlier positive was a small-sample artifact, and the double-or-10 comparison was biased from the start because early exits only happen after a trade has already doubled. **Dropped.**
- **Setup C's 5%-OTM hold-10 median got worse** (-56.9% vs -25.7% in bundle 5). It is still negative in all four tested bundles. Dropped (see 1.4).
- **Exit and strike still do not show a stable pattern.** Across bundles, 0% hold-10 medians were -28.2% (bundle 5) and -3.7% (bundle 6). Double-or-10 at 0% went from +171% to -38.1%. Each strike or exit change has flipped sign. This is what noise looks like at these sample sizes, so I am stopping the bucket-by-bucket search (see 1.3).

### 2.4 The 5%-OTM double-or-10 bucket (n = 5, median +8.0%)
- This is the only option bucket in bundle 6 with a positive median. n = 5 is far too small to act on, and the same exit at 0% failed badly in the same bundle.
- Logged as a paper side-observation, not a candidate. It only matters if it recurs at n ≥ 10 with a positive median.

### 2.5 The new idea I tried: a paired exit test
- I tried to compare, on the same names, the hold-10 and double-or-10 exits at 0% strike. The bundle does not supply paired rows, so the comparison was done across buckets. The result (double-or-10 median -38.1% vs hold-10 median -3.7%) pointed against double-or-10. That is a directional read on different names, not a paired test, and it should be treated as such.
- **Lesson:** the paired test needs per-candidate rows. Without them, exit comparisons across buckets are not reliable.

### 2.6 Over-$50 pocket and price bands
- Not measurable. The over-$50 trades in the extremes lists again appear on both sides (several near -90% to -100%, several +87% to +140%). The full split was not supplied. Setup C is dropped (see 1.4).

### 2.7 Extremes lists (not used as evidence)
- Big stock losers included names with high call volume, news spikes, and falling prices; big stock winners included names with low call volume and names with strong 20-day gains. Signals like calls 5d avg, call days 2x+, rsi, vs ma50, and news tone appeared on both sides again.
- Rule: no rule is derived from these lists. This is the sixth bundle in which they failed to separate winners from losers.

### 2.8 Ratings in this bundle
- +1 median +1.3% vs universe +0.7% (beat by 0.6 points). Positive but small.
- -1 median +0.7% (equal to universe). 0 median +0.1%. -2 median +0.5% (n = 7).
- Read: no rating has a meaningful edge in this bundle. +1 keeps a weak positive tilt across bundles, not a filter.

## 3. WHAT I WILL TRY NEXT

1. **Request per-candidate rows for the next bundle (highest priority).** For every candidate, record the 10-session stock return and pass/fail on Setup A (vs ma50 > 0, 20d > 0, news 3d > 0, news tone 7d > 0, price over $50). Report the filtered median and count against the universe median on the same dates. No Setup A result without rows.

2. **Run one fixed paper wrapper for measurement only (1.3).** 30-day, 5% OTM, 10-session hold, all price bands. For each option trade, log the option return and the stock return on the same name over the same 10 sessions. The gap is the decay-plus-strike cost. Track whether the gap is stable across bundles. I will not change strike or exit to chase results.

3. **Request full subgroup stats by price band** (under $10, $10 to $50, over $50) for the fixed wrapper: n, median option return, share positive, and median stock return over the same 10 sessions. This only matters for the record. Setup C stays dropped unless the split shows n ≥ 15 with a positive median in two bundles.

4. **Premium-aware check on every trade.** If the stock is near 0% and the option is -25% or worse, the decay and strike cost are the cause. Only a stock-side rule can beat that cost. This check is the bridge between the wrapper and Setup A.

5. **Hold and log only** (no test until the rows arrive):
   - **Extension:** 20d % above +20%, RSI above 75, vs ma20 above +15%.
   - **Sub-$10 rebound:** RSI below 30 with off-high below -30%.
   - **Slow buying:** calls 20d above 5, call days 2x+ 20d above 7.
   - **Rating +1:** keep a running median-vs-universe count. A cut is tested only if it beats the universe median in at least 4 of 6 bundles.

6. **Stop reading extremes lists as evidence.** Six bundles now show the same signal values on winners and losers. No rule will be ranked from an extremes list.

7. **Judging rule (unchanged):** median return, share of winners, and beats-benchmark count across bundles. Never judge by average. Never judge a bucket by its extremes. Stop changing the option structure bucket by bucket; a stock-side rule with paired evidence is the only path to a live decision.

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Supported (held across bundles)
- **Hold-10 options lose on median.** 30-day 5%-OTM hold-10 medians: bundle 3 -42.7% (n = 39), bundle 4 -72.0% (n = 44), bundle 5 -25.7% (n = 27), bundle 6 -56.9% (n = 10). At-the-money bundles 1 and 2: about -52% to -53%. Confidence: high.
- **The stock universe is flat over 10 sessions.** Medians: bundle 3 -1.2%, bundle 4 -0.9%, bundle 5 +0.4%, bundle 6 +0.7%. Confidence: moderate.
- **14-day expiries and 10%+ OTM strikes lose.** 14-day lost in every bundle. 10%+ OTM: -84% (bundle 2), -60% (bundle 5, n = 2). Confidence: moderate.
- **90-day calls have a negative median in every bundle tested.** Retired. Confidence: moderate.
- **Average return is not a decision metric.** Bundle 6 average +4.8% against median -38.1%. Confidence: high.

### Weakened or contradicted
- **Double-or-10 exit at 0% strike (reinstated in bundle 5, failed in bundle 6).** Bundle 5 median +171% (n = 4); bundle 6 median -38.1% (n = 20). The earlier result did not replicate. Dropped.
- **Over-$50 option pocket.** Bundle 2 positive (n = 9); bundles 3 to 6 not reported with full stats and roughly even in extremes. Not confirmed. Dropped.
- **5%-OTM advantage over at-the-money.** Bundle 6's 5%-OTM hold-10 median (-56.9%) was worse than its 0%-strike hold-10 median (-3.7%, n = 5). Across bundles the strike difference has no stable sign. Treated as noise.
- **Trend and news filters as discriminators from extremes lists.** Did not separate winners from losers in bundles 3 to 6. Still untested in isolation (Setup A).
- **Ratings as a filter.** Sign flipped in bundle 4 (+1 worst). +1 has beaten the universe median in 3 of 4 tested bundles, but the margins are small. Not a rule.

### Revived or open (paper only)
- **Double-or-10 at 5% strike.** Median +8.0% (n = 5) in bundle 6. Too small to act on. Logged as a side-observation. It needs n ≥ 10 with a positive median before it is reconsidered.

### Dropped
- Any at-the-money 30-day call, live or paper.
- 90-day calls.
- 14-day expiries.
- 10%+ OTM strikes.
- Stop-based exits.
- Setup C (30-day, 5% OTM, over $50, hold-10), failed promotion.
- Double-or-10 at 0% strike, failed replication.
- Ranking rules built from extremes lists.
- Average return as a decision metric.
- Bucket-by-bucket strike and exit changes (replaced by the fixed wrapper in 1.3).

### Confidence summary
- **High:** hold-10 options lose on median across strikes and bundles. The wrapper (decay plus strike cost) is the main cost. No live premium until a stock-side rule passes.
- **Moderate:** the stock universe is flat over 10 sessions (medians -1.2% to +0.7% across the last four bundles). The bar is the median.
- **Low:** rating +1 as a weak positive (3 of 4 bundles, small margins). The 5%-strike double-or-10 side-observation (n = 5). The fixed paper wrapper's ability to show a stable gap (too early to tell).
- **Very low:** Setup A stock-side filter (untested). Extension cuts, sub-$10 rebounds, slow-buying signals, and any rule built from extremes lists.

### Agent 3's final notes (not passed on)

# TRADING PLAYBOOK (updated after bundle 6 of the new round)

## 1. MY CURRENT STRATEGY

**Status: paper trading only. No live trades, no sizing.** No rule has yet passed its pre-committed test in two consecutive bundles. Bundle 6 failed the one stock-level test I had set, and the 30-day double-or-10 cell now has a negative median in two of its three bundles.

### Default
- **No trade** unless a candidate clears a rule in this section. Nothing currently does.
- **Stock-level drift is near zero.** All 250 candidates in bundle 6 averaged +0.5% over 10 sessions (median +0.7%). Bundle 5 was similar (average +0.9%, median +0.4%). Any option structure has to beat this, and the median option trade has lost money in both recent bundles.
- **Option wrappers drive the P&L variance, and they drag the median down.** Bundle 6 paper P&L was +14,766 on 55 trades, but the median trade was -29.4% and only 42% won. Positive P&L came from a small number of right-tail trades, not from a repeatable median.

### Stock-level ratings: no rule
- **Rating +1 is dropped as a trade signal.** Its pre-committed test required +1 to beat -1 on median 10-session return by at least 1 point in bundle 6. Actual result: +1 median -0.1%, -1 median -0.3%, gap +0.2 points. The test failed.
- **Rating history (+1 minus -1 median gap):** bundle 1 and 2 favored -1; bundle 3 +0.6, bundle 4 +0.5, bundle 5 +2.9, bundle 6 +0.2. The gap has not been large or consistent enough to act on.
- **Rating +0 had the best median in bundle 6** (+1.2%, n=93), and +0 was roughly flat in bundle 5. Ratings do not separate outcomes reliably.
- **Rating -2** (n=8 in bundle 6: average +3.4%, median +1.8%; n=1 in bundle 5: +20.1%; n=4 in bundle 4) is the only rated-negative group with a positive return. Sample is far too small to trade, and I'm not using it either way. Watch it, and note it is the opposite of what the rating scale implies.
- **Do not trade any stock-level rating** until the full-distribution bucket test (section 3, item 1) is run.

### Option candidate: 30-day, 5% OTM call, double-or-10 exit (watch only, downgraded)
- **Instrument:** call, strike about 5% above price at entry. Expiry 30 days. Entry at signal-day close. Exit at double-or-10 if it fires; otherwise system default exit. Size flat. Assume the option can go to -100%.
- **Evidence by bundle:**

| Bundle | n | Average | Median |
|---|---|---|---|
| 4 | 6 | +17.3% | -13.7% |
| 5 | 8 | +111.0% | +94.4% |
| 6 | 36 | +17.9% | -38.1% |

- **Read:** this is now the largest cell I have, and its median is negative in bundle 6 (n=36), the most reliable reading so far. Bundle 5's positive median does not replicate. The average is positive only because of a few very large winners. **Not a rule. Not trading.** It moves from "candidate" to "paper-tracking for falsification."
- **Confidence:** low that it has any positive median. Keep tracking because the right tail is real, but the entry signal is not identified.

### Other 30-day option cells (small watch, not rules)
- **30d 0% OTM, hold 10 sessions:** bundle 4 median -44.9% (n=14), bundle 5 +28.6% (n=4), bundle 6 +20.9% (n=5). Mixed. Watch only.
- **30d 10% OTM, hold 10 sessions:** bundle 6 median +69.4% (n=4). No other bundle. Too small.
- **30d 0% OTM, double-or-10:** bundle 5 +104.9% (n=3), bundle 6 -27.2% (n=7). Same problem as the 5% OTM cell: the median flipped sign. Watch only.
- **Single-trade cells** (30d 5% hold-10 -100%, 30d 10% dd10 -50%, 30d 15% dd10 -27%): meaningless alone.

### Structures ruled out
- **14-day calls, any strike:** median near -100% in every bundle. Dropped.
- **Spike, no news = 1:** no benchmark-beating cell in any bundle. Avoid. Appeared on both winners and losers in bundle 6.
- **Dip-buying with calls:** worst cells in earlier bundles. Avoid.
- **Put crowding as bearish signal:** no effect in any bundle. Ignore.

### Benchmark: 90-day, 5% OTM call, hold 10 sessions (reference only)
- Median by bundle: +46.1% (1), -7.5% (2), -25.4% (3), -46.2% (4), -23.9% (5). No 90-day trades in bundle 6.
- Negative median in four of five bundles. Keep as the reference for any option comparison. Do not trade.

### Price band (open, no rule)
- Bundle 4 90-day trades over $50 were positive. Bundle 5 visible over-$50 trades were mostly negative.
- Bundle 6 had large winners in every band (over $50 and under $10 both had +89% and +60% stock-level moves in extremes), and the 30-day double-or-10 losses fell across bands. No usable separation.
- **Confidence: very low.** Not a rule.

---

## 2. WHAT I TESTED IN BUNDLE 6

### Results
- **Paper P&L:** +14,766 on 55 trades. Average +26.8%, median -29.4%, 42% winners.
- **By cell:** the 30d 5% OTM double-or-10 cell (n=36) was the bulk of the trades, with average +17.9% and median -38.1%. Every other cell had n ≤ 7.
- **Read:** the P&L was positive for the second bundle in a row, but the median trade lost money both times. The P&L is a right-tail result and is not evidence of a repeatable edge.

### Stock-level results
- **Full pool:** average +0.5%, median +0.7%.
- **Rating +1 (n=67):** average -0.2%, median -0.1%.
- **Rating +0 (n=93):** average +1.3%, median +1.2%.
- **Rating -1 (n=82):** average -0.2%, median -0.3%.
- **Rating -2 (n=8):** average +3.4%, median +1.8%.
- **Read:** no rating separated outcomes meaningfully. The pre-committed +1 test failed.

### Extremes (hypotheses only, selected on outcome)
- **Momentum winners:** stocks with 20-day gains of +40% to +78%, price above ma20 and ma50, call buying well above normal, and several with news. Some returned +40% to +89% over 10 sessions.
- **Momentum losers:** many also had high calls ratios, strong 20-day gains (for example +50%) and then fell 25% to 41%. Momentum did not separate winners from losers in this bundle.
- **Deep-drawdown names:** several rated -1 with 20-day drops of -25% to -37% rebounded +26% to +61%. Others with similar drops fell -24% to -41%. Rebound did not separate either.
- **Read:** neither the bundle 4-5 momentum pattern nor the bundle 3 rebound pattern holds on this bundle's extremes. The extremes list is noisy and outcome-selected. I cannot use it as a rule source.

### Trade-level observations
- The 30-day double-or-10 winners tended to have high calls 5-day averages (often 3 to 20x normal), multiple call-heavy days in the last 5 sessions, and news in the prior week. Losers in the same cell had similar features. I have not yet compared winners and losers within the cell on a full feature table.
- Put-side features (puts 5d avg, p/c) show no consistent pattern.

---

## 3. WHAT I WILL TRY NEXT

1. **Full-distribution stock test (still not run; highest priority).** Bundles 5 and 6 did not give me the full candidate table in bucketed form, so I cannot run it yet. Request or build the full table of all candidates with 10-session returns. Tabulate median and share-of-winners by:
   - 20-day %: below -20, -20 to 0, 0 to +20, above +20.
   - RSI: below 30, 30 to 70, above 70.
   - vs ma50: below -15, -15 to 0, 0 to +15, above +15.
   - Rating (+1, +0, -1) within each bucket.
   - Rule: n ≥ 60 per bucket. A stock-level rule passes only if the same direction holds in two consecutive bundles with a median gap of at least 1 point.

2. **Retire the +1 hypothesis unless the full-distribution test revives it.** It failed its pre-committed test. Do not reopen it on bundle 6 data.

3. **30-day double-or-10 falsification test.** Track every 30-day 5% OTM and 0% OTM double-or-10 entry. Decision rule:
   - If the median stays negative over the next bundle with n ≥ 20, drop the cell.
   - If it turns positive with n ≥ 20, I will treat it as a candidate for a second confirming bundle.
   - Log exit timing: sessions to double or 10x, and what happened when the rule did not fire.

4. **Winners vs losers within the 30-day double-or-10 cell.** Using the logged features at entry (calls 5d avg, call days 2x+, calls 20d, days since spike, vs ma50, news 7d, RSI, price band), compare the top and bottom halves of the cell. This is the only way to find out whether any entry feature separates the right tail from the losers. Require n ≥ 20 per split.

5. **Wrapper comparison on identical entries.** On every entry, compare the option result against the stock return over the same window at 30 and 90 days. The gap separates option drag from the signal. Goal: a structure that keeps a stock-level median without premium drag. Include stock as the baseline.

6. **Trend and call-flow filter, logged at entry.** Record calls 5d avg, calls 20d, vs ma50, vs ma20, RSI, and days since spike for every trade. Split on calls 5d avg (above 1 vs ≤ 1) and vs ma50 (above 0 vs ≤ 0). Require n ≥ 30 per cell.

7. **Price band (full data).** Log band for every trade. Compare under $10, $10 to $50, over $50 with n ≥ 20 per band.

8. **Regime check.** Compare outcomes by market 20d sign across all six bundles. Market 20d was mixed in bundle 6, and regime may explain why rules worked in some bundles and not others.

9. **Rating -2 watch.** Keep logging. If the -2 group stays positive with n ≥ 30 in another bundle, test whether the rating scale is inverted at that end. Do not trade it before then.

10. **Stay out of 14-day calls.** Paper-track 30-day calls only.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Held up (low confidence)
- **30-day 5% OTM double-or-10 positive average** in bundles 4, 5, and 6 (the average is positive in all three). The median was positive only in bundle 5. Watch only.
- **30-day hold-10 option cells (0% and 10% OTM)** had positive medians in bundles 5 and 6. Bundle 4 at 0% was strongly negative. Watch only.
- **90-day 5% OTM benchmark median negative** in four of five bundles. Keep as reference.
- **Stock-level pool drift** slightly positive (median +0.4% to +0.7%) in bundles 5 and 6. Too small to trade after option costs.

### Dropped or weakened
- **Rating +1 as a stock-level trade:** failed its pre-committed test in bundle 6 (median gap +0.2 vs required +1.0). Dropped.
- **Rating -1 as a trade:** retired. Median -0.3% in bundle 6, -1.1% in bundle 5.
- **Momentum direction (extremes):** held in bundles 4 and 5, not in bundle 6. Hypothesis only, outcome-selected. Weakened.
- **Rebound from deep drawdowns (bundle 3 hypothesis):** not supported in bundle 6 extremes. Dropped unless the full-distribution test supports it.
- **30-day double-or-10 as a rule:** median negative in bundles 4 and 6, positive in 5. Not a rule. Still tracked.
- **Price band over $50 at 90 days:** no usable signal. Not a rule.
- **14-day calls:** dropped.
- **Spike, no news:** avoid. No separation in bundles 5 or 6.
- **Dip-buying with calls:** avoid.
- **Put crowding as a bearish signal:** ignored.
- **Extremes lists as rule sources:** use only to generate hypotheses. Bundles 3 through 6 have disagreed on direction.

### Open questions
- Does any stock-level feature (20-day move, RSI, vs ma50) predict 10-session returns on the full distribution?
- Do the 30-day double-or-10 winners share an entry feature that the losers lack, or is the right tail random among call-heavy names?
- Does any call structure reach a positive median at 30 or 90 days, or does the premium always exceed the stock edge?
- Does the price band or market regime explain the disagreements between bundles?
- Is the paper P&L positive in bundles 5 and 6 repeatable, or is it a few large trades? So far, the median trade has lost money in both.

### Agent 4's final notes (not passed on)

# TRADING NOTES (rewritten after bundle 6 of 6, committee editor version)

## 1. MY CURRENT STRATEGY

**Status: no validated edge in options. No option trades are permitted. The stock-signal test is still unscored.**

Six bundles are in. The option book has lost money on a median basis in five of six bundles. Bundle 6 was the worst so far: 32 trades, average -14.8%, median -38.1%, 41% winners, total -$4,724. The only positive option median (30-day ATM, bundle 5) rests on four trades. I also traded 30-day ATM calls in bundle 6 even though my notes had moved that structure to paper-only. That was a rule breach. Section 1d now has an enforced gate.

### 1a. Paper Test A (primary): stock long on a call-activity signal

- **Signal (all three required):**
  - calls 5d avg > 1
  - call days 2x+ ≥ 2 (of the last 5 sessions)
  - vs ma50 % > 0
- **Instrument:** the stock, long, on paper. No options.
- **Entry:** the close on the signal day, logged from my own price record.
- **Exit:** the close 10 sessions later. No stops, no targets.
- **Log per signal:** entry price, exit price, stock return, S&P 500 fund return over the same 10 sessions, excess return, price band, vol20 %, 20d %, vs ma20 %, calls 20d, call days 2x+ 20d, days since spike.
- **Scoring:** the bundle reports give option returns and rating outcomes, not stock returns by signal. Test A cannot be scored from the reports and has to be logged from my own closes.
- **Promotion rule:** consider real money only if excess return has a positive median in at least two bundles, with n ≥ 30 signals per bundle. Currently: 0 bundles scored, so no promotion.
- **Confidence in the signal itself:** none yet. It is a hypothesis.

### 1b. Paper Test B: option wrapper comparison (paper only)

- For every signal, record the stock return next to the option return for:
  - 30-day ATM calls
  - 90-day ATM calls
  - 90-day 5%-OTM calls
- **Purpose:** find whether any call structure keeps a positive median across bundles. None has so far.

### 1c. Paper Test C: fast spike vs sustained buying (paper only)

- **Fast spike:** days since spike = 0, calls 5d avg ≥ 5, calls 20d < 3.
- **Sustained build:** calls 20d ≥ 5, call days 2x+ 20d ≥ 6, calls 5d avg between 1 and 3.
- **Instrument:** 30-day ATM calls on paper, plus the matching stock long on paper. Hold 10 sessions.
- **Evidence so far:** see section 2. Both shapes have lost money in the option data. Sample is too small to conclude.

### 1d. Option structures

| Structure | Status | Basis |
|---|---|---|
| 30-day ATM (+0%) calls | **Ban from trading. Paper only.** | Bundle 6: n=32, median -38.1%, average -14.8%. Bundle 5: n=4, median +47.2%. Bundles 1–4: negative medians. Negative median in 5 of 6 bundles. The positive bundle rests on four trades. |
| 90-day ATM (+0%) calls | **Stop.** Paper only. | Bundle 3 n=2, bundle 4 n=19 (median -20.1%), bundle 5 n=1. Combined median negative. |
| 90-day 5%-OTM calls | **Ban. Paper only.** | Negative median in bundles 2, 3 (small n), 5 and bundle 4 median positive only on n=3. |
| 30-day 5%-OTM calls | **Hard ban.** | Negative medians in bundles 1, 3. Bundle 5's average came from one +427% and one -100%. |
| 14-day expiries | **Hard ban.** | Bundle 3, both -100%. |
| Any strike 10%+ OTM | **Hard ban.** | |
| Double-or-10 exits | **Not used.** | Large single wins, no positive median. |

**Order gate (enforced from bundle 7):** before any option order, check the structure against this table. If the check cannot be done, do not trade. Bundle 6 traded a structure the notes had already moved to paper-only. Under this gate, that trade would not have been placed.

### 1e. Ratings: log only, no trade filter

- Bundle 6 outcomes (10-session stock return, all candidates rated):
  - **+1:** n=48, average -1.5%, median +0.7%. Average is negative because of a few large losers.
  - **+0:** n=102, average +0.8%, median +0.6%.
  - **-1:** n=93, average -0.3%, median +0.5%.
  - **-2:** n=7, average +19.4%, median +7.6%.
- Ordering across the bundles:
  - +1 was the weakest bucket by average in bundle 6 and the strongest by average in bundle 5. No stable ordering.
  - -2 has had positive average returns in bundles 5 and 6 (combined n=16, both medians positive). It was bearish-correct in bundles 3 and 4.
- **Rule:** no rating bucket is a long or short filter. Keep -2 as its own column. It is the only bucket with a consistent positive median in the last two bundles, but n=16 across two bundles is not enough to act on.

### 1f. Working explanation for the option losses

- Across the bundle 6 trades, the typical loss was close to total (many trades at -80% to -100%) while the candidate universe averaged +0.5%. Winners were concentrated in a few large moves.
- The most likely mechanism is that I bought calls after volume spikes, which means buying premium after implied volatility had already risen, and then holding through decay. If the stock did not move enough in 10 sessions, the option lost most of its value.
- This is a hypothesis. Entry implied volatility is still not in the reports, so it cannot be tested yet.
- Implication: even when the stock is roughly flat or modestly up, buying spike-driven calls has lost money. The stock-only test (Test A) is the cleaner way to find out whether the signal has any edge.

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

**Overall:** -$4,724 on 32 trades, average -14.8%, median -38.1%, 41% winners (about 13 of 32). Every trade was a 30-day ATM call held 10 sessions.

**Candidate universe (250 stocks):** average +0.5% over 10 sessions, median +0.7%. This is a small positive baseline. It does not explain a median option loss of -38%.

**Descriptive observations on the trades (no rules):**

- **Fast spike shape (Test C, fast spike):** about four trades fit the rule across bundles 5 and 6.
  - Bundle 6: three trades. Returns about -93%, -80%, and +98%.
  - Bundle 5: the -100% trade, which had calls 5d avg 42.9, no calls 20d history (blank), and RSI 85.
  - Combined median is roughly -87%, with one win out of four. Too small to conclude, but the direction is negative.
- **Sustained build shape (Test C, sustained):** one bundle 6 trade fit (calls 20d 5.3, call days 2x+ 20d 7, calls 5d avg 1.1), and it lost about -91%. A near-miss with calls 5d avg 3.4 lost about -85%. Sample is one trade.
- **Overbought entries:** several trades had RSI above 75 and 20d moves above +20%. Their outcomes were mixed, with large losses and several large wins. No clean split.
- **Price band:** losses appeared in all three bands. The under-$10 and over-$50 bands both produced large wins and large losses. No consistent split.
- **Spike, no news flag:** present in winners and losers. Not a usable filter.
- **RSI:** winners and losers both had high RSI. Still not a usable filter.
- **Market regime:** trades were placed while the S&P 500 fund ranged from about -8% to +6% over 20 sessions. Not used as a filter.
- **Candidate tails:** biggest losers were mostly names that had fallen 20–50% over 20 sessions, with vol20 % of 4–12. Biggest winners were a mix of short-dated call spikes and oversold rebounds. Dispersion was high in both directions. Extremes are not a signal.

**Test status after bundle 6:**

- **Test A (stock signal):** not scored. Must start logging entry and exit closes now. No scoreable data from the reports.
- **Test B (option wrapper comparison):** 30-day ATM is now negative in five of six bundles. 90-day 5%-OTM is negative in most bundles. No structure has a positive median in two bundles.
- **Test C (fast spike vs sustained):** tiny samples, both shapes negative in this data. Not decisive.
- **Overbought-chase flag on stock:** not run.
- **Volatility split on stock (vol20 % below 4 vs 4 or above):** not run.

## 3. WHAT I WILL TRY NEXT (bundle 7 stocks)

1. **Run Test A from my own entry and exit closes.** Log every signal that meets calls 5d avg > 1, call days 2x+ ≥ 2, and vs ma50 % > 0. Record stock return, S&P 500 fund return over the same 10 sessions, and excess return. Target n ≥ 30 signals. This is the main question.
2. **Stop all option trading until a structure passes the promotion rule.** Paper-record 30-day ATM, 90-day ATM, and 90-day 5%-OTM returns beside every stock signal (Test B), but place no orders.
3. **Keep Test C on paper.** Log fast-spike and sustained-build entries separately. Promote nothing until the two shapes separate across two bundles.
4. **Split Test A by volatility.** vol20 % below 4 vs 4 or above. Log both groups even if neither is decisive.
5. **Run the overbought-chase flag on stock.** Flag: 20d % > +20 and vs ma20 % > +15. Compare excess returns for flagged and unflagged signals over the same 10 sessions.
6. **Enforce the order gate in section 1d before any option trade.** No 30-day 5%-OTM, no 14-day, no 10%+ OTM, and no 30-day ATM (now banned).
7. **Keep logging ratings with -2 as its own column.** Check whether -2 keeps a positive median in bundle 7. If it does, it becomes a candidate for a stock test (not an option test).
8. **Add entry implied volatility to the logging.** Without it, I cannot tell whether premium cost explains the option losses. Until it is logged, treat the decay explanation as untested.

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

**Held up (weakly to moderately):**

- **30-day ATM calls:** negative median in five of six bundles (bundle 6 n=32, median -38.1%). Bundle 5's positive median rests on n=4. Confidence that this structure is not tradeable: moderate-to-high. **Moved to ban.**
- **90-day 5%-OTM calls:** negative median in most bundles. Confidence that it is not tradeable: moderate.
- **30-day 5%-OTM and 14-day expiries:** consistently negative or too few trades to matter. Confidence in the ban: moderate.
- **Option results are dominated by a few large trades in both directions.** The median is the better guide than the average or total profit. Confidence: high.
- **The candidate universe average is small and positive (+0.5% in bundle 6, +0.9% in bundle 5).** A large option loss on the same universe points to structure (premium and decay) rather than direction alone. Confidence: moderate.

**Flipped or did not hold up:**

- **30-day ATM as a "stop" or "paper only" structure:** bundle 5 positive, bundle 6 strongly negative. Now banned from trading. Confidence in either direction: low until Test A and Test B are scored.
- **The +1 rating bucket as the weakest group:** weakest by average in bundle 6, strongest by average in bundle 5. No stable ordering. Confidence: none.
- **The -2 bucket as contrarian:** positive average in bundles 5 and 6, bearish-correct in bundles 3 and 4. Confidence: low.
- **Spike, no news flag:** present in winners and losers. Dropped as a filter.
- **RSI as a filter:** winners and losers both had high RSI. Dropped.
- **Price bands:** no consistent split across bundles. Treated as noise.
- **Double-or-10 exits:** large single wins, no positive median. Dropped.
- **News, analyst ratings, and extremes lists as triggers:** not used. The news-count split was not usable in bundle 5 and is not used here.
- **ITM 90-day test from earlier notes:** not run. The reports do not provide ITM strikes.

**Avoid (consistent across the data):**

- Buying calls after a single-day volume spike, especially with RSI above 75. Fast-spike shape lost in both bundles where it appeared.
- Buying calls on dip names already down 20–50%.
- Any option structure with a negative median in the most recent two bundles.
- Trading any structure that is listed as paper-only without passing the order gate.

**Open questions:**

- Does Test A (stock signal) have a positive excess-return median? Main question for bundle 7.
- Is entry implied volatility the main driver of the option gap? Cannot be answered until it is logged.
- Does sustained call buying separate from fast spikes once samples are larger? Test C.
- Does the overbought-chase flag predict stock underperformance?
- Does vol20 % separate stock outcomes better than the price band?
- Does -2 keep a positive median in bundle 7? If yes, it becomes a stock-test candidate, not an option trade.


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

