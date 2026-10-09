# Committee generations (2026-10-09 19:08 UTC)

Total spent on all agent runs: $2.99. Candidate pool: {'train': 2998, 'score': 1439, 'holdout': 2000, 'test': 2720}.

Four agents train independently on six stock bundles; code scores their rules; an editor writes the
notes passed on. The scoring run trades blind months with the editor's notes. "Random" makes the same
number and kind of trades on random candidates in the same weeks. Rating correlation: does a higher
rating go with a better 10-session stock return (0 = no skill, ranges are 95%). Every trade is $1,000.

## Runs

| gen | who | phase | trades | profit $ | random profit $ | mean % | win % | rating corr (95% range) | top rated % | bottom rated % | unreadable | cost $ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | agent1 | train | 233 | 88953.0 | 11743.2 | 38.18 | 30.0 | -0.027 (-0.085 to 0.031) | -1.79 | 0.53 | 1/151 | 0.269 |
| 1 | agent2 | train | 298 | 111695.7 | 28190.8 | 37.48 | 29.2 | 0.034 (-0.019 to 0.095) | 1.85 | -0.3 | 0/151 | 0.2573 |
| 1 | agent3 | train | 249 | -427.4 | 27016.5 | -0.17 | 28.5 | -0.013 (-0.073 to 0.044) | 0.12 | 0.41 | 1/151 | 0.271 |
| 1 | agent4 | train | 213 | 69348.1 | 36060.9 | 32.56 | 31.0 | 0.045 (-0.012 to 0.096) | -0.35 | -0.19 | 0/151 | 0.2744 |
| 1 | scorer | score | 271 | 15275.1 | 14905.0 | 5.64 | 31.7 | -0.031 (-0.089 to 0.018) | 1.38 | 1.64 | 5/144 | 0.2811 |

## Luck check

- Different rules tested on training data so far: 28 (by the agents and the editor).
- Editor rules checked on the blind months: 8; passed clearly (whole 95% range above buying everything the same way): 0.
- Expected to pass by luck alone: about 0.2. Treat a pass as real only if it clearly beats that count and the rule keeps passing in later generations.

## Blind scoring trades by list (hindsight check)

The big-mover list was chosen for stocks that later had 3+ days up 15%, so results there can come
from hindsight alone. The wide list (chosen from January 2024 data only) is the honest test.
Random = the same kind of trades on random candidates from the same list in the same weeks.

| gen | list | trades | mean % | random mean % | profit $ | random profit $ |
|---|---|---|---|---|---|---|
| 1 | big movers (hindsight) | 202 | +7.36 | -6.12 | +14,858 | -12,366 |

## Generation 1

### Editor's rules, tested on all training months and bundles

- under10_90d_10otm (when price = <$10: buy the 90-day call 10% above the price, exit hold10): 159 trades, average +54.9% (95% range -2.8% to +163.9%, resampling whole weeks), median -18.6%, 36% winners. Buying every candidate the same way: +16.0%. Beat that in 6 of 6 bundles; first half of the months +108.5%, second half +4.7%.
- callspike3_5d_up (when calls >= 3 and 5d % > 0: buy the 30-day call 0% above the price, exit hold10): 467 trades, average +24.1% (95% range -7.8% to +82.6%, resampling whole weeks), median -39.0%, 33% winners. Buying every candidate the same way: +4.0%. Beat that in 4 of 6 bundles; first half of the months +36.4%, second half +11.1%.
- ma20_runup15_30d_5otm (when vs ma20 % > 0 and 20d % > 15: buy the 30-day call 5% above the price, exit hold10): 446 trades, average +13.9% (95% range -5.0% to +33.6%, resampling whole weeks), median -48.8%, 29% winners. Buying every candidate the same way: +7.7%. Beat that in 4 of 6 bundles; first half of the months +10.9%, second half +16.7%.
- extended_runup_90d_10otm (when 20d % >= 7 and vs ma50 % >= 10: buy the 90-day call 10% above the price, exit hold10): 121 trades, average +60.5% (95% range -9.9% to +188.2%, resampling whole weeks), median -18.6%, 36% winners. Buying every candidate the same way: +16.0%. Beat that in 5 of 6 bundles; first half of the months +204.7%, second half -3.0%.
- fiveday_surge_90d_5otm (when 5d % > 10: buy the 90-day call 5% above the price, exit hold10): 100 trades, average +69.8% (95% range -16.0% to +229.4%, resampling whole weeks), median -24.9%, 34% winners. Buying every candidate the same way: +11.5%. Beat that in 4 of 6 bundles; first half of the months +146.7%, second half -10.3%.
- under10_callspike3_30d_5otm (when price = <$10 and calls >= 3: buy the 30-day call 5% above the price, exit hold10): 282 trades, average +40.0% (95% range -11.9% to +125.2%, resampling whole weeks), median -47.2%, 30% winners. Buying every candidate the same way: +7.7%. Beat that in 4 of 6 bundles; first half of the months +63.5%, second half +15.8%.
- combo_spike5_up_ma20_runup (when calls >= 5 and 5d % > 0 and vs ma20 % > 0 and 20d % > 15: buy the 30-day call 5% above the price, exit hold10): 155 trades, average -10.0% (95% range -32.4% to +21.9%, resampling whole weeks), median -55.9%, 25% winners. Buying every candidate the same way: +7.7%. Beat that in 2 of 6 bundles; first half of the months -31.4%, second half +12.3%.
- crash_knife_90d_10otm (when 5d % <= -10 and 1d % <= -5: buy the 90-day call 10% above the price, exit hold10): 24 trades, average +36.8% (95% range -15.8% to +115.2%, resampling whole weeks), median -27.8%, 46% winners. Buying every candidate the same way: +16.0%. Beat that in 2 of 4 bundles; first half of the months +79.9%, second half +10.9%.

### The same rules on the blind scoring months (never shown to agents)

- under10_90d_10otm (when price = <$10: buy the 90-day call 10% above the price, exit hold10): 99 trades, average -5.5% (95% range -19.8% to +15.4%, resampling whole weeks), median -19.1%, 30% winners. Buying every candidate the same way: +2.9%. Beat that in 2 of 6 bundles; first half of the months -6.7%, second half -3.7%.
- callspike3_5d_up (when calls >= 3 and 5d % > 0: buy the 30-day call 0% above the price, exit hold10): 287 trades, average -4.8% (95% range -19.0% to +11.8%, resampling whole weeks), median -40.0%, 30% winners. Buying every candidate the same way: -1.6%. Beat that in 4 of 6 bundles; first half of the months -11.4%, second half +3.4%.
- ma20_runup15_30d_5otm (when vs ma20 % > 0 and 20d % > 15: buy the 30-day call 5% above the price, exit hold10): 280 trades, average -2.3% (95% range -19.0% to +16.1%, resampling whole weeks), median -48.3%, 30% winners. Buying every candidate the same way: -1.4%. Beat that in 2 of 6 bundles; first half of the months -4.7%, second half +0.1%.
- extended_runup_90d_10otm (when 20d % >= 7 and vs ma50 % >= 10: buy the 90-day call 10% above the price, exit hold10): 83 trades, average -2.1% (95% range -19.1% to +22.9%, resampling whole weeks), median -20.4%, 31% winners. Buying every candidate the same way: +2.9%. Beat that in 1 of 6 bundles; first half of the months -15.2%, second half +11.4%.
- fiveday_surge_90d_5otm (when 5d % > 10: buy the 90-day call 5% above the price, exit hold10): 68 trades, average -3.6% (95% range -24.0% to +25.9%, resampling whole weeks), median -22.0%, 25% winners. Buying every candidate the same way: -1.4%. Beat that in 2 of 6 bundles; first half of the months -12.1%, second half +5.0%.
- under10_callspike3_30d_5otm (when price = <$10 and calls >= 3: buy the 30-day call 5% above the price, exit hold10): 179 trades, average -3.6% (95% range -20.4% to +15.0%, resampling whole weeks), median -43.3%, 30% winners. Buying every candidate the same way: -1.4%. Beat that in 3 of 6 bundles; first half of the months -0.9%, second half -7.6%.
- combo_spike5_up_ma20_runup (when calls >= 5 and 5d % > 0 and vs ma20 % > 0 and 20d % > 15: buy the 30-day call 5% above the price, exit hold10): 118 trades, average -0.7% (95% range -27.7% to +36.0%, resampling whole weeks), median -49.1%, 30% winners. Buying every candidate the same way: -1.4%. Beat that in 2 of 6 bundles; first half of the months -16.7%, second half +14.7%.
- crash_knife_90d_10otm (when 5d % <= -10 and 1d % <= -5: buy the 90-day call 10% above the price, exit hold10): 9 trades, average -5.9% (95% range -31.5% to +21.9%, resampling whole weeks), median -10.3%, 44% winners. Buying every candidate the same way: +2.9%. Beat that in 0 of 1 bundles; first half of the months +1.6%, second half -11.9%.

### Editor's notes (passed to the next generation)

# Options-Flow Playbook: Committee Notes for the Next Generation

## 0. Bottom line

- **No option setup has passed the pass test yet.** Every configuration the code tested has a negative median return (typically −18% to −50%). Positive averages come from a small number of very large winners. Any option idea must be treated as unvalidated until its median is positive, net of costs.
- **The best-supported lead is the under-$10 band.** It beat the same-configuration all-candidate baseline in most bundles across two different option setups. It is still a losing trade on the median.
- **The most stable-looking momentum and flow combinations** are the call-spike-with-5-day-up rule, the 5-day surge, and the above-MA20 with 20-day run-up rule. Each has a positive average in both halves of the test period, though none has a positive median.
- **The biggest unresolved question** is why option results are so much worse than the stock moves behind them. Until that is measured, the next generation should not trust any per-trade option P&L.

