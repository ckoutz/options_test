# Paper traders (2026-10-17 07:50 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 97,269 | -2.73% | -1.91% | 91% | 4 | 5 | 0 | 3 | 0.26 |
| 2 | 98,247 | -1.75% | -1.91% | 86% | 3 | 6 | 1 | 2 | 0.37 |
| 3 | 99,824 | -0.18% | -1.91% | 90% | 2 | 7 | 3 | 2 | 0.38 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-15** (3 steps, 0 order attempts, $0.00): 2026-10-15: No new orders. Held PLTR 210 Nov-13 call (3 contracts, now 10.15 vs 13.60 fill, -25%, option stop at -50%) and the three STMOM share positions: MRNA up about 8%, SHOP -1.3%, ILMN -1.5%, none at the 12% stop or below the 50-day. No earnings conflicts before planned exits (~10-27/10-28). Account about 89% cash. Journal updated with positions, stops, and open experiments. No new setup passed the rules today, and the existing experiments need their full sample before judging.
- **2026-10-16** (3 steps, 0 order attempts, $0.01): Fri 2026-10-16: No new orders. Reviewed the open book: PLTR 210 Nov-13 call (3 contracts, about -27%, option stop at -50%, planned exit about 10-28), and STMOM share positions MRNA (+13%), SHOP (+1.6%), ILMN (-2.1%). None is at the 12% stop or below its 50-day. Earnings calendar checked: no held name reports before its planned exit. No new setup passed the S1 or STMOM gates, so I stay about 89% cash. Journal updated with the cash rationale and re-entry conditions.
- **2026-10-17** (4 steps, 1 order attempts, $0.01): Sat 2026-10-17: PLTR 210 Nov-13 call was at 4.80 vs 13.60 fill (-65%), past my -50% option stop. Placed a sell limit at 4.60 for all 3 contracts to exit on the next session. The stop was missed because PLTR gapped down on 10-16 and I had no resting stop order. Held the STMOM share positions (MRNA +4%, SHOP -3%, ILMN -5%); none is at its 12% stop, and none reports earnings before the ~10-27 planned exit. No new trades: the market 20-day return is near zero and no stock passed the momentum gate. About 91% cash. Journal updated: S1 paused pending review, and a rule added to place GTC stops at option entry.

### Agent 2

- **2026-10-15** (5 steps, 1 order attempts, $0.01): 2026-10-15: DELL closed at the -10% stop: market sell of 8 sh submitted for the next open (entry 553.95, now 489, -11.7%). DDOG (-7.5%) and TEAM (-2.6%) kept under their -10% stops and earnings-window rules. C-stock gate open but the exact screen is not yet written, so no C-stock trades. No options. Journal updated with the stop record and an action item to write the C-stock screen.
- **2026-10-16** (5 steps, 1 order attempts, $0.01): 2026-10-16: Placed one H52-stock limit buy for GTLB (86 sh, limit 57, ~5% of account), the third slot in the max-3 H52 book. GTLB is 0.1% off its 52-week high, 19% above its 50-day average, with no earnings in the 20-session window. Kept DDOG (-6.9%, stop 257.36) and TEAM (+3.4%, stop 188.96 or close below ma50). Did not trade C-stock: the screen still needs to be written down and confirmed before any entry. Journal updated with the GTLB exit plan and a draft C-stock screen for review.
- **2026-10-17** (3 steps, 1 order attempts, $0.00): 2026-10-17: DDOG closed 247.11 on 10/16, below my written 257.36 close-based stop, so I submitted a market sell of 17 sh for the next open (entry 285.95, about -14%). TEAM (-1.0%, stop close below 188.96 or ma50) and GTLB (-7.3%, exit at close below 50d MA or about -10% from 56.92 entry, around 51.2) remain open and above their stops. No new entries: SPY 5d -2.0% opens the C-stock gate but the screen is not finalized, and H52 slots are not filled because breadth is narrow (31%). Journal updated with the DDOG stop record and a lesson to check stops against the newest close first. Cash about 86%.

### Agent 3

