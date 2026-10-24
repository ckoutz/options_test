# Paper traders (2026-10-24 08:09 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,954 | -3.05% | -2.33% | 95% | 2 | 8 | 0 | 3 | 0.29 |
| 2 | 99,309 | -0.69% | -2.33% | 75% | 5 | 9 | 4 | 2 | 0.45 |
| 3 | 100,128 | +0.13% | -2.33% | 85% | 3 | 13 | 6 | 2 | 0.43 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-22** (3 steps, 0 order attempts, $0.00): 2026-10-22: No new orders. Held MRNA (+15.6%, stop 184, planned exit ~10-27, Phase 3 data 10-24 covered by stop), SHOP (-2.4%, stop 153.7, earnings 11-03 after exit), ILMN (+1.8%, stop 242.7, earnings 10-29 after close, after planned exit). ACN passes stock screen but market 20-day return is ~0, so entry gate stays closed. About 92% cash. Journal updated.
- **2026-10-23** (2 steps, 0 order attempts, $0.00): Fri 2026-10-23: No new orders. Market 20-day return is still slightly negative (-0.5%), so the entry gate stays closed and cash is about 95%. Holding ILMN (9 sh, -2.3%, stop 242.7; earnings 10-29, planned exit ~10-27) and SHOP (14 sh, -3.7%, stop 153.7). Both have resting GTC stops. Corrected the journal: MRNA was stopped out on 10-20 at 183.54, so it has not been held since then. My 10-21 and 10-22 notes were wrong. Journal updated.
- **2026-10-24** (3 steps, 0 order attempts, $0.00): Sat 2026-10-24: no new orders. Market gate still closed (SPY -1.3% vs 20-day average, 20-session return -0.9%), so I stay about 95% cash on purpose. Holding ILMN (9 sh, stop 242.7, planned exit to be placed 10-26 ahead of 10-29 earnings) and SHOP (14 sh, stop 153.7). Journal updated with the cash-waiting reason and the exact re-entry conditions. Reconciled against the account: MRNA is not held.

### Agent 2

- **2026-10-22** (2 steps, 0 order attempts, $0.00): 2026-10-22: No new orders. GTLB (54.58, -1.6% today) and TEAM (221.75, -1.7% today) both remain above their stops (GTLB ~51.2 / 50d MA; TEAM 188.96 / ma50). Breadth 39.3% above ma50, just under my 40% return-to-trading threshold, and the C-stock screen is still not finalized in writing, so no new entries. Cash ~90%, reason recorded in journal. Journal updated.
- **2026-10-23** (15 steps, 6 order attempts, $0.07): Breadth rose to 44.1% above ma50, clearing my 40% return threshold. I wrote the C-stock screen before trading: $10+, DV>=14M, above 50d MA, vol20 at or below 100%, no pending takeovers, rank by 1-month return, top 3 at ~5% each, hold 10 sessions. The first attempt at CBRL and ACN was rejected for exceeding the 5% size cap. After applying the screen, I placed day limit buys on DXC (300 @16.40), RXO (169 @29.10), and KSS (198 @24.90), each about $4,900, with stops at about -8% to -10%. The screen was written after seeing the leaders list, so there is some hindsight, and I'm judging it on the trade record. GTLB and TEAM stay open with stops unchanged (GTLB ~51.2, TEAM 188.96). Journal updated.
- **2026-10-24** (2 steps, 0 order attempts, $0.00): Saturday 2026-10-24, no market session. Confirmed the three C-stock limit buys filled on 10/23 (DXC, RXO, KSS). Checked all five positions against their stops (DXC 14.80, RXO 26.20, KSS 22.40, GTLB ~51.2, TEAM 188.96); none is close to triggering. No new orders. Cash is 75.2%, with the reason and the conditions for adding exposure written in the journal. Next review on Monday 10/26.

### Agent 3

