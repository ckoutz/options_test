# Agent notes (2026-10-08 20:52 UTC)

Every lessons document each generation passed on, oldest first, then what the agents wrote
week by week in their latest runs. Lineages without -v2 are the first test, whose weekly
replies were cut off (no trades) and were not saved.

## blank, generation 1 (anthropic/claude-haiku-5.5, 2026-10-08T18:16:08+00:00)

(empty)

## blank, generation 2 (anthropic/claude-haiku-5.5, 2026-10-08T18:22:57+00:00)

(empty)

## blank, generation 3 (anthropic/claude-haiku-5.5, 2026-10-08T18:29:44+00:00)

# Lessons Document: Generation 1 ## Status This generation made no trades, so it produced no evidence. Nothing below is a validated rule. Treat every item as a hypothesis to test, not a fact. ## What we know - **No trades, no results.** We have no data on which signals, instruments, expiries, strikes, or exits perform well or badly. - **Doing nothing is a valid baseline, not a failure.** Its score is zero. Any strategy you adopt should beat zero after costs, or it is not worth running. ## Starting principles (low confidence, untested) These are general reasoning, not findings. 1. **Start from the columns, not from a story.** Before trading, write down which columns you will use and what threshold or combination would trigger an entry. Decide this in advance, not after seeing outcomes. 2. **Prefer simple rules.** One or two conditions are easier to evaluate than many. Many conditions on a small sample mostly fit noise. 3. **Define the exit before the entry.** Set the exit rule (time-based, target, or stop) at the same time as the entry, so results are measurable. 4. **Pick one instrument and one expiry to begin.** Mixing instruments, expiries, and strikes makes results impossible to attribute. 5. **Strike choice matters, but we have no data on it.** Test at least two levels (for example, at-the-money and one step out-of-the-money) before drawing conclusions. ## How to build real lessons - **Log every decision**, including no-trade decisions and the reason for each. - **Record the columns' values at entry**, the exit reason, and the result after costs. - **Use a holdout.** Form rules on one segment of data and check them on a later segment. A rule that only works in-sample is not a lesson. - **Count trades before believing anything.** Under roughly 30 comparable trades, treat any win rate or average return as indicative only. Under 100, treat conclusions as provisional. - **Compare against doing nothing and against a simple baseline** (for example, always entering the same way with the same exit). - **Watch for overfitting:** if you tried many thresholds and kept the best, the result is likely luck. ## Confidence summary

## blank-v2, generation 1 (anthropic/claude-haiku-5.5, 2026-10-08T18:49:06+00:00)

# Lessons for the Next Trader **Baseline:** Over 136 trades of $1,000 each, the overall result was -4.1% average and -5.5k total, with 45% winners. Trading shares was roughly flat (+0.4% average, -1.1% median, 92 trades). Most option variants lost money. Treat everything below as hypotheses, not established edges. ## Rules, with confidence 1. **Default to shares unless an option setup clearly beats them. Confidence: moderate.** Shares were the only large group near breakeven. Options lost on most variants, and their losses were often total (-100%), so one bad option trade costs far more than one bad share trade. 2. **Avoid 30-day calls struck above the money with a 10-day hold. Confidence: moderate.** The 30d +5%, +10%, and +15% hold10 groups averaged roughly -50% to -65%. Short expiry leaves too little time for the move to arrive. 3. **Avoid the "double_or_10" exit as a default. Confidence: moderate.** It produced the largest single gains and many of the largest losses. Its median outcome was poor, so it behaves like a lottery ticket, not a plan. 4. **Longer expiry (90 days) with a 10-day hold is the least bad option structure. Confidence: low.** The 90d +20% hold10 group averaged +13.6% over 3 trades, and the 90d +0% hold10 group had a positive median (+4.5%) but a negative average. Both samples are too small to trust. 5. **Do not trust the ratio columns (calls, puts, long, short, shares) as predictors. Confidence: moderate that they were not useful here.** Large and small values showed up in both winners and losers. I found no threshold that separated them. 6. **Short-term price moves (1d, 5d) and volatility (vol20) did not separate winners from losers in this data. Confidence: low.** Several large losses followed positive 1d and 5d moves, and some winners had weak early moves. ## What failed - Far-OTM short-dated calls: nearly every variant lost most of its premium. - Averaging across all option types hid the few winners. Medians were often worse than averages, meaning results depended on a handful of outliers. - Sizing every trade at $1,000 regardless of instrument risk. ## Sample caveats - Most groups have 1 to 11 trades. A single trade drives several results (the +258% and +123% gains each come from one or two trades). - Groups were chosen after seeing results, which inflates apparent edges. - Results cover one period. Regime changes may invalidate everything above. ## Next steps - Collect more trades in the 90-day hold10 structures before sizing up. - Test shares against 90-day options at equal dollar risk. - Record whether the exit rule fired and why, to separate strategy from luck.