## 1. How to read the scorebook

- **"Beat baseline in X of N bundles"** compares each rule with buying every candidate the same way in the same bundle, not with zero. The all-candidate figures differ by configuration: +4.0% for 30-day at-the-money calls, +7.7% for 30-day 5%-out-of-the-money calls, +11.5% for 90-day 5%-out calls, and +16.0% for 90-day 10%-out calls.
- **Median is the decision number.** Averages are inflated by tails. A rule with a 60% average and a −20% median is a lottery ticket, not an edge.
- **"Halves"** are the first and second halves of the test months. A rule whose average is positive in both halves is more credible than one that is strong in one half and negative in the other.
- **Scorebook numbers supersede any figure the traders quoted** and are the basis for the tables below.

## 2. STRATEGY: setups worth carrying forward (paper, not capital)

None of these clears the pass test. They are ranked by strength of code evidence.

### Tier A: most consistent code evidence

**A1. Under-$10 band (control with the strongest relative record)**
- 90-day, 10% out-of-the-money, exit after 10 sessions: 159 trades, average +54.9%, **median −18.6%**, 36% winners. Beat the all-candidate baseline in **6 of 6 bundles**. Halves: +108.5% and +4.7%.
- 30-day, 5% out-of-the-money control: 657 trades, average +30.6%, median −46.6%, 29% winners. Beat the baseline in 5 of 6 bundles. Halves: +47.3% and +13.9%.
- **Read:** Cheap names are a consistent source of large winners and of large losers. The median is still negative. The band has the least negative medians among the large samples, which makes it the best place to test a sizing or structure change. Traders disagreed on this, so treat it as a lead.

**A2. Call spike with 5-day up (30-day at-the-money)**
- Condition: calls ≥ 3 and 5-day change > 0.
- 467 trades, average +24.1%, median −39.0%, 33% winners. Beat baseline in 4 of 6 bundles. Halves: +36.4% and +11.1%.
- **Read:** the largest sample with positive averages in both halves. The median is still negative.

**A3. Above-MA20 with 20-day run-up (30-day, 5% out-of-the-money)**
- Condition: price above its 20-day average and 20-day change > +15%.
- 446 trades, average +13.9%, median −48.8%, 29% winners. Beat baseline in 4 of 6 bundles. Halves: +10.9% and +16.7%.
- **Read:** the most stable across halves of any large sample. Weak median.

### Tier B: strong on average, unstable in time

**B1. Extended run-up (90-day, 10% out-of-the-money)**
- Condition: 20-day change ≥ +7% and price ≥ +10% above its 50-day average.
- 121 trades, average +60.5%, median −18.6%, 36% winners. Beat baseline in 5 of 6 bundles. Halves: **+204.7% and −3.0%**.
- **Read:** nearly all the gain came in the first half. Treat as a lead that may be regime-dependent.

**B2. Five-day surge (90-day, 5% out-of-the-money)**
- Condition: 5-day change > +10%.
- 100 trades, average +69.8%, median −24.9%, 34% winners. Beat baseline in 4 of 6 bundles. Halves: +146.7% and −10.3%.
- **Read:** same pattern as B1: strong first half, weak second half.

**B3. Dip below the 50-day average, up on the day (30-day, at-the-money)**
- Condition: price ≥ 10% below its 50-day average and up on the day.
- 151 trades, average +19.0%, median −27.4%, 36% winners. Beat baseline in 4 of 6 bundles. Halves: +69.2% and −0.3%.
- The 90-day, 10%-out version of the same idea did worse: 36 trades, average −7.0%, median −17.9%, beat baseline in only 2 of 5 bundles. **The expiry and strike seem to matter.** Test the 30-day at-the-money version first.

### Tier C: weak but not dead

- **Overbought (RSI > 70), 30-day at-the-money:** 291 trades, average +13.8%, median −34.7%, beat baseline in 4 of 6 bundles. Not a loser by average. Not a winner by median. Agent 1 labelled it "expect loss"; the code does not support that label.
- **Crash knife (5-day ≤ −10% and 1-day ≤ −5%), 90-day, 10%-out:** 24 trades, average +36.8%, median −27.8%, **46% winners (highest win rate in the scorebook)**. Beat baseline in 2 of 4 bundles. Small sample.
- **Call spike above 5× (30-day, 5%-out):** 453 trades, average +20.8%, median −49.7%, beat baseline in 3 of 6 bundles. Stronger than the 2×–4× bucket, which is negative (see avoid list).

## 3. STRUCTURE AND EXECUTION (applies to any test)

- **Instrument:** long calls only, in every test so far. Spreads have not been tried (see new ideas).
- **Expiry:** 30-day and 90-day only. 14-day calls are banned by all four traders.
- **Strike:** no strike has a positive median across bundles. The 10%-out band had a positive median in one bundle and a negative one in another. Treat strike choice as open.
- **Exit:** hold 10 sessions. The double-or-10 exit was dropped by every trader that tested it. Exits other than hold-10 are not yet compared on a matched basis.
- **Sizing:** 1% of the book per trade (2% maximum), total open option premium no more than about 10% of the book. Most trades lose most of their premium, so size on the assumption of a full loss.
- **Logging for every trade:** strike as % of price, days to expiry, bid, ask, fill, mid at entry and exit, open interest, rule that triggered, rating if used, and the stock's 10-session return on the same name. Without the last field, option losses cannot be separated from stock moves.
- **Process:** hard limits on trade count and stand-down periods must be enforced by the system, not discipline. One trader broke both in bundle 6.

## 4. WHAT TO AVOID

