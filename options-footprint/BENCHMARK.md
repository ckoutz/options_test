# Machine learning benchmark (2026-10-09 04:56 UTC)

Training candidates: 2,998. Blind scoring candidates: 1,439. Same columns, months, costs and pick limits as the agents; nothing tuned on the blind months.
Ranges are 95%, resampling whole weeks. Every trade is $1,000.

| strategy | trades | profit $ | average % (95% range) | median % | win % | random same-trades profit $ |
|---|---|---|---|---|---|---|
| Model, stock or calls | 401 | -17,443 | -4.3 (-9.1 to -0.3) | -1.4 | 43.6 | -8,541 |
| Buy every candidate's stock | 1439 | +8,405 | +0.6 (-0.6 to +1.8) | -0.6 | 47.1 | +7,771 |
| Random picks, stock or calls | 235 | -71,284 | -30.3 (-41.8 to -17.9) | -60.4 | 26.8 | -42,206 |
| Model, calls only | 342 | -28,309 | -8.3 (-20.0 to +5.0) | -27.6 | 33.9 | -37,073 |
| Random picks, calls only | 215 | -62,168 | -28.9 (-44.0 to -10.4) | -70.1 | 25.1 | -46,827 |

- How well the model ranks stocks (predicted vs actual 10-session return, 0 = no skill): 0.004
- Model, stock or calls mostly traded: stock (307), call 30d +0% double_or_10 (16), call 30d +5% double_or_10 (12), call 14d +0% double_or_10 (11)
- Model, calls only mostly traded: call 30d +0% double_or_10 (85), call 90d +0% double_or_10 (41), call 30d +0% hold10 (38), call 14d +0% double_or_10 (28)

Read it this way: the model has an edge only if its average beats the random same-trades
picker AND the bottom of its 95% range is above that. The agents' blind runs should be compared
with the model's line for the same instruments.
