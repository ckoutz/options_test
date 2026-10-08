# Machine learning benchmark (2026-10-08 22:50 UTC)

Training candidates: 2,090. Blind scoring candidates: 1,017. Same columns, months, costs and pick limits as the agents; nothing tuned on the blind months.
Ranges are 95%, resampling whole weeks. Every trade is $1,000.

| strategy | trades | profit $ | average % (95% range) | median % | win % | random same-trades profit $ |
|---|---|---|---|---|---|---|
| Model, stock or calls | 355 | -6,557 | -1.9 (-11.5 to +8.4) | -9.5 | 38.6 | -6,248 |
| Buy every candidate's stock | 1017 | +10,080 | +1.0 (-0.5 to +2.4) | -0.3 | 48.5 | +10,170 |
| Random picks, stock or calls | 230 | -23,280 | -10.1 (-25.6 to +8.2) | -33.2 | 33.0 | +1,104 |
| Model, calls only | 331 | -14,296 | -4.3 (-19.4 to +10.4) | -41.2 | 31.7 | +2,185 |
| Random picks, calls only | 225 | -16,526 | -7.3 (-22.4 to +6.2) | -40.5 | 32.9 | -11,925 |

- How well the model ranks stocks (predicted vs actual 10-session return, 0 = no skill): 0.077
- Model, stock or calls mostly traded: stock (134), call 30d +0% double_or_10 (40), call 30d +10% double_or_10 (19), call 14d +0% double_or_10 (16)
- Model, calls only mostly traded: call 30d +0% double_or_10 (120), call 14d +0% double_or_10 (35), call 30d +5% double_or_10 (24), call 30d +0% hold10 (21)

Read it this way: the model has an edge only if its average beats the random same-trades
picker AND the bottom of its 95% range is above that. The agents' blind runs should be compared
with the model's line for the same instruments.
