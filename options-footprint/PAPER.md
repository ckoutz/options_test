# Paper traders (2026-10-22 08:36 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 97,719 | -2.28% | -0.64% | 92% | 3 | 8 | 0 | 3 | 0.28 |
| 2 | 98,929 | -1.07% | -0.64% | 90% | 2 | 6 | 1 | 2 | 0.38 |
| 3 | 100,862 | +0.86% | -0.64% | 84% | 3 | 8 | 3 | 2 | 0.39 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-20** (5 steps, 3 order attempts, $0.01): Held the three STMOM share positions (MRNA, SHOP, ILMN); none at stop or below 50-day. Placed resting GTC stop-loss orders on all three at their planned 12% levels (MRNA 184, SHOP 153.7, ILMN 242.7), per the lesson from the missed PLTR option stop. No new trades: no stock passed the momentum gate and the market 20-day return is roughly flat. About 92% cash. Journal updated. MRNA has Phase 3 melanoma data Sat 10-24, inside the hold; the GTC stop covers the gap risk.
- **2026-10-21** (3 steps, 0 order attempts, $0.00): 2026-10-21: No new orders. Held the three STMOM share positions with resting GTC stops (MRNA 184, SHOP 153.7, ILMN 242.7). MRNA +15%, SHOP -1%, ILMN -3%; none at stop, MRNA Phase 3 data Sat 10-24 is covered by the stop. ACN passed the stock-level momentum screen but the market 20-day return is -0.6%, so the entry gate stays closed. About 92% cash. Journal updated with positions, watch item ACN, and re-entry conditions.
- **2026-10-22** (3 steps, 0 order attempts, $0.00): 2026-10-22: No new orders. Held MRNA (+15.6%, stop 184, planned exit ~10-27, Phase 3 data 10-24 covered by stop), SHOP (-2.4%, stop 153.7, earnings 11-03 after exit), ILMN (+1.8%, stop 242.7, earnings 10-29 after close, after planned exit). ACN passes stock screen but market 20-day return is ~0, so entry gate stays closed. About 92% cash. Journal updated.

### Agent 2

- **2026-10-20** (3 steps, 0 order attempts, $0.01): 2026-10-20: No new orders. Checked both open positions against the newest closes (10/19 data): GTLB 53.29 is above its ~51.2 stop and well above its 50d MA; TEAM 214.75 is above its 188.96 stop and ma50. Both stay open. Market breadth is still narrow (30.8% above ma50), so the H52 screen gave no new qualified names beyond the two holdings, and the C-stock screen is still not written down, so no C-stock entries. Cash ~90%; the reason and the conditions for returning to trading are recorded in the journal.
- **2026-10-21** (3 steps, 0 order attempts, $0.01): 2026-10-21: No new orders. GTLB (55.00, above ~51.2 stop and 50d MA) and TEAM (221.11, at 52-week high, above 188.96 stop and ma50) both remain open and within their rules. Breadth improved to 36.2% above ma50 but is still below the 40-50% level I set for returning to active trading, and the C-stock screen is still not written down, so no new entries. Cash ~90%. Journal updated.
- **2026-10-22** (2 steps, 0 order attempts, $0.00): 2026-10-22: No new orders. GTLB (54.58, -1.6% today) and TEAM (221.75, -1.7% today) both remain above their stops (GTLB ~51.2 / 50d MA; TEAM 188.96 / ma50). Breadth 39.3% above ma50, just under my 40% return-to-trading threshold, and the C-stock screen is still not finalized in writing, so no new entries. Cash ~90%, reason recorded in journal. Journal updated.

### Agent 3

- **2026-10-20** (3 steps, 1 order attempts, $0.00): Oct 20: No new entries. I placed a GTC protective stop-sell on 350 IOVA at 12.50 (-8% from the 13.90 fill). MRNA (226.89, stop 191.10) and TEAM (214.75, stop 192.20) stay in EXP1 with their GTC stops. The three EXP1 names are all extended above their 20-day averages. The 3-name cap is full, so there are no new buys. Planned exits are about Oct 27 to 30, or the stops. Journal updated.
- **2026-10-21** (2 steps, 0 order attempts, $0.00): Oct 21: No new orders. Held the three EXP1 positions (IOVA 14.90 vs 13.90 entry, MRNA 240.46 vs 207.68, TEAM 219.78 vs 208.99). All GTC stops remain in place (IOVA 12.50, MRNA 191.10, TEAM 192.20). The 3-name cap is full, so no new entries. Planned exits: MRNA and TEAM about Oct 27, IOVA about Oct 31, or the stop, whichever is first. Market softening (S&P -1.2% over 5 sessions) and FOMC Oct 27-28 ahead. Journal updated.
- **2026-10-22** (3 steps, 0 order attempts, $0.00): Oct 22: No new orders. Held the three EXP1 positions: IOVA 14.42 (entry 13.90, stop 12.50), MRNA 241.34 (entry 207.68, stop 191.10), TEAM 221.75 (entry 208.99, stop 192.20). All GTC stops in place. The three-name cap is full, so no new entries. Planned exits: MRNA and TEAM around Oct 27, IOVA around Oct 31, or the stop, whichever comes first. Equity 100,862, about 84% cash. Journal updated.

## Orders in the last 7 days

| agent | when (UTC) | order | status | strategy | note |
|---|---|---|---|---|---|
| 1 | 2026-10-17T07:49 | sell 3 PLTR261113C00210000 limit 4.6 | accepted | S1-live-30d-ATM |  |
| 1 | 2026-10-20T08:31 | sell 11 MRNA stop | pending_new |  |  |
| 1 | 2026-10-20T08:31 | sell 14 SHOP stop | pending_new |  |  |
| 1 | 2026-10-20T08:31 | sell 9 ILMN stop | pending_new |  |  |
| 2 | 2026-10-16T08:10 | buy 86 GTLB limit 57.0 | pending_new | H52-stock |  |
| 2 | 2026-10-17T07:49 | sell 17 DDOG market | accepted | H52-stock |  |
| 3 | 2026-10-17T07:50 | buy 350 IOVA limit 13.9 | rejected | EXP1 stock momentum-quality, 10-session  | opening a position needs 'exit_plan' (strategy name, why, and 'I am wrong if...') |
| 3 | 2026-10-17T07:50 | sell 350 IOVA stop | rejected | - | you hold 0 and short selling is not enabled (request it if you need it) |
| 3 | 2026-10-17T07:50 | buy 350 IOVA limit 13.9 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-20T08:31 | sell 350 IOVA stop | pending_new | EXP1 protective stop |  |

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
