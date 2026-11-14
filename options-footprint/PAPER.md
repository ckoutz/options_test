# Paper traders (2026-11-14 10:24 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,712 | -3.29% | -3.05% | 100% | 0 | 9 | 1 | 3 | 0.37 |
| 2 | 96,931 | -3.07% | -3.05% | 95% | 1 | 13 | 4 | 2 | 0.53 |
| 3 | 98,284 | -1.72% | -3.05% | 90% | 2 | 21 | 7 | 2 | 0.52 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-11-12** (3 steps, 0 order attempts, $0.00): No orders. Account flat at $96,712 (100% cash), reconciled with journal. SPY 759.81 is -0.1% vs its 20-day average, so the +1% reclaim gate stays closed. ACN (1m +18.8%, 3m +43%, no earnings in 30 days) remains the watch candidate but will not be entered until the market gate opens. Journal updated with the waiting reason and re-entry conditions.
- **2026-11-13** (3 steps, 0 order attempts, $0.00): No orders. Account flat at $96,712 (100% cash). SPY 757.12 is 0.3% below its 20-day average, so the +1% gate is still closed. ACN (1m +16%, 3m +42%) slipped to just below its MA20 after a -5.7% week, so it is not entered. Journal updated with waiting reason and re-entry conditions (SPY gate plus ACN reclaiming MA20).
- **2026-11-14** (3 steps, 0 order attempts, $0.00): 2026-11-14: No orders. Account flat at $96,712 (100% cash), reconciled with journal. SPY 754.37 is 0.6% below its 20-day average, so the +1% reclaim gate stays closed. ACN (250.49, -0.4% vs MA20, 1m +11%, 3m +48%) is still the watch candidate but not entered: it needs the market gate and its own MA20 reclaim. Journal updated with the waiting reason and re-entry conditions.

### Agent 2

- **2026-11-12** (4 steps, 0 order attempts, $0.01): 11/12: No new orders. SPY is back to its 20-day average (-0.1%), but no liquid screen name passes all filters: the 1-month leaders are chases or have vol above 100%, and TRAX is pre-revenue with a large EPS miss. Cash gate is half met, so I stay in cash. KSS (24.48-24.65, stop 22.40, earnings 11/23 outside the hold) stays. Journal updated with the cash reason and exact return triggers.
- **2026-11-13** (3 steps, 0 order attempts, $0.01): 2026-11-13: No new orders. SPY slipped to -0.3% vs its 20-day average, so the market gate is still not met, and no liquid screen name passes the filters (leaders are chases or vol over 100%; TRAX is pre-revenue with a large EPS miss). KSS closed 23.50 on 11/12 (-4.7%), still above the 22.40 stop, earnings 11/23 outside the hold. Cash ~95%. Journal updated with the cash reason and exact return triggers.
- **2026-11-14** (3 steps, 0 order attempts, $0.01): 2026-11-14: No new orders. SPY is 0.6% below its 20-day average, so the market gate is still not met, and the liquid screen is again dominated by chases and vol-over-100% names. KSS closed 24.00 (+2.1%), above the 22.40 stop, with earnings 11/23 outside the hold. Cash ~95%. Journal updated with the cash reason and the exact return triggers.

### Agent 3

- **2026-11-12** (3 steps, 0 order attempts, $0.01): Nov 12: HAE still held (39 sh, 120.54, -1.5% today), GTC stop at 114.20 in place, planned exit around Nov 20. Re-screened the top 6-month leaders against EXP1 filters: all are extended, 100%+ vol, gapped, or fail trend; AMPL is the closest and needs an earnings check before any entry. No new orders. Account about 95% cash by design; journal updated with the cash rationale and what would bring me back to investing.
- **2026-11-13** (4 steps, 1 order attempts, $0.01): Nov 13: HAE still held with its 114.20 stop in place. AMPL passed every EXP1 filter (6m rank 100, vs_ma20 +3.4, vol 50%, no earnings in the next 30 days, no gap up), so I placed a day limit buy of 283 sh at 17.25 (~5% of equity) with an exit plan of an 8% stop and a 10-session exit. Journal updated with the cash-streak rationale and the redeploy conditions.
- **2026-11-14** (2 steps, 1 order attempts, $0.00): Saturday 2026-11-14, no session. Placed a GTC protective stop sell on AMPL (283 sh) at 15.83, 8% under the 17.19 fill, since I had missed placing one on the fill day. HAE stop at 114.20 remains in place. No new entries: no name passes the EXP1 filters. Journal updated with the cash rationale, the redeploy conditions, and the stop lesson. Planned exits: HAE and AMPL around Nov 20 and Nov 27.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 3 | 2026-11-13T10:58 | buy 283 AMPL limit 17.25 | pending_new | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-11-14T10:24 | sell 283 AMPL stop | accepted | EXP1 stock momentum-quality protective s |  |

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
