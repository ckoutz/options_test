# Paper traders (2026-11-21 11:00 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,712 | -3.29% | -11.35% | 100% | 0 | 9 | 1 | 3 | 0.38 |
| 2 | 96,643 | -3.36% | -11.35% | 100% | 0 | 15 | 4 | 2 | 0.56 |
| 3 | 97,955 | -2.04% | -11.35% | 95% | 1 | 22 | 8 | 2 | 0.55 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-11-19** (3 steps, 0 order attempts, $0.00): No orders. Account flat at $96,712 (100% cash), reconciled with journal. SPY 730.20 is 3.1% below its 20-day average, so the +1% reclaim gate stays closed. ACN fell 4.9% to 227.49 (-9.5% vs MA20) and is not entered. Journal updated with the waiting reason and re-entry conditions.
- **2026-11-20** (3 steps, 0 order attempts, $0.00): 2026-11-20: No orders. Account flat at $96,712 (100% cash). SPY 715.87 fell 2.0% on the day and is 4.7% below its 20-day average, so the +1% reclaim gate stays firmly closed. ACN fell to 218.58 (-12.3% vs MA20), a falling knife, not entered. Journal updated with the waiting reason (cash over 75% for 20+ sessions) and exact re-entry conditions: SPY gate plus a stock passing the stock gate and an earnings check.
- **2026-11-21** (3 steps, 0 order attempts, $0.00): No orders. Account flat at $96,712 (100% cash), reconciled with journal. SPY closed 689.81, 7.8% below its 20-day average, so the +1% reclaim gate stays firmly closed. ACN at 221.17 is still 10.8% below its MA20 (falling knife per lesson 10) and not entered. Journal updated with the waiting reason and re-entry conditions (SPY gate, a stock passing the stock gate, and an earnings check).

### Agent 2

- **2026-11-19** (5 steps, 1 order attempts, $0.01): 11/19: No new entries. SPY 730.2 is 3.1% below its 20-day average and falling, so the market gate is still closed; the liquid screen's 1-month leaders are chases or vol above 100%. KSS rebounded to 24.04, but the earnings tool shows a report on 11/23 inside the planned hold, and the last quarter missed EPS by 46%. I placed a day limit sell of 198 shares at 23.90 to exit before the report. Cash is about 95%. Journal updated with the cash reasoning, the earnings correction, and the exit.
- **2026-11-20** (3 steps, 1 order attempts, $0.00): 2026-11-20: Market gate still closed. SPY 715.87 is down 7.4% over 20 sessions and breadth is 35.7%. The liquid screen's 1-month leaders are chases (60%+ above 20d) or vol above 100%, so no new entries. KSS closed 22.99 on 11/19, below the 23.90 exit limit, which never filled. Earnings are on 11/23 inside the hold, and the last quarter missed EPS by 46%. I placed a market sell of 198 KSS to exit before the report. Cash is about 95%. The journal is updated with the cash reasoning and the return triggers.
- **2026-11-21** (3 steps, 0 order attempts, $0.01): 2026-11-21: No new orders. SPY 689.81 is 7.8% below its 20-day average and 9.2% below its 50-day, with breadth at 32%, so the market gate is still closed. The liquid screen's 1-month leaders are crash-rebound names with volatility above 100% or chases, and the losers are falling knives, so nothing passes. Account is 100% cash at about 96.6k. Journal updated with the cash reason and the exact return triggers.

### Agent 3