- **2026-10-15** (4 steps, 3 order attempts, $0.03): Oct 15: No new entries. Verified the Sept CPI print (core +0.3% m/m, headline +0.6%, hotter than expected, so the EXP1 size-cut rule does not trigger). Placed GTC protective stop-sells at about -8% on the three EXP1 positions (PLTR 191.60, MRNA 191.10, TEAM 192.20). Cash stays about 86%. The EXP1 exit is about Oct 27 or the stop. OKTA still passes the screen but the 3-name cap is full. Journal updated.
- **2026-10-16** (3 steps, 0 order attempts, $0.00): Oct 16: No new orders. EXP1 positions (MRNA 236.5, PLTR 200.5, TEAM 217.12) remain well above their GTC stops (191.10, 191.60, 192.20). The 3-name cap is full, so OKTA passes the screen but is not bought. Equity 100,709, about 85% cash. Plan: hold to about Oct 27 exit or stop, whichever comes first. Journal updated.
- **2026-10-17** (6 steps, 3 order attempts, $0.02): Oct 17: PLTR was stopped out Oct 15, which freed one EXP1 slot. IOVA passes the EXP1 filters on the Oct 16 close (3m rank 100, above 20d and 50d, 8% below its 52w high). I placed a day limit buy for 350 IOVA at 13.90 (about $4,865, within the $5,000 cap), tagged EXP1, with an exit plan. The -8% protective stop at 12.50 goes on once the fill is confirmed. OKTA no longer qualifies (below its 20d). MRNA and TEAM stay open with their GTC stops. Cash is about 90%. Journal updated.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-10-13T04:18 | buy 3 PLTR261113C00210000 limit 13.68 | accepted | S1-live-30d-ATM |  |
| 1 | 2026-10-13T04:18 | buy 11 MRNA limit 216.0 | accepted | STMOM-shares-10d |  |
| 1 | 2026-10-13T04:18 | buy 14 SHOP limit 181.0 | accepted | STMOM-shares-10d |  |
| 1 | 2026-10-13T04:18 | buy 9 ILMN limit 279.0 | accepted | STMOM-shares-10d |  |
| 1 | 2026-10-17T07:49 | sell 3 PLTR261113C00210000 limit 4.6 | accepted | S1-live-30d-ATM |  |
| 2 | 2026-10-13T04:18 | buy 8 DELL limit 582.0 | accepted | H52-stock (E1010-2-615b) |  |
| 2 | 2026-10-13T04:18 | buy 24 TEAM limit 210.0 | rejected | H52-stock (E1010-2-615b) | this position would cost $5,040; the Experiment-level limit is $5,000 (5% of the account, or one contract up to 10%) |
| 2 | 2026-10-13T04:18 | buy 17 DDOG limit 291.0 | accepted | H52-stock (E1010-2-615b) |  |
| 2 | 2026-10-13T04:18 | buy 23 TEAM limit 210.0 | accepted | H52-stock (E1010-2-615b) |  |
| 2 | 2026-10-15T08:17 | sell 8 DELL market | pending_new | H52-stock |  |
| 2 | 2026-10-16T08:10 | buy 86 GTLB limit 57.0 | pending_new | H52-stock |  |
| 2 | 2026-10-17T07:49 | sell 17 DDOG market | accepted | H52-stock |  |
| 3 | 2026-10-13T04:19 | buy 23 MRNA limit 215.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-13T04:19 | buy 24 TEAM limit 209.0 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $5,016; the Experiment-level limit is $5,000 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-13T04:19 | buy 23 PLTR limit 210.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-13T04:19 | buy 23 TEAM limit 209.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-15T08:18 | sell 23 PLTR stop | pending_new |  |  |
| 3 | 2026-10-15T08:18 | sell 23 MRNA stop | pending_new |  |  |
| 3 | 2026-10-15T08:18 | sell 23 TEAM stop | pending_new |  |  |
| 3 | 2026-10-17T07:50 | buy 350 IOVA limit 13.9 | rejected | EXP1 stock momentum-quality, 10-session  | opening a position needs 'exit_plan' (strategy name, why, and 'I am wrong if...') |
| 3 | 2026-10-17T07:50 | sell 350 IOVA stop | rejected | - | you hold 0 and short selling is not enabled (request it if you need it) |
| 3 | 2026-10-17T07:50 | buy 350 IOVA limit 13.9 | accepted | EXP1 stock momentum-quality, 10-session  |  |

## Open experiments

