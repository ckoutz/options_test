# Paper traders (2026-10-10 21:48 UTC)

Season 1: 6 months, with a checkpoint at 3 months.

Agent 1: the research committee's final playbook. Agent 2: the playoff pick (the trader whose approach held up best). Agent 3: fresh, no notes (the control).

| agent | equity $ | return since start | S&P 500 since start | cash % | positions | orders sent | rejected | open experiments | model cost $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 100,000 | +0.00% | +0.00% | 100% | 0 | 0 | 0 | 1 | 0.02 |
| 2 | 100,000 | +0.00% | +0.00% | 100% | 0 | 0 | 0 | 1 | 0.00 |
| 3 | 100,000 | +0.00% | +0.00% | 100% | 0 | 0 | 1 | 1 | 0.01 |

The random-twin skill score, risk-adjusted return and experiment points arrive in the next build phase; they are computed from the saved trades, so they will cover these first days too.

## Requests waiting for you

- none

## Latest days

### Agent 1

- **2026-10-10** (6 steps, 2 order attempts, $0.02): Saturday 2026-10-10. Market is up modestly (20d +3%, breadth only 32% above 50d, so narrow). Screened for S1 momentum-gate names. Chose XP (Nov-13 32 call x15 at 2.77, about $4.2k, ~4% of account) and MRNA (Nov-13 220 call x1 at 32.25, about $3.2k; IV 108% makes it costly). Registered experiment S1-live-01. The order tool returned dry_run=true and no open orders are shown, so I must verify the orders on Monday and re-place if needed. Journal updated with exit plans (around 10 sessions, or cut at -50%).

### Agent 2

- **2026-10-10** (1 steps, 0 order attempts, $0.00): 2026-10-10 (Saturday, markets closed): no trades. Rule C's market gate requires the S&P 500 5-session return to be negative; the fund is +1.2% over 5 sessions, so no rule C signals are eligible. Leaders and flow lists remain dominated by extreme or thin names that don't match the setup. Staying 100% cash; journal updated with the gate status and the conditions that would bring me back.

### Agent 3

- **2026-10-10** (5 steps, 3 order attempts, $0.01): Saturday review. Market breadth is weak (32% of stocks above 50-day MA), with leadership narrow. Registered experiment E1010-3-8f2e: buy 52-week-high momentum stocks at 5% size, judged against random twins after 20 trades. Placed limit orders for P (32 sh at 156, about $5.0k) and TEAM (23 sh at 209, about $4.8k) for the 2026-10-12 session. The first TEAM order was rejected for exceeding the $5,000 experiment cap; resized to 23 shares. Stock-only, no options, given the research showing options are overpriced. Journal updated with the plan and exit rules.

## Open experiments

- agent 2 (dry run) **Rule C paper log (trend + flow block, stock long, 10 sessions)** (E1010-2-bb9b): Stocks with 20d return >= 20%, close vs ma20 <= 7.6%, close vs vwap <= 0.8%, price >= $10, dollar volume >= $14M, and no flow block, have a positive median 10-session return when the market 5d return  Expect: Median 10-session stock return above 0 and average above the all-candidate benchmark (about +0.5% median). Expect weak edge, roughly +1% median at bes. Judge by 2026-11-09.
- agent 1 (dry run) **S1-live-01** (E1010-1-6739): S1 (20d%>=20, vs ma50>=15, market 20d>0, shares>=1) buying 30-day ATM calls on live names gives positive average and beats random twins, including the wide list. Expect: Average near the scorebook (+28%), median negative (-20%ish). Win rate ~40%. Exits after 10 sessions.. Judge by 2026-11-09.
- agent 3 (dry run) **52w-high momentum stock trades, 5% size** (E1010-3-8f2e): Liquid stocks at a 52-week high with strong 3-month and 1-month momentum keep drifting up over the next 10 sessions, beating random stocks of the same size and holding time. Expect: Modest edge of about +1% over 10 sessions versus random twins; many trades will be needed to see it through noise.. Judge by 2026-11-09.
