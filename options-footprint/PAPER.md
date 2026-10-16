# Paper traders (2026-10-16 08:10 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 99,190 | -0.81% | -0.81% | 89% | 4 | 4 | 0 | 3 | 0.26 |
| 2 | 99,158 | -0.84% | -0.81% | 90% | 2 | 5 | 1 | 2 | 0.36 |
| 3 | 100,709 | +0.71% | -0.81% | 85% | 3 | 6 | 1 | 2 | 0.37 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-14** (4 steps, 0 order attempts, $0.01): 2026-10-14: No new orders. The three share positions (MRNA, SHOP, ILMN) and the PLTR 210 Nov-13 call filled at yesterday's limits and are in the book. Checked earnings dates: MRNA (10-29 pre-market), ILMN (10-29 after close) and SHOP (11-03 pre-market) all fall after the planned ~10-27 share exit, and PLTR (11-09) after the ~10-28 option exit, so no hold conflicts with earnings. Account equity about $100,044 (+0.04% since season start) vs S&P roughly flat. Journal updated with positions, exit rules and open experiments. Still mostly cash (about 89%).
- **2026-10-15** (3 steps, 0 order attempts, $0.00): 2026-10-15: No new orders. Held PLTR 210 Nov-13 call (3 contracts, now 10.15 vs 13.60 fill, -25%, option stop at -50%) and the three STMOM share positions: MRNA up about 8%, SHOP -1.3%, ILMN -1.5%, none at the 12% stop or below the 50-day. No earnings conflicts before planned exits (~10-27/10-28). Account about 89% cash. Journal updated with positions, stops, and open experiments. No new setup passed the rules today, and the existing experiments need their full sample before judging.
- **2026-10-16** (3 steps, 0 order attempts, $0.01): Fri 2026-10-16: No new orders. Reviewed the open book: PLTR 210 Nov-13 call (3 contracts, about -27%, option stop at -50%, planned exit about 10-28), and STMOM share positions MRNA (+13%), SHOP (+1.6%), ILMN (-2.1%). None is at the 12% stop or below its 50-day. Earnings calendar checked: no held name reports before its planned exit. No new setup passed the S1 or STMOM gates, so I stay about 89% cash. Journal updated with the cash rationale and re-entry conditions.

### Agent 2

- **2026-10-14** (3 steps, 0 order attempts, $0.00): 2026-10-14: No new orders. Kept the three H52-stock positions (DELL, DDOG, TEAM, about 5% each). DELL has no earnings in the window. TEAM and DDOG report 2026-11-05, inside the 20-session hold; I accept that as part of the experiment and will not add through earnings. The C-stock gate technically reopened (SPY 5d -0.1%), but I ran no screen and placed no trades, so I did not claim a C-stock entry. Journal updated with the book, earnings dates and the screen rule.
- **2026-10-15** (5 steps, 1 order attempts, $0.01): 2026-10-15: DELL closed at the -10% stop: market sell of 8 sh submitted for the next open (entry 553.95, now 489, -11.7%). DDOG (-7.5%) and TEAM (-2.6%) kept under their -10% stops and earnings-window rules. C-stock gate open but the exact screen is not yet written, so no C-stock trades. No options. Journal updated with the stop record and an action item to write the C-stock screen.
- **2026-10-16** (5 steps, 1 order attempts, $0.01): 2026-10-16: Placed one H52-stock limit buy for GTLB (86 sh, limit 57, ~5% of account), the third slot in the max-3 H52 book. GTLB is 0.1% off its 52-week high, 19% above its 50-day average, with no earnings in the 20-session window. Kept DDOG (-6.9%, stop 257.36) and TEAM (+3.4%, stop 188.96 or close below ma50). Did not trade C-stock: the screen still needs to be written down and confirmed before any entry. Journal updated with the GTLB exit plan and a draft C-stock screen for review.

### Agent 3

- **2026-10-14** (3 steps, 0 order attempts, $0.04): Oct 14: No new orders. The three EXP1 positions (MRNA, PLTR, TEAM, all entered Oct 13) are within their stops: MRNA about +3%, PLTR flat, TEAM about -1%. OKTA passes the screen but the 3-name cap is full. I could not confirm the September CPI print (only previews), so I did not change position size; the rule is to cut EXP1 to 3% if core is above 0.6% m/m, and I'll recheck before any new entry. Cash remains about 85%. Journal updated with the status, risks, and the exit schedule (about Oct 27 or the -8% stop).
- **2026-10-15** (4 steps, 3 order attempts, $0.03): Oct 15: No new entries. Verified the Sept CPI print (core +0.3% m/m, headline +0.6%, hotter than expected, so the EXP1 size-cut rule does not trigger). Placed GTC protective stop-sells at about -8% on the three EXP1 positions (PLTR 191.60, MRNA 191.10, TEAM 192.20). Cash stays about 86%. The EXP1 exit is about Oct 27 or the stop. OKTA still passes the screen but the 3-name cap is full. Journal updated.
- **2026-10-16** (3 steps, 0 order attempts, $0.00): Oct 16: No new orders. EXP1 positions (MRNA 236.5, PLTR 200.5, TEAM 217.12) remain well above their GTC stops (191.10, 191.60, 192.20). The 3-name cap is full, so OKTA passes the screen but is not bought. Equity 100,709, about 85% cash. Plan: hold to about Oct 27 exit or stop, whichever comes first. Journal updated.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-10-13T04:18 | buy 3 PLTR261113C00210000 limit 13.68 | accepted | S1-live-30d-ATM |  |
| 1 | 2026-10-13T04:18 | buy 11 MRNA limit 216.0 | accepted | STMOM-shares-10d |  |
| 1 | 2026-10-13T04:18 | buy 14 SHOP limit 181.0 | accepted | STMOM-shares-10d |  |
| 1 | 2026-10-13T04:18 | buy 9 ILMN limit 279.0 | accepted | STMOM-shares-10d |  |
| 2 | 2026-10-13T04:18 | buy 8 DELL limit 582.0 | accepted | H52-stock (E1010-2-615b) |  |
| 2 | 2026-10-13T04:18 | buy 24 TEAM limit 210.0 | rejected | H52-stock (E1010-2-615b) | this position would cost $5,040; the Experiment-level limit is $5,000 (5% of the account, or one contract up to 10%) |
| 2 | 2026-10-13T04:18 | buy 17 DDOG limit 291.0 | accepted | H52-stock (E1010-2-615b) |  |
| 2 | 2026-10-13T04:18 | buy 23 TEAM limit 210.0 | accepted | H52-stock (E1010-2-615b) |  |
| 2 | 2026-10-15T08:17 | sell 8 DELL market | pending_new | H52-stock |  |
| 2 | 2026-10-16T08:10 | buy 86 GTLB limit 57.0 | pending_new | H52-stock |  |
| 3 | 2026-10-13T04:19 | buy 23 MRNA limit 215.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-13T04:19 | buy 24 TEAM limit 209.0 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $5,016; the Experiment-level limit is $5,000 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-13T04:19 | buy 23 PLTR limit 210.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-13T04:19 | buy 23 TEAM limit 209.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-15T08:18 | sell 23 PLTR stop | pending_new |  |  |
| 3 | 2026-10-15T08:18 | sell 23 MRNA stop | pending_new |  |  |
| 3 | 2026-10-15T08:18 | sell 23 TEAM stop | pending_new |  |  |

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
