```
Storage: postgres
Fill rate (contract actually traded on the entry day): flag 8606/20385, control 7743/20385

=== Exit rule: hold10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money      -18.4   -56.5    32         -13.2   -53.0    33    1039
 14 days  +5%           -28.1   -80.2    24          -8.1   -81.9    22    1023
 14 days  +10%          -32.0   -81.9    16         -14.7   -79.9    19     814
 14 days  +15%          -37.6   -82.1    15         -25.5   -77.4    17     558
 14 days  +20%          -41.9   -84.7    14         -37.6   -80.1    16     374
 30 days  at money      -14.7   -33.5    34          -8.8   -31.7    34     909
 30 days  +5%           -13.0   -47.8    30          -3.7   -48.1    28     937
 30 days  +10%          -14.5   -49.2    24          -7.5   -45.6    26     787
 30 days  +15%          -12.6   -48.1    21          -1.5   -45.7    26     569
 30 days  +20%          -19.0   -48.2    20         -16.8   -48.7    23     400
 90 days  at money      -11.3   -18.0    33          -6.5   -17.3    33     237
 90 days  +5%            -4.1   -16.4    37          -5.4   -21.5    33     267
 90 days  +10%           -7.3   -19.1    33          -9.5   -23.4    28     238
 90 days  +15%           -6.2   -24.6    29          -7.0   -23.6    30     201
 90 days  +20%          -13.8   -24.4    28          -8.7   -21.9    31     156

=== Exit rule: double_or_10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money      -10.8   -48.9    36          -5.4   -40.8    38    1039
 14 days  +5%           -14.9   -70.3    31          +1.3   -70.2    32    1023
 14 days  +10%          -18.9   -69.8    26          +6.4   -65.7    31     814
 14 days  +15%          -21.6   -68.1    24          +3.3   -62.3    30     558
 14 days  +20%          -22.4   -75.5    22         -13.1   -66.4    26     374
 30 days  at money      -10.6   -30.6    36          -3.1   -24.6    37     909
 30 days  +5%            -6.5   -42.6    33          +2.4   -38.6    34     937
 30 days  +10%           -6.0   -44.3    30         +10.5   -38.2    34     787
 30 days  +15%          -10.4   -43.5    26          +8.8   -37.7    32     569
 30 days  +20%           -4.5   -45.1    25          -7.8   -42.4    29     400
 90 days  at money       -9.5   -17.4    34          -6.8   -17.3    33     237
 90 days  +5%            -3.3   -15.4    38          -6.9   -21.5    33     267
 90 days  +10%           -3.0   -18.6    34          -9.3   -23.4    28     238
 90 days  +15%           -8.1   -24.1    29          -7.0   -23.6    30     201
 90 days  +20%          -11.2   -24.4    28          -8.1   -21.9    31     156

=== Exit rule: expiry  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money      -21.6  -100.0    29         -19.5  -100.0    31    1030
 14 days  +5%           -37.4  -100.0    18         -22.5  -100.0    18    1013
 14 days  +10%          -52.3  -100.0     8         -44.5  -100.0    10     801
 14 days  +15%          -82.5  -100.0     4         -63.9  -100.0     6     548
 14 days  +20%          -84.6  -100.0     3         -76.9  -100.0     5     369
 30 days  at money      -23.3  -100.0    28         -22.7  -100.0    30     897
 30 days  +5%           -27.8  -100.0    20         -32.0  -100.0    18     922
 30 days  +10%          -44.8  -100.0    13         -57.3  -100.0    11     768
 30 days  +15%          -65.1  -100.0     6         -62.6  -100.0     8     555
 30 days  +20%          -75.9  -100.0     4         -79.7  -100.0     6     392
 90 days  at money      -16.4  -100.0    28         -19.5  -100.0    30     218
 90 days  +5%           -28.8  -100.0    22         -20.6  -100.0    24     241
 90 days  +10%          -29.3  -100.0    16         -29.0  -100.0    19     216
 90 days  +15%           +1.7  -100.0    16         -19.4  -100.0    17     178
 90 days  +20%          -53.5  -100.0    12         -61.3  -100.0    11     141

Returns include a 5% cost on each side of the trade. Control days are non-flag days on the
same stocks. A useful pattern beats its controls by a clear margin, in the median too, since
a few huge winners can lift a mean on their own.
```