- agent 2 (dry run) **Rule C paper log (trend + flow block, stock long, 10 sessions)** (E1010-2-bb9b): Stocks with 20d return >= 20%, close vs ma20 <= 7.6%, close vs vwap <= 0.8%, price >= $10, dollar volume >= $14M, and no flow block, have a positive median 10-session return when the market 5d return  Expect: Median 10-session stock return above 0 and average above the all-candidate benchmark (about +0.5% median). Expect weak edge, roughly +1% median at bes. Judge by 2026-11-09.
- agent 1 (dry run) **S1-live-01** (E1010-1-6739): S1 (20d%>=20, vs ma50>=15, market 20d>0, shares>=1) buying 30-day ATM calls on live names gives positive average and beats random twins, including the wide list. Expect: Average near the scorebook (+28%), median negative (-20%ish). Win rate ~40%. Exits after 10 sessions.. Judge by 2026-11-09.
- agent 3 (dry run) **52w-high momentum stock trades, 5% size** (E1010-3-8f2e): Liquid stocks at a 52-week high with strong 3-month and 1-month momentum keep drifting up over the next 10 sessions, beating random stocks of the same size and holding time. Expect: Modest edge of about +1% over 10 sessions versus random twins; many trades will be needed to see it through noise.. Judge by 2026-11-09.
- agent 1 **S1-live-30d-ATM** (E1010-1-a499): Strong-trend stocks (20d % >= 20, vs ma50 >= 15, market 20d > 0, shares >= 1) bought as 30-day ATM calls beat random 30-day ATM calls after costs. Expect: Average positive but median negative (scorebook: avg +28%, median -21%). Expect about 40% winners. Wide-list result unknown; judge on my own picks wit. Judge by 2026-11-09.
- agent 1 **D1-live-stock-dip** (E1010-1-213c): Oversold stocks (rsi<35) bought as shares during a market dip (market 5d <= -1.5%) gain about 1.5% over 10 sessions versus the benchmark of about 0.6%. Expect: Median +1.5% over 10 sessions, 55-65% winners. Edge small; costs are small for shares.. Judge by 2026-11-09.
- agent 2 **C-stock: trend-in-weak-market long, 10 sessions** (E1010-2-4296): Stocks with 20-session gains of 20%+ and price within 7.6% of the 20-day average and close not above VWAP by 0.8%+ keep positive 10-session returns when the market's 5-session return is negative. Inhe Expect: Median 10-session stock return above zero, average beating the all-candidate benchmark (about +0.5% median). I expect a modest edge of about +1 to +2%. Judge by 2026-11-09.
- agent 3 **EXP2 large-cap news-gap overreaction fade** (E1010-3-7d1b): Large liquid stocks (dollar volume >= $500M) that fall 8%+ in one session on non-fundamental or sector-spillover news, while still above their 200-day trend, recover part of the drop over the next 10  Expect: Modest bounce of 1-3% on average, but high variance; I expect it to be roughly a coin flip, and I will judge it honestly against random twins.. Judge by 2026-11-09.
- agent 1 **STMOM-shares-10d** (E1010-1-66ad): Liquid large-cap stocks in the top of the 1-month return ranking, with price above the 50-day average, keep drifting up over the next 10 sessions (short-term momentum for high-turnover names, Medhat a Expect: Gross +0.5% to +1% over 10 sessions, about 52-55% winners. Median near zero or slightly positive. Beating random-twin shares by a small margin; if not. Judge by 2026-12-15.
- agent 2 **H52-stock: near 52-week high, above 50d, long 20 sessions** (E1010-2-615b): Stocks trading within 5% of their 52-week high with a rising 50-day average (George and Hwang 2004 style anchoring effect) keep outperforming random stocks over the next 20 sessions, and this holds wh Expect: Median 20-session stock return modestly above the random-stock benchmark, about +0.5 to +1.5%. Expect a small edge, with wide dispersion. Not large.. Judge by 2026-11-09.
- agent 3 **EXP1 stock momentum-quality, 10-session hold** (E1010-3-8b83): Liquid stocks (dollar volume >= $200M) that are near their 52-week high, above both 20- and 50-day averages, and in the top decile of 3-month return keep outperforming over the next 10 sessions, beati Expect: Average excess return of about +1% over 10 sessions vs random liquid stocks, hit rate modestly above 50%. Cost is low (no options), so a small edge ca. Judge by 2026-11-09.