## Weekly notes: blank-v2, generation 1, train

(weeks the agent passed were not recorded for this run)
- week 1 [stock -13%; call 30d +0% hold10 -100%]: C3 shows bullish call flow with muted puts and a rising trend. C5 has heavy call buying after a selloff, and its options are cheap.
- week 2 [call 30d +15% hold10 -30%; call 90d +0% hold10 +134%; call 30d +10% hold10 -61%]: Broad bullish call flow across tenors with put crowd-out (C4, C9); cheap long-dated OTM call surge (C10). Avoided extreme spikes.
- week 3 [stock +8%; stock +25%]: Heavy call and share surges with momentum, no option premium drag. Other names are chasing spikes or lack a clear signal.
- week 4 [stock +0%; stock -10%; stock -14%]: Stock trades avoid the 5% option cost. C6 and C9 show strong call crowding; C4 has puts collapsing after a 24% drop.
- week 5 [stock +25%; stock -18%; stock -17%]: Stock trades beat calls so far. These show call, share and put surges with strong 1-5 day momentum, so I'm riding it on stock.
- week 6 [stock -9%; call 30d +10% double_or_10 -37%; call 30d +5% hold10 -99%]: Bullish call-volume surges with OTM and medium-dated flow; C1 has cheap OTM calls and calls crowding out puts.
- week 7 [stock -9%; call 90d +10% hold10 +43%; stock -3%]: Bullish call-volume crowding with few puts in C1 and C11; C9 is oversold with heavy long-dated call buying.
- week 8 [stock +6%; stock -3%]: Heavy long-dated call buying with puts fading (C1); strong short-dated call surge with rising shares near highs (C8). Passing the rest.
- week 9 [stock -21%; stock +3%]: Strong volume and momentum in C2; C12 shows heavy two-sided flow with rising shares and price. Other setups look like noise.
- week 10 [stock -3%; stock -19%]: Call-heavy buying with puts falling (p/c drop above 3) and rising price momentum. Passing on the parabolic and mixed-signal names.
- week 11 [stock -11%]: Heavy call buying into a 22% off-high drawdown with RSI near 30; chasing spikes like C6 has lost repeatedly, so I skipped those.
- week 12 [stock +19%; call 90d +0% hold10 +5%]: Call buying surging with puts gone on a pullback (C6); medium-dated call accumulation in C3. Avoided overbought chases.
- week 13 [stock -1%; stock -18%]: Oversold dips with RSI near 20 and heavy call buying may bounce; past chases of spikes reverted, so I avoided those.
- week 14 [stock -1%; stock -16%]: C10 shows heavy long-dated call buying with falling puts; C3 has steady trend and rising shares. Passing on the rest.
- week 15 [call 30d +5% double_or_10 -100%; call 90d +5% hold10 -60%]: Heavy OTM and medium-dated call buying with a sharp up day; I skipped overextended spikes that lost before.
- week 16 [call 90d +10% hold10 +10%]: Heavy call buying across expiries with near-zero put volume and a breakout above the 50-day average; other candidates looked like chasing or thin signals.
- week 18 [stock -0%; call 30d +10% hold10 -66%]: C2 shows momentum with calls rising near highs. C11 has heavy OTM call flow and a cheap 10% strike.
- week 19 [stock +9%; call 90d +10% hold10 -60%]: Heavy call buying, no put flow, and a strong 5-day trend. Passed on overextended names with high RSI.
- week 20 [stock +2%; stock -23%]: Heavy call and share volume with strong momentum in C6; C12 shows a short-dated call surge on a pullback. Options costs have been hard to overcome, so I stayed with stock.
- week 21 [stock +5%]: Put volume is very low, long-dated call buying is heavy, and price is rising. Passing on the rest, which look like overbought chases or bearish flow.
- week 22 [stock +0%; stock -19%]: Strong call-led momentum with rising shares volume and price above both averages. Passing on the rest; the option track record has been poor.
- week 23 [call 30d +0% hold10 -100%; stock -2%]: Strong call buying with almost no put flow; both are cheap, bullish-skewed setups after recent pullbacks.
- week 24 [stock +1%]: Call volume surge with shares at 2.8x after a 30% drop; calls crowding out puts. Single small stock bet, since short-dated calls have lost heavily.
- week 25 [call 90d +0% hold10 +29%; call 90d +5% hold10 +18%]: Unusual long-dated call buying with cheap 90-day premiums; passing on overextended, put-heavy, and shorter-dated setups.
- week 26 [stock -23%; stock -3%; call 90d +0% hold10 +19%]: Strong call-led bullish flow with long-dated call crowding and falling put/call; momentum names, sized small.
- week 27 [call 90d +0% hold10 +30%]: Heavy long-dated call buying with puts fading and a healthy uptrend; a pullback entry. Other setups looked weaker.
- week 28 [call 90d +10% hold10 +59%; call 14d +0% double_or_10 -23%]: C10 has heavy call buying and a dip, with 90-day calls historically best. C1 is a cheap, speculative call-spike bet.
- week 29 [call 90d +10% hold10 -24%; stock +18%]: Cheap 90-day call on a quiet put-heavy-free name; stock on call-volume surge with short-term momentum. Passing the rest.
- week 30 [call 90d +10% hold10 -39%; call 90d +20% hold10 +9%; stock -10%]: 90-day calls have been the only reliably profitable option trade; C7 and C11 show call-led flow with cheap 90-day strikes; C2 shows heavy call volume.
- week 31 [call 90d +20% hold10 +69%; call 90d +0% hold10 +8%]: Heavy long-dated call flow in momentum names; 90-day calls have been my best-performing structure.
- week 32 [stock -2%]: Calls crowding out puts with heavy long-dated call interest, mild pullback from high; cheap stock entry. Other setups look like overheated or bearish.
- week 33 [call 90d +0% hold10 -54%; call 90d +0% hold10 -23%]: 90-day calls have been the only reliably profitable structure; these show heavy call-side unusual flow.
- week 34 [call 90d +15% hold10 +33%; call 90d +5% hold10 -68%]: Strong call-over-put flow and momentum in C4; C2 shows a 17x long-dated call spike with puts falling.
- week 35 [call 90d +20% hold10 -37%; call 90d +10% hold10 +51%]: Bullish call-skewed flow with very low put/call and surging long-dated calls; 90-day calls have performed best.
- week 36 [call 90d +0% hold10 -90%; stock +1%]: Heavy medium-term call buying with puts absent and no overextension; C12 has the strongest call-flow signal.
- week 37 [call 30d +5% hold10 +2%; call 30d +15% hold10 -71%]: Strong call crowding with puts collapsing (C2 p/c 0.16, C1 p/c drop 2.4); cheap 30-day strikes limit cost.
- week 38 [call 90d +0% hold10 -8%]: Down 14% from its high with RSI 37 and medium-dated call buying, a rebound setup. Low conviction, so one trade only.
- week 39 [stock +0%]: Extreme call and share volume with strong momentum; calls have lost heavily, so I take only the stock.
- week 40 [call 90d +5% hold10 +13%]: Heavy call and long-dated call surge with price momentum; most other candidates look overextended or show no unusual activity.
- week 41 [call 30d +5% hold10 -70%; stock +10%]: Strong call flow with puts crowded out and momentum; options are cheap; passing on the rest, which looks like noise.
- week 42 [call 90d +10% hold10 -18%; call 14d +0% double_or_10 +123%]: C1 shows heavy long-dated call buying with puts fading; C3 has huge call flow and cheap at-the-money premium. Others look overextended or put-driven.
- week 43 [stock +3%; stock +18%; stock +4%]: Stock trades have lost least; these have heavy call flow, low put/call, and momentum confirmation.
- week 44 [stock -6%; stock +6%; call 90d +5% hold10 -25%]: Heavy medium- and long-dated call flow with OTM crowding in C4, C7 and C10, while put activity is light. Skipped overheated C1.
- week 45 [stock -3%; stock -13%]: Extreme call-skew with put collapse and a pullback from highs in C1; C12 shows heavy call buying with low put/call. Parabolic movers skipped.
- week 46 [stock -20%; call 90d +0% hold10 -60%]: C5 shows strong call crowding with put collapse and no overbought reading. C9 has heavy long-dated call buying with low put activity.
- week 47 [stock +11%; call 30d +0% double_or_10 +258%]: C1 shows heavy call buying, low put/call and a deep drop, a possible reversal. C9 has cheap options and big out-of-money call interest.
- week 48 [stock +12%; stock +14%]: Strong call-volume surges with low put/call and no extreme overextension versus the 50-day average. Passing on parabolic C9.
- week 49 [stock +34%; call 30d +15% double_or_10 -77%]: Heavy call buying across strikes with share volume surge and fresh breakout; C11 cheap OTM call with medium-dated interest.
- week 50 [stock -10%; stock -21%]: Momentum names with rising short-term volume and calls outpacing puts; passing on the rest given weak track record.
- week 51 [stock -21%; stock -6%; stock +17%]: Strong call-flow surges with put crowd-out and rising prices; stock avoids option decay that hurt past trades.
- week 52 [stock +53%; stock -4%]: Heavy call and share volume with a 5-day rebound in C3 and a 1-day jump in C7. Calls have mostly lost money, so I avoided them.
- week 53 [stock -15%; stock -12%]: C3 shows strong breakout volume near highs; C1 has heavy call buying after a deep selloff, a speculative bounce.
- week 54 [stock -14%; stock -4%; stock -15%]: Bullish flow with low puts and strong call crowding; avoided heavy-put names and expensive short-dated options.
- week 55 [stock -5%; stock +24%]: C3 shows call buying crowding out puts after a 44% drawdown; C2 has heavy call and share volume on a breakout day.
- week 56 [stock +23%]: Calls surging 2.8x while put volume collapses (p/c drop 2.6), stock beaten down 41% off high; the most coherent bullish setup this week.
- week 57 [stock -4%]: Heavy call and OTM call crowding with 2.8x share volume, down 30% from the high. Otherwise nothing clears the bar; stock trades have averaged slightly negative.
- week 58 [stock +18%; stock -1%]: Heavy call and long-dated call surges after sharp selloffs with high share volume, RSI oversold; reversal bet on stock.
- week 59 [stock -26%]: Strong volume-confirmed momentum (calls 14x, shares 4.8x, long calls 20x); stock cost is low, and other setups look like lottery-style losers.
- week 61 [stock +8%; stock +1%]: Call-led surges with put volume falling and long-dated call buying, after pullbacks from recent highs. Other setups looked overextended or cost-inefficient.
- week 62 [stock -12%; stock +16%]: Heavy long-dated and OTM call buying on a pullback (C1), plus broad call demand on a steady rally without extreme overbought readings (C5). Selective, as recent trades mostly lost.
- week 63 [stock +46%; call 14d +5% double_or_10 -100%]: Strong call and share surges with short-dated call crowding; puts are light. Skipped overbought or put-heavy names.
- week 64 [stock +4%]: Strong bullish call flow with puts collapsing, shares up 1.5x, and price not overbought. Option costs have been losing, so I stick to stock.
- week 65 [stock +5%; stock +2%]: Strong call-heavy flow with very low put volume and no overheating. Calls have lost badly, so I stick to stock.
- week 66 [stock +12%]: Heavy call buying (9x calls, 15x far-OTM) with low put activity and a non-overbought RSI of 50. Other setups looked weak or overextended.
- week 67 [stock -11%; stock +27%]: Stock trades have the lowest cost. C9 is at its high with heavy volume; C3 shows strong 20-day momentum with rising shares volume.
- week 68 [stock -12%; stock -4%; stock +1%]: Stock trades have been near breakeven, while options lost heavily. Chose names with strong call crowding over puts.
- week 69 [stock +17%; stock -10%]: Strong uptrends with pullbacks and call crowding; stock trades avoid the heavy option decay that has hurt results.
- week 70 [stock -10%; stock +7%]: Heavy call-dominated flow (p/c near zero), short and long calls surging, and price near highs with positive 5-day momentum. Stock is cheaper to trade than calls here.
- week 71 [stock +33%; stock +9%]: Heavy OTM call buying and volume surges with price up over 5 sessions. C1 looks overextended, so I passed it.

