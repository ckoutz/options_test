# Paper traders (2026-11-06 10:55 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,712 | -3.29% | -5.80% | 100% | 0 | 9 | 1 | 3 | 0.35 |
| 2 | 96,926 | -3.07% | -5.80% | 91% | 2 | 13 | 4 | 2 | 0.50 |
| 3 | 98,247 | -1.75% | -5.80% | 100% | 0 | 18 | 7 | 2 | 0.50 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-11-04** (3 steps, 0 order attempts, $0.00): 2026-11-04: No orders. Account flat at $96,712 (100% cash). SPY is 1.8% below its 20-day average and 1.6% below its 50-day, so the market gate stays closed. ACN is the watch candidate (1m +31%, 3m +50%, no earnings in the next 30 days), but I will only enter once SPY is clearly above its 20-day average. Journal updated with the cash-waiting reason and re-entry conditions.
- **2026-11-05** (3 steps, 0 order attempts, $0.00): No orders. Account still flat at 100% cash ($96,712). SPY rallied 1.7% today but sits at -0.1% versus its 20-day average, short of my +1% gate, so entries stay closed. ACN remains the watch candidate (1m +37%, no earnings in 30 days). Journal updated with the waiting reason and re-entry conditions.
- **2026-11-06** (3 steps, 0 order attempts, $0.00): 2026-11-06: No orders. Account flat at $96,712 (100% cash). SPY is at 733, 4.2% below its 20-day average and 4.3% below its 50-day, after a -4.4% session on 11-05. The market gate is firmly closed. ACN (1m +36%, 3m +52%, no earnings in 30 days) stays on the watch list, but I will not enter into a falling tape. Journal corrected: the old 766.81 SPY level was stale. Re-entry needs SPY at least 1% above its 20-day average with a positive 20-day return, plus ACN or a peer passing the stock gate.

### Agent 2

- **2026-11-04** (3 steps, 0 order attempts, $0.00): 11/04: No new orders. GTLB (52.37, stop ~51.2) and KSS (23.62, stop 22.40) both above stops and inside their rules (no earnings in hold). SPY is still 1.8% below its 20-day average, so the journal's return condition (breadth above 40% and SPY above its 20d average, or a clean screen name with no earnings in hold) is only half met. Screen names are speculative (vol over 100%) or have earnings inside the hold. Cash ~90.5%. Journal updated with the cash reason and exact return triggers.
- **2026-11-05** (3 steps, 0 order attempts, $0.00): 11/05: No new orders. Screened for entries again: MAX passes vol and DV but is a chase (+28% in 5 days, 24% above 20d, no earnings in 30 days) so I passed. SGRY and BRZE fail vol (164%, 181%). SPY still below its 20-day average, so the cash rule is half met. Existing positions KSS (25.40, stop 22.40) and GTLB (52.19, stop ~51.2) are above stops with no earnings in their windows. Cash ~90%. Journal updated with the return triggers and the chase lesson.
- **2026-11-06** (3 steps, 1 order attempts, $0.00): 11/06: SPY fell 4.4% on 11/05 and sits 4.2% below its 20-day average. GTLB closed 48.99, below my 51.2 stop, so I placed a market sell for 86 shares under H52-stock. KSS (23.90, stop 22.40, reports 11/23) stays. No new entries: the screen names are all vol above 100% and the market is weak, so cash stays about 91%. Journal updated with the cash reason and return triggers.

### Agent 3

- **2026-11-04** (3 steps, 0 order attempts, $0.00): Nov 4: No new orders. HTFL (54.40) and NTSK (21.84) remain above their GTC stops (50.98, 20.42), with exits planned around Nov 6. No new names pass the EXP1 filters (earnings inside hold, extended, or volatile). Cash about 90% by design; the journal records the reasons and the re-entry conditions.
- **2026-11-05** (7 steps, 3 order attempts, $0.01): Nov 5: Both EXP1 positions reached their planned 10-session exit. I cancelled the GTC stops (HTFL 50.98, NTSK 20.42) and queued market sells for HTFL 88 sh and NTSK 221 sh, to fill at the Nov 6 open. One placeholder sell was rejected because the shares were held for the stop; no harm. I found no new names that pass the EXP1 filters (earnings inside hold, extended, or gapped), so no new entries. Cash will be about 99% after fills, which is deliberate until a name passes. Journal updated with the cash rationale, redeploy conditions and the Nov 6 re-screen plan.
- **2026-11-06** (4 steps, 1 order attempts, $0.01): Nov 6: Screened 6-month leaders against EXP1 filters (vs_ma20 < +10, no earnings in hold, no up-gap). HAE passes (6m rank 99, vs_ma20 +3.4, no earnings through Dec 6, low 29% vol). Placed a day limit buy of 39 sh at 124.50 (~5% of equity), with an 8% stop (~114.2) and a 10-session exit around Nov 20. Most other leaders were extended, gapped down, or had earnings in the window, so they were skipped. Journal updated with the reasoning and the cash rationale. The HTFL/NTSK exits from Nov 5 are complete.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-11-03T10:51 | sell 14 SHOP market | rejected | STMOM-shares-10d | you hold 0 and short selling is not enabled (request it if you need it) |
| 2 | 2026-10-31T09:39 | sell 169 RXO market | accepted | C-stock |  |
| 2 | 2026-10-31T09:39 | sell 23 TEAM market | accepted | H52-stock |  |
| 2 | 2026-11-06T10:54 | sell 86 GTLB market | pending_new | H52-stock |  |
| 3 | 2026-11-05T10:53 | sell 1 HTFL market | rejected |  | Alpaca refused: HTTP 403: {"available":"0","code":40310000,"existing_qty":"88","held_for_orders":"88","message":"insufficient qty available for order (requested |
| 3 | 2026-11-05T10:53 | sell 88 HTFL market | pending_new | EXP1 exit |  |
| 3 | 2026-11-05T10:53 | sell 221 NTSK market | pending_new | EXP1 exit |  |
| 3 | 2026-11-06T10:55 | buy 39 HAE limit 124.5 | pending_new | EXP1 stock momentum-quality, 10-session  |  |

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
