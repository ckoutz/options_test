# Paper traders (2026-10-31 09:39 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,769 | -3.23% | -2.88% | 98% | 1 | 9 | 0 | 3 | 0.31 |
| 2 | 97,428 | -2.57% | -2.88% | 81% | 4 | 12 | 4 | 2 | 0.48 |
| 3 | 99,325 | -0.67% | -2.88% | 89% | 2 | 15 | 6 | 2 | 0.46 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-29** (3 steps, 0 order attempts, $0.00): 2026-10-29: No new orders. SPY is only marginally above its 20-day average (+0.2%, 20-day return +1.1%), so the market gate is not clearly open and the account stays about 97% cash. SHOP (14 sh, about 168, -3.7%) is held under the 10-day rule with its GTC stop at 153.7; earnings are 11-03 pre-market. Journal updated with the cash-waiting reason and re-entry conditions. ACN noted as a candidate, not bought.
- **2026-10-30** (3 steps, 0 order attempts, $0.00): 2026-10-30: No new orders. SPY is 0.2% below its 20-day average, so the market gate stays closed and the account is about 97% cash. ACN is strong but has no clean gate, so I passed. SHOP (14 sh, about 164, -6%) is held under the 10-day rule with its GTC stop at 153.7. Earnings are 11-03 pre-market. Journal updated and reconciled with the account.
- **2026-10-31** (3 steps, 0 order attempts, $0.00): 2026-10-31 (Saturday): No new orders. Account reconciled: 97.7% cash, SHOP 14 sh at 157.49 (-9.8%) with GTC stop 153.7 resting. SHOP reports 11-03 before open (EPS est 0.47, recent record mixed); I'll decide that morning whether to sell at the open. Market gate remains closed (S&P 20-session -1.1%, only 47.5% of stocks above 50-day), so no new entries. Journal updated with the corrected SHOP price and re-entry conditions.

### Agent 2

- **2026-10-29** (3 steps, 0 order attempts, $0.00): 2026-10-29: No new orders. All five positions are above their stops: DXC 16.09 (stop 14.80, earnings after the close today), RXO 27.60 (stop 26.20, after a -5% day), KSS 23.68 (stop 22.40), GTLB ~55.60 (stop ~51.2), TEAM 208.30 (stop 188.96). All three C-stock slots are full, so no new entries. FIGS is the candidate for the next free slot. Cash is 75.9%; the reason for waiting and the return conditions are in the journal.
- **2026-10-30** (5 steps, 1 order attempts, $0.01): 10/30: DXC gapped to 13.05 on a guidance cut, below my 14.80 stop, so I sold all 300 shares at market. Passed on FIGS because its earnings (11/05) fall inside the 10-session hold. No new buys. Remaining: RXO, KSS, GTLB, TEAM. RXO and TEAM report 11/05, and I lean toward exiting them before the report. Cash about 76%. Journal updated with the reason for waiting and the new no-earnings-in-hold rule.
- **2026-10-31** (4 steps, 2 order attempts, $0.01): 10/31 (Saturday): Submitted market exits for RXO (169 sh) and TEAM (23 sh) to avoid the 11/05 earnings window. RXO had already reported on 10/29, so the date in my notes was likely wrong; I'll verify. KSS and GTLB held (both above stops, no earnings in their windows). No new entries: breadth is about 44-47% and most screen names have earnings inside the hold. Cash about 81%. Journal updated with the return conditions.

### Agent 3

- **2026-10-29** (4 steps, 1 order attempts, $0.01): Oct 29: Cancelled the IOVA GTC stop (12.50) and placed a market sell of 350 IOVA (planned 10-session EXP1 exit; fill expected Oct 30). Replacement candidate CDNA (vs MA20 +7.9, not extended) will be bought the next session after the sale fills, to respect the 3-name cap. CAI and GRAL now too extended. HTFL and NTSK held to ~Nov 6 with GTC stops 50.98 and 20.42. Cash ~84% by design; journal updated with the cash rationale and the redeploy plan.
- **2026-10-30** (3 steps, 1 order attempts, $0.00): Oct 30: IOVA exit filled (350 sh at 11.20). Placed a day limit buy of 69 CDNA at 72 (about 5% of equity), to fill the freed EXP1 slot. CDNA passes the screen (vs_ma20 +6.6, 0.8% off its 52-week high). Stop at about -8% once filled, and a 10-session exit around Nov 12. HTFL and NTSK are still held to ~Nov 6 with GTC stops at 50.98 and 20.42. Cash stays high by design: the 3-name cap and narrow filters mean few entries. Journal updated with the cash rationale and redeploy conditions.
- **2026-10-31** (5 steps, 0 order attempts, $0.01): Oct 31: No new orders. CDNA's 72 limit expired unfilled after the stock ran to 87 (+22% on Oct 30, vs_ma20 +28), so I dropped it rather than chase. Other screen candidates (LIFE, QLYS) have earnings inside a 10-session hold (Nov 2 and Nov 9), and CAI/GRAL are extended or volatile, so no entries. HTFL and NTSK are held with GTC stops at 50.98 and 20.42, with planned exits around Nov 6. Cash about 89%, deliberate per the journal; redeploy conditions are written there.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-10-27T09:00 | sell 9 ILMN market | pending_new | STMOM-shares-10d |  |
| 2 | 2026-10-30T10:01 | sell 300 DXC market | pending_new | C-stock stop exit |  |
| 2 | 2026-10-31T09:39 | sell 169 RXO market | accepted | C-stock |  |
| 2 | 2026-10-31T09:39 | sell 23 TEAM market | accepted | H52-stock |  |
| 3 | 2026-10-29T09:58 | sell 350 IOVA market | pending_new | EXP1 exit |  |
| 3 | 2026-10-30T10:01 | buy 69 CDNA limit 72.0 | pending_new | EXP1 stock momentum-quality, 10-session  |  |

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
