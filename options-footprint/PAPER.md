# Paper traders (2026-10-10 23:02 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | not started | | | | | | | | |
| 2 | not started | | | | | | | | |
| 3 | not started | | | | | | | | |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Latest days

### Agent 1

- **2026-10-10** (5 steps, 0 order attempts, $0.01): Research day, no orders (Sat 2026-10-10). Market: S&P 778.57, near high, 20d +3%, but only 32% of stocks above 50-day, so breadth is narrow. Dip rules and S5 inactive. S1 (strong-trend calls) is the live candidate. Exact 20-session gate check: PLTR +25% (passes, vs ma50 +18%), AMD +17.8% (fails). PLTR Nov 6 210 call mid ~13.09 (IV 59%, tight spread), planned 3 contracts at the open Monday only if the price is not chased above ~217. Saved the S1-candidates watchlist and updated the journal with the game plan and exit/stop rules. Still 100% cash. Experiments S1-live-30d-ATM and D1-live-stock-dip are registered.

### Agent 2

- **2026-10-10** (4 steps, 0 order attempts, $0.03): Research day, no orders. Market: SPY near its high (+1.2% over 5 sessions) but only 32% of stocks above their 50-day average, so breadth is narrow. Inherited rule C needs a negative 5-day market gate, which fails today, so no entries. Registered experiment C-stock (20 trades to judge, 5% sizing when it fires). Journal rewritten as a game plan. Next session: check SPY 5-day and screen rule C only if the gate opens.

### Agent 3

- **2026-10-10** (6 steps, 0 order attempts, $0.04): Research day, no orders. Market: S&P near highs (+3% 20d) but narrow breadth (32% above 50d), yields at 24-year highs, CPI and bank earnings next week. Options are expensive (AAPL 41-day ATM call ~3% of stock per week plus 10%+ round-trip cost), so I'm defaulting to stock-only strategies. Registered two experiments: EXP1 (E1010-3-8b83) liquid momentum-near-highs, 10-session hold, 30 trades to judge; EXP2 (E1010-3-7d1b) large-cap gap-down fade, 20 trades. Saved watchlists for both and wrote the game plan in the journal: on Monday re-screen with leaders(), buy up to 3 EXP1 names at 5%, watch TMUS for stabilization for EXP2.

## Open experiments

- agent 2 (dry run) **Rule C paper log (trend + flow block, stock long, 10 sessions)** (E1010-2-bb9b): Stocks with 20d return >= 20%, close vs ma20 <= 7.6%, close vs vwap <= 0.8%, price >= $10, dollar volume >= $14M, and no flow block, have a positive median 10-session return when the market 5d return  Expect: Median 10-session stock return above 0 and average above the all-candidate benchmark (about +0.5% median). Expect weak edge, roughly +1% median at bes. Judge by 2026-11-09.
- agent 1 (dry run) **S1-live-01** (E1010-1-6739): S1 (20d%>=20, vs ma50>=15, market 20d>0, shares>=1) buying 30-day ATM calls on live names gives positive average and beats random twins, including the wide list. Expect: Average near the scorebook (+28%), median negative (-20%ish). Win rate ~40%. Exits after 10 sessions.. Judge by 2026-11-09.
- agent 3 (dry run) **52w-high momentum stock trades, 5% size** (E1010-3-8f2e): Liquid stocks at a 52-week high with strong 3-month and 1-month momentum keep drifting up over the next 10 sessions, beating random stocks of the same size and holding time. Expect: Modest edge of about +1% over 10 sessions versus random twins; many trades will be needed to see it through noise.. Judge by 2026-11-09.
- agent 1 **S1-live-30d-ATM** (E1010-1-a499): Strong-trend stocks (20d % >= 20, vs ma50 >= 15, market 20d > 0, shares >= 1) bought as 30-day ATM calls beat random 30-day ATM calls after costs. Expect: Average positive but median negative (scorebook: avg +28%, median -21%). Expect about 40% winners. Wide-list result unknown; judge on my own picks wit. Judge by 2026-11-09.
- agent 1 **D1-live-stock-dip** (E1010-1-213c): Oversold stocks (rsi<35) bought as shares during a market dip (market 5d <= -1.5%) gain about 1.5% over 10 sessions versus the benchmark of about 0.6%. Expect: Median +1.5% over 10 sessions, 55-65% winners. Edge small; costs are small for shares.. Judge by 2026-11-09.
- agent 2 **C-stock: trend-in-weak-market long, 10 sessions** (E1010-2-4296): Stocks with 20-session gains of 20%+ and price within 7.6% of the 20-day average and close not above VWAP by 0.8%+ keep positive 10-session returns when the market's 5-session return is negative. Inhe Expect: Median 10-session stock return above zero, average beating the all-candidate benchmark (about +0.5% median). I expect a modest edge of about +1 to +2%. Judge by 2026-11-09.
- agent 3 **EXP1 stock momentum-quality, 10-session hold** (E1010-3-8b83): Liquid stocks (dollar volume >= $200M) that are near their 52-week high, above both 20- and 50-day averages, and in the top decile of 3-month return keep outperforming over the next 10 sessions, beati Expect: Average excess return of about +1% over 10 sessions vs random liquid stocks, hit rate modestly above 50%. Cost is low (no options), so a small edge ca. Judge by 2026-11-09.
- agent 3 **EXP2 large-cap news-gap overreaction fade** (E1010-3-7d1b): Large liquid stocks (dollar volume >= $500M) that fall 8%+ in one session on non-fundamental or sector-spillover news, while still above their 200-day trend, recover part of the drop over the next 10  Expect: Modest bounce of 1-3% on average, but high variance; I expect it to be roughly a coin flip, and I will judge it honestly against random twins.. Judge by 2026-11-09.
