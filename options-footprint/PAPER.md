# Paper traders (2026-10-13 04:20 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 100,000 | +0.00% | +0.00% | 100% | 0 | 4 | 0 | 3 | 0.24 |
| 2 | 100,000 | +0.00% | +0.00% | 100% | 0 | 3 | 1 | 2 | 0.34 |
| 3 | 100,000 | +0.00% | +0.00% | 100% | 0 | 3 | 3 | 2 | 0.29 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Answered requests

- R1010-1-4eb0 approved: Please add a free earnings-date calendar (upcoming and last report dates with EPS actual vs estimate) for liquid US stocks. Needed to avoid buying opt — Approved. New tool earnings: report dates, before open or after close, EPS estimate vs actual and surprise, plus each stock's last few quarters (Finnhub free plan, so history is short). Sector funds already work in price_history: any symbol, e.g. XLK, XLE, XLF.
- R1010-3-0d86 approved: Request for free data built from existing sources: (1) per-stock share turnover (shares traded / shares outstanding) so I can split the short-term mom — Approved. New tool turnover: shares outstanding, daily turnover over 20 and 120 sessions, and whether trading has picked up, plus industry and market value. New tool earnings covers report dates for the next 30 or more sessions.
- R1010-2-23a9 approved: Request: historical end-of-day option quotes (bid/ask/IV/delta, 20-60 DTE, near-the-money calls and puts) for liquid US stocks over the last 2 years,  — Partly approved. New tool option_history: past daily prices for any option contract, expired ones included, from early 2024 (about 2.5 years), with the stock close and implied volatility worked out each day. Limits: these are daily closing trades, not bid/ask quotes, and delta is not included. Subtract realistic spread costs yourself. Earnings history: see the new earnings tool.

## Latest days

### Agent 1

- **2026-10-10** (8 steps, 0 order attempts, $0.23): Research day, no orders (Sat 2026-10-10). Searched six-plus topics across momentum, short-term reversal, post-earnings drift, variance risk premium, options flow, sector rotation, dip-buying and option costs, and read three sources. Checked the leader list, options-flow scan, PLTR history/options and news against the research. Decisions: keep S1 (PLTR Nov 6 210 call, 3 contracts at the Monday open only if the open is 200-217 and the gate still holds). Registered a new share-momentum experiment STMOM-shares-10d (20 trades, judge 2026-12-15) with a watchlist of candidates. Rejected short-term reversal, PEAD for now, variance-premium selling, and index dip-buying, with reasons written in the journal. Filed a data request for an earnings-date calendar and sector ETF histories. Still 100% cash.
- **2026-10-13** (6 steps, 4 order attempts, $0.01): Tue 2026-10-13. Ran the S1 gate on PLTR using the 10-12 close: passes (20-session +20.6%, 17% above 50-day). Placed a limit buy for 3x PLTR 2026-11-13 210 call at 13.68 (S1-live-30d-ATM). Applied the STMOM rule to 1-month leaders with dollar volume >= $1bn and price above 50-day: bought MRNA 11 sh (limit 216), SHOP 14 sh (limit 181), ILMN 9 sh (limit 279) under STMOM-shares-10d. Each position is about 2.5% of account. Orders execute 10-14. Exit plans: options after about 10 sessions, shares after about 10 sessions (~10-27), or on a 12% stop or a close below the 50-day. Journal updated, including the $1bn dollar-volume deviation from the plan's $300m.

### Agent 2

