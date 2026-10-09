# Committee generations (2026-10-09 04:57 UTC)

Total spent on all agent runs: $2.99. Candidate pool: {'train': 2998, 'score': 1439, 'holdout': 2000, 'test': 2720}.

Four agents train independently on six stock bundles; code scores their rules; an editor writes the
notes passed on. The scoring run trades blind months with the editor's notes. "Random" makes the same
number and kind of trades on random candidates in the same weeks. Rating correlation: does a higher
rating go with a better 10-session stock return (0 = no skill, ranges are 95%). Every trade is $1,000.

## Runs

| gen | who | phase | trades | profit $ | random profit $ | mean % | win % | rating corr (95% range) | top rated % | bottom rated % | unreadable | cost $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | agent1 | train | 56 | 1428.8 | -218.4 | 2.55 | 50.0 | 0.001 (-0.054 to 0.056) | 1.63 | 1.11 | 0/151 | 0.2055 |
| 1 | agent2 | train | 84 | -486.2 | 1050.0 | -0.58 | 53.6 | -0.025 (-0.079 to 0.026) | 1.63 | 0.97 | 0/151 | 0.2074 |
| 1 | agent3 | train | 78 | 2431.0 | 702.0 | 3.12 | 43.6 | -0.004 (-0.059 to 0.041) | -1.12 | 0.3 | 1/151 | 0.1992 |
| 1 | agent4 | train | 87 | -3353.8 | -1818.3 | -3.85 | 42.5 | 0.012 (-0.041 to 0.063) | -1.06 | 0.56 | 0/151 | 0.1992 |
| 1 | scorer | score | 304 | 5214.6 | 3374.4 | 1.72 | 48.0 | -0.061 (-0.125 to -0.007) | 1.23 | 3.1 | 0/144 | 0.1995 |

## Luck check

- Different rules tested on training data so far: 28 (by the agents and the editor).
- Editor rules checked on the blind months: 8; passed clearly (whole 95% range above buying everything the same way): 1.
- Expected to pass by luck alone: about 0.2. Treat a pass as real only if it clearly beats that count and the rule keeps passing in later generations.
  - passed: deep off-high recovering (generation 1): blind average 5.27% versus 1.25% for buying everything

## Generation 1

### Editor's rules, tested on all training months and bundles

- oversold dip reversal (when 5d % < -8 and rsi < 35: buy the stock): 247 trades, average +2.8% (95% range +0.2% to +6.0%, resampling whole weeks), median -0.0%, 50% winners. Buying every candidate the same way: +1.1%. Beat that in 3 of 6 bundles; first half of the months +3.0%, second half +2.7%.
- avoid overbought RSI (when rsi > 70: buy the stock): 359 trades, average +0.9% (95% range -1.2% to +3.5%, resampling whole weeks), median -1.1%, 45% winners. Buying every candidate the same way: +1.1%. Beat that in 3 of 6 bundles; first half of the months -0.0%, second half +1.7%.
- deep off-high recovering (when off high % < -30 and vs ma20 % > 0: buy the stock): 79 trades, average +1.2% (95% range -4.4% to +7.0%, resampling whole weeks), median -0.8%, 46% winners. Buying every candidate the same way: +1.1%. Beat that in 3 of 6 bundles; first half of the months +4.1%, second half +0.1%.
- avoid volatile penny stocks (when price = <$10 and vol20 % > 60: buy the stock): 2 trades, average +153.3% (too few trades or weeks for a range), median +153.3%, 100% winners. Buying every candidate the same way: +1.1%. Beat that in 0 of 0 bundles.
- trend momentum above ma50 (when 20d % > 15 and vs ma50 % > 0: buy the stock): 506 trades, average +2.9% (95% range +0.8% to +5.0%, resampling whole weeks), median -0.5%, 48% winners. Buying every candidate the same way: +1.1%. Beat that in 5 of 6 bundles; first half of the months +4.8%, second half +1.7%.
- below ma50 but turning up (when vs ma50 % < -10 and 1d % > 0: buy the stock): 219 trades, average +4.0% (95% range +1.6% to +6.7%, resampling whole weeks), median +0.7%, 52% winners. Buying every candidate the same way: +1.1%. Beat that in 5 of 6 bundles; first half of the months +6.1%, second half +3.3%.
- calm stock call 30-day (when vol20 % < 25 and rsi < 45: buy the 30-day call 0% above the price, exit hold10): 658 trades, average -6.1% (95% range -14.7% to +3.7%, resampling whole weeks), median -37.9%, 30% winners. Buying every candidate the same way: +4.0%. Beat that in 2 of 6 bundles; first half of the months -0.1%, second half -11.9%.
- avoid crowded put-heavy names (when p/c > 1.5 and vs ma20 % < 0: buy the stock): 159 trades, average +0.3% (95% range -1.9% to +2.4%, resampling whole weeks), median -0.7%, 47% winners. Buying every candidate the same way: +1.1%. Beat that in 1 of 6 bundles; first half of the months +1.0%, second half -0.3%.

### The same rules on the blind scoring months (never shown to agents)

- oversold dip reversal (when 5d % < -8 and rsi < 35: buy the stock): 76 trades, average +1.9% (95% range -1.4% to +4.8%, resampling whole weeks), median +0.0%, 50% winners. Buying every candidate the same way: +1.2%. Beat that in 4 of 6 bundles; first half of the months -2.0%, second half +4.6%.
- avoid overbought RSI (when rsi > 70: buy the stock): 291 trades, average +0.7% (95% range -1.7% to +3.0%, resampling whole weeks), median -0.7%, 47% winners. Buying every candidate the same way: +1.2%. Beat that in 2 of 6 bundles; first half of the months +0.2%, second half +1.0%.
- deep off-high recovering (when off high % < -30 and vs ma20 % > 0: buy the stock): 92 trades, average +5.3% (95% range +1.5% to +9.6%, resampling whole weeks), median +2.8%, 59% winners. Buying every candidate the same way: +1.2%. Beat that in 5 of 6 bundles; first half of the months +5.4%, second half +5.2%.
- avoid volatile penny stocks (when price = <$10 and vol20 % > 60: buy the stock): 1 trades, average +21.4% (too few trades or weeks for a range), median +21.4%, 100% winners. Buying every candidate the same way: +1.2%. Beat that in 0 of 0 bundles.
- trend momentum above ma50 (when 20d % > 15 and vs ma50 % > 0: buy the stock): 349 trades, average +0.8% (95% range -1.4% to +3.3%, resampling whole weeks), median -2.4%, 43% winners. Buying every candidate the same way: +1.2%. Beat that in 2 of 6 bundles; first half of the months +0.1%, second half +1.5%.
- below ma50 but turning up (when vs ma50 % < -10 and 1d % > 0: buy the stock): 85 trades, average +4.8% (95% range +1.1% to +8.8%, resampling whole weeks), median +2.1%, 60% winners. Buying every candidate the same way: +1.2%. Beat that in 5 of 6 bundles; first half of the months +4.8%, second half +4.8%.
- calm stock call 30-day (when vol20 % < 25 and rsi < 45: buy the 30-day call 0% above the price, exit hold10): 208 trades, average +3.0% (95% range -12.0% to +20.4%, resampling whole weeks), median -26.5%, 36% winners. Buying every candidate the same way: -1.6%. Beat that in 4 of 6 bundles; first half of the months +8.6%, second half -2.4%.
- avoid crowded put-heavy names (when p/c > 1.5 and vs ma20 % < 0: buy the stock): 42 trades, average +4.3% (95% range -0.3% to +9.5%, resampling whole weeks), median +1.5%, 60% winners. Buying every candidate the same way: +1.2%. Beat that in 3 of 6 bundles; first half of the months +5.3%, second half +3.5%.

