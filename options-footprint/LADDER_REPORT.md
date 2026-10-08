```
Storage: postgres
Fill rate (contract actually traded on the entry day): flag 188228/331110, control 0/0

=== Exit rule: hold10  (mean return %, win rate %; flags vs random control days) ===
expiry  strike     flag mean   win  control mean   win  trades
 14 days  ATM             +0.8    31          +nan   nan   17680
 14 days  +5%             +3.7    27          +nan   nan   18133
 14 days  +10%            +9.2    23          +nan   nan   17421
 14 days  +15%           +11.6    21          +nan   nan   16126
 14 days  +20%           +15.2    20          +nan   nan   14579
 30 days  ATM             +3.3    33          +nan   nan   15874
 30 days  +5%             +6.1    31          +nan   nan   16419
 30 days  +10%           +10.1    28          +nan   nan   16084
 30 days  +15%           +21.2    27          +nan   nan   15357
 30 days  +20%           +26.0    26          +nan   nan   14103
 90 days  ATM             -3.4    34          +nan   nan    4653
 90 days  +5%             -2.7    34          +nan   nan    4907
 90 days  +10%            -1.6    34          +nan   nan    4787
 90 days  +15%            -0.6    33          +nan   nan    4599
 90 days  +20%            +0.2    33          +nan   nan    4403

=== Exit rule: double_or_10  (mean return %, win rate %; flags vs random control days) ===
expiry  strike     flag mean   win  control mean   win  trades
 14 days  ATM             -3.5    35          +nan   nan   17680
 14 days  +5%             -2.3    33          +nan   nan   18133
 14 days  +10%            +1.7    30          +nan   nan   17421
 14 days  +15%            +4.7    29          +nan   nan   16126
 14 days  +20%            +6.8    28          +nan   nan   14579
 30 days  ATM             -1.1    35          +nan   nan   15874
 30 days  +5%             +0.7    34          +nan   nan   16419
 30 days  +10%            +3.8    32          +nan   nan   16084
 30 days  +15%            +7.5    32          +nan   nan   15357
 30 days  +20%           +10.0    31          +nan   nan   14103
 90 days  ATM             -3.9    35          +nan   nan    4653
 90 days  +5%             -3.0    34          +nan   nan    4907
 90 days  +10%            -1.5    34          +nan   nan    4787
 90 days  +15%            -0.4    34          +nan   nan    4599
 90 days  +20%            +0.4    34          +nan   nan    4403

=== Exit rule: expiry  (mean return %, win rate %; flags vs random control days) ===
expiry  strike     flag mean   win  control mean   win  trades
 14 days  ATM             +4.3    30          +nan   nan   17487
 14 days  +5%             +7.2    25          +nan   nan   17933
 14 days  +10%           +12.9    20          +nan   nan   17238
 14 days  +15%           +14.3    16          +nan   nan   15939
 14 days  +20%           +17.6    14          +nan   nan   14413
 30 days  ATM             +9.8    31          +nan   nan   15548
 30 days  +5%            +14.0    27          +nan   nan   16075
 30 days  +10%           +18.2    23          +nan   nan   15757
 30 days  +15%           +29.2    19          +nan   nan   15028
 30 days  +20%           +33.1    16          +nan   nan   13792
 90 days  ATM            +60.5    32          +nan   nan    4188
 90 days  +5%            +63.3    30          +nan   nan    4429
 90 days  +10%           +63.9    27          +nan   nan    4306
 90 days  +15%           +69.0    25          +nan   nan    4117
 90 days  +20%           +76.2    24          +nan   nan    3937

Mean returns include a 5% cost on each side of the trade. A useful pattern beats the
control days by a clear margin, not just zero; buying calls on random days usually loses.
```
