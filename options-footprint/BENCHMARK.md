# Machine learning benchmark (2026-10-09 02:25 UTC)

Training candidates: 2,998. Blind scoring candidates: 1,439. Same columns, months, costs and pick limits as the agents; nothing tuned on the blind months.
Ranges are 95%, resampling whole weeks. Every trade is $1,000.

| strategy | trades | profit $ | average % (95% range) | median % | win % | random same-trades profit $ |
|---|---|---|---|---|---|---|
| Model, stock or calls | 388 | +5,791 | +1.5 (-5.1 to +9.1) | -0.8 | 45.9 | -7,993 |
| Buy every candidate's stock | 1439 | +8,405 | +0.6 (-0.6 to +1.8) | -0.6 | 47.1 | +8,490 |
| Random picks, stock or calls | 231 | -78,532 | -34.0 (-44.9 to -22.9) | -67.2 | 25.5 | -40,310 |
| Model, calls only | 354 | -27,992 | -7.9 (-19.7 to +4.9) | -29.3 | 32.5 | -44,321 |
| Random picks, calls only | 210 | -64,936 | -30.9 (-46.7 to -12.1) | -73.4 | 24.3 | -47,187 |

- How well the model ranks stocks (predicted vs actual 10-session return, 0 = no skill): 0.04
- Model, stock or calls mostly traded: stock (251), call 30d +0% double_or_10 (32), call 30d +5% double_or_10 (21), call 14d +0% double_or_10 (13)
- Model, calls only mostly traded: call 30d +0% double_or_10 (89), call 30d +0% hold10 (43), call 90d +0% double_or_10 (38), call 14d +0% double_or_10 (33)

Read it this way: the model has an edge only if its average beats the random same-trades
picker AND the bottom of its 95% range is above that. The agents' blind runs should be compared
with the model's line for the same instruments.