### Editor's notes (passed to the next generation)

# Committee Notes: Final Editorial Summary (Bundles 1 to 6)

## 0. How to use these notes

- **Trust the code scorebook over any single trader's claim.** The scorebook tests each rule on all training candidates across all six bundles. The four traders each saw one bundle in depth, and their trade samples are very small.
- **Read the scorebook labels with care.** Several trader-chosen names describe the opposite of what the code measured. Each line reads "(when [condition]: buy the stock)". The condition defines the trades. The name is the trader's intent and may not match the result. Judge each rule by its numbers.
- **Every rule here is in-sample.** The code tested rules on the same candidates the traders studied, and many rules were tried. Some results will be chance, and the scorebook does not separate chance from edge.
- **No rule is confirmed.** The scorebook shows several rules with better means than the buy-everything baseline, but for most of them the 95% range includes the baseline. The one exception is noted in section 3.

## 1. Evidence quality and data integrity

### 1a. The four traders saw different things

- All four traders worked independently on the same stocks and weeks. Trade counts are expected to differ because each trader chose different trades.
- **Candidate-level counts should not differ, but they do.** Each bundle has 200 rated candidates, yet the rating bucket counts for bundle 6 differ across traders:

| Trader | +2 | +1 | 0 | -1 | -2 |
|---|---|---|---|---|---|
| Trader 1 | not listed | 9 | 132 | 55 | 4 |
| Trader 2 | not listed | 23 | 96 | 77 | 4 |
| Trader 3 | 1 | 25 | 79 | 91 | 4 |
| Trader 4 | 4 | 33 | 86 | 74 | 3 |

- The bundle 6 median for the 0 bucket ranged from +0.6% (Trader 4) to -2.9% (Trader 3). The -1 bucket median ranged from -3.3% to +0.8%. These cannot all be right for the same 200 candidates.
- Likely causes: different rating definitions or buckets, copying errors, or different subsets. The committee cannot tell which is correct.

### 1b. Bundle 6 trade records disagree

| Trader | Bundle 6 stock trades | Option trades | Bundle 6 result |
|---|---|---|---|
| Trader 1 | 0 | 0 | none |
| Trader 2 | 4 | 0 | -73 (dollars) |
| Trader 3 | 14 | not stated | -89 (dollars) |
| Trader 4 | 18 | 2 | -1,498 (dollars), about -7.5% average |

- Trader 1 reports that no bundle 6 candidate-level data was supplied. Traders 3 and 4 report candidate-level features. The scorebook uses candidate-level data, so Trader 1's gap is at least partly resolved by the scorebook, but the committee should confirm what data each trader received.
- Trader 3 says "91 candidates" but its rating table sums to 200. The 91 is the -1 count, so this appears to be a labeling slip.

### 1c. Other data gaps

- **Trade-level history is incomplete.** Trader 1 reports 55 stock trades and 1 option trade cumulatively. Trader 2 reports 84 trades, including 2 calls. Logging was inconsistent across traders, and no trader logged every trade with rating, rule, dollars, and exit reason.
- **Columns are not fully defined.** Windows, units, and definitions for 1d %, 5d %, 20d %, vol20 %, vs ma20 %, vs ma50 %, off high %, rsi, and price band are assumed, not verified. Calls, puts, p/c, p/c drop, short, medium, long, otm, and shares have no confirmed definitions.
- **Option fields are missing.** Expiry, strike, and days to expiry were not recorded in usable form. The "90-day call 0% above price" and "30-day call" labels come from the scorebook's rule definitions, not from verified trade records.
- **No pool or candidate median was recorded in the trader notes.** Excess-over-median comparisons cannot be done from them. The scorebook gives the buy-everything mean (+1.1% for stocks) but not the median.
- **Unverified outlier.** The +151% trade in bundle 2 has not been verified. Exclude it from all pooled figures.
- **Earlier-bundle notes are truncated** for Traders 3 and 4. Their claims about bundles 1 to 5 cannot be checked, and several of their "held in N bundles" statements are not verifiable. Trader 1's and Trader 2's bundle histories are internally consistent but not independently checked.

(The notes were cut off here by the reply limit.)

### Agent 1's final notes (not passed on)

# Final Working Notes (after bundle 6 of 6)

## 0. Evidence base

- **Bundles completed:** 6 of 6. Each bundle used a new set of stocks.
- **Candidates rated:** 1,200 across six bundles (200 each). Rating-level results are the largest sample, and they have not shown a stable, usable edge.
- **Stock trades:** 55 cumulative (21 in B1, 28 in B2, 4 in B3, 2 in B4, 0 in B5, 0 in B6).
- **Option trades:** one (B1). None since.
- **Bundle 6 trades:** none. Bundle 6 adds nothing to trade-level evidence.
- **Pooled trade results:** still not computable from these notes. I do not estimate one.
- **Data supplied for bundle 6:** rating-bucket level only. No candidate-level features, no per-name forward returns, no index return, no date range, and no candidate median. This is the same gap as bundle 5.
- **Bundle 6 classification:** descriptive only. It fails the data-readiness check I set in section 9 of the bundle 5 notes, so it cannot support a finding, a test result, or a rule change.

## 1. Process status

| # | Fix | Status after bundle 6 | Evidence |
|---|---|---|---|
| 1 | Log every trade with rating, rule, entry/exit, dollars, exit reason | **Not done** | No trades in B5 or B6. The B4 gap is still open, and nothing has been logged in the required form. |
| 2 | Log features for all 200 candidates, not only traded names | **Not done** | No candidate features for B5 or B6. This blocks T1, T2, T3, and T6 for the second bundle running. |
| 3 | Glossary for every column | **Not done** | No glossary has been provided. See section 1a. |
| 4 | Market context per bundle (index return, date range, candidate median) | **Not done** | No index return, date range, or candidate median for B5 or B6. The +0 median is still a proxy. |
| 5 | Verify the +151% trade from bundle 2 | **Still open** | Unverified. Excluded from every pooled statistic. |
| 6 | Pre-register tests before opening data | **Written, but not executable with the data supplied** | Thresholds have not been changed. Most tests cannot run because the inputs are missing. |

**Summary:** after six bundles, none of the four process fixes that would let me attribute results to a signal has been completed. Bundles 5 and 6 were both evaluated at bucket level only. My conclusions are therefore limited to the rating-bucket patterns in section 2.

**Rule for now:** no new stock trades on the strength of a rating alone. Trades cannot be attributed to a signal or evaluated against a baseline until fixes 1, 2, and 4 are in place.

### 1a. Column status

Usable provisionally. Units and windows still need verification against the source:

- **1d %, 5d %, 20d %:** price return over 1, 5, and 20 sessions (assumed; verify whether the window ends on the signal date).
- **vol20 %:** 20-session volatility (assumed; verify definition).
- **vs ma20 %, vs ma50 %:** percent distance of price from the 20- and 50-session moving averages (assumed).
- **off high %:** percent below the recent high (assumed; verify lookback).
- **rsi:** relative strength index (assumed period 14; verify).
- **price band:** price bucket, for example $10–50 (verify bucket edges).

