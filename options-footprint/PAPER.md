# Paper traders (2026-11-28 11:42 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,712 | -3.29% | -6.40% | 100% | 0 | 9 | 1 | 3 | 0.40 |
| 2 | 96,643 | -3.36% | -6.40% | 100% | 0 | 15 | 4 | 2 | 0.58 |
| 3 | 98,264 | -1.74% | -6.40% | 100% | 0 | 24 | 10 | 2 | 0.59 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-11-26** (3 steps, 0 order attempts, $0.00): 2026-11-26: No orders. Account flat at $96,712.20 (100% cash), reconciled with journal. SPY 716.70 is 3.2% below its 20-day average, so the +1% gate stays closed. ACN 240.49 rallied 3.5% but is still 2.4% below its MA20, so it is not entered under lesson 10. Journal updated with the waiting reason and re-entry conditions (SPY gate open plus a stock passing the stock gate, with ACN needing an MA20 reclaim and an earnings check; ACN reports 12-16).
- **2026-11-27** (3 steps, 0 order attempts, $0.00): 2026-11-27: No orders. Account flat at $96,712.20 (100% cash), reconciled with journal. SPY 716.70 remains 3.2% below its 20-day average, so the +1% gate stays closed. ACN 240.49 is 2.4% below its MA20 (reclaim ~246) and not entered under lesson 10. Journal updated: still waiting; re-entry requires SPY gate open plus a stock passing the stock gate, and for ACN an MA20 reclaim and earnings check (reports 12-16).
- **2026-11-28** (3 steps, 0 order attempts, $0.00): 2026-11-28 (Sat): No orders. Account flat at $96,712.20, 100% cash, reconciled with journal. SPY 728.32 is 1.3% below its 20-day average (gate needs +1%), so the S1 market gate stays closed. ACN 241.84 is 1.7% below its MA20 (reclaim ~246) after a 10.6% five-day run; not entered under lesson 10 and lesson 9 (no chasing relief rallies). Still waiting for the SPY gate plus a stock passing the stock gate. Journal updated.

### Agent 2

- **2026-11-26** (3 steps, 0 order attempts, $0.00): 2026-11-26: No orders. SPY 716.7 is still 3.2% below its 20-day average, so the market gate is closed. The 1-month liquid leaders are either crash rebounds with volatility above 100% or chases more than 20% above the 20-day average. The closest name, XERS, has volatility of 103%, just over my limit. Account is 100% cash at about 96.6k. Journal updated with the cash reasoning and the exact conditions that would bring me back.
- **2026-11-27** (3 steps, 0 order attempts, $0.00): 2026-11-27: No orders. SPY 716.7 is still 3.2% below its 20-day average, so the market gate stays closed. The 1-month liquid leaders are crash rebounds with vol above 100% or chases 20%+ above the 20d average; XERS is closest but its vol20 is 103%. Account remains 100% cash at about 96.6k. Journal updated with the cash reasoning and the exact return triggers (SPY close above 20d avg plus a screen name passing all filters).
- **2026-11-28** (3 steps, 0 order attempts, $0.00): 2026-11-28 (Saturday): No orders. SPY 728.32 rose 1.6% on 11/27 but is still 1.3% below its 20-day average, so the market gate stays closed. Screen leaders are either crash rebounds with volatility above 100% or stocks well above their 20-day average (UPBD, XERS, INSM, SBIT, BRBR, VRDN). Account remains 100% cash at about 96.6k. Journal updated with cash reasons and exact return triggers.

### Agent 3

- **2026-11-26** (8 steps, 2 order attempts, $0.01): 11-26: Reviewed AMPL (283 sh, 17.10) and the three EXP1 candidates (CERT, APPN, INTA), which pass the technical and earnings filters. No new entries: breadth was 37.4% on the last reading, below my 50% gate, so cash stays about 95% by design. Problem: I cancelled AMPL's GTC stop for review, and the cancel is stuck in pending_cancel. Both replacement attempts at 15.83 were rejected because the 283 shares are still held for the old order. AMPL may be unprotected right now. Next session: check the account first and re-place the stop, or exit at the open since the planned time exit (~Nov 27) is due. Lesson recorded: do not cancel stops for review.
- **2026-11-27** (3 steps, 1 order attempts, $0.00): 11-27: AMPL's old GTC stop was gone (no open orders), so the position was unprotected. Per the planned 10-session time exit, I placed a day market sell of 283 AMPL for 11-30. Screened CERT, APPN and INTA: they pass technical filters, but breadth (42.8% above 50-day) is still below my 50% redeploy gate and not in the 30-40% sample-building band. No new entries; account stays about 95% cash by design. Journal updated with the cancel-stop lesson and the redeploy conditions.
- **2026-11-28** (3 steps, 0 order attempts, $0.00): 11-28 (Saturday): Account is 100% cash at $98,264 after AMPL's planned time exit filled at 17.29 on 11-27. Screened CERT (passes technical filters) and APPN (passes; extended at 52w high). INTA is outside the liquid universe. Breadth is 42.8%, below my 50% redeploy gate and outside the 30-40% sample-building band, so no new entries. Journal updated with the cash rationale and the exact conditions that would bring me back: breadth above 50%, or a pre-registered 5% sample trade if breadth stays 30-40% through about Dec 1.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 3 | 2026-11-25T12:51 | sell 283 AMPL stop | pending_new | EXP1 stock momentum-quality exit |  |
| 3 | 2026-11-26T12:27 | sell 283 AMPL stop | rejected | EXP1 stock momentum-quality exit | Alpaca refused: HTTP 403: {"available":"0","code":40310000,"existing_qty":"283","held_for_orders":"283","message":"insufficient qty available for order (request |
| 3 | 2026-11-26T12:28 | sell 283 AMPL stop | rejected | EXP1 stock momentum-quality exit | Alpaca refused: HTTP 403: {"available":"0","code":40310000,"existing_qty":"283","held_for_orders":"283","message":"insufficient qty available for order (request |
| 3 | 2026-11-27T12:15 | sell 283 AMPL market | pending_new | EXP1 stock momentum-quality exit |  |

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
