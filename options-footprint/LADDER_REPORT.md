```
Storage: postgres
Fill rate (contract actually traded on the entry day): flag 190351/335415, control 0/0

=== Exit rule: hold10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       +0.7   -56.6    31             -       -     -   17900
 14 days  +5%            +3.7   -71.5    27             -       -     -   18345
 14 days  +10%           +9.2   -77.5    23             -       -     -   17625
 14 days  +15%          +11.9   -79.8    21             -       -     -   16334
 14 days  +20%          +15.1   -80.6    20             -       -     -   14770
 30 days  at money       +3.2   -37.9    33             -       -     -   16048
 30 days  +5%            +6.0   -45.0    31             -       -     -   16585
 30 days  +10%          +10.0   -50.1    28             -       -     -   16255
 30 days  +15%          +21.0   -51.8    27             -       -     -   15532
 30 days  +20%          +25.9   -52.5    26             -       -     -   14270
 90 days  at money       -3.6   -18.9    34             -       -     -    4690
 90 days  +5%            -2.9   -19.6    34             -       -     -    4946
 90 days  +10%           -1.7   -21.1    34             -       -     -    4824
 90 days  +15%           -0.8   -21.4    33             -       -     -    4639
 90 days  +20%           +0.0   -22.9    33             -       -     -    4440

=== Exit rule: double_or_10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       -3.7   -50.6    35             -       -     -   17900
 14 days  +5%            -2.4   -64.2    33             -       -     -   18345
 14 days  +10%           +1.5   -70.1    30             -       -     -   17625
 14 days  +15%           +4.4   -72.0    29             -       -     -   16334
 14 days  +20%           +6.7   -72.6    28             -       -     -   14770
 30 days  at money       -1.2   -35.5    35             -       -     -   16048
 30 days  +5%            +0.6   -42.1    34             -       -     -   16585
 30 days  +10%           +3.6   -46.4    32             -       -     -   16255
 30 days  +15%           +7.3   -47.6    32             -       -     -   15532
 30 days  +20%           +9.8   -48.1    31             -       -     -   14270
 90 days  at money       -4.0   -18.9    34             -       -     -    4690
 90 days  +5%            -3.1   -19.4    34             -       -     -    4946
 90 days  +10%           -1.7   -20.7    34             -       -     -    4824
 90 days  +15%           -0.5   -20.9    34             -       -     -    4639
 90 days  +20%           +0.2   -22.4    34             -       -     -    4440

=== Exit rule: expiry  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       +4.0  -100.0    30             -       -     -   17700
 14 days  +5%            +7.1  -100.0    25             -       -     -   18138
 14 days  +10%          +12.8  -100.0    20             -       -     -   17435
 14 days  +15%          +14.3  -100.0    16             -       -     -   16140
 14 days  +20%          +17.2  -100.0    14             -       -     -   14597
 30 days  at money       +9.4  -100.0    30             -       -     -   15712
 30 days  +5%           +13.6  -100.0    26             -       -     -   16231
 30 days  +10%          +17.9  -100.0    23             -       -     -   15917
 30 days  +15%          +28.8  -100.0    19             -       -     -   15192
 30 days  +20%          +32.9  -100.0    16             -       -     -   13948
 90 days  at money      +60.0  -100.0    32             -       -     -    4220
 90 days  +5%           +62.9  -100.0    30             -       -     -    4464
 90 days  +10%          +63.2  -100.0    27             -       -     -    4340
 90 days  +15%          +68.3  -100.0    25             -       -     -    4153
 90 days  +20%          +75.4  -100.0    24             -       -     -    3970

Returns include a 5% cost on each side of the trade. Control days are non-flag days on the
same stocks. A useful pattern beats its controls by a clear margin, in the median too, since
a few huge winners can lift a mean on their own.
```