Unknown. Do not use in any rule until defined:

- calls, puts, p/c, p/c drop
- short, medium, long
- otm
- shares

### Correction to earlier notes

- **Bundle 5 median ordering (section 2 of the bundle 5 notes) was wrong.** By median, the correct order is -1 (-0.3%) > +1 (-0.4%) > +0 (-2.5%) > -2 (-2.9%). The earlier text put +1 above -1. The -1 and +1 buckets are both near zero, so the difference is immaterial, but the record should be right.
- **Bundle 4 "H1 effectively dropped" error** was corrected in the bundle 5 notes. It stands corrected here: H1 has never been dropped under the pre-registered rule.

## 2. Rating signal

**Status: not usable as a trigger.** The rating does not separate good from bad outcomes reliably across six bundles. Relative ordering versus the +0 bucket shows a weak pattern for +1 and -1. Absolute medians are negative in most bundles for every bucket.

### Bundle 6 results (n = 200, bucket level)

| Rating | n | Avg | Median |
|---|---|---|---|
| +1 | 9 | +2.5% | +1.2% |
| +0 | 132 | +0.9% | -1.1% |
| -1 | 55 | -1.0% | -0.4% |
| -2 | 4 | -7.3% | -10.1% |

Notes on this bundle:

- The +1 bucket (n = 9) and the -2 bucket (n = 4) are below the 30-name reporting floor. Neither can be reported as a finding.
- The +0 median (-1.1%) is the proxy for candidate-level drift. It is not the true candidate median, which was not supplied.
- The +0 mean (+0.9%) sits well above its median (-1.1%). This is the same skew pattern seen in other buckets, so the mean should not be read alone.

### Six-bundle table

Format: avg / median (n). Pooled means are count-weighted from bundle averages and are approximate. Pooled medians cannot be computed from the bundle-level data.

| Rating | B1 | B2 | B3 | B4 | B5 | B6 | Pooled avg (n) |
|---|---|---|---|---|---|---|---|
| +1 | -0.2 / -2.2 (35) | +7.2 / +3.1 (37) | +3.5 / -0.3 (30) | -5.0 / -5.6 (17) | -2.6 / -0.4 (22) | +2.5 / +1.2 (9) | ≈ +1.6% (150) |
| +0 | -1.3 / -2.0 (76) | +2.7 / +1.8 (64) | -1.2 / -1.9 (105) | -2.2 / -2.9 (114) | -1.8 / -2.5 (109) | +0.9 / -1.1 (132) | ≈ -0.6% (600) |
| -1 | +1.1 / +0.6 (77) | +0.6 / -1.2 (77) | +6.4 / -1.3 (58) | -2.8 / -4.0 (69) | +1.3 / -0.3 (62) | -1.0 / -0.4 (55) | ≈ +0.8% (398) |
| -2 | +9.7 / +2.5 (12) | +5.0 / -2.0 (22) | -5.0 / -4.8 (7) | not tested | +0.3 / -2.9 (7) | -7.3 / -10.1 (4) | ≈ +3.2% (52) |

### Median gap versus the +0 bucket (same bundle)

Positive means the bucket's median beat the +0 median in that bundle. This is the form the pre-registered T4 test uses.

| Bucket | B1 | B2 | B3 | B4 | B5 | B6 | Beat +0 median |
|---|---|---|---|---|---|---|---|
| +1 | -0.2 | +1.3 | +1.6 | -2.7 | +2.1 | +2.3 | 4 of 6 |
| -1 | +2.6 | -3.0 | +0.6 | -1.1 | +2.2 | +0.7 | 4 of 6 |
| -2 | +4.5 | -3.8 | -2.9 | n/a | -0.4 | -9.0 | 1 of 5 |

### Median sign (negative count out of bundles tested)

- **+1:** negative in 4 of 6 (B1, B3, B4, B5). Positive in B2 and B6.
- **+0:** negative in 5 of 6 (B1, B3, B4, B5, B6). Positive only in B2.
- **-1:** negative in 5 of 6 (B2, B3, B4, B5, B6). Positive only in B1.
- **-2:** negative in 4 of 5 tested (B2, B3, B5, B6). Positive in B1.

### What the six bundles show

- **+1 versus +0 (median):** +1 beat +0 in 4 of 6 bundles (B2, B3, B5, B6). It lost in B1 (by 0.2 points) and in B4 (by 2.7 points). The B6 gain (+2.3) rests on n = 9. Pooled, the +1 mean (≈ +1.6%) is still driven by B2 (+7.2%). Excluding B2, the pooled +1 mean is about -0.4%. The relative ordering is the most consistent pattern in this data, but its absolute median is still negative in most bundles.
- **-1 versus +0 (median):** -1 also beat +0 in 4 of 6 bundles (B1, B3, B5, B6). Its absolute median is negative in 5 of 6 bundles. Its mean is pulled up by skew (B3: +6.4% mean with -1.3% median).
- **-2:** the bucket beat +0 in only 1 of 5 tested. Its pooled mean (≈ +3.2%) comes from skew in B1 and B2. In B6 it had its worst result yet (median -10.1%), but n = 4 is too small to report. Overall, the -2 bucket does not support a buy signal.
- **+0 (reference):** the largest group (600 of 1,200) has a pooled mean of about -0.6% and a median that is negative in 5 of 6 bundles. It is a weak reference point, not an edge benchmark.
- **Ordering still flips across bundles.** No bucket ordering has held in more than two consecutive bundles, and the B6 pattern (+1 and -1 above +0) is not yet a stable one.

**Conclusion:** the rating does not separate outcomes reliably in absolute terms. The +1 and -1 buckets show a modest relative edge over +0 on medians in four of six bundles, but the samples per bundle are small and the absolute returns are mostly negative. Ratings may be recorded as description. They are not a buy or sell trigger.

## 3. Market and regime

- **The +0 proxy median has been negative in five of six bundles** (B1, B3, B4, B5, B6). Bundle 2 is the only exception.
- **Consecutive negative proxy medians:** B3, B4, B5, and B6 (four in a row).
- **Bundle 6 proxy (-1.1%) was the least negative since bundle 2.** This is a small move on a proxy, and it does not change the picture.
- **Bundle 6 bucket medians were mixed in sign:** +1 was positive (+1.2%), while +0 (-1.1%), -1 (-0.4%), and -2 (-10.1%) were negative.
- **Interpretation (unconfirmed):** the candidate universe may have drifted down over the 10 sessions in most bundles. If so, raw returns mostly reflect the regime rather than the rating. I still have no index data to confirm this.
- **Needed:** index return, date range, and candidate-level median for every bundle (fix 4). Without these, "excess return" cannot be computed correctly.

**Going forward:** express returns relative to each bundle's candidate median before pooling. Do not pool raw returns across bundles with different medians. Until that is possible, the only comparisons available are within-bundle comparisons against the +0 bucket, and these are descriptive.

## 4. Trade-level evidence

**Bundle 4 trades (n = 2, both losers), unchanged:**

| | Trade A | Trade B |
|---|---|---|
| Result | -12.2% | -7.5% |
| 1d % | +5.9 | +12.4 |
| 5d % | +3.0 | +7.9 |
| 20d % | -3.9 | +8.6 |
| vs ma20 % | +4.5 | +14.9 |
| vs ma50 % | +9.9 | +6.9 |
| off high % | -4.4 | -22.1 |
| rsi | 55.0 | 70.0 |
| price band | $10–50 | $10–50 |