- **2026-10-10** (9 steps, 0 order attempts, $0.33): Research day, no orders. Reviewed 9 strategy families (time-series momentum, short-term reversal, PEAD, variance premium, options flow, industry momentum, retail earnings option losses, 52-week-high anchoring, large-cap 12-1 momentum). Most edges are small, decay after costs, or are gross-only; options look like a loss-maker for retail. Market: SPY 778.57, near its high, but breadth is narrow (32% above ma50), leadership is in tech and speculative names, and yields and oil are high. C-stock gate (SPY 5d < 0) fails today, so no entries. Registered H52-stock (52-week-high anchoring, stock only, 20 trades). Filed a data request for historical option quotes and earnings dates. Saved a candidate watchlist. Journal written as a game plan with research notes.
- **2026-10-13** (5 steps, 4 order attempts, $0.01): 2026-10-13: C-stock gate closed (SPY 5d +0.4%), no trades. H52-stock screen run: placed limit buys for DELL (8 sh, <=582), DDOG (17 sh, <=291), and TEAM (23 sh, <=210; 24 was rejected for exceeding the $5,000 experiment cap). Each about 5% of account. No options. Exits planned after 20 sessions (~2026-11-10) or on a close below the 50d MA / -10% from entry. Journal updated with the screen, candidates passed over, and the sizing rule.

### Agent 3

- **2026-10-10** (10 steps, 0 order attempts, $0.28): Research day, no orders. Market: S&P near highs (778.57, +3% 20d) but narrow breadth (32% above 50d), 10y yield near 5.26%, CPI Oct 14, Fed Oct 28. Research covered four families: momentum (Medhat & Schmeling 2022: short-term momentum in liquid high-turnover large caps, survives costs), short-term reversal (Quantpedia: survives only in the largest stocks, costs eat it elsewhere), PEAD (cost-sensitive, rejected for now), and option buying (negative expected returns in the literature, rejected as default), plus low-beta and industry momentum as background. Corrected the EXP1 candidate list against the 3-month leaders screen: META, NVDA, AAPL, AMZN, GOOGL, PTC, P, MRNA fail the filters; kept TEAM, OKTA, HPE, PLTR, VEEV, MPC, MSFT, FRO, U. TMUS fails EXP2's above-200-day filter (down 33% over 12 months). Options: IV is 40-58% on TMUS/PLTR and about 26% on AAPL, so no option trades. Filed data request R1010-3-0d86 for turnover and an earnings calendar. Journal rewritten as a full game plan with research notes. Both experiments stay registered; Monday's plan is to apply the EXP1 screen to that day's data and buy up to 3 names at 5%.
- **2026-10-13** (4 steps, 4 order attempts, $0.01): Applied the EXP1 screen to the Oct 12 close (3m leaders, $200M+ liquidity, above 20d and 50d, within 10% of 52w high, vs_ma20 <= 15%). Placed three limit buys at 5% each, tagged E1010-3-8b83: MRNA (23 sh, limit 215), PLTR (23 sh, limit 210), TEAM (23 sh, limit 209). Exit is 10 sessions later (about Oct 27) or an 8% stop. The first TEAM order was rejected for breaching the $5,000 experiment cap, so I resized it. OKTA passes but is not bought because the 3-name cap is full. TMUS fails EXP2's 200-day filter, so no EXP2 trade. No options. About 85% of the account stays in cash. Software and AI concentration is a known risk. Journal updated.

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
| 3 | 2026-10-10T21:37 | buy 1 AAPL limit 1.0 | rejected | smoke | too small: $1 is under the 1% minimum ($1,000) |
| 3 | 2026-10-10T21:37 | buy 1 AAPL261120C00340000 limit 10.42 | dry-run | smoke |  |
| 3 | 2026-10-10T21:40 | buy 1 AAPL limit 1.0 | rejected | smoke | too small: $1 is under the 1% minimum ($1,000) |
| 3 | 2026-10-10T21:40 | buy 1 AAPL261120C00340000 limit 10.42 | dry-run | smoke |  |
| 3 | 2026-10-13T04:19 | buy 23 MRNA limit 215.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-13T04:19 | buy 24 TEAM limit 209.0 | rejected | EXP1 stock momentum-quality, 10-session  | this position would cost $5,016; the Experiment-level limit is $5,000 (5% of the account, or one contract up to 10%) |
| 3 | 2026-10-13T04:19 | buy 23 PLTR limit 210.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |
| 3 | 2026-10-13T04:19 | buy 23 TEAM limit 209.0 | accepted | EXP1 stock momentum-quality, 10-session  |  |

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
