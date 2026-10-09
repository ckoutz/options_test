# Open interest test (2026-10-09 01:03 UTC)

134 stocks with Databento open interest; 1,010 candidate days with it. Open interest after the candidate day versus 5 and 20 sessions earlier (new positions opened). Each row splits candidate days into fifths by that measure and shows the top fifth against all days: the stock's next-10-session return and a 30-day at-the-money call held 10 sessions (realistic costs). Ranges are 95%, resampling whole weeks.

## Training months (690 days)

| measure | top fifth threshold | stock: top fifth % (range) | stock: all % | call: top fifth % | call: all % | days |
|---|---|---|---|---|---|---|
| call_oi_chg5 | 17.15 | +2.85 (-1.4 to +8.0) | +1.57 | -7.8 | -2.3 | 131 |
| call_oi_otm_chg5 | 29.65 | +3.88 (-0.7 to +8.4) | +1.57 | +22.4 | -2.3 | 131 |
| call_oi_long_chg5 | 16.76 | +2.78 (-0.8 to +6.8) | +1.57 | +7.2 | -2.3 | 131 |
| call_oi_short_chg5 | 97.48 | +2.37 (-3.9 to +11.1) | +0.80 | +4.0 | -4.8 | 81 |
| put_oi_chg5 | 14.66 | +2.22 (-2.2 to +7.8) | +1.57 | -3.3 | -2.3 | 131 |
| call_oi_chg20 | 36.11 | +3.24 (+0.2 to +6.4) | +1.12 | -26.0 | -6.4 | 134 |
| call_oi_otm_chg20 | 54.76 | +2.60 (-0.5 to +5.8) | +1.12 | -16.3 | -6.4 | 134 |
| call_oi_long_chg20 | 45.96 | +2.76 (-0.1 to +5.5) | +1.12 | -7.2 | -6.4 | 134 |
| call_oi_short_chg20 | 203.33 | +7.28 (+2.2 to +14.0) | +1.70 | +23.9 | -2.4 | 101 |
| put_oi_chg20 | 36.05 | +0.61 (-2.8 to +4.2) | +1.12 | -28.1 | -6.4 | 134 |
| put_call_oi | 0.87 | +0.65 (-3.0 to +5.4) | +1.47 | -8.8 | -2.8 | 138 |

## Blind months (never used to choose anything) (320 days)

| measure | top fifth threshold | stock: top fifth % (range) | stock: all % | call: top fifth % | call: all % | days |
|---|---|---|---|---|---|---|
| call_oi_chg5 | 21.03 | -0.50 (-5.3 to +4.7) | +0.40 | -16.3 | -6.7 | 63 |
| call_oi_otm_chg5 | 32.14 | +2.53 (-1.9 to +9.3) | +0.40 | -12.4 | -6.7 | 63 |
| call_oi_long_chg5 | 17.56 | +1.19 (-3.3 to +6.3) | +0.40 | -9.2 | -6.7 | 63 |
| call_oi_short_chg5 | 98.57 | -3.59 (-8.2 to +1.2) | -1.08 | -61.9 | -19.4 | 36 |
| put_oi_chg5 | 21.83 | -2.17 (-6.0 to +1.9) | +0.40 | -13.2 | -6.7 | 63 |
| call_oi_chg20 | 36.02 | -1.95 (-6.3 to +2.8) | +0.30 | -38.9 | -11.3 | 62 |
| call_oi_otm_chg20 | 51.84 | -1.41 (-5.9 to +3.6) | +0.30 | -34.2 | -11.3 | 62 |
| call_oi_long_chg20 | 44.03 | +0.35 (-4.4 to +6.0) | +0.30 | -24.8 | -11.3 | 62 |
| call_oi_short_chg20 | 236.36 | +0.32 (-5.0 to +6.0) | -0.44 | -33.2 | -13.5 | 52 |
| put_oi_chg20 | 35.17 | -1.14 (-4.3 to +2.1) | +0.30 | -26.0 | -11.3 | 62 |
| put_call_oi | 0.82 | +3.37 (+0.3 to +6.2) | +0.41 | +11.0 | -6.8 | 64 |

Read it this way: a measure matters only if its top fifth beats 'all' in the training months AND
again in the blind months, with the range clear of the 'all' figure. Many measures are tested here, so
one or two will look good by chance.