**Bundle 5 and bundle 6 trades:** none.

**Pattern observed (B4):** both trades were bought after positive 1-day and 5-day moves and while above their 20-session average. Both then fell sharply.

**Interpretation:** a hypothesis, not a finding. Two trades cannot establish it. Two further bundles have not added trade evidence, and candidate-level features were not supplied, so H5 cannot be tested.

## 5. Hypothesis register

Status definitions: Confirmed, Weakened, Contradicted, Untested, Single-bundle, Mixed, Unverified, Dropped.

| # | Idea | Evidence | Status | Confidence |
|---|---|---|---|---|
| H1 | Rating +1 beats +0 (median) | Beat +0 median in B2, B3, B5, B6 (4 of 6). Lost in B1 (marginal) and B4 (clear). Pooled mean ≈ +1.6%, driven by B2; ≈ -0.4% excluding B2. Absolute median negative in 4 of 6. Per-bundle n ranges from 9 to 37, below the 30-name floor in B5 and B6. | **Mixed. Relative edge in most bundles, not validated. Not a buy trigger.** Not dropped under the pre-registered rule. | Low |
| H2 | Rating -2 is a buy signal | Median negative in 4 of 5 tested bundles. Beat +0 median in 1 of 5. Pooled mean positive only through skew. B6 median -10.1% (n = 4). | **Contradicted as a buy signal.** | Low |
| H3 | Rating -1 is a rebound signal | Beat +0 median in 4 of 6 bundles. Absolute median negative in 5 of 6. Mean skew is large. | **Weakened as a buy trigger.** Description only. | Low |
| H4 | Rating +0 is a neutral baseline | Median negative in 5 of 6 bundles. Pooled mean ≈ -0.6%. Largest group. | **Descriptive only.** Weak reference point. | Low |
| H5 | Buying after large 1-day and 5-day gains loses | Two losing trades in B4. No candidate-level test: B5 and B6 features were not supplied. | **Single-bundle, untested at candidate level.** T1 and T2 not run. | Low |
| H6 | Candidate universe drifts down over 10 sessions | +0 proxy median negative in 5 of 6 bundles; four in a row (B3–B6). No index data. | **Strengthened, still unconfirmed.** | Low–medium |
| H7 | Options (calls/puts/p/c) carry information | One options trade in B1. Columns undefined. | **Untested / excluded.** | None |
| H8 | The +151% trade in B2 is a real result | Not verified. | **Unverified, excluded from clean pools.** | n/a |

**Dropped as tradable rules:** H1 and H3 as buy triggers. H2 is contradicted as a buy signal. H1 is in mixed status, not dropped under the pre-registered rule.

## 6. Trading restrictions

These are caution flags, not validated rules. All remain in force.

- **Avoid chasing sharp short-term strength (provisional).** Do not open a new stock position when 1d % is above +5 and vs ma20 % is above +10, until H5 is tested at candidate level. Basis: two trades, both losers, low confidence. Still in force because T1 and T2 could not be run on B5 or B6.
- **Do not size up on a rating.** No bucket has shown a stable positive absolute median across bundles. The +1 and -1 relative edge over +0 is not enough to size on.
- **Do not open positions on the -2 rating.** It is contradicted as a buy signal (section 5, H2).
- **Stand aside by default.** Without a validated signal and with the logging gaps still open, do not open new positions unless a logged rule is in place.
- **Do not treat the +1 or -1 relative edge as evidence.** It rests on small per-bundle samples and does not survive a pooled view that excludes skew from individual bundles.

## 7. Pre-registered tests: bundle 6 results

Thresholds were not changed after any bundle's data was seen.

**Data required and status for bundle 6:**

| Required input | Supplied for B6? |
|---|---|
| Candidate-level features (all 200) | No |
| Per-candidate 10-session forward return | No (bucket-level only) |
| Bundle index return and candidate median | No |
| Column glossary | No |

**Data-readiness check (from bundle 5, section 9):** failed. Bundle 6 is therefore descriptive only. No test result below is reported as a finding.

| Test | Result | Reason |
|---|---|---|
| T1 (H5): 1d % > +5 vs ≤ +5 | **Not run** | No candidate features. |
| T2 (H5): vs ma20 % > +10 vs ≤ +10 | **Not run** | No candidate features. |
| T3: off high % ≤ -20 vs > -20 | **Not run** | No candidate features. |
| T4 (H1): +1 vs +0 median | **Run at bucket level. Not falsified.** +1 median (+1.2%) above +0 median (-1.1%). Gap +2.3 points. n = 9, below the 30-name floor. | Direction held; sample too small to report. |
| T5 (H6): bundle median sign | **Reported, descriptive only.** The +0 median (proxy) was negative. The +1 bucket was positive. Bundle median not supplied. | Information only. |
| T6: rsi ≥ 70 vs < 70 | **Not run** | No candidate features. |

**Consequences:**

- No test moved H5 or any trading restriction.
- T1, T2, T3, and T6 have now gone unrun for two bundles. They cannot be evaluated until candidate-level features are logged.
- H1 is not dropped. The B6 T4 result is one more non-falsification, and it is underpowered.

## 8. Confidence summary

- **High:** none. No idea has held across the six bundles with a consistent direction and a positive excess return.
- **Medium:** none. The +1 and -1 relative edge over +0 is the closest thing to a pattern, and it is not strong enough for medium confidence.
- **Low–medium:** H6 (four consecutive negative proxy medians; no index data).
- **Low:** H1 and H3 (relative edge in four of six bundles, absolute medians mostly negative, small n), H2 (contradicted as a buy signal, small n), H5 (two trades, no candidate test), H4 (descriptive only).
- **None:** H7 (undefined columns), H8 (unverified trade).

## 9. Lessons across six bundles

- **Pre-registration without the data pipeline is not enough.** I wrote tests that need candidate-level features, and bundles 5 and 6 both arrived at bucket level only. The data-readiness check was set in bundle 5 but was not enforced in bundle 6. Enforce it before the bundle is opened, not after.
- **Small buckets produce noisy medians.** The +1 bucket moved from -5.6% to -0.4% to +1.2% median over three bundles. The -2 bucket moved from -4.8% to -2.9% to -10.1%. Do not report any split under 30 names as a finding.
- **Mean and median disagree often.** The -1 bucket's mean and median have opposite signs in B5, and the +0 mean and median disagree in B6. Report both and do not act on the mean alone.
- **Relative and absolute results can point different ways.** +1 and -1 beat the +0 median in four of six bundles, but their own medians were negative in most bundles. The relative result is not evidence of a profitable signal.
- **Logging gaps are the binding constraint.** Across six bundles, no trade has been logged with its rating, rule, dollars, or exit reason, and no candidate-level features have been logged for bundles 5 or 6. Without these, no hypothesis can move past "untested" or "descriptive," however many bundles are run.
- **Ideas that worked in one bundle and failed in another:** the +1 bucket (B2 strong, B4 weak), the -1 bucket (B1 and B3 strong, B2 and B4 weak), and the -2 bucket (B1 strong, B6 weakest on record). None has held across consecutive bundles.

## 10. Final position and recommendations

**Overall conclusion:** after six bundles

(The notes were cut off here by the reply limit.)

### Agent 2's final notes (not passed on)

# Working Notes: Final Review (after Bundles 1 to 6)

## 0. Scope and status