- **2026-11-19** (6 steps, 2 order attempts, $0.01): 2026-11-19: Re-screened the top 25 six-month leaders against EXP1 filters. None qualify (extended, high-vol, or gapped), so no new entries. HAE's planned time exit is due 11-20. My first limit sell was rejected because the GTC stop held all shares, so I cancelled that stop and placed a day limit sell of 39 sh at 122.00 (order a47e4c4b). If it doesn't fill, HAE is unprotected and I need to re-place a stop. AMPL (283 sh, stop 15.83) is held to its ~Nov 27 planned exit. Account ~90% cash by design; journal updated with the cash rationale, the redeploy conditions, and the lesson about GTC stops blocking exits.
- **2026-11-20** (3 steps, 0 order attempts, $0.01): 2026-11-20: HAE time exit filled at 122.80 on 11-19, so HAE is closed. Only AMPL remains (283 sh, 16.54, GTC stop 15.83). Re-screened the top 6-month leaders against EXP1 filters: none pass. Near-misses (TRAX, INTA, CERT, PD, APPN) are below their 20-day averages and still need earnings checks. Breadth fell to 35.7%, so my redeploy conditions are not met. No new orders; staying in cash by design. Journal updated.
- **2026-11-21** (3 steps, 0 order attempts, $0.01): Saturday 11-21: No new orders. Re-screened the top 6-month leaders against EXP1 filters (vs_ma20 < +10, vol < 60%, no earnings in hold, no 5%+ gap); none qualify, and breadth fell to 32% with the S&P fund down about 10% over 20 sessions, so my redeploy conditions are not met. Only AMPL is held (283 sh at 16.20, -5.8%) with a GTC stop at 15.83 and a planned time exit around Nov 27. Account is about 95% cash by design; journal updated with the cash rationale and the conditions that would bring me back.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 2 | 2026-11-19T11:36 | sell 198 KSS limit 23.9 | pending_new | H52-stock exit (legacy position) |  |
| 2 | 2026-11-20T11:34 | sell 198 KSS market | pending_new | H52-stock exit (legacy position) |  |
| 3 | 2026-11-19T11:36 | sell 39 HAE limit 122.0 | rejected | EXP1 stock momentum-quality exit | Alpaca refused: HTTP 403: {"available":"0","code":40310000,"existing_qty":"39","held_for_orders":"39","message":"insufficient qty available for order (requested |
| 3 | 2026-11-19T11:36 | sell 39 HAE limit 122.0 | pending_new | EXP1 stock momentum-quality exit |  |

## Open experiments

- agent 2 (dry run) **Rule C paper log (trend + flow block, stock long, 10 sessions)** (E1010-2-bb9b): Stocks with 20d return >= 20%, close vs ma20 <= 7.6%, close vs vwap <= 0.8%, price >= $10, dollar volume >= $14M, and no flow block, have a positive median 10-session return when the market 5d return  Expect: Median 10-session stock return above 0 and average above the all-candidate benchmark (about +0.5% median). Expect weak edge, roughly +1% median at bes. Judge by 2026-11-09.
- agent 1 (dry run) **S1-live-01** (E1010-1-6739): S1 (20d%>=20, vs ma50>=15, market 20d>0, shares>=1) buying 30-day ATM calls on live names gives positive average and beats random twins, including the wide list. Expect: Average near the scorebook (+28%), median negative (-20%ish). Win rate ~40%. Exits after 10 sessions.. Judge by 2026-11-09.
- agent 3 (dry run) **52w-high momentum stock trades, 5% size** (E1010-3-8f2e): Liquid stocks at a 52-week high with strong 3-month and 1-month momentum keep drifting up over the next 10 sessions, beating random stocks of the same size and holding time. Expect: Modest edge of about +1% over 10 sessions versus random twins; many trades will be needed to see it through noise.. Judge by 2026-11-09.
- agent 1 **S1-live-30d-ATM** (E1010-1-a499): Strong-trend stocks (20d % >= 20, vs ma50 >= 15, market 20d > 0, shares >= 1) bought as 30-day ATM calls beat random 30-day ATM calls after costs. Expect: Average positive but median negative (scorebook: avg +28%, median -21%). Expect about 40% winners. Wide-list result unknown; judge on my own picks wit. Judge by 2026-11-09.
- agent 1 **D1-live-stock-dip** (E1010-1-213c): Oversold stocks (rsi<35) bought as shares during a market dip (market 5d <= -1.5%) gain about 1.5% over 10 sessions versus the benchmark of about 0.6%. Expect: Median +1.5% over 10 sessions, 55-65% winners. Edge small; costs are small for shares.. Judge by 2026-11-09.
- agent 2 **C-stock: trend-in-weak-market long, 10 sessions** (E1010-2-4296): Stocks with 20-session gains of 20%+ and price within 7.6% of the 20-day average and close not above VWAP by 0.8%+ keep positive 10-session returns when the market's 5-session return is negative. Inhe Expect: Median 10-session stock return above zero, average beating the all-candidate benchmark (about +0.5% median). I expect a modest edge of about +1 to +2%. Judge by 2026-11-09.
- agent 3 **EXP2 large-cap news-gap overreaction fade** (E1010-3-7d1b): Large liquid stocks (dollar volume >= $500M) that fall 8%+ in one session on non-fundamental or sector-spillover news, while still above their 200-day trend, recover part of the drop over the next 10  Expect: Modest bounce of 1-3% on average, but high variance; I expect it to be roughly a coin flip, and I will judge it honestly against random twins.. Judge by 2026-11-09.
- agent 2 **H52-stock: near 52-week high, above 50d, long 20 sessions** (E1010-2-615b): Stocks trading within 5% of their 52-week high with a rising 50-day average (George and Hwang 2004 style anchoring effect) keep outperforming random stocks over the next 20 sessions, and this holds wh Expect: Median 20-session stock return modestly above the random-stock benchmark, about +0.5 to +1.5%. Expect a small edge, with wide dispersion. Not large.. Judge by 2026-11-09.
- agent 3 **EXP1 stock momentum-quality, 10-session hold** (E1010-3-8b83): Liquid stocks (dollar volume >= $200M) that are near their 52-week high, above both 20- and 50-day averages, and in the top decile of 3-month return keep outperforming over the next 10 sessions, beati Expect: Average excess return of about +1% over 10 sessions vs random liquid stocks, hit rate modestly above 50%. Cost is low (no options), so a small edge ca. Judge by 2026-11-09.
- agent 1 **STMOM-shares-10d** (E1010-1-66ad): Liquid large-cap stocks in the top of the 1-month return ranking, with price above the 50-day average, keep drifting up over the next 10 sessions (short-term momentum for high-turnover names, Medhat a Expect: Gross +0.5% to +1% over 10 sessions, about 52-55% winners. Median near zero or slightly positive. Beating random-twin shares by a small margin; if not. Judge by 2026-12-15.
