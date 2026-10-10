# Committee generations (2026-10-10 19:56 UTC)

Total spent on all agent runs: $47.28. Candidate pool: {'train': 2998, 'holdout': 2000, 'score': 1439, 'test': 2720}.

Four agents train independently on six stock bundles; code scores their rules; an editor writes the
notes passed on. The scoring run trades blind months with the editor's notes. "Random" makes the same
number and kind of trades on random candidates in the same weeks. Rating correlation: does a higher
rating go with a better 10-session stock return (0 = no skill, ranges are 95%). Every trade is $1,000.

## Runs

| gen | who | phase | trades | profit $ | random profit $ | mean % | win % | rating corr (95% range) | top rated % | bottom rated % | unreadable | cost $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8 | agent1 | train | 222 | -38416.2 | -28105.2 | -17.3 | 28.4 | -0.032 (-0.078 to 0.014) | -0.67 | 1.71 | 6/151 | 0.5875 |
| 8 | agent2 | train | 211 | -11921.3 | -15614.0 | -5.65 | 32.7 | -0.018 (-0.056 to 0.025) | -0.43 | 1.48 | 2/151 | 0.5645 |
| 8 | agent3 | train | 222 | 17330.8 | -11499.6 | 7.81 | 34.2 | 0.041 (-0.002 to 0.088) | 0.1 | 1.12 | 6/151 | 0.5789 |
| 8 | agent4 | train | 230 | -15958.9 | -14053.0 | -6.94 | 29.1 | -0.004 (-0.049 to 0.043) | -0.27 | 1.46 | 6/151 | 0.6101 |
| 8 | scorer | score | 270 | -42963.2 | -58644.0 | -15.91 | 28.5 | -0.027 (-0.08 to 0.043) | -0.13 | 0.43 | 2/144 | 1.1849 |
| 9 | agent1 | train | 217 | -20821.6 | -25128.6 | -9.6 | 33.6 | 0.004 (-0.059 to 0.068) | 1.45 | 1.17 | 8/151 | 0.506 |
| 9 | agent2 | train | 201 | -19809.1 | -15637.8 | -9.86 | 33.8 | -0.003 (-0.055 to 0.055) | 2.12 | 1.71 | 4/151 | 0.4711 |
| 9 | agent3 | train | 239 | 5411.8 | -17972.8 | 2.26 | 30.5 | 0.03 (-0.027 to 0.092) | 1.74 | 1.37 | 0/151 | 0.5014 |
| 9 | agent4 | train | 214 | -13103.7 | -18339.8 | -6.12 | 29.4 | -0.004 (-0.039 to 0.031) | 1.23 | 1.67 | 9/151 | 0.5696 |
| 9 | scorer | score | 135 | -17955.1 | -26095.5 | -13.3 | 28.9 | -0.046 (-0.104 to 0.021) | -0.51 | 0.92 | 5/144 | 0.9221 |
| 10 | agent1 | train | 198 | -11189.8 | -18869.4 | -5.65 | 35.4 | 0.036 (-0.034 to 0.095) | 1.89 | 1.13 | 2/151 | 0.519 |
| 10 | agent2 | train | 191 | -16867.5 | -16406.9 | -8.83 | 32.5 | 0.066 (-0.003 to 0.123) | 1.83 | 0.81 | 2/151 | 0.477 |
| 10 | agent3 | train | 176 | 524.9 | -16667.2 | 0.3 | 36.4 | 0.027 (-0.03 to 0.072) | 0.42 | 1.29 | 5/151 | 0.5404 |
| 10 | agent4 | train | 189 | -28697.0 | -14685.3 | -15.18 | 32.8 | 0.006 (-0.043 to 0.059) | 0.5 | 1.75 | 6/151 | 0.4836 |
| 10 | scorer | score | 130 | -15387.2 | -24817.0 | -11.84 | 26.9 | -0.036 (-0.1 to 0.027) | 0.51 | 0.79 | 8/144 | 1.1136 |

## Luck check

- Different rules tested on training data so far: 118 (by the agents and the editor).
- Editor rules checked on the blind months: 24; passed clearly (whole 95% range above buying everything the same way): 0.
- Expected to pass by luck alone: about 0.6. Treat a pass as real only if it clearly beats that count and the rule keeps passing in later generations.

## Blind scoring trades by list (hindsight check)

The big-mover list was chosen for stocks that later had 3+ days up 15%, so results there can come
from hindsight alone. The wide list (chosen from January 2024 data only) is the honest test.
Random = the same kind of trades on random candidates from the same list in the same weeks.

| gen | list | trades | mean % | random mean % | profit $ | random profit $ |
|---|---|---|---|---|---|---|
| 8 | big movers (hindsight) | 154 | -11.50 | -13.87 | -17,707 | -21,360 |
| 8 | wide (honest) | 116 | -21.77 | -27.93 | -25,256 | -32,399 |
| 9 | big movers (hindsight) | 110 | -9.17 | -12.40 | -10,092 | -13,644 |
| 9 | wide (honest) | 25 | -31.45 | -24.83 | -7,863 | -6,208 |
| 10 | big movers (hindsight) | 102 | -6.54 | -15.82 | -6,674 | -16,138 |
| 10 | wide (honest) | 28 | -31.12 | -18.71 | -8,713 | -5,239 |

## Generation 10

### Editor's rules, tested on all training months and bundles

- S5 exact 30d ATM (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0: buy the 30-day call 0% above the price, exit hold10): 57 trades, average +48.4% (95% range +5.9% to +85.7%, resampling whole weeks), median +5.8%, 53% winners. Buying every candidate the same way: -11.8%. Beat that in 4 of 6 bundles; first half of the months +47.8%, second half +49.2%.
- S5 entries as stock 10d (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0: buy the stock, hold 10 sessions): 80 trades, average +5.3% (95% range -1.1% to +12.3%, resampling whole weeks), median -2.2%, 48% winners. Buying every candidate the same way: +0.6%. Beat that in 5 of 6 bundles; first half of the months +2.7%, second half +8.6%.
- S5 plus market 20d up (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 46 trades, average +54.2% (95% range +11.6% to +98.6%, resampling whole weeks), median +13.9%, 56% winners. Buying every candidate the same way: -11.8%. Beat that in 5 of 6 bundles; first half of the months +44.0%, second half +66.4%.
- S5 deeper dip 5d<-1.5 (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < -1.5: buy the 30-day call 0% above the price, exit hold10): 17 trades, average +55.3% (95% range -20.4% to +136.9%, resampling whole weeks), median +12.8%, 53% winners. Buying every candidate the same way: -11.8%. Beat that in 3 of 3 bundles; first half of the months +53.6%, second half +58.3%.
- S5 at 90d ATM (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0: buy the 90-day call 0% above the price, exit hold10): 20 trades, average +20.0% (95% range -8.7% to +46.3%, resampling whole weeks), median +7.6%, 60% winners. Buying every candidate the same way: -8.4%. Beat that in 4 of 4 bundles; first half of the months -14.3%, second half +61.9%.
- S1 at 90d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 90-day call 0% above the price, exit hold10): 45 trades, average -1.0% (95% range -16.6% to +16.6%, resampling whole weeks), median -14.5%, 40% winners. Buying every candidate the same way: -8.4%. Beat that in 3 of 5 bundles; first half of the months +4.5%, second half -3.3%.
- S1 plus call days 2+ (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and call days 2x+ >= 2: buy the 30-day call 0% above the price, exit hold10): 127 trades, average +35.5% (95% range +3.3% to +76.1%, resampling whole weeks), median -17.5%, 42% winners. Buying every candidate the same way: -11.8%. Beat that in 6 of 6 bundles; first half of the months +38.8%, second half +33.3%.
- S1 low option cost (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and option cost % < 12: buy the 30-day call 0% above the price, exit hold10): 132 trades, average +24.4% (95% range -5.7% to +64.1%, resampling whole weeks), median -29.8%, 35% winners. Buying every candidate the same way: -11.8%. Beat that in 5 of 6 bundles; first half of the months +16.7%, second half +28.9%.

### The same rules on the blind scoring months (never shown to agents)

- S5 exact 30d ATM (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0: buy the 30-day call 0% above the price, exit hold10): 34 trades, average +17.5% (95% range -46.0% to +95.9%, resampling whole weeks), median -55.2%, 26% winners. Buying every candidate the same way: -15.4%. Beat that in 2 of 6 bundles; first half of the months +56.3%, second half -6.5%.
- S5 entries as stock 10d (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0: buy the stock, hold 10 sessions): 45 trades, average +0.7% (95% range -6.2% to +8.8%, resampling whole weeks), median -4.0%, 49% winners. Buying every candidate the same way: +0.6%. Beat that in 2 of 6 bundles; first half of the months +8.9%, second half -4.3%.
- S5 plus market 20d up (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 31 trades, average +26.1% (95% range -39.9% to +104.1%, resampling whole weeks), median -49.1%, 29% winners. Buying every candidate the same way: -15.4%. Beat that in 2 of 6 bundles; first half of the months +65.8%, second half +0.9%.
- S5 deeper dip 5d<-1.5 (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < -1.5: buy the 30-day call 0% above the price, exit hold10): 2 trades, average -77.5% (too few trades or weeks for a range), median -77.5%, 0% winners. Buying every candidate the same way: -15.4%. Beat that in 0 of 0 bundles.
- S5 at 90d ATM (when 20d % >= 20 and call days 2x+ >= 2 and market 5d % < 0: buy the 90-day call 0% above the price, exit hold10): 11 trades, average -39.2% (95% range -62.3% to -22.0%, resampling whole weeks), median -50.0%, 9% winners. Buying every candidate the same way: -7.2%. Beat that in 0 of 0 bundles; first half of the months -56.8%, second half -29.1%.
- S1 at 90d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 90-day call 0% above the price, exit hold10): 44 trades, average +6.6% (95% range -22.2% to +45.6%, resampling whole weeks), median -17.5%, 32% winners. Buying every candidate the same way: -7.2%. Beat that in 4 of 6 bundles; first half of the months -11.1%, second half +24.4%.
- S1 plus call days 2+ (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and call days 2x+ >= 2: buy the 30-day call 0% above the price, exit hold10): 111 trades, average -7.4% (95% range -32.0% to +20.4%, resampling whole weeks), median -44.5%, 28% winners. Buying every candidate the same way: -15.4%. Beat that in 3 of 6 bundles; first half of the months -9.3%, second half -5.4%.
- S1 low option cost (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and option cost % < 12: buy the 30-day call 0% above the price, exit hold10): 112 trades, average -19.3% (95% range -32.3% to -7.2%, resampling whole weeks), median -37.0%, 26% winners. Buying every candidate the same way: -15.4%. Beat that in 2 of 6 bundles; first half of the months -27.7%, second half -11.7%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

*Committee editor's synthesis. Inputs: the previous playbook, four traders' final notes, and the code-tested scorebook for every rule the traders stated. Where a trader's figure and the scorebook differ, the scorebook is used.*

**Conventions**
- Returns are per-trade returns on premium (options) or on price (stock), bought on the signal day at the close and held 10 sessions unless noted.
- "Benchmark" means buying every candidate with the same instrument, expiry, strike and exit.
- "Range" is the 95% range from resampling whole weeks.
- "Halves" are the first and second half of the sample by month. This is a time split, not first and second half of each month. One trader misread it as a calendar-of-month effect.
- "x of 6" is the number of bundles in which the rule beat its benchmark.
- "Wide list" is the honest, no-hindsight sample. About 60% of candidates come from a list chosen because the stocks later had several +15% days. Strong-momentum rules look better on the hindsight part for that reason alone.
- Every rule is written with exact conditions so it can be restated and scored.

**Test-environment facts**
- **Costs are charged everywhere**, including every benchmark. Each side costs 5% of premium or $0.05 a share, whichever is larger. A round trip is at least 10% of premium, and much more on cheap options.
- **Calls that expire inside the hold are not offered**, and the scorebook skips them. The "-100% on a stock that rose" marks were real expiries, not bad marks.
  - Agent 4's "model-risk audit" worry is answered.
  - Old figures that included these trades are history.
- **Available for trades and rules:**
  - Long calls (30-day or 90-day; 0%, 5% and 10% above the price), held 10 sessions for options.
  - Call spreads (buy one strike, sell a higher one). One scored spread rule had a benchmark of -45%, so the structure is costly.
  - Stock rules scored over 5, 10 or 20 sessions, so the stock edge can be measured separately from the option.
- **Not available:** puts, short selling, in-the-money calls, option bid/ask or volume, daily option paths, earnings dates, sector, market cap. Data is daily closes only.
- **Check count:** the traders ran 24, 25, 20 and 27 rule checks (96 in all), so some lucky results are expected. Prefer results that show up across bundles, both halves, the wide list and several traders.

---

## 0. BOTTOM LINE

1. **The average call loses.** Benchmarks for buying every candidate, held 10 sessions, costs included:

| Structure | Benchmark average |
|---|---|
| 30-day ATM | -11.8% (wide list only: -19.5%) |
| 30-day 5% above | -12.2% |
| 30-day 10% above | -17.7% |
| 90-day ATM | -8.4% |
| 90-day 5% above | -7.4% |
| 90-day 10% above | -9.7% |
| 30-day call spread, 0% to +10% | -45.0% |

2. **Only rules that pick very strong, trending names with active call flow turn the option average clearly positive.** The two best are:
   - **S1** (strong momentum plus volume, up market): +28.4%, 6 of 6, both halves positive, median -21.5%.
   - **S5** (new this generation: strong trend plus call-flow days in a down 5-day market): **+48.4%**, range +5.9% to +85.7%, **median +5.8%**, both halves about +48%, 4 of 6.
   - S5 is the first 30-day call rule with a positive median and a range that excludes zero. It has 57 trades, one trader found it, and its wide-list sample is only 9 trades. Treat it as the top lead, not a settled rule.
3. **Stock-level edges are real but tiny.**
   - The best stock rules have medians of +0.8% to +1.6% over 10 sessions, against about +0.1% to +0.6% for buying everything.
   - Several have positive halves and positive wide-list results (section 1B).
   - A round trip on an option costs at least 10%, so these edges cannot be bought with an ordinary option. Four separate tests of "stock edge as a call" lost (section 2).
4. **Momentum edges are weakest on the no-hindsight list.** Several momentum stock rules had a negative wide-list median:
   - P-E: -1.8%.
   - P-A: -3.1%.
   - Rule C: -7.5% on 2 trades.
   - S1 as a stock with price over $50 and no market gate: 42 trades, +1.4%, median -0.5%, 1 of 5.
   - **Every option rule built on momentum must report its wide-list number.** S1's has not been seen yet.
5. **Thin call flow is the one avoid every trader and the scorebook agree on.** The pattern is 0 to 1 of the last 5 days at 2x+ calls, or no short-dated call activity. In both cases the stock itself underperforms.
6. **Ratings are noise.** In four traders' hands the ratings sign flipped across bundles. Ignore them.

---

## 1. STRATEGY: SETUPS WORTH TRADING (paper, or small flat size)

Take every signal that passes. Skipping signals loses the few large winners that make the averages.
- Spread premium over many names at flat small size, and never add after wins.
- Size so that -100% on every open position is survivable.
- The rules below overlap heavily because they pick the same trending names. Do not count them as independent confirmations.

### 1A. Option rules (current scorebook, costs included, expiring contracts excluded)

**S5. Strong trend plus call-flow days in a down 5-day market, 30-day ATM (new; credit Agent 3).**
- Rule: 20d % ≥ 20 and call days 2x+ ≥ 2 and market 5d % < 0. Buy the 30-day call 0% above the price.
- Result: 57 trades, **+48.4%** (range +5.9% to +85.7%), **median +5.8%**, 53% winners. Benchmark -11.8%, 4 of 6. Halves **+47.8% and +49.2%**.
- Wide list only: 9 trades, +15.9% average, median -68.0%, against -19.5%. This is too thin to judge, and the median there is bad.
- The same trader's stock-only rules in this family were weak:
  - Rule C, stock: 23 trades, median -2.7%.
  - Trend above 40 with market 5d < 0, stock: 53 trades, median -2.5%.
  - Broad-breadth trend, stock: 78 trades, median -1.2%.
- So S5's edge is an option-convexity effect on big moves, not a stock edge. It has not been tested as a stock rule.
- Tension with S1: S5 wants the market's last 5 days down, while S1 wants the market's last 20 days up. The two use different horizons, and each may be selecting a pullback within a strong market. The market-5d × market-20d interaction has not been mapped (section 4).
- Priority: restate S5 exactly, then test its variants (section 4).

**S1. Strong-momentum gate, 30-day ATM.**
- Rule: 20d % ≥ 20 and vs ma50 % ≥ 15 and market 20d % > 0 and shares ≥ 1. Buy the 30-day call 0% above the price.
- Result: 138 trades, **+28.4%** (range +0.5% to +68.4%), median -21.5%, 39% winners. Benchmark -11.8%, **6 of 6**. Halves +26.4% and +29.5%.
- It is the most consistent option rule. The range barely clears zero, so the size is uncertain. The stock version of the same gate has a thin edge (+6.0% average, +1.4% median over 168 trades in the old tally, shrinking to about +2.7% in the latest bundle).

| Variant | Trades | Average | Range | Median | Beat | Halves |
|---|---|---|---|---|---|---|
| **S1-tail** (20d % ≥ 40, vs ma50 % ≥ 15, market 20d > 0, shares ≥ 1) | 60 | **+35.5%** | -10.7% to +115.5% | **-16.1%** | 4 of 6 | +13.8% / +46.4% |
| **S1-nospike** (S1 without shares, plus days since spike ≥ 1) | 75 | +29.5% | -1.8% to +62.5% | -37.9% | 5 of 6 | +54.6% / +15.4% |
| **S1-flow** (20d % ≥ 20, vs ma50 % ≥ 15, market > 0, call days 2x+ ≥ 1; **30-day 5% above**, benchmark -12.2%) | 155 | +24.5% | -10.0% to +65.3% | -37.9% | 5 of 6 | +27.4% / +22.5% |
| **S1-cap** (20d % ≥ 20, vs ma50 % 15 to 40, market > 0, no shares condition) | 125 | +13.5% | -8.4% to +36.2% | -31.7% | 6 of 6 | +23.6% / +6.1% |
| **S1 with close vs vwap % ≥ 0.9** (no market gate, no shares condition) | 78 | +19.7% | | -28.4% | 5 of 6 | +33.3% / +10.3% |
| **S1 with shares < 1** (control, no market gate) | 45 | +18.2% | | -41.0% | 3 of 6 | +34.7% / +3.8% |

What the variants say:
- Shares ≥ 1 helps the median and the beat rate.
- Capping the trend at 40 hurts. Very extended names carry the average.
- Call-flow days ≥ 1 adds nothing on top of the trend gate.
- VWAP is neither a filter nor an exclusion.
- The stock-level "S1 cap" (20 to 40, vs ma20 ≤ 7, vwap ≤ 0.8) also failed Agent 1's pre-set test (median -2.2%).

**S2. Strong trend plus news, 30-day ATM.**
- Rule: vs ma50 % > 11.9 and news 7d ≥ 1.
- Result: 215 trades, **+15.1%** (range -7.2% to +42.0%), median -30.8%, 33% winners. Benchmark -11.8%, 5 of 6. Halves +2.2% and +24.4%.
- It is the best-sized rule with no market gate, and its first half is weak.

**S3. Sustained call buying with momentum and moderate IV, 30-day ATM.**
- Rule: calls 20d ≥ 1.5 and 20d % ≥ 10 and market 20d % > 0 and iv % < 60.
- Result: 123 trades, **+16.9%** (range -7.1% to +42.2%), median -37.1%, 4 of 6. Halves +23.0% and +11.8%.
- Without the iv gate it is weaker. The version with 20d % between 10 and 25 loses (-7.6%), and the "iv ≥ 60 after a surge" control was -3.5%.
- Very low IV is bad, so this is not simply "lower IV is better".

**S4. Cheap iv/realized with trend and news, 30-day 5% above.**
- Rule: iv/realized < 0.75 and news 7d ≥ 1 and 20d % > 0.
- Result: 138 trades, +12.8% (range -18.4% to +50.6%), median -55.6%, 4 of 6. Halves +1.8% and +27.5%.
- It is a tail-seeker with a very negative median.

**Option rules that did not transfer from stock signals** (all negative medians):

| Rule | Trades | Average | Median | Beat | Halves |
|---|---|---|---|---|---|
| Gate A (flow) as 30-day ATM call, IV ≤ 45 | 149 | -7.7% | -31.5% | 4 of 6 | +11.8% / **-30.9%** |
| High breadth (≥ 67.8) as 30-day ATM call | 269 | +2.9% | -30.1% | 4 of 6 | +6.7% / +2.3% |
| Bounce (market dip plus off high) as 90-day ATM call | 63 | -10.8% | -18.1% | 1 of 6 | +12.2% / -23.2% |

- On the wide list, the high-breadth call was -6.2% against -19.5% (a decent relative result, still negative).
- The Gate A call on the wide list was -17.9% against -19.5%.

### 1B. Stock-level rules (underlying edges; scored as shares, 10 sessions)

Use these to measure whether a signal has any edge before wrapping it in an option. The 10-session benchmark is +0.6% (wide list +0.1%).

| Rule (exact conditions) | Trades | Avg (range) | Median | Beat | Halves | Wide list (no hindsight) |
|---|---|---|---|---|---|---|
| **D1. Oversold in a market dip:** market 5d % ≤ -1.5 and rsi < 35 | 224 | +3.3% (+0.4% to +6.0%) | **+1.6%** | 5 of 6 | **+4.2% / +2.7%** | 73 trades, +1.5% avg, +1.5% median |
| **G2. Two to three 5d call days, calm RSI:** call days 2x+ 2 to 3 and rsi < 68 and call days 2x+ 20d ≥ 8 | 196 | +3.2% (+0.6% to +6.4%) | **+1.4%** | 5 of 6 | +4.4% / +2.1% | 76 trades, +0.9% avg, +1.4% median |
| **G1. Gate A widened:** call days 2x+ 1 to 5 and call days 2x+ 20d ≥ 8 and shares ≥ 1 | 391 | +1.9% (-0.1% to +4.0%) | +0.8% | **6 of 6** | +1.7% / +2.2% | 136 trades, +1.0% avg, +1.4% median |
| Gate A narrow (5d call days 1 to 3) | 243 | +2.2% (-0.4% to +5.2%) | +0.4% | 4 of 6 | +2.3% / +2.2% | 81 trades, +1.3% avg, +0.4% median |
| Gate A with rsi < 68 (instead of shares) | 392 | +2.1% (+0.1% to +4.2%) | +0.4% | 6 of 6 | +2.6% / +1.6% | 157 trades, +0.8% avg, +0.7% median |
| **D2. Bounce:** market 5d % ≤ -1.5 and off high % ≤ -15 | 376 | +3.5% (+0.2% to +6.6%) | +1.5% | 6 of 6 | +6.7% / +1.4% | 82 trades, +1.2% avg, +1.7% median |
| D2 at off high ≤ -20 | 310 | +3.2% (0.0% to +5.9%) | +1.5% | 5 of 6 | +6.0% / +1.6% | 57 trades, +1.5% avg, +2.3% median |
| D2 with price over $50 | 72 | +2.9% | +3.4% | 4 of 6 | +8.3% / +0.3% | 37 trades, +0.6% avg, +1.9% median |
| **B1. High breadth:** breadth % ≥ 67.8 | 387 | +1.7% (-0.2% to +3.6%) | +1.0% | 5 of 6 | +0.7% / +1.9% | 158 trades, +1.2% avg, +1.4% median |
| **D3. Market dip:** market 20d % between -12 and -4 | 401 | +1.7% (-4.0% to +6.1%) | +1.3% | 4 of 6 | **+6.7% / +0.1%** | 164 trades, +0.6% avg, +1.3% median |
| Market dip with stock not off its high (the D2 control) | 307 | +0.9% (-1.4% to +3.2%) | +1.0% | 2 of 6 | +1.9% / -0.8% | 182 trades, +1.1% avg, +1.1% median |
| P-E: 20d % ≥ 20 and iv/realized ≤ 0.8 | 136 | +6.1% (+1.6% to +11.1%) | +0.7% | 5 of 6 | +4.3% / +8.6% | 21 trades, +1.7% avg, **-1.8% median** |
| Puts 5d avg between 1.4 and 2.5 | 662 | +1.8% (+0.1% to +3.9%) | -0.2% | 4 of 6 | +1.3% / +2.3% | 275 trades, +0.8% avg, +0.5% median |

How to read this table:
- **The best stock rules by consistency** are D1, G2 and B1. All have positive halves and positive wide-list medians, with medians of +1.0% to +1.6%.
- **G1 and G2 point to a call-flow structure.**
  - Two to three call days in the last 5 sessions, on top of sustained 20-day flow, is the sweet spot.
  - Pooled thin flow (0 to 1 days) is bad.
  - The 3-to-5 band alone showed a pooled median of -0.6% in Agent 4's own tally (737 trades, not code-scored here).
  - Agent 1's bundle-6 bins agreed: 2 to 3 days +2.7% median, 0 to 1 days -3.6%.
- **Market-dip rules work mainly in earlier months.**
  - D3's +6.7% / +0.1% and D2's +6.7% / +1.4% are the same fading effect, probably sharing the same few dip episodes. Their independent event count is small.
  - The market-dip control with the stock not off its high is positive on the wide list (+1.1%) but 2 of 6 and negative in the second half.
  - So the stock-off-high leg adds to the dip. The off-high leg alone does nothing: 765 trades, +0.3%, median -1.1%, 1 of 6.
- **D1 is the cleanest dip rule** (positive in both halves, ranges above zero, wide list +1.5%). Most of its edge is probably the same dip effect, so it overlaps with D2.
- **Dip and breadth rules are mutually exclusive in time.** The joint P-C × P-F rule matched no trades. Both are positive and the middle zone is negative (section 2), so this is not a single-regime story.
- **Stock edges are tiny next to option costs.** None of these is a call-buying rule by itself. Their use is as a stock-level test of whether a signal has information, and as a base for the 5-, 10- and 20-session stock-horizon tests (section 4).

### 1C. 90-day baskets with a positive median (best medians, unstable)

The "screen" means: news 7d ≥ 1 and call days 2x+ ≥ 2 and call days 2x+ ≤ 5 and days since spike ≥ 1. These were scored in the previous generation and are not re-scored this round.

| Rule | Trades | Average | Median | Winners | Beat | Halves |
|---|---|---|---|---|---|---|
| **Screen, 90-day ATM** (benchmark -8.4%) | 58 | +0.4% (range -11.6% to +12.1%) | **+3.1%** | 53% | 4 of 6 | +7.0% / -6.6% |
| **Screen, 90-day 5% above** (benchmark -7.4%) | 55 | +1.9% (range -16.8% to +19.8%) | **+1.8%** | 51% | 4 of 6 | +15.5% / -17.0% |
| **Slow buying with news, 90-day ATM** (call days 2x+ 20d ≥ 8 and news 7d ≥ 1) | 81 | -1.0% | +1.7% | 51% | 3 of 6 | +4.1% / -5.1% |

- These are the only option baskets with a positive median (costs included), apart from S5. All three have a second-half collapse and heavy overlap.
- Controls:
  - Call days ≤ 1 with news: 127 trades, -8.7%, median -15.9%.
  - News < 1 with call days ≥ 2: 125 trades, **-14.1%**, 1 of 6.
- Failed variants:
  - Screen plus iv < 60: -2.4%, median -6.0%.
  - Screen plus shares 5d avg 1.3 to 1.7: -5.5%.
  - Screen plus vs ma50 between -13.5 and -2.7: -12.2%.
- Treat these as a research lead for a positive median, not a trade rule.

### 1D. Rules from the previous generation, not yet re-scored

These figures came from the old scorebook, which included expiring contracts and may differ. Restate them for clean numbers.

- **R1: overbought with sustained call buying, 30-day 5% above.**
  - Rule: rsi > 70 and calls 20d > 2.
  - Old result: 175 trades, +34.0%, median -53.4%, 5 of 6, halves +62.5% and +15.0%. With calls 20d ≤ 2 it was +1.0%.
  - **R1-$50** (add price over $50 and market 20d % > 0): 44 trades, +52.4%, median -21.5%, 5 of 6, halves +40.9% and +60.4%.
  - **R1b** (same entries at 30-day ATM, market > 0): 153 trades, +7.8%, halves +27.6% and -2.2%.
  - **R1c** (R1 at 10% above, exit when the option doubles, else after 10 sessions): 147 trades, +6.9%, 6 of 6.
- **R2-OTM:** 20d % > 20 and vs ma50 % > 15, 30-day 10% above: 211 trades, +26.2%, median -57.4%, 6 of 6. S1 is its better-median relative.
- **R3:** vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price over $50, at 5% above: 143 trades, +23.4%, 4 of 6.
- **R4:** calls 20d ≥ 1.5 and 20d % ≥ 10 and vs ma20 % ≥ 5, at 5% above: 297 trades, +17.8%, 6 of 6.
- **R5:** 5d % > 5 and vs ma20 % > 5 and news 3d ≥ 1, at 5% above: 186 trades, +16.4%, 4 of 6.
- **R6:** vs ma50 % > 0 and 20d % > 0 and market 20d % > 0, at 5% above: 666 trades, +9.1%, 6 of 6.
- **R7:** market 20d % > 0 and vs ma50 % > 0 and rsi > 60, at 5% above: 430 trades, +9.4%, 6 of 6.
- **R8:** price over $50 and vs ma50 % > 0 and market 20d % > 0, 30-day ATM: 259 trades, +5.0%, median -25.1%, 6 of 6.
- **R9/R10:** weaker (+5.2% and +9.1%).
- **R11/R12:** 90-day 10% above, steadier. +3.3% (median -16.1%) and +7.0% (median -8.0%).

### 1E. Weak add-ons and leads

- **News 7d ≥ 1, 30-day 5% above (old):** 1,125 trades, -6.4% against -12.2%, 5 of 6. Steady, still negative.
- **Call persistence 3+ with market > 0, 30-day ATM:** 394 trades, -8.9%, 3 of 6.
- **Sub-$10 with calls 20d > 10, 30-day 10% above (old):** 47 trades, +39.9%, 3 of 6. A lottery, and suspect given the cost floor.
- **Oversold with quiet calls, 90-day 5% above (old):** 8 trades. Too small.

### 1F. Sizing and structure guidance

- **Use 30-day ATM** (or 5% above) for trend rules. ATM has much better medians than 10% above (-21.5% against -57.4% for the same idea).
- **Median ranking of structures:**
  - S5 at 30-day ATM: +5.8%.
  - 90-day screens: about 0% to +3%, unstable.
  - 30-day ATM with strong gates (S1, S1-tail): -16% to -22%.
  - 30-day 5% above tail-seekers: -38% to -56%.
- **Never use 14-day expiries.** Three live 14-day trades lost -100%, -100% and -1.2%, and short expiries risk expiring inside the hold.
- **Hold 10 sessions.** There is no evidence that any exit rescues a bad entry. Double-or-10 is validated only as R1c (old), and a live test was negative (-72% median).
- **Market gate:**
  - S1, S2, S3 and the old rules use a rising-market gate (20d > 0). S5 uses a falling 5-day market.
  - Do not drop either until the head-to-head test is done.
  - Avoid the mild-dip zone at the stock level (section 2).
- **Costs are already inside these numbers.** Real fills may be somewhat worse.
- **Call spreads:** the one scored spread rule had a -45% benchmark and -48.8% average. Do not use spreads without a specific reason.

---

## 2. AVOID

### Confirmed by the current scorebook

- **Thin 5-day call flow** (call days 2x+ ≤ 1, dollar volume ≥ $14M): 1,256 stock trades, -0.1%, median -0.4%, 1 of 6.
  - Quiet 5d flow with active 20d flow: 158 trades, median -0.2%, 2 of 6.
  - Bundle 6 bins agreed (-3.6% median, 26% up). Traders 1, 3 and 4 and the scorebook agree.
- **No short-dated call activity** (short ≤ 0, dollar volume ≥ $14M):
  - Stock: 471 trades, -0.7%, median -1.2%, 1 of 6, second half -2.3%, wide list -1.0%.
  - Option: short ≤ 0 and news ≥ 1 at 30-day 5% above: -23.2% (195 trades, 1 of 6).
- **The mild market zone:**
  - Market 20d % between -4 and 0: 623 stock trades, -0.0%, median -0.1%, 1 of 6, halves +2.1% / -3.5%.
  - Market 5d % between -2 and 0: 769 trades, -0.1%, median -0.9%, 2 of 6.
  - Both dips and strong breadth do better than the middle.
  - Note the tension with S5, whose 5d < 0 includes deeper dips.
- **The stock leg alone** (off high ≤ -15 with no market dip): 765 trades, median -1.1%, 1 of 6.
- **Extreme beta** (beta > 1.9): 633 stock trades, average +1.4% but median -1.6%, wide list -0.8%. Not a good filter either way.
- **Stock edge wrapped in an option, lost four times:**
  - The Gate A call.
  - The bounce at 90-day ATM.
  - The oversold stock rule at 5% above with a market gate (-31.7%, 65 trades, 1 of 6).
  - The high-breadth call (median -30%).
- **Very low IV:** market 20d > 0, vs ma50 > 0, news ≥ 1, iv % < 30 at 5% above: **-35.6%** (83 trades, 1 of 6).
  - Likely cause: the cost floor on cheap options.
  - Live trades showed negative medians in every IV band (-20% to -46% at 30-day ATM).
- **Mild strength:** calls 20d ≥ 1.5, 20d % between 10 and 25, market > 0, 30-day ATM: -7.6%.
- **Pullback inside strong call flow:** off high between -16 and -8, calls 20d ≥ 1.5, 30-day ATM: -10.4%.
- **Shares 5d avg band 1.25 to 1.7 as an option rule:** -8% to -11%.
- **Momentum without volume:** shares < 1 version of S1, median -41.0%, 3 of 6.
- **Flow without news at 90-day:** -14.1%.
- **Low call flow with news at 90-day:** -8.7%.
- **The stock rule "momentum plus price over $50, no market gate":** 42 trades, median -0.5%, 1 of 5 beating the benchmark.

### Avoid from the previous generation (old scorebook, not re-scored)

- Surge follow-through, overextended fall, oversold with heavy calls (-27% to -30%).
- Momentum or any call rule when market 20d % < 0 (-11% to -48%), except possibly S5's 5-day version.
- Non-extended stocks in an up market (-17.7%).
- The $10 to $50 price band.
- Heavy 20-day calls with no news (-14.6%).
- Stacks of weak filters.
- Ratings of any kind.
- 14-day expiries and 10%-plus out-of-the-money strikes.
- Judging a rule by total dollars, one trade, or a median over fewer than 20 trades.
- Real money in sub-$10 names.

### Dropped or demoted

- **"Top bin of vs ma50 or 20d % is bad"** was a one-bundle quantile read. Rule-level scores show strong trend winning in options.
- **Close vs vwap thresholds.** Neither a filter nor an exclusion (neutral).
- **RSI ≥ 68 exclusion.** It does not lift the Gate A median, but the "2 to 3 days plus rsi < 68" version is the top stock rule, so treat RSI < 68 as an optional overlay.
- **Spike yesterday, 1-day move band, IV > 85 exclusion, IV < 40 filter, dollar-volume cutoffs, iv/realized ≥ 1.5 exclusion.** All unsupported or reversed.
- **Market 5d and 20d gates for stock** are noisy across bundles in single-bin reads. Use rule-level scores only.
- **Rule C** (20d % ≥ 20 and market 5d < 0 and caps, as stock): scored 23 trades, median -2.7%. Dropped.

---

## 3. WHERE THE TRADERS AGREED AND DISAGREED

**Agreed**
- The median option trade loses. Averages come from a few large winners.
- Ratings are noise. The sign flipped across bundles for all four.
- No real-money options without a positive median.
- 14-day, out-of-the-money and sub-$10 structures are bad or untrustworthy.
- Thin call flow (0 to 1 days in the last 5) is an avoid.
- Zero short-dated call activity is an avoid.
- Stock-level edges are small.

**Disagreed**
- **Stock or option.**
  - Agents 1, 2 and 3 trade stock. Agent 4 stays on paper. All four lost on live option books (about -$4,000 to -$15,600 per bundle for three; Agent 3 gained +$4,258 on five lottery winners).
  - The scorebook shows S1 and S5 positive on average at option level, with S5 the first positive median. Option form multiplies the average and leaves a negative median for S1.
- **Strong trend.** Agents 1, 3 and 4 found momentum stock rules thin (medians near zero, negative on the wide list). The scorebook shows the same momentum selection producing option averages of +13% to +48%. These are different risk profiles. Whether the option edge survives the no-hindsight test is open.
- **Call-flow bands.**
  - Agent 1 found 1 to 5 days with 20-day flow ≥ 8 positive on 391 stock trades.
  - Agent 4 dropped bands 1 to 2 and 3 to 5.
  - The scorebook confirms G1 (6 of 6) and shows 2 to 3 days is better (G2). Agent 4's pooled-band numbers are consistent with the 2 to 3 band carrying the edge.
- **Market gate.**
  - Agents 1 and 3 found market bins noisy.
  - Agent 2's rule is a market-dip rule. Agent 4 backed both dip (P-C) and high breadth (P-F).
  - The scorebook shows that dips and high breadth beat the middle, and that S1 (market up) and S5 (market 5d down) both work as options. The gate is regime-dependent and untested head to head.
- **The dip effect.** Agent 2 and Agent 4's dip rules are the same fading effect. Agent 4 read the +6.7% / +0.1% split as a first-half-of-month artifact, but "halves" here means first and second half of the sample, so it is a fade over time.
- **IV.** Agent 4 liked low IV/realized (P-E +6.1% average, wide-list median -1.8%). Agent 3 gated iv < 60. The scorebook penalises iv < 30 heavily. Only the loose iv < 60 gate (S3) has option-level support.
- **Option audit.** Agent 4's "model risk" claim is resolved by the expiry fact.

---

## 4. NEW IDEAS TO TEST

State each as an explicit rule. Require n ≥ 60, report both halves **and the wide list**, and compare to the benchmark.

1. **Dissect S5 (credit Agent 3; top priority).**
   - Restate the exact rule: 20d % ≥ 20 and call days 2x+ ≥ 2 and market 5d % < 0, 30-day ATM.
   - Test, one change at a time:
     - market 5d % < -1 and < -2;
     - market 5d % ≥ 0 (the control);
     - call days 2x+ ≥ 3;
     - 20d % ≥ 30;
     - add market 20d % > 0;
     - 5% above;
     - 90-day ATM;
     - add vs ma50 % ≥ 15 or shares ≥ 1.
   - Also score S5's entries as a stock, over 5, 10 and 20 sessions.
   - Success is a positive median in both halves with a wide-list result near zero or better.
2. **S1 at longer expiry.** Test S1 at 90-day ATM and 90-day 5% above. S1 at 30-day has a -21.5% median, and the only other positive medians are 90-day baskets. Success is a positive median with both halves positive.
3. **Wide-list audit of the best option rules.** Report S1, S5, S2 and S3 on the wide list only. If the wide-list result is poor, treat the option edge as hindsight-selection.
4. **Market regime map.** Bucket market 5d % × market 20d % (for example: 5d < -1.5 with 20d > 0; both < 0; 5d ≥ 0 with 20d > 0) and score S1, S2, S5 and G1 in each cell. This reconciles S1's up-market gate with S5's down-5-day gate and the dip-versus-middle finding.
5. **Stock horizons.** Re-score D1, D2, G1, G2 and B1 at hold 5, 10 and 20. The 10-session choice has no evidence behind it. A slower stock edge may justify a longer horizon, and a stock holding gives a no-expiry-risk way to harvest small edges.
6. **Stack flow and market.** Test G2 plus D1 (2 to 3 call days, rsi < 68, and oversold in a market dip), and G2 plus B1 (the same with breadth ≥ 67.8). Dips and breadth are mutually exclusive in time, so each can only be tested against the benchmark, not combined.
7. **S1 add-ons**, one per rule at 30-day ATM: price over $50, iv % < 60, news 7d ≥ 1, call days 2x+ ≥ 2 (the S5 flow idea), rsi > 60, short ≥ 1. Note the stock version of S1 with price over $50 and no market gate was weak.
8. **Cost-aware selection.** The new "option cost %" column gives the round-trip cost of the ATM call. Test S1, S5 and S2 split by option cost % (for example under 12%, 12% to 20%, over 20%) and by price over $50. Success is a median that improves without the average collapsing.
9. **Event-priced options.** Test iv 90d/30d < 1 (near-term options priced for a move) and iv/1y realized inside S1 and S5. Untested; credit the new columns.
10. **Re-score the previous generation's top rules cleanly:** R1, R1-$50 (widen it: rsi > 60 or 65, calls 20d > 1.5, or price over $30, to reach n ≥ 60), R3, R4, R6, R7, R8 and R11/R12.
11. **Strength ladder.** Under a market-up gate, bucket 20d % (0 to 10, 10 to 20, 20 to 40, 40+) at 30-day ATM. Current evidence is S1-cap (15 to 40) +13.5% against S1-tail (40+) +35.5%.
12. **Cheap iv/realized inside strength baskets.** Test iv/realized < 0.75 inside S1, S2 and R4. The standalone S4 was +12.8%. Note P-E (stock) had a negative wide-list median.
13. **Exit variants.** Test double-or-10 on S1, S1-tail and S5 at ATM and 5% above.
14. **Break-even-aware selection (Agent 4's idea).** Estimate each candidate's break-even stock move from its premium and IV. Test candidates whose recent 20d % and vol20 exceed it.
15. **Basket simulation.** Equal-premium weekly baskets of S1, S5, S2 and S3: worst week, overlap, and whether the 6-of-6 record survives deduplication.
16. **Sub-$10 lottery with costs known.** Test calls 20d > 5, > 10 and > 20 with trend and market gates. The floor means entries start about 14% or more in the hole.
17. **Puts 5d avg 1.4 to 2.5** (credit Agent 3): +1.8% over 662 stock trades, 4 of 6, median -0.2%. Test it inside strength baskets as a sustained-hedging or contrarian marker.
18. **Medium-dated call ratio 0.26 to 0.69** (one bundle bin, +2.7% median). Test as an add-on.

**Removed or no longer needed:** put spreads, bear call spreads, deep ITM calls, and short selling cannot be implemented. Call spreads can be tested, but the one scored version had a -45% benchmark, so they are low priority.

---

## 5. OPEN QUESTIONS

- **Positive median.** S5 shows +5.8%, with 53% winners and stable halves, but only 57 trades and a bad wide-list median on 9 trades. Is it real, or a hindsight-list effect? The 90-day screens (+3.1% and +1.8%) fade in the second half.
- **What does the market 5d × 20d regime look like?** S1 wants a rising market, S5 a falling 5-day market, and dips and high breadth both help stock rules while the middle zone is negative.
- **Does the hindsight list drive the momentum option edge?** Momentum stock rules were negative on the wide list. S1's wide-list option result has not been seen.
- **Does S1 persist?** The latest bundle's S1 stock trades averaged only about +2.7%. S1's option range barely clears zero, and tail trades carry the average.
- **Why does mild strength lose while strong strength wins?** Is it premium relative to the move, convexity capture, or the cost floor?
- **Is the cost floor the main reason cheap options lose?** Very low IV, sub-$10 and far out-of-the-money all lose. This has not been isolated, and the new "option cost %" column may settle it.
- **Why do stock edges disappear in the option wrapper?** The oversold, Gate A, bounce and breadth stock rules all lose as calls. Small stock edges seem to need a big move to survive the 10% round trip.
- **Will the dip effect return?** D2 and D3 faded over time (+6.7% first half to +0.1% to +1.4% second half). If the next sample's second half is flat or negative, treat the dip as a regime that has ended.
- **What are the residual -50% to -70% losses on flat stocks?** They are probably real decay plus costs and IV drops. Premium and expiry data in trade lists could confirm.
- **Does over $50 act as a liquidity, low-IV or cost-floor proxy?** It helped the old R1, R3 and R8 results, and it helped D2 on median (+3.4% on 72 trades). It hurt S1 as a stock rule without a market gate.

### How the committee would remake the test (not passed on)

# REDESIGN PROPOSAL

## 1. WHAT BLOCKED US (ranked by damage)

1. **Too little independent data, too many looks at it.**
   - Six bundles of about 250 candidates gave roughly 3,000 trades. Most rules had 20 to 400 trades, and the dip rules rest on a handful of market episodes.
   - The traders ran 96 rule checks in total, and results still bounce around. Agent 4: "Most option subsets have fewer than 15 trades, and single-bundle differences are not reliable." Agent 1: "The lower bound touches zero, so this is not a strong result."
   - Nobody could say how many lucky rules to expect, because no null distribution was shown. S5 (+48%, median +5.8%) can't be told apart from a lucky pick.
2. **The hindsight list contaminates the sample.**
   - About 60% of candidates were chosen because they later rose 15% or more. Every momentum rule is biased on that part.
   - The honest wide list is small, so it gives a verdict on only 9 to 80 trades. S5's wide-list median was -68% on 9 trades, which is neither confirmation nor refutation.
3. **We only see the candidates, not the universe.**
   - A "signal" can't be compared with the same week's non-signal stocks. Market and regime effects are mixed up with stock effects.
   - Examples: the dip rule versus the "stock off its high" control, and S1's rising-market gate versus S5's falling-market gate.
4. **Instruments don't match the edges.**
   - The stock edges are about +1% per 10 sessions. A call costs at least 10% round trip, and the fixed 10-session hold, calls only, with no puts, straddles or exits, leaves nothing to harvest them with.
   - Four tests of "stock edge as a call" lost. Agent 2's stop-loss sub-test never got a score.
   - Option winners were lottery tickets, with medians of -20% to -70%.
5. **Feedback was coarse and noisy.**
   - Fifth-bins, ties and 5 checks per bundle pushed traders to chase single bins that flipped sign. Agent 1: "Tie-based binning makes this unreliable."
   - Agent 3: "The bundle 6 bins are not enough to rebuild the intersection." Agent 3 also couldn't test its own rule because it hadn't logged it.
   - The scorebook and the traders' tallies disagreed, and the earlier scorebook included expired contracts.
6. **Anonymous stocks and hidden dates.**
   - We can't dedupe repeat signals on the same name, see calendar events (expiry week, FOMC, earnings), or separate regime from luck.
   - One trader misread "halves", and none could explain why a rule works (Agent 2: "I still cannot say why it works").
7. **Discretionary live trading was uninformative and costly.** It gave 26 to 36 option trades per bundle with large sign swings, and Agent 4 concluded "discretionary selection did not add value." Ratings flipped sign for all four traders.
8. **Same-close entry is optimistic.** The signal uses the close, and the trade fills at that same close.

## 2. DATA TO ADD (most useful first)

1. **The full universe for every week**, such as all liquid optionable US stocks, with a flag for whether each was a candidate. Daily data is enough. It enables matched, same-week, beta-adjusted benchmarks and lets us test whether a signal adds anything beyond the market.
2. **Candidates chosen without hindsight.** Use a rule-based or random pick made from data available at the time. If the hindsight list stays, label it and score it separately by default. This directly fixes the momentum bias.
3. **Persistent anonymous stock IDs and a day index.** Add a coarse calendar label (month, expiry week, FOMC week) and keep exact dates hidden if you must. This allows deduping, clustered-by-stock-and-week statistics, and calendar tests. Earnings dates (public, cheap) would also let us test event-priced options, because IV rises into earnings and crushes after.
4. **Index and volatility history.** Give SPY and VIX (and the VIX term structure) with 20 or more years of daily data, not just per-candidate market columns. The dip effect can then be tested on thousands of days rather than a few episodes.
5. **Historical option chain snapshots.** These come from vendors such as ORATS or CBOE DataShop. Give bid, ask

### Agent 1's final notes (not passed on)

# Trading Notes: Generation 2, Final Version (after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

### Core stance

- **I trade the stock, not the option.** Stock trades have the most consistent evidence. Option results swing sign from bundle to bundle and are dominated by a few large moves. Bundle 6 confirmed this: 26 option trades lost $4,026, with a -29.5% median, even though the all-candidates stock control median was positive (+0.5%).
- **Ratings are ignored.** They have had no reliable sorting power across the generation. The one exception is noted in section 2, and it is not a rule.
- **Position size stays small and flat.** One position per stock per signal. No adding to winners or losers.

### Primary rule: Gate A, call-flow (stock)

Buy the stock at the signal-day close. Hold 10 sessions. Enter only if all three hold:

1. **Call days 2x+ over the last 5 sessions: 1 to 5.** (Start with 1 to 5 as the primary version. The narrower 1 to 3 band is a subset that I will keep reporting.)
2. **Call days 2x+ over the last 20 sessions: 8 or more.**
3. **Shares ratio today: 1.0 or more.**

Evidence, pooled across the six bundles:

| Version | Trades | Average | Median | Win % | Bundles beating control |
|---|---|---|---|---|---|
| Gate A, 5-day call days 1 to 3 | 243 | +2.2% | +0.4% | 53% | 4 of 6 |
| Gate A widened, 5-day call days 1 to 5 | 391 | +1.9% | +0.8% | 54% | 6 of 6 |
| Control (all candidates) | ~3,000 | +0.6% | ~0% | ~48% | n/a |

- Both halves of the months were positive for both versions (narrow: +2.3% and +2.2%; widened: +1.7% and +2.2%).
- Wide-list subset (no hindsight, the names I would have seen without the full-list view): narrow 81 trades, +1.3% average, +0.4% median. Widened 136 trades, +1.0% average, +1.4% median. Wide-list control: +0.1%.
- The 95% resampling range for the average is roughly -0.2% to +4.1% (widened). The lower bound touches zero, so this is not a strong result.

**Confidence:** moderate on direction (the widened version beat control in every bundle and has a positive median). Low-moderate on size. The median edge is small, a few tenths of a percent to under 1%, so transaction costs and slippage matter.

**Evidence on the 8+ leg (20-session call days):** It is weak. Bundle 5 showed a negative median for 7 to 15 call days. Bundle 6 showed +1.7% for 7 to 12 (62% up), and 5 to 7 showed -0.1%. I keep the leg because it is part of the tested rule, but I do not treat it as independently proven.

**Evidence on the 5-day leg:** Bundle 6 supports it. Stocks with 2 to 3 call days at 2x+ in the last 5 sessions had a +2.7% median (74% up). Stocks with 0 to 1 days had -3.6% (26% up). This is the strongest single bin I have seen in the 5-day column.

### Secondary comparator: S1 momentum (as written)

Buy at the close, hold 10 sessions, if: 20-session change ≥ 20%, vs ma50 ≥ 15%, market 20d > 0, shares ≥ 1, price over $50.

- Evidence: 38 trades before bundle 6, +5.2% average, +0.6% median, 55% winners, beat control in 4 of 5 bundles.
- Generation 1 had 168 trades, +6.0% average, +1.4% median, and beat control in 6 of 6 bundles.
- **Role:** comparator only. Its average depends on a right tail. Its median is close to zero. It mostly selects extended names, and bundles 4 and 5 showed those names underperform.
- Wide-list subset is thin (2 trades, -0.9%).

### S1 cap: dropped

The cap (20-session change 20 to 40, vs ma20 ≤ 7, close vs vwap ≤ 0.8) was meant to remove S1's worst tail. It did not. With bundle 6 included, the cap has 41 trades, +3.9% average, but a **-2.2% median**. It beat control in 5 of 6 bundles, but its median is worse than S1 as written (+0.6%). My pre-set rule was to adopt the cap only if it beat S1 on median in bundle 6. It did not. I drop the cap.

### Exclusions (softened)

I am downgrading most of the hard exclusions I used in earlier notes, because bundle 6 contradicted several of them.

- **Close vs vwap above 0.8%:** Bundle 6 showed +1.2% median (56% up) in the 0.63 to 8.13 bin. Earlier bundles were negative. Treat as a soft warning, not a hard exclusion.
- **1-day move between +1.4% and +3.9%:** Bundle 6 showed +1.5% in the 0.6 to 2.5 range. Not confirmed. Drop as a hard rule.
- **RSI at or above 68:** Bundle 6 showed -0.2% median (50% up) for 66 to 95. Weak. Gate A with RSI below 68 and vwap ≤ 0.8 (no 20-session or shares conditions) has a pooled median of about 0%, versus +0.4% for gate A. The filter lowers the average and does not raise the median. Do not add it to gate A.
- **Keep:** no sub-$10 names for options; no IV above 90 for options; no expiry under 30 days; no call spreads.

### Options: suspended for sizing

- **30-day ATM call, 0% strike, hold 10 sessions:** Pooled median is clearly negative. Generation 1: -21.5% median over 138 trades. Bundle 4: -26%. Bundle 5: +88% on only 6 trades. Bundle 6: -18.2% median over 20 trades, with 27% of all option trades as winners. The bundle 6 breakdown by implied volatility was negative in every IV band (median -40% below IV 30, -34% at 30 to 42, -46% at 44 to 60, -20% at 61 to 90, -24% above 90).
- **Bundle 6 option pattern:** Stocks that rose 2% to 4% in 10 sessions often produced option losses of 2% to 10%. Option winners needed large stock moves (+10% to +24%). Option returns amplified the stock move but did not add an edge.
- **90-day ATM call:** Suspended. Median by bundle was +33%, -1%, +35%, -49%, -33%. Bundle 6 added no 90-day data.
- **Calls at +5%, +10%, +20% strikes:** Bundle 6 had 6 trades total, averaging -65% excluding the single +63% winner. Not viable at this sample.
- **Rule for options:** log only. Do not size. Revisit only if a narrow test (below) shows a positive median over at least two bundles.

### Sizing and risk

- Flat, small stock positions. Confidence on size is low.
- One position per stock per signal. No pyramiding.
- Options: zero position size for now. If an option test is run, assume -100% on any position.

---

## 2. WHAT I TESTED IN THIS BUNDLE (bundle 6)

### My own trades

- 26 option trades. Profit -$4,026. Average -15.5%, median -29.5%, 27% winners.
- By form:
  - 30-day 0% call, hold 10: 20 trades, average -5.0%, median -18.2%.
  - 30-day +5% call, hold 10: 4 trades, average -66%, median -78%.
  - 30-day +10% call: 1 trade, +63%.
  - 30-day +20% call: 1 trade, -100%.
- Ratings: +1 (35 stocks) averaged +4.8% over 10 sessions, median +2.0%. Rated 0 averaged +0.3%. Rated -1 averaged -0.1%. Rated -2 (3 stocks) averaged -6.4%.
  - I note the +1 group as a one-bundle observation. Ratings have shown no reliable sorting power in earlier bundles, so I do not act on this.

### Bundle-wide stock results

- All 250 candidates: average +0.7%, median +0.5%. The market was supportive for the typical name.
- Gate A widened beat the control again in this bundle (the 6 of 6 record).
- S1 cap failed its pre-set test (see section 1).

### Bins that held in bundle 6

- **5-day call days 2x+:** 2 to 3 days +2.7% median (74% up). 0 to 1 days -3.6% (26% up). Strongest support for the call-flow gate.
- **Days since last spike:** The bins were inconsistent (a 0 bin at -6.2%, a 0-to-1 bin at +5.6%). Tie-based binning makes this unreliable. Keep dropped.
- **News in the 7 days before the close:** 1 to 2 articles +1.6% (68% up); 2 to 28 articles +3.0% (64% up); zero articles about 0%. Consistent with bundle 5. The news add-on is still a candidate, not a rule.
- **News tone 7d, 0.1 to 0.24:** +4.1% (73% up). One bundle; log only.
- **Beta 1.42 to 1.92:** +3.3% (72% up). Beta above 1.96: -3.4% (30% up). Noisy; log only.
- **Market 5d between -2.1 and -0.2:** -3.4% (36% up). Market 20d between -12 and -4: +2.8% (66% up). Market bins remain noisy; no market gate.
- **Off the 60-day high 17% to 30% below:** +1.9% (54% up). Opposite of bundle 5. Not a usable rule.
- **20-session change 3% to 13%:** +1.0%. Not an edge.

### Bins that failed or contradicted earlier notes

- Close vs vwap above 0.63: +1.2% (contradicts earlier exclusion).
- RSI 66 to 95: -0.2% (weak; not a strong overbought effect this bundle).
- 1-day moves 0.6% to 2.5%: +1.5% (contradicts the 1-day exclusion).
- IV above 90 for options: option results were negative across the board. Stock median in the top IV band was +0.8%, so the exclusion is not about the stock, only the option.

### Options by implied/realized ratio (bundle 6)

- 0.73 to 0.96: median -19%.
- 1.52 to 2.96: median -24%.
- Ratio does not separate winners from losers in this bundle. Dropped as an entry filter (it was already dropped).

---

## 3. WHAT I WILL TRY NEXT (next generation)

Pre-registered. I will report average, median, win %, trade count, and bundle-wide control median for each.

**Stock tests (run all):**
1. **Control:** buy every candidate, hold 10 sessions.
2. **Gate A widened (primary):** 5-day call days 2x+ between 1 and 5; 20-day call days 2x+ ≥ 8; shares ≥ 1.0.
3. **Gate A narrow (subset check):** same, but 5-day call days 1 to 3.
4. **S1 as written (comparator only).**
5. **News add-on:** gate A widened plus news 7d between 1 and 3 articles. I will not read the median until there are at least 100 trades pooled. Until then, this is a flag, not a rule.
6. **Overlay test:** gate A widened plus RSI below 68. Test only as an overlay on median. Drop it if the median does not improve over gate A.

**Options (logging only):**
- 30-day ATM call, 0% strike, hold 10 sessions, on gate A widened names with IV at or below 45, no underlying under $10. Log only. I will not size it unless the median is positive in two consecutive bundles.
- 90-day tests: parked.

**Decision rules:**
- Gate A widened stays the primary stock rule if its pooled median stays positive and it beats control in most bundles. Size modestly (still small) only after the next bundle confirms it in both halves.
- If gate A's median turns negative in the next bundle, reduce to a token size and report the failure.
- If the news add-on's median is above gate A's, with at least 100 trades, consider adding it as a second-tier rule.
- S1 stays as comparator. Do not adopt the cap.
- Options stay at zero size.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Stock evidence summary (cumulative)

| Rule | Trades | Average | Median | Win % | Bundles beating control |
|---|---|---|---|---|---|
| Control (all candidates) | ~3,000 | +0.6% | ~0% | ~48% | n/a |
| Gate A narrow (5-day 1 to 3, 20-day ≥ 8, shares ≥ 1) | 243 | +2.2% | +0.4% | 53% | 4 of 6 |
| Gate A widened (5-day 1 to 5) | 391 | +1.9% | +0.8% | 54% | 6 of 6 |
| Call days 1 to 3 plus news 1 to 3 (7d) | 710 | +0.6% | +0.4% | 52% | 3 of 6 |
| Gate A with RSI below 68 and vwap ≤ 0.8 | 1,263 | +0.6% | ~0% | 50% | 3 of 6 |
| S1 as written | 38 (before bundle 6) | +5.2% | +0.6% | 55% | 4 of 5 |
| S1 cap | 41 | +3.9% | -2.2% | 44% | 5 of 6 |

Interpretation:
- Gate A has the most reliable record: a small positive median, beat control more often than not, and both halves of the months were positive.
- The news add-on (710 trades across the call-days-plus-news rule) is positive but small. It is not clearly additive to gate A yet.
- S1's averages are real but depend on a right tail. Its median is near zero.
- The RSI and vwap overlay lowers the average without raising the median. Drop as a hard filter.

### Option evidence summary

| Form | Results | Read |
|---|---|---|
| 30-day ATM call, hold 10 | Gen 1 median -21.5% (138 trades); bundle 4 -26%; bundle 5 +88% (6 trades); bundle 6 -18.2% (20 trades) | Negative in most samples. Suspended. |
| 90-day ATM call, hold 10 | Medians +33%, -1%, +35%, -49%, -33% by bundle | Not validated. Suspended. |
| Out-of-the-money calls (+5% to +20%) | Bundle 6: 6 trades, mostly losses | Not viable at this sample. |
| Double-or-10 exits | Bundle 5 +28.5% on 6 trades; mixed elsewhere | Too few to judge. Dropped as headline rule. |

Pattern: option outcomes track the stock's 10-session move, amplified. Option medians do not add an independent edge at current sample sizes. Winners need stock moves of roughly +10% or more; the bundle 6 stock moves of +2% to +4% produced option losses.

### Dropped or demoted

- **Ratings:** no reliable sorting power over six bundles. The bundle 6 +1 group is noted but not acted on.
- **Days since spike:** bins were inconsistent. Dropped.
- **S1 cap:** failed its pre-set test in bundle 6. Dropped.
- **Close vs vwap above 0.8 exclusion:** contradicted in bundle 6. Soft warning only.
- **1-day move exclusion (1.4% to 3.9%):** not confirmed in bundle 6. Dropped as hard rule.
- **RSI 68+ exclusion:** weak in bundle 6 and does not improve the gate A median. Dropped as hard rule.
- **Call spreads:** dropped after bundle 3.
- **Option cost ≤ 10% filter:** dropped after bundle 3.
- **iv/realized ≥ 1.5 exclusion:** not supported; dropped as entry filter.
- **Dollar volume under 11M exclusion:** reversed across bundles. Dropped.
- **Market 20d and 5d gates:** noisy across bundles. Market gate kept only as a soft condition in S1.
- **Beta above ~2:** mixed. Dropped as a rule.
- **Short-dated calls (14 days or less):** one losing trade (-94%). Avoid until tested.
- **Oversold with news as a call (generation 1):** -31.7%. The stock edge did not survive the option wrapper.

### Open questions for the next generation

- Does gate A widened keep a positive median on new stocks? This is the main question. Six bundles say yes so far, but the median is only about 0.8%.
- Does the 8+ call-day leg over 20 sessions add anything, or is it noise? Evidence is mixed.
- Does the news add-on (1 to 3 articles in 7 days) add to gate A, or is it a proxy for the same names?
- Is there a stock-level option edge at a longer horizon, or is the option form a leveraged version of a weak stock signal? Still open. The 120-day test is parked.
- Why did the 2 to 3 call-day bin do so well in bundle 6 (+2.7% median) when the 0 to 1 bin was so negative? Is that a stable structure or a one-bundle pattern?

(Recorded by the system: this trader ran 24 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)

### Agent 2's final notes (not passed on)

# TRADING NOTES: FINAL (after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

### 1.1 Core stance

- **The only rule I trade is a stock position, not an option.** I buy the stock after a market-wide selloff when the stock has fallen well off its recent high. I hold it 10 sessions.
- **No options in the book.** Options have lost money in every bundle where I traded them. The bundle 4, 5 and 6 books total -$13,118 (-$4,120, -$3,312, -$5,686). Every option structure I traded had a negative median. The lottery-style winners do not make up for the losers, and I cannot yet tell them apart in advance.
- **Judge rules on median, on both halves of the sample, and on the wide list (no hindsight).** Averages are driven by a few large trades.
- **Paper size only** until a rule holds on fresh data for several more bundles.

### 1.2 PRIMARY: post-selloff stock bounce

**Entry (at the signal-day close):**
- `market 5d %` ≤ -1.5 (the S&P 500 fund fell at least 1.5% over the last 5 sessions), **and**
- `off high %` ≤ -15 (the stock closed at least 15% below its highest close of the last 60 sessions).
- Optional, same rule: `rsi` < 68 (in practice this removes almost nothing; see 1.2c).

**Instrument:** the stock, long, equal size on every signal.

**Exit:** sell at the close of session 10, regardless of P&L.

**Stop:** none in the rule as traded. A -15% stop (sub-test A) was pre-registered for bundle 6 but I have no reported result for it, so it is not adopted.

**Pooled evidence (6 bundles, 376 trades):**

| Measure | Result |
|---|---|
| Average 10-session return | +3.5% |
| Median | +1.5% |
| Win rate | 56% |
| 95% range of the average (whole-week resampling) | +0.2% to +6.7% |
| Buy-all benchmark, same candidates | +0.6% average |
| Bundles beaten (vs buy-all) | 6 of 6 |
| First half / second half of months | +6.7% / +1.4% |
| Wide list (no hindsight) | 82 trades, average +1.2%, median +1.7% (benchmark +0.1%) |

**Bundle 6 alone:** the bounce rule beat buy-all again, and the second half was positive (+1.4%). The second-half downgrade rule (two negative second halves in a row) has not triggered. The effect has shrunk from the first half, so I hold it at paper size.

**Confidence: medium.** Direction has held in six of six bundles and the lower bound of the range is just above zero. Against that: the effect is fading, the average depends on a set of large rebounds, and I still cannot say why it works.

### 1.2a What the controls showed

- **Off-high without a market dip is not a bounce.** Off-high ≤ -15 with market 5d % > -1.5: 765 trades, average +0.3%, median -1.1%, 46% winners. It beat buy-all in 1 of 6 bundles. Wide list average 0.0%, median +0.7%.
- **Conclusion:** the stock's own drop does not predict a rebound. The rule works only when the market has also fallen. The rule is therefore a market-dip rule conditioned on the stock being well off its high.
- **Still untested:** a market dip with the stock *not* off its high (market 5d ≤ -1.5, off high > -15). If that group also bounces, the stock leg is not needed at all. I have not run this, and it is the first thing to check on new data.

### 1.2b Depth

- **-15 is the rule.** -25 off high (with the market leg): 240 trades, average +2.3%, median +0.6%, 53% winners, beat buy-all in 5 of 6 bundles. Its median is well below the -15 rule's +1.5%. Deeper is not better. **Drop -25.**
- **-20 off high** was the co-equal arm in bundles 1 to 5 (pooled +4.0% average, +1.5% median, 256 trades). I have no separate bundle 6 result for it in this report, so I keep it as a tracked variant and do not promote it over -15.

### 1.2c Subsets on the primary

- **RSI ≥ 68 exclusion:** the rule with RSI < 68 gives 370 trades (average +3.5%, median +1.6%) against 376 without the filter. Only about 6 primary signals were overbought. The earlier "overbought lags" finding does not show up inside the bounce. **Not a filter; the question is moot at this sample size.**
- **Breadth above 50% (market breadth):** 16 trades, average +14.8%, median +7.8%, 81% winners, beat buy-all in 1 of 2 bundles where scored. The subset is very small, and two of its trades contribute a lot of the average. **Track only. Not a filter.** This is the one subset worth a clean test on new data (see section 3).
- **Price over $50:** 53 trades through bundle 5 (average +4.2%, median +4.4%). The pre-registered test was whether the over-$50 median stays above +3% and the second half stays positive. Bundle 6 does not give a clean over-$50 result in this report. **Not adopted.** The price tilt is small and the rest of the rule averages about +3.5% anyway.
- **IV under 40:** 26 trades, average +3.9%, median +2.6%. The rest of the rule (IV 40+) still averages about +3.6%, so IV does not separate winners from losers inside the rule. **Not a filter.** In bundle 6 the stock-level IV bins showed no monotone pattern (median returns +1.2%, -0.8%, -1.1%, +2.9%, +0.8% across IV fifths), so the earlier "expensive IV hurts" finding has weakened.
- **Market 20-session return above zero:** the subset's second half was negative and the wide list was flat. The rule works in both market trends. **Not a filter.**

### 1.3 Option arms: all retired

- **90-day at-the-money control (old control A): killed.** Its pre-registered kill rule was a negative median in the first 20 trades. Across the bundle 5 control (7 trades, median -8.8%) and the bundle 6 book's 90-day trades (9 trades, median -26.3%), the median is negative and the sample has passed 20 trades. The average stays positive only because a few trades won big. Stop.
- **30-day at-the-money call:** stopped in bundle 5. Bundle 6 confirmed it: the 30-day +0% book trades had a -12.9% median; 30-day +5% trades had a -50% median.
- **Never trade as a standing strategy:**
  - Any call of 30 days or less.
  - Strikes 5% or more out of the money.
  - Double-or-10 structures and wide call spreads.
  - Options bought after a 20-session run above +50%.
  - Any option on a sub-$10 stock as a standard entry (lottery only).
- **Bundle 6's 14-day trades:** 14-day +0% and 14-day +15% both lost 100%. 14-day +5% lost 1.2%. Short-dated calls are the worst structure I have traded.

### 1.4 Ratings: retired

- The ratings test was pre-registered: in bundle 6, the +1 bucket's median minus the 0 bucket's median must be positive.
- Bundle 6 result: +1 (40 stocks) median +0.2%; 0 (113 stocks) median +0.5%. Difference **-0.3%. The test fails.** The -1 bucket (83 stocks) had median -0.1%, and the -2 bucket (7 stocks) was too small to read.
- Bundle 5's +1 > 0 > -1 ordering did not repeat. Ratings are retired entirely. They do not inform entries, sizing or exits.

### 1.5 Entry hygiene

- Enter at the signal-day close. Do not chase the next morning's gap.
- Log every signal, including ones that fail the gate, so the control groups stay complete.
- Keep positions equal in size. No sizing on conviction, ratings or option structure.

## 2. WHAT I TESTED IN THIS BUNDLE

### 2.1 My book (bundle 6)

- **Total:** -$5,686 on 30 trades. Average -19.0%, median -27.4%, 27% winners. All options.
- **30-day +0% (10 trades):** average -4.5%, median -12.9%.
- **90-day +0% (9 trades):** average -21.4%, median -26.3%.
- **30-day +5% (4 trades):** average -49.9%, median -50.0%.
- **90-day +5% (3 trades):** average -12.9%, median -28.6%.
- **14-day trades (3 total):** two at -100%, one at -1.2%.
- **30-day +10% (1 trade):** +107.9%. **30-day +0% (1 trade):** +117.8%. These two large winners were the book's only real gains. Both were on stocks that were up, not down, and both were lottery-sized bets.
- **Lesson:** the book lost because it was options, and the wrong expiry and strike were a multiplier, not the cause. The only structure that made money was a lottery ticket.

### 2.2 Stock-level results (bundle 6, 250 candidates)

- **Buy-all:** average +0.7%, median +0.5%.
- **Market 5-session bins (noisy):** the mildest dip bin (-2.1% to -0.2%) had a median of -3.4% (36% up). The deepest dip bin (below -2.1%) had +0.8%. The bounce did not show up cleanly in this bundle's market bins. The rule still beat buy-all because the off-high condition does the selecting inside the dip. I cannot explain the mild-dip result yet, and it is a reason to keep testing rather than to change the rule.
- **Off-high bins:** the deepest bin (-75% to -31%) had +0.5%; the -30% to -18% bin had +1.9%; -17% to -8% had -0.2%. No clean gradient.
- **RSI:** oversold (6 to 33) +1.4%, and 33 to 44 +1.6%. Mid-range (45 to 66) about -1.0%. Overbought (66 to 95) -0.2%. Oversold names did better this bundle; overbought did not clearly lag.
- **Breadth:** non-monotone. Lowest fifth +1.1%, top fifth +1.3%, middle -0.2% to -0.5%. Breadth is not a reliable ordering signal.
- **Days since spike:** names with a call spike today had a median of -6.2% (2% up); names one session after a spike had +5.6% (94% up). The bins overlap and the sample in each is small. Log only.
- **News:** names with no news in the last 7 days had a median of -10.6%; names with news had higher medians. Too few names in the zero-news bin to trust. Log only.
- **Call-volume signals** (calls ratio, call days, calls 5-day average, calls 20-day): no consistent direction. Log only.
- **Dollar volume and market volatility:** no consistent direction. Not used.

### 2.3 Option-level results (bundle 6)

- **30-day at-the-money calls by IV:** medians of -40%, -34%, -46%, -20%, -24% across the five bins. Negative in every bin.
- **30-day at-the-money calls by implied/realized:** medians of -50%, -19%, -19%, -43%, -24%. Negative in every bin, and the cheapest bin was no exception.
- **Takeaway:** options lose on median regardless of how the implied volatility is priced. Expensive premium does not explain the loss, and cheap premium does not rescue it.

### 2.4 Rule checks scored in bundle 6

- **Primary (-15 off high, market dip):** held in bundle 6 and remains the best rule tested.
- **Control (off high, no dip):** no edge. This is the most useful result from this set of tests: the stock leg alone does not work.
- **Depth -25:** weaker than -15 on median.
- **RSI < 68 gate:** no change in results.
- **Breadth above 50 subset:** strong average on very few trades.
- **Ratings test:** failed. Ratings retired.
- **Sub-test A (stop):** no reported result. Not adopted.

## 3. WHAT I WILL TRY NEXT

Each item is pre-registered. This is the final bundle for this generation, so these are the tests to run on the next stocks I see.

1. **Keep the primary as the only traded rule:** -15 off high, market 5d ≤ -1.5, stock long, exit at session 10, no option.
   - **Pass criteria for the next bundle:** positive median, average above buy-all (+0.7%), and second-half average not negative.
   - **Downgrade rule:** if the second half is negative in two bundles in a row, move the rule to control.
   - **Current second-half status:** pooled +1.4% (bundle 6 positive). Not triggered.

2. **Missing market-leg control (highest priority).** Market 5d ≤ -1.5 with off high > -15. Purpose: test whether the market dip alone predicts a bounce. If this group bounces as well as the primary, the stock-level condition is not needed and the rule should be rewritten around the market leg. If it does not, the two-leg rule stands.

3. **Sub-test A: -15% hard stop on the primary (paper arm).** Carry it from bundle 6 forward as a paper arm. Adopt only if it keeps the median and does not cut the average by more than about 1 percentage point below the primary.

4. **Sub-test B: -20 vs -15 off high.** Score both on identical signals, with at least 20 trades per arm. Promote -20 only if it beats -15 on median in the new bundle as well as in bundle 5. -25 is already dropped.

5. **Breadth above 50 on bounce signals.** The subset had +14.8% average and +7.8% median on 16 trades, but it is too small to act on. Track it separately on new data. Adopt as a filter only if the subset keeps a positive median and beats the rest of the primary on its own.

6. **Price over $50.** Track separately. Adopt only if the over-$50 median stays above +3% and the second half is positive.

7. **Overbought and run-up exclusion.** Only about six primary signals were overbought, so there is nothing to test yet. Drop unless the overbought count rises.

8. **Options: none.** I will not run any option control. The 90-day control is killed. The 30-day control is stopped. The 14-day and out-of-the-money structures are not to be traded.

9. **Ledger (every signal):** gate pass or fail, entry close, exit close after 10 sessions, market 5d and 20d, off-high %, RSI, 20-session return, IV, breadth, dollar volume, and days since the last call spike.

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### 4.1 Evidence, with confidence

- **Options as my primary structure lose (high confidence).** Books of -$4,120, -$3,312 and -$5,686 across bundles 4 to 6. Negative medians in every IV and implied/realized bin I measured.
- **30-day at-the-money calls lose on median (high confidence).** Negative in every bin in bundles 4, 5 and 6.
- **Short-dated calls (14 days) and out-of-the-money strikes destroy capital (high confidence).** Repeated -100% outcomes.
- **Post-selloff bounce with the market leg (medium confidence).** Six of six bundles beat buy-all. Pooled average +3.5%, median +1.5%, 95% range +0.2% to +6.7%. Fading but still positive in the second half.
- **Off-high alone does not predict a bounce (medium confidence).** The control's median is -1.1%.
- **Deeper threshold (-25) is worse than -15 (medium-low confidence).** Lower median and average pooled.
- **Ratings have no edge (medium confidence).** Pre-registered test failed in bundle 6 after a positive bundle 5. Retired.
- **Overbought stocks lag (low confidence).** Did not show up inside the bounce rule; too few overbought signals to test.
- **Breadth above 50 (low confidence).** Strong on 16 trades, too few to adopt.
- **IV predicts stock returns (low confidence now).** Monotone in bundle 5, but no pattern in bundle 6.

### 4.2 Ideas dropped or retired

- **90-day at-the-money call control:** killed (negative median over the sample).
- **30-day at-the-money call:** stopped.
- **Out-of-the-money strikes, double-or-10 structures, wide call spreads, 14-day calls:** never trade.
- **Options after a parabolic run (20-session move above +50%):** never trade.
- **Ratings as a signal:** retired.
- **Deeper off-high threshold (-25):** dropped.
- **IV under 40 as an entry filter:** dropped.
- **Market 20-session return above zero as a gate:** dropped.
- **Call-volume signals (calls ratio, call days, calls 5-day average, calls 20-day):** log only.
- **Dollar volume and market volatility bins:** not used.
- **Sub-$10 stocks as a standard entry:** lottery only.

### 4.3 Open questions

- **Is the bounce a market-regime effect or a stock-level reversal?** The control says the stock leg alone does nothing. The missing market-leg control (section 3, item 2) will settle whether the market dip is the whole rule.
- **Why does the mild market-dip bin lose in bundle 6?** The rule still beat buy-all in that bundle, but the market bins are noisy and the pattern does not match bundle 5's.
- **Does the effect survive new data?** The first half averaged +6.7% and the second half +1.4%. If the next bundle's second half is flat or negative, treat the bounce as a regime that has ended and stop trading it.
- **What separates the large option winners from the large losers?** I still cannot tell from the columns I have. Until I can, I do not trade options.

(Recorded by the system: this trader ran 25 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)

### Agent 3's final notes (not passed on)

# TRADING NOTES: GENERATION 2, after bundle 6 of 6

## 1. CURRENT STRATEGY

**Core principle:** Judge every rule by the stock's own 10-session return, not by option P&L. Options have not shown a stable positive median in any bundle I have tested. Trade the stock only, flat size, no adding after wins.

**Status: rule C is on hold.** It is no longer a live rule. It stays on paper, with no sizing, until a bundle confirms it. Bundle 6 did not pass the test I set for it (see Section 2).

### Rule C (paper only): trend in a weak market, stock long

**Entry, all required:**
- **Trend:** 20d % ≥ 20.
- **Market down:** market 5d % < 0. *(Unconfirmed; see below.)*
- **Extension cap:** vs ma20 % ≤ 7.6 and close vs vwap % ≤ 0.8. *(Weakened in bundle 6; keep the cap but treat it as moderate-low confidence.)*
- **Price:** ≥ $10.
- **Liquidity:** dollar volume ≥ $14M (prefer $30M+).
- **Flow block:** call days 2x+ (last 5 sessions) must not be 0 or 1. Short-dated call activity (short) must not be exactly zero.

**Instrument:** the stock, long. No options.
**Exit:** hold 10 sessions. No stops, no targets.
**Sizing:** flat and identical on every trade. Size is zero until rule C is confirmed on a bundle I log directly.

**Evidence and confidence:**
- Bundles 1 to 5 (rule check, 23 trades): +7.2% average, +2.1% median, 65% winners, beat the all-candidate benchmark in 4 of 5 bundles. This came from a rule chosen from earlier bundles' data, so it is in-sample.
- Bundle 6: no logged rule C trades. The bundle 6 bins are not enough to rebuild the intersection, and the individual bins for the trend and market gates were weak (see Section 2). Confidence in rule C is now **low to moderate**.

### Filters that block entries (all candidates)

- **Price under $10, or dollar volume under $14M.** Keep as a floor. Bundle 6 gave no sign that the thinnest names are better or worse in a way I can use.
- **Call days 2x+ of 0 or 1 in the last 5 sessions.** Avoid. Confidence **high**. Bundle 6: the 0-1 bin had a -3.6% median (26% up). Bundles 4, 5 and 6 all agree.
- **Short-dated call activity exactly zero.** Avoid. Confidence **moderate-high**. Bundle 6: -5.0% median, 29% up. Bundle 6 is the sixth bundle in a row where this group was weak.

### Soft signals (weigh, do not block)

- **Implied volatility above about 89%:** bundle 5 said weak (-3.2% median). Bundle 6 did not replicate it (the 93 to 314 bin was +0.8%, 51% up). Downgraded to a neutral note.
- **Beta above about 1.9:** bundle 6's top beta bin (1.96 to 6) was -3.4% median, 30% up. Bundle 6's 1.42 to 1.92 bin was +3.3%, 72% up. The sign flips at the top, so this is at most a soft negative at the extreme. Bundle 4 and 5 conflict with each other on this too.
- **Vs ma50 at 11 and above:** bundle 4 and 5 said weak (about -1.5%). Bundle 6 showed -0.2%. Downgraded to a very soft note.
- **Breadth 67.9 to 80.5%:** positive in bundle 5 (+2.2%) and mildly positive in bundle 6 (+1.3%, 60% up). Two bundles, same direction, still small. Watch.

### Ratings

Ratings stay out of entries. In bundle 6 the pattern ran against my earlier "no consistent order" reading: rated +1 had a -0.7% median (23 stocks), rated -1 had +1.1% (94 stocks), and rated -2 had -1.4% (8 stocks, watch only). That is one bundle, so it is a note, not a rule. Track it, and do not trade on it.

### Options (retired from live trading)

- **30-day at-the-money call, held 10 sessions:** Retired from live trading. Bundle 6's all-candidate figures for this instrument had negative medians in every implied-volatility bin (-24% to -46%) and every implied/realized bin (-19% to -50%). Bundle 5 had a positive median, bundle 4 a negative one. The positive results in some bundles came from a small number of large winners.
- **All out-of-the-money and 90-day calls:** Retired.
- **Call spreads, double-or-10 exits, and fixed +5/+10/+15% out-of-the-money targets:** Retired.
- **My bundle 6 option trades were a breach of this plan.** I traded calls, not rule C stock entries, despite the rule to keep options paper-only. Stop option trades entirely.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### My own trades (28, all calls)

- Profit: +$4,258. Average +15.2%, median -34.5%, 32% winners.
- The 30-day at-the-money call held 10 sessions (17 trades) had +18.3% average and -10.4% median. The +5% setting (5 trades) had +57.8% average and -71.3% median. The +10% setting (4 trades) averaged -75.0%.
- The profit came from five large option winners (+157%, +118%, +513%, +521%, +225%). In those trades the stock moved +2.6% to +32.6% and premium was cheap (1.1% to 10.7% of price). Most losers lost close to the whole premium, and most stocks in the losing trades were flat to down.
- **Conclusion:** option P&L is a lottery on a few large moves. The median trade lost money. This is not a repeatable edge, and it is not what the stock rules measure.

### Stock-level results (250 candidates)

- All candidates: average +0.7%, median +0.5%. This is the benchmark for any stock rule.
- Option result by implied volatility bin (30-day at-the-money call, held 10): medians -40%, -34%, -46%, -20%, -24%. No bin was positive.

### Rule C in bundle 6: not confirmed

The pre-set test was: keep rule C if the bundle 6 median is above zero and the average beats the benchmark. I did not log rule C trades in bundle 6, so the test cannot be run directly. The bin evidence does not support keeping it live:

- **Trend (20d % ≥ 20):** the top 20d bin (13.3 to 123%) had +0.8% median, 52% up. Not a meaningful edge.
- **Market down (market 5d < 0):** the -2.1 to -0.2% bin had **-3.4% median, 36% up**. The -11.5 to -2.2% bin had +0.8%, 52% up. This contradicts bundle 5's +1.8% for the same gate. The market gate is now a coin flip.
- **Extension cap:** vs ma20 above 6 had -0.3% median, 50% up. Bundle 5's -2.4% to -3.2% was not repeated. The cap is still not contradicted, but the evidence for it weakened.
- **Close vs vwap above 0.63:** +1.2% median, 56% up. This bin was positive, not negative, so the close-vs-vwap cap is not supported here.

**Decision:** rule C moves to paper only, at zero sizing, until a logged bundle confirms it. Rule C is not dropped, because bundle 6 gave no clean rule test.

### Filter bins that held in bundle 6

- **Call days 2x+ 0-1:** weak again (-3.6% median, 26% up). Strongest result in the bundle set.
- **Zero short-dated calls:** weak again (-5.0% median, 29% up).
- **Medium-dated calls ratio 0.26 to 0.69:** +2.7% median, 70% up. Positive, but I did not test it inside any rule, and it is one bin.
- **Puts 5-session average 1.38 to 2.49:** +1.4% median, 64% up. Also one bin, untested.

### Bins that failed or were mixed

- **Market 5-session down:** failed (see above).
- **Trend at 20d ≥ 20:** top bin weak (+0.8%).
- **Extension cap at 7.6:** softened.
- **Implied volatility above 89%:** not replicated.
- **Beta above 1.9:** flips sign at the top; mixed.
- **Market 20-session dip:** -4 to -0.1% bin was -1.8% (40% up); -12.3 to -4.2% bin was +2.8% (66% up). Mixed, deprioritized.
- **Days since spike:** the bins are tied and hard to read. The spike-today bin was -6.2% with only 2% up, while the 0-to-1 bin was +5.6% and 94% up. Not usable until I can separate these cleanly.
- **Option cost and news bins:** heavily tied. The 10% option-cost floor and the zero-news bins produce wide, unreliable spreads. Do not use them for decisions.

### Bundle-level context

- Bundle 6's all-candidate median (+0.5%) was close to flat. A stock rule needs to beat roughly zero to be useful, and most bins did not.

---

## 3. WHAT I WILL TRY NEXT

1. **Paper-track rule C on the next bundle, logged directly.** Log every candidate that passes the rule, with bundle number, 10-session stock return, and the benchmark. Confirm rule C only if the median is above zero and the average beats the benchmark. Drop it if the median is below zero. Do not change the thresholds before the next bundle.

2. **Market gate test.** Split the market 5-session condition into three bins and check each one inside the trend group. The bundle 5 and bundle 6 results disagree, so I need a clean read before I keep the gate.

3. **Flow block as the one firm filter.** Keep "call days 2x+ of 0 or 1 is an avoid" and "zero short-dated calls is an avoid." Test whether they hold inside any other rule I build.

4. **Ceiling test within trend.** Split trend at 40 on the next bundle. Only add a ceiling if the above-40 group is clearly worse across two bundles.

5. **Medium-dated call ratio (0.26 to 0.69) and puts 5-session average (1.4 to 2.5).** Both showed positive medians in bundle 6, which is a single read. Log them on every candidate for the next bundle as cross-checks. Do not trade on them yet.

6. **Ratings (-1 versus +1).** Track whether the -1 group beats the +1 group again. Two bundles with opposite signs would settle it as noise. Still not an entry input.

7. **Options: paper only, with a fixed log.** For any future option mark, record strike, premium as percent of price, implied volatility, days to expiry, entry and exit stock close, model value at exit, and whether the mark differs from the model by more than 30 points. Do not trade options live until the median is positive across at least two bundles.

8. **Trade log discipline.** Every trade must be tagged as "rule C stock" or "other." No option trades unless the rule explicitly allows them.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Held up across bundles

- **Call days 2x+ of 0 or 1 is an avoid.** Bundles 4, 5 and 6. Confidence: high.
- **Zero short-dated call activity is an avoid.** Confidence: moderate-high.
- **Option results are unstable on median and do not support live sizing.** Confidence: high that they should stay out of sizing. Low on direction.

### Weak, mixed or unproven

- **Rule C (trend plus market-down plus caps).** Bundles 1 to 5 positive; bundle 6 not tested directly and its bins weak. Confidence: low to moderate. Paper only.
- **Extension cap at 7.6 and close-vs-vwap at 0.8.** Held in bundles 2 to 5; weak in bundle 6. Confidence: moderate-low.
- **Market 5-session down gate.** Bundle 5 positive, bundle 6 negative. Confidence: low.
- **Beta extremes.** Mixed; soft only.
- **Breadth 67 to 80%.** Two bundles mildly positive. Watch.
- **Thin names under about $14M.** Mixed. Keep the floor.
- **Ratings.** Bundle 6 showed -1 above +1. Single bundle. Watch only.

### Dropped

- **Ratings as an entry input.** Dropped.
- **Trend plus flow with no market gate (rule B).** Dropped (-2.0% average, -4.1% median earlier).
- **Pullback 15-29% off the 60-day high.** Dropped.
- **Market 20-session dip as a primary gate.** Deprioritized.
- **Shallow dip inside uptrend (vs ma50 -8 to 0).** Dropped; too few trades.
- **90-day and out-of-the-money calls, 5% and 10% out-of-the-money calls, call spreads, double-or-10 exits.** Retired.
- **Sub-$10 names.** Excluded.
- **All option trading as a live strategy.** Halted after bundle 6.

### Open questions for the next bundle

- Does rule C keep a positive median when logged directly on new stocks?
- Does the market 5-session down gate separate outcomes inside the trend group?
- Do the medium-dated call ratio and puts 5-session average hold their bundle 6 signal?
- Does breadth above 67% carry weight inside any rule?

(Recorded by the system: this trader ran 20 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)

### Agent 4's final notes (not passed on)

# TRADING NOTES: GENERATION 2, FINAL (after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Status: real-money option trading stays suspended.** Everything runs on paper until a rule meets all four re-entry criteria in section 1.6. No current setup meets them.

### 1.1 What I trade: nothing with real money yet

Across six bundles, every 10-session at-the-money or near-the-money 30-day call setup has had a negative median option return. Bundle 6 made that clear again: total P&L -$15,636 on 36 trades, median -73.7%, 25% winners. The stock-level median across all 250 candidates was +0.5%, so the broad market gave no help to a long-call wrapper.

The reasons the option wrapper fails here:

- **Premium and cost are large relative to typical moves.** Bundle 6 option costs were roughly 0.2% to 7% of the price for the premium paid, plus about 10% round-trip cost on most lines. A typical candidate's 10-session move was about 1%. The stock has to make a large move in the right direction within a short window just to break even.
- **Option results do not track the stock move cleanly.** In bundle 6 several trades lost 100% while the stock rose (for example, a stock up about 7% and a stock up about 13% with a -100% option result). Others gained 150% to 190% on stocks up 3% to 12%. Until I audit fills, exit assumptions, and pricing, I cannot tell whether the model is accurate. This is a model-risk problem, not just a signal problem, and it is a blocker for any real-money option trade.
- **The 10-session exit has no evidence of superiority.** The option-level median is negative under every exit tested.

### 1.2 What I trade on paper: stock-level signals

These are ranked by how consistently they hold, not by their average.

**P-C. Market dip rebound (strongest broad rule, moderate confidence).**
- Columns: market 20d % between -12 and -4.
- Instrument: the stock itself (shares), long only.
- Hold: 10 sessions.
- Evidence (401 trades, pooled through bundle 6): average +1.7%, median +1.3%, 56% up. The 95% range by resampling whole weeks is -3.6% to +6.1%. Beat the all-candidate benchmark in 4 of 6 bundles. Wide list (no hindsight): 164 trades, average +0.6%, median +1.3%.
- Caveats: the edge is concentrated in the first half of each month (+6.7%) versus the second half (+0.1%). In bundle 5 the wider -12 to -1 band had a negative median. Confidence is moderate that the stock-level return is positive, and low that it survives a split by half-month.

**P-F. High breadth (strongest on the no-hindsight list, moderate confidence).**
- Columns: breadth % at or above 67.8 (roughly the top fifth of the historical range).
- Instrument: shares, long.
- Hold: 10 sessions.
- Evidence (387 trades, pooled): average +1.7%, median +1.0%, 55% up. Beat the benchmark in 5 of 6 bundles. Wide list: 158 trades, average +1.2%, median +1.4%. This is the only rule whose wide-list median is above its full-sample median, which matters because it was not selected with hindsight.
- Bundle 6 bin 67.9 to 80.5: +1.3% median, 60% up, consistent with the pooled result.
- Confidence: moderate. It has the best no-hindsight evidence of anything I track. The first-half and second-half split is +0.7% and +1.9%, so both halves are positive.

**P-E. Momentum gate with low implied-to-realized volatility (paper, low confidence).**
- Columns: 20d % at or above 20, iv/realized at or below 0.8, shares only.
- Hold: 10 sessions.
- Evidence (136 trades, pooled): average +6.1%, median +0.7%, 54% up. Beat the benchmark in 5 of 6 bundles. The 95% range is +1.8% to +11.7%.
- Wide list: 21 trades, average +1.7%, **median -1.8%**. The average depends on a small number of large winners, and the wide-list median is negative.
- Confidence: low. The positive average is real in the sample but its median is fragile and the no-hindsight version is negative. Do not promote until the wide-list median is positive over at least 30 trades.

**P-A. Momentum gate alone (demoted to watch).**
- Columns: 20d % at or above 20, vs ma50 % at or above 15, days since spike at or above 1.
- Evidence (118 trades, pooled): average +4.6%, median +0.1%, 50% up. Beat the benchmark in 5 of 6 bundles, but the median is essentially zero.
- Wide list: 9 trades, average -1.9%, median -3.1%.
- Confidence: low. The gate's average is driven by tails. It is not a standalone rule.

### 1.3 Option structures: all paper, none tradable

- 30-day at-the-money call, hold 10: negative median in all six bundles. Bundle 6 median -100% on several trades.
- 30-day at-the-money call, 5% or 10% out-of-the-money, hold 10: bundle 5 median +17.9% on four trades. Bundle 6 showed +3.0% average on one trade (+15%-strike variant had +18.2% average on two trades). Across bundles the sample is about 12 trades with a mixed median. Too small to act on.
- 30-day call with a +10% double-or-10 exit: bundle 6 average -0.5%, median -72.1% on nine trades. Negative median.
- 90-day at-the-money call on the momentum gate (P-B): median -22.9% over 31 trades. Negative.
- 14-day at-the-money call: bundle 5 had three trades with a +139% median, and bundle 6 had two trades with -26% and one with -100%. Too few trades to call it.
- Call spreads (30-day, 0% to +10%): negative median in bundles 4, 5, and 6.

### 1.4 Rules I no longer use

- **Call-days 2x+ 3–5 band.** The bundle 5 result (+3.0% median, 64% up) did not hold. Pooled over 737 trades it is average +0.5%, **median -0.6%**, 48% up, beat the benchmark in only 3 of 6 bundles. Wide list: 284 trades, average -0.3%, median -0.4%. Demoted to dropped.
- **Call-days 1–2 band.** Pooled over more than 1,200 trades it has a median near zero, and the 0–1 bin has been weak in multiple bundles. Dropped as a lead rule.
- **Extension reversal (vs ma50).** No edge in the pooled data. Dropped.
- **Ratings.** Ratings were not used for any decision. In bundle 6, stocks I rated -1 averaged +2.9% over 10 sessions, and stocks I rated +1 averaged -1.0%. That is an inverse relation in one bundle, and I will not treat it as a signal. It is a reason to audit how I rate, not a reason to flip the ratings.

### 1.5 Position and risk rules (for any future real money)

- Sub-$10 names: paper only. Bundle 6 showed large sub-$10 outliers in both directions, and the average is dominated by them.
- Liquidity (dollar volume) is not a reliable filter on its own; it has had no consistent effect on median returns.
- Size any eventual trade so that a full loss of the premium is tolerable. Bundle 6 showed that a single bad option position can lose more than the premium's expected value.

### 1.6 Re-entry criteria for real money

A rule returns to real money only when all four hold:

1. Median option result is positive over at least 60 trades pooled across bundles.
2. Both halves of the month sample are positive.
3. The stock-level median on the same signals exceeds the round-trip option cost (about 10%) plus decay. For a stock-only rule, the stock median must simply be positive after realistic fills.
4. The wide-list (no-hindsight) sample is also positive, with at least 30 trades.

No current setup meets all four. P-C and P-F come closest on criteria 2 and 4 at the stock level. Neither is an option trade.

---

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

### 2.1 My own trades (36 trades, real money, option-based)

- Loss: -$15,636. Median -73.7%, average -43.4%, 25% winners.
- 30-day at-the-money call, hold 10: 9 trades, average -61.5%, median -71.8%.
- 30-day at-the-money call, +10% strike, double-or-10 exit: 9 trades, average -0.5%, median -72.1%.
- 30-day at-the-money call, +0% strike, hold 10: 4 trades, median -60.9%.
- 30-day at-the-money call, +5% strike, hold 10: 4 trades, median -95.4%.
- 30-day call, +15% strike, hold 10: 2 trades, average +18.2%. The only positive average among the common structures, but on two trades.
- Several other single-trade structures lost 22% to 100%.
- Losers and winners both had stock moves in the same range: stocks that fell 3% to 11% lost 100%, and stocks that rose 3% to 12% produced winners of +73% to +191%, plus several -100% losses on stocks that also rose. The option result was not a clean function of the stock move. This needs an audit before any further real-money option trade.

### 2.2 Stock-level results, all 250 candidates

- Average +0.7%, median +0.5%.
- Rated +1 (49 stocks): average -1.0%. Rated -1 (87 stocks): average +2.9%. Ratings are not used.
- Call-ratio fifths: the lowest call ratio (0.01 to 0.77) had the best median (+2.6%, 64% up). The highest call-ratio fifth (5.45+) was +0.7%. Single-bundle observation.
- Short-dated call ratio at zero: median -5.0%, 29% up. Single-bundle observation, possibly related to names with no active short-dated call interest.
- Medium-dated call ratio, 1.53 to 5.6: median -2.4%, 36% up.
- Market 20-day at -12.3 to -4.2: median +2.8%, 66% up (supports P-C). Market 20-day at -4 to -0.1: median -1.8%, 40% up.
- Market 5-day at -2.1 to -0.2: median -3.4%, 36% up. Watch item.
- Breadth 67.9 to 80.5: median +1.3%, 60% up (supports P-F).
- Implied volatility bins: 8.5 to 30.3 median +1.2%; 61 to 90.9 median +2.9%. Mixed.
- News: names with zero news in the prior 7 days had 46% up in the middle bin. Tied-value bins are small. Watch item.
- Off-the-high bin -30.1 to -17.7 had median +1.9%, 54% up. Watch item.

### 2.3 Option-level IV bands (30-day at-the-money call, hold 10)

- IV 8.5 to 30: median -40%, average -17%.
- IV 30 to 42: median -34%, average -25%.
- IV 44 to 60: median -46%, average +13% (skewed by a few large winners).
- IV 61 to 90: median -20%, average +1%.
- IV 90 to 314: median -24%, average +2%.
- Every IV band has a negative median. Option-level IV does not rescue the setup.

### 2.4 New idea tested: low implied-to-realized volatility

- Tested as P-E at the stock level. The stock median was +0.7% (136 trades), but the no-hindsight sample was -1.8% median (21 trades). Inconclusive, kept on paper.
- The iv/realized bins for the full bundle: 0.13 to 0.73 had -1.9% median; 0.73 to 0.96 had +2.0% median, 63% up; 0.97 to 1.22 had +0.7%. Non-monotonic, which argues against a clean relationship.
- Option level: the iv/realized ≤ 0.72 fifth had a median near -50%. Cheap options did not produce a positive option median.

### 2.5 Results I should treat as noise

- Individual single-trade wins of +100% or more, mostly on sub-$10 names. These drive the averages and do not repeat.
- The +9.0% bin for option cost at exactly 10% (97% up). This is a tied-value artifact, not a signal.
- The zero-news bins with 0% or 100% up. These are tied values with very small counts.

### 2.6 What this bundle told me

- The stock-level evidence that has held most consistently is market-dip rebound (P-C) and high breadth (P-F). Both are positive on medians, both have wide-list samples, and neither depends on a single bundle.
- The option wrapper is the binding constraint, and the option results do not reconcile cleanly with stock moves. Until that is audited, option results are not decision-grade.
- Momentum and low IV/realized look positive on averages but are fragile on medians and on the no-hindsight list.
- Discretionary selection did not add value in this bundle.

---

## 3. WHAT I WILL TRY NEXT

Each test needs at least 60 trades pooled across bundles, both halves of the month reported, a same-tenor benchmark, and one change at a time. Stock-level tests come first.

1. **Audit the option model before any further option paper trades.** Reconcile the -100% outcomes on stocks that rose, check fill and exit assumptions, and confirm how each option's expiry and strike were selected. Pass criterion: the modeled option result for a given stock path should match a hand calculation within a reasonable tolerance on at least 10 trades.

2. **High breadth on shares (P-F), priority.** Track breadth at or above 67.8 on the stock level. Target 60+ wide-list trades. Report first and second halves of each month. Test whether the effect holds when market 20-day is negative versus positive, to see whether breadth is independent of the dip rule.

3. **Market dip rebound split (P-C).** Compare -12 to -4 against -4 to 0 and 0 to +3, all on stock returns, all reported by half-month. Check whether the first-half edge is a calendar artifact.

4. **Combined P-C and P-F (stock level).** Test the joint condition (market 20-day between -12 and -4 and breadth at or above 67.8). If it cannot beat either rule alone, keep them separate.

5. **Momentum with low IV/realized (P-E), wide-list only.** Grow the no-hindsight sample to 30 trades before any further judgment. If the wide-list median stays negative, drop it.

6. **Option cost comparison.** For every paper setup, log stock median and option median side by side. If the stock median cannot cover about 10% plus decay, the setup is not an option trade.

7. **Exit timing (stock level).** Compare exits at 5, 10, and 20 sessions on P-C and P-F. The 10-session exit has no evidence of superiority.

8. **Watch items (no action):** market 5-day moves between -2 and 0 (weak in bundles 4, 5, and 6), zero news in the prior 7 days, names sitting 12% or more off their high, and call-ratio bins at zero for short-dated calls.

9. **Ratings.** Keep logging them, do not act on them. Audit whether my ratings have any predictive value against stock returns, pooled across bundles, before deciding whether to keep recording them.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### 4.1 Evidence summary by rule (pooled through bundle 6)

| Rule | Trades | Average | Median | Hit rate | Bundles beating benchmark | Wide list (no hindsight) | Status |
|---|---|---|---|---|---|---|---|
| P-C market dip (20d -12 to -4), stock | 401 | +1.7% | +1.3% | 56% | 4 of 6 | 164 trades, avg +0.6%, median +1.3% | Paper, strongest broad rule |
| P-F high breadth (≥67.8), stock | 387 | +1.7% | +1.0% | 55% | 5 of 6 | 158 trades, avg +1.2%, median +1.4% | Paper, best no-hindsight result |
| P-E momentum + iv/realized ≤0.8, stock | 136 | +6.1% | +0.7% | 54% | 5 of 6 | 21 trades, avg +1.7%, median -1.8% | Paper, fragile |
| P-A momentum gate, stock | 118 | +4.6% | +0.1% | 50% | 5 of 6 | 9 trades, avg -1.9%, median -3.1% | Demoted to watch |
| Call-days 2x+ 3–5, stock | 737 | +0.5% | -0.6% | 48% | 3 of 6 | 284 trades, avg -0.3%, median -0.4% | Dropped |
| All candidates (benchmark) | 2,998 | — | ~+0.5% | — | — | — | Reference |
| 30-day ATM call, hold 10, option | many | mixed | negative in all six bundles | — | — | — | Not tradable |
| 90-day ATM call on momentum gate | 31 | -2.3% | -22.9% | 39% | 4 of 5 | 2 trades, -49.5% | Paper control only |

### 4.2 Confidence levels

- Option median negative for every 10-session at-the-money setup: high (six bundles).
- Option results do not reconcile cleanly with stock moves: high. This is a model-audit issue.
- Market-dip rebound on stock: moderate. Positive in the pooled sample, weaker in the second half of months.
- High breadth on stock: moderate. Best no-hindsight evidence I have.
- Momentum gate alone: low. Positive average, near-zero median, negative wide list.
- Momentum with low IV/realized: low. Positive average, fragile median, negative wide-list median.
- Call-days 3–5 and 1–2 bands: dropped. Pooled medians are at or below zero.
- Out-of-the-money (10%) call at 30 days: very low. About 12 trades with a mixed median.
- Ratings: none. Inverse relation in bundle 6 is noted, not used.

### 4.3 Dropped or downgraded

- Call-days 3–5 band (bundle 5's positive result did not hold pooled).
- Call-days 1–2 band (median near zero, weak in multiple bundles).
- Extension reversal vs ma50 (no pooled edge).
- Liquidity and extension add-ons (no consistent effect).
- IV ≤ 90 gate (no help in bundle 4; replaced by the paper iv/realized test, which is also weak).
- Ratings for any decision.
- Out-of-the-money calls at 5%+ strikes and 90-day 5%-out calls (negative medians across bundles).
- Call spreads at 30 days (negative median in bundles 4, 5, and 6).
- Option-level news add-on.
- Sub-$10 names for real money.

### 4.4 Honest caveats

- Samples are small. Most option subsets have fewer than 15 trades, and single-bundle differences are not reliable.
- Several rules worked in one bundle and failed in another: the momentum gate, the call-days bands, the market-dip band as it was defined in bundle 5, and the liquidity add-on.
- Averages on the stock level are dominated by a handful of very large winners, often in sub-$10 names. Judge by median and hit rate, and show the average separately.
- Fills on thin or cheap names are probably worse than the model. Real-money fills must be logged against modeled cost before any real trade.
- The three generation-2 real-money results to date are -$9,074 (bundle 4), -$2,106 (bundle 5), and -$15,636 (bundle 6). Option-based discretionary trading has lost money in every bundle where it was run. That record is the strongest evidence I have, and it argues for staying on paper.
- What is most likely true: no option wrapper I have tested has a reliable positive median, and my discretionary selection has not added value. The stock-level market-dip and breadth rules are the most promising direction, but neither has been confirmed on a clean, no-hindsight sample of sufficient size. Confirming them is the work for the next generation.

(Recorded by the system: this trader ran 27 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)


## Generation 9

### Editor's rules, tested on all training months and bundles

- S1 90d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 90-day call 0% above the price, exit hold10): 45 trades, average -1.0% (95% range -16.2% to +15.6%, resampling whole weeks), median -14.5%, 40% winners. Buying every candidate the same way: -8.4%. Beat that in 3 of 5 bundles; first half of the months +4.5%, second half -3.3%.
- S1 30d ATM replicate (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 30-day call 0% above the price, exit hold10): 138 trades, average +28.4% (95% range +0.5% to +68.4%, resampling whole weeks), median -21.5%, 39% winners. Buying every candidate the same way: -11.8%. Beat that in 6 of 6 bundles; first half of the months +26.4%, second half +29.5%.
- S1 tail 90d 5% above (when 20d % >= 40 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 90-day call 5% above the price, exit hold10): 15 trades, average -8.7% (95% range -24.9% to +12.8%, resampling whole weeks), median -8.7%, 33% winners. Buying every candidate the same way: -7.4%. Beat that in 2 of 3 bundles; first half of the months +4.7%, second half -15.4%.
- Strong momentum plus news 30d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and news 7d >= 1: buy the 30-day call 0% above the price, exit hold10): 110 trades, average +35.2% (95% range +3.0% to +79.2%, resampling whole weeks), median -25.9%, 36% winners. Buying every candidate the same way: -11.8%. Beat that in 5 of 6 bundles; first half of the months +3.1%, second half +57.4%.
- Strong momentum price over 50 30d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and price = >$50: buy the 30-day call 0% above the price, exit hold10): 36 trades, average +51.7% (95% range -4.8% to +114.3%, resampling whole weeks), median -19.6%, 44% winners. Buying every candidate the same way: -11.8%. Beat that in 6 of 6 bundles; first half of the months +38.9%, second half +61.9%.
- Screen plus trend 90d ATM (when news 7d >= 1 and call days 2x+ >= 2 and vs ma50 % > 0 and market 20d % > 0: buy the 90-day call 0% above the price, exit hold10): 55 trades, average -3.0% (95% range -20.3% to +11.4%, resampling whole weeks), median -19.8%, 40% winners. Buying every candidate the same way: -8.4%. Beat that in 3 of 6 bundles; first half of the months -12.2%, second half +1.1%.
- R1 over 50 restated (when rsi > 70 and calls 20d > 2 and market 20d % > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 42 trades, average +30.8% (95% range -15.3% to +86.1%, resampling whole weeks), median -21.5%, 43% winners. Buying every candidate the same way: -12.2%. Beat that in 5 of 6 bundles; first half of the months -22.1%, second half +66.8%.
- S2 trend news 30d ATM (when vs ma50 % > 11.9 and news 7d >= 1 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 174 trades, average +24.5% (95% range -3.3% to +55.7%, resampling whole weeks), median -25.9%, 35% winners. Buying every candidate the same way: -11.8%. Beat that in 5 of 6 bundles; first half of the months +0.9%, second half +39.6%.

### The same rules on the blind scoring months (never shown to agents)

- S1 90d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 90-day call 0% above the price, exit hold10): 44 trades, average +6.6% (95% range -22.2% to +45.6%, resampling whole weeks), median -17.5%, 32% winners. Buying every candidate the same way: -7.2%. Beat that in 4 of 6 bundles; first half of the months -11.1%, second half +24.4%.
- S1 30d ATM replicate (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 30-day call 0% above the price, exit hold10): 128 trades, average -3.3% (95% range -24.7% to +20.9%, resampling whole weeks), median -39.4%, 30% winners. Buying every candidate the same way: -15.4%. Beat that in 5 of 6 bundles; first half of the months -7.6%, second half +1.7%.
- S1 tail 90d 5% above (when 20d % >= 40 and vs ma50 % >= 15 and market 20d % > 0 and shares >= 1: buy the 90-day call 5% above the price, exit hold10): 18 trades, average +30.5% (95% range -30.2% to +153.0%, resampling whole weeks), median -18.1%, 28% winners. Buying every candidate the same way: -7.1%. Beat that in 1 of 3 bundles; first half of the months -27.4%, second half +88.4%.
- Strong momentum plus news 30d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and news 7d >= 1: buy the 30-day call 0% above the price, exit hold10): 99 trades, average +4.1% (95% range -24.4% to +34.5%, resampling whole weeks), median -33.3%, 33% winners. Buying every candidate the same way: -15.4%. Beat that in 4 of 6 bundles; first half of the months -2.9%, second half +10.7%.
- Strong momentum price over 50 30d ATM (when 20d % >= 20 and vs ma50 % >= 15 and market 20d % > 0 and price = >$50: buy the 30-day call 0% above the price, exit hold10): 26 trades, average -19.9% (95% range -36.3% to -2.3%, resampling whole weeks), median -32.1%, 31% winners. Buying every candidate the same way: -15.4%. Beat that in 3 of 5 bundles; first half of the months -19.1%, second half -20.5%.
- Screen plus trend 90d ATM (when news 7d >= 1 and call days 2x+ >= 2 and vs ma50 % > 0 and market 20d % > 0: buy the 90-day call 0% above the price, exit hold10): 56 trades, average -15.4% (95% range -27.4% to -5.3%, resampling whole weeks), median -24.8%, 23% winners. Buying every candidate the same way: -7.2%. Beat that in 2 of 6 bundles; first half of the months -18.2%, second half -12.0%.
- R1 over 50 restated (when rsi > 70 and calls 20d > 2 and market 20d % > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 26 trades, average -16.2% (95% range -48.1% to +15.8%, resampling whole weeks), median -48.5%, 31% winners. Buying every candidate the same way: -19.3%. Beat that in 2 of 3 bundles; first half of the months +2.0%, second half -37.6%.
- S2 trend news 30d ATM (when vs ma50 % > 11.9 and news 7d >= 1 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 155 trades, average -1.4% (95% range -23.5% to +22.9%, resampling whole weeks), median -38.1%, 34% winners. Buying every candidate the same way: -15.4%. Beat that in 5 of 6 bundles; first half of the months -8.9%, second half +6.1%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

(Committee editor's synthesis. Inputs: the previous playbook, four traders' final notes, and the code-tested scores of each trader's rules on all candidates over six bundles. Where a trader's figure and the scorebook differ, the scorebook is used.)

**Conventions.** Returns are per-trade option returns on premium, bought on the signal day and held 10 sessions unless noted.
- "Benchmark" means buying every candidate with the same expiry, strike and exit.
- "Range" is the 95% range from resampling whole weeks.
- "Halves" are the first and second half of the sample by month.
- "x of 6" is how many of the six bundles the rule beat its benchmark in.
- Every rule is written with exact conditions so it can be restated and scored.

**Test-environment facts that change earlier assumptions (stated by the people who run the test):**
- **Trading costs are charged everywhere**, including the scorebook and every benchmark. Each side costs 5% of premium or $0.05 a share, whichever is larger.
  - The previous playbook said the scorebook charged no spread. That was wrong.
  - This explains much of the benchmark loss of about -11% to -12%. A round trip costs at least 10% of premium, and much more on cheap options.
  - The $0.05 floor bites hardest on sub-$10 stocks, low-IV names, and far out-of-the-money strikes. This is a hypothesis, not a tested result.
- **The "-100% on a stock that rose" marks were real expiries.** Those calls expired inside the hold and were settled at exercise value. Such contracts are no longer offered, and the scorebook skips them.
  - Older figures that included them are history.
  - The earlier "mark audit" worry about those trades is mostly answered.
  - The previous generation's rule statistics (section 1B) were computed before this fix. They must be treated as unreplicated until re-scored.
- **Puts, short selling, spreads and in-the-money calls are NOT available.** Data is daily closes only.
  - The previous playbook's "deep ITM calls, bull call spreads, put debit spreads and bear call spreads" ideas cannot be tested. They are removed.
  - Only long calls (30-day or 90-day; 0%, 5% and 10% above the price) with a fixed hold or simple exit are testable.

---

## 0. BOTTOM LINE

**The average call loses. Rules that pick very strong, trending names in an up market turn the average clearly positive, but the median stays negative. Only two 90-day baskets show a positive median, and both flip sign between halves.**

Benchmark averages for buying every candidate, held 10 sessions, costs included:

| Structure | Benchmark average |
|---|---|
| 30-day at-the-money (ATM) | -11.8% |
| 30-day 5% above | -12.2% |
| 30-day 10% above | -17.7% |
| 90-day ATM | -8.4% |
| 90-day 5% above | -7.4% |
| 90-day 10% above | -9.7% |

**What this generation established:**
1. **The best verified call rule is the strong-momentum gate (S1).**
   - It is 20d % ≥ 20, vs ma50 % ≥ 15, market 20d % > 0, shares ≥ 1, bought as a 30-day ATM call.
   - Result: 138 trades, **+28.4%**, 6 of 6 bundles, both halves positive (+26.4% and +29.5%). Median -21.5%.
   - Its range (+0.5% to +68.4%) barely clears zero, so the edge is real in direction but wide in size.
   - Two of its reported variants have a median near -16%.
   - ATM beats the 10%-above strike on median for the same idea (-21.5% versus -57.4% in the old scorebook).
2. **Stock-level edges are small, and options are leveraged bets on large moves.**
   - The same S1 gate bought as shares: 168 trades, average +6.0%, **median +1.4%**, 55% winners, 6 of 6 vs a +0.6% benchmark (traders' tally).
   - The 40%-plus tail as shares: 69 trades, +9.3%, median +3.3%.
   - Other trader stock cores (+0.4% to +0.7% median) are much thinner.
   - The option form multiplies the average about 4 to 5 times and leaves a negative median.
3. **A stock-level edge does not transfer to options unless the stock moves a lot.**
   - Oversold, news ≥ 1, no spike today was a trader's best stock rule (183 trades, +2.0% average, +0.7% median, 5 of 6).
   - As a 30-day 5%-above call with the market gate it scored **-31.7%** (65 trades, 1 of 6).
   - Small bounces do not cover cost plus decay.
4. **Mild strength loses and strong strength wins.**
   - Calls 20d ≥ 1.5, 20d % between 10 and 25, market up, 30-day ATM: -7.6% (151 trades).
   - The same family with iv < 60 and no upper cap on 20d %: +16.9%.
   - The 40%-plus tail of S1 is the best slice (+35.5%).
5. **The market gate stayed intact.** Every trader's call rule included it, and no trader found a case where dropping it helped. It has still not been tested head to head with the gate removed (see section 4).

---

## 1. STRATEGY: SETUPS WORTH TRADING (paper, or small flat size)

Take every signal that passes. Skipping signals loses the few large winners that make the averages.
- Spread premium across many names with flat small size, and never add after wins.
- Size so that a -100% loss on every open position is survivable.
- The rules below overlap heavily because they pick the same trending names. Do not count them as independent confirmations.
- Each trader ran 14 to 18 rule checks, so some lucky results are expected. Prefer results seen across bundles, halves and traders.

### 1A. Tier 1: current scorebook (costs included, expiring contracts excluded)

**S1. Strong-momentum gate, 30-day ATM call**
- Rule: 20d % ≥ 20 and vs ma50 % ≥ 15 and market 20d % > 0 and shares ≥ 1. Buy the 30-day call 0% above the price.
- Result: 138 trades, **+28.4%** (range +0.5% to +68.4%), median -21.5%, 39% winners. Benchmark -11.8%, **6 of 6**. Halves +26.4% and +29.5%.
- Credit: Agent 2's stock gate, converted to an option.

Variants, all scored against the same benchmark:

| Variant | Trades | Average | Range | Median | Beat | Halves |
|---|---|---|---|---|---|---|
| **S1-tail** (20d % ≥ 40, vs ma50 % ≥ 15, market > 0, shares ≥ 1) | 60 | **+35.5%** | -10.7% to +115.5% | **-16.1%** | 4 of 6 | +13.8% / +46.4% |
| **S1-nospike** (S1 without the shares condition, plus days since spike ≥ 1) | 75 | +29.5% | -1.8% to +62.5% | -37.9% | 5 of 6 | +54.6% / +15.4% |
| **S1-flow** (20d % ≥ 20, vs ma50 % ≥ 15, market > 0, call days 2x+ ≥ 1; **30-day 5% above**, benchmark -12.2%) | 155 | +24.5% | -10.0% to +65.3% | -37.9% | 5 of 6 | +27.4% / +22.5% |
| **S1-cap** (20d % ≥ 20, vs ma50 % between 15 and 40, market > 0; no shares condition) | 125 | +13.5% | -8.4% to +36.2% | -31.7% | 6 of 6 | +23.6% / +6.1% |
| **S1 with close vs vwap % ≥ 0.9** (no market gate, no shares condition) | 78 | +19.7% | | -28.4% | 5 of 6 | +33.3% / +10.3% |
| **S1 with shares < 1** (control; no market gate) | 45 | +18.2% | | -41.0% | 3 of 6 | +34.7% / +3.8% |

Reading the variants:
- The shares ≥ 1 condition improves the median and the beat rate. Compare S1 (median -21.5%, 6 of 6) with the thin-volume control (median -41.0%, 3 of 6).
- Capping the trend at 40 did not help. The very extended names carry the average, and halves got worse.
- Call-flow days ≥ 1 does not add anything on top of the trend gate.
- Close vs vwap at the top (≥ 0.9) does not hurt. VWAP is neither a filter nor an exclusion.
- The no-spike-today version is not better than S1 and has a lopsided first half.

**S2. Strong trend plus news, 30-day ATM**
- Rule: vs ma50 % > 11.9 and news 7d ≥ 1.
- Result: 215 trades, **+15.1%** (range -7.2% to +42.0%), median -30.8%, 33% winners. Benchmark -11.8%, 5 of 6. Halves +2.2% and +24.4%.
- Credit: Agent 4. This is the best-sized verified rule with no market gate, and it has a weak first half.

**S3. Sustained call buying with momentum, moderate IV, 30-day ATM**
- Rule: calls 20d ≥ 1.5 and 20d % ≥ 10 and market 20d % > 0 and iv % < 60.
- Result: 123 trades, **+16.9%** (range -7.1% to +42.2%), median -37.1%, 35% winners. Benchmark -11.8%, 4 of 6. Halves +23.0% and +11.8%.
- Credit: Agent 3. Its shares version (same filter, no option) had median only +0.4%.
- At 90-day 5% above: 30 trades, +5.8%, median -18.5%, 3 of 5, halves -13.8% and +15.7%. Too small and unstable.
- Without the iv < 60 gate:
  - Calls 20d between 1.5 and 2.2, 20d % ≥ 10, market > 0: 60 trades, +20.1%, 4 of 6.
  - Adding call days 2x+ ≥ 1 gave 243 trades at -1.6%.
- The IV gate may matter. The "iv ≥ 60 after a surge" control (calls 20d ≥ 1.5, 20d % ≥ 25, iv % ≥ 60, market > 0) scored -3.5% (108 trades), even though it requires a stronger run.
- Very low IV is bad, so this is not simply "lower IV is better" (see section 2).

**S4. Cheap iv/realized with trend and news, 30-day 5% above**
- Rule: iv/realized < 0.75 and news 7d ≥ 1 and 20d % > 0.
- Result: 138 trades, +12.8% (range -18.4% to +50.6%), median -55.6%, 32% winners. Benchmark -12.2%, 4 of 6. Halves +1.8% and +27.5%.
- Credit: Agent 4's option-level idea, partly confirmed. It is a tail-seeking rule with a very negative median.

### 1B. Tier 1 from the previous generation (old scorebook, NOT yet re-scored)

These figures came from the old scorebook, which included contracts that expired inside the hold and so may differ. Restate them to get clean numbers. Some were big and consistent.

- **R1: overbought with sustained call buying, 30-day 5% above.**
  - Rule: rsi > 70 and calls 20d > 2.
  - Old result: 175 trades, +34.0%, median -53.4%, 5 of 6. Halves +62.5% and +15.0%.
  - The call-flow condition adds the edge (control with calls 20d ≤ 2: +1.0%).
  - **R1-$50**: add price over $50 and market 20d % > 0. Old result: 44 trades, **+52.4%**, median -21.5%, 43% winners, 5 of 6, halves +40.9% and +60.4%. Small n, and the range touches zero.
  - **R1b**: the same entries at 30-day ATM with market > 0: 153 trades, +7.8%, halves +27.6% and -2.2%.
  - **R1c**: R1 at 10% above, exit when the option doubles, else after 10 sessions: 147 trades, +6.9%, 6 of 6.
- **R2-OTM: momentum run, 30-day 10% above.** Rule: 20d % > 20 and vs ma50 % > 15. Old result: 211 trades, +26.2%, median -57.4%, 6 of 6. S1 above is the ATM, market-gated, shares-gated version and has a better median.
- **R3: trend, news tone and price.** Rule: vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price over $50. At 30-day 5% above: 143 trades, +23.4%, 4 of 6, halves +23.8% and +23.1%.
- **R4: momentum accumulation.** Rule: calls 20d ≥ 1.5 and 20d % ≥ 10 and vs ma20 % ≥ 5. At 30-day 5% above: 297 trades, +17.8%, 6 of 6.
- **R5: momentum plus news.** Rule: 5d % > 5 and vs ma20 % > 5 and news 3d ≥ 1. At 30-day 5% above: 186 trades, +16.4%, 4 of 6.
- **R6: uptrend in a rising market.** Rule: vs ma50 % > 0 and 20d % > 0 and market 20d % > 0. At 30-day 5% above: 666 trades, +9.1%, 6 of 6, halves +5.1% and +11.3%.
- **R7: regime gate.** Rule: market 20d % > 0 and vs ma50 % > 0 and rsi > 60. At 30-day 5% above: 430 trades, +9.4%, 6 of 6.
- **R8: price, trend and market gate, 30-day ATM.** Rule: price over $50 and vs ma50 % > 0 and market 20d % > 0. Old result: 259 trades, +5.0%, median -25.1%, 6 of 6. Halves -5.1% and +11.3%.
- **R9/R10 (30-day ATM and 30-day 5% above):** 20d % > 20 and vs ma50 % > 10 and rsi > 60 (+5.2%, 205 trades); 20d % ≥ 25 and vs ma20 % ≥ 10 (+9.1%, 209 trades).
- **R11/R12: 90-day 10% above, steadier.**
  - R11: vs ma50 % > 0 and market 20d % > 0: 183 trades, +3.3%, median -16.1%.
  - R12: calls 5d avg > 1 and vs ma50 % > 0 and market 20d % > 0 and price over $50: 42 trades, +7.0%, median -8.0%.

### 1C. 90-day baskets with a positive median (best medians, but unstable)

All use the 90-day call and the "screen". **Screen** means: news 7d ≥ 1 and call days 2x+ ≥ 2 and call days 2x+ ≤ 5 and days since spike ≥ 1.

| Rule | Trades | Average | Median | Winners | Beat | Halves |
|---|---|---|---|---|---|---|
| **Screen, 90-day ATM** (benchmark -8.4%) | 58 | +0.4% (range -11.6% to +12.1%) | **+3.1%** | 53% | 4 of 6 | +7.0% / -6.6% |
| **Screen, 90-day 5% above** (benchmark -7.4%) | 55 | +1.9% (range -16.8% to +19.8%) | **+1.8%** | 51% | 4 of 6 | +15.5% / -17.0% |
| **Slow buying with news, 90-day ATM** (call days 2x+ 20d ≥ 8 and news 7d ≥ 1) | 81 | -1.0% | +1.7% | 51% | 3 of 6 | +4.1% / -5.1% |

- These are the only option baskets with a positive median (and costs included). All three have a second-half collapse and heavy overlap.
- Controls support the news and flow conditions:
  - Call days 2x+ ≤ 1 with news 7d ≥ 1: 127 trades, -8.7%, median -15.9%.
  - News 7d < 1 with call days 2x+ ≥ 2: 125 trades, **-14.1%**, median -22.5%, 1 of 6.
- Other 90-day variants that failed: screen plus iv < 60 (92 trades, -2.4%, median -6.0%, 5 of 6); screen plus shares 5d avg 1.3 to 1.7 (40 trades, -5.5%); screen plus vs ma50 between -13.5 and -2.7 (30 trades, -12.2%).
- Treat these as the best research lead for a positive median, not as a trade rule.

### 1D. Stock-level reference (trader tallies, not option scores)

If the next generation can test stock outcomes, these are the stock-level numbers (hold 10 sessions, benchmark about +0.6%):

| Rule | Trades | Average | Median | Winners | Beat |
|---|---|---|---|---|---|
| S1 gate | 168 | +6.0% | **+1.4%** | 55% | 6 of 6 |
| S1 tail (20d % ≥ 40, trend, market > 0, shares ≥ 1) | 69 | +9.3% | +3.3% | 58% | |
| Oversold (rsi ≤ 35, days since spike > 0, news 7d ≥ 1) | 183 | +2.0% | +0.7% | 56% | 5 of 6 |
| S3 core (calls 20d ≥ 1.5, 20d % ≥ 10, market > 0, iv % < 60) | 130 | +2.3% | +0.4% | 51% | 5 of 6 |
| Screen (news, call days 2 to 5, spike not today) | 299 | +0.8% | -0.1% | 49% | 3 of 6 |

- Only the S1 gate has a stock median meaningfully above zero. Bundle 6's own S1 trades averaged only about +2.7%, so the edge is shrinking.
- The oversold rule shows how stock edges do not become option edges (section 0, item 3).

### 1E. Weak add-ons and leads (not trade-worthy alone)

Old-scorebook items, still unchecked on the new scorebook, are marked (old).
- **News 7d ≥ 1, 30-day 5% above (old):** 1,125 trades, -6.4%, 5 of 6 vs -12.2%. It is steady across halves but still negative. Agent 2 found it lowered the S1 stock median, so test it as an add-on, not a default.
- **Call persistence 3+ with market > 0, 30-day ATM:** 394 trades, -8.9%, 3 of 6 vs -11.8%. A little better than the benchmark.
- **Calls 20d 1.05 to 1.52 with call days 2x+ 2 to 3, 30-day ATM (old):** 159 trades, +0.4%, median -31.3%.
- **Sub-$10 with calls 20d > 10, 30-day 10% above (old):** 47 trades, +39.9%, 3 of 6. A paper-size lottery only. The cost floor and mark quality make it suspect.
- **Oversold with quiet calls, 90-day 5% above (old):** 8 trades, median +13.2%. Too small to act on.

### 1F. Sizing and structure guidance

- **ATM or 5% above for 30-day trades.** ATM has far better medians for the momentum gate than 10% above (-21.5% against -57.4%).
- **Median ranking of structures:**
  - 90-day screens: about 0% to +3%, unstable.
  - 90-day 10% above with trend plus market gate: -8% to -16% (old).
  - 30-day ATM with strong gates (S1 tail, S1): -16% to -22%.
  - 30-day 5% above tail-seekers: -38% to -56%.
- **Never use 14-day expiries.** Hold 10 sessions; no exit rescues a bad entry. Double-or-10 is only validated as R1c (old).
- **Always apply market 20d % > 0 to trend and flow rules, and pair it with stock strength.**
- Costs are already inside these numbers. Real fills may still be somewhat worse.

---

## 2. AVOID

### Confirmed bad by the current scorebook

- **Oversold with news and heavy-ish flow as a call (even with a good stock-level record):** 30-day 5% above, rsi ≤ 35, days since spike > 0, news 7d ≥ 1, market > 0: **-31.7%** (65 trades, 1 of 6, 18% winners). Small bounces do not pay for a call.
- **No short-dated call activity:** short ≤ 0 and news 7d ≥ 1, 30-day 5% above: **-23.2%** (195 trades, median -72.6%, 24% winners, 1 of 6). Names with zero activity in near-dated calls are very bad.
- **Very low IV:** market 20d % > 0, vs ma50 % > 0, news 7d ≥ 1, iv % < 30, 30-day 5% above: **-35.6%** (83 trades, median -64.3%, 1 of 6).
  - A single-bundle read had suggested "low IV is better". The scorebook says no.
  - The likely reason is that cheap options lose a larger share to the cost floor and rarely move far enough.
- **Mild strength:** calls 20d ≥ 1.5, 20d % between 10 and 25, market 20d % > 0, 30-day ATM: -7.6% (151 trades, 28% winners). The same applies to near-high moderate momentum (old: -20.9%).
- **Pullback inside strong call flow:** calls 20d ≥ 1.5, off high % between -16 and -8, market > 0, 30-day ATM: -10.4% (135 trades, 2 of 6).
- **Shares 5d average band 1.25 to 1.7 as an option rule:**
  - With calls 20d ≥ 1.5 and market > 0: -8.2% (138 trades).
  - With news 7d ≥ 1 and shares ≥ 1: -10.6% (171 trades, 30-day ATM).
  - At 90-day ATM: -5.5% (40 trades).
  - A stock-level two-bundle lead does not help a call.
- **Momentum without volume:** the thin-volume (shares < 1) version of S1 has median -41.0% and beat the benchmark in only 3 of 6 bundles. Keep shares ≥ 1.
- **Flow without news at long expiry:** news 7d < 1 with call days 2x+ ≥ 2, 90-day ATM: -14.1%.
- **Low call flow:** call days 2x+ ≤ 1 with news 7d ≥ 1, 90-day ATM: -8.7%.

### Avoid from the previous generation (old scorebook, not re-scored)

- Surge follow-through, overextended fall, oversold with heavy calls (-27% to -30%), and momentum or any call rule when market 20d % < 0 (-11% to -48%).
- Non-extended stocks in an up market (-17.7%).
- Shares today < 1 as a general filter, 30-day 5% above (-18.2%, 868 trades).
- Heavy 20-day calls with no news (-14.6%).
- The $10 to $50 price band (the worst band).
- Stacks of weak stock-level filters (-8% to -15%).
- Ratings of any kind: noise.
- 14-day expiries and 10%-plus out-of-the-money strikes, except the specific R2/R4/R6 uses listed.
- Judging a rule by total dollars, by one trade, or by a median over fewer than 20 trades.
- Trading sub-$10 names for real money.

### Dropped or demoted by the traders' work

- **Vs ma50 or 20d % "top bin is bad".** One bundle showed it. The scorebook says very strong trend wins (S1, S1-tail, S2). This was a single-bundle quantile read, so trust the rule-level scores.
- **Spike yesterday:** the stock rule was flat (+0.1% median, 2 of 6).
- **Close vs vwap as an edge:** neutral.
- **High IV exclusion:** iv % > 85 with news 7d ≥ 1 (30-day 5% above) scored -8.1%, better than its -12.2% benchmark (196 trades, 4 of 6). Do not exclude high IV on this evidence.

---

## 3. WHERE THE TRADERS AGREED AND DISAGREED

**Agreed:**
- The median option trade loses; averages come from a few big winners.
- Ratings are noise.
- No live money in options, flat small size, no adding after wins.
- 14-day expiries and sub-$10 names are bad or untrustworthy.
- The market 20d % > 0 gate (used by Agents 2, 3, and 4's own baseline).
- Call flow on 0 to 1 of the last 5 days is bad.
- News present is better than none.

**Disagreed (scorebook verdict):**
- **Whether to trade stock or options.** Agents 2 and 3 traded stock because option medians are negative.
  - Scorebook: the S1 stock rule has a positive median (+1.4%). The option form has a much higher average and a negative median. These are different risk profiles, not a contradiction.
- **Strong trend.** Agents 2, 3, and 4 doubted the top vs ma50 and 20d % bins after one bundle. The scorebook shows the strong-trend option rules winning (S1, S1-tail, S2). The doubters were wrong at the rule level.
- **Trend cap.** Agent 2 proposed capping the trend at 40. The scorebook says the cap lowers the average from +28.4% to +13.5% and weakens the second half.
- **Call-day thresholds.** Agent 3 suspected ≥ 1 was as good as ≥ 2. Adding ≥ 1 to the strong-momentum gate did not help (S1-flow +24.5% against S1 +28.4%), and ≥ 2 to 5 was confirmed only in the 90-day screen.
- **IV.** Agent 3 gated at iv < 60 and Agent 4 liked iv < 30. The scorebook penalizes iv < 30 heavily and shows no benefit from excluding high IV, so only the loose iv < 60 gate in S3 has any support.
- **90-day.** Agent 1 reported 90-day calls with a positive median. The scorebook confirms +3.1% and +1.8% but with opposite halves.
- **Close vs vwap.** Agent 3 treated vwap ≥ 0.18 as a lead. It never became an option rule, and the extreme-VWAP S1 variant was neutral.

---

## 4. NEW IDEAS TO TEST

State each as an explicit rule so it can be scored. Require n ≥ 60, report both halves, and compare to the benchmark.

1. **S1 at longer expiry (top priority).** Test S1 at 90-day ATM and 90-day 5% above.
   - S1 at 30-day has a negative median (-21.5%), and the only positive medians so far come from 90-day baskets.
   - Success is a positive median with both halves positive.
2. **Strength plus screen at 90 days.** Add vs ma50 % ≥ 15 and 20d % ≥ 20, or just vs ma50 % > 0 and market 20d % > 0, to the screen (news 7d ≥ 1, call days 2x+ 2 to 5, spike not today) at 90-day ATM.
   - This tests whether strong trend repairs the screen's second half.
3. **S1 add-ons.** Test S1 plus each of:
   - price over $50;
   - iv % < 60;
   - news 7d ≥ 1;
   - call days 2x+ ≥ 2;
   - rsi > 60;
   - short ≥ 1 (any near-dated call activity, the opposite of the bad "short ≤ 0" cell).
   - One add-on per rule, at 30-day ATM.
4. **Re-score the previous generation's top rules cleanly.** R1, R1-$50, R3, R4, R6, R7, R8, and R11/R12 (section 1B), now with expiring contracts removed and costs included.
   - Also test widened R1-$50 (rsi > 60 or 65, calls 20d > 1.5, market 5d % > 0, or price over $30) to reach n ≥ 60.
5. **Cost-aware selection.** The cost floor ($0.05 a share) is heavy on cheap premiums.
   - Test S1, S2 and R4 restricted to price over $50, and separately to iv % ≥ 30.
   - Test premium as a share of price, if the scorer exposes it, with a minimum around 3%.
   - Success is a median that improves without the average collapsing.
6. **Strength ladder and the cliff.** Under a market-up gate, bucket by 20d % (0 to 10, 10 to 20, 20 to 40, 40+) at 30-day ATM.
   - Find the threshold and whether the 40+ tail keeps improving.
   - The current evidence is S1-cap (15 to 40) +13.5% against S1-tail (40+) +35.5%.
7. **Cheap iv/realized inside strength baskets.** Test iv/realized < 0.75 inside S1, S2, and R4. The standalone rule (S4) was +12.8%.
8. **Exit variants.** Test the double-or-10 exit on S1 and S1-tail at ATM and 5% above, and a 15 or 20 session hold if the scorer supports it. R1c is the only old double-or-10 result that worked (10% above).
9. **Sustained-flow measures inside strength gates.** Test long calls 20d, otm calls 20d, and call days 2x+ 20d inside S1 and R4.
10. **Market-gate strength.** Test market 20d % > 1 and > 2 against > 0, and a no-market-gate version of S1 and S2 (AB-nm style), so the gate itself has a measured value.
11. **Break-even-aware selection (Agent 4's idea).** Estimate each candidate's break-even stock move from its own premium and IV, and test candidates whose recent 20d % and vol20 exceed it.
12. **Basket simulation.** Equal-premium weekly baskets of all Tier 1 passers (S1, S2, S3, R1, R4, R6): worst week, overlap, and whether the 6-of-6 record survives deduplication.
13. **Sub-$10 lottery, now with costs known.** Test calls 20d > 5, > 10 and > 20 with trend and market gates. The floor means these entries start about 14% or more in the hole.

**Untested and removed (cannot be implemented here):** deep in-the-money calls, bull call spreads, put debit spreads, bear call spreads, and any short selling.

---

## 5. OPEN QUESTIONS

- **Positive median.** Can any call setup have a positive median with stable halves?
  - The candidates are the 90-day screens (+3.1% and +1.8%, but halves +7.0% / -6.6% and +15.5% / -17.0%).
  - S1-tail at 30-day ATM has a median of -16.1% with a +35.5% average.
- **Why do the 90-day screens fade in the second half?** Is it regime, premium level, or a few weeks?
- **Is the cost floor the main reason cheap options lose?** Very low IV (-35.6%), sub-$10, and far out-of-the-money all lose. The $0.05 floor and 5% fee suggest this, but it is not isolated.
- **Does the S1 edge persist?** The new bundle's S1 stock trades averaged only +2.7%. S1's option range barely excludes zero (+0.5%), and tail trades carry the average.
- **Why does mild strength lose while strong strength wins?** Premium cost relative to the move, convexity capture, or the cost floor?
- **Does the market gate generalize?** The sample is up-market-heavy, and no trader saw a sustained decline.
- **Does the stock edge ever matter in options?** The oversold stock rule (+0.7% median) lost 31.7% as an option. Small stock edges seem to need a big move to survive the wrapper.
- **What are the residual -50% to -70% losses on flat stocks?** They may be real decay plus costs and IV drops rather than stale marks. Premium and expiry data in the trade lists could settle this.
- **Does over $50 act as a liquidity, low-IV or cost-floor proxy?** It helped the old R1, R3, and R8 results.

### How the committee would remake the test (not passed on)

# REDESIGN PROPOSAL

## 1. WHAT BLOCKED YOU (ranked)

1. **Too little data, too many hypotheses.** Each bundle has about 250 candidates and there were six bundles, which gives about 3,000 candidates in total. Quintile bins have about 50 names each.
   - Agent 1: "the median carries roughly ±5% noise. Bins that look strong in one bundle often do not repeat."
   - Nearly every bin-level finding flipped sign: vs ma50 top bin, 20d %, iv/realized, ratings, market 5d.
   - The system recorded 14 to 18 rule checks per trader, so lucky rules were expected. There was no held-out data to separate luck from edge.
   - The playbook says the four traders' rules "overlap heavily because they pick the same trending names", so the six agreements are not independent.
2. **One regime.** Agent 1: "Six bundles, mostly rising or mixed markets." The playbook admits "no trader saw a sustained decline". The market gate was never tested head to head and could not be, because there were almost no down-market weeks.
3. **The wrapper hid the signal.** Long calls only, with a round-trip cost of at least 10% of premium, a negative benchmark of -8% to -18%, and a negative median in nearly every cell. Stock edges of +0.7% median became -31.7% as calls. The traders could not tell whether a signal was weak or the wrapper was too costly. The stock results were only traders' own tallies, not scorebook-verified.
4. **Facts about the test were learned late.** Costs, expiry handling and the "-100% on a stock that rose" marks were explained only after a generation of work. Agent 4: "Option results are unreliable until the mark audit closes." Agent 4 also needed "the trade log, not the summary report", and could not report its own rule's bundle 6 row. Agent 1's cited figures differed from the scorebook's.
5. **Feedback was coarse.** Quintile bins with ties ("Bin edges that tie at zero… unreadable") made days-since-spike unusable. Only 3 scored rules per review forced guesswork. Medians were reported without ranges.
6. **Fixed 10-session hold, daily closes, no path.** This blocked tests of exits, of holding 20 to 40 days, and of break-even timing. The traders were also unable to separate gap risk from drift.
7. **Anonymous names and hidden dates.** There was no way to control for earnings, sector, or market cap, or to see what kind of event a "spike" was.

## 2. DATA TO ADD (most useful first)

- **Days to next earnings, and a flag for earnings inside the hold.** This lets us test whether IV-crush and gap risk explain the option losses and the big winners.
- **IV rank/percentile against the stock's own history, plus an IV term structure** (30-day and 90-day IV). Raw IV levels were uninterpretable. Agent 4's "low IV is better" was reversed by the scorebook.
- **Option liquidity at entry:** open interest, option volume, bid-ask spread, and the real costs charged. This lets us test whether the cost floor, rather than the signal, drives losses.
- **Sector or industry code, market cap bucket, and beta.** With these we can compute returns relative to the market and to sector. Right now "strong trend wins" may only be beta in an up market.
- **Market context:** a volatility index level, market breadth, and a regime label. This lets us test the market gate.
- **Realized forward returns at 1, 3, 5, 10, 20 and 40 sessions** for each candidate, for stock and for every option grid cell. This enables hold-period and exit tests without new bundles.
- **Non-candidates.** Add a random sample of the universe that was not flagged, so we can see whether candidate selection itself carries information.

All of this is available from standard daily stock and options data, except bid-ask, which needs end-of-day quotes. Intraday paths are not needed.

## 3. TOOLS AND INSTRUMENTS

- **Shares as a scored instrument**, with costs. The strongest verified edge (S1 as stock, median +1.4%) was only a trader tally.
- **Longer expiries and exits:** 90-day and 180-day calls, and holds of 5, 10, 20 and 40 sessions. Add stop and target exits (double-or-10, trailing stop) as scorable options, since each trader asked for them.
- **Cheaper option structures:** if feasible, in-the-money calls (low time value) and call spreads. They were removed, but a limited-risk, low-cost wrapper is the obvious answer to the cost and decay drag. If still impossible, say so up front.
- **Analysis tools:**
  - A trade-level CSV of every candidate with all columns and outcomes.
  - A sandbox for scoring unlimited rules on training bundles.
  - A break-even-move calculator: the stock move needed to cover premium plus cost.

## 4. CHANGES TO THE TEST ITSELF

1. **Larger, longer, more varied sample.** Use 50 to 100 candidates per week and at least 100 weeks, covering rises, falls, high-volatility and flat regimes.
2. **Locked holdout.** Provide a training set, a validation set, and a final set that is scored once. Rules are frozen before the final scoring.
3. **Unlimited rule checks on training only, with the count of trials reported.** Use a multiple-testing correction. The final scoring applies to at most 3 pre-registered rules.
4. **Score every rule the same way.**
   - n, mean, median, trimmed mean, and win rate.
   - Week-resampled 95% range.
   - Both halves.
   - Within-week comparison against the rest of that week's candidates.
   - Beat rate per bundle.
   - Overlap with other submitted rules.
5. **Give the full environment description on day one:** costs, expiry handling, data limits, and the scorebook's definitions of rules.
6. **Replace quintiles with fixed rule-defined buckets.** Use thresholds chosen in advance, with tied values assigned deterministically.
7. **Score by median and by break-even rate, not only by average.** A rule that only works through a few large winners should be labelled as such.

### Agent 1's final notes (not passed on)

# TRADING NOTES: FINAL (AFTER BUNDLE 6 OF 6)

## 1. MY CURRENT STRATEGY (PAPER ONLY)

No real money. No option structure has passed the gate (a positive median across at least three bundles, with the mark audit closed). The option wrapper stays on paper. Stock-level results decide what I would act on, and after six bundles the stock screen has not shown a reliable median edge.

### 1a. Stock screen (paper, the setup I track)

Entry at the signal close, equal weight, hold 10 sessions, sell at the close. No stop-loss, since none has been tested.

**Gates (all must hold):**

1. **News:** news 7d ≥ 1. Best band is 1 to 2 articles.
2. **Call flow:** call days 2x+ in the last 5 sessions = 2 to 5. Exclude 0 and 1.
3. **No spike today:** days since spike ≥ 1. Confidence is now low-moderate (see 2c).

**Split and ranking variables (not gates):**

- **Shares 5-day average between about 1.3 and 1.7.** Bundle 5 gave +3.3% (66% up) and bundle 6 gave +3.4% (62% up). This is the most consistent new ranking signal. Confidence: low-moderate, two bundles. Use to order candidates or as a test split.
- **Slow buying (call days 2x+ over the last 20 sessions).** Counts of 8 or more were positive in bundles 3, 4 and 6. Counts of 2 to 4 were negative in bundle 5 (3 to 4 days, -3.1%) and bundle 6 (2 to 4 days, -1.8%). Use as a ranking aid, avoiding the 2 to 4 range. Confidence: low-moderate.
- **Overextension (vs ma50).** Test split, not a gate. The band from -13.5% to -2.7% was positive in bundle 6 (+3.6%, 59% up). The top band (above +12%) was positive in bundle 5 (+5.4%) and negative in bundles 1 and 6 (-3.0%, 43% up). Treat the top band as unresolved. Confidence: low.

**Honest status of the screen:** Pooled over 299 screen trades, the average return is +0.8% and the median is -0.1% (49% up). Buying every candidate the same way gave +0.6% average. The screen beat buy-everything on average in only 3 of 6 bundles. It has no reliable median edge, so it is a candidate filter, not a proven rule.

### 1b. Option wrapper (paper, secondary)

- **30-day calls: suspended.** The 30-day at-the-money and 0 to 5% out calls had negative medians in every bundle tested. Bundle 6: 30-day 0% strike, 11 trades, median -52.4%. Bundle 5: 30-day 5% above, 18 trades, median -47.4%.
- **90-day calls: observe only.** Bundle 6 90-day 0% strike: 12 trades, average -3.9%, median -13.6%. Bundle 6 90-day 5% above: 6 trades, average +9.0%, median +9.9%. Bundle 5 90-day calls had positive medians on 7 trades. Pooled screen names at the 0% strike: 58 trades, median +3.1%, average +0.4%, beat buy-everything in 4 of 6 bundles. Its first-half result was +7.0% and its second-half result was -6.6%, so it is unstable. Confidence: low. Not validated.
- **Expiry direction: 90 days is consistently less bad than 30 days.** In bundle 6 the 90-day 0% median (-13.6%) was far better than the 30-day 0% median (-52.4%). This fits time decay. Entry only with at least 60 sessions to expiry.
- **Strike:** at the money or 0 to 5% above. Avoid 10% or more above. Bundle 6 90-day 15% above gave -69.7% on one trade and 90-day 10% above gave +51.3% on one trade. Neither is evidence.
- **Exit:** hold 10 sessions. The double-or-10 exit remains unvalidated (bundle 6's 377.8% winner was a 30-day 0% call on a stock up 82%, one trade).
- **Sizing:** equal, small premium. Assume the premium can go to -100%.
- **Per-trade record:** sessions to expiry at entry and exit, premium as % of price, implied vol at entry, realized vol, stock move, exit mark, mark source, and audit flag.

### 1c. Why the wrapper is the problem

My own bundle 6 trades: 33 trades, average +1.8%, median -16.4%, 36% winners, net +$603. The dollars came from a few large winners. The median was negative, and the 30-day group drove the damage. Stock-level buy-everything was +1.4% average and 0.0% median. Across six bundles the most reliable finding is the gap between stock returns and option returns at the same names. Stock picks have at best a small, unstable edge. Short-dated, out-of-the-money calls turn a flat stock into a loss.

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### 2a. My own trades
- 33 trades, +$603, average +1.8%, median -16.4%, 36% winners.
- 90-day 0%: 12 trades, median -13.6%.
- 30-day 0%: 11 trades, median -52.4%.
- 90-day 5% above: 6 trades, median +9.9%.
- Single-trade groups (90-day 10%, 15%, 20%; 30-day 5%) are anecdotes.

### 2b. Rule checks scored by code (pooled over six bundles)
- **Core screen stock** (news 7d ≥ 1, call days 2x+ 2 to 5, spike not today): 299 trades, average +0.8%, median -0.1%, 49% up. Beat buy-everything in 3 of 6 bundles. **No median edge.**
- **Core screen, 90-day 0% call, hold 10:** 58 trades, average +0.4%, median +3.1%, 53% up. Beat buy-everything in 4 of 6 bundles. Unstable across halves (+7.0% vs -6.6%). **Not validated.**
- **Screen with close vs VWAP above 0:** 154 trades, average +0.3%, median -0.6%, 46% up. Beat buy-everything in 3 of 6 bundles. **Fails.** The bundle 5 finding that VWAP above 0 helped did not survive pooling. Drop as a ranking.

**Pre-commit for bundle 6** (the screen must beat buy-everything on median in bundle 6 and in pooled bundles 5 and 6): **not met on the evidence reported.** The screen's pooled median is -0.1%, and buy-everything's bundle 6 median was 0.0%. The three vs-ma50 and momentum splits I planned were not reported separately for bundle 6. I cannot show a median edge for any split.

### 2c. Quintile bins (bundle 6, all 249 names)

**Flow and news (replicated):**
- **Call days 2x+ (last 5):** 0 to 1 gave -1.4% to -1.6% (37 to 38% up). 1 to 2 gave +4.2% (60% up). 2 to 3 gave 0.0%. 3 to 5 gave +4.3% (64% up). **Exclusion of 0 to 1 held again.**
- **News 7d:** zero news gave -1.8% (32% up). 1 to 2 gave +4.0% (72% up). 2 or more gave +1.7%. **News 1 to 2 is the most stable positive band** (bundle 5: +4.7%, 80% up; bundle 6: +4.0%, 72% up).
- **Shares 5-day average:** 1.33 to 1.72 gave +3.4% (62% up); below 1.1 was negative; above 1.75 was -0.4%. **Replicated in bundles 5 and 6.**
- **Slow buying (call days 2x+ over 20 sessions):** 2 to 4 gave -1.8% (36% up). 4 to 6 gave +3.7% (66% up). 6 to 8 gave -3.1% (38% up). 8 to 13 gave +3.9% (62% up). Non-monotone, but the 2 to 4 range has now been negative in two bundles.

**Spike (not clean):**
- Days since spike 0 appears as two bins in this bundle's labels: one at -9.1% (0% up) and one at +5.3% (86% up). The tie edges make it impossible to tell which bin is which, so this is not usable.
- Days since spike 0 to 3 combined gave +3.7% (60% up). Days since spike 3 to 10 gave +1.7%. 10 to 60 gave -1.1%.
- **The bundle 2 to 5 pattern (spike today is bad) was not confirmed in bundle 6.** Confidence drops to low-moderate.

**Trend and position:**
- **20-session return:** -11.9 to -2.6% gave +3.7% (60% up). Above +13.5% gave -1.8% (42% up). **Conflicts with bundle 5** (strong trend was positive). Dropped as a ranking.
- **vs ma50:** -13.5 to -2.7% gave +3.6% (59% up). Above +11.9% gave -3.0% (43% up). See the unresolved top band in 1a.
- **Close vs VWAP:** the bins are mixed. Positive bins were +2.0% and +1.3% (56% up each), while the top bin (above +0.9%) was -0.7%. Pooled screen result is negative (see 2b).
- **1-day return:** 1.2 to 3.6% gave +1.5% (56% up). Above 3.7% gave -2.4% (42% up). Down days were flat, not bad. Bundle 5 said the opposite on down days. Not a rule.
- **5-day return:** -6.5 to -2.3% gave +2.5% (56% up). Otherwise flat.
- **RSI:** above 68 gave +1.9% (56% up); 56 to 68 gave -1.0%. Non-monotone. Not used.
- **Off-high:** -16 to -7.8% gave +3.9% (59% up). Other bins flat or negative. Not monotone. Not used.

**Option and volatility:**
- **IV/realized (stock-level):** the top band (above 1.23) was -0.5% to -1.1%. **The bundle 5 reversal reading (top band positive) did not hold.** Dropped as a signal.
- **IV (30-day at-the-money call, 30-day hold):** 61.5 to 84 gave -11% average, -32% median. Above 85 gave -25% average, -70% median. Above 86 on the stock side gave -5.4% (40% up). Expensive options continue to show poor outcomes.
- **Puts 5-day average:** 2.6 to 5.5 gave +3.6% (60% up). One bundle; not used.

**Market:** market 5d between 0.6 and 1.5% gave +2.8% (60% up); market 20d between 1.5 and 2.6% gave +2.8% (62% up). Conflicts with bundles 4 and 5. Not used.

### 2d. Option structure (bundle 6)
- **30-day at-the-money call, hold 10, by implied volatility:** every band had a negative median. Lowest IV band (7 to 30) gave avg +14%, median -27%.
- **By implied/realized ratio:** 0.13 to 0.75 gave avg +44%, median -30%. Every other band had a negative median (-25% to -46%).
- No option band passed the median gate.

### 2e. Mark audit: still open
- Bundle 6 rows with flat-to-down stocks and 11 to 19 sessions to expiry were marked -74% to -83%. Rough model checks suggest some of these may be harsher than a simple time-value model. Example: 19 sessions, implied vol 45%, stock -2.6%, premium 4.8%, recorded mark -74%. A simple model gives roughly -55% to -65%. This is a rough check, not an audit.
- No bundle 6 row hit the -90% flag (stock flat or up more than 2%).
- The bundle 5 flagged rows (including the -100% on a 23-session trade and the +200% single trade) remain unchecked.
- **Audit procedure (required before any option ranking):**
  1. Recompute each mark with a standard model using entry and exit stock prices, strike, sessions to expiry, entry implied vol, and realized vol.
  2. Flag any mark more than 20 percentage points from the model.
  3. Flag any mark of -90% or worse where the stock is flat or up more than 2%.
  4. Re-score bundles 2 to 6 with flagged marks corrected or removed, and report both versions.

### 2f. Ratings (for the record)
- Bundle 6 rated +1: 23 names, median +1.7%. Rated +0: 84 names, median -1.0%. Rated -1: 133 names, median +0.4%. Rated -2: 9 names, median +4.9%.
- The extremes ran in the right direction in bundle 6, but the sample is small and the middle bands were not monotone. Ratings were noise in bundles 1 to 5. Not used. This is a watch item only.

## 3. WHAT I WILL TRY NEXT

No further bundles are scheduled in this series. If more data arrives, the following tests are in priority order.

1. **Freeze the stock screen** (news 7d ≥ 1, call days 2x+ = 2 to 5, spike not today). Report median, average, win rate and sample against buy-everything on the same names, with the pooled and per-bundle results.
2. **Test the shares 5-day average band (about 1.3 to 1.7)** as a split inside the screen against the rest of the screen names. This is the one new idea with two bundles of agreement.
3. **Test vs ma50 bands inside the screen:** between -1 and +4, above +4, and buy-everything, all on identical names. Expect the answer to decide whether the top band is a separate regime.
4. **Re-test the spike-today exclusion cleanly:** spike today vs spike 1 session ago vs spike 2 to 9 sessions ago vs none in 60 sessions, inside the screen and unconditionally, with bins that do not tie at zero. Drop the exclusion if it does not hold.
5. **Option wrapper, reduced:** 90-day calls only, at the money or 5% above, at least 60 sessions to expiry, on screen names. Compare 30-day and 90-day on the same names in the same bundle. Every row carries audit tags. Option conclusions stay provisional until the audit closes.
6. **Close the mark audit** (section 2e) before any option review.
7. **Keep ratings out. Keep paper trading.**

## 4. SUPPORTING EVIDENCE AND IDEAS I HAVE DROPPED

### Confidence summary (final)

| Rule or finding | Evidence | Confidence |
|---|---|---|
| Call days 2x+ (last 5) = 2 to 5; exclude 0 to 1 | Best or near-best in bundles 1, 3, 4, 5, 6. Bundle 6: 0 to 1 at -1.4% to -1.6%, 3 to 5 at +4.3% | Moderate |
| News 7d ≥ 1, best at 1 to 2 | Positive in bundles 3, 4, 5, 6 (bundle 6: 1 to 2 at +4.0%, 72% up; zero news -1.8%) | Moderate |
| Shares 5-day average about 1.3 to 1.7 | Bundle 5 +3.3% (66% up), bundle 6 +3.4% (62% up) | Low-moderate (two bundles) |
| Core screen (news, flow, no spike today) | Pooled median -0.1%; beat buy-everything on average in 3 of 6 bundles | Low. No median edge proven |
| Spike today excluded | Negative in bundles 2 to 5; not confirmed in bundle 6 (bin labels ambiguous) | Low-moderate |
| Slow buying: 8+ days in 20 positive; 2 to 4 negative | Bundles 3, 4, 6 (8+); bundles 5, 6 (2 to 4) | Low-moderate; ranking aid |
| Vs ma50 between -13.5% and -2.7% positive | Bundle 6 only (+3.6%, 59% up) | Low; test |
| Vs ma50 above +12% | Bundle 5 +5.4%; bundles 1 and 6 negative | Unresolved; test |
| Close vs VWAP above 0 inside the screen | Pooled 154 trades, median -0.6%; bundle 5 positive | Dropped (failed pooled check) |
| 20-session return as a ranking | Bundle 5 positive; bundle 6 reversed | Dropped |
| IV/realized as a signal | Bundle 5 top band positive; bundle 6 negative | Dropped |
| 30-day calls, 0% to 5% out, hold 10 | Negative median in every bundle tested (bundle 6 0%: -52.4%; bundle 5 5%: -47.4%) | Strong evidence against |
| 90-day calls, 0% to 5% out | Bundle 5 positive; bundle 6 0% median -13.6%, 5% median +9.9%; pooled 58 trades, median +3.1% but unstable halves | Low; observe |
| 90-day vs 30-day expiry | 90-day consistently less negative in bundle 6 (median -13.6% vs -52.4%) | Moderate on direction; magnitude small-sample |
| Double-or-10 exit | One real trade in bundle 5 and one in bundle 6; negative medians in bundles 3 and 4 | Not validated |
| Ratings of any kind | Bundle 6 extremes ran right; middle bands not monotone; noise in bundles 1 to 5 | Not used; watch |

### Demoted or dropped
- **Close vs VWAP above 0 as a ranking:** pooled screen result negative (median -0.6%). Dropped.
- **20-session return as a ranking:** bundle 5 and bundle 6 disagree. Dropped.
- **IV/realized as a signal:** the bundle 5 reversal did not hold in bundle 6. Dropped.
- **Short-term reversal (names down 2% to 5% over 5 sessions):** flat or negative in bundle 5. Dropped.
- **Market 5d and 20d as filters:** flipped between bundles. Not used.
- **Calls 5-day average as a ranking:** reversed between bundles 3 and 4. Dropped.
- **Implied vol as a gate or ranking:** no monotone pattern for stocks; the option-level IV pattern is negative at high IV but not a tradable rule. Dropped.
- **Off-high, RSI and 1-day-return bands:** non-monotone across bundles. Not used.
- **Zero-news names as a short signal:** not supported. Excluded from the screen, not shorted.
- **Sub-$10 names:** unreliable marks and large tail moves. Excluded.
- **14-day expiries:** avoid.
- **Calls 1 to 2 days 2x+ as a standalone positive:** weak in bundles 2 and 4. Only the 1 to 2 band of the 5-day count is positive in bundle 6, so do not use it alone.
- **30-day options (any strike), double-or-10 exit:** suspended.

### Caveats
- Six bundles, mostly rising or mixed markets. Regime risk is high. Market-level patterns flipped between bundles.
- Each quintile holds about 50 names, so the median carries roughly ±5% noise. Bins that look strong in one bundle often do not repeat.
- Bin edges that tie at zero (as in the days-since-spike bins here) make some bins unreadable.
- Stock-level effects are real in averages but thin in medians. Most names do not beat buy-everything. A few large winners carry the average.
- Option results are unreliable until the mark audit closes. The wrapper problem persists regardless of marking errors.
- Bid-ask spreads and fill quality are not in these numbers. Real option results would be worse, and stock results somewhat worse.
- Many cells have fewer than 10 trades. Do not act on them.

(Recorded by the system: this trader ran 18 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)

### Agent 2's final notes (not passed on)

# TRADING NOTES: v6 (after bundles 1 to 6)

## 1. MY CURRENT STRATEGY

### 1a. Traded rule: stock-level strength gate (R2)

Buy the stock itself, long, at the entry-day close, when all four conditions hold:

- **20d % ≥ 20**
- **vs ma50 % ≥ 15**
- **market 20d % > 0**
- **shares ≥ 1** (share volume today ÷ its 20-session median)

**Universe:** price ≥ $10. Sub-$10 names are paper only.
**Instrument:** the stock. No options.
**Exit:** at the close 10 sessions after entry. No stop-loss, no early profit-taking, no exits to rescue or accelerate a trade.
**Size:** flat and small. Do not add after wins or losses. No single position should be large enough to decide the result.

**Evidence (code-scored, all six bundles, about 3,000 candidates):**
- **168 trades**, average **+6.0%**, median **+1.4%**, 55% winners.
- 95% range of the average (resampling whole weeks): about +1.7% to +10.7%.
- Every-candidate benchmark over the same period: +0.6% average. The gate beat it in **6 of 6 bundles**.
- Positive in both halves of the sample (first half of months +6.9%, second half +5.6%).
- Bundle 6 alone added about 33 trades. Derived from the cumulative totals, they averaged roughly **+2.7%**. Weaker than earlier bundles, but still positive. The median cannot be derived.

**What the gate is, structurally:**
- **The trend condition (vs ma50 ≥ 15) supplies the median.** The 20-to-40 band with trend and shares ≥ 1 is about 99 trades, with an implied average near +3.7%. Its median is not reported, and the second half was weak in earlier bundles.
- **The 40-and-above tail supplies the average.** The tail (20d ≥ 40, vs ma50 ≥ 15, market positive, shares ≥ 1) has **69 trades, average +9.3%, median +3.3%, 58% winners**. This is the first time the tail median has been reported. It is positive, though the average is still driven by large winners (95% range +2.5% to +18.9%). The newest tail trades were roughly flat by derivation, but the rounding in earlier implied figures makes that noisy.
- **Market condition:** the arm test in bundle 5 favored keeping it (removed trades averaged about -3.6%). Keep it.

**Confidence:**
- High that the gate beats buying everything (6 of 6 bundles).
- Moderate that the trend condition supplies the median.
- Moderate that the tail median is positive (69 trades, +3.3%).
- Low on the size of the edge. The median is about +1.4% to +2%, and the average depends on the tail.

### 1b. Conditions dropped
- **News 7d ≥ 1 as an add-on:** lowered the median. Dropped.
- **News articles as a bin signal:** sign flips across bundles. Dropped.
- **Spike yesterday (days since spike = 1) inside the trend gate:** Bundle 6 scored 23 trades, average +2.4%, **median +0.3%**, beat the benchmark in only 3 of 6 bundles. The earlier bin signal did not survive as a condition. Dropped.

### 1c. Ratings: not an input
- Bundle 6 by rating: +2 median -9.1% (4 stocks), +1 median -0.5% (45), 0 median -0.1% (102), -1 median +0.5% (90), -2 median +2.1% (8).
- Bundle 5 showed +2 at a high median; bundle 6 showed it negative. Across six bundles the ordering has reversed repeatedly.
- Keep the raw columns. Do not use ratings to select trades.

### 1d. Options: paper comparator only, paused

I do not trade options. The option marks are not reliable enough to set policy, and the option medians remain negative.

- **Bundle 6:** 35 trades, average **+5.0%**, median **-21.6%**, 37% winners. The average again came from a few very large call winners (one 30-day call 10% above the price returned +221% on two trades). The median was negative.
- **Bundle 5:** median -4.6% (best average so far, still a negative median).
- **Bundles 1 to 4:** medians -41.7% to -75%.
- Option bins in bundle 6: the lowest implied-vol band (7 to 30) had median -27%, and the highest (86 to 224) had median -70%. No implied-vol band had a positive median.

**Mark problems (persist, and now confirmed by the premium check):**
- Two bundle-6 losses fail the premium sanity check. One 30-day call lost -75% with the stock down only 0.5%, which breaks the rule against losses beyond -60% when the stock fell less than 3%. Another lost -88% with implied vol of 108% and a premium of 5.7% of price, below half the expected at-the-money value of about 13%.
- Several other large losses (-82.5% and -77.6%) came on modest stock moves (-6% and -4%). These look too large but do not trip the strict rules.
- Some large gains are plausible (+463% on a stock up 82%), but the same mark system produces both, so individual option outcomes are not trustworthy.

**Premium sanity check (apply to every option mark):** an at-the-money call's premium is roughly 0.4 × implied vol × √(sessions to expiry ÷ 252) as a share of the stock price. Flag any trade where the recorded premium is below half of that value, any loss beyond -60% when the stock fell less than 3%, or any -100% when the stock rose during the hold.

**Confidence:** high that the option median has not been positive. Low that any recorded option return is accurate.

---

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

### 2a. Gate and its splits
- **Gate (cumulative, six bundles):** positive, beat the benchmark in 6 of 6 bundles. Bundle 6's own trades averaged roughly +2.7% (derived), so the edge is smaller in the newest sample but did not turn negative.
- **Tail (40 and above, with trend):** median +3.3% over 69 trades. Positive on median for the first time with a reported figure.
- **Spike-yesterday add-on:** median +0.3%, beat the benchmark in 3 of 6 bundles. Not adopted.

### 2b. Bin-level observations (250 candidates, median 10-session return)

**Supporting the gate's structure:**
- **Shares 5d avg 1.33 to 1.72:** +3.4%, 62% up. **0.91 to 1.08:** -0.8%. Consistent with shares ≥ 1 as a filter.
- **Call days 2x+ in last 5 sessions, 1 or more:** +4.2% (1 to 2), +4.3% (3 to 5), 60% to 64% up. **0 or 1:** -1.6% to -1.4%. Positive for 1 or more, the same direction as bundle 5.
- **Close vs VWAP:** middle bins were positive (+1.3% to +2.0%) but the top bin (0.9 and above) was -0.7%. The bundle-5 signal that favored buyers paying up into the close did not replicate cleanly.

**Contradicted this bundle:**
- **vs ma50 % 11.9 to 85.5:** **-3.0% median, 43% up.** In bundle 5 this top trend bin was the strongest (+5.4%). Pooled across bundles the trend condition still holds at the gate level, but the top bin is unstable. Watch it.
- **20d % 13.5 to 124:** -1.8% median, 42% up. Same top-bin weakness as vs ma50. Bundle 5 showed the reverse. This is the clearest reason not to trust bin-level top-tail results on single bundles.
- **vs ma20 % top bin:** -0.9%. Not consistent with bundle 5 (+1.6%).
- **Market 20d %:** no clean ordering (bins ranged from +2.8% to -1.1%).

**Weak, non-monotone, or noise:**
- **Spike today (days since spike = 0):** very mixed (-9.1% in one bin, +5.3% in a tied bin). Ties at integers make this unreliable. Bundle 5 showed a negative spike-today bin, but bundle 6 does not confirm it cleanly.
- **Days since spike 3 to 10:** +1.7%. Not separately tested.
- **Off high %, RSI, news, IV bins, implied/realized ratio:** noise or sign flips.

### 2c. Universe
All 249 candidates in bundle 6: average +1.4%, median 0.0%. The gate is a selection tool, not a market call. The gate's bundle-6 trades earned more than the universe, but a smaller margin than the cumulative figures suggest.

### 2d. Ideas that did not survive
- **Spike-yesterday as a gate condition** (median +0.3% in trend, 3 of 6 bundles).
- **Ratings** (reversed ordering across bundles).
- **Call-buying over 20 sessions** (non-monotone).
- **Calls 20d bins** (non-monotone).
- **Close vs VWAP as a gate add-on:** not adopted. Its bin pattern did not replicate cleanly, and the arm was not scored by code this bundle.
- **Options on any gate or universe:** median still negative in all six bundles.

---

## 3. WHAT I WILL TRY NEXT

1. **Score R2 as written on the next bundle.** Target at least 30 gate trades. Report average, median, win rate, both halves of the sample, the every-candidate benchmark, and the tail median (40-and-above with trend) separately from the 20-to-40 band.

2. **Test a trend cap, not a trend penalty.** Bundle 6's top trend bin (vs ma50 ≥ 12) had a negative median, while bundle 5's was positive. Compare the gate against an arm that requires vs ma50 between 15 and 40. Adopt the cap only if it beats plain R2 on median across two bundles and does not cut trades below about half.

3. **Close-vs-VWAP add-on arm (retest).** Gate plus close vs vwap % ≥ 0.18. Adopt only if it beats plain R2 on median in the next bundle and keeps at least half the trades. Bundle 6's top-bin result argues against it.

4. **Spike-today exclusion arm.** Gate, excluding names with days since spike = 0. Report the spike-today cell as a control. Bin edges are tied at integers, so check raw values before trusting it.

5. **Call-buying arm.** Gate plus call days 2x+ in the last 5 sessions ≥ 1. Drop the 20-session version. This has been positive in two consecutive bundles.

6. **Trend split, reported every bundle.** 20-to-40 with trend and 40-and-above with trend, each with its average, median, and win rate.

7. **Options: keep paused.** Restart only after the mark audit:
   - Gate names only, at least 10 per bundle.
   - Arms: the 30-day call 5% above the price, the at-the-money 30-day call, and the stock.
   - Record sessions to expiry and premium as % of price at entry.
   - Apply the premium sanity check to every trade. Report medians with and without flagged trades. Bundle 6 had at least two flagged trades (a -75% loss on a -0.5% stock move, and a -88% loss with a premium below half of expected).
   - No option conclusion until the flagged share is small and the unflagged median is clearly separated from the stock arm.

8. **Keep the hold rule.** Exit after 10 sessions at the close. No exceptions.

9. **Keep ignoring ratings.**

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Evidence I carry forward
- **R2 gate (stock only):** High that it beats buying everything (6 of 6 bundles). Moderate that its median is positive (+1.4%, 168 trades). Low on the size of the edge. Bundle 6's trades were weaker than the cumulative average.
- **Trend condition (vs ma50 ≥ 15) as the source of the median:** Moderate. The top trend bin reversed in bundle 6, so the condition is kept at the gate level and its extremes are under test.
- **40-and-above tail (with trend):** Moderate-positive. Median +3.3% over 69 trades; average +9.3%, with a wide range.
- **Market condition:** Moderate. The arm test favored keeping it. Stock-level bins are mixed.
- **Shares ≥ 1:** Moderate. The 1.33-to-1.72 bin was positive in bundle 6, and the 0.91-to-1.08 bin was negative. Consistent with earlier bundles.
- **Call buying (1 or more call-heavy days in the last 5 sessions):** Low to moderate. Positive in bundles 5 and 6.
- **Spike yesterday:** Dropped as a condition.
- **Close vs VWAP:** Low. Not adopted.
- **Options have not shown a positive median:** High confidence in the direction. Mark quality is poor, so the size is uncertain.
- **Ratings have no predictive ordering:** High confidence across six bundles.

### Ideas dropped or downgraded
- **News 7d ≥ 1 as a condition:** Dropped. Lowered the median.
- **News articles as a bin signal:** Dropped. Sign flips.
- **Spike yesterday in trend:** Dropped. Median +0.3%, 3 of 6 bundles beat the benchmark.
- **Call-buying over 20 sessions:** Dropped. Non-monotone.
- **Calls 20d bins:** Dropped. Non-monotone.
- **"Extended vs ma50 is bad" as a penalty:** Dropped as a bin rule. Trend is kept as a gate requirement. A cap is under test.
- **Ratings as an input:** Dropped.
- **Option structures on the full universe (no gate):** Dropped.
- **14-day expiries:** Dropped.
- **Sub-$10 lottery structures:** Paper only. Marks suspect.
- **Exits to rescue a losing trade:** Not allowed.
- **Lowering or removing the $10 floor:** Not tested. Keep.

### Overall confidence
**Moderate on the direction, low on the size.** The stock-level gate is the one result I trust enough to trade, in the flat, small, stock-only form in section 1a. It beat the every-candidate benchmark in all six bundles and has a positive median over 168 trades. The 40-and-above tail now has a positive reported median, and the bundle-6 trades were positive but smaller than earlier ones. The top trend bin reversed this bundle, which is a reason to test a cap rather than assume the trend story is complete. The option results remain negative on median, and their marks are still internally inconsistent. The next bundle must answer three questions: whether a trend cap improves the median, whether call-buying on 1 or more days adds to the gate, and whether the gate's edge holds up in a fresh sample without the strongest tail winners.

(Recorded by the system: this trader ran 18 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)

### Agent 3's final notes (not passed on)

# Trading Notes: End of Generation 2 (after bundle 6 of 6)

## 1. Current strategy

### 1a. Summary
I trade one stock-level rule with real money: buy shares when a name shows sustained call buying during a rising market, and sell after 10 sessions. Options stay on paper. Bundle 6 did not change that. The option wrapper's paper results are mixed, and no option structure has shown a stable positive median across bundles.

### 1b. Real-money entry rule (shares only, all must hold on the entry-day close)
- **calls 20d ≥ 1.5** (sustained call buying over 20 sessions, not a single spike)
- **20d % ≥ 10** (the stock is up at least 10% over 20 sessions)
- **market 20d % > 0** (the S&P 500 fund is up over 20 sessions)
- **iv % < 60** (the ~30-day at-the-money call implies a moderate move; names with no IV reading are excluded)

Take every name that passes. No discretionary picks, no ratings input.

**Not in the real-money rule:** call days 2x+ (5d), close vs vwap %, shares 5d avg, shares ≥ 1, vs ma20 % ≥ 5. These are tags or paper tests until they pass the tests in section 3.

### 1c. Exit and sizing
- **Hold 10 sessions.** Exit at the 10th session close. No stops, no adjustments, no early exits.
- **Size:** the same small dollar amount on every signal. No adding after wins, no sizing up on chart quality.
- **Sizing stays fixed.** Do not size up until the stock core shows at least 30 trades in each of two consecutive bundles, beats the benchmark in both, and keeps a median no worse than -2%. The paper option profit this bundle (+$28,729) does not count toward this test.

### 1d. Standing exclusions (real money)
- **Market 20d % ≤ 0.** No signals. Every call-buying rule has lost in these regimes.
- **Sub-$10 names.** Paper only.
- **Shares < 1** on the entry day.
- **IV ≥ 60.** Bundle 6's IV bins support this (see 2e).
- **Oversold (RSI < 30).** Failed in bundles 4 and 5. Excluded.
- **Ratings as a gate.** Dropped. Ratings have flipped pattern every bundle.
- **Double-or-10 exits, 14-day expiries, strikes 10%+ above price, discretionary option picks.** Out.

### 1e. Paper measurement (not a trading decision)
- On every name that passes the entry rule, log a 30-day call at 0%, 5%, and 10% above the price, plus a 90-day 5% call, held 10 sessions. Only trades with at least 20 sessions to expiry count in the averages.
- Record premium as a percent of price, IV, iv/realized, and the stock's 10-session return on every trade.

### 1f. Why the stock core and not options
- Stock outcomes depend on whether the stock moves. Option outcomes depend on whether the stock moves by more than the premium, and in a short window that is a narrow band. Across the bundle 6 universe, the 30-day at-the-money call had a negative median in every IV band and every iv/realized band.
- The option paper results are driven by a handful of large winners. Bundle 6's 50 trades averaged +57.5% with a -1.3% median and 48% winners. The median is what matters for a repeatable rule.

### 1g. Confidence
- **Stock core: low to moderate.** Cumulative across six bundles, the core without the call-day filter has 130 trades, average +2.3%, median +0.4%, 51% winners. Its 95% range (resampled by week) is +0.2% to +4.5%, which excludes zero. It beat the all-candidate benchmark in 5 of 6 bundles. The median is thin, and the top 20-day bin was negative in bundle 6 (see 2e).
- **Option wrapper: very low for real money.** The 30-day at-the-money call is the closest structure to a pass (see 2a), but it has about 20 to 29 trades, not 30 or more, and its positive medians have not replicated.

---

## 2. What I tested in bundle 6 and how it went

### 2a. Paper option trades (bundle 6)
- **Total:** 50 trades, +$28,729. Average +57.5%, median -1.3%, 48% winners.
- **30-day 0% (at the money), hold 10:** 20 trades, average +38.8%, **median +11.6%**. The first option structure with a positive median over 20+ trades in any bundle. Bundle 5's 30-day 0% group (9 trades) had a median of -14%. Across the two bundles that is about 29 trades with mixed medians.
- **30-day 5%, hold 10:** 8 trades, average +181.8%, median +175.6%. This same structure had medians of +37.5% (bundle 3), -39% (bundle 4), and -41% (bundle 5). It has not replicated.
- **30-day 10%, hold 10:** 7 trades, average +64.8%, median -71%. Negative median, large average from a few winners.
- **90-day structures and others:** 3 trades each for 90-day 0% (median +65%) and 90-day 10% (median -0.1%), and single trades elsewhere. Too small to read.
- **What the winners had:** stocks up 6% to 82% over the hold, often after 20-day gains of 20% to 125%, with rising call volume and options priced at 0.3% to 17.5% of the stock price.
- **What the losers had:** stocks flat, down, or up only briefly, with the option expiring near -70% to -100%.
- **Option-wrapper verdict:** the 30-day 0% structure is the best candidate wrapper so far, but it has not reached 30 trades, and its positive median came in one bundle after a negative one. Keep it on paper.

### 2b. Universe and ratings
- All 249 candidates: average +1.4%, median 0.0%. Benchmark for the bundle.
- **Ratings:** +2 averaged -2.1% (5 stocks, median -4.0%). +1 averaged +4.0% (48, median +2.5%). +0 averaged +1.8% (103, median -0.3%). -1 averaged -1.1% (80, median -2.2%). -2 averaged +6.0% (13, median +6.7%).
- The rating pattern flipped again. Over four bundles, +1 and -2 have been the best groups at different times, and -1 has been weak in most. Ratings stay paper-only.

### 2c. Rule checks (cumulative across all six bundles)
- **Core without call-day filter** (calls 20d ≥ 1.5, 20d % ≥ 10, market 20d % > 0, IV < 60): **130 trades, average +2.3%, median +0.4%, 51% winners.** Beat the benchmark (+0.6% cumulative) in 5 of 6 bundles. First half of months +2.7%, second half +2.1%.
- **Core plus close vs vwap % ≥ 0.18:** **55 trades, average +3.1%, median +1.3%, 56% winners.** Beat the benchmark in only 3 of 6 bundles. First half +3.7%, second half +2.8%. The median improvement is real in the cumulative data, but the benchmark-beat rate is lower than the core's.
- **Call-day filter (call days 2x+ ≥ 2) inside the core:** the earlier filtered version (66 trades) averaged +3.2% with a +0.4% median. Against the unfiltered core (+2.3%, +0.4%), the filter adds to the average and ties on the median. The pre-registered pass rule needed both to improve, so **it fails on the median.**

### 2d. Pre-registered tests from bundle 5's notes
1. **Full stock rule (core + shares ≥ 1 + vs ma20 ≥ 5):** not scored in this bundle's report. Still unscored. Not adopted.
2. **Call-day filter, same names:** fails on median (tie at +0.4%). Stays a tag.
3. **Close vs vwap ≥ 0.18:** cumulative results favor adding it, but the bundle 6 quintiles are mixed (see 2e), and the bundle-6-only score was not reported. **Not scored as a pass. Carried forward.**
4. **Shares 5d avg (1.25 to 1.6):** not scored against the core. Bundle 6's quintile for shares 5d avg (1.33 to 1.72) was +3.4% median, 62% up. Second positive bundle. Promoted to a test (section 3).
5. **IV gate complement:** not scored rule-by-rule. Bundle 6's IV bins are consistent with the gate (see 2e). Partial support.
6. **Days-since-spike recheck:** **unresolved.** The day-0 quintile edges collapse, so one bin reads -9.1% (0% up) and another reads +5.3% (86% up). The binning cannot separate day 0 from day 1. Needs a rule-based split, not quintiles.
7. **Wrapper logging:** the 30-day at-the-money call reached 20 trades with a +11.6% median. Pass rule needs 30 trades. **Not met, closest yet.**
8. **Hold-period test:** not run.
9. **Market gate:** holds. No exceptions in any rule check.

### 2e. Stock-level reads (bundle 6, median 10-session return, % up)
**Replications (same sign as earlier bundles):**
- **Call days 2x+ (5d):** 1 to 2 days +4.2% (60% up); 3 to 5 days +4.3% (64% up); 0 days -1.6% (37% up). Third bundle with 1 or more call days positive and zero days negative. **However, the 2 to 3 bin was 0.0%,** so the ≥ 2 threshold in the core is not clearly better than ≥ 1. Open question.
- **Shares 5d avg (1.33 to 1.72):** +3.4%, 62% up. Second bundle positive (bundle 5 bin 1.25 to 1.6: +3.3%).
- **IV bins:** below 60 is positive in the quintiles (+0.8%, -0.3%, +1.2%). The 61.8 to 85.9 bin is -0.2% and 86.5 and up is -5.4% (40% up). Supports the IV < 60 gate.
- **Calls 20d:** 1.17 to 1.68 was +2.9% (66% up); 1.69 to 2.66 was -2.8% (39% up). Bundle 5 showed the same shape (1.49 to 2.15 positive, 2.21 to 4.99 negative). **Two bundles, same shape.** The ≥ 1.5 floor sits in the positive region, and the bins above about 1.7 to 2.2 have been weaker. Possible cap test (section 3).

**Failures and weakening signals:**
- **20d % top bin (13.5 to 124):** -1.8%, 42% up. Bundle 5's top bin was +2.7%. The 20d % ≥ 10 condition includes this bin. Concern: the strongest 20-day runs have not been rewarded in one of two bundles.
- **Close vs vwap:** the bins at 0.23 to 0.86 (+1.3%, 56% up) and -0.09 to 0.22 (+2.0%, 56% up) were positive, but the top bin (0.9 to 5.6) was -0.7% (48% up). Bundle 5's top bins were the strongest. The threshold is positive, but the top end is not.
- **vs ma50 % top bin (11.9 to 85.5):** -3.0%, 43% up. Bundle 5 was +5.4%. **Sign flipped. Dropped.**
- **iv/realized top band (1.67 to 4.05):** -0.5%, 50% up. The 1.23 to 1.64 band was -1.1%, 44% up. Bundles 4 and 5 were positive. **Sign flipped. Dropped.**
- **News tone 7d (0.2 to 0.4):** -3.5%, 30% up. Bundles 4 and 5 were positive in the 0 to 0.3 range. **Mixed. Not a gate.**
- **Call days 2x+ (0 days):** -1.6%, 37% up. Consistent with bundle 5.

**New reads (one bundle, watch):**
- **Off-high (-16% to -7.8% from the 60-session high):** +3.9%, 59% up. Pullbacks inside an uptrend.
- **RSI 68 to 89:** +1.9%, 56% up. Bundle 5's 68 to 95 bin was +0.9%. Two bundles positive. Not a gate, since the core already selects strong names.

### 2f. Ideas I tried and what they showed
- **Close vs vwap ≥ 0.18:** Cumulatively adds to the core on average (+0.8 points) and median (+0.9 points), with 55 trades. But beats the benchmark in only 3 of 6 bundles. Bundle 6's quintiles are mixed. Lead, not a gate.
- **Option wrapper at 30-day 0%:** the best paper structure with 20 trades in bundle 6. Not replicated in bundle 5 at the median.
- **Universe-wide ATM 30-day call:** median negative in every IV band (-18% to -70%) and every iv/realized band (-25% to -46%) except the lowest iv/realized band's average. The positive trade median is a feature of the entry names, and n is small.

---

## 3. What I will try next (bundle 7 onward, each with a pass rule)

1. **Call-day threshold, same names.** Score the core with call days 2x+ ≥ 1 against the core with ≥ 2 (and the no-filter core).
   - *Pass:* the ≥ 1 version beats both the ≥ 2 and no-filter versions on average and median, with at least 20 trades.
   - *Fail:* keep the no-filter core as the real-money rule. Drop the call-day filter.

2. **Calls 20d cap.** Score the core with calls 20d between 1.5 and 2.2 against the core with no cap.
   - *Pass:* the capped version beats the uncapped core on average and median, with at least 30 trades, in bundle 7 alone.
   - *Fail:* drop the cap. Keep ≥ 1.5 as the floor.

3. **20d % upper bound.** Score the core with 20d % between 10 and 25 against the core with 20d % above 25.
   - *Pass:* the 10-to-25 band beats the above-25 band on average and median in bundle 7.
   - *Fail:* keep 20d % ≥ 10 with no cap.

4. **Close vs vwap ≥ 0.18, bundle-only score.** Score it inside the core on bundle 7 alone. Report the top bin (above 0.9) separately.
   - *Pass:* adds to the core on average and median, with at least 20 trades, and the top bin is not negative.
   - *Fail:* drop the lead.

5. **Shares 5d avg 1.25 to 1.6 inside the core.** Score as a standalone tag on the core.
   - *Pass:* median above the core and at least 20 trades in bundle 7.
   - *Fail:* drop.

6. **Days since spike, clean split.** Score day 0 and day 1 as separate, non-overlapping groups, with at least 20 trades each.
   - *Pass:* same sign in both groups and at least 20 trades each.
   - *Fail:* drop as a data artifact.

7. **Wrapper logging.** Continue 30-day 0%, 5%, and 10% and 90-day 5% calls on the entry names.
   - *Pass:* a structure with a median better than -20% and an average at least as high as the core's, over at least 30 trades.
   - *Status:* 30-day 0% at 20 trades (bundle 6) and about 29 across two bundles. Not yet 30 in one bundle. Keep logging.

8. **Hold-period test.** If 5-, 10-, and 20-session returns are supplied, compare them on the core. *Pass:* a different hold beats 10 sessions on both average and median.

9. **Market gate stays.** No signal when market 20d % ≤ 0.

10. **IV gate, rule-level.** Score IV < 60 against IV ≥ 60 on the same base. *Pass:* IV < 60 wins on average and median. *Fail:* keep the gate only if bundle 7 shows the rule-level result still holds.

**Not carried forward:** the full stock rule (core + shares ≥ 1 + vs ma20 ≥ 5) is dropped as a real-money idea. The extras were never scored and the core is the only real-money rule.

---

## 4. Supporting evidence and dropped ideas

### Evidence supporting the stock core
- **Cumulative:** 130 trades, average +2.3%, median +0.4%, 95% range +0.2% to +4.5%, beat the benchmark in 5 of 6 bundles.
- **Call days 2x+ (5d) ≥ 1:** positive in bundles 4, 5, and 6 when at least one such day occurred. Zero such days was negative in bundles 5 and 6.
- **IV < 60:** bundle 6 quintiles favor the gate. 86+ IV was the weakest bin in bundles 5 and 6.
- **Market gate:** every call-buying rule has lost when market 20d % < 0.

### Caution on the stock core
- The median is +0.4%. The average depends on a few large winners.
- The 20d % top bin was negative in bundle 6 (-1.8%). The 20d ≥ 10 condition has not been tested for an upper bound.
- The close-vs-vwap lead's top bin was negative in bundle 6.
- Benchmark moves: +1.8% (bundle 4), +1.3% (bundle 5), +1.4% (bundle 6). Judge by beating it, not by raw returns.

### Evidence against the option wrapper
- **Bundle 3:** 31 trades, median -38%.
- **Bundle 4:** 38 trades, median -43%.
- **Bundle 5:** 41 trades, median -35%.
- **Bundle 6:** 50 trades, median -1.3%. Positive for the 30-day 0% group (20 trades, median +11.6%), but the 30-day 10% group had a median of -71%.
- Across the universe, the 30-day at-the-money call had a negative median in every IV band and every iv/realized band in bundle 6.

### Dropped ideas
- **vs ma50 % top bin:** strong in bundle 5, negative in bundle 6. Dropped.
- **iv/realized top band:** positive in bundles 4 and 5, negative in bundle 6. Dropped.
- **Market 5d % momentum:** sign flipped between bundles. Dropped.
- **News count, 1 to 2 articles in 7 days:** sign flipped across bundles 3 to 5. Dropped.
- **Oversold alone (RSI < 30, no call filter):** 170 trades, median -1.2%, beat the benchmark in 2 of 5 bundles. Failed.
- **Oversold with call buying:** failed in bundle 4.
- **Calls 20d as a ranking (higher is better):** not monotonic. The 1.5 floor works better as a range than as a ranking.
- **Ratings as an input:** flipped pattern in every bundle. Paper-only.
- **30-day 5% as the main wrapper:** the median has not replicated across bundles.
- **Discretionary option picks, double-or-10 exits, 14-day expiries, strikes 10%+ above price, sub-$10 names for real money:** negative in earlier bundles, not revisited.

### Leads kept as tags (not traded)
- **Close vs vwap ≥ 0.18:** cumulative median +1.3%, 55 trades. Test in section 3, item 4.
- **Shares 5d avg 1.25 to 1.7:** positive in bundles 5 and 6. Test in section 3, item 5.
- **Calls 20d 1.2 to 2.2:** positive shape in bundles 5 and 6. Test in section 3, item 2.
- **Off-high pullback (-16% to -8%):** +3.9% in bundle 6. One bundle.
- **RSI 68+:** positive in bundles 5 and 6. Tag only.
- **Days since spike, day 0 vs day 1:** unresolved, needs clean bins.

(Recorded by the system: this trader ran 14 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)

### Agent 4's final notes (not passed on)

# WORKING NOTES: END OF BUNDLE 6 (GENERATION 2)

## 1. MY CURRENT STRATEGY

**Status: paper trades only.** No real money. Option marks have not been audited, and option medians have been negative in every 30-day bucket in every bundle. My stock-level results are more trustworthy than option results. My own picks and ratings are not part of the strategy.

### 1a. Lead candidate: stock-level AB+O (oversold, no spike today)

Scored on the 10-session stock return, not on an option.

- **RSI (14-session) ≤ 35**
- **Days since spike > 0** (exclude today's spike)
- **News 7d ≥ 1**
- Hold 10 sessions. No stops.

**Cumulative record (all bundles, 183 trades):** average +2.0% (95% range -1.1% to +5.6%), median +0.7%, 56% winners. Buy-everything benchmark over the same period: +0.6%. Beat the benchmark in 5 of 6 bundles. First half of the months +0.7%, second half +3.2%.

**Confidence: low-moderate.** This is the strongest stock-level result I have. Its edge is small, and its average depends on a few large moves. The RSI condition alone is not a rule (see section 4).

### 1b. Option baseline AB (pre-registered, unchanged, under review)

Enter when all hold:
- Market 20d % > 0
- Vs ma50 % > 0 and 20d % > 0
- News 7d ≥ 1
- iv/realized < 1

Instrument: 30-day call, strike about 5% above price. Require at least 20 sessions to expiry at entry. Exit after 10 sessions (or at expiry if sooner). No stops, adds, or early exits. One equal premium unit per signal.

**Status:** AB's median is strongly negative (-58.1% after bundle 5, 123 trades). Its positive average comes from a few very large winners. **I cannot yet report AB's bundle 6 result on its own.** The bundle 6 report gives no AB-only row. I must pull AB's bundle 6 trades from the trade log before I state anything about this bundle.

AB is not a recommendation to trade real money. It remains a paper test until the exit-mark and expiry audits are done.

### 1c. Option sub-filters to test inside AB (not yet rules)

- **IV band:** Bundle 6 option-level data show high IV is worst on both average and median. At-the-money 30-day calls with IV 85 to 224% had a median of -70% (avg -25%). IV 7 to 30% had a median of -27% (avg +14%). Test "IV below 30 (or 25)" inside AB.
- **iv/realized below 0.75:** Bundle 6 option-level: avg +44%, median -30%. The other bands had averages of -9% to +2% and medians of -25% to -46%. This is the best option-level band in bundle 6 (single bundle; bundle 5's stock-level read was negative for this band, so it is unconfirmed).

### 1d. Exclusions (apply to every entry)
- Spike today (days since spike = 0), until bundle 6's contradicting read is resolved (section 2c).
- Shares today < 1 (see section 4 for the evidence on this filter).
- Fewer than 20 sessions to expiry.
- 14-day expiries.
- Sub-$10 names with extreme call volume, until marks are audited.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### 2a. Stock baseline
- All 249 candidates: average +1.4%, median -0.0%. Roughly half rose.
- Ratings: rated +1 (35 stocks) averaged +5.0%, median +1.7%. Rated 0 (60) averaged -1.4%. Rated -1 (133) averaged +2.1%. Rated -2 (16) averaged -1.0%, median -3.4%. The +1 bin was positive here, but the ordering is not consistent across bundles. Ratings stay retired.

### 2b. My own trades (not part of the strategy)
- 27 trades, +$5,389. Average +20.0%, median -9.5%, 48% winners.
- The 30-day at-the-money-or-5%-above call bucket (8 trades) had a median of -49.1%. The total profit came from a few large winners, the same tail pattern as in bundles 4 and 5.

### 2c. Rule checks (cumulative across all bundles, as reported)

| Rule | Trades | Average | Median | Winners | Buy-all | Halves | Beat benchmark |
|---|---|---|---|---|---|---|---|
| AB+O (oversold, no spike today, news ≥ 1) | 183 | +2.0% | +0.7% | 56% | +0.6% | +0.7% / +3.2% | 5 of 6 |
| Spike exactly yesterday | 231 | +0.1% | +0.1% | 50% | +0.6% | -0.9% / +1.3% | 2 of 6 |
| Vs ma50 top quintile (above 12.7) | 474 | +2.3% | -0.1% | 49% | +0.6% | +2.7% / +2.0% | 5 of 6 |

What these say:
- **AB+O** is the best stock-level combination so far (section 1a).
- **Spike yesterday has weakened.** Bundles 3 to 5 looked strong on the quintile bins, but the cumulative rule check is flat (median +0.1%, beats buy-all in only 2 of 6 bundles). **Demoted to low confidence.** Do not trade it.
- **Vs ma50 top quintile** has a positive average and a median near zero. Its average depends on tails. **Bundle 6 contradicted it** (see 2d).

### 2d. Stock-level quintile reads, bundle 6 (median 10-session return, % up)

**Confirmed from earlier bundles:**
- **Shares 5-day ratio 1.33 to 1.72:** +3.4%, 62% up. Bundle 5 gave +3.3% (66%). Two bundles now positive. This is the most consistent stock-level bin I have. Confidence rises to moderate.
- **Shares 5-day ratio 0.5 to 0.9:** -2.1%, 43% up. Thin share volume is weak again.
- **Shares today 2.25 to 9.2:** +2.0%, 58% up. Shares today 0.89 to 1.1: -1.6%, 44%. Supports the shares-today filter (≥ 1).
- **News 7d:** the 0-news bin (0 to 1) was -1.8%, 32% up. The 1 to 2 news bin was +4.0%, 72% up. News present beats no news again (fourth bundle).
- **Call persistence (call days 2x+ in last 5 sessions):** 0 to 1 values were negative (about -1.4% to -1.6%, 37% to 38% up). 3 to 5 gave +4.3% (64% up). The value 2 bin was flat (0.0%, 50%). Partly confirmed: the "0 or 1 is negative" part holds. The threshold at 2 is not clearly better than 1.
- **Exact zero short-dated call ratio:** -4.0%, 16% up (bundle 6). Bundle 5 showed -2.9% (25% up) for the same boundary. **Two bundles negative at exact zero.** Treat "no short-dated call activity" as a negative signal (watch, low-moderate).

**Contradicted:**
- **Spike today (days since spike = 0):** The bin labelled 0 splits into two. One tiny bin was -9.1% (0% up). The other was +5.3% (86% up). The "0 to 3 days" bin was +3.7% (60% up). This does not replicate the three-bundle pattern that made spike-today the weakest bin. **Confidence in the spike-today exclusion drops to low-moderate.** Keep it in AB+O because the combined rule check was measured on all bundles, but flag it as contested.
- **Vs ma50 top quintile (11.9 to 85.5):** -3.0%, 43% up. Bundle 5 showed +5.4% (71% up). The -13.5 to -2.7 bin was +3.6% (59% up). In bundle 6, stocks that were extended underperformed and stocks that dipped below their 50-day outperformed. This is the opposite of the continuation read from bundle 5. **The trend question is unresolved.** The cumulative rule check (+2.3% avg, -0.1% median) is driven by tails.
- **20-day change:** The -11.9 to -2.6% bin was +3.7% (60% up). The top bin (13.5 to 124%) was -1.8% (42% up). This is a mild reversal pattern, the reverse of the trend-continuation reading. One bundle. Watch.

**Mixed or noise:**
- **RSI:** 10 to 34: +0.8% (55% up). 34 to 45: +0.6%. 45 to 56: -0.7%. 56 to 68: -1.0%. 68 to 89: +1.9%. This is U-shaped in bundle 6 and was monotonic in bundle 5. The oversold bin was mildly positive here, so it did not fail as it did in bundle 5. Cumulative RSI evidence is still weak on its own.
- **Close vs vwap:** Top quintile +1.3% (bin 0.23 to 0.86), but the 0.9+ bin was -0.7%. The bundle 5 top quintile (+2.4%) did not replicate. Watch item, downgraded.
- **Iv:** 7 to 30%: +0.8%. 86 to 224%: -5.4% (40% up). High IV is the weakest stock bin in bundle 6.
- **iv/realized:** Below 0.75: +0.8%. Above 1.23: -0.5% to -1.1%. Bundle 5 showed the reverse at the stock level. Still unresolved at the stock level.
- **Puts 5-day avg 2.61 to 5.51:** +3.6%, 60% up. Positive in bundle 6. Not previously tested as a filter. Watch.
- **Market 20d:** 1.5 to 2.6 was +2.8% (62% up). Above 2.6 was -1.0% to -1.1%. Bundle 5's best bin was 2.4 to 3.6. The stock-level market read is still unstable.
- **Off high:** -16 to -7.8% was +3.9% (59% up). Earlier bundles dropped this. Noise until replicated.

### 2e. Option-level reads (bundle 6)

- **30-day at-the-money call, held 10 sessions, by IV:**
  - 7 to 30%: avg +14%, median -27%
  - 30 to 43%: avg +9%, median -18%
  - 43 to 62%: avg +12%, median -20%
  - 62 to 84%: avg -11%, median -32%
  - 85 to 224%: avg -25%, median -70%
- **30-day at-the-money call, by iv/realized:**
  - Below 0.75: avg +44%, median -30%
  - 0.75 to 0.99: avg +2%, median -25%
  - 1.00 to 1.21: avg -9%, median -43%
  - 1.23 to 1.63: avg -21%, median -46%
  - 1.64 to 3.34: avg -17%, median -31%

Every bucket has a negative median. The IV pattern (low IV better, high IV much worse) and the iv/realized pattern (cheap best) both point the same way. Both are single-bundle reads at the option level.

**Big winners follow big stock moves.** The largest option gains came with stock moves of +82%, +46%, +12%, +10%, and +9%. Options add leverage to a real move. A winner on a flat stock is suspicious (see 2f).

**Big losers on large stock declines are probably real.** Three trades lost 91% to 95% with the stock down 20% to 22%. A strike 5% above the price expires nearly worthless when the stock falls that far.

### 2f. Exit-mark audit (top priority, still open)

**Flagged this bundle (loss above 60% with the stock within ±5%):**
- -63.1% with the stock at -3.8% (IV 65%, 26 sessions to expiry, premium 8.9% of price)
- -71.4% with the stock at +2.5% (IV 33%, 25 sessions to expiry, premium 1.3% of price, 10% above strike)

**Also suspicious (losses of 49% to 54% on flat stocks):**
- -53.7% with the stock at -1.5% (IV 26%, 30 sessions)
- -49.1% with the stock at -0.1% (IV 39%, 24 sessions)
- -49.0% with the stock at -0.9% (IV 27%, 23 sessions)

Five of these losses on flat stocks are unlikely to come from decay alone over 10 sessions with IV around 26 to 40%. This pattern has now appeared in bundles 5 and 6. I cannot yet tell stale marks from real decay or from a wrong contract. **I am lowering the flag threshold to a loss above 45% with the stock within ±5%.** That catches the five trades above.

**Winners on flat stocks are also suspicious:** +95.7% with the stock at +3.7% (IV 20%, 26 sessions) and +49.5% with the stock at +6.6%. These are as implausible as the flat-stock losses. Cheap entries cut both ways.

**Premiums under 1% of price:** None in bundle 6 (lowest was 1.3%).

**Not yet done:** Re-marking flagged trades to intrinsic value at session 10, and the with-and-without comparison. This needs the trade log, not the summary report.

### 2g. Expiry audit (still open)
Sub-20-session trades need to be removed from AB, and the sign of AB recomputed. Not done for bundle 5 or bundle 6.

### 2h. Execution
Bid-ask cost is still not in the book. Every positive option average is an upper bound.

---

## 3. WHAT I WILL TRY NEXT (bundle 7)

Pre-register everything. For each test, report n, average, median, win rate, 95% range where available, both halves of the months, and the same bundle's buy-everything benchmark.

**Priority 1: Audits (required before any option rule changes)**
1. **Exit-mark audit.** Flag every trade where the option lost more than 45% while the stock moved within ±5%. Report results with and without flagged trades, and with flagged trades re-marked to intrinsic value at session 10 (or a model value at the traded IV). No rule change until this is done.
2. **AB bundle 6 result.** Pull AB's bundle 6 trades from the log and report them as a separate row. Back-fill AB's bundle 5 row the same way.
3. **Expiry audit.** For every AB trade, report how many change sign when sub-20-session trades are removed.

**Priority 2: Stock-level tests (scored on stock return, no options)**
4. **AB+O (lead candidate).** Keep the rule as written. Report every bundle separately. Confirm the median stays positive.
5. **AB+O plus shares today ≥ 1.** Explicit arm.
6. **AB+O plus shares 5-day avg 1.33 to 1.72.** Explicit arm (promoted from quintile read, two bundles positive).
7. **AB+O with spike-today exclusion removed.** Tests whether the exclusion is helping or hurting after bundle 6's contradiction.
8. **AB+O plus call days 2x+ ≥ 2 (and separately ≥ 3).** Tests whether the threshold should move to 3.
9. **AB+ (existing shadow arm) and AB+U (uncapped: no vs ma50 or 20d caps).** Compare on the same stocks as the benchmark.
10. **Trend test, rewritten.** Stock-level: top vs ma50 quintile (above 11.9) versus the rest, and the 20-day top bin versus the rest. Bundle 5 said continuation; bundle 6 said fade. Report both signs and let the next bundle decide.

**Priority 3: Option-level tests (inside AB, paper)**
11. **AB with IV below 30 versus AB with no IV condition.** Judge on average and halves only (medians are negative in every arm).
12. **AB with iv/realized below 0.75 versus AB as written.** Bundle 6 option-level showed this band best.
13. **AB without the market gate (AB-nm).** Same stocks as AB. Decides whether the gate stays.
14. **Strike logging.** At-the-money, 5% above, and 10% above on the same signals. Needs 15 to 20 trades per strike before reading.
15. **Hold logging.** 5-, 10-, and 15-session outcomes on the same signals.

**Watch items (log, do not act):**
- Puts 5-day average 2.6 to 5.5 (+3.6%, bundle 6 only).
- Exact-zero short-dated call ratio (negative in bundles 5 and 6). Check whether this is a data-boundary artifact.
- 20-day change reversal pattern (bundle 6 only).
- Close vs vwap top quintile (did not replicate in bundle 6).
- Market 20d between 1.5 and 2.6 (bundle 6 best; bundle 5 best was 2.4 to 3.6).

---

## 4. SUPPORTING EVIDENCE AND IDEAS I HAVE DROPPED

### Supporting evidence (with confidence)

- **Options have negative medians on this structure (all bundles, all 30-day buckets).** High confidence. Averages come from a few large winners.
- **Option results are sensitive to IV and iv/realized.** Low IV and cheap iv/realized did better in bundle 6 (option level). Low-moderate. Unconfirmed at the stock level.
- **AB+O (oversold, no spike today, news ≥ 1) beats buy-all in 5 of 6 bundles, median +0.7%.** Low-moderate. Second half much stronger than first (+3.2% vs +0.7%).
- **News present beats no news.** Moderate, four bundles.
- **Shares 5-day ratio 1.33 to 1.72 beats others.** Moderate, two bundles (+3.3%, +3.4%). Best stock bin in both.
- **Shares today ≥ 1 (not thin) is positive.** Low-moderate, three bundles.
- **Thin shares 5-day ratio (0.5 to 0.9) is negative.** Low-moderate, two bundles.
- **Call persistence: 0 or 1 days is negative, 3 to 5 is positive.** Moderate. The threshold of 2 is unclear.
- **Exact-zero short-dated call ratio is negative.** Low, two bundles. Possibly a boundary artifact.
- **Oversold (RSI ≤ 35) is weak alone.** Bundle 5 negative, bundle 6 mildly positive. Low. Used only inside AB+O.
- **Ratings (all forms) show no reliable ordering.** Bundle 6's +1 bin was positive, but the -2 bin was negative and the ordering has not held across bundles. Retired.

### Dropped or demoted

- **Spike yesterday as a rule.** Demoted. The cumulative rule check is flat (+0.1% median, beats buy-all in 2 of 6). The quintile bins from bundles 3 to 5 did not hold up in aggregate.
- **Spike-today exclusion.** Contested. Strong in bundles 3 to 5, but bundle 6's split bins were positive. Kept only in AB+O, flagged.
- **Vs ma50 continuation.** Contested. Positive average, median near zero, and bundle 6's top quintile was negative. Not a rule until resolved.
- **Overextension fade (vs ma50, vs ma20, 20d).** Failed in bundles 4 and 5. Bundle 6 showed a mild reversal pattern in 20-day change, so the question is open, not closed.
- **News 1 to 2 cap.** Dropped. Keep news ≥ 1 with no upper cap.
- **Puts spike fade and heavy calls spike exclusion.** Not replicated. Dropped.
- **Otm calls ratio.** Flipped between bundles. Dropped.
- **Market 20d gate at stock level.** Unstable. Kept only inside AB until AB-nm is tested.
- **Close vs vwap top quintile.** Did not replicate in bundle 6. Watch only.
- **Off-high, news tone, realized vol, vol20.** Not used. Off-high had a single positive bin in bundle 6 that does not yet justify a rule.
- **14-day expiries and sub-$10 lottery names.** Excluded until marks are audited.
- **Premium paid under 1% of price.** Excluded until marks are audited.

### Open questions

- Does AB+O's edge survive a seventh bundle, especially its first-half weakness?
- Does the spike-today exclusion help or hurt? Bundle 6 says it may not matter.
- Does vs ma50 continue or fade? Bundle 5 says continue, bundle 6 says fade.
- Are the flat-stock losses of 49% to 71% (and the flat-stock wins of 50% to 96%) real decay, or stale marks? The exit-mark audit decides this. Until it is done, no option result is trusted.
- Does the low-IV, cheap-iv/realized option band hold at the stock level and in a second bundle?
- What is the bid-ask cost on 30-day, 5%-above calls at these prices? This decides whether any positive option average survives.
- Does the market gate matter in a bundle where the market moves more than the recent ones?

(Recorded by the system: this trader ran 18 rule checks on its finished bundles during this generation. More checks mean more chances for a lucky rule.)


## Generation 8

### Editor's rules, tested on all training months and bundles

- R1 overbought sustained calls 5% OTM (when rsi > 70 and calls 20d > 2: buy the 30-day call 5% above the price, exit hold10): 175 trades, average +34.0% (95% range +1.9% to +67.5%, resampling whole weeks), median -53.4%, 34% winners. Buying every candidate the same way: -12.2%. Beat that in 5 of 6 bundles; first half of the months +62.5%, second half +15.0%.
- R1-$50 overbought calls up market (when rsi > 70 and calls 20d > 2 and market 20d % > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 44 trades, average +52.4% (95% range -6.9% to +135.3%, resampling whole weeks), median -21.5%, 43% winners. Buying every candidate the same way: -12.2%. Beat that in 5 of 6 bundles; first half of the months +40.9%, second half +60.4%.
- R2 momentum run up market 10% OTM (when 20d % > 20 and vs ma50 % > 15 and market 20d % > 0: buy the 30-day call 10% above the price, exit hold10): 173 trades, average +42.5% (95% range +4.3% to +83.0%, resampling whole weeks), median -49.8%, 33% winners. Buying every candidate the same way: -17.7%. Beat that in 6 of 6 bundles; first half of the months +25.6%, second half +52.1%.
- R4 momentum accumulation (when calls 20d >= 1.5 and 20d % >= 10 and vs ma20 % >= 5: buy the 30-day call 5% above the price, exit hold10): 297 trades, average +17.8% (95% range -5.4% to +39.9%, resampling whole weeks), median -50.4%, 33% winners. Buying every candidate the same way: -12.2%. Beat that in 6 of 6 bundles; first half of the months +27.3%, second half +11.1%.
- R3 trend news tone over $50 (when vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 143 trades, average +23.4% (95% range -5.9% to +59.0%, resampling whole weeks), median -41.3%, 38% winners. Buying every candidate the same way: -12.2%. Beat that in 4 of 6 bundles; first half of the months +23.8%, second half +23.1%.
- R6 uptrend up market plus news (when vs ma50 % > 0 and 20d % > 0 and market 20d % > 0 and news 7d >= 1: buy the 30-day call 5% above the price, exit hold10): 349 trades, average +15.2% (95% range -1.8% to +34.6%, resampling whole weeks), median -48.3%, 30% winners. Buying every candidate the same way: -12.2%. Beat that in 5 of 6 bundles; first half of the months -0.5%, second half +24.6%.
- R11 90d trend up market 10% OTM (when vs ma50 % > 0 and market 20d % > 0: buy the 90-day call 10% above the price, exit hold10): 183 trades, average +3.3% (95% range -10.6% to +17.0%, resampling whole weeks), median -16.1%, 38% winners. Buying every candidate the same way: -9.7%. Beat that in 5 of 6 bundles; first half of the months +0.5%, second half +4.6%.
- R8 over $50 trend up market ATM (when price = >$50 and vs ma50 % > 0 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 259 trades, average +5.0% (95% range -9.7% to +18.7%, resampling whole weeks), median -25.1%, 38% winners. Buying every candidate the same way: -10.9%. Beat that in 6 of 6 bundles; first half of the months -5.1%, second half +11.3%.

### The same rules on the blind scoring months (never shown to agents)

- R1 overbought sustained calls 5% OTM (when rsi > 70 and calls 20d > 2: buy the 30-day call 5% above the price, exit hold10): 148 trades, average -24.5% (95% range -45.2% to -2.1%, resampling whole weeks), median -59.9%, 26% winners. Buying every candidate the same way: -19.8%. Beat that in 2 of 6 bundles; first half of the months -14.3%, second half -34.8%.
- R1-$50 overbought calls up market (when rsi > 70 and calls 20d > 2 and market 20d % > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 30 trades, average -21.5% (95% range -49.3% to +8.2%, resampling whole weeks), median -48.5%, 27% winners. Buying every candidate the same way: -19.8%. Beat that in 2 of 6 bundles; first half of the months +2.0%, second half -42.2%.
- R2 momentum run up market 10% OTM (when 20d % > 20 and vs ma50 % > 15 and market 20d % > 0: buy the 30-day call 10% above the price, exit hold10): 159 trades, average -21.7% (95% range -42.0% to -1.2%, resampling whole weeks), median -59.9%, 25% winners. Buying every candidate the same way: -20.6%. Beat that in 4 of 6 bundles; first half of the months -14.0%, second half -29.7%.
- R4 momentum accumulation (when calls 20d >= 1.5 and 20d % >= 10 and vs ma20 % >= 5: buy the 30-day call 5% above the price, exit hold10): 225 trades, average -19.4% (95% range -36.0% to -1.5%, resampling whole weeks), median -59.7%, 26% winners. Buying every candidate the same way: -19.8%. Beat that in 3 of 6 bundles; first half of the months -13.2%, second half -26.0%.
- R3 trend news tone over $50 (when vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price = >$50: buy the 30-day call 5% above the price, exit hold10): 89 trades, average -7.8% (95% range -40.0% to +30.7%, resampling whole weeks), median -56.2%, 28% winners. Buying every candidate the same way: -19.8%. Beat that in 3 of 6 bundles; first half of the months +17.1%, second half -24.8%.
- R6 uptrend up market plus news (when vs ma50 % > 0 and 20d % > 0 and market 20d % > 0 and news 7d >= 1: buy the 30-day call 5% above the price, exit hold10): 284 trades, average -12.1% (95% range -27.6% to +2.9%, resampling whole weeks), median -51.3%, 28% winners. Buying every candidate the same way: -19.8%. Beat that in 5 of 6 bundles; first half of the months -10.1%, second half -14.2%.
- R11 90d trend up market 10% OTM (when vs ma50 % > 0 and market 20d % > 0: buy the 90-day call 10% above the price, exit hold10): 159 trades, average -11.1% (95% range -20.0% to +0.3%, resampling whole weeks), median -24.8%, 26% winners. Buying every candidate the same way: -7.8%. Beat that in 2 of 6 bundles; first half of the months -11.8%, second half -10.3%.
- R8 over $50 trend up market ATM (when price = >$50 and vs ma50 % > 0 and market 20d % > 0: buy the 30-day call 0% above the price, exit hold10): 188 trades, average -20.9% (95% range -35.1% to -4.2%, resampling whole weeks), median -42.0%, 29% winners. Buying every candidate the same way: -14.7%. Beat that in 2 of 6 bundles; first half of the months -22.9%, second half -19.0%.

### Editor's notes (passed to the next generation)

# PLAYBOOK FOR THE NEXT GENERATION

(Committee editor's synthesis. Inputs: the previous playbook and its code-tested scorebook, plus four traders' final notes and the code-tested scores of their own rules on all candidates over six bundles. Where a trader's figure and the scorebook differ, the scorebook is used.)

**Conventions.** Returns are per-trade option returns on premium, bought on the signal day and held 10 sessions unless noted.
- "Benchmark" means buying every candidate with the same expiry, strike and exit.
- "Range" is the 95% range from resampling whole weeks.
- "Halves" are the first and second half of the sample by month.
- "x of 6" is how many of the six bundles the rule beat its benchmark in.
- Every rule is written with exact conditions so you can restate it and have it scored.

---

## 0. BOTTOM LINE

**The option wrapper loses on average. Filters that pick strong, trending, overbought stocks in an up market turn some baskets positive, but only through a few large winners. No tested rule has a positive median.**

Benchmark averages for buying every candidate, held 10 sessions:

| Structure | Benchmark average |
|---|---|
| 30-day at-the-money (ATM) | -10.9% |
| 30-day 5% above | -12.2% (median -57.3%, 27% winners, 2,276 trades) |
| 30-day 10% above | -17.7% (median -67.6%, 23% winners) |
| 90-day ATM | -8.4% |
| 90-day 5% above | -7.4% |
| 90-day 10% above | -9.7% |
| 14-day ATM on call-volume surges | -15.2% |

**Main lessons of this generation:**
1. **Stock-level "signals" in the 1-to-3-point range do not make an option profitable.**
   - All four traders ended paused or paper-only after six bundles. Their stock-level edges were small: call days 2x+ of 2 to 5, news 7d of 1 to 2, calls 20d of 1.05 to 1.52, close vs vwap, and exclusions of high vol20 or realized vol.
   - Those edges were about +1% to +3.5% in stock median against a universe median near +0.4%.
   - Traders measured that a 30-day ATM call needs the stock up roughly +2% to +4% over 10 sessions to break even. A 5% above call needs roughly +6% to +12%.
   - Scored on every candidate, the traders' own gates mostly landed at -10% to 0% at ATM and -6% to -9% at 5% above. That is a little better than the benchmark and still negative.
2. **What the scorebook rewards is large moves.** Winning option trades needed the stock up about +3% to +17%. The rules that pay pick names that move a lot in the trend direction.
   - Strong trend, momentum, overbought status with sustained 20-day call buying, an up market, and price over $50 are the ingredients.
   - Mild strength loses and strong strength wins (see the strength cliff below).
3. **The market gate is the clearest sign flip.** Every call rule lost in a market with a negative 20-day return. Market 20d % > 0 alone does not help. It must be paired with stock strength.
4. **Traders' notes and scorebook disagree repeatedly.**
   - Three of four traders concluded vs ma50 %, RSI and the over-$50 band do not matter, or are noise, because single-bundle fifths flip sign.
   - Scored on all candidates, those same features, used as strong thresholds and combined with a market gate, are what separate the positive baskets.
   - **Trust the all-candidate scorebook over single-bundle quantile reads.**
5. **There is a persistent data-quality shadow.** Every trader flagged -100% exit marks on stocks that were flat or up, and "30-day" trades with 9 to 19 sessions to expiry. The scorebook does not audit this. Medians may be too pessimistic, and averages may be affected in either direction.

---

## 1. STRATEGY: SETUPS WORTH TRADING (paper, or small flat size)

All rules are bought on the entry day and exited after 10 sessions unless noted.
- Take every signal that passes. Do not cherry-pick, because skipping signals loses the few big winners.
- Spread premium across many names, use flat small size, and never add after wins.
- Size so that a -100% loss on every open position is survivable.
- These rules overlap heavily, because they pick up the same trending, overbought, up-market names. Do not count them as independent confirmations.

### 1A. Tier 1: positive average, large n, beat the benchmark in most bundles

These figures come from the previous generation's code scorebook. None of the four traders tested them, so they remain the best statistics available. Treat them as unreplicated out of sample.

**R1. Overbought with sustained call buying, 30-day call 5% above**
- Rule: rsi > 70 and calls 20d > 2.
- Result: 175 trades, average **+34.0%** (range +1.9% to +67.5%), median -53.4%, 34% winners. Benchmark -12.2%, 5 of 6. Halves +62.5% and +15.0%.
- Control (rsi > 70 and calls 20d ≤ 2): 119 trades, +1.0%. The call-flow condition adds the edge.
- The vs ma50 % > 0 version is the same (172 trades, +33.0%), so that condition adds nothing.
- Calls 20d > 2 sits just under the "calls 20d at or below 2.1" cut that Agent 4 used as a gate. Agent 4's gate, news 7d ≥ 1 and calls 20d ≤ 2.1 and vol20 % ≤ 5, scored -9.3% at 5% above. The upper cut on sustained call flow is therefore not a good rule when the stock is overbought. Heavy 20-day call buying helps on strong stocks and hurts on weak ones.
- **R1-$50** (price over $50, rsi > 70, calls 20d > 2, market 20d % > 0, 30-day 5% above): 44 trades, **+52.4%** (range -6.9% to +135.3%), median **-21.5%**, 43% winners, 5 of 6. Halves **+40.9% and +60.4%**.
  - This is the best average, the best median and the most even halves of any 30-day variant, but n is small and the range touches zero.
- **R1b.** Same entries at 30-day ATM with market 20d % > 0: 153 trades, +7.8%, median -39.0%, 5 of 6. Halves +27.6% and -2.2%.
- **R1c.** rsi > 70 and calls 20d > 2, 30-day 10% above, exit as soon as the option doubles, else after 10 sessions: 147 trades, +6.9% (range -12.5% to +24.2%), median -44.2%, 6 of 6. Halves +12.2% and +3.6%. This is the only double-or-10 result that works.

**R2. Momentum run, 30-day call 10% above**
- Rule: 20d % > 20 and vs ma50 % > 15.
- Result: 211 trades, **+26.2%** (range -6.0% to +61.0%), median -57.4%, 30% winners. Benchmark -17.7%, **6 of 6**. Halves +11.9% and +35.9%.
- The looser version (20d % > 15, vs ma50 % > 10) is +14.4%. Stricter is better.
- Never use it when market 20d % < 0 (38 trades, -47.8%).
- At 90 days: 57 trades, -4.4%, median -20.3%.

**R3. Trend, news tone and over $50, 30-day call 5% above**
- Rule: vs ma50 % > 0 and 20d % > 0 and news tone 7d > 0 and price over $50.
- Result: 143 trades, **+23.4%** (range -5.7% to +56.8%), median -41.3%, 38% winners, 4 of 6. Halves +23.8% and +23.1%.

**R4. Momentum accumulation**
- Rule: calls 20d ≥ 1.5 and 20d % ≥ 10 and vs ma20 % ≥ 5.
- At 30-day 5% above: 297 trades, **+17.8%** (range -5.4% to +39.9%), median -50.4%, **6 of 6**. Halves +27.3% and +11.1%.
- At 30-day 10% above: 279 trades, +7.0%, 6 of 6.
- R4b, with market 20d % > 0 at ATM: 243 trades, +6.1%, 5 of 6. Halves +11.4% and +3.0%.

**R5. Momentum plus news, 30-day call 5% above**
- Rule: 5d % > 5 and vs ma20 % > 5 and news 3d ≥ 1.
- Result: 186 trades, +16.4%, median -48.4%, 4 of 6. Halves +13.0% and +20.8%.

**R6. Uptrend in a rising market, 30-day call 5% above**
- Rule: vs ma50 % > 0 and 20d % > 0 and market 20d % > 0.
- Result: 666 trades, **+9.1%** (range -6.7% to +24.7%), median -48.8%, **6 of 6**. Halves +5.1% and +11.3%.
- At 10% above: 561 trades, +8.8%, 6 of 6. Halves -4.7% and +16.1%.

**R7. Regime gate, 30-day call 5% above**
- Rule: market 20d % > 0 and vs ma50 % > 0 and rsi > 60.
- Result: 430 trades, **+9.4%**, median -47.9%, **6 of 6**. Halves +0.0% and +15.1%.
- Without the rsi condition: 756 trades, +6.1%, 6 of 6.
- ATM version (vs ma20 % > 0 and market 20d % > 0): 885 trades, -4.2%, 6 of 6. It beats the benchmark but is still negative.

**R8. Price, trend and market gate, 30-day ATM**
- Rule: price over $50 and vs ma50 % > 0 and market 20d % > 0.
- Result: 259 trades, +5.0%, median -25.1%, 38% winners, **6 of 6**. Halves -5.1% and +11.3%.
- The four-gate version (adds 20d % > 0): 236 trades, +6.6%, 5 of 6.
- Do not use the 10% above version (halves -37.0% and +24.7%).
- This is the best median of the 30-day positive-average rules.

**R9. Winner profile, 30-day ATM**
- Rule: 20d % > 20 and vs ma50 % > 10 and rsi > 60.
- Result: 205 trades, +5.2%, median -42.6%, 5 of 6. Halves +10.3% and +1.9%.

**R10. Run-ups, 30-day call 5% above**
- Rule: 20d % ≥ 25 and vs ma20 % ≥ 10.
- Result: 209 trades, +9.1%, 5 of 6. Halves +3.5% and +14.6%.
- Extension does not fade at 30 days.

**R11. 90-day call 10% above**
- Rule: vs ma50 % > 0 and market 20d % > 0.
- Result: 183 trades, +3.3%, median -16.1%, 5 of 6. Halves +0.5% and +4.6%.
- The market gate is the point: the same stock condition with market 20d % < 0 averaged -12.9%.

**R12. 90-day call 10% above, over $50**
- Rule: calls 5d avg > 1 and vs ma50 % > 0 and market 20d % > 0 and price over $50.
- Result: 42 trades, +7.0%, median **-8.0%**, 45% winners, 4 of 6. Halves -8.3% and +13.9%.

### 1B. New this generation: weakly confirmed filters from the traders' rules

These are not trade-worthy alone. They are useful as add-on filters that beat their benchmarks but average near zero or below.

- **News 7d ≥ 1, 30-day 5% above:** 1,125 trades, -6.4%, median -53.3%, **5 of 6** vs -12.2%. Halves -6.3% and -6.5%.
  - This is the most replicated stock-level filter across four traders. It is steady across halves, but still negative.
  - Test it as an add-on to R1, R4 and R6.
- **Calls 20d 1.05 to 1.52 with call days 2x+ of 2 to 3, 30-day ATM:** 159 trades, **+0.4%** (range -22.4% to +26.7%), median -31.3%, 36% winners, 4 of 6 vs -10.9%. Halves +2.0% and -0.9%.
  - Agent 2's trade-level idea, confirmed as roughly break-even.
  - With call days 2x+ ≥ 2 only: 177 trades, -2.1%, 4 of 6.
- **News 7d of exactly 1 near the 60-day high, 30-day ATM** (news 7d ≥ 1 and news 7d ≤ 1 and off high % ≥ -15): 244 trades, **+0.1%**, median -31.4%, 4 of 6. Halves -7.9% and +6.6%.
- **News 7d of exactly 1, call days 2x+ of 2 to 5, vol20 % < 5.1, 30-day ATM:** 155 trades, -0.3%, median -31.3%, 3 of 6. Halves -5.0% and +4.0%.
- **Call days 2x+ of 2 to 5, 90-day call 10% above:** 296 trades, -6.0% (range -16.4% to +3.7%), median -25.6%, 5 of 6 vs -9.7%. Halves -8.5% and -3.5%.
  - The same rule at 90-day ATM is -10.3%, 2 of 6, so it does not work at ATM.
- **Off high % ≥ -2 with call days 2x+ of 2 to 3, 30-day ATM:** 195 trades, -6.0%, 4 of 6. Halves +5.6% and -13.7%.
- **Mixed filters at 30-day ATM:** news 3d ≥ 1 and close vs vwap % > 0 and call days 2x+ ≥ 2 scored -4.2% (218 trades, 4 of 6, halves +6.7% and -18.7%).
- **Quiet after a spike, 30-day ATM** (days since spike ≥ 20 and calls 5d avg < 1): 117 trades, +10.1%, 2 of 6, both halves positive (+20.3% and +1.6%).
- **Sub-$10 with huge call volume, 30-day 10% above** (price under $10 and calls 20d > 10): 47 trades, +39.9% (range -19.2% to +107.3%), median -45.1%, 3 of 6. Halves +34.8% and +46.8%. This is a paper-size lottery only.
- **Oversold quiet-call pattern, 90-day 5% above** (rsi < 30 and off high % ≤ -30 and calls 20d < 1.5): 8 trades, +20.6%, **median +13.2%**.
  - It is the only positive median seen anywhere, but n = 8. It is a lead only.
- **Oversold, 90-day ATM** (rsi < 30): 66 trades, -5.0%, median -7.8%, 4 of 6.
- **Fresh spike, 90-day ATM** (days since spike from 1 to 5): 150 trades, -3.1%, median -11.8%, 5 of 6.

### 1C. Sizing and structure guidance

- **Tail-seeking basket:** 30-day 5% above with R1 to R7. Median about -40% to -57%.
- **Steadier basket:** 90-day 10% above with the trend plus market gate (R11, R12). Median -8% to -16%.
- **Middle road:** 30-day ATM with R8. Median -25%.
- **Best median among the big-average rules:** R1-$50 (-21.5%, n = 44).
- Never use 14-day expiries. Hold 10 sessions; no exit rescues a bad entry.
- **Always apply market 20d % > 0 to trend, momentum and call-flow rules, and pair it with stock strength.**
- The scorebook charges no bid-ask spread. Real results will be worse than these averages.

---

## 2. AVOID

### Confirmed bad (scorebook)

- **Surge follow-through** (1d % ≥ 5 and shares 5d avg ≥ 3 and news 3d ≥ 1), 30-day 5% above: -38.8% (30 trades).
- **Overextended fall** (5d % ≥ 25 and rsi ≥ 70 and 1d % ≤ 0): -61.5% (10 trades).
- **Oversold with heavy calls:** -27% to -30% in every variant (rsi < 30 with calls 20d ≥ 1.5, > 2 or > 3), 0 of 6 at ATM.
- **Oversold deep off-high**, sub-$10 oversold rebounds, and large down day with call spike: -23% to -24%.
- **Momentum in a down market** (R2 plus market 20d % < 0): -47.8%.
- **Any call rule when market 20d % < 0:** -11% to -16% and worse in second halves.
- **Non-extended stocks in an up market** (market 20d % > 0, 20d % ≤ 20, vs ma20 % ≤ 10), 30-day 5% above: -17.7% (1,167 trades, 1 of 6).
- **Near-high moderate momentum** (off high % ≥ -1.6 and 20d % ≥ 4.6 and 20d % ≤ 14.2), 30-day ATM: **-20.9%** (136 trades, 2 of 6).
  - A trader read this as a "momentum" lead. It is bad.
  - Mild strength does not pay while strong strength does. The cliff appears to sit somewhere around 20d % of 15 to 20.
- **Shares today < 1** (shares < 1), 30-day 5% above: **-18.2%** (868 trades, 1 of 6, both halves about -17% to -20%). Skip these names. This was confirmed on a large n.
- **Heavy 20-day calls with no news** (calls 20d > 2.1 and news 7d < 1), 30-day 5% above: -14.6% (454 trades). Heavy flow needs a strong stock behind it.
- **The traders' 5-day call-flow gates at 30-day ATM** were negative: call days 2x+ of 0 to 1 scored -14.0% (1,110 trades, 2 of 6). That is a mild confirmation that low flow is bad at 30 days. At 90-day ATM low flow scored -6.5%, 4 of 6, so it is no worse than average there.
- **Close vs vwap ≥ 0.2 with call days 2x+ ≥ 2**, 30-day ATM: -12.2% (437 trades). VWAP is not an edge. Mid-price (price $10 to $50) versions are worse (-16.6%).
- **$10 to $50 band:** the worst band at 30-day 5% above (-19.6%) and at every 90-day ATM gate.
- **Gate combinations that pass many trader filters:**
  - Agent 2's core gate (call days 2x+ of 2 to 3, news 7d of 1 to 2, realized vol % < 80): -8.7% (208 trades, 2 of 6).
  - Agent 4's full v7 gate: -9.3% at 5% above (438 trades) and -6.4% at ATM. Adding price $10 to $50 made it -15.5%.
  - Agent 3's calls 2-5, vol20 % < 5.1, realized vol % < 80: -8.8% (827 trades).
  - Multi-condition stacks of weak stock-level signals do not become edges.
- **High realized vol (> 80) and high vol20 (> 5), as exclusions:** neutral at best.
  - Realized vol > 80 at ATM scored -8.7% (505 trades), which is better than its benchmark of -10.9%.
  - High vol20 at 5% above scored -12.5%, equal to its benchmark. Do not rely on vol exclusions.
- **Ratings of any kind:** noise, as every trader concluded. Six bundles, sign flips.
- **14-day expiries; 10%+ out-of-the-money strikes** outside R2, R4, R6 at 10% above, and the sub-$10 huge-call lottery.
- **Exits to rescue bad entries,** single-bundle reads, and "positive median" claims from fewer than 20 trades.
  - The traders' own bundle totals were dominated by one trade. One 14-day, 10% above trade returned +2,596% and produced almost all of one bundle's profit.
- **Using total dollar P&L or the average alone to judge a rule.**
- **Trading sub-$10 names for real money.** Both tails are extreme and the marks are suspect.

---

## 3. WHERE THE TRADERS AGREED AND DISAGREED

**Agreed:**
- The median option trade loses and the averages come from a few outliers.
- The 30-day ATM call has a negative median in every IV band and every iv/realized band.
- Ratings are noise.
- Stock-level edges are small, with call days 2x+ of 2 to 5 as the most replicated.
- No live money, flat size and no adding after wins.
- The valuation and exit-quote audit is the main unresolved data question.
- 14-day expiries are bad, and sub-$10 is risky.

**Disagreed (scorebook verdict):**
- **90-day structures.**
  - Agent 1 found the 90-day 10% above arm did not replicate (median near zero) and dropped the 30-day arms. Agent 4 saw nothing in either.
  - Scorebook: 90-day 10% above is steadier and slightly positive only with the trend plus market gate (R11, R12). Plain call-flow persistence at 90-day 10% above is -6.0%.
- **Strike.**
  - Agent 2 wanted ATM only. Agent 4 saw a +70.9% median at ATM on 6 trades.
  - Scorebook: ATM is better than OTM on median (R8, -25%), but OTM 5% above has the larger averages in momentum rules (R1, R3, R4, R6).
  - The 6-trade ATM median is noise.
- **Market gate.** Agents 2 and 4 dropped market 5d and 20d as "noise" from single-bundle fifths. The scorebook shows it as the cleanest sign flip. Keep it.
- **vs ma50, RSI and over $50.**
  - Agent 4 dropped them. Agent 1 dropped the vs ma50 veto and found the RSI veto reversed.
  - Scorebook: these variables work at strong thresholds combined with an up-market gate. The traders' dropped "extended" vetoes are correctly dropped.
- **Volatility exclusions.** Agents 3 and 4 gated out the top fifth of vol20 and realized vol. The scorebook shows no clear value.
- **Oversold names.** Agent 4 retired "oversold with heavy calls loses". The scorebook says keep avoiding it. Oversold plus quiet calls at 90 days is only a lead.

---

## 4. NEW IDEAS TO TEST

State each as an explicit rule so it can be scored. Require n ≥ 60, report both halves, and compare to the benchmark.

1. **Widen R1-$50 (top priority).**
   - Loosen to reach n ≥ 60 while keeping both halves positive: rsi > 60 or > 65, calls 20d > 1.5, market 5d % > 0 in place of market 20d % > 0, add vs ma50 % > 0, or price over $30.
   - Test the same stocks at ATM and 10% above.
2. **Add the traders' filters to the strong-strength baskets.** Nobody has tested them as add-ons to the strength rules.
   - Add news 7d ≥ 1 (the best-replicated filter) to R4, R6 and R7.
   - Add shares ≥ 1 (the shares < 1 exclusion) to R1, R4 and R6.
3. **Strength ladder and the cliff.**
   - Under a market-up gate, bucket by 20d % (0 to 10, 10 to 20, 20 to 40, 40+) and by vs ma50 %.
   - Mild strength loses (-17.7% non-extended, -20.9% near-high mild momentum) and strong strength pays (R2, R10).
   - Find the threshold and whether there is an upper bound.
4. **Wrapper replacement (untested; all traders hinted at it).** Plain shares have medians near 0 and options -40% to -60%.
   - Test deep in-the-money calls (strike 5% to 10% below price, 60 to 90 days) and bull call spreads on R1, R2, R4 and R6.
   - Success is the first positive median.
5. **Oversold plus quiet calls at long expiry.**
   - Test rsi < 30 and calls 20d < 1.5 at 90-day ATM, 5% and 10% above, with and without the market gate and price over $50.
   - This is the only positive median seen, from 8 trades.
6. **Exit variants for gated baskets.** R1c (double-or-10) works at 10% above. Test it and a 15 or 20 session hold on R1, R1-$50, R2, R4 and R6 at 5% above.
7. **iv/realized inside the strength baskets.** Traders saw richer iv/realized with better 30-day ATM medians in one bundle. The option scorebook has never tested it on gated names. Test iv/realized below 1 and above 1.25 inside R1, R4 and R6.
8. **Sustained-flow measures.** Test long calls 20d, otm calls 20d and call days 2x+ 20d as the flow measure inside overbought and momentum gates.
9. **Break-even-aware selection.** Estimate each candidate's break-even stock move from its own premium, then test whether candidates with large recent 20d % and low premium relative to vol20 are better. This is Agent 4's "signal versus wrapper" test.
10. **Fade the chasers with defined risk (paper only).** Test put debit spreads or bear call spreads on surge follow-through and overextended fall (loosen to 1d % ≥ 3, 5d % ≥ 15 to get n ≥ 60).
11. **Sub-$10 huge-call-volume lottery.** Test calls 20d thresholds of 5, 10 and 20 with trend and market gates, but only after the exit-quote check.
12. **Basket simulation.** Check equal-premium weekly baskets of all Tier 1 passers: the worst week, bid-ask costs, and whether the 6-of-6 record survives removing overlapping names.
13. **Exit-quote audit.** Test how Tier 1 averages change when -100% prints on rising stocks are excluded.

---

## 5. OPEN QUESTIONS

- **Positive median.** Can any call setup have one? The candidates are R1-$50 (-21.5%), R12 (-8.0%), oversold 90-day ATM (-7.8%), and the 8-trade oversold quiet-call cell (+13.2%). Does it require deep in-the-money calls, spreads or shares?
- **Exit marks and expiry counts.**
  - Do the -100% marks on flat or rising stocks reflect real wipeouts or stale marks?
  - Do "30-day" contracts really have about 21 sessions to expiry? Several trades showed 9 to 19.
  - If marks and counts are wrong, medians are overstated in either direction.
- **First half versus second half.** R1 fell from +62.5% to +15.0% and R1b from +27.6% to -2.2%, while R2, R3, R6, R7 and R8 rose. R1-$50 stayed even. Is the R1 fade a regime, a volatility effect, the lower-priced names, or a few weeks?
- **Does the market gate generalize?** The sample is up-market-heavy, and no trader saw a sustained decline. A regime change could reverse the averages.
- **Why do mild strength and near-high momentum lose while strong strength wins?** Is it premium cost relative to move, convexity capture, or something else?
- **Why does 20-day call flow help overbought names but hurt oversold ones, and 5-day flow not help?**
- **Over $50.** Is it a liquidity, low-implied-volatility or size proxy? It helps at 30 days and OTM strikes, but barely at 90-day ATM.
- **Sub-$10 huge call volume.** Is the +39.9% lottery real, or an artifact of stale or optimistic marks?
- **Do the 90-day tail results hold?** Are the +3% to +7% at 90 days with median -8% to -16% an edge net of bid-ask?
- **Do small stock-level edges (+1% to +2% over the universe median) ever matter?** They are well below the +2% to +4% break-even move, so they probably only matter with a wrapper that does not lose on flat stocks.

### How the committee would remake the test (not passed on)

# Redesign proposal

## 1. What blocked us (most limiting first)

1. **Option marks could not be trusted, so no option result was final.**
   - Agent 4: "Impossible-looking -100% marks… Several trades labelled 30-day were 'expired at session 9'." Agent 2: "Exit prices, settlements, and expiry counts are unaudited."
   - Agent 1: "Exit IV and the bid/ask are still missing for most trades… I cannot yet split losses between decay, IV change, and spread."
   - Every trader ended with "audit first" and none could finish it. The scorebook charges no spread and does not audit marks either.
   - The central question was whether the median trade really loses 40-60%. We cannot say whether that is real or a pricing artifact.

2. **Too few trades, too much noise, and too many looks at the data.**
   - Agent 2: "Anything below 30 trades is a lead, not evidence." Agent 4: "standard error… roughly ±15 to 20 points per trade."
   - Each bundle gave about 30-40 trades and roughly 250 candidates. Fifths of that contain about 50 names.
   - Signals flipped sign from bundle to bundle (RSI, vs ma50, iv/realized, shares, calls 5d).
   - The playbook then picked winners from a large scorebook search on the same six bundles. Several rules (R1) already decay from the first half to the second.
   - Nobody can separate a discovered edge from a selected one without a locked holdout.

3. **Feedback was too coarse to test a gate.**
   - Agent 2: "The bundle summary gives fifths, not gate passers." Agent 4: "cannot be reconstructed exactly." Gate compliance "was not recorded."
   - A "test" of a combined rule could not be run. It was planned for three bundles and never done.

4. **One market regime, with the market hidden.**
   - Agent 2: "None of the six bundles tested a sustained market decline."
   - The only clear sign flip (market 20d % > 0) is exactly the thing we cannot validate out of sample. Hidden dates and anonymous tickers also remove earnings, sector and event context.

5. **The wrapper was fixed and always lost.**
   - Calls only, 14 to 90 days, strike at or above the money, and a 10-session exit. Break-even needed +2% to +4% (ATM) while the best stock edges were +1% to +3%.
   - Agent 1: "Path data is still missing." No exit test, structure test or shares comparison could really be run.

6. **The candidates are already screened.** The benchmark is "all candidates", not the market. Signal edges relative to a pre-selected, call-surge universe may not transfer.

## 2. Data to add (ranked)

1. **Full option chain snapshots** at entry and at every day of the hold. For each strike and expiry: bid, ask, last, volume, open interest, IV and delta. Plus actual expiry date and calendar days to expiry. This lets us:
   - fill at bid/ask,
   - audit every mark,
   - split P&L into stock move, IV change, decay and spread,
   - price any structure (spreads, deep ITM) honestly.
2. **Earnings dates** (days to next and since last earnings) and ex-dividend dates. This tests whether the IV crush and large moves are event-driven, and removes the earnings confound from every signal.
3. **Daily OHLC path for each candidate for 20+ sessions after entry**, plus returns at 1/5/10/20/40 sessions. This allows exit tests, stops, MFE/MAE and break-even-hit analysis.
4. **Market and sector context:** SPY/QQQ and sector ETF returns, VIX level and term structure, beta. This allows excess-return scoring, regime splits and a test of whether the market gate is just beta.
5. **Coarse date labels** (year and quarter, or a regime label such as bull, chop or bear) instead of fully hidden dates. Without them we can never learn when rules fail.
6. **IV term structure and skew** (30 vs 90 day, 25-delta put vs call), market cap, average dollar volume and short interest. These bear on cost and liquidity, and on why over $50 helps.
7. **A control universe:** a random sample of liquid optionable stocks with no signal, run through the same pipeline each week.

## 3. Tools and instruments

1. **Wrapper alternatives**, scored on the same entries:
   - Shares (the honest control).
   - Deep ITM calls (delta 0.7-0.85, 60-90 days).
   - Bull call spreads, and put and bear spreads for the "fade the chasers" rules.
   - Calendar and diagonal structures, to cut vega exposure.
2. **Variable holds:** 5, 10, 20 and 40 sessions, with scored stops and take-profits. The scorebook should compute these on the daily path automatically.
3. **A queryable analysis environment.** Traders should be able to:
   - cross-tabulate any combination of columns,
   - score a written rule against a training set on demand,
   - get gate-pass counts, mean, median, week-block bootstrap range, halves and beat-the-benchmark rate, so they stop hand-reading fifths.
4. **A pricing and break-even calculator** that takes entry premium, IV and DTE, and returns required stock move and expected decay.
5. **Realistic fills:** mid minus a fraction of the spread, or the bid/ask crossing, built into every score.

## 4. Changes to the test itself

1. **Scale up the sample and score automatically.**
   - Show all liquid optionable names each week, not about 10 hand-picked trades.
   - Run 100+ weeks, so any rule has n in the hundreds in each half.
   - Score every candidate under every standard structure, instead of relying on the ~35 trades the traders chose to make.
   - Traders choose rules, not trades.
2. **Lock a final holdout.** Use time-ordered train, validation and test periods. The final test period is scored once per generation, never shown, and covers at least one down market. Cap the number of rules a generation may submit, and report a multiple-testing-adjusted result (for example the best rule's rank against rules built from shuffled labels).
3. **Separate the two questions in the scoring.**
   - Stock signal: excess return versus SPY and versus the control universe, at several horizons.
   - Wrapper: option return against shares and against the benchmark option.
   - Always report median, mean, trimmed mean without the top 5 trades, and percent of trades above break-even.
4. **Enforce data hygiene in the scorer.** Reject any trade with fewer than the stated sessions to expiry. Flag -100% marks where the stock closed above the strike. Report results with and without flagged trades.
5. **Fixed pre-registration.** Rules are written with exact

### Agent 1's final notes (not passed on)

# TRADING NOTES: LONG-DATED OPTIONS ON STOCK SIGNALS (after bundle 6 of 6)

## 0. Bottom line

- **Still paper only.** Six bundles, about 222 paper trades. Cumulative paper P&L is roughly -$38,000. No live capital.
- **The 90-day, 10%-above call did not replicate.** Bundle 5 showed a +36.5% median on 5 trades. Bundle 6 gave a median of +0.1% (average -0.9%) on 16 trades. Pooled across both bundles, the arm's median is near zero. It is not promotable.
- **The 30-day structures remain negative.** The 30-day 0% call was -22.9% median on 6 trades. The 30-day 5%-above call has had a negative median in every bundle. The 30-day ATM call has had a negative median in every implied-volatility (IV) and implied/realized band in both bundles 5 and 6. I am dropping the 30-day arms from the primary test.
- **Stock-level signals are weak and unstable.** Only one signal has held in more than two bundles: call-flow persistence (2x+ call volume on 2 or more of the last 5 sessions). Its edge in bundle 6 was about 1 to 2 points over the universe median, which is too small to carry an option structure alone.
- **Valuation and expiry problems are still present.** Several trades in bundle 6 break the entry and settlement rules. Option medians should not be quoted as reliable until the Section 1.5 checks pass.
- **The go/no-go criteria in Section 3 are not met.**

---

## 1. MY CURRENT STRATEGY

### 1.1 What the strategy is trying to do

A long call only makes money if the stock rises by more than the premium paid, plus decay, plus the bid/ask spread, within the hold period. The aim is to find stocks likely to rise by a few percent over 10 sessions, then hold an option that does not need a large move to break even. Short-dated, far-OTM calls need large moves and have failed in every bundle. The 90-day structure loses less to decay, but its break-even move has not been measured reliably yet.

### 1.2 Stock-level entry rules (decide the stock first)

Column names follow the system definitions.

**A. Required: call-flow persistence**
- **call days 2x+ (last 5 sessions) = 2 to 5.**
  - Bundle 6: 2 to 3 days gave +1.4% median (68% up). 3 to 5 days gave +2.4% (66% up). 0 to 1 days gave -1.6% (34% up). The universe median was +0.4%.
  - Bundle 5: 2 to 3 days gave +1.3% (60% up). 0 to 1 days gave -3.2% (28% up). 3 to 5 days gave -0.7%.
  - Bundle 4: 2 to 3 days gave +3.0% (66% up).
  - Bundle 3: 2 days gave +2.8% (74% up).
  - Direction has held in four bundles for 2 to 3 days, and in bundle 6 it also held for 3 to 5 days. Bundle 5's negative 3 to 5 result did not repeat. Confidence in direction: moderate. Confidence in size: low, since the edge over the universe median is roughly 1 to 2 points.
- **Use 2 to 5 days as the entry band.** Do not use 0 to 1 days as a long entry.

**B. Vetoes (revised)**
- **RSI veto: demoted to a soft veto.** Bundle 6 showed RSI 58 to 68 at +0.6% and RSI 68 to 91 at +0.9% (56% up), both above the universe median. Bundle 5 (65 to 88) was -2.4%. Bundle 4's watch band (58 to 68) was -3.0%. Results disagree across bundles, so I will not exclude high-RSI names outright. Log RSI and test it on the next bundle.
- **vs ma50 veto: dropped as a hard veto.** Bundle 6 showed vs ma50 of +12.6% to +84% at +2.2% median (62% up), the best bin. Bundle 5 showed it flat. Bundles 3 and 4 showed it negative. Across four bundles the sign flips. Do not use it.

**C. Tie-breakers (rank candidates that pass A, not gates)**
- **Mild dip below the 20-session average.** Bundle 6 did not confirm it: vs ma20 at -5% to -0.4% gave -0.3% (50% up), and at -0.3% to +2.8% gave +1.4%. Bundle 5 gave +1.2% and bundle 4 gave +2.2% for the dip. Result: mixed. Demoted to a watch item.
- **Off the 60-day high.** Bundle 6: -6.7% to -1.7% gave +0.9%; -1.6% to 0 gave +1.1%; -13.9% to -6.9% gave -0.8%. Weak, not useful.
- **Cheap options (iv/realized below 0.68).** Bundle 6 gave -0.4% (50% up), reversing bundle 5's +1.8%. The top iv/realized bin (above 1.57) gave +1.8%. Dropped as a tie-breaker. Keep logging.
- **Calls 20d (slow sustained buying) between 1.05 and 1.52.** Bundle 6 gave +3.8% median (71% up), the strongest bin in the bundle. It is one bundle and the bin is narrow. Treat as a hypothesis to test, not a rule.
- **News 7d of 1 to 2 articles.** Bundle 6 gave +2.7% (72% up). Bundle 5 gave the same bin a negative result for 2+ articles. Watch only.

**Dropped as rules (no stable sign across bundles):**
- Heavy 5-day call buying (calls 5d avg top fifth): bundle 4 +2.9%, bundle 5 -2.0%. Bundle 6 quintile results were mixed, with 2.39 to 4.4 at +1.0% and 4.41+ at +0.8%.
- Share volume building (shares 5d avg above about 1.7): bundle 4 +3.5%, bundle 5 -2.0%, bundle 6 +0.6% for the top bin.
- Deep pullback (vs ma50 -13% to -4%): bundle 5 -2.3%, bundles 2 to 4 positive, bundle 6 mixed (-0.8% for -9.1% to -1.6%, +1.1% for the lowest bin).

### 1.3 Option structure (paper)

**Primary test arms (both run on the same names, same day, same expiry rule):**
- **Arm 1: 90-day call, strike 10% above entry, held 10 sessions.** The arm the notes previously called primary. Its evidence now points to an unproven, possibly zero median.
- **Arm 2: 90-day call, at-the-money (0% above), held 10 sessions.** Bundle 6 had 4 trades with a +21.3% median and +39.7% average. That is far too few to trust, but it is the only positive option group in bundle 6 and the strike choice is the main variable to test.

**Expiry rules (enforced at entry):**
- 90-day arms: 60 to 90 sessions to expiry at entry. Reject below 60. Bundle 6 had one 90-day trade at 48 sessions. That violates the rule and must be excluded from the medians.
- 30-day arms: removed from the primary test. If kept for reference, 25 to 30 sessions to expiry at entry. Bundle 6 had a 30-day trade at 11 sessions to expiry, which must be excluded.

**Strike and hold:**
- Strikes 0% and 10% above entry for the 90-day arms. Do not use 15% or 20% strikes.
- Hold 10 sessions. Log the 20-session mark as well, for the exit test.
- Exit at mid. Log bid, ask, mid, and exit IV.

**Off list (do not paper trade):**
- 14-day and 30-day expiries (removed from primary, see above).
- Strikes 15% or more above entry (bundle 6: 90-day 15% median -30.1%, 90-day 20% -47.5%).
- Double-or-10 exits.
- Any structure with fewer than 60 sessions to expiry (90-day arms) at entry.

**Sizing:** paper. If ever live: a quarter of normal size, no adding after wins.

### 1.4 Mechanism (hypothesis, not confirmed)

- **Why the 30-day structures fail.** Bundle 6 medians were: 30-day 0% -22.9%, 30-day 10% -50%. Time decay alone does not explain losses of this size over 10 sessions. The likely drivers are a fall in IV after entry and wide bid/ask spreads. Exit IV has not been logged for enough trades to confirm this.
- **Why the 90-day structure might work.** Over 10 sessions, a 60-to-90-session option loses a smaller share of its value to decay, so the stock move matters more. Break-even for the 10%-OTM call probably needs a stock gain of roughly 4% to 8%. The ATM call needs less. This is a hypothesis. Bundle 6's 10%-OTM 90-day trades show a 0.1% median when the stocks' median move was about +0.4%, so the arm is not clearly beating break-even.
- **Implication.** Stock-level filters must find names with a few percent of upside. The option must be chosen so that a few percent is enough. The ATM 90-day arm is a more direct test of that.

### 1.5 Valuation and data rules (must pass before any median is reported)

For every paper trade, log:
1. Entry date, expiry date, sessions to expiry at entry (reject if below the arm's minimum).
2. Entry bid, ask, mid. Entry IV.
3. Exit date, sessions held, exit bid, ask, mid. Exit IV.
4. Stock price at entry and exit. Strike.
5. Settlement check: if expired, value must equal max(stock − strike, 0).

**Automatic flags (re-mark before reporting):**
- Any -100% mark where the stock closed above the strike at the mark date. Bundle 5 had one.
- Any -100% or near-total loss with sessions remaining at mark where the stock fell less than 3%. Bundle 6 had a 30-day ATM trade (paid 2.5%, 28 sessions, stock -2.8%) marked -100% with the call finishing well below its premium. Check against a simple option-pricing calculation at exit IV.
- Any mark of -85% or worse where the stock fell less than 3%, unless exit IV fell sharply.
- Any "30-day" trade expiring at session 9 or 10. The expiry chooser or session counting is still wrong.
- Any gain well above the stock move for a 10%-OTM strike. Bundle 6 has one 90-day 10%-OTM call marked +9.2% with the stock up 0.9%. An OTM call gaining that much on a flat stock needs an IV explanation. Check it.

**Report:** option medians as marked and re-valued at mid, both with and without the flagged trades. Do not compare 30-day and 90-day medians until both are re-valued and expiry-filtered.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### 2.1 Results

- **Option trades:** 31. Profit -$1,388. Average -4.5%, median -9.8%, 35% winners.
- **90-day, 10% above, held 10:** 16 trades, average -0.9%, median +0.1%. Bundle 5's +36.5% median did not replicate. Pooled with bundle 5 (21 trades), the median is near zero.
- **90-day, 0% (ATM), held 10:** 4 trades, average +39.7%, median +21.3%. Too small to read, but it is the only positive option group in this bundle.
- **90-day, 5% above:** 1 trade, -36.1%.
- **90-day, 15% above:** 2 trades, average -30.1%.
- **90-day, 20% above:** 1 trade, -47.5%.
- **30-day, 0% (ATM), held 10:** 6 trades, average -15.0%, median -22.9%.
- **30-day, 10% above:** 1 trade, -50.0%.
- **Universe:** all 250 candidates averaged +2.5% over 10 sessions, median +0.4%. This is a better tape than bundle 5 (median -1.0%) and similar to bundle 4 (median +0.6%).

### 2.2 Option-level findings

- **30-day ATM by IV band:** the median was negative in all five bands. The top band (83.5 to 436) had an average of +36% but a median of -39%, so the average came from a few large winners.
- **30-day ATM by iv/realized:** the median was negative in all five bands (-29% to -59%). Bundle 6 confirms that IV and iv/realized do not rescue the 30-day structure.
- **90-day arms:** the median was near zero for the 10%-OTM strike. The ATM strike had the only positive median, on very few trades.
- **Losses are concentrated in long-dated stocks that rallied or fell far.** Several 90-day 10%-OTM trades lost 50% to 90% while the stock fell 2% to 25%. Others gained over 100% with stock gains of 8% to 20%. Dispersion is very wide relative to the stock move.

### 2.3 Stock-level findings

- **Call days 2x+ in last 5 (2 to 3):** +1.4% (68% up). Held.
- **Call days 2x+ in last 5 (3 to 5):** +2.4% (66% up). Held, and reversed bundle 5's negative.
- **Call days 2x+ in last 5 (0 to 1):** -1.6% (34% up). Held as a negative.
- **Calls 20d between 1.05 and 1.52:** +3.8% (71% up). New, one bundle.
- **RSI 58 and above:** +0.6% to +0.9%. The RSI veto did not replicate. Demoted.
- **vs ma50 above +12.6%:** +2.2% (62% up). The extended-name veto reversed. Dropped.
- **Mild dip (vs ma20 -5% to -0.4%):** -0.3% (50% up). Did not replicate.
- **Low iv/realized (below 0.68):** -0.4%. Did not replicate bundle 5.
- **Close vs VWAP above 0.78%:** +2.2% (66% up). Buyers paying up into the close. New, one bundle.
- **Market 5d between +2.4% and +5.7%:** +1.9% (68% up). Market context, not a stock signal.
- **News 7d (1 to 2 articles):** +2.7% (72% up). Watch.
- **Ratings:** rated -1 had the most names (106) with a +4.5% average but only a +0.4% median. Ratings do not separate winners from losers on median. Keep logging, do not use.

### 2.4 Valuation and settlement problems found

- One 30-day ATM trade was entered with 11 sessions to expiry, which breaks the 25-session minimum. Exclude it from the medians.
- One 90-day trade was entered with 48 sessions to expiry, which breaks the 60-session minimum. Exclude it.
- One 30-day ATM trade was marked -100% with 28 sessions to expiry and a 2.8% stock drop. It needs re-marking before it counts.
- One 90-day 10%-OTM trade was marked +9.2% with the stock up only 0.9%. It needs an IV explanation before it counts.
- Exit IV and the bid/ask are still missing for most trades. This is the main gap. I cannot yet split losses between decay, IV change, and spread.

### 2.5 What I did not do

- I did not run a clean paired test (90-day ATM and 90-day 10%-OTM on the same names, same day). This bundle has the two strikes on different names, so the comparison is confounded.
- I did not test the time-stop (10 vs 20 sessions) or any take-profit rule. Path data is still missing.

---

## 3. WHAT I WILL TRY NEXT (bundle 7)

Priority order. Nothing moves toward live capital until both a stock-level signal and an option-level median pass.

1. **Fix valuation and expiry (mandatory, before any median is reported).**
   - Apply every check in Section 1.5 to every trade.
   - Reject 90-day entries under 60 sessions and 30-day entries under 25 sessions.
   - Re-mark any trade the flags catch. Report medians with and without flagged trades.

2. **Paired structure test on the same names, same day.** For every name that passes entry rule A, paper-trade:
   - the 90-day ATM call (0% above), and
   - the 90-day call 10% above entry.
   Hold 10 sessions. Log exit IV, bid, ask, and the 20-session mark. This replaces the 30-day comparison arm.

3. **Stock-level test against the bundle's universe median.** Measure:
   - Call days 2x+ in last 5 at 2 to 3 versus 4 to 5, versus 0 to 1.
   - RSI at or above 68 versus below 58, to decide whether the RSI veto is dead.
   - Calls 20d between 1.05 and 1.52 (new), as a tie-breaker test.
   - Close vs VWAP above 0.78%, as a tie-breaker test.
   Combined test: call days 2x+ at 2 to 5, with no hard veto. Promote a combined rule only if it beats the bundle's universe median by at least 1.5 points on at least 25 names, with a positive median.

4. **Required for any 90-day arm to be promoted.** A positive median on at least 20 trades per bundle for two bundles, after valuation checks. Record the stock move at exit so the break-even move can be measured directly.

5. **Exit test.** Compare a 10-session time stop with a 20-session hold on the 90-day ATM arm. Add a take-profit rule (for example +50%) only if path data is available.

6. **Ratings: keep logging, do not test as a signal** unless a third bundle shows a stable median inversion.

7. **Keep off:** 14-day and 30-day expiries (removed from primary), strikes 15% or more above entry, double-or-10 exits, and any 90-day structure under 60 sessions at entry.

**Go/no-go for any live capital (unchanged):**
- An option-level median above zero, on at least 40 paper trades across at least two bundles, for the 90-day arm, after valuation fixes and expiry checks.
- The stock-level combined signal beats the universe median by at least 1.5 points in at least two bundles.
- Both conditions met. Until then, no live capital.

**Current status against the criteria:** neither condition is met. The 90-day 10%-OTM arm has 21 pooled trades with a near-zero median. The call-flow signal beats the universe median by about 1 to 2 points in bundles 4, 5, and 6, but not by 1.5 points in every bundle.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### 4.1 Held up across bundles

- **Call-flow persistence (2 or more of the last 5 sessions with 2x+ call volume).** Positive in bundles 3, 4, 5, and 6. Bundle 6 also extended the result to 3 to 5 days. Moderate confidence in direction, low in size.
- **Low call-flow (0 to 1 days) as a negative.** Negative in bundles 5 and 6. Moderate confidence.
- **30-day call structures (5%-OTM, 10%-OTM, ATM): negative median in every bundle tested.** High confidence that these, as traded, have no positive median. Retired from primary testing.
- **Small size and no adding after wins.** High confidence. Limits damage regardless of edge.

### 4.2 Conflicting or failed

- **RSI veto (65 and above).** Negative in bundles 2, 4, and 5. Positive in bundle 6. Demoted to a soft veto pending bundle 7.
- **Extended above ma50 (+12% and above) as a veto.** Negative in bundles 3 and 4, flat in bundle 5, positive in bundle 6. Dropped.
- **Mild dip below short-term averages.** Positive in bundles 4 and 5, flat in bundle 6. Watch only.
- **Deep pullback (vs ma50 at or below about -10%).** Positive in bundles 2, 3, and 4, negative in bundle 5, mixed in bundle 6. Do not use as a filter.
- **Cheap options (iv/realized below 0.68).** Positive in bundle 5 (+1.8%), flat or negative in bundle 6 (-0.4%). Dropped as a rule.
- **Heavy 5-day call buying and share volume building.** Positive in bundle 4, negative in bundle 5, mixed in bundle 6. Dropped as rules.
- **IV as a return predictor.** Bundles 2 and 3 suggested lower IV was better. Bundles 4, 5, and 6 did not confirm. IV is a risk note only: log it, and review the 90-day arm at high IV.
- **The 90-day, 10%-OTM arm.** Bundle 5 showed +36.5% median on 5 trades. Bundle 6 showed +0.1% on 16 trades. The bundle-5 result did not replicate. Pooled, it is near zero. Kept as the comparison arm in the paired test, not as a promoted structure.
- **News and news tone.** Bundle 4 strongly positive, bundle 5 positive at 7 days of 0 to 1 articles but negative at 2+, bundle 6 positive at 1 to 2 articles. Watch only. The zero-news bins contain many ties and are not usable.
- **Ratings.** The mean and median by rating disagree in every bundle. Not a signal.

### 4.3 New observations from bundle 6 (one bundle only)

- **Calls 20d between 1.05 and 1.52 (sustained slow call buying):** +3.8% median, 71% up. Test again.
- **Close vs VWAP above 0.78%:** +2.2% median, 66% up. Test again.
- **The strongest option results came from names with large stock gains,** not from any stock-level filter. Option medians in this bundle were driven by the stock move dispersion, which the entry rules did not predict.

### Agent 2's final notes (not passed on)

# TRADING NOTES: FINAL (after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Status: paper only. No live trades.** Over six bundles I have found no stock-level rule that clearly beats its control, and no option structure with a positive median. Bundle 6 lost $2,960 across 37 trades (average -8.0%, median -15.5%, 35% winners). Bundle 5 lost $8,343. Bundle 4 was positive, but its average came from a handful of large winners. The option wrapper is not yet shown to add value over holding the stock.

### 1a. Bottom line

- **The ATM 30-day call held 10 sessions has a negative median in every IV band and every IV/realized band across the full bundle-6 candidate table, not just my trades.** Bundle 6's option-level medians were -38%, -37%, -21%, -30%, and -39% across the five IV bands, and -59%, -29%, -40%, -15%, and -17% across the five IV/realized bands. Combined with bundles 3–5, that is a consistent drag on the median.
- **Stock direction sets almost every option result.** In bundle 6, every 30-day ATM trade where the stock fell 3% or more lost 65–100%. Trades where the stock rose 4.5% or more were positive in most cases (+23% to +160%). The break-even stock move for this structure is about **+2% to +4%**, higher than the +0% to +1% I used early on. The exact level is not pinned down; bundle 6 has no clean trades between +2% and +4%.
- **Large wins are real but rare and not selectable.** A few stocks that rose 8–11% after entry drove the averages. I cannot pick those names reliably, so the median is the number to watch.
- **Even when the stock rises, the option can lose.** Flat-to-slightly-positive stocks lost in every bundle. The premium decays while the stock sits still.
- **The stock-level edge is small.** Bundle 6's full field had a median of +0.4% and an average of +2.5% over 10 sessions. An ATM 30-day call needs more than that to break even, so most gated names will still lose on the option.

### 1b. Entry gate (paper, version 6)

Every condition is checked on the entry day. The gate is a hypothesis under test, not an established rule.

1. **Call days 2x+ (last 5 sessions) is 2 or 3.** This is the most replicated stock-level signal. The 0–1 bucket has been negative in every bundle where I tested it (bundle 6: 0 days -0.8%, 1 day -1.6% with 34% up; bundle 5: -3.2%; bundles 2–4 also negative). The 2–3 bucket was positive in bundles 2–6 (bundle 6: +1.4%, 68% up; bundle 5: +1.3%, 60%; bundle 4: +3.0%). The 3–5 bucket was positive in bundle 6 (+2.4%, 66%) and bundle 4 (+3.5%) but negative in bundle 5 (-0.7%). Keep 2–3 as the gate. Log 4–5 as a paper arm.
2. **News in the last 7 sessions is 1 or 2 articles (preferred), and news 3d is 1 or more.** Bundle 6 showed +2.7% (72% up) for 1–2 articles over 7 days, versus +0.6% for 0–1 and +1.8% for 2+. Bundle 5 showed the one-article bucket was strongest. News present at any count was positive in bundle 4. The "heavy news is bad" split from bundle 5 was **not** replicated in bundle 6: the top 3-day news fifth (1–22 articles) returned +3.5% (68% up). Heavy news is no longer excluded from the gate. Zero news in 3 days stays on the paper arm only, because its buckets are tie-heavy and inconsistent.
3. **Lead, not gate: close vs vwap above 0.** Bundle 6 showed a clean slope: the top fifth (close at least +0.78% above today's VWAP) returned +2.2% (66% up); the 0.22–0.77 fifth returned +1.0%; negative values were flat or negative. One bundle only. Record it and test it as an added condition on the next bundle.
4. **Lead, not gate: near the 60-day high.** Bundles 5 and 6 both showed the same direction: within about 1.6% of the 60-day high was +1.1% (bundle 6), and deep pullbacks were -0.1% to -0.8% in bundle 6 and -2.9% to -4.6% in bundle 5. The slope is gentle in bundle 6. Confidence low to moderate.
5. **Lead, not gate: avoid high realized and volume volatility.** Realized vol above about 80% and vol20 above about 5% were the worst bands in bundle 6 (-3.2%, 46% up in both). Bundle 5 showed the same direction for vol20 above 3.8. Bundle 4 showed the opposite in the middle range. Use as an exclusion on paper only.

**Excluded (paper):** call days 2x+ of 0 or 1; news 3d of 0; realized vol above 80.

**Dropped as gates after bundle 6:**
- **vs ma50 cap at +5.5:** contradicted. Bundle 6 showed +1.4% (62% up) for 4.6–12.4% above the 50-day, and +2.2% (62% up) above 12.6%. Dropped.
- **20d cap at +5:** contradicted. Bundle 6 showed +1.5% for 4.6–14.2%, and +1.3% above 14.6%. Dropped.
- **RSI below 53:** reversed. Bundle 6 showed a monotone increase in median return with RSI, from -0.1% (RSI 8–36) to +0.9% (68–91). Bundle 5 showed the opposite. Dropped.
- **iv/realized below 0.7:** reversed. Bundle 6's lowest iv/realized fifth was -0.4% (50% up). Dropped as a lead.
- **Heavy-news exclusion (3+ articles):** contradicted. Dropped.

**Gate status:** I still cannot score the gate as a whole against an ungated control. The bundle summary gives fifths, not gate passers, and the fifths do not align with the gate thresholds. I have no gate-level control result. Trade-level gate compliance was not recorded in bundles 3–6, so trade results cannot be attributed to the gate.

### 1c. Instrument, expiry, strike, and exit (paper)

- **Instrument:** 30-day call, at-the-money (ATM), held exactly 10 sessions.
- **Exit:** time-based at session 10. No stops, no profit targets, no adds, no double-or-10.
- **Sizing:** one fixed minimum unit per signal. Never size up after a win.
- **Strike:** ATM. Across bundles 4–6, ATM beat 5%, 10%, and 20% above on median in each bundle. Bundle 6 medians: 5% above was -77.3% (one trade), 10% above -24.3% (one trade), 15% above +69.6% (one trade). The sample is too small to call this a reversal.
- **Expiry:** 30-day on paper. The 14-day and 90-day trades in bundle 5 were negative. The 90-day trade in bundle 6 was +1.1%, on two trades, which is not enough to change the plan.
- **Benchmark:** every paper trade records the stock's 10-session return next to the option return. The option must beat the shares result to justify the wrapper.

### 1d. Do not trade

- Any live trade. Paper only, until the audit in section 3 is complete and a gated arm beats its control on stock returns in two consecutive bundles.
- Expiries other than 30-day on the core arm (45–60 day is paper-only).
- Double-or-10 exit.
- Strikes other than ATM.
- Ungated names. Every paper trade must pass the gate and be logged with its values.
- Sub-$10 names with IV above about 150%. These produced some extreme outliers and many large losses.
- Ratings of any kind.

### 1e. Reasoning

- **Stock selection and the wrapper are separate problems.** The gate has to pick stocks that rise, and the option then needs the stock to move roughly +2% to +4% to break even. Bundle 6's field median was +0.4%, so most gated names will still lose on the option.
- **The wrapper is the dominant loss.** Across bundles 3–6, the ATM 30-day median has been negative in every IV band and every IV/realized band. Premium is paid up front and decays. On flat or down stocks, the option goes to near zero.
- **The shares arm is the honest control.** If a gated stock's 10-session return is not clearly positive, the option cannot be. The option must beat shares to justify its cost.
- **The stock-level signals are weak.** Call days 2x+ of 2–3 is the one signal with a stable positive result, and its median edge over the field is about +1% to +1.5%, which is smaller than the option's break-even move.

---

## 2. WHAT I TESTED IN THIS BUNDLE AND HOW IT WENT

### My trades (bundle 6)

- **Result:** 37 trades, -$2,960, average -8.0%, median -15.5%, 35% winners.
- **30-day ATM, hold 10:** 31 trades, average -6.7%, median -15.5%.
- **Other structures (1–2 trades each):** 30-day 5% above -77.3%; 30-day 10% above -24.3%; 30-day 15% above +69.6%; 90-day ATM +1.1%; 90-day 5% above -57.4%. Too few to read.
- **Stock move versus option result (30-day ATM):**
  - Stocks down 3% or more: every trade lost 65–100%.
  - Stocks between about -2% and +2%: mostly losses, including one trade at +1.9% that is marked -100% (see audit).
  - Stocks up 4.5% to 11%: winners in nearly every case (+23% to +160%). One stock up 5.5% returned only +22.9%.
  - Read as a rule of thumb: the option needs a clear move up, not just a small one.
- **Entry premium:** paid between about 1% and 9% of the price. Trades with the largest premiums (7–9%) were mostly losers on flat or down stocks.

### Stock-level results (250 candidates)

- **Overall:** median +0.4%, average +2.5%. Bundle 5 was -1.0% median, so this bundle was stronger for the field.
- **Ratings:** rated -1 averaged +4.1% (median +0.5%) across 130 stocks; rated +1 averaged +0.2%; rated 0 averaged +0.8%. No stable ordering; this is consistent with dropping ratings.
- **Call days 2x+ (5 sessions):** 0 days -0.8% (48% up); 1 day -1.6% (34%); 2 days ~0% (region 1–2 at -0.7%); 2–3 days +1.4% (68% up); 3–5 days +2.4% (66%). The 2–3 gate held; the 3–5 range was positive here.
- **News 3d:** the top fifth (1–22 articles) returned +3.5% (68% up). The lower fifths were tie-heavy and noisy. The "heavy news hurts" split did not replicate.
- **News 7d:** 1–2 articles +2.7% (72% up); 2–27 articles +1.8% (60%); 0–1 +0.6% (56%).
- **Close vs vwap:** monotone. Top fifth (0.78% and above) +2.2% (66% up); bottom fifths negative.
- **Off high:** near the high (-1.6% to 0) +1.1% (61% up); deeper pullbacks were flat to negative.
- **iv/realized:** bottom fifth -0.4% (50% up); top fifth +1.8% (59% up). Opposite of bundle 5.
- **Calls 20d (slow, sustained buying):** the 1.05–1.52 band returned +3.8% (71% up), the best bucket in the bundle. Other bands were flat to mildly negative. One bundle; treat as a lead.
- **Realized vol (top fifth, 81.6% and above):** -3.2% (46% up). Volume-volatility (vol20 top fifth) was -3.2% (46% up). Consistent with bundle 5 for the top band.
- **Shares 5d avg:** 1.25–1.68 +2.1% (62% up); above 1.7 +0.6%. Not clean enough to use.
- **Puts 5d avg:** top fifth (6.2 and above) +1.7% (68% up). Weak lead.
- **Market 5d and 20d:** noise, as before.

### Option-level results (ATM 30-day, hold 10, full candidate table)

- **By IV:** median negative in every band: 4.8–27% (-38%); 27.5–40% (-37%); 40–57.6% (-21%); 57.6–83% (-30%); 83.5–436% (-39%). Averages were mixed because of outliers.
- **By IV/realized:** median negative in every band: 0.17–0.68 (-59%); 0.68–0.95 (-29%); 0.95–1.25 (-40%); 1.25–1.57 (-15%); 1.57–3.43 (-17%). The highest average (+47%) came from the most expensive-IV band, but its median was still negative.

### Settlement and data audit (new issues)

- **Trades marked -100% with the stock up.** One ATM 30-day trade with the stock up 1.9%, paid 1.6% of price, and 14 sessions to expiry is marked -100%. An ATM call on a rising stock should not expire worthless. This is either a data error or a settlement error. It is the second bundle in a row with a suspect -100% on a rising stock (see bundle 5).
- **Sessions to expiry look inconsistent.** Several 30-day ATM trades show 11, 14, or 19 sessions to expiry at entry. A 30-day calendar expiry is about 21 sessions. Either the expiry count is wrong or the field means something other than days remaining at entry.
- **Entry premiums look low for the stated IV.** Several trades show premiums of 1.1–1.8% of price with IV of 18–25% over 30 days. That is below a standard at-the-money estimate for those IVs. Confirm the premium source.
- **Exit prices are still unverified.** The audit from bundle 5 was not run, so the -100% marks cannot be trusted until it is.

---

## 3. WHAT I WILL TRY NEXT

Bundle 6 is the last bundle in this run. Priorities for any further work, in order:

1. **Option and settlement audit (blocking).** Before any further option result is used:
   - Re-verify every exit price against a real quote or settlement value, with a focus on trades marked -100% while the stock is flat or up (including the +1.9% trade in bundle 6 and the 5%-above trade in bundle 5).
   - Reconcile sessions-to-expiry against the calendar expiry for every 30-day trade.
   - Confirm the entry premium source and check the premium-to-IV relationship.
   - Split each loss into IV change, stock move, time decay, and spread.
   - Log entry and exit premium as a percent of price, and entry and exit IV.
2. **Gate versus control on stocks (highest priority for any new bundle).** Score the gate (call days 2x+ of 2–3; news 7d of 1–2 or news 3d of 1+; close vs vwap above 0; realized vol below 80) against an ungated control on the same candidates. The gate passes only if its stock median beats the control and is positive in both halves of the bundle (by entry order). Log every candidate, including losers. This test has now been planned across three bundles and has not been run as a clean control.
3. **Break-even test.** For every ATM entry, record the stock's 10-session return. Test whether trades at +2% or more are positive and trades below +1% are negative. Bundle 6 suggests the break-even sits between about +2% and +4%, so the test should use that range.
4. **Lead tests to add to the gate (one bundle each so far):** close vs vwap above 0; calls 20d between 1.05 and 1.52; off-high within 7%.
5. **Expiry test (paper).** Test 45–60 day expiries on the same passers, to see whether flat-stock losses shrink with less decay. Paper only.
6. **Shares control.** Continue recording the shares return next to every option trade. If the shares return is not positive on the gated names, the option cannot add value.
7. **Strike.** Keep ATM. Stop testing strikes above ATM unless a new bundle shows the reverse.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Held up (with confidence)

- **Stock direction predicts option sign.** Bundles 3–6: stocks down 3% or more lost on essentially every 30-day ATM trade. Confidence: high.
- **The ATM 30-day median is negative in every IV and IV/realized band.** Bundles 3–6, including the full bundle-6 candidate table. Confidence: high that the wrapper is a drag on the median.
- **Call days 2x+ of 0–1 is weak.** Negative in bundles 2, 3, 4, 5, and 6. Confidence: moderate to high.
- **Call days 2x+ of 2–3 is positive.** Positive in bundles 2, 3, 4, 5, and 6 (bundle 6 +1.4%, 68% up). Confidence: moderate to high. Upper end (3–5) mixed.
- **ATM beats OTM strikes on median.** Bundles 4, 5, and 6 at least directionally. Bundle 3 is the exception (n=4). Confidence: moderate.

### New or partially replicated (lead, not yet a rule)

- **News in the last 7 days of 1–2 articles.** Bundle 6 +2.7% (72% up); bundle 5 one-article bucket strongest; bundle 4 news present positive. Confidence: low to moderate.
- **Close vs vwap above 0.** Bundle 6 only, clean monotone slope. Confidence: low.
- **Near the 60-day high.** Bundles 5 and 6, same direction, different magnitude. Confidence: low to moderate.
- **Calls 20d between 1.05 and 1.52.** Bundle 6 only, +3.8% (71% up). Confidence: low.
- **Realized vol above 80 and vol20 above 5 as exclusions.** Bundles 5 and 6 both negative in the top band; bundle 4 contrary in the middle range. Confidence: low.

### Weakened or contradicted

- **Heavy news is bad (3+ articles).** Bundle 5 said so; bundle 6 said +3.5% for 1–22 articles. Dropped.
- **vs ma50 cap at +5.5.** Bundle 4 said weak; bundle 5 said about 0%; bundle 6 said +1.4% to +2.2%. Dropped.
- **20d cap at +5.** Bundle 6 said +1.3% to +1.5% above +4.6. Dropped.
- **RSI below 53.** Bundle 5 said better; bundle 6 said worse. Dropped.
- **iv/realized below 0.7.** Bundle 5 said +1.8%; bundle 6 said -0.4%. Dropped.
- **Shares 5d avg above 1.64.** Bundle 4 +3.5%, bundle 5 -2.0%, bundle 6 +0.6% (above 1.7). Dropped.
- **Calls 5d avg above 4.2.** Bundle 4 +2.9%, bundle 5 -2.0%. Dropped.
- **Long calls 20d 0.15–1.16.** Bundle 4 +4.5%, bundle 5 -1.0%. Dropped.
- **Deep below the 50-day as a positive.** Bundle 4 +3.7%, bundle 5 -2.3%. Dropped.
- **Calls ratio band 0.65–1.6.** Bundle 3 +2.4%; bundles 4 and 5 did not replicate. Dropped.
- **Big up days as a loser.** Bundle 3 negative; bundle 4 +1.5%. Dropped.
- **Ratings.** Bundle 2: rated -2 led. Bundle 3: rated -2 trailed. Bundle 4: rated -1 led. Bundle 5: rated -1 was -0.6%. Bundle 6: rated -1 was +4.1% average, +0.5% median. No stable ordering. Dropped.
- **Market 5d and 20d.** Noise across bundles. Dropped.
- **IV bands at the stock level.** No stock-level signal. Option-level medians negative in all bands. IV is still recorded because it sets the premium.

### Dropped

- Ratings, in any form.
- Double-or-10 exit.
- 14-day expiry (live and paper).
- Sub-$10 high-IV names.
- Premium ratio as a gate (log only).
- Calls ratio, calls 5d avg, long calls, shares, RSI, iv/realized, vs ma50 and 20d caps as gates.
- Puts-to-calls as a gate (non-monotone).
- Market-regime rules (noise).

### Honest limits

- **Six bundles, about 180 trades total, and most buckets have fewer than 50 candidates.** Anything below 30 trades is a lead, not evidence.
- **The gate has not been tested as a whole against a control.** Each piece was measured alone, and the bundle summaries are too coarse to score the combination.
- **Trade-level gate compliance was not recorded** in bundles 3–6. Trade results cannot be attributed to the gate.
- **Exit prices, settlements, and expiry counts are unaudited.** At least two trades in bundles 5 and 6 (a -100% with the stock up, and a session-count mismatch) look wrong. The true size of the wrapper's loss is uncertain until the audit is done.
- **Bid-ask spreads and fill quality are not charged.** Real results will be worse, especially on low-volume and high-IV names.
- **Stock-level edge is small.** The best buckets show about +1% to +3.5% median. The option needs about +2% to +4% to break even, so most gated trades will lose even when the stock rises a little.
- **Positive averages come from a few large winners.** The median trade has been a large loss in each of bundles 4–6.
- **Market regime.** None of the six bundles tested a sustained market decline. A falling-market regime could change every rule here.
- **Conclusion:** after six bundles, the evidence does not support live trading. The stock-level signals are worth carrying forward as paper leads, and the option wrapper needs to be fixed or dropped before it is considered again.

### Agent 3's final notes (not passed on)

# Working Notes: Call Buying on the Signal Screen (Version 6)

*Evidence base: six bundles (about 1,500 candidates, 222 paper trades). Nothing is validated. Each rule is a hypothesis with a stated confidence. Bundle 6 was a fresh sample used for out-of-sample checks. Bundles 4 to 6 are the core evidence for the rules below.*

---

## 1. MY CURRENT STRATEGY

### 1a. Bottom line
- **No option structure has a validated positive median return.** The 30-day at-the-money (ATM) call held 10 sessions is still negative in every bundle where it was run at scale: B4 -15% (10 trades), B5 -38.5% (24 trades), B6 -13.2% (27 trades). The median improved in B6, but the median is still negative.
- **Bundle 6's +$25,435 is not evidence of an edge.** One trade (a 14-session, 10%-OTM call, +2,596%) produced most of the total. Across the 41 trades, the average return is +62%. Remove that single trade and the average falls to about -1% (40 trades). The trade itself broke three of my rules: 11 sessions to expiry (minimum is 20), a 10% OTM strike (ATM is preferred), and a 14-day expiry (the table is for 30 days). Log it as an outlier, not a validation.
- **Default action: no trade.** A bundle with no passing stock-level candidates is a valid result.
- **Paper trade only.** Live capital requires a positive median option return over at least 30 pre-screened trades that meet all the screen rules, replicated on a fresh bundle.
- **Process rule:** run the stock-level screen on the bundle's full candidate table before any entry. Stock-level screens run first, option structure second. Any trade that fails a hard exclusion is not counted toward the test, even if it wins.

### 1b. Why the option wrapper loses (the mechanism I now work from)
- **The stock has to move more than I first assumed.** My earlier breakeven estimate was +1.5% to +2% in the stock over 10 sessions. B6 trades suggest the real figure is closer to +3% to +4%. Every positive ATM hold-10 trade in B6 had the stock up about +3.3% to +16.9% over the hold. Most losing trades had the stock flat or down. The gap between my estimate and the observed threshold may come from bid/ask spread and exit marks (see the exit audit below).
- **The stock universe median is too low.** All 250 B6 candidates averaged +2.5% over 10 sessions but had a median of only +0.4%. An ATM call needs a stock median of roughly +3% or more to have a median return near zero. The screen has to lift the stock median well above the universe median.
- **Premium is small, so costs matter.** Entries cost 1% to 6% of the stock price. A 1% to 2% bid/ask spread at entry and exit is a large share of that premium. Losses of -80% to -100% on trades where the stock fell only 3% to 5% (B6) do not fit a simple delta-and-theta model. They may reflect stale marks or wide exit spreads.
- **Implied vol did not separate option outcomes** in B5 or B6. The 30-day ATM hold-10 median was negative in every IV band in B6 (-21% to -39%).

### 1c. Stock-level screen (entry candidates)
Entries require the core rules below. Each rule is listed with its status. Stock-level results are medians against the universe median for that bundle, and only the replicated rules are used to build the entry set.

**Core rules (replicated in two or more bundles, same direction):**

| Rule | Threshold | Evidence | Confidence |
|---|---|---|---|
| **Call days 2x+ in last 5 sessions** | Must be 2 to 5 (not 0 or 1) | 0–1 bin negative in B4 (-2.1% to -2.7%), B5 (-1.4% to -3.2%), B6 (-1.6%, 34% up). 2–3 bin positive in all three: B4 +3.0% (66% up), B5 +1.3% (60%), B6 +1.4% (68%). 3–5 bin in B6 +2.4% (66% up). | **Medium-high** that 0–1 names are poor. **Medium** that 2–5 names beat the universe; B6 margin over the universe median (+1.0) was below the 2-point pass threshold. |
| **Exactly 1 news article in 7 days** | news 7d = 1 | B4 +8.3% (70% up), B5 +7.8% (80% up). B6 did not isolate the exact-1 bin. The B6 bin 1 to 2 articles was +2.7% (72% up), +2.3 over the universe median (0.4%). | **Medium.** Strongest replicated stock-level signal, but B6 only supports it through the wider 1-to-2 band. Next bundle must report exact-1 separately. |
| **High-volatility exclusion, top fifth of vol20** | Exclude vol20 above about 5.1% | Negative in B2, B3, B5, and B6 (B6 top fifth -3.2%, 46% up). B4 contrary. | **Medium.** |
| **High realized-volatility exclusion, top fifth** | Exclude realized vol above about 80% | B6 top fifth -3.2% (46% up). B5 realized vol 43 to 84 was negative. B2 and B3 also negative. B4 contrary. | **Medium.** Threshold differs by bundle; the top fifth is the most consistent cut. |

**Tags (keep logging, do not gate on yet):**

| Tag | Evidence | Confidence |
|---|---|---|
| **Close at or above VWAP** (close vs vwap % ≥ +0.2) | **New in B6, exploratory.** Monotone across bins: bottom two negative (-1.0%, -0.4%, -0.6%); +0.2 to +0.8 bin +1.0% (62% up); above +0.8 bin +2.2% (66% up). Top bin +1.8 over universe median, just short of the 2-point rule. | **Low.** One bundle. Candidate for B7 test. |
| **Within 15% of 60-day high** (off high % ≥ -15) | B4 at high +0.5%. B5 negative beyond -15%. B6: -1.6% to 0 bin +1.1% (61% up), -6.7% to -1.7% +0.9% (57%), -13.9% to -6.9% -0.8%, beyond -14% -0.1% to -0.3%. | **Low-medium.** Direction consistent, effect small. Use as an exclusion candidate for names more than 15% below the high. |
| **Shares ratio elevated, 1.2 to 1.8** | B6 shares today 1.28–1.78 +1.9% (60% up); shares 5d avg 1.25–1.68 +2.1% (62% up). B5 shares 0.95–1.27 +1.9%. | **Low.** Two bundles, different bins. Test explicitly in B7. |
| **Slow call buying, calls 20d 1.05 to 1.52** | B6 +3.8% (71% up, best bin in B6). B4 1.1 to 2.1 +2.8%. B5 1.14 to 1.6 -1.0% (reversed). | **Low.** Two of three bundles positive. Keep as a tag. |
| **RSI** | B6 small monotone rise (8–36 -0.1%; 68–91 +0.9%). | **Low.** Not a gate. |

**Dropped or contrary:**

| Rule | Why dropped |
|---|---|
| Deep pullback below ma50 | B4 +3.7%, B5 -2.6%, B6 +1.1% (-69% to -9% bin, 59% up); no consistent direction. |
| Positive news tone as a gate | B5 top tone bin +1.4%; B6 tone 0 to 0.2 +4.4% but the adjacent bin was -0.8%. Unstable. Log as a tag. |
| Calls 5d avg above 4.5 | B5 -2.0% (reversed vs B4 +2.9%). B6 bins +1.5% (0.93–1.53) and -1.1% (1.54–2.37). |
| Put/call ratio | B6: highest fifth -0.7% (48% up), second-highest +0.5%. No edge. |
| Ratings (+2 to -2) | Unusable. B6 medians: +2 +9.0% (n=5), +1 +1.6%, 0 -0.5%, -1 +0.2%, -2 -2.0%. Non-monotone in every bundle. |
| Off-high tag as a gate | Only small effects. See above. |
| 5-day drop of 7% or more | B5 -4.2% (36% up), B4 negative. B6 lowest 5-day fifth (≤ -3.3%) only -0.8%. Weak; keep as a low-confidence exclusion, not a rule. |

**Pre-registered pass rule (for any new bin, run before any entry):**
- At least 40 names in the passing set.
- Median exceeds the all-candidate median by at least **2.0 percentage points**.
- At least 55% of names rose.
- Same sign relative to the all-candidate median in at least one earlier bundle (B4 or B5 or B6, whichever is not the new one).
- Components must pass individually before any combination is tested.

### 1d. Instrument, structure, and exit (paper)
- **Calls only.** No puts.
- **Expiry about 30 calendar days, at least 20 sessions left at entry.** Trades with fewer than 20 sessions are excluded. B6's 11-session trade was a violation and is not counted.
- **Strike: ATM (0%) is primary.** ATM hold-10 median was -15% (B4), -38.5% (B5), and -13.2% (B6). The 5% OTM hold-10 showed +40% (2 trades) in B6 but was -55% in B5 (4 trades). Confidence that ATM beats OTM on median: **medium-low**. Log 5% OTM on the same entries.
- **10% OTM: paper only, not in primary set.** B6 -72% (2 trades), B5 -91% (1 trade), and the outlier +2,596% (1 trade, rule-violating).
- **Hold 10 sessions is primary.** Double-or-10 was negative in B6 (3 trades, median -45.7%; other single trades -70% and -63%) and mixed in earlier bundles. Keep it logged, not used.
- **90-day structures: paper only.** B5 6 trades, median about -45%. B6 2 trades at 5% OTM averaged +24.8%, 2 trades at 10% OTM averaged -66.9%. Pooled, negative and too small to judge.
- **No hold to expiry.** Any trade settled or expired early needs an exit-quote audit before its result counts.

### 1e. Hard exclusions (risk and cost controls)
- **Sub-$10 price.** Fills both tails in every bundle. Excluded from real money. No evidence of positive expectancy.
- **Fewer than 20 sessions to expiry at entry.**
- **Implied vol above 60 (30-day ATM IV).** Cost and risk control. Not shown to predict option losses (B6 IV 57.6–82.8 median -30%; 83.5+ median -39%).
- **Top fifth of vol20 and top fifth of realized vol** (see 1c). Stock-level exclusions, the most consistent of the volatility cuts.
- **Stock more than 15% below its 60-day high:** candidate exclusion, low-medium confidence.
- **Zero call days 2x+ in last 5 sessions** (or only one): exclude. Best-replicated negative result in the table.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

**Result:** +$25,435 on 41 trades. Average +62.0%, median -13.5%, 44% winners.
- Excluding the +2,596% outlier, average is about -1% on 40 trades.
- The dollar P&L cannot be split by trade from these notes without position sizes. Treat the dollar figure as dominated by the outlier.

**Option structures and results:**
- 30-day ATM, hold-10: 27 trades. Average +8.4%, median -13.2%.
- 30-day 5% OTM, hold-10: 2 trades. Average +40.2%, median +40.2% (small n; one winner at +86%).
- 30-day 5% OTM, double-or-10: 3 trades. Median -45.7%.
- 30-day ATM, double-or-10: 1 trade, -70.4%.
- 30-day 10% OTM, hold-10: 2 trades. Median -71.9%.
- 30-day 10% OTM, double-or-10: 1 trade, -62.9%.
- 90-day 5% OTM, hold-10: 2 trades, average +24.8%.
- 90-day 10% OTM, hold-10: 2 trades, average -66.9%.
- 14-day 10% OTM, hold-10: 1 trade, +2,596%. Rule violations: 11 sessions to expiry, 10% OTM, 14 days. Outlier only.

**What the ATM trades showed:**
- **Winners needed the stock to rise about +3% to +17%** over the hold. Losers were mostly flat-to-down stocks, and some lost 80% to 100% on stock moves of -3% to -12%.
- **Losses of 80% to 100% on small stock moves are too large for the model.** Several losing trades paid 2% to 5% of price with IV of 14% to 39%, and the stock fell 3% to 5%. This is the exit-quote concern from B5, now seen again. Until audited, these losses may be overstated. The audit has not been done.
- **IV did not separate outcomes.** Hold-10 ATM medians by IV band: 4.8–27 (-38%), 27.5–40 (-37%), 40–57.6 (-21%), 57.6–82.8 (-30%), 83.5–436 (-39%). No monotone pattern.
- **Implied/realized ratio:** medians were lowest when IV was cheap versus realized (ratio 0.17–0.68: -59%; 0.68–0.95: -29%; 0.95–1.25: -40%) and better when IV was rich (1.25–1.57: -15%; 1.57–3.43: -17%, average +47%). This is the reverse of "rich options lose." Low confidence (per-bin n not stated, likely about 8 trades). Log, do not act on it.

**Stock-level results (B6, all 250 candidates):** average +2.5%, median +0.4%.
- Biggest stock-level winners and losers were distributed across ratings and columns, with no clean pattern. The largest losers (-37%, -26%, -25%) had high realized vol, high IV, or large 20-day declines.

**Ratings (B6 medians):** +2 (n=5) +9.0%; +1 +1.6%; 0 -0.5%; -1 +0.2%; -2 -2.0%. Not monotone. Ratings are dropped.

**Columns tested in this bundle (against the universe median of +0.4%):**
- Call days 2x+ in last 5 sessions, 2–3 bin: +1.4% (68% up). **Replicated in direction; margin over universe too small to pass the rule in B6.**
- Call days 2x+ in last 5 sessions, 0–1 bin: -1.6% (34% up). **Negative in all three bundles.**
- News 7d, 1–2 articles: +2.7% (72% up). Exact-1 bin not isolated. **Passes the rule on this band; exact-1 test still needed.**
- News 7d 0–1 band: +0.6% (56% up). Zero-news bins were mixed in B6 (one at -7.0% with 0% up, one at +1.8% with 78% up), so the zero-news exclusion is weaker than in B4 and B5.
- Close vs VWAP above +0.2: +1.0% and +2.2% (62% and 66% up). **New, exploratory.**
- Vol20 top fifth: -3.2% (46% up). **Negative, consistent with B2, B3, B5.**
- Realized vol top fifth: -3.2% (46% up). **Negative, consistent with B5.**
- Calls 20d 1.05–1.52: +3.8% (71% up). **Best B6 bin, but B5 reversed.**
- Off-high beyond -14%: -0.1% to -0.3%. Small negative.
- Shares 1.28–1.78: +1.9% (60% up). Single-bundle tag.

**Trade-level observations to carry forward:**
- The ATM trades that won had stock moves of roughly +3% to +17%. The strongest winners (+134% to +192%) had stock moves of +4.5% to +12.2% with news in the prior 3 to 7 days.
- Stock moves that were flat or negative almost always produced losses.

---

## 3. WHAT I WILL TRY NEXT (BUNDLE 7)

1. **Build the combined entry screen and test each component first.** A candidate must pass all of the following, each tested alone on the new bundle before combining:
   - News 7d = 1 (report exact-1 separately; if not available, report 1 to 2 separately).
   - Call days 2x+ in last 5 sessions = 2 to 5.
   - Vol20 at or below the top-fifth cut (about 5.1%).
   - Realized vol below the top-fifth cut (about 80%).
   - Price $10 to $50 or above $50 (exclude sub-$10).
   - At least 20 sessions to expiry.
   Then report the combined set's stock median against the universe median. Pass rule: median at least 2.0 points above universe median, 55%+ up, n at least 40.

2. **Test close vs VWAP as a gate candidate.** Pre-register: names with close at least +0.2% above VWAP must show a median at least 2.0 points above universe median in B7, with at least 55% up. If it passes, it joins the entry screen as a tag first, then as a rule after a second bundle.

3. **Test shares ratio 1.2 to 1.8 (today and 5-day average)** as a tag with a pre-registered pass rule.

4. **Exit audit (mandatory before any trade counts).** For every ATM trade, record entry mid, bid, ask, and exit mid, bid, ask, with timestamps. Compare realized losses with a model using delta, theta, and the stock move. If audited losses are materially smaller than marked losses, the bundle results need restating. No trade counts toward the test until this is done.

5. **Enforce expiry and strike rules.** Trades with fewer than 20 sessions to expiry or on strikes other than ATM are logged as exploratory and excluded from the primary result. Report the primary result separately from the exploratory set.

6. **Test the ATM breakeven.** From the audited B6 and B7 trades, estimate the stock move needed for a positive option return at each IV band. Replace my earlier +1.5% to +2% estimate with the measured threshold.

7. **Continue 30-day ATM hold-10 as primary.** Keep 5% OTM logged on the same entries. Keep 90-day and double-or-10 as paper only.

---

## 4. SUPPORTING EVIDENCE AND IDEAS I HAVE DROPPED

### Evidence summary by structure (all bundles)
- **30-day ATM hold-10:** B4 -15% (10 trades), B5 -38.5% (24), B6 -13.2% (27). Negative in all three. Best median among the strikes tested.
- **30-day 5% OTM hold-10:** B5 -55% (4), B6 +40% (2). Too small to judge. Negative pooled.
- **30-day double-or-10:** Negative or mixed in every bundle. B6 median -45.7% (3 trades).
- **90-day:** B5 about -45% (6 trades). B6 mixed (+24.8% at 5% OTM, -66.9% at 10% OTM). Negative pooled.
- **10% OTM:** Negative in every bundle where tested.

### Stock-level evidence (replicated columns)
- **Call days 2x+ 2–3 (last 5 sessions):** B4 +3.0%, B5 +1.3%, B6 +1.4% (vs universe medians -1.0% in B5 and +0.4% in B6). Direction holds in three bundles; magnitude is modest. Medium confidence.
- **Call days 0–1:** negative in B4, B5, and B6. Medium-high confidence.
- **News 7d = 1:** B4 +8.3%, B5 +7.8%. B6 only supports the 1-to-2 band (+2.7%). Medium confidence; exact-1 test needed in B7.
- **Vol20 top fifth:** negative in B2, B3, B5, B6; B4 contrary. Medium confidence.
- **Realized vol top fifth:** negative in B5 and B6, plus earlier bundles. Medium confidence.
- **Off-high beyond -15%:** negative in B4, B5, B6 (small in B6). Low-medium confidence.
- **Close vs VWAP above +0.2%:** B6 only. Low confidence.

### Ideas dropped
- **Ratings (+2 to -2):** non-monotone in every bundle. Dropped.
- **Deep pullback below ma50:** reversed between B4 and B5, and not clear in B6. Dropped.
- **Calls 5-day average above 4.5:** reversed in B5. Dropped.
- **Put/call ratio and puts 20d as gates:** no consistent direction. Dropped.
- **Positive news tone as a gate:** unstable across bins. Tag only.
- **IV band and IV/realized ratio as option-level filters:** no consistent edge in B5 or B6. The one B6 pattern (rich IV had better medians) is low confidence. Logged only.
- **Double-or-10 exit:** negative in B6 and mixed in earlier bundles. Logged, not used.
- **14-day and 10%-OTM structures:** outside the primary set. The B6 outlier came from a trade that broke these rules; it does not justify changing them.

### Agent 4's final notes (not passed on)

# Working Notes: Final Version After Bundle 6 of 6

## 1. Current Strategy

### Status

Live trading stays suspended. Live size is zero. Everything runs on paper until an arm passes the reactivation test. No arm has passed.

Cumulative profit across six bundles is about -$16,000. Bundle 6 (+$14,273) was the second positive bundle, after bundle 2 (+$5,294). The option wrapper's results are dominated by a few very large winners, and the median trade has lost money in every bundle. Bundle 6's median trade was -38.2%.

### Reactivation test (unchanged)

An arm needs all three of the following:
- at least 60 trades,
- a positive median 10-session option return,
- a positive result in at least two separate bundles.

No arm meets this. The 90-day 5% arm is demoted to paper log. It drew only one trade in bundle 6, so it has no new evidence.

### Valuation and expiry audit (blocking, applies to every expiry)

Every option P&L figure in this document is provisional. Bundle 6 shows three problems that must be fixed before any option result is final:

1. **Impossible-looking -100% marks.** One 30-day 5%-strike call was marked at -100% on a session where the stock was up 5.3% with 12 sessions left. A call struck 5% above a stock that has just risen 5.3% should not expire worthless. Other -100% marks have 18 to 23 sessions to expiry.
2. **Expiry labels that do not match session counts.** Several trades labelled 30-day were "expired at session 9, settled at exercise value." A 30-calendar-day contract has about 21 sessions. Either the label or the session count is wrong.
3. **Average and median disagree in a way that depends on the mark.** Winners of +100% to +1,235% sit alongside losers of -100%. If the -100% marks are wrong, the profit figure is wrong too, in either direction.

Required before any option decision: recompute every trade with sessions-to-expiry taken from the contract's actual expiry date, mark unexpired options at a consistent model or market mid, and re-score every arm under one rule. This includes the 90-day arm, which I previously treated as exempt.

### Entry gate (v7, paper only)

A candidate qualifies for a paper entry only if all of the following hold. Every candidate is logged whether or not it passes, so the gate can be checked against the full universe.

1. **Price at or above $10.** Excluded below. Sub-$10 names were the worst band in bundles 1 to 3 and produced both the largest winners and losers in bundles 5 and 6. Confidence: moderate that sub-$10 is a poor place to trade options; the stock-level evidence is still thin.

2. **At least one news article in the prior 7 days (news 7d ≥ 1).** This is the strongest stock-level rule in the record and it held in bundle 6, though with a smaller gap than in bundles 4 and 5.
   - Bundle 4: no-news bins median about -9.6% and +0.4%; one-article bin +8.3%.
   - Bundle 5: no-news bins median about -9.8% and -0.6%; one-article bin +7.8%.
   - Bundle 6: no-news bins median -7.0% and +1.8%; news 7d 1 to 2 +2.7% (72% up); news 7d 2+ +1.8% (60% up).
   - The rule is "at least one," not "more is better." Higher article counts did not add in bundle 5 (2+ articles -1.3%) and were only mildly positive in bundle 6.
   - The 3-point gap in bundle 6 is smaller than the 5-point margin I set for confirmation. I count this as directional replication, not a clean confirmation.
   - Confidence: moderate to good. Three bundles agree on direction.

3. **Calls 20d at or below about 2.1.** Above this cut, names underperformed in bundles 3, 4 and 5. Bundle 6 agreed: 2.24 to 4.84 gave -0.5% (46% up), and 1.05 to 1.52 gave +3.8% (71% up). Confidence: moderate on the upper cut; low on any lower band, which was positive in bundle 6 but not in bundle 5.

4. **Volatility not in the top fifth (vol20 ≤ about 5%).** This is new in v7. The top vol20 fifth was negative in bundle 5 (3.76 to 5.26 band, -3.0%) and in bundle 6 (5.14 and above, -3.2%, 46% up). Realized vol above 81.6 was also -3.2% in bundle 6. Bundle 4's top fifth was flat, so this is two-bundle support. Confidence: low to moderate. It is a candidate gate, to be confirmed in bundle 7.

**Paper-only exclusion (new, derived from bundle 6 and needing confirmation):**
- Shares today below 1.0 (the lowest two fifths of today's share ratio ran -1.1% and -1.1% median in bundle 6; the bottom fifth was -3.4% in bundle 5). This replaces the earlier "shares at 0.75 or above" exclusion, which bundle 6 contradicted: names at 1.0 to 1.8 were positive (+1.3% to +1.9%).

**Dropped from the gate:**
- **vs ma50 band (-4% to +12%).** Bundle 6 reversed the ceiling: names above +12.6% gave +2.2% median (62% up), the best bin. The ceiling is now flat-to-negative in bundles 2 to 5 but positive in bundle 6. The floor has no clear support either. The band is not a gate until this resolves.
- **RSI below 65.** Bundle 6 showed RSI 68 to 91 as the best RSI bin (+0.9%, 56% up). Overbought names are negative in bundles 2, 3 and 5 and positive in bundles 4 and 6. Logged only.
- **Pullback band** (vs ma20 -8% to -2%; vs vwap20 -7.5% to -2.6%). Bundle 6 showed both bands at about -0.3% with about 50% up. The pass condition for this test failed. Dropped.
- **Five-day change below -7%** as a paper exclusion. Bundle 6's bottom fifth (5d % ≤ about -3.3% in the fifths, -33.99 to -3.26) was only -0.8% (48% up). Weakened to logged only.

### Instrument and exit

- **Benchmark wrapper:** 30-day call, 5% strike above the price, held 10 sessions. Paper only. Bundle 6: 21 trades, average +6.5%, median -42.7%. The average is supported by a few large winners.
- **0% strike (30-day):** paper only. Bundle 6 median +70.9% on 6 trades, which is the first clearly positive median for this arm. The arm's median has now been negative in bundles 1, 3 and 5 and positive in bundles 4 and 6. Mixed. Not promoted.
- **10% strike (30-day):** bundle 6 average +216.0% but median -62.5% on 5 trades. The average is one trade; the median is the honest number. Paper only.
- **90-day 5% and 10%:** paper log only. Bundle 6 had three trades between them, which says nothing. Bundle 5 median for 90-day 5% was -27.2% (15 trades); bundle 4 was -7.2% (6 trades). Pooled median negative. Both wait for the audit.
- **Exit: hold 10 sessions.** Still the default. No alternative has beaten it on median in a clean test. Double-or-10 exits remain deprioritized.
- **14-day expiries: excluded.**

### Sizing

- Live: zero.
- Paper: one flat unit per candidate that passes the gate. Also log every candidate that fails, with the reason.
- Never size up on an average. Never add after a win.

### Why this structure

The wrapper needs the stock to move by the premium plus the strike distance within 10 sessions. For a 30-day 5%-strike call with a premium of 1% to 7% of price, that is roughly +6% to +12% in 10 sessions. The universe's typical 10-session return is near zero (bundle 6 median +0.4%, average +2.5%), so most candidates need a large move just to break even.

The implied-volatility evidence points the same way. In bundle 6, the 30-day at-the-money call's median 10-session value change was negative in every IV bin (-21% to -39%) and in every iv/realized bin except the top two (-15% to -17%). Time decay alone explains much of the median loss. The signal and the wrapper both have to work, and the wrapper currently works against the signal.

So the next question is not "which option arm wins" but "does the gated set clear break-even more often than the universe?" That is measured in section 3.

## 2. Bundle 6: What Happened and What I Learned

### Results

- **Bundle total:** +$14,273 on 38 trades. Average +37.6%, median -38.2%, 37% winners (14 of 38).
- **Arms:** 30-day 5% (21 trades, median -42.7%); 30-day 0% (6, median +70.9%); 30-day 10% (5, median -62.5%); 90-day 10% (2, median -33.1%); other arms one trade each.
- **The profit came from tail winners.** The median trade lost 38%. The profit is not reliable until the audit is complete, and even then it rests on about 14 winning trades.
- **Universe (250 candidates):** average +2.5%, median +0.4% over 10 sessions. A better tape than bundle 5 (median -1.0%). This matters: bundle 6's option profit came partly from a rising market, which says little about the signal.
- **Ratings:** +1 (36 stocks) median +1.7%; +0 (48) median -0.7%; -1 (152) median +0.3%; -2 (14) median +5.7%. The -2 bucket was positive here and was -7.3% in bundle 5 on 18 stocks. The ordering is not stable. Ratings stay dropped.

### Pre-registered tests

**Test 3: v6 gate forward test.** Gated set: price ≥ $10, news 7d ≥ 1, vs ma50 between -4% and +12%, RSI below 65, calls 20d ≤ 2.1. The pass condition was gated median exceeding ungated median by 3 points, with more than 55% of gated names rising.
- **Result: inconclusive.** The summary gives single-factor fifths, not cross-tabulated combinations, so the gated median cannot be reconstructed exactly.
- **Single-factor reads:** news 7d ≥ 1 was positive (+0.6% to +2.7%); calls 20d ≤ 2.1 was positive in its lower two bins; vs ma50 in the -4 to +12 band was about flat (-0.8% to +1.4%); RSI below 65 was about flat to slightly positive. The gate's components point in the right direction, but the combined gate's edge is not demonstrated.

**Test 4: news gate on its own.** Pass condition: median advantage with the same sign and at least 5 points.
- **7-day version: directionally replicated, magnitude short.** Sign held. Gap roughly 3 to 4 points against a 5-point target.
- **1-day version: failed.** News 1d ≥ 1 was +2.0% (64% up), but the no-news 1d bins were erratic (-8.9%, -2.6%, +1.9%, +12.4%). No clean gap. Dropped as a separate test; the 7-day version is the gate.

**Test 7: paper exclusions.** Pass condition: both reproduce as negative.
- **Shares today below 0.75:** the rule as written did not reproduce. Names at 1.0 to 1.8 were the positive bins. The exclusion is restated as shares today below 1.0 (new cut, derived from this bundle, so it needs bundle 7 confirmation).
- **Five-day change below -7%:** bottom fifth -0.8% (48% up). Not reproduced in any meaningful sense.

**Test 8: pullback band.** Pass condition: positive median and more than 55% up. Failed in both bins.

**Test 1: valuation and expiry audit.** Not completed in this bundle. The -100% marks and the expiry-session mismatch described above are still open. This is the single most important open item.

### What replicated, failed, or is new

**Replicated:**
- **Ratings are noise.** Six bundles now. The ordering changes sign from one bundle to the next. Confidence: high.
- **The 30-day ATM call decays on 10-session holds.** Median negative in every IV bin and in most iv/realized bins. Confidence: high on direction.
- **News in the prior 7 days.** Directionally held in bundle 6. Confidence: moderate to good, with three bundles of support.
- **Calls 20d above about 2.1 is weak.** Held in bundle 6 (2.24 to 4.84 bin -0.5%, 46% up). Confidence: moderate.

**Failed or reversed:**
- **Ceiling on vs ma50 above +12.** Reversed in bundle 6 (+2.2%, 62% up above 12.6). Dropped from the gate. Confidence in the ceiling is now low.
- **RSI 65 and above as weak.** Reversed in bundle 6 (+0.9%, 56% up above 68). Dropped from the gate.
- **Pullback band as a lead.** Failed in bundle 6. Dropped.
- **Shares today at 0.75 or above as a bad sign.** Reversed in bundle 6: the 1.0 to 1.8 band was the positive band. Replaced by the shares-below-1.0 exclusion.
- **iv/realized as a signal.** Bundle 5 said the lowest ratio was best; bundle 6 says the highest bins (1.25 to 1.57, median -15%; above 1.57, median -17%) were better than the lowest (median -59%). Still unstable. Logged only.
- **Call days 2x+ over 5 sessions, 3 to 5 days.** Bundle 5 showed -0.7%; bundle 6 showed +2.4% (66% up). Conflicting. Logged only.

**New:**
- **High volatility names underperformed.** vol20 top fifth -3.2% (46% up) and realized vol top fifth -3.2% (46% up). The second bundle in a row that high-volatility names have been weak in the top fifth (bundle 5 also). This is the new gate candidate (v7, item 4).
- **Near the 60-session high was mildly positive.** Off-high between -1.6% and 0% gave +1.1% (61% up), the best bin. Names 20-day up 4.6% to 14.2% gave +1.5% (62% up). Both fit a momentum reading that bundle 5's pullback reading contradicts. Logged as a watch item, not a gate.
- **Low calls today was the worst band.** Calls ratio 0.06 to 0.55 gave -2.6% (34% up), the lowest bin. Mid-range calls (1.29 to 3.15) gave +3.5% (62% up). Logged; the non-monotone shape makes it hard to turn into a rule.

### Lessons from this bundle

- **Profit and median point in opposite directions, and the median is the honest number.** The bundle made money on tail winners while the median trade lost 38%. A paper arm that makes money only through three or four trades is not a strategy.
- **A rising tape lifts the wrapper.** Bundle 6's universe was up 0.4% median, bundle 5's was down 1.0%. The option profit moved with the tape, which is a warning against reading any single bundle's P&L as signal.
- **The audit has to come first.** Bundle 6's most striking outliers (+1,235%, +454%) and its -100% marks cannot be trusted until the mark rule is fixed.

## 3. What I Will Try Next

Each test is pre-registered. Record the result, then decide. Do not change thresholds mid-bundle.

1. **Complete the valuation and expiry audit before any further option decision.** For every trade in bundles 2 to 6:
   - Recompute sessions-to-expiry from the actual expiry date, and reconcile against the 30-day and 90-day labels.
   - Confirm how an unexpired option is marked at exit (market mid, model price, or intrinsic). Re-mark any -100% trade where the stock finished at or above the strike with more than 5 sessions left, and report how many such marks change.
   - Re-score every arm under one rule, including the 90-day arm.
   - Report the median and the hit rate with and without the top five winners in each bundle, so the tail's contribution is visible.

2. **Measure the signal directly, separate from the wrapper.** For every gated candidate and every control candidate, record:
   - the 10-session stock return;
   - whether the return exceeded the break-even move for the instrument (premium plus strike distance, computed from the candidate's own premium at entry);
   - the hit rate for gated and control groups.
   - Pass condition: gated hit rate exceeds the control hit rate by at least 5 points. If it does not, the instrument does not match the signal, whatever the option P&L shows.

3. **Forward test gate v7 in bundle 7.** Gated set: price ≥ $10, news 7d ≥ 1, calls 20d ≤ 2.1, vol20 ≤ about 5%. Pass condition: gated median 10-session return exceeds the ungated median by at least 3 points and more than 55% of gated names rise. Record the combined gate's result, not just the single-factor bins, so the gate is tested as a whole. Log the vs ma50 band and RSI as separate comparisons.

4. **Confirm the news gate on its own.** Compare names with at least one article in 7 days against names with none, same instrument. Pass condition: median advantage with the same sign and at least a 5-point gap. Bundle 6 gave about 3 to 4 points.

5. **Confirm the shares paper exclusion.** Test shares today below 1.0 against 1.0 and above. Pass condition: below-1.0 names have a negative median in bundle 7 with fewer than 50% up. Retire the 0.75 cut completely.

6. **Confirm the volatility gate.** Test vol20 above about 5% against the rest in bundle 7. Pass condition: top-fifth median below the universe median by at least 1 point. Note that the 5% threshold was chosen after seeing bundle 6's fifths, so its bundle-7 result carries more weight than bundle 6's.

7. **Test the 30-day 0% strike against the 30-day 5% strike on the gated set only, after the audit.** Bundle 6 showed 0% at +70.9% median on 6 trades and 5% at -42.7% on 21. Pooled 0% median across bundles is still mixed. Pass condition for any promotion: positive pooled median across at least 60 trades and positive in two bundles. Do not change the wrapper and the signal in the same bundle.

8. **Keep the 90-day 5% and 10% arms as paper logs.** Do not promote until the audit is complete and the pooled median is clearly positive.

9. **Sub-$10 (paper only).** Keep logging sub-$10 names with high call activity separately. Never live.

10. **Momentum watch item.** Log names within 1.6% of the 60-session high, and names 4.6% to 14.2% up over 20 sessions, as a separate paper bin. Pass condition: positive median with more than 55% up in bundle 7. This is a test of the bundle 6 reading, not a gate.

11. **Drop ratings from every decision.**

## 4. Supporting Evidence and Dropped Ideas

### Held up across bundles

- **Ratings are noise.** Six bundles. Confidence: high.
- **The 30-day ATM call decays on 10-session holds.** Median negative in every bundle's IV and iv/realized bins. Confidence: high on direction, moderate on size given the audit.
- **News in the prior 7 days.** Directional support in bundles 4, 5 and 6. The no-news bins are negative or flat, and the one- to two-article bins are positive. The gap was about 8 points in bundle 4, 8 in bundle 5, and about 3 in bundle 6. Confidence: moderate to good.
- **Calls 20d above about 2.1 is weak.** Negative in bundles 3, 4, 5 and 6. Confidence: moderate.
- **Hold 10 remains the default exit.** No alternative has beaten it on median in a clean test. Confidence: low to moderate.
- **Sub-$10 is high variance and risky.** Worst in bundles 1 to 3; both extremes in bundles 5 and 6. Confidence: moderate.

### Conflicting (logged only)

- **vs ma50 above +12.** Negative or flat in bundles 2 to 5; +2.2% in bundle 6. Not a gate.
- **Overbought (RSI 65 and above).** Negative in bundles 2, 3 and 5; positive in bundles 4 and 6. Not a gate.
- **Call days 2x+ over 5 sessions, 3 to 5 days.** -0.7% in bundle 5; +2.4% in bundle 6.
- **iv/realized.** Bundle 5 favored the lowest ratio; bundle 6 favored the highest. Unstable.
- **Long-dated call activity.** Conflicting between bundles 4 and 5; not revisited in bundle 6.
- **Stock-level IV bins.** Bundle 6's 40 to 57.6% IV bin was the best median (-21% for the 30-day call; +1.5% for the stock, 56% up), but bundle 5 showed the 29 to 43% band as the best option median. No IV gate.
- **Mild 20-day moves.** Bundle 5 favored -11% to -3%; bundle 6 favored +4.6% to +14.2%. Logged.

### Changed

- **Volatility:** from "lower is better" (bundle 5) to "high volatility weak in the top fifth" (bundles 5 and 6). Candidate gate.
- **Shares today:** from "top fifth weak" (bundle 5) to "below 1.0 weak, 1.0 to 1.8 positive" (bundle 6). Replaced the 0.75 exclusion.
- **0% strike:** from "median negative in three of four bundles" to "mixed": median +70.9% in bundle 6 on 6 trades. Paper only.
- **vs ma50 band:** from "floor -4, ceiling +12" to "no gate." Both edges unsupported after bundle 6.

### Failed or dropped

- **90-day 5% as primary paper arm:** failed in bundle 5; no new evidence in bundle 6.
- **Calls 5d avg and shares 5d top fifth (volume confirmation cluster):** reversed in bundle 5. Dropped.
- **Deep off-high pullback as a lead:** reversed in bundle 5. Dropped.
- **Pullback band (vs ma20 -8% to -2%; vs vwap20 -7.5% to -2.6%):** failed in bundle 6. Dropped.
- **Five-day change below -7% as a paper exclusion:** not reproduced in bundle 6. Logged only.
- **1-day news as a separate gate:** no clean gap in bundle 6. Dropped in favor of the 7-day version.
- **IV cap and IV gates:** not replicated. No IV gate.
- **RSI above 68 exclusion:** sign inconsistent. Dropped.
- **Market 5d and 20d gates:** no consistent effect in bundles 2 to 6. Dropped.
- **Puts 5d avg band:** conflicting between bundles 2 and 3. Dropped.
- **Over-$50 preference:** not visible in bundles 3 to 6. Dropped.
- **Double-or-10 exits:** lost in bundle 4 and deprioritized.
- **Sizing up on the average:** not supported.
- **Oversold with heavy calls:** no consistent positive return.
- **Ratings:** dropped entirely.

### Confidence summary

- **High:** ratings are noise; the 30-day ATM call decays on 10-session holds; the option wrapper, not only the signal, drives the median loss.
- **Moderate to good:** news in the prior 7 days (three bundles, directional, magnitude varies). Calls 20d above about 2.1 is weak (four bundles).
- **Moderate:** sub-$10 is risky; high volatility in the top fifth is weak (two bundles).
- **Low:** the shares-below-1.0 exclusion (one bundle, derived from its own data); near-high momentum watch item; vs ma50 band; RSI; the combined gate's edge (not yet demonstrated); the 0% strike arm.
- **Sample caveat:** pooled option results across bundles 2 to 6 total about 130 trades, with negative medians for the main arms. The standard error on any single average is roughly ±15 to 20 points per trade. The audit is open, so the size of any option loss or gain is not settled.
- **Bottom line:** the evidence still does not support live trading. Bundle 6's profit came from a few outsized winners on a rising tape, and the median trade lost money. The most useful paper work now is:
  - (a) completing the valuation and expiry audit;
  - (b) measuring whether gated names clear break-even more often than the universe, which tests the signal separately from the wrapper;
  - (c) confirming the news-in-7-days effect and the new volatility gate in bundle 7.