- **Bundles reviewed:** 6 (final). Bundle 6 was a fresh set of stocks.
- **Candidates rated:** about 1,200 candidate-observations across six bundles. Bundle 6 contributed 200.
- **Trades:** 84 total. Bundle 6 added 4 (all recorded as "stock," treated as shares; see Section 5).
- **Purpose of this document:** Close open questions, decide what to keep, drop, or leave as hypothesis, and set out what the evidence does and does not support. No new signals are claimed here.

---

## 1. Bundle log

| Bundle | Result | Instrument | Stock mean / median / hit rate | Pool mean (10-session) | Key takeaway |
|---|---|---|---|---|---|
| 1 | Profit -280 on 22 trades | Mostly shares, 2 calls (both large losers: -27.6%, -86.2%) | +4.3% / +1.9% / not recorded | not recorded | Shares did well, calls did badly. Ratings did not predict in the expected direction. |
| 2 | Profit +100 on 31 trades | Shares only | +0.3% / +1.6% / 61% | not recorded | Median positive, mean near zero. Two large losers drove most of the damage. |
| 3 | Profit -228 on 26 trades | Shares only | -0.9% / -1.0% / 50% | not recorded | Left tail heavier. 8 of 10 visible losers lost more than 10%. |
| 4 | No trades (rating data only) | None | n/a | about -2.7% | Every rating bucket had a negative median. |
| 5 | Profit -6 on 1 trade | Shares (inferred) | -0.6% / -0.6% / 0% | about -0.8% (derived) | Single small loss on an extended run-up. Too few trades to test anything. |
| 6 | Profit -73 on 4 trades | Shares (assumed) | -1.8% / -1.9% / 50% | about +0.3% (derived) | All four trades were oversold, deep-drawdown names. Median negative. The -1 bucket led on both mean and median. The -2 bucket lost. |

**Cumulative (bundles 1 to 6):** -487 across 84 trades.

**Shares-only record (bundles 2, 3, 5, and 6):** about -207 on 62 trades. Mean about -0.3%. Hit rate about 55%. Median per bundle: positive in bundle 2, negative in bundles 3, 5, and 6.

**Overall verdict on stock-side performance:** Across six bundles, there is no evidence of a positive edge in the trades taken. Bundle 1 is the only bundle with a clearly positive stock result, and it also contained the two large call losses. The total is negative and the sample is still small.

---

## 2. What changed in bundle 6

1. **The -1 bucket was the best bucket on both mean and median.** n=77, mean +1.5%, median +0.8%. Excess over pool: about +1.2 points on the mean. This is the first bundle in which -1 had a positive median (apart from bundle 1).
2. **The -2 bucket reversed.** n=4, mean -5.0%, median -6.2%. Bundle 5's -2 result (n=10, mean +8.9%, median +3.8%) did not repeat. The bucket's sign has now flipped between consecutive bundles.
3. **The 0 bucket was flat on the mean and negative on the median.** n=96, mean +0.4% (about +0.1 points above pool), median -2.0%.
4. **The +1 bucket was the second-worst on the mean.** n=23, mean -3.2%, median -0.3%. Excess about -3.5 points.
5. **All four trades were oversold names in deep drawdowns.** RSI ranged from 8 to 22. Each trade was 4.6% to 16.6% below its 20-day average and 19.5% to 46.5% below its 20-day high. Results: -6.6%, -5.0%, +1.2%, +3.0%. Mean -1.8%, median -1.9%.
6. **The RSI-below-30 hypothesis was tested directly and failed in this bundle.** See Section 6.
7. **No calls were traded.** The call question remains unanswered by recent data.
8. **No losing trade approached -10%.** The worst was -6.6%. The stop rule was not tested by any trade in this bundle.

---

## 3. Rating signal

### Bundle 6 results (10-session forward return, 200 candidates)

| Rating | n | Mean | Median | Excess vs. pool (mean) |
|---|---|---|---|---|
| +1 | 23 | -3.2% | -0.3% | about -3.5 pts |
| 0 | 96 | +0.4% | -2.0% | about +0.1 pts |
| -1 | 77 | +1.5% | +0.8% | about +1.2 pts |
| -2 | 4 | -5.0% | -6.2% | about -5.3 pts (n=4) |

**Pool mean:** about +0.3%. Derived from the bucket means weighted by n (counts sum to 200). This is not read from a separate pool figure.

**Methodological note:** The plan for this bundle specified an adoption criterion based on "excess-over-pool median." No pool median has been recorded in any bundle, so excess medians cannot be computed. This review uses excess means where available and reports medians alongside them without subtracting them from the pool mean. Future bundles should record the pool median as well.

### Pooled view across six bundles (approximate, weighted by n)

| Rating | Pooled n | Pooled mean (approx.) | Medians by bundle (B1 / B2 / B3 / B4 / B5 / B6) | Negative median count | Read |
|---|---|---|---|---|---|
| +1 | 148 | about +1.8% | -1.0 / +1.6 / -3.1 / -6.7 / -2.4 / -0.3 | 5 of 6 | Pooled mean is carried by early outliers. Median negative in most bundles. Not a buy signal. |
| 0 | 525 | about -0.7% | -1.5 / 0.0 / -1.0 / -1.5 / -2.5 / -2.0 | 5 of 6 (one zero) | Largest bucket. Median negative in most bundles. Mean tracks the pool. |
| -1 | 482 | about +0.9% | +0.7 / -0.7 / -2.4 / -4.7 / -1.8 / +0.8 | 4 of 6 | Mean mildly above pool in the two bundles with a recorded pool mean. Median is the least stable number. |
| -2 | 42 | about +2.0% | +8.0 / -1.7 / -4.8 / -19.0 / +3.8 / -6.2 | 4 of 6 | Extreme dispersion. Pooled mean is driven by small-n and outlier bundles. Not reliable. |

**Data flags:** Bundle 1 counts sum to 199, not 200. Bundle 2 has no +2 row. These are unresolved (see Section 8). Pooled figures are approximations.

**Pool mean across bundles:** Recorded only for bundles 4, 5, and 6 (about -2.7%, -0.8%, and +0.3%). Average of those three is about -1.1%. Pool means for bundles 1 to 3 are not recorded, so cross-bundle excess cannot be computed for them.

### Excess-over-pool mean, bundles where it is computable

| Rating | B5 excess | B6 excess | Both bundles beat pool? |
|---|---|---|---|
| +1 | about -1.3 | about -3.5 | No (both negative) |
| 0 | about -2.6 | about +0.1 | Mixed |
| -1 | about +2.4 | about +1.2 | Yes |
| -2 | about +9.7 (n=10) | about -5.3 (n=4) | Mixed (sign flipped) |

### Assessment

- **The -1 bucket is the most consistent positive-mean bucket in the two bundles where excess is computable.** It beat the pool in both. Its median was negative in four of six bundles. The mean is not a clean signal (a few large winners carry it), and the sample is small relative to the bucket's variance. Confidence: low.
- **The -2 bucket is too unstable to use.** Its sign flipped between bundles 5 and 6, and its pooled mean rests on n=42 with heavy dispersion. The earlier "contrarian" reading of -2 is not established.
- **The +1 bucket failed.** Median negative in five of six bundles. Below the pool on mean in both bundles where excess is computable. Confidence that +1 is not a buy signal: medium.
- **The 0 bucket is not clearly "pool drift" and not clearly "neutral."** Its mean tracked the pool in bundle 6 but was well below it in bundle 5. Its median has been negative in five of six bundles. Avoid treating 0 as a neutral default: confidence low-to-medium.
- **Best bucket by bundle:** -2 (B1), +1 on mean (B3), 0 (B4), -2 (B5), -1 (B6). The winner changes almost every bundle. This is still closer to noise than to structure.
- **Contrarian ordering:** It held in bundle 5 (-2 and -1 above pool, 0 and +1 below). It held only partly in bundle 6 (-1 above pool, but -2 below and 0 flat). Across the two bundles where it can be checked, it held in one of two. Not established.