**Structural avoids (high confidence):**
- **Far out-of-the-money strikes (15%+ and 20%+):** consistently negative medians (one trader's 30-day 20%-out median was −70.6%).
- **14-day calls at any strike:** near-total losses in every bundle tested.
- **Blind call buying on all candidates:** the broad 30-day at-the-money control (1,750 trades) has a median of −39.0% and beat itself in 0 of 6 bundles. The average of +4.0% depends on tails.
- **Chasing one-day shocks:** the "vol above 6% and 1-day above +15%" rule has an average of −26.6% and median −53.3% (30-day, 5%-out), beating baseline in only 1 of 6 bundles. The "1-day above +15%" rule on 90-day calls is also negative (average −14.4%, median −40.9%).

**Rules the code did not confirm (avoid as a positive signal):**
- **Deep below the 60-day high (≤ −20%), 30-day 5%-out:** average −9.5%, median −49.7%, beat baseline in 2 of 6 bundles.
- **Call spike 2×–4× (30-day 5%-out):** average −8.4%, median −44.5%, beat baseline in 2 of 6 bundles.
- **Oversold (RSI < 35) with put/call < 0.5:** average +1.0%, median −36.0%, beat baseline in 3 of 6 bundles.
- **Oversold 5-day drop (RSI < 35, 5-day ≤ −10%), 90-day 10%-out:** average +1.5%, median −23.8%, beat baseline in 1 of 4 bundles.
- **Quiet call buying** (large call spike with calm shares and price): the research team found fewer big moves than average. Not used.
- **Put/call collapse alone:** no predictive power in any test.

**Stock ratings:** do not trade on them, or on their inverse. The +1 group reversed sign across bundles. The −2 group may be a weak exclusion, but the sample is about 16 stocks across bundles.

## 5. Where the traders agreed and disagreed

**Agreed:**
- Option medians are negative in every bundle for every configuration. Positive averages depend on a few trades above +100%.
- The typical candidate stock is flat to down over 10 sessions (median stock 10-session return negative in most bundles). Stock-level upside tails (above +20%) are roughly 5% of candidates.
- Price band, RSI, volatility, and put/call do not separate winners from losers in trade-level data.
- Stand-down and trade-cap rules must be enforced automatically.
- Full candidate data with 10-session returns, and stock returns for the traded names, are needed to measure anything.

**Disagreed:**
- **Strike:** Agent 1 says at-the-money only, excluding 5%+ out. Agent 4 favors 10%-out on 90-day. Agent 3 says 20%-out was least bad through bundle 5. Agent 2 saw 30-day 5%-out as positive in one bundle and negative in another. The code shows 5%-out averages can be positive while medians remain negative.
- **Expiry:** Agent 4 favors 90-day, Agent 1 and 2 favor 30-day, Agent 3 says 90-day beats 30-day only sometimes.
- **Overbought and oversold:** Agent 1 saw RSI as a warning sign. Code shows overbought is not worse than baseline by average, and oversold is weak in both directions.
- **Diagnosis:** Agent 1 thinks execution and measurement are the main problem. Agent 4 thinks decay, implied volatility change, and spreads explain the gap. Agent 2 and Agent 3 closed the program, reading the negative medians as a signal problem.
- **Rating:** Agent 4 logs +1 and −2 as weakly informative. Agent 2 and Agent 3 dropped rating as noise.

## 6. NEW IDEAS TO TEST (untested)

Credit: the code confirmed the under-$10 band, the call-spike-with-5-day-up rule, the above-MA20 with 20-day run-up rule, and the extended run-up rule. The ideas below build on them or address the structural gap.

1. **Call debit spreads instead of naked calls (untested).** A long call with a short call further out caps the premium and reduces exposure to decay and implied-volatility changes. Apply it first to the under-$10 band and the extended run-up. Compare median return, not average. Its main attraction is that it may turn a negative-median setup into something closer to break-even.

2. **Implied-volatility cheapness filter (untested).** Log implied volatility rank at entry, and test buying only when it is below its own 60-day history. This tests Agent 4's implied-volatility hypothesis directly. If the premium is expensive at entry, a flat stock can still lose money. Do this with the decomposition (below) first.

3. **Decomposition test (untested, no new money).** For each paper trade, record the stock's 10-session return, the entry and exit premium, and the premium return that the stock move alone would have implied (using delta). The gap is the structural cost of decay, implied-volatility change, and spread. If the gap explains most of the loss, the problem is the instrument, not the signal.

4. **Volatility-scaled strike (untested, creative).** Instead of a fixed percent out-of-the-money, set the strike at a multiple of the expected 10-session move (vol20 times the square root of 10). This asks whether the strike needs to be reached, rather than assuming a fixed percentage works across stocks with very different volatility. Test it on the under-$10 band and the call-spike rule.

5. **Long-dated arm for decay (untested).** Test 120–180 days on the under-$10 band and the extended run-up. If losses are mostly decay, longer expiry should show a smaller premium loss for the same stock move.

6. **Shares control on the same signals (untested, gate test).** Equal-dollar long positions in shares for the under-$10 band, the extended run-up, the call-spike-with-5-day-up rule, and the above-MA20 rule, held 10 sessions, reporting median, mean, and both tails. If shares do not show a positive median, no option structure can be expected to produce one. This should run before any further option test.

7. **Combined flow and price filters (untested).** Test the intersection of the best rules: call spike ≥ 5× with 5-day up and above MA20 with 20-day run-up. Also test the under-$10 band as a filter on the call-spike rule. Require each combination to beat its own components on the median.

8. **Crash-knife with a longer horizon (untested).** The one-day-crash knife had the highest win rate in the scorebook (46%), but a negative median. Test it with 120–180-day expiry and with a hold of 20 sessions rather than 10, to see whether it needs more time to pay.

9. **Stock-level tail gate (untested).** Before testing any further options, measure the 10-session stock upside tail (above +20%, +50%) for each feature group on the full table. Pre-register a threshold (for example, 1.5× the all-candidate rate with at least 15 candidates). Only groups that pass should be tested with options.

## 7. OPEN QUESTIONS

- **Why are option medians so much worse than the stock median?** This is the largest open question. Until the decomposition runs, no option result should be read as evidence about signals.
- **Does the under-$10 advantage survive a shares test?** If it does, it is a stock-level effect that options may only be amplifying. If not, it is an option-pricing artifact.
- **Is the strong first half of the extended run-up and 5-day surge rules a regime effect?** Two of the best-looking rules lost money in the second half. The next generation should check whether the market condition changed, not only whether the rule still works.
- **Do rules that beat baseline by average also beat it by median when the sample is larger?** Most positive averages in the scorebook rest on fewer than 500 trades with tails above +100%.
- **Does the call-spike signal predict volatility rather than direction?** The research team found big moves in both directions after 10% weeks. If so, the right structure may be neither a call nor a put, but a volatility structure. This has not been tested.
- **Data gap:** full candidate tables with every column and 10-session returns, and stock returns for every traded name, have not been supplied in bundles 3 to 6. Every filter test in those bundles relied on extreme lists or summaries. The next data delivery should include them.

## 8. Process rules for the next generation

- Judge each configuration by its **median net of costs**, its **trimmed mean** (largest trade removed), the **share of total profit from the largest trade**, and the **halves**. Never headline the raw average or the total profit.
- A configuration is a lead only when it beats its own all-candidate baseline in most bundles and its median is positive in at least two separate bundles.
- Pre-register any new rule, its strike and expiry, and its exit before the bundle is run.
- Log every candidate, including skipped ones, and the rule that stopped it.
- Keep paper and real-money logs separate, and enforce stand-down periods in the system.

### Agent 1's final notes (not passed on)

# Options-Flow Candidates: Working Notes (Final, after Bundle 6 of 6)

## 1. Current Strategy and Rules

### Status: suspended. No trades until the execution audit passes.

- Trading stays suspended. Bundle 6 was supposed to be a zero-trade stand-down, but the record shows 31 trades placed. That is a control failure, not a result. Those trades are non-compliant and do not count toward any decision.
- Resumption requires all of the following:
  1. The audit in section 3 is complete, with at least 10 valid trades in the audited bundles.
  2. The median on valid trades is no worse than -20%.
  3. The system enforces the stand-down and the 10-trade cap automatically, not by my discipline alone.

### The setup I am testing (a hypothesis, not an edge)

**Instrument and contract**
- Calls only. Puts are not part of the setup.
- Expiry: 30-day bucket only, about 25 to 35 calendar days to expiry at entry.
- Strike: at the money, within about 2% of the share price. Strikes 2% or more out of the money are excluded. Strikes 5% or more out are excluded on the strongest evidence I have (see section 4).

**Eligibility and ranking**
- Rating filter: skip +1 and -2. Eligible: +0 and -1. Neither has shown an edge I trust.
- Trade cap: 10 per bundle, enforced by the system. Rank eligible candidates in bundle order, not by how exciting they look, and stop at 10.
- Every trade record must include the rating, the strike as a percent of price, days to expiry, and the bid and ask at entry. A trade missing any of these is non-compliant.
- Log every candidate, including skipped ones, with the rule that stopped it.

**Entry execution check (mandatory, logged)**
- Record: strike, share price, days to expiry, bid, ask, fill price, and open interest.
- Skip if the bid-ask spread is wide relative to the premium. Log it as "skipped, spread."
- Record the mid at entry and the mid at exit next to the fills, so fill quality can be separated from the signal.

**Sizing**
- Maximum premium per trade: 2% of capital.
- Assume most trades lose most of their premium, because that is what bundles 4 to 6 show.

**Exit**
- Hold 10 sessions, no stop, no doubling. Fixed until the audit is done.

### Why this setup, and why I no longer trust the measurement

- The original logic was that ATM calls limit premium decay and that the break-even move over 10 sessions is modest. That still holds on paper.
- The trade results do not fit that logic. In bundle 6, roughly half the trades lost 50% to 100% of premium, and four lost 80% or more. Several of those losing stocks had flat or modestly up 5-day and 20-day moves. A 30-day ATM call held 10 sessions should keep a large share of its premium when the stock is flat or up. Losing 80% to 100% under those conditions points to a measurement or execution problem: wrong strike or expiry, stale or wide fills, a mismatched contract, or exit prices that were not tradable.
- The stock-level data does not explain the option losses. Across the 200 bundle-6 candidates, the average 10-session stock return was +0.3% and the median was -0.8%. The option P&L is far more negative than the stock moves.
- **Conclusion:** no per-trade option result from bundles 4, 5 or 6 can be trusted to measure the signal until the audit passes.

## 2. What I Tested in Bundle 6 and How It Went

### Headline (not valid as a strategy result)

- **31 trades** placed against a stand-down rule of zero. Profit +7,802. Average +25.2%, median -20.8%, 32% winners.
- Hold-10 subset: 28 trades, average +24.9%, median -24.9%.
- Double-or-10 exit subset: 3 trades, average +27.6%, median -5.8%. Too few to judge the exit.
- The positive total and average come from a few large winners (+448% and +672% among the 20 trades shown in detail). The median is negative, and the median is the honest number. The positive total does not mean the strategy works.

### Trade-level pattern (20 trades visible in the record)

- 10 trades lost 49.7% to 100%. Of those, 7 were in the $10 to $50 band and 3 were over $50. None were under $10.
- 10 trades gained +7% to +672%. Of those, 8 were in the $10 to $50 band and 2 were over $50.
- **Price band:** no separation. Both tails are spread across bands.
- **Medium ratio (≤1.5):** 6 of the 10 worst trades and 5 of the 10 best trades. No separation.
- **Short and long spikes, calls, puts, p/c, p/c drop, shares, RSI, vol20, 20-day move, distance from averages, drawdown:** no consistent separation between winners and losers in the visible trades. Several winners had 20-day moves near zero or negative, and several losers had 20-day moves of +2% to -8%.
- **The trade rows do not show the rating or strike percent,** so I cannot check rule compliance trade by trade. This is a logging gap, which the audit must close.

### Stock-level ratings (all 200 candidates, 10-session return)

| Rating | Stocks | Average | Median |
|---|---|---|---|
| +1 | 15 | -1.2% | -0.2% |
| +0 | 89 | +0.4% | -0.3% |
| -1 | 93 | +0.5% | -2.1% |
| -2 | 3 | -0.3% | +1.3% |
| All 200 (baseline) | 200 | +0.3% | -0.8% |

- **+1:** underperformed the baseline on average (-1.2% vs +0.3%). Over six bundles it has been mixed. It beat the baseline only in bundle 5 (8 stocks). Still skipped.
- **+0:** in line with the baseline.
- **-1:** average in line, median below the baseline (-2.1% vs -0.8%). Eligible under the rules but still no evidence of an edge.
- **-2:** 3 stocks, too few to judge. Skipped.
- **Conclusion:** ratings separate little. No rating beat the baseline by a margin I would trust in this bundle.

### Double-or-10 exit

- Three trades, median -5.8%, average +27.6%. The average depends on one or two large winners. The exit cannot be evaluated on this sample and remains untested in a clean way.

### Discipline

- Stand-down broken: 31 trades against zero.
- Cap broken: 31 trades against 10.
- Rating and strike not logged per trade.
- I cannot say from the record which trades complied with any rule. Treat all 31 as unmeasured.

## 3. What I Will Try Next

1. **Execution audit (mandatory before any trade).** For every trade in bundles 4, 5 and 6, check:
   - Strike as a percent of share price at entry (within 2%?).
   - Days to expiry at entry (25 to 35?).
   - Rating (+0 or -1?).
   - Entry and exit fills versus the displayed mid, and the bid-ask spread at each.
   - Whether the recorded P&L can be reproduced from the option's entry and exit prices. Any trade with a -80% or worse result on a flat-to-up stock is flagged invalid until explained.
   - Whether sub-$10 and over-$50 trades had abnormally wide spreads or thin open interest.
   - Whether out-of-bucket trades (the 90-day trade in bundle 5, any non-30-day trade in bundle 6) are excluded.

   Output: a list of trades marked valid or invalid with reasons. Recompute the median on valid trades only. If fewer than 10 are valid, the bundle is inconclusive.

2. **Enforce the controls in the system, not in my head.** The stand-down and the 10-trade cap must be hard limits in the order system. If the system cannot enforce them, the strategy stays suspended.

3. **Build the stock-level dataset without trading.** Continue logging every candidate with its rating, strike-rule status, expiry, spread estimate and 10-session stock return. Six bundles of stock-level data now exist. This is the cleanest evidence available and it costs nothing.

4. **Resume trading only after the audit passes.** Passing means at least 10 valid trades and a valid-trade median no worse than -20%. If the audit finds the measurement is broken, fix it and re-audit before any trade.

5. **If trading resumes:** 30-day ATM calls only, +0 or -1 only, at most 10 per bundle, every trade logged with full fills. Hold 10 sessions with no stop.

6. **Exit test (later).** Only after the audit confirms the option returns are real, compare hold-10 with a stop-loss or a time-based exit, using valid trades only. Doubling is not worth testing on a sample of three.

7. **Older price setup (not started).** Stocks more than 10% below the 50-day average but up on the day, as 30-day ATM calls under the same rules. Run it only after the audit and the controls are in place, and compare it with the same setup without the flow filter, so the flow columns have to earn their place.

## 4. Supporting Evidence and Dropped Ideas

**The 30-day ATM setup across six bundles**
- Bundle 1: average about +31% on 13 trades.
- Bundle 2: hold-10 average +12.7%.
- Bundle 3: average +436% (about +44% without one trade), median -7.5% on 26 trades.
- Bundle 4: average -36.7%, median -48.5% on 52 trades. Cap broken.
- Bundle 5: average -6.0%, median -46.5% on 32 trades. Cap broken.
- Bundle 6: average +25.2%, median -20.8% on 31 trades. Stand-down and cap broken.
- Median negative in four of six bundles. The averages are carried by a few large winners. The setup is unproven, and it may be broken by execution.

**Stock-level baseline**
- The stock-level baseline (all candidates, 10 sessions) has been close to zero: bundle 5 median -2.2%, bundle 6 average +0.3%, median -0.8%. The stocks did not fall enough to explain the option losses in bundles 4 and 5. In bundle 6, the option losses were also larger than the stock moves can explain.

**Rating evidence**
- **+1:** underperformed the baseline in bundles 1 to 4 and in bundle 6. Outperformed in bundle 5 (8 stocks). Mixed, and the total sample is small. Skip for now.
- **-2:** average returns of +4.3%, +22.9%, -0.6%, -7.2%, -0.7% and -0.3% across six bundles. No edge. Skip.
- **+0 and -1:** gaps versus baseline flip between bundles. No edge I trust.

**Strike evidence**
- OTM strikes (5% or more out of the money): every trade lost in bundles 1 and 3 (19 of 19). Keep excluded. Bundles 5 and 6 have no clean OTM sample, since the strike check was not logged per trade.

**Features tested and dropped (no consistent separation across bundles)**
- Medium ratio: no separation in bundles 4, 5 or 6.
- p/c and p/c drop.
- Calls, puts, shares, short, long and OTM spikes.
- RSI, 1-day and 5-day moves, 20-day move.
- Volatility (vol20), drawdown from the 60-day high, distance from the 20-day and 50-day averages.
- Price band: flips between bundles and between tails. Kept only as an execution concern (spread and open interest).

**Ideas dropped**
- Blind call buying (losing or tail-driven in every bundle).
- 14-day calls (losing in bundle 1, one trade in bundle 3).
- 90-day calls (too few trades to judge).
- 5% or more OTM calls (lost in every clean test).
- Put/call collapse as a standalone signal (no evidence).
- Doubling exit (three trades in bundle 6, median -5.8%; not testable at this size).

## 5. Confidence Levels

- **Avoid OTM strikes (5% or more):** high. 19 of 19 losses, no contrary evidence.
- **The option measurement is reliable:** very low. Losses of 80% to 100% on flat-to-up stocks are not explained by time decay, and bundle 6 has an unexplained gap between control and result.
- **30-day ATM hold-10 has a positive expectancy:** very low. Median negative in four of six bundles. The positive averages come from a small number of large winners.
- **Skip -2:** moderate. No edge across six bundles.
- **Skip +1:** low to moderate. Mixed; underperformed in bundle 6 on 15 stocks.
- **+0 or -1 carries an edge:** none.
- **Medium at or below 1.5 helps:** none. No separation in bundles 5 or 6.
- **Price band, p/c, RSI, drawdown, volatility, spikes carry a signal:** none found.
- **Stand-down and cap as safeguards:** the rules are sound, but they failed in bundle 6, so they are not yet working. Confidence that the system enforces them: low until the controls are built into it.

## 6. Discipline Rules (enforced regardless of results)

- No trade unless every hard rule in section 1 is met and the entry execution check is logged.
- No more than 10 trades per bundle, enforced by the system.
- Stand-down bundles are zero trades. Bundle 6 broke this. It must not happen again.
- No live or paper trading until the audit passes and the valid-trade median is no worse than -20%.
- Skip -2 without exception. Skip +1 until retested with more stocks.
- Log every candidate, rating, strike status and reason for rejection.
- Judge each bundle by the median on audited, compliant trades only. Never by the total, the average, or the headline win.
- A large winner outside the rules does not validate the strategy, and a large loser outside the rules does not disprove it. Only audited, rule-following trades count.

### Agent 2's final notes (not passed on)

# Options-Flow Trading: Final Working Notes (after bundle 6 of 6)

## 1. CURRENT STRATEGY AND RULES

### Status
**Closed. No validated setup. I am not trading options.**

Six bundles, 298 option trades, and about 1,200 stock ratings. The 30-day +10% OTM hold-10 cell, the main test cell, failed the decision rule I set after bundle 5:

- **Median:** -33.6% over 19 trades. Still negative.
- **Trimmed average (top trade removed):** about -16% over 18 trades. Still negative. The +1,235.5% winner accounts for the whole positive average (+49.5% untrimmed).

Under the rule, option trading is closed. Bundle 6 had a positive total (+11,869), but that total comes from one trade above +1,000%. The rule exists so that a single tail trade cannot reopen the program. I am following it.

Across all 44 bundle 6 trades, the trimmed average is also slightly negative (about -1%). The median is -36% and 30% of trades won.

### Instrument and expiry
- **No option trades.** Calls, puts, and spreads are all off.
- Do not restart option testing without a new design: a fresh hypothesis, a pre-registered rule, and a fresh bundle. Bundle 6 showed that a single cell can look positive on total and average while failing on median and trimmed average.

### Entry, strike, exit
- **No entry screen is validated.** Across six bundles, no column (call spike, put/call, p/c drop, short/medium/long expiry mix, OTM share, shares, 1-day, 5-day, 20-day, vol20, vs ma20, vs ma50, off-high, RSI, price band) has separated winners from losers in a consistent direction.
- **No strike is a candidate.** 30d +10% OTM is negative on median in bundles 4, 5, and 6. 30d +5% OTM has a 3-trade positive cell in bundle 6 (median +204%) after a -84% average in bundle 5. Pooled across bundles 5 and 6 (7 trades), the average is about +20%, with no reliable median. One-bundle samples this small cannot be acted on.
- **Exit:** hold-10 is the only exit reported in bundle 6. double_or_10 and split exits were not logged, so the matched exit test is still not done. Do not compare exits.

### Sizing (applies to any future test)
- Premium at risk: no more than 1% of the book per trade, never more than 2%.
- Total open option premium: no more than about 10% of the book.
- Longest losing streak: report every bundle.
- **Bundle 6 did not report premium at risk, total open premium, or longest losing streak.** Sizing compliance cannot be judged for bundle 6. The bundle is counted as incomplete for sizing.

### Stock ratings
- **Not a filter. Do not trade on ratings or their inverse.**
- **+1:** Below baseline in bundles 4 and 5, above baseline in bundle 6 (+5.1% average, +1.2% median, vs +0.3% and -0.8% baseline). Sign has flipped across bundles. The negative-expectancy label I planned does not hold. Remove the label.
- **+0:** Near baseline in bundle 6 (+0.1% average, -0.2% median). Not informative.
- **-1:** Below baseline in bundle 6 (-0.9% average, -2.6% median). Above baseline in bundle 5. Unstable.
- **-2:** Two stocks in bundle 6, average -4.2%. About 16 stocks pooled. Still too few to read.

### Confidence summary
- Option median negative in every bundle (six of six): **high.**
- Positive option totals come from a few trades above +100%: **high.**
- Any strike, expiry, or exit as a candidate: **none.**
- Any entry column as a filter: **none.**
- Ratings as a filter: **none.** The +1 pattern reversed in bundle 6.
- 30d +5% OTM as a revived cell: **very low.** Three trades in one bundle.
- Sizing rule (1% per trade, 10% total open): **high** as a risk rule, whether or not options are traded.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### Option trades (44 trades, hold-10 only)
| Cell | Trades | Average | Median |
|---|---|---|---|
| 30d +10% OTM | 19 | +49.5% | -33.6% |
| 30d 0% OTM | 13 | +17.6% | -36.7% |
| 30d +5% OTM | 3 | +157.6% | +203.8% |
| 90d 0% | 3 | -34.4% | -50.3% |
| 14d 0% | 2 | -92.7% | -92.7% |
| 90d +5% | 1 | +26.7% | +26.7% |
| 90d +10% | 1 | -33.8% | -33.8% |
| 14d +5% | 1 | -100.0% | -100.0% |
| 30d +15% | 1 | -59.6% | -59.6% |

- **Total profit:** +11,869. Average +27.0%, median -36%, 30% winners.
- **Key trade:** the 30d +10% winner at +1,235.5% (price over $50, RSI 46, 20-day +23%, 37% above its 50-day average). Removing it turns the 30d +10% cell's average negative.
- **Winners did not separate on any column.** The +266.9% winner (price $10 to $50, RSI 63, off-high -3%) and the +180% winner (RSI 73, off-high -12%) look nothing like each other, and the losers span the same ranges.
- **Losers included** cases with low RSI (14 to 31), high RSI (81), near-high and deep-off-high names, and all three price bands.

### Stock ratings (all candidates, 10 sessions)
Baseline: average +0.3%, median -0.8%.

| Rating | Count | Average | Median |
|---|---|---|---|
| +1 | 25 | +5.1% | +1.2% |
| +0 | 93 | +0.1% | -0.2% |
| -1 | 80 | -0.9% | -2.6% |
| -2 | 2 | -4.2% | -4.2% |

Read: the +1 group led in bundle 6 and trailed in bundles 4 and 5. The -1 group trailed in bundle 6 and led in bundle 5. Ratings do not predict stock returns in a stable direction. The +1 group's bundle 6 result rests on 25 stocks and is not enough to act on.

### New idea tried: direction versus premium decay
Not completed. The stock's 10-session return was not logged alongside each option return for all 44 trades. The option program is now closed, so this test is not needed for trading. It remains useful for research.

### Process gaps (not completed in bundle 6)
- Premium at risk, total open premium, longest losing streak: **not reported.**
- Matched exit test (hold-10, double_or_10, split): **not logged.** Only hold-10 appears.
- 10-session base rate of +10% and +20% moves across all 200 candidates: **not reported.** This is the number needed to judge whether any option structure can break even.
- Under-$10 base rate across all candidates: **not reported.**
- Call-spike split (2x to 4x vs above 5x): **not completed.**
- Deep-below-high split (-20% off the 60-day high): **not completed.**

---

## 3. WHAT I WILL TRY NEXT

The option program is closed. Any further work is research on stock behavior. It is not a trading plan and it does not reopen options.

1. **10-session base rate.** For every candidate in bundles 4 to 6, record the share with a 10-session move of +10% or more, and of +20% or more, and the share that fell 10% or more. Without this, no option result can be judged against break-even.
2. **Under-$10 base rate.** Count the share of candidates under $10 across all bundles. Compare with the tail split (pooled 9 of 24 tail losers and 11 of 24 tail winners under $10 in bundles 4 and 5). Act only if the excess is clear.
3. **Deep-below-high test.** Split all candidates at -20% off the 60-day high. Compare average and median 10-session return with baseline. Drop if it does not beat baseline on both.
4. **Call-spike split.** Split candidates at 2x to 4x vs above 5x call volume. Record counts and median 10-session return in each bucket. This is research only. It does not restart option trading.
5. **Ratings.** Keep logging all ratings. Pool bundles 4 to 6 for +1 and -1. Do not trade them. Do not label +1 as negative. Keep logging -2 until there are about 20 stocks.
6. **Reporting.** Any future bundle must report premium at risk, total open premium, and the longest losing streak, or it is counted as incomplete.

If any option work restarts in future, it needs a fresh bundle with a pre-written rule, a logged matched exit test, a base rate for the same window, and the sizing fields reported. Judge it on median and trimmed average, not total P&L.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### Evidence that held up
- **Negative option median in all six bundles** (-53%, -22%, -52%, -51%, -52%, and negative in bundle 6). Confidence: high.
- **Positive totals rest on a small number of trades above +100%.** Bundle 6's +11,869 comes mostly from one trade at +1,235.5%. Confidence: high.
- **Sizing rule.** Most option trades lose most of their premium. Confidence: high.
- **Far-OTM short-dated calls lose** (15% and 20% OTM at 14 or 90 days; 14-day 5% OTM). Bundle 6 added 14-day 0% (-93%), 14-day 5% (-100%), and 90-day 0% (average -34%). Confidence: moderate, thin samples.

### Mixed or failed
- **30d +10% OTM as candidate.** Positive in bundles 2 and 3, negative median in bundles 4, 5, and 6. Trimmed average negative in bundle 6. Dropped.
- **30d +5% OTM.** Dropped after bundle 3. Bundle 5: 4 trades, average -84%. Bundle 6: 3 trades, average +158%, median +204%. Pooled about +20% over 7 trades, median unreliable. Not revived. Would need a fresh test.
- **30d 0% OTM.** Poor in bundle 4, mixed in bundle 5, negative median in bundle 6 (13 trades, median -37%). Dropped.
- **Hold-10 over double_or_10.** Favored in bundles 4 and 5. Bundle 6 did not log double_or_10 or split, so no comparison is possible. The exit definition is still unverified. Not used.
- **Oversold RSI as a winner signal.** Winners at low RSI in bundles 1 and 5, losers too. Bundle 6 winners at RSI 46 to 73. Dropped.
- **Under-$10 names as a tail predictor.** Balanced on both sides. Dropped until the base rate is measured.
- **Momentum as a tail predictor.** Tail winners and losers both had strong recent gains in bundle 5. Bundle 6's largest winner had 20-day +23%, and its losers included strong and weak momentum. Dropped.
- **Stock ratings as a filter.** The +1 group's sign flipped between bundles. Dropped.

### Dropped
- Trading on stock ratings, or the inverse of any rating.
- Following the largest stock movers as a signal.
- Reading total P&L as edge.
- Any single trade-level column as an entry filter.
- All strike and expiry cells as candidates.
- The +1 negative-expectancy label.
- Option trading, pending a new design and a fresh bundle.

### Agent 3's final notes (not passed on)

# Trading Playbook: Final Notes (rev. 7, after all six bundles)

## 1. CURRENT STRATEGY AND RULES

### 1.1 Status

- **Long-call program: closed to new orders.** No option orders are placed. Option ideas are logged on paper only.
- **Reason:** Six bundles and about 250 option trades. The median option trade lost money in every bundle (bundle 2 −12.1%, bundle 3 −31.1%, bundle 4 −54.8%, bundle 5 −61.3%, bundle 6 −40.8%). The average is near zero or positive only when a few trades return several hundred percent. Bundle 6 ended at −$37, almost flat, but its average of −0.2% came from six winners out of 20, and five of those six winners were 90-day or 30-day trades with large moves.
- **Reopening condition:** Section 1.3. The gate has not been met.
- **Confidence the program should stay closed:** High. Every bundle's median is negative, and the option edge has never been reproduced in a second bundle.

### 1.2 Structure (for reference only; not trading)

Recorded so a future test can compare like with like. None of this is an active rule.

- **Instrument:** long calls.
- **Expiry:** 30-day and 90-day. The 14-day expiry is out (worst bucket in bundles 1 and 5, and in bundle 6 the 14-day +5% trade lost 35%).
- **Strike:** no preferred strike. The 20% OTM arm was the least bad through bundle 5. In bundle 6 it was poor (30-day +20% median −70.6%, n=2). The 30-day +5% arm had the only strongly positive bundle-6 median (+203.8%, n=5), but its bundle-5 median was −44.8% (n=5). One bundle does not decide between arms.
- **Exit:** hold 10 sessions. `double_or_10` is out (bundle 5 median −100%, n=4; 12 trades total with no support).
- **Price band:** no separation. Both winners and losers appear in every band. Log only.
- **Over $50:** provisional exclusion from bundles 2–3 evidence. Bundle 6 had one +252.7% winner in this band, so the exclusion is weakened. Keep it provisional.

### 1.3 Gate to reopen options (unchanged)

All four must hold on a fixed, pre-registered stock-level test set:

1. A feature group has a 10-session tail rate (above +20%) at least 1.5 times the all-candidate rate, with at least 15 candidates in the group.
2. The group's median 10-session stock return is positive.
3. A shares test on the same stocks has a positive median.
4. Only then, an option structure test with a pre-registered median threshold.

**Status: not met.** Criterion 1 could not be assessed (see Section 2.4).

### 1.4 Mechanism (structural, medium-high confidence)

- **The typical candidate does not rally.** Median 10-session stock return: bundle 4 −3.4%, bundle 5 −2.2%, bundle 6 −0.8%. Means were −0.8% (bundle 5) and +0.3% (bundle 6). A 20% OTM strike is almost never reached by the typical stock.
- **Upside tail is real but small.** Bundle 6: at least 10 of 200 (5%) rose more than +20%; at least 2 (1%) rose more than +50%; none in the listed extremes rose more than +100%. Bundle 5: at least 9 of 200 above +20%. Bundle 4: at least 6 of 200. These are floors from extreme-move lists, not full counts.
- **Downside tail is as large.** Bundle 6: at least 10 of 200 fell more than 20%, worst −36.8%. Bundle 5: at least 12. Long-share tests must report both tails.
- **Premium decay compounds the problem.** The option median is far worse than the stock median, consistent with a thin upside tail plus decay.

### 1.5 Rating (directional rating from prior bundles)

- **Rating is not a selector, gate, or filter.** Keep logging it.
- **The "+1 underperforms" finding did not replicate.** Median 10-session return for rating +1: bundle 4 −4.7%, bundle 5 −3.6%, bundle 6 +0.3%. Bundle 6 is the only bundle where +1 led. Average for +1 in bundle 6 was +1.5% (n=40), against +0.4% for 0 and −0.4% for −1.
- **Short-side "+1 short" hypothesis: dropped.** It would have lost money in bundle 6 (median stock +0.3%, mean +1.5%).
- **Confidence:** Low in any direction for the rating.

---

## 2. WHAT I TESTED IN BUNDLE 6 AND HOW IT WENT

### 2.1 Options (paper-logged under the suspension; no new orders were supposed to be placed)

**Result: −$37 on 20 trades. Average −0.2%, median −40.8%, 6 of 20 winners (30%).**

| Bucket | Trades | Average | Median | Read |
|---|---|---|---|---|
| 30d +5%, hold10 | 5 | +100.0% | +203.8% | Three large winners (+203.8%, +210.9%, +252.7%), one at −100%, one at −67%. Only bucket with a large positive median this bundle. |
| 30d +15%, hold10 | 3 | −51.8% | −52.1% | Negative. |
| 90d +20%, hold10 | 2 | +21.8% | +21.8% | +80.0% and −36.4%. n=2. |
| 30d +10%, hold10 | 2 | −47.0% | −47.0% | Negative. |
| 30d 0%, hold10 | 2 | +6.9% | +6.9% | Mixed (+31.5%, −17.7%). |
| 30d +20%, hold10 | 2 | −70.6% | −70.6% | Negative. |
| Singles (90d +10%, 14d +5%, 90d 0%, 90d +5%) | 4 | −86% to +2% | | Too small to read. |

**What this tells me:**

- The bundle-6 result is the same pattern as bundles 2–5: the median is negative, and the average is carried by a few trades.
- The 30-day +5% winners share some features with the stock-level winners: above MA20 (+6.5% to +15.5%), positive 1-day move, RSI 63–81. But the bundle's 30-day +5% losers (−100%, −67%) also showed above-MA20 and positive 1-day readings, so the profile does not separate winners from losers. Five trades cannot support a rule.
- Several winners had elevated `short` (35.2, 88.3, 8.2) and `calls` (5.8–7.8). The bundle's losers also included high `short` and `calls` values, so there is no separation.

### 2.2 Stock-level ratings (all 200 candidates, 10-session returns)

| Rating | Stocks | Average | Median |
|---|---|---|---|
| +1 | 40 | +1.5% | +0.3% |
| 0 | 83 | +0.4% | −1.8% |
| −1 | 77 | −0.4% | −0.6% |

- **All candidates:** average +0.3%, median −0.8%.
- The rating ordering reversed relative to bundles 4 and 5. Treat the rating as noise.

### 2.3 Extreme movers (what was visible; the lists are biased to extremes)

- **Top winners (+20% or more):** 10 stocks. Most had positive 20-day moves (+1% to +33%) and positive `vs ma20 %`. Four of the top 12 winners were rated −1, which is close to the −1 share of the sample (38%), so there is no enrichment.
- **Top losers (−20% or worse):** 10 stocks. Several also had positive 20-day moves and positive `vs ma20 %`. One had a 20-day move of +337.5% and `vs ma20 %` of +33.2%, and it fell 23%.
- **Conclusion:** the visible columns do not separate the stocks that rose from the stocks that fell. Features such as above-MA20, positive 20-day, and high `short`/`calls` appear among both winners and losers.

### 2.4 Tail measurement (Section 3.2 of rev. 6): not completed

- **The pre-registered tail-by-feature test was not possible.** I received extreme lists and summary statistics, not the full 200-row table. I cannot compute tail rates by `vol20 %`, `5d %`, `vs ma20 %`, `20d %`, `rsi`, `1d %`, or `price` band.
- **The shares test (Section 3.3) was not run as a separate test.** The rating-group returns above are a proxy for long-only shares, but they are not the pre-registered feature-group test.
- **Consequence:** the directional-tail search is **inconclusive, not failed.** Decision rule 3.5 cannot be applied. I cannot say that no feature enriches the tail, only that I have not measured it.
- **Confidence in this conclusion:** High (the data were not provided).

### 2.5 New idea tried in bundle 6

- **Pre-registered tail bands and stock-level tail measurement** (Section 3.1–3.2). Not completed for the reason above.
- **Rating +1 short hypothesis** (Section 3.3). Tested via the rating-group returns. Failed: median +0.3% for +1 stocks, so a short would have lost on the median. Dropped.

---

## 3. WHAT I WILL TRY NEXT

Bundle 6 was the last bundle in this series. The option program stays closed. The following are the only planned steps, and each is conditional.

### 3.1 If any further measurement is commissioned

1. **Obtain the full candidate table (all rows and all columns), not extreme lists.** This is the precondition for every test below.
2. **Run the pre-registered tail measurement** with the cut-offs fixed in rev. 6, Section 3.1:
   - `vol20 %`: below 4%, 4–6%, above 6%.
   - `5d %`: below 0, 0–10, above 10.
   - `vs ma20 %`: above or below 0.
   - `20d %`: below −15%, −15% to +15%, above +15%.
   - `rsi`: below 30, 30–70, above 70.
   - `1d %` (absolute): below 5%, 5–15%, above 15%.
   - `price`: under $10, $10–50, over $50.
3. **Report both tails** (above +20%, +50%, +100%, and below −20%) for every group, against the all-candidate rate (about 5% above +20%, about 5% below −20%, about 1% above +50%, based on bundle 6 floors).
4. **Apply gate criterion 1.** A group needs at least 1.5 times the all-candidate tail rate with at least 15 candidates. Given the base rate, that is roughly 7.5% above +20%.
5. **Run a shares test on the same stocks.** Equal-dollar long positions, held 10 sessions, with median, mean, and both tails.

### 3.2 Decision rules

- **If no group reaches 1.5 times the base tail rate with at least 15 candidates,** the directional-tail search ends. Option trading stays closed.
- **If one group reaches it and its shares median is positive,** run a new, pre-registered test on fresh stocks. No option trading until that test passes all four gate criteria.
- **If one group reaches it but its shares median is negative,** drop the group. A tail rate alone is not enough, because the downside tail is equally large.
- **Regardless of result:** the stock upside tail (about 5% above +20%, about 1% above +50%) is far below what a 20% OTM call needs to pay after premium decay. Options do not become viable unless the tail is several times the base rate.

### 3.3 Logging rules

- Every candidate counts, whether or not it meets a feature condition. Compare each group to the all-candidate median and tail rate.
- Log but do not filter on: `rating`, `calls`, `puts`, `p/c`, `p/c drop`, `short`, `medium`, `long`, `otm`, `shares`, `20d %`, `vs ma50 %`, `off high %`, `rsi`, `price`.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### 4.1 Evidence summary

| Idea | Evidence | Confidence |
|---|---|---|
| Long calls have a positive median | Median negative in all five option bundles (−12.1%, −31.1%, −54.8%, −61.3%, −40.8%). Average positive only through a few large winners. | High that the program is not profitable as run. Program closed. |
| Median stock move is too small for an OTM call | Medians −3.4% (bundle 4), −2.2% (bundle 5), −0.8% (bundle 6). | Medium-high (structural). |
| Stock upside tail about 5% above +20% | Floors: 6/200 (bundle 4), 9/200 (bundle 5), 10/200 (bundle 6). About 1% above +50% in bundle 6. | Medium. Floors only. Full measurement not done. |
| Stock downside tail at least 5% below −20% | At least 12/200 (bundle 5), at least 10/200 (bundle 6). | Medium. Matters for any shares test. |
| Rating +1 underperforms | Bundles 4 and 5 yes. Bundle 6 reversed (+0.3% median, best group). | Dropped. |
| Rating +1 short | Bundle 6 median +0.3%, so a short would have lost. | Dropped. |
| 30-day +5% arm is best | Bundle 6 median +203.8% (n=5). Bundle 5 median −44.8% (n=5). | Very low. Opposing bundles. Not evidence. |
| 30-day +15% is less bad | Bundle 5 median −22.4% (n=4). Bundle 6 median −52.1% (n=3). | Dropped. |
| 20% OTM is the least-bad strike | Bundle 6 20% median −70.6% (n=2). Bundle 5 no advantage over 5% or 15%. | Dropped. |
| 90-day beats 30-day | Bundle 2 yes, bundle 3 no, bundle 4 yes (n=4), bundle 6 one pair (+21.8% median, n=2). | Very low. Not tested further. |
| 14-day expiry is worst | Worst bucket in bundles 1 and 5. Bundle 6 14-day +5% −35.4%. | Medium-low. Out. |
| double_or_10 exit | 12 trades; bundle 5 median −100%. | Out. Hold10 stays. |
| Pullback tilt (below MA20, low RSI) | Failed in bundles 4, 5. | Dropped. |
| 5-day momentum enriches winners | Bundle 4 yes. Bundles 5 and 6 no clear separation. | Dropped as option filter. Retest only via full-table tail test. |
| Volatility (`vol20 %`) enriches winners | Bundle 4 no. Bundle 5 extreme winners 2.8% to 19.3%. | Not supported. Retest via bands in 3.1. |
| Above MA20 and positive 20-day enriches winners | Bundle 6: five of six option winners above MA20; but losers showed the same features. | Not supported. Extreme-list bias. |
| Large call or short volume enriches winners | Bundle 5 some winners; bundle 6 winners and losers both high. | Unconfirmed. Log only. |
| Price band separates winners | Winners in every band across bundles. | No separation. Log only. |
| Over $50 contracts are weak | Bundles 2–3 negative. Bundle 6 one +252.7% winner. | Low. Provisional exclusion, weakened. |
| Event-driven tails (large 1-day moves) | Top stock winners in bundles 4–6 had large 1-day moves, but many losers did too. | Hypothesis. Test via `1d %` bands. |
| Option trading during measurement bundles | Bundle 5 broke the rule. | Out. Rule enforced. |

### 4.2 Ideas dropped

- **14-day calls.** Out.
- **10% and 15% OTM arms.** Mostly negative medians. Out.
- **ATM and 0% strikes.** Weak in bundles 2, 3, 5, and 6 (bundle 6 0% median +6.9%, n=2, is not enough to revive them). Out.
- **Pullback tilt as a filter.** Out.
- **Rating as a selector or gate.** Out.
- **Rating +1 as a short signal.** Out.
- **`5d %` momentum as an option filter.** Out.
- **Option trading during measurement bundles.** Out.

### 4.3 Caution

- Six bundles, about 250 option trades, and the median option trade has lost in every bundle.
- The bundle 6 dollar result (−$37) is near zero, but that hides a −40.8% median. The average is driven by a few large winners.
- Bundle-to-bundle swings in small buckets (30-day +5%, 90-day +20%, rating +1) are sampling noise until replicated.
- **The consistent findings:** (1) the typical candidate stock is flat to down over 10 sessions; (2) option averages depend on a few large winners; (3) no visible feature has been shown to predict those winners on the full sample; (4) the directional-tail search was never fully measured.

### Agent 4's final notes (not passed on)

# TRADING NOTES (final, after bundle 6 of 6)

## 1. MY CURRENT STRATEGY

**Status: real-money option trading is off. Paper only.** No stock filter has passed on full candidate data. The stock baseline has been negative on the median in five of six bundles.

### 1.1 Paper benchmark arm (the only option configuration still running)

- **Instrument:** calls expiring about 90 days out (15–60 days only if 90-day contracts are unavailable, logged separately).
- **Strike:** 10% above the current price only. The 0% and 5% bands are dropped (see 1.2).
- **Exit:** sell after 10 sessions. No double-or-10 exit, no early exit on a move.
- **Size:** 1% of notional, one open position at a time.
- **Why the 10% band:** it is the only strike band with a positive median in the latest bundle (bundle 6: 13 trades, median +23.2%, mean +32.4%). In bundle 5 the same band had a median of −35.6% (10 trades). The sign has flipped between bundles, so this is a lead, not a validated setup.

### 1.2 Banned or retired

- **Calls expiring within 30 days, any strike:** retired. Negative medians in bundles 3–6. The one bundle-6 30-day trade at +20% strike lost 97.9%.
- **Calls expiring within 14 days, any strike:** banned. Near-total losses in every bundle tested.
- **Strikes above 10%:** not traded.
- **0% and 5% strike bands (90-day):** dropped from the paper arm. Pooled over two bundles, the 0% band's median was −36.5% (bundle 5, 7 trades) and −44.6% (bundle 6, 7 trades). The 5% band's median was −68.9% (bundle 5, 4 trades) and −37.6% (bundle 6, 6 trades). Both are negative in both bundles.
- **Blind call buying with no stock-level filter:** not used.

### 1.3 Stock-level selection: no buy rule

- No candidate filter has been measured on full candidate data. Every filter is a hypothesis.
- **Baseline 10-session median by bundle:** bundle 1 −0.2%, bundle 2 +0.2%, bundle 3 −1.6%, bundle 4 −3.4%, bundle 5 −2.2%, bundle 6 −0.8%. The median is negative in five of six bundles. The average can be positive (bundle 6: +0.3%) because a few large winners lift it.
- **Any filter must beat the same bundle's baseline median by a clear margin.** A filter that only works in one bundle is a lead.

### 1.4 Rating: logged, not used as an input

- **Bundle 6 medians:** +1 +0.5% (15 stocks), +0 −0.2% (92), −1 −2.0% (77), −2 −4.2% (16). This is the first bundle where the medians fall in rating order.
- **Across bundles, the order is not stable.** In bundle 5 the order was +1, −1, −2, +0 with +0 lowest.
- **Do not buy or avoid a stock because of its rating.** The rating is logged so the pattern can be checked when full data arrives.

### 1.5 Judging any configuration

A configuration counts only if all three hold:
1. Positive median, net of costs (about 5% each way plus decay).
2. Positive mean with the single largest trade removed.
3. The largest trade is no more than one third of the configuration's total profit (meaningful only when total profit is positive).

Also report: trade count, median, trimmed mean, largest-trade share, winner count, and the decomposition gap (see 3.2). Never headline the raw mean.

### 1.6 Reasoning

- **Option losses are far larger than stock losses would explain.** In bundle 6 the option median was −27.3% and the candidate stock median was −0.8%. Even with leverage, a small stock move should cost a much smaller share of premium. Something other than direction is consuming the premium.
- **Working hypotheses (not findings):**
  - *Implied-volatility reversion:* scanner triggers (heavy call volume, big moves) often coincide with an implied-volatility spike that later fades, shrinking premium even when the stock is flat.
  - *Time decay and spreads:* 10-session decay plus bid/ask cost on entry and exit is largest in cheap, thinly traded contracts.
  - *Strike needs a move:* a 10% OTM call only pays if the stock rises enough to cover premium.
- **Option results are not a leveraged version of stock results** until the decomposition is done.
- **Medians and trimmed means only.** Single trades swing the averages: bundle 6 had several trades above +100% and two below −95%.
- **Stopping real-money trading costs little.** Bundle 6 lost $2,032 on 31 trades. Bundle 5 lost $6,913 on 25.

---

## 2. WHAT I TESTED IN BUNDLE 6

**200 candidates, 31 option trades, profit −$2,032. Average −6.6%, median −27.3%, 32% winners.**

### 2.1 Option results by configuration

| Configuration | Trades | Median | Mean | Read |
|---|---|---|---|---|
| 90d, 0% strike, hold10 | 7 | −44.6% | −50.3% | Negative median; dropped |
| 90d, 5% strike, hold10 | 6 | −37.6% | −27.9% | Negative median; dropped |
| 90d, 10% strike, hold10 | 13 | +23.2% | +32.4% | Positive median; lead, not validated |
| 30d, +0% strike, hold10 | 1 | −20.3% | −20.3% | Retired family; one trade |
| 30d, +10% strike, hold10 | 1 | −6.2% | −6.2% | Retired family; one trade |
| 30d, +15% strike, hold10 | 1 | −72.9% | −72.9% | Retired family; one trade |
| 30d, +20% strike, hold10 | 1 | −97.9% | −97.9% | Retired family; one trade |
| 30d, +20% strike, double-or-10 | 1 | +93.0% | +93.0% | Retired family; one trade, not a rule |

**Points to carry forward:**

- **Strike ordering appeared in this bundle.** Median rose with strike distance: 0% −44.6%, 5% −37.6%, 10% +23.2%. Bundle 5 showed no such ordering (10% median −35.6%, worse than the 0% band's −36.5% only by a little). Two bundles is not enough to call a pattern. It also may reflect which names happened to draw 10% strikes.
- **The 10% band's positive result is not a clean pass.** Pooling bundles 5 and 6 gives 23 trades with a median sign that depends on which bundle is included. It fails the pass criteria in 1.5 and 3.4.
- **Visible 10% trades:** the bundle reported only some of the 13 trades' details. Of the 10 visible, 8 were positive and the two largest losses were −65.1% and −54.8%. Both losers had a negative 5-day move. Several winners had 5-day gains of 5% or more, but the sample is too small to use that as a rule.
- **Price band:** the 90-day 10% trades were spread across $10–50, over $50 and under $10. The price band does not yet separate winners from losers in the option arm.
- **Option losses far exceeded stock losses in the same bundle.** The worst option trades (−97.9%, −78.9%, −72.9%) came from names whose candidate-level 10-session returns were not supplied, so the decomposition could not be run.

### 2.2 Stock-level results (all 200 candidates)

- **Baseline:** +0.3% average, −0.8% median over 10 sessions.
- **Rating buckets (10-session stock return, average / median):**
  - **+1 (15 stocks):** −3.7% / +0.5%. Above baseline on median.
  - **+0 (92 stocks):** +2.1% / −0.2%. Slightly above baseline on median; the average is lifted by large winners.
  - **−1 (77 stocks):** −0.4% / −2.0%. Below baseline on median.
  - **−2 (16 stocks):** −2.6% / −4.2%. Below baseline on median.
- **+1 has now been above baseline on median in bundles 4, 5 and 6** (missed in bundle 3). It is a watch item, not a buy rule.
- **−2 has been below baseline on median in bundles 3, 4 and 6, and at baseline in bundle 5.** It is the strongest exclusion candidate so far, but it is still low-confidence and untested on full data.

### 2.3 Tail patterns (top and bottom ~12 candidate stocks; anecdotal)

**Bottom tail:**
- **Price band:** about 4 under $10, 6 in $10–50, 1 over $50.
- **Prior 20-session move:** about 6 of 11 had a 20-session gain of +7% or more. One name was up 337.5% over 20 sessions and 130% above its 50-session average, and still fell 23%.
- **Sharp 5-day rallies:** about 5 of 11 had 5-day gains of +10% or more. Almost no bottom-tail name had a 5-day decline of −10% or more.
- **RSI:** mixed, from 36 to 73.

**Top tail:**
- **Price band:** about 3 under $10, the rest in $10–50 and over $50.
- **Prior 20-session move:** about 8 of 12 had a 20-session gain of +7% or more. That is higher than the bottom tail, which is the opposite of the extension hypothesis.
- **Several top names were far above their 50-session average** (up to +30%), and one was far below it (−67.6%) with a deep drawdown from its high. Both extremes appear among winners.
- **Calls crowding:** 3 of the top 12 had calls ≥ 5. The bottom tail had 2–3. No separation.

**What the tails say:**
- Extension (20-day and 50-day run-up) does not separate losers from winners in this bundle. It is not supported.
- Sharp 5-day rallies appear in the bottom tail and in the top tail. The 5-day rally exclusion is still unsupported.
- The falling-knife idea (5-day decline ≤ −10%) gets no support as a loser signal here: almost no bottom-tail name had one.
- Under $10 and $10–50 again hold both tails.
- These are 11–12 names per side. They are reasons to test, not results.

### 2.4 New idea attempted: the option-to-stock decomposition

- **Not measured.** The 10-session stock return for each traded name was not supplied, only for the candidate tails. The decomposition needs the traded names' stock returns, which I did not receive. This is the third bundle in which a planned test could not be run.
- **Long-dated paper arm (120–180 days):** not run in bundle 6.
- **Shares control:** not run.

### 2.5 What I did not get

- **The full candidate list with every column and each 10-session return was not supplied.** Only tails and bucket summaries were. This is the fourth bundle in a row (3, 4, 5, 6) without full data.
- **Stock returns for the 31 traded names were not supplied.** This blocks the decomposition.
- Every filter test remains "not measurable" for bundle 6.

---

## 3. WHAT I WILL TRY NEXT

### 3.1 Data requirements (top priority)

- **Every candidate row with all columns and its 10-session return.** Without it, no filter can be compared with the same bundle's median. If it is not supplied, the filter tests are recorded as "not measurable" and no conclusions are drawn from tails.
- **For every option trade, the stock's 10-session return on the same name.** Without it, the decomposition cannot run.

### 3.2 Pre-registered tests for bundle 7 (fixed in advance)

Each test is compared with the same bundle's baseline median.

1. **Option decomposition (highest priority, no new money).** For each paper option trade, record the stock's 10-session return, premium at entry and exit, and the premium return implied by the stock move alone (using entry delta or the closest estimate). The gap is the structural cost (volatility change, decay, spread). If the gap explains most of the loss, the problem is instrument and pricing, not stock selection, and no stock filter can rescue the current instrument.

2. **90-day 10% band, paper, with stock filters logged.** Continue as the lead. Log every trade's stock return and filter pass/fail. Target at least 20 trades across the pooled bundles before any judgment.

3. **Long-dated paper arm (120–180 days, 10% strike band, hold10).** Logged separately. If the 90-day losses are mostly decay, the longer expiry should show a smaller premium loss for the same stock move. This tests the instrument, not a new strategy.

4. **Price-setup filter:** vs ma50 ≤ −10% AND 1d > 0. Compare median and mean with the baseline and with the complement.

5. **Falling-knife filter:** 5d ≤ −10%, split by 1d: a one-day crash (1d ≤ −5%) versus a slow drift (1d between −5% and 0%). Keep them separate.

6. **Extension test (replaces the earlier 5-day rally exclusion):** 20d ≥ +7% AND vs ma50 ≥ +10%. Test whether these names underperform the baseline median on stock returns. Bundle 6's tails did not support it, so the test is a check on the full list.

7. **Under-$10 control:** compare under $10, $10–50 and over $50 on median and interquartile range. Aim: find a band with a stable median before any option trade is placed there.

8. **Crowding and overbought:** calls ≥ 5 AND rsi > 70, measured on stock return. Not supported in the tails across four bundles.

9. **Rating −2 exclusion:** low-confidence candidate. Test on full data. Bundle 6 supports it (median −4.2% vs baseline −0.8%).

10. **Rating +1 watch:** logged, not used as a rule. Above baseline on median in bundles 4–6.

11. **Shares control:** hold filter-passing stocks in shares for 10 sessions. If shares do not beat the baseline median, the option results cannot be explained as leverage on a real stock edge.

### 3.3 Decision rule at the end of bundle 7

- **Option trading (real money):** stays off unless the pass criteria in 3.4 are met.
- **Decomposition result:** if the structural gap explains most of the option loss, the next step is to change the instrument or stop option trading. Do not change the stock filter in response.
- **Stock filter:** a candidate only if, in the bundle alone, it beats the same bundle's baseline median by a clear margin, and it also holds on pooled full-data bundles. A single-bundle pass is a lead.
- **If no filter passes:** option trading stays off. The stock-level baseline (negative median in five of six bundles) is the main lesson.

### 3.4 Pass criteria before any real-money option trade

- At least 20 trades in the configuration, pooled across bundles, from stocks that passed a pre-specified stock-level filter.
- Positive median net of cost, in the pooled data and in at least two separate bundles.
- Positive mean with the single largest trade removed.
- No single trade more than one third of the configuration's total profit.

**Current status:**
- **90-day, 10% strike, hold10:** positive median in bundle 6, negative in bundle 5. No stock filter. **Fails. Paper lead.**
- **90-day, 0% and 5% strikes:** negative medians in bundles 5 and 6. **Dropped from paper arm.**
- **30-day configurations:** negative in bundles 3–6. **Retired.**
- **14-day calls:** **Banned.**
- **Stock-level filters:** not measurable on full data. **Hypotheses only.**
- **Long-dated arm, decomposition, shares control:** not yet run. **Next paper tests.**

### 3.5 Logging

- **For each option trade:** expiry bucket, strike band, price band, exit rule, premium at entry and exit, the stock's 10-session return on the same name, every column value, the 5-day move, each stock filter as pass or fail, and the rating (logged, not used).
- **For each stock candidate:** when full data is supplied, every column and its 10-session return.
- **Reporting:** count, median, trimmed mean, largest-trade share, winner count, and the decomposition gap, for each configuration.

---

## 4. SUPPORTING EVIDENCE AND DROPPED IDEAS

### 4.1 Status of each idea

| Idea | Bundles tested | Result | Status |
|---|---|---|---|
| 90d, 10% OTM, hold10 | 5–6 (23 trades in bundles 5–6) | Median −35.6% in bundle 5, +23.2% in bundle 6 | **Paper lead; not validated** |
| 90d, 0% OTM, hold10 | 5–6 (14 trades) | Negative median in both bundles | **Dropped** |
| 90d, 5% OTM, hold10 | 5–6 (10 trades) | Negative median in both bundles | **Dropped** |
| 30d, any strike, any exit | 3–6 | Negative medians; one +93% trade in bundle 6 not replicable | **Retired** |
| 14-day calls, any strike | 3+ | Consistent losers near −100% | **Banned** |
| Option structural cost (decay, spread, IV change) | Inferred from bundles 4–6 | Option medians far below candidate stock medians; not measured | **Test by decomposition (3.2, item 1)** |
| Longer expiry reduces premium loss | Not yet tested | — | **Paper test (3.2, item 3)** |
| Strike distance improves returns | 5–6 | Bundle 6 showed monotonic median by strike; bundle 5 did not | **Unclear; watch, not a rule** |
| Subjective rating predicts returns | 6 | +1 above baseline in bundles 4–6; −2 below in bundles 3, 4, 6; order not stable | **Logged only; not an input** |
| Avoid +1 names | 6 | Reversed in bundles 4–6 | **Dropped** |
| Avoid −2 names | 4 | Below baseline in bundles 3, 4, 6; at baseline in bundle 5 | **Low-confidence exclusion; test on full data** |
| Price-setup filter (vs ma50 ≤ −10, up on day) | Tails only | Not measurable | **Top stock-level test; awaiting full data** |
| Falling-knife filter (5d ≤ −10) | Tails only | Almost absent from bottom tail in bundle 6 | **Untested; split by 1d %** |
| 5-day rally exclusion (5d ≥ +10) | Tails (bundles 4–6) | Present among both big losers and big winners | **Dropped** |
| Extension filter (20d ≥ +7 AND vs ma50 ≥ +10) | Tails (bundles 5–6) | Bundle 6: top tail had more 20d ≥ +7 names than bottom tail | **Not supported in tails; test on full data** |
| Call crowding and overbought (calls ≥ 5, rsi > 70) | Tails (bundles 2–6) | No separation | **Stock-level test only** |
| Blind call buying | 6 | Median losses in most configurations | **Not used without a filter** |
| "Quiet" call buying as a buy signal | Research team | Consistent with research finding that it is weak | **Not used** |

### 4.2 Lessons from six bundles

- **The stock baseline median is negative in five of six bundles.** The candidate list tends to drift down over 10 sessions. Any filter must be judged against the same bundle's baseline.
- **Option losses are much larger than candidate stock losses.** This is the main correction in these notes. The structure of the option (decay, spread, volatility change) is the first suspect, and it still has not been measured.
- **The 90-day 10% band flipped sign between bundles 5 and 6.** This is the clearest reason to keep it on paper and not on real money.
- **Under $10 and $10–50 hold both tails in most bundles.** Winners and losers both come from there. Control this band before trading options in it.
- **Momentum and crash-rebound winners both appear.** Tails cannot separate them.
- **The data gap has lasted four bundles.** Without full candidate data and traded-name stock returns, no filter has been measured and the decomposition has not run. This is the largest limitation in the record.

### 4.3 Caveats

- Six bundles, about 213 option trades in total. Most configurations have fewer than 25 trades.
- No stock-level filter has been measured on the full candidate list.
- Assumptions to keep checking:
  - "+X%" means strike offset above the price.
  - "hold10" means exit after 10 sessions.
  - The option return is the return on the premium paid, not on the stock.
  - The rating is subjective and may be noise.
  - The decomposition's stock-implied premium uses an estimated delta, so its result will be approximate.

### 4.4 Confidence summary

- **14-day and 30-day calls lose:** high confidence (consistent losses across bundles).
- **Option premium losses exceed what stock moves alone would explain:** moderate confidence, pending the decomposition.
- **90-day, 10% OTM, hold10 has a positive median:** **not supported**. One positive bundle and one negative bundle. Paper lead only.
- **90-day, 0% and 5% strikes have positive medians:** **not supported**. Dropped.
- **The stock baseline median is negative:** moderate confidence (five of six bundles).
- **The subjective rating adds value:** very low confidence. Logged only.
- **Avoid −2 names:** low-to-moderate confidence; supported in three of four bundles where it was measured.
- **Avoid +1 names:** dropped.
- **Price-setup, falling-knife and extension filters help:** unknown; need full data.
- **Under $10 is the most dispersed band:** moderate confidence as a pattern, low as a rule until tested.

