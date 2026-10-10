# Playoff (2026-10-10 20:41 UTC)

Finalists: the agents (from every lineage) whose best rule held up best when code tested it on all
training months. Each then traded the blind months with only its own final notes and rules, stock or
calls allowed. Judged on the **wide list** (chosen January 2024, no hindsight): average return per trade
minus the same kind of trade on random wide-list candidates in the same weeks, 95% range by week.

| finalist | best training rule (edge) | blind trades | WIDE: trades, agent vs random % | WIDE excess (range) | big movers: agent vs random % | cost $ |
|---|---|---|---|---|---|---|
| gen10 gen 9 agent1 | Tail tracker R1 strict (+22.01) | 45 | 27: -19.00 vs -14.02 | -4.98 (-12.55 to +1.58) | -4.98 vs -2.89 (18) | 0.3339 |
| gen10b gen 10 agent3 | trend and flow, 30d call (+17.67) | 19 | 8: -2.09 vs -1.59 | -0.51 (-3.10 to +3.21) | +3.82 vs -0.10 (11) | 0.3287 |
| gen10 gen 5 agent1 | overbought heavy calls, weak prior (+14.17) | 0 | - | - | - | 0.2268 |
| gen10 gen 7 agent4 | R1 gate 30d 5pct hold10 (+13.19) | 143 | 46: -22.90 vs -25.34 | +2.44 (-21.29 to +31.07) | -25.22 vs -13.67 (97) | 0.3095 |
| gen10b gen 9 agent2 | R2 gate, calls 30d ATM (+12.24) | 91 | 15: -1.03 vs -0.14 | -0.89 (-4.72 to +2.72) | -2.15 vs -0.58 (76) | 0.3053 |

## Verdict

- Nobody beat random on the wide list clearly. Best showing: gen10 gen 7 agent4 (+2.44% per trade versus random, range crossing zero). Treat that as luck;
  choose paper account 2 for the most interesting strategy rather than this result.
- 5 finalists were tested, so one passing narrowly could still be chance.