### Rating rules (final)

- **"The rating is not an entry trigger."** Kept. No bucket ordering has been stable across six bundles. The -1 bucket's mean advantage in two bundles is not enough for an entry rule. Confidence: medium.
- **"The rating is not a short trigger."** Kept. The -2 bucket's sign flipped between bundles 5 and 6, and its median was negative in four of six bundles only because of a few extreme results. Shorting on the rating carries unbounded risk and no stable edge. Confidence: medium.
- **"Do not treat 0-rated candidates as a neutral default."** Kept, at low-to-medium confidence. The median has been negative in five of six bundles.
- **"+1 is not a buy signal."** Kept. Confidence: medium.
- **"Use excess-over-pool returns in review."** Kept, with the caveat that excess medians need a recorded pool median.
- **Adoption test (from the plan): a rule is adopted only if its sign holds on the excess-over-pool median in at least four of six bundles.** No rating rule meets this. The -1 mean advantage has been observed in two of two computable bundles, but the test was defined on medians and pool medians are unavailable. Under the stated test, no rating rule is adopted.

---

## 4. Stock trades

### Bundle 6 (four trades)

| Trade | Price band | RSI | 20-day return | Off 20-day high | Result (10 sessions) |
|---|---|---|---|---|---|
| 1 | Below $10 | 21.0 | -12.5% | -46.5% | -6.6% |
| 2 | $10 to $50 | 8.0 | -25.3% | -33.1% | -5.0% |
| 3 | $10 to $50 | 14.0 | -23.6% | -28.9% | +1.2% |
| 4 | Above $50 | 22.0 | -16.0% | -19.5% | +3.0% |

- **Summary:** n=4, mean -1.8%, median -1.9%, hit rate 50%.
- **Common feature:** All four were oversold (RSI 8 to 22), below both the 20-day and 50-day averages, and well off their 20-day highs. This is a "deep-downtrend, oversold" entry profile.
- **Feature spread:** 1-day returns from -5.8% to +1.3%. 5-day returns from -11.8% to +1.5%. 20-day volatility from 1.5% to 3.4%. Two trades were in the $10 to $50 band, one below $10, and one above $50.
- **Dollar consistency check (inference, not recorded data):** Total -$73 across returns of -6.6%, -5.0%, +1.2%, and +3.0%. If all four positions were about $1,000, the per-trade dollars would be about -$66, -$50, +$12, and +$30, summing to about -$74. This matches the -$73 total, which supports an implied position size near $1,000. Position size is still not recorded and this remains an inference.
- **Assumption:** All four were shares. The summary lists "stock" and no expiry or strike, which is consistent with shares, but this is not confirmed.
- **Ratings for these four stocks were not recorded in the trade summary.** The trades cannot be linked to the rating table.

### Cumulative stock-side record (bundles 1 to 6)

- 84 trades in total. Shares-only record (bundles 2, 3, 5, 6): about -207 on 62 trades. Mean about -0.3%. Hit rate about 55%.
- Left tail: The worst losses were -86.2% (call, B1), -41.7% (B2), and -26.0% (B3). Eight of ten visible losers in bundle 3 lost more than 10%.
- Bundle 6 had no tail losses.

### Calls

- Two calls in bundle 1, both large losers (-27.6%, -86.2%). No calls since then.
- **Calls are 2 of 84 trades.** The evidence is negative but thin.
- **Rule:** No new call positions until a bundle with calls shows a positive median and expiry, strike, and days-to-expiry are recorded for every option trade. Kept. Confidence: medium.

### Expiry and strike

- Not recorded in usable form for any past trade, including bundle 6.
- **Rule:** Record expiry, strike, and days-to-expiry for every option trade. Kept. Without these, call results cannot be attributed to moneyness or time decay.

---

## 5. Hypotheses ledger

### RSI below 30 as an entry filter: DROPPED

- **Origin:** One bundle of visible support (bundle 3).
- **Bundle 4:** No trades.
- **Bundle 5:** The one trade had RSI 69, outside the range.
- **Bundle 6:** Four trades, all with RSI below 30 (8 to 22). Median -1.9%, mean -1.8%, hit rate 50%. This is the direct test, and it did not support the hypothesis.
- **Threshold test:** The plan required at least 15 RSI-below-30 trades across two or more bundles with a positive median. Cumulative count is about 4 to 5 in the recorded bundles (the bundle 3 count is not recorded in these notes), and the median is not positive.
- **Decision:** Dropped as an entry filter. Confidence that RSI below 30 is a useful entry filter: low, and bundle 6 weighs against it.

### Oversold deep-downtrend entries: NEW, NEGATIVE OBSERVATION

- **Observed:** Bundle 6's four trades all fit this profile. Median -1.9%.
- **Status:** Hypothesis only, observed once, four trades. Confidence very low. Not a rule.
- **Implication:** Taken together with the RSI result, the recent entries that were "oversold" were not rewarded over 10 sessions. This is consistent with a falling-knife pattern but cannot be distinguished from the four-trade noise floor.
- **Note:** This is the same profile as the RSI hypothesis. Do not count it as a separate test.

### Extended-momentum entries (strong 5

(The notes were cut off here by the reply limit.)

### Agent 3's final notes (not passed on)

# Working Notes for the Committee Editor (Bundle 6 of 6)

**Scope and caveats**
- My earlier working notes were cut off in the request, so I cannot confirm which earlier ideas held across bundles. Every claim below rests on this bundle alone (14 trades, 91 candidates across all rating levels). Any idea that appeared in earlier notes should be treated as unverified until re-tested against the other five bundles.
- The data does not say which instrument (calls, puts, or shares) each trade used, so no rule below is instrument-specific. Where I mention calls, puts, or shares, I am citing the column values, not a known trade structure.
- Sample sizes are small. Treat all confidence levels below as provisional.

---

## 1. Results Summary

- Total profit: -$89 on 14 trades. Average return -0.6%, median +0.5%, 50% winners (7 of 14).
- The mean sits below the median because two large losses (-26.9% and -24.6%) account for about 51.5 points of the roughly -8.8 points of summed trade returns. Position sizing and tail control matter more than hit rate here.

---

## 2. Rating Signal: Did Not Predict in This Bundle

Ten-session forward returns by rating:

| Rating | Stocks | Mean | Median |
|---|---|---|---|
| +2 | 1 | +3.8% | +3.8% |
| +1 | 25 | +0.1% | -0.2% |
| 0 | 79 | +0.2% | -2.9% |
| -1 | 91 | +0.3% | -0.4% |
| -2 | 4 | +2.7% | +2.3% |

**Findings**
- Ratings did not separate winners from losers. Mean returns are essentially flat across +1, 0, and -1, and the -1 group outperformed the +1 group on average.
- The -2 group (4 stocks) had a positive mean, so negative ratings did not identify stocks to avoid or short.
- Rating 0 shows a large gap between mean (+0.2%) and median (-2.9%). A small number of big winners pulls the mean up while most stocks in that group fell. Medians and hit rates are more informative here than means.
- The +2 result is a single stock and carries no weight.