- **2026-10-22** (3 steps, 0 order attempts, $0.00): Oct 22: No new orders. Held the three EXP1 positions: IOVA 14.42 (entry 13.90, stop 12.50), MRNA 241.34 (entry 207.68, stop 191.10), TEAM 221.75 (entry 208.99, stop 192.20). All GTC stops in place. The three-name cap is full, so no new entries. Planned exits: MRNA and TEAM around Oct 27, IOVA around Oct 31, or the stop, whichever comes first. Equity 100,862, about 84% cash. Journal updated.
- **2026-10-23** (9 steps, 6 order attempts, $0.03): Oct 23: MRNA fell 17.6% on Oct 22 on a reported trial-data leak. Its 191.10 GTC stop appears to have filled before my cancel, so the position is out (verify the fill). Market sell of TEAM placed for its planned 10-session exit. Two EXP1 replacement buys placed as day limits: HTFL 88 sh at 56 and NTSK 221 sh at 22.50, both under the $4,978 cap. The first attempts were rejected for cap or short-position reasons, so I resized them. IOVA holds its 12.50 stop. Stops for HTFL and NTSK go on after fills. Journal updated.
- **2026-10-24** (3 steps, 2 order attempts, $0.01): Saturday Oct 24: no new entries. Placed GTC protective stop-sells: HTFL 88 sh at 50.98 and NTSK 221 sh at 20.42 (both -8% from fills). IOVA keeps its 12.50 stop. HTFL has a new lawsuit headline (Heartflow vs Elucid), noted as risk. Cash about 85%, which is deliberate: the EXP1 filters are narrow, the three open names are extended, and the 3-name cap is full. Journal updated with the cash rationale and the conditions for redeploying. Next: IOVA exit around Oct 30-31; HTFL/NTSK exits around Nov 6; FOMC Oct 27-28.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-10-20T08:31 | sell 11 MRNA stop | pending_new |  |  |
| 1 | 2026-10-20T08:31 | sell 14 SHOP stop | pending_new |  |  |
| 1 | 2026-10-20T08:31 | sell 9 ILMN stop | pending_new |  |  |
| 2 | 2026-10-23T08:35 | buy 73 CBRL limit 68.0 | rejected | C-stock (E1010-2-4296) | this position would cost $4,964; the Experiment-level limit is $4,943 (5% of the account, or one contract up to 10%) |
| 2 | 2026-10-23T08:35 | buy 19 ACN limit 262.0 | rejected | C-stock (E1010-2-4296) | this position would cost $4,978; the Experiment-level limit is $4,943 (5% of the account, or one contract up to 10%) |
| 2 | 2026-10-23T08:35 |  0   | rejected |  | side must be buy or sell and qty must be positive |
| 2 | 2026-10-23T08:35 | buy 300 DXC limit 16.4 | pending_new | C-stock (E1010-2-4296) |  |
| 2 | 2026-10-23T08:35 | buy 169 RXO limit 29.1 | pending_new | C-stock (E1010-2-4296) |  |
| 2 | 2026-10-23T08:35 | buy 198 KSS limit 24.9 | pending_new | C-stock (E1010-2-4296) |  |
| 3 | 2026-10-20T08:31 | sell 350 IOVA stop | pending_new | EXP1 protective stop |  |
| 3 | 2026-10-23T08:36 | sell 23 MRNA market | rejected | EXP1 exit | you hold 0 and short selling is not enabled (request it if you need it) |
| 3 | 2026-10-23T08:36 | sell 23 TEAM market | pending_new | EXP1 exit |  |
| 3 | 2026-10-23T08:36 | buy 89 HTFL limit 56.0 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $4,984; the Experiment-level limit is $4,978 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-23T08:36 | buy 222 NTSK limit 22.5 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $4,995; the Experiment-level limit is $4,978 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-23T08:36 | buy 88 HTFL limit 56.0 | pending_new | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-23T08:37 | buy 221 NTSK limit 22.5 | pending_new | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-24T08:09 | sell 88 HTFL stop | accepted | EXP1 protective stop |  |
| 3 | 2026-10-24T08:09 | sell 221 NTSK stop | accepted | EXP1 protective stop |  |

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
