# Paper traders (2026-10-29 09:58 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,930 | -3.07% | -0.74% | 98% | 1 | 9 | 0 | 3 | 0.31 |
| 2 | 98,434 | -1.57% | -0.74% | 76% | 5 | 9 | 4 | 2 | 0.47 |
| 3 | 101,218 | +1.22% | -0.74% | 84% | 3 | 14 | 6 | 2 | 0.45 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-27** (5 steps, 1 order attempts, $0.01): 2026-10-27: Planned exit of ILMN (9 sh) placed as a market sell ahead of its 10-29 after-close earnings; cancelled its GTC stop 242.7 to avoid a double sell. SHOP (14 sh, stop 153.7) held under the 10-day rule, with earnings 11-03 after the window. No new entries: market gate still closed (SPY 20-day -0.8%), about 95% cash. Journal updated with the cash-waiting reason and re-entry conditions.
- **2026-10-28** (3 steps, 0 order attempts, $0.00): 2026-10-28: No new orders. SPY is 0.1% below its 20-day average, so the market gate stays closed and the account remains about 97% cash. SHOP (14 sh, about 165.8, -5%) is held under the 10-day rule with its GTC stop at 153.7; earnings are 11-03 pre-market. ILMN was sold 10-27 ahead of earnings and MRNA is not held. Journal updated with the cash-waiting reason and re-entry conditions.
- **2026-10-29** (3 steps, 0 order attempts, $0.00): 2026-10-29: No new orders. SPY is only marginally above its 20-day average (+0.2%, 20-day return +1.1%), so the market gate is not clearly open and the account stays about 97% cash. SHOP (14 sh, about 168, -3.7%) is held under the 10-day rule with its GTC stop at 153.7; earnings are 11-03 pre-market. Journal updated with the cash-waiting reason and re-entry conditions. ACN noted as a candidate, not bought.

### Agent 2

- **2026-10-27** (4 steps, 0 order attempts, $0.01): 2026-10-27: No new orders. All five positions (DXC, RXO, KSS, GTLB, TEAM) are well above their stops; KSS is closest at 23.65 vs 22.40 stop. Breadth is 44.4% above ma50, above my 40% threshold, but all three C-stock slots are full. FIGS and RPD pass the screen's volume and trend filters and are on the watch list for the next free slot. Cash 75.3%; the reason for waiting is in the journal.
- **2026-10-28** (3 steps, 0 order attempts, $0.00): 2026-10-28: No new orders. All five positions are above their stops (KSS closest at 23.78 vs 22.40). The C-stock slots are full, so I'm holding. FIGS and RPD stay on the watch list for the next free slot. Cash 75.5%; the reason for waiting and the return conditions are in the journal. Next review: DXC earnings 10/29 after close.
- **2026-10-29** (3 steps, 0 order attempts, $0.00): 2026-10-29: No new orders. All five positions are above their stops: DXC 16.09 (stop 14.80, earnings after the close today), RXO 27.60 (stop 26.20, after a -5% day), KSS 23.68 (stop 22.40), GTLB ~55.60 (stop ~51.2), TEAM 208.30 (stop 188.96). All three C-stock slots are full, so no new entries. FIGS is the candidate for the next free slot. Cash is 75.9%; the reason for waiting and the return conditions are in the journal.

### Agent 3

- **2026-10-27** (3 steps, 0 order attempts, $0.01): 2026-10-27: No new orders. The EXP1 3-name cap is full (IOVA, HTFL, NTSK), and the screen's passing names (LIFE, GRAL, CAI, CDNA) are the next candidates for an open slot. IOVA exits ~Oct 30-31 (stop 12.50), HTFL/NTSK ~Nov 6 (stops 50.98 and 20.42). Cash ~85%, deliberate per the journal. Journal updated with the cash rationale and redeployment conditions.
- **2026-10-28** (3 steps, 0 order attempts, $0.01): Oct 28: No new orders. The EXP1 3-name cap is full (IOVA, HTFL, NTSK). IOVA's planned 10-session exit is Oct 30, and the slot then goes to the best screen name (CAI or CDNA preferred; GRAL is extended after a +7.6% day). HTFL and NTSK are held to ~Nov 6 with GTC stops at 50.98 and 20.42. Cash about 84%, which is deliberate per the journal. Journal updated.
- **2026-10-29** (4 steps, 1 order attempts, $0.01): Oct 29: Cancelled the IOVA GTC stop (12.50) and placed a market sell of 350 IOVA (planned 10-session EXP1 exit; fill expected Oct 30). Replacement candidate CDNA (vs MA20 +7.9, not extended) will be bought the next session after the sale fills, to respect the 3-name cap. CAI and GRAL now too extended. HTFL and NTSK held to ~Nov 6 with GTC stops 50.98 and 20.42. Cash ~84% by design; journal updated with the cash rationale and the redeploy plan.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-10-27T09:00 | sell 9 ILMN market | pending_new | STMOM-shares-10d |  |
| 2 | 2026-10-23T08:35 | buy 73 CBRL limit 68.0 | rejected | C-stock (E1010-2-4296) | this position would cost $4,964; the Experiment-level limit is $4,943 (5% of the account, or one contract up to 10%) |
| 2 | 2026-10-23T08:35 | buy 19 ACN limit 262.0 | rejected | C-stock (E1010-2-4296) | this position would cost $4,978; the Experiment-level limit is $4,943 (5% of the account, or one contract up to 10%) |
| 2 | 2026-10-23T08:35 |  0   | rejected |  | side must be buy or sell and qty must be positive |
| 2 | 2026-10-23T08:35 | buy 300 DXC limit 16.4 | pending_new | C-stock (E1010-2-4296) |  |
| 2 | 2026-10-23T08:35 | buy 169 RXO limit 29.1 | pending_new | C-stock (E1010-2-4296) |  |
| 2 | 2026-10-23T08:35 | buy 198 KSS limit 24.9 | pending_new | C-stock (E1010-2-4296) |  |
| 3 | 2026-10-23T08:36 | sell 23 MRNA market | rejected | EXP1 exit | you hold 0 and short selling is not enabled (request it if you need it) |
| 3 | 2026-10-23T08:36 | sell 23 TEAM market | pending_new | EXP1 exit |  |
| 3 | 2026-10-23T08:36 | buy 89 HTFL limit 56.0 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $4,984; the Experiment-level limit is $4,978 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-23T08:36 | buy 222 NTSK limit 22.5 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $4,995; the Experiment-level limit is $4,978 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-23T08:36 | buy 88 HTFL limit 56.0 | pending_new | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-23T08:37 | buy 221 NTSK limit 22.5 | pending_new | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-24T08:09 | sell 88 HTFL stop | accepted | EXP1 protective stop |  |
| 3 | 2026-10-24T08:09 | sell 221 NTSK stop | accepted | EXP1 protective stop |  |
| 3 | 2026-10-29T09:58 | sell 350 IOVA market | pending_new | EXP1 exit |  |

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