**Decisions**
- **Drop:** "Negative rating = short or avoid." No support in this bundle (4 stocks at -2, 91 at -1, both with non-negative forward returns). Confidence this is not predictive: moderate, based on one bundle.
- **Drop:** "+1 = buy." Mean +0.1%, median -0.2%. No edge over the other ratings. Confidence: moderate.
- **Hold:** The rating scale as a whole is unvalidated. Do not size positions on rating alone until it shows a separation in at least two or three bundles.

---

## 3. Trade-Level Patterns

### Rule A: Avoid entries far above the 20-day moving average (vs ma20 % > ~5)
- Trades with vs ma20 above 5%: 5 trades, average -11.5%, median -10.3%. Four of five lost. The one winner (+5.5%) had vs ma20 of 7.2%.
- Trades with vs ma20 at or below 5%: 9 trades, average +5.4%, median +3.8%. Seven of nine won.
- The two worst trades (-26.9%, -24.6%) were both in the extended group (vs ma20 of 13.8% and 5.1%).
- **Evidence:** 14 trades, one bundle. The gap is large but the sample is small and not yet confirmed out of sample.
- **Confidence:** Low-to-moderate. Worth testing in the next bundles as a filter, not as a standalone signal.

### Rule B: Be cautious after sharp short-term spikes in low-priced stocks
- Price under $10: 3 trades, average -11.1%, median -10.3%. Two losses were large.
- The worst trade had 1d % +4.2, 5d % +14.8, and vs ma20 % +13.8.
- The third trade in this group had 1d % +11.0 and 5d % +8.6, and lost 10.3%.
- The one winner in this group (+3.8%) had 5d % +10.0 but off-high % of -9.5, so it was not at a fresh spike.
- **Evidence:** 3 trades. Too few to state a rule with confidence.
- **Confidence:** Low. Possibly overlaps with Rule A, since the same stocks were extended. Do not treat as separate until tested.

### Rule C: Price bucket (weak, possibly confounded)
- Under $10: average -11.1% (3 trades)
- $10 to $50: average +1.3%, median +1.2% (7 trades)
- Over $50: average +4.0%, median +2.7% (4 trades)
- **Evidence:** 14 trades. Price bucket may simply be proxying for extension and volatility (see Rule A and below).
- **Confidence:** Low. Use as a context variable, not as a filter.

### Volatility (vol20 %)
- The worst trade had vol20 of 8.1%, the highest in the bundle. Only one other trade exceeded 5%, and that was a large loss as well.
- Winners ranged from about 1.7% to 4.4%.
- Possible pattern: high 20-day volatility increases the size of losses. One trade is not enough to confirm this.
- **Confidence:** Low. Monitor.

### RSI
- Winners had RSI values between about 41 and 65. Losers were in a similar range (50 to 62), and one winner had RSI 14. No usable RSI threshold emerged.
- **Decision:** No RSI rule. Note that RSI did not separate outcomes in this bundle.

### Short interest and put/call columns
- The two largest-short-interest trades had mixed results: one lost -10.7% range (short 17.0) and another won +10.7% (short 17.0 at the same level), so short interest alone does not separate outcomes.
- The put/call drop column showed large values in both winners and losers. No consistent direction.
- **Decision:** No rule. Insufficient signal.

### Other columns (medium, long, otm, 20d %, off high %)
- Off-high % and 20-day % did not show a usable split. The worst trades had off-high of -20.3% and -14.9%, but winners also spanned that range.
- Winners with long-term (long) readings above about 5 appeared in both the $10 to $50 and over-$50 groups. Too few trades to make a claim.
- **Decision:** No rules from these columns this bundle.

---

## 4. Position Sizing and Tail Risk

- The two largest losses (about -26.9% and -24.6%) account for more than the total net loss. Average trade return is negative only because of these tails.
- Median trade return (+0.5%) is positive, so the typical trade was not a loser.
- **Recommendation:** Cap per-trade size so that a single extended-stock loss cannot dominate a bundle. Confidence: moderate, since tail losses are a recurring feature of small-sample results.

---

## 5. Ideas Dropped or Downgraded

| Idea | Status | Reason |
|---|---|---|
| Negative rating as short or avoid signal | Dropped | Negative-rated stocks had non-negative average forward returns (+0.3% at -1, +2.7% at -2). |
| +1 rating as a buy signal | Dropped | No edge over neutral or negative ratings in this bundle. |
| Rating scale as a whole | Unvalidated | No separation across rating levels. Needs testing in other bundles. |
| Short interest as a standalone filter | Dropped for now | Mixed results at the same short-interest level. |
| RSI thresholds | Dropped for now | No separation found. |
| Buying after 5-day spikes (any price) | Downgraded to Rule B | Only three low-priced trades showed the pattern; overlaps with extension. |

---

## 6. Ideas to Test Next

1. **Extension filter:** Compare outcomes for entries with vs ma20 above versus below 5% across the other five bundles. This is the most promising finding here.
2. **Rating validation:** Measure whether the rating separates forward returns in each bundle separately. If it does not hold in two or more bundles, retire it.
3. **Volatility cap:** Test whether excluding vol20 above about 5% reduces tail losses without removing too many winners.
4. **Tail management:** Test a per-trade size cap or stop rule for extended low-priced names.
5. **Instrument tracking:** Record which instrument each trade used. Without this, we cannot tell whether losses come from the stock, the instrument, or the expiry/strike choice.

---

## 7. Confidence Summary

| Finding | Trades | Bundles | Confidence |
|---|---|---|---|
| Rating does not predict forward returns | 91+79+25+4+1 stocks | 1 | Moderate |
| Extended entries (vs ma20 > 5%) underperform | 5 vs 9 trades | 1 | Low–moderate |
| Low-priced, post-spike entries lose | 3 trades | 1 | Low |
| High vol20 associated with large losses | 1–2 trades | 1 | Low |
| Price bucket differences | 3/7/4 trades | 1 | Low |
| Tail losses dominate net P&L | 14 trades | 1 | Moderate |

### Agent 4's final notes (not passed on)

# Working Notes: Final Version for Committee Editor

## 0. Scope and caveats (read first)

- **Only bundle 6 is verified here.** My working notes were cut off, so I cannot see what I wrote before bundle 6 or what bundles 1 to 5 showed. Every "bundles held" claim below is therefore **unverified**. Where a rule is listed, it rests on bundle 6 alone unless I say otherwise. Please replace the "bundles" field with the counts from the earlier notes if they are available.
- **Sample sizes are tiny.** Bundle 6 has 18 stock trades and 2 option trades. Rules drawn from 6 to 18 trades are hypotheses to test, not settled edges.
- **Ratings sample is larger.** The rating-bucket results cover every candidate I rated (about 200), not only the traded ones, so they are more reliable than the trade-level splits.

## 1. Bundle 6 results in brief

- Total profit: **-$1,498** on 20 trades. Average -7.5%, median -1.6%, 40% winners.
- Stock trades (18): average **+0.8%**, median **-0.8%**. The stock book was roughly flat.
- Option trades (2): 30-day calls at +15% (double_or_10) at **-68.5%**, and 30-day calls at +10% (hold10) at **-95.3%**. Both were total losses of premium.
- The arithmetic checks out: (18 × 0.8 − 68.5 − 95.3) / 20 ≈ −7.5%. **The option trades produced essentially all of the loss.** The stock selection was approximately break-even.

