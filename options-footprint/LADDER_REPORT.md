```
Storage: postgres
Fill rate (contract actually traded on the entry day): flag 125867/281670, control 114306/281715

=== Exit rule: hold10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       -7.4   -50.8    33          -7.3   -50.7    34   15045
 14 days  +5%            -8.1   -74.7    25          -4.9   -75.7    25   14647
 14 days  +10%           -8.4   -73.8    21         -11.2   -74.9    21   11059
 14 days  +15%           -7.1   -71.3    19         -15.4   -71.6    19    7703
 14 days  +20%          -12.2   -69.8    18         -18.5   -69.8    17    5371
 30 days  at money       -5.6   -34.2    34          -4.3   -32.5    35   13584
 30 days  +5%            -2.8   -47.0    30          +0.8   -47.4    30   13814
 30 days  +10%           +1.6   -47.5    27          +2.8   -47.8    27   11121
 30 days  +15%           +5.6   -45.7    26          +4.6   -45.3    26    7962
 30 days  +20%           +7.4   -44.5    25          +2.7   -44.6    24    5603
 90 days  at money       -7.1   -15.4    36          -8.1   -15.1    35    4189
 90 days  +5%            -5.7   -18.2    36          -5.0   -17.1    35    4505
 90 days  +10%           -3.3   -20.5    35          -3.4   -18.3    35    4037
 90 days  +15%           -1.3   -21.3    33          -4.0   -19.6    33    3286
 90 days  +20%           +1.4   -17.8    32          -1.4   -17.3    32    2389

=== Exit rule: double_or_10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       -6.6   -44.0    37          -6.1   -44.3    37   15045
 14 days  +5%            -3.8   -65.3    32          -0.7   -66.1    33   14647
 14 days  +10%           -0.6   -63.9    30          +2.1   -63.4    31   11059
 14 days  +15%           +1.9   -60.6    28          +7.0   -60.2    29    7703
 14 days  +20%           +4.0   -60.7    27          +1.6   -58.9    27    5371
 30 days  at money       -5.4   -31.7    36          -4.0   -29.7    37   13584
 30 days  +5%            -0.8   -42.9    34          +1.1   -41.6    35   13814
 30 days  +10%           +4.3   -42.9    33          +7.4   -41.6    34   11121
 30 days  +15%           +7.1   -39.7    31         +11.6   -37.9    32    7962
 30 days  +20%          +12.2   -38.5    30         +11.6   -37.3    31    5603
 90 days  at money       -7.0   -15.3    36          -8.0   -15.1    36    4189
 90 days  +5%            -5.9   -17.9    36          -5.4   -17.0    36    4505
 90 days  +10%           -3.9   -20.2    35          -3.8   -17.8    35    4037
 90 days  +15%           -2.0   -20.7    34          -3.4   -18.7    33    3286
 90 days  +20%           +1.6   -17.2    33          -1.7   -16.9    32    2389

=== Exit rule: expiry  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       -8.3  -100.0    32          -9.4  -100.0    32   14912
 14 days  +5%           -14.5  -100.0    20         -12.4  -100.0    20   14501
 14 days  +10%          -25.3  -100.0    13         -26.1  -100.0    12   10945
 14 days  +15%          -31.4  -100.0     9         -40.1  -100.0     9    7605
 14 days  +20%          -43.4  -100.0     6         -50.3  -100.0     6    5311
 30 days  at money       -8.7  -100.0    32          -5.5  -100.0    32   13374
 30 days  +5%           -12.2  -100.0    22          -8.1  -100.0    22   13567
 30 days  +10%          -21.5  -100.0    15         -11.8  -100.0    15   10917
 30 days  +15%          -28.5  -100.0    11         -16.8  -100.0    12    7793
 30 days  +20%          -35.3  -100.0     8         -23.2  -100.0     8    5493
 90 days  at money      +10.0   -89.0    35          +6.4   -91.0    34    3867
 90 days  +5%            +4.3  -100.0    28         +14.0  -100.0    29    4117
 90 days  +10%           +9.4  -100.0    23         +10.9  -100.0    23    3693
 90 days  +15%           +9.3  -100.0    17         +17.8  -100.0    18    2974
 90 days  +20%          +20.5  -100.0    14          +1.8  -100.0    14    2163

Returns include a 5% cost on each side of the trade. Control days are non-flag days on the
same stocks. A useful pattern beats its controls by a clear margin, in the median too, since
a few huge winners can lift a mean on their own.
```
