```
Storage: postgres
The raw ladder trades are archived (GitHub Release); showing the saved summary from 2026-10-08.

=== Exit rule: hold10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       +1.3   -54.3    32          -2.6   -56.4    31   26752
 14 days  +5%            +3.7   -69.5    28          -1.7   -71.3    27   27388
 14 days  +10%           +8.9   -76.3    24          +2.1   -78.8    23   26189
 14 days  +15%           +9.3   -78.3    22          +5.9   -80.6    21   24128
 14 days  +20%          +13.9   -79.3    20          +8.8   -80.9    19   21677
 30 days  at money       +3.5   -36.5    34          +2.6   -36.5    34   24021
 30 days  +5%            +5.6   -43.6    31          +3.2   -44.1    31   24830
 30 days  +10%           +8.8   -49.0    29          +6.3   -49.1    28   24251
 30 days  +15%          +17.4   -50.6    27         +10.0   -51.1    27   22942
 30 days  +20%          +21.8   -51.8    26         +11.4   -51.8    26   20959
 90 days  at money       -4.5   -19.2    34          -2.4   -16.5    35    6824
 90 days  +5%            -3.3   -19.9    34          -3.6   -17.6    34    7186
 90 days  +10%           -2.1   -21.1    33          -2.6   -19.1    34    7030
 90 days  +15%           -1.3   -21.6    33          -1.9   -19.2    34    6747
 90 days  +20%           -0.9   -23.2    33          -1.2   -20.8    34    6446

=== Exit rule: double_or_10  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       -2.6   -48.3    36          -3.0   -49.6    36   26752
 14 days  +5%            -1.4   -61.6    33          -1.8   -63.2    33   27388
 14 days  +10%           +1.5   -68.3    31          +0.5   -69.3    31   26189
 14 days  +15%           +3.7   -70.1    30          +2.8   -70.6    30   24128
 14 days  +20%           +5.6   -70.7    29          +5.5   -70.2    29   21677
 30 days  at money       -0.1   -33.9    36          +0.5   -33.7    36   24021
 30 days  +5%            +1.2   -40.5    35          +1.0   -40.6    34   24830
 30 days  +10%           +3.4   -45.2    33          +3.4   -44.8    33   24251
 30 days  +15%           +7.0   -46.2    32          +6.4   -45.8    33   22942
 30 days  +20%           +9.4   -46.8    32          +8.5   -45.8    32   20959
 90 days  at money       -4.6   -19.1    34          -3.2   -16.4    35    6824
 90 days  +5%            -3.5   -19.6    34          -3.7   -17.5    35    7186
 90 days  +10%           -2.1   -20.7    34          -3.1   -18.8    34    7030
 90 days  +15%           -1.0   -21.3    34          -2.1   -18.9    35    6747
 90 days  +20%           -0.3   -22.9    34          -1.4   -20.5    34    6446

=== Exit rule: expiry  (return %, flags vs control days on the same stocks) ===
expiry   strike    FLAG mean  median  win%  CONTROL mean  median  win%  trades
 14 days  at money       +5.1  -100.0    31          +2.3  -100.0    30   26486
 14 days  +5%            +7.4  -100.0    25          +2.3  -100.0    24   27102
 14 days  +10%          +11.5  -100.0    20          +5.9  -100.0    20   25917
 14 days  +15%          +11.8  -100.0    17          +7.8  -100.0    16   23863
 14 days  +20%          +18.0  -100.0    14         +10.0  -100.0    13   21439
 30 days  at money      +11.2  -100.0    32         +12.7  -100.0    31   23572
 30 days  +5%           +14.2  -100.0    27         +14.7  -100.0    27   24351
 30 days  +10%          +17.3  -100.0    23         +24.5  -100.0    22   23786
 30 days  +15%          +25.5  -100.0    20         +29.0  -100.0    19   22486
 30 days  +20%          +30.8  -100.0    17         +30.8  -100.0    16   20531
 90 days  at money      +60.9   -99.5    34         +59.1  -100.0    34    6143
 90 days  +5%           +64.5  -100.0    32         +63.1  -100.0    32    6479
 90 days  +10%          +66.9  -100.0    30         +64.5  -100.0    28    6330
 90 days  +15%          +72.5  -100.0    27         +71.1  -100.0    26    6049
 90 days  +20%          +79.9  -100.0    26         +74.5  -100.0    24    5777

Returns include a 5% cost on each side of the trade. Control days are non-flag days on the
same stocks. A useful pattern beats its controls by a clear margin, in the median too, since
a few huge winners can lift a mean on their own.
```
