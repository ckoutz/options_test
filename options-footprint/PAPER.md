# Paper traders (2026-11-04 10:57 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 96,712 | -3.29% | -3.05% | 100% | 0 | 9 | 1 | 3 | 0.34 |
| 2 | 97,168 | -2.83% | -3.05% | 91% | 2 | 12 | 4 | 2 | 0.49 |
| 3 | 98,252 | -1.75% | -3.05% | 90% | 2 | 15 | 6 | 2 | 0.47 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-31** (3 steps, 0 order attempts, $0.00): 2026-10-31 (Saturday): No new orders. Account reconciled: 97.7% cash, SHOP 14 sh at 157.49 (-9.8%) with GTC stop 153.7 resting. SHOP reports 11-03 before open (EPS est 0.47, recent record mixed); I'll decide that morning whether to sell at the open. Market gate remains closed (S&P 20-session -1.1%, only 47.5% of stocks above 50-day), so no new entries. Journal updated with the corrected SHOP price and re-entry conditions.
- **2026-11-03** (8 steps, 1 order attempts, $0.02): 2026-11-03: Account is flat with 100% cash ($96,712.20). The SHOP 14-share position from my journal is no longer held. I cancelled its resting GTC stop (153.7) and a market exit was rejected because there were 0 shares. The SHOP exit price and date are unverified, probably a stop fill on 11-02. No new orders: the S&P is below its 20- and 50-day averages (-2.2%, -1.9%), so the market gate is closed. Journal and experiment E1010-1-66ad are corrected to the flat account. Next step: reconcile holdings and open orders before writing any exit plan.
- **2026-11-04** (3 steps, 0 order attempts, $0.00): 2026-11-04: No orders. Account flat at $96,712 (100% cash). SPY is 1.8% below its 20-day average and 1.6% below its 50-day, so the market gate stays closed. ACN is the watch candidate (1m +31%, 3m +50%, no earnings in the next 30 days), but I will only enter once SPY is clearly above its 20-day average. Journal updated with the cash-waiting reason and re-entry conditions.

### Agent 2

- **2026-10-31** (4 steps, 2 order attempts, $0.01): 10/31 (Saturday): Submitted market exits for RXO (169 sh) and TEAM (23 sh) to avoid the 11/05 earnings window. RXO had already reported on 10/29, so the date in my notes was likely wrong; I'll verify. KSS and GTLB held (both above stops, no earnings in their windows). No new entries: breadth is about 44-47% and most screen names have earnings inside the hold. Cash about 81%. Journal updated with the return conditions.
- **2026-11-03** (3 steps, 0 order attempts, $0.00): 11/03: No new orders. Checked earnings: KSS reports 11/23 and GTLB has no report in the 30-day window, so both are inside the rules. KSS 24.15 (stop 22.40), GTLB 52.11 (stop ~51.2, watch it). Market is weak (SPY -2.2% vs 20-day average), breadth ~51%, and most screen names have earnings inside the hold, so I stay ~91% cash. Journal updated with the cash reason and return conditions (breadth above 40% and SPY back above its 20-day average, or a screen name with no earnings in its hold).
- **2026-11-04** (3 steps, 0 order attempts, $0.00): 11/04: No new orders. GTLB (52.37, stop ~51.2) and KSS (23.62, stop 22.40) both above stops and inside their rules (no earnings in hold). SPY is still 1.8% below its 20-day average, so the journal's return condition (breadth above 40% and SPY above its 20d average, or a clean screen name with no earnings in hold) is only half met. Screen names are speculative (vol over 100%) or have earnings inside the hold. Cash ~90.5%. Journal updated with the cash reason and exact return triggers.

### Agent 3

- **2026-10-31** (5 steps, 0 order attempts, $0.01): Oct 31: No new orders. CDNA's 72 limit expired unfilled after the stock ran to 87 (+22% on Oct 30, vs_ma20 +28), so I dropped it rather than chase. Other screen candidates (LIFE, QLYS) have earnings inside a 10-session hold (Nov 2 and Nov 9), and CAI/GRAL are extended or volatile, so no entries. HTFL and NTSK are held with GTC stops at 50.98 and 20.42, with planned exits around Nov 6. Cash about 89%, deliberate per the journal; redeploy conditions are written there.
- **2026-11-03** (3 steps, 0 order attempts, $0.01): Nov 3: No new orders. HTFL and NTSK fell 7-10% on Nov 2 but remain above their GTC stops (50.98, 20.42), with exits planned around Nov 6. Screened CAI, GRAL, QLYS, LIFE and the 6-month leaders: all either gapped down or extended, or have earnings inside a 10-session hold, so none passes the EXP1 filters. Cash about 90% by design; re-entry conditions are in the journal.
- **2026-11-04** (3 steps, 0 order attempts, $0.00): Nov 4: No new orders. HTFL (54.40) and NTSK (21.84) remain above their GTC stops (50.98, 20.42), with exits planned around Nov 6. No new names pass the EXP1 filters (earnings inside hold, extended, or volatile). Cash about 90% by design; the journal records the reasons and the re-entry conditions.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-11-03T10:51 | sell 14 SHOP market | rejected | STMOM-shares-10d | you hold 0 and short selling is not enabled (request it if you need it) |
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
- agent 2 **H52-stock: near 52-week high, above 50d, long 20 sessions** (E1010-2-615b): Stocks trading within 5% of their 52-week high with a rising 50-day average (George and Hwang 2004 style anchoring effect) keep outperforming random stocks over the next 20 sessions, and this holds wh Expect: Median 20-session stock return modestly above the random-stock benchmark, about +0.5 to +1.5%. Expect a small edge, with wide dispersion. Not large.. Judge by 2026-11-09.
- agent 3 **EXP1 stock momentum-quality, 10-session hold** (E1010-3-8b83): Liquid stocks (dollar volume >= $200M) that are near their 52-week high, above both 20- and 50-day averages, and in the top decile of 3-month return keep outperforming over the next 10 sessions, beati Expect: Average excess return of about +1% over 10 sessions vs random liquid stocks, hit rate modestly above 50%. Cost is low (no options), so a small edge ca. Judge by 2026-11-09.
- agent 1 **STMOM-shares-10d** (E1010-1-66ad): Liquid large-cap stocks in the top of the 1-month return ranking, with price above the 50-day average, keep drifting up over the next 10 sessions (short-term momentum for high-turnover names, Medhat a Expect: Gross +0.5% to +1% over 10 sessions, about 52-55% winners. Median near zero or slightly positive. Beating random-twin shares by a small margin; if not. Judge by 2026-12-15.