## Weekly notes: blank-v2, generation 1, validation

(weeks the agent passed were not recorded for this run)
- week 1 [stock; call 90d +10% hold10]: C8 has heavy long-dated call buying and the 90d hold10 structure is the least bad so far. C1 has momentum; shares are the default.
- week 3 [stock]: Shares were the only near-breakeven group. C6 is a pullback in an uptrend, with price above its 50-day average, so a modest stock trade fits the lessons. Options lost on most variants.
- week 5 [stock; stock]: Shares are the default. C3 looks oversold with calls crowding out puts; C9 is a dip in a strong uptrend. Options setups here look weak.
- week 6 [stock]: Extreme oversold (RSI 8, 20d -49%) with a fresh bounce. Shares were the only near-breakeven group, so I use shares, not options.
- week 7 [stock; stock]: Shares are the default. C10 and C9 are at 60-day highs with strong 5d gains and heavy call buying, without the extreme overextension of C6 or C8.
- week 8 [stock; stock]: Shares were the only near-breakeven group. Both are strong 20-day momentum names near highs; options at this structure have lost money.
- week 10 [stock; stock]: Default to shares per lessons. C4 and C7 show strong trend with call-heavy flow and low put/call. Options lost on most variants, so I skipped them.
- week 12 [stock; stock]: Shares default per lessons; C4 and C10 show broad call demand with volume and momentum. Options here are short-dated or unavailable at 90d, which lost before.
- week 15 [stock; stock]: Shares were the only near-breakeven group. Both show steady uptrends with normal volume and no extreme call crowding. Options have lost money, so I avoided them.
- week 16 [stock]: Shares are the default per lessons; options lost broadly. C2 is deeply oversold (RSI 22) with a small up day, a weak mean-reversion case.
- week 17 [stock; call 90d +20% hold10]: Shares are the default. C3 tests the 90-day +20% hold10 structure, the least-bad option group in the lessons.
- week 18 [call 90d +20% hold10]: Strong heavy call-buying trend; 90-day hold10 is the least-bad structure per lessons, and it is cheap at 3.6% of price. Low confidence.
- week 19 [stock]: Shares were the only near-breakeven group. C2 is a mild pullback in an uptrend, above its 50-day average, with normal volume. Other setups look like falling knives or spikes.
- week 21 [stock; stock]: Shares are the default per lessons. Both are deeply oversold (RSI 16 and 20) after sharp drops, a possible rebound setup. Low conviction.
- week 23 [stock]: Bullish flow: calls up, puts down, 5-day gain of 13.7%, and a stock-only trade avoids option decay. Low conviction.
- week 26 [stock; stock]: Shares were the only near-breakeven group. Both show strong call-volume surges with positive momentum and no clear option edge, so I take shares only.
- week 27 [stock]: Heavy call-volume surge with a strong 1d move; shares are the lesson-favored low-cost structure. Other candidates lack a clear edge.
- week 28 [stock; stock]: Shares were the only near-breakeven group. Both picks show call-heavy trends above their moving averages, with lower option cost risk.
- week 31 [stock; stock]: Shares were the only near-breakeven group. Both picks are oversold or pulled back in uptrends, a weak but reasonable setup. No option structure looks favored.