## 2. Rating calibration (all candidates, 10-session forward return)

| Rating | n | Average | Median |
|---|---|---|---|
| +2 | 4 | -0.1% | -2.7% |
| +1 | 33 | -0.1% | -0.2% |
| 0 | 86 | +2.6% | +0.6% |
| -1 | 74 | -2.3% | -3.3% |
| -2 | 3 | +2.0% | -3.5% |

Findings:

- **Negative ratings worked directionally.** Rating -1 had a median of -3.3% against +0.6% for rating 0, a spread of about 3.9 points. Confidence: moderate, given one bundle.
- **Positive ratings did not add value.** Rating +1 and +2 combined (n=37) had medians of -0.2% and -2.7%, below the neutral group. Rating 0 outperformed both on median and average. This is the most important calibration problem in bundle 6.
- **Rating -2 (n=3) is uninformative.** Ignore it.
- **Action:** treat -1 as a avoid or exclude signal. Stop using +1 and +2 as buy signals until they show a positive median in a later bundle. Confidence in the +1/+2 failure: moderate; in the -1 signal: moderate.

## 3. Stock-trade rules (18 trades, bundle 6)

### 3a. Rule that held up best: price relative to the 20-day moving average (vs ma20)

- **vs ma20 > 0 (11 trades):** 8 winners, 3 losers, average about **+5.9%**. Median well above zero.
- **vs ma20 < 0 (7 trades):** 0 winners, average about **-7.2%**. This includes the worst stock trade (-25.5%, vs ma20 -11.7%).
- Losers above ma20 were the two trades with vs ma20 of 5.4 and 6.5 that still fell, plus one at 0.7. The best winners clustered at vs ma20 between 0.4 and 3.4.
- **Rule:** enter stocks only with vs ma20 > 0. Avoid stocks below ma20. Consider not chasing extended readings (vs ma20 above about 6%), since two of the three losers above ma20 were in that range.
- **Confidence:** moderate on direction (the split is clean), low on the exact threshold. Test whether 0 to 4% outperforms 4% and above in the next bundle.

### 3b. Drawdown from the 52-week high (off high)

- **Off high at or below -19% (6 trades):** all 6 were zero or negative, average about **-6.2%**. This includes -44.9%, -38.1%, -31.8%, -23.7%, -23.4%, -19.3%.
- **Off high of -9% or shallower:** most winners came from here.
- **Rule:** avoid stocks more than about 19% below their 52-week high. Confidence: moderate, since it overlaps with 3a (deep drawdowns were also below ma20).

### 3c. Combined weak-trend filter

- Stocks that were below ma20 **and** more than 19% off the high: all losers in this bundle. Strong candidate filter, but it is largely a restatement of 3a and 3b, so do not count it as independent evidence.

### 3d. Momentum chasing

- The stock with a 20-day gain of +15.8% and vs ma20 +5.4% lost -9.5%. Single trade. Possibly a warning against buying after large 20-day runs, but confidence is low. Watch whether 20-day gains above about 10% lose money in future bundles.

### 3e. Ideas to drop (no usable signal in bundle 6)

- **Put/call ratio, put/call drop, call and put volumes (calls, puts, medium, long, shares):** winners and losers overlapped heavily. No threshold separated them. Drop as entry filters for now.
- **One-day move (1d %) and five-day move (5d %):** big up days (+8 to +11%) appeared in both winners and losers. Drop.
- **Price band:** the under-$10, $10 to $50, and over-$50 bands all contained winners and losers. Price did not separate outcomes. Drop as a filter.
- **RSI:** winners ranged from about 41 to 65, losers from 16 to 69. No stable band. Weak; keep as a monitored column only.
- **20-day move alone:** mixed. Negative 20-day moves dominated losses, but the link is mostly through 3a and 3b.

## 4. Option-trade rules (2 trades, bundle 6)

- **Both 30-day call trades lost more than two-thirds of premium.** One was -68.5% (+15% target, double_or_10 exit) and the other -95.3% (+10% target, hold10 exit). The exit structures did not protect against losses.
- **Shared setup of the two losers:** price $10 to $50, vs ma50 about -6.2% (both), off high -18% to -27%, and 30-day calls with out-of-the-money measures of about 6 to 10. One had rsi 49 and the other 51, so RSI was neutral.
- **Rule (provisional):** do not buy 30-day out-of-the-money calls on stocks that are below their 50-day average and well off their highs. This is consistent with 3a and 3b.
- **Sizing rule:** until an option strategy shows an edge over at least 10 trades, cap option risk per trade so that a total loss cannot dominate the book. Two trades sank the bundle.
- **Confidence:** high that the option sizing and structure cost money here; low on any specific option threshold, since n=2.
- **Exit observation:** the hold10 exit did not stop the loss. A stop-loss or shorter expiry is worth testing, but I have no evidence yet on which works.

## 5. What I learned (new in bundle 6)

1. **The stock signal and the option signal are different problems.** My stock selection was close to neutral (+0.8% average), but my option selection was destructive. Keep the two evaluated separately.
2. **Trend position matters more than the flow columns.** vs ma20, vs ma50, and off-high distance separated outcomes; put/call and volume columns did not.
3. **Negative ratings are more reliable than positive ones.** Use the rating scale asymmetrically: exclude on -1, do not promote on +1 or +2.
4. **Option losses are fast and total.** A premium loss of 68% to 95% in 30 days means one option trade can outweigh about 10 average stock trades. Size accordingly.
5. **Small samples mislead.** The bundle 6 option results would look like a trend if I had only two data points in a bundle, and they could easily be bad luck. Keep recording trades before drawing conclusions.

## 6. Open questions for the next bundle

- Does vs ma20 > 0 still separate winners from losers, and at what threshold does it stop working?
- Do stocks more than 19% off the high keep losing money out of sample?
- Does rating +1 or +2 ever show a positive median? If not after another bundle, drop it.
- Are 30-day calls ever profitable in this setup, or should options be paused entirely until one structure shows an edge?
- Test a shorter expiry or a stop-loss on option trades, rather than hold10.
- Re-check the 20-day-run-up warning (section 3d) with more trades.
- Log which earlier-bundle rules have replicated, so each rule's "bundles held" field reflects real data.

## 7. Summary table of rule status

| Rule | Status | Evidence (bundle 6) | Confidence |
|---|---|---|---|
| Buy only when vs ma20 > 0 | Keep | 11 trades, avg +5.9%; below ma20: 7 trades, avg -7.2% | Moderate |
| Avoid off high ≤ -19% | Keep | 6 trades, all ≤ 0, avg -6.2% | Moderate |
| Exclude rating -1 | Keep | Median -3.3% vs +0.6% for rating 0 (n=74) | Moderate |
| Promote rating +1 or +2 | Drop | Medians -0.2% and -2.7% (n=37) | Moderate |
| No 30-day OTM calls on weak trend setups | Keep | 2 of 2 lost 68% to 95% | High on losses, low on pattern |
| Cap option risk per trade | Add | Two option losses exceeded the stock book's profit | High |
| Put/call, volume, 1-day, price band as filters | Drop | No separation | Moderate |
| Avoid chasing 20-day runs above about 10% | Watch | 1 trade, -9.5% | Low |
| Test shorter expiry or stop on options | Add | hold10 exit failed to limit loss | Low (no test yet) |

