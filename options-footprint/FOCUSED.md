# Focused test (2026-10-09 13:42 UTC)

Every stock-day with options data for bundles 1 to 6: **88,937 training** and **39,415 blind** stock-days, 545 stocks. The question: will the stock beat the average stock over the next 10 sessions (bought at the next session's close)?
Settings were chosen on the latest fifth of the training weeks only; blind months were used once, to judge. Ranges are 95%, resampling whole weeks.

Rank correlation compares the model's daily ranking of all stocks with what actually happened (0 = no skill; in professional stock selection, a steady 0.02 to 0.05 is considered valuable). Top tenth = the stocks the model liked most each day.

| columns | settings chosen | check-set rank correlation | BLIND rank correlation (range) | blind days it was positive | top tenth vs average stock, % per 10 sessions (range) | top tenth raw return % |
|---|---|---|---|---|---|---|
| Options flow (21) | 7 leaves, 100 trees | +0.001 | +0.009 (-0.016 to +0.033) | 50 of 93 | +2.67 (+0.89 to +4.65) | +4.25 |
| Technical analysis (13) | 7 leaves, 100 trees | -0.007 | +0.028 (-0.004 to +0.060) | 61 of 93 | +2.91 (+1.13 to +4.76) | +4.49 |
| Market (2) | 7 leaves, 100 trees | -0.005 | +0.015 (+0.001 to +0.031) | 54 of 93 | -0.23 (-0.87 to +0.39) | +1.35 |
| News (5) | 7 leaves, 100 trees | +0.011 | +0.017 (+0.000 to +0.034) | 61 of 93 | -0.21 (-1.15 to +0.72) | +1.36 |
| Flow + technical (34) | 7 leaves, 100 trees | +0.013 | +0.021 (-0.003 to +0.047) | 61 of 93 | +2.64 (+0.95 to +4.42) | +4.22 |
| Everything (41) | 7 leaves, 100 trees | +0.004 | +0.021 (-0.006 to +0.051) | 58 of 93 | +2.91 (+0.98 to +4.87) | +4.48 |

The average stock returned +1.58% per 10 sessions in the blind months.

## Verdict

(6 column groups were tested, so one passing narrowly could still be chance; a real signal
should pass clearly and make sense alongside the others, e.g. 'Everything' should not be worse than its parts.)

- No column group's blind ranking skill was clearly above zero (whole 95% range above zero for both
  the rank correlation and the top tenth's excess return). With this much data, that is a strong
  sign these columns don't predict which stocks beat others over 10 sessions.

## Is it just volatility?

A model can beat the average stock in a rising market just by picking jumpy stocks. Three checks:

1. **Volatility only:** each day, buy the tenth of stocks with the highest 20-day volatility. No model.
2. **Same-volatility yardstick:** compare each pick with the average stock of the *same* volatility (same tenth by 20-day volatility, same day). Picking jumpy stocks earns nothing here.
3. **Market-sensitivity yardstick:** subtract what the stock's market sensitivity (beta, from the previous 60 sessions) predicts from the market's move over the same 10 sessions.

| top tenth chosen by | its 20-day volatility, % a day (all stocks) | its beta | vs average stock | vs same-volatility stocks | after market sensitivity |
|---|---|---|---|---|---|
| Volatility only (no model) | 19.16 (4.76) | 2.15 | +3.01 (+0.71 to +5.42) | +0.00 (-0.00 to +0.00) | +2.85 (+0.47 to +5.49) |
| Options flow | 9.66 (4.76) | 1.67 | +2.67 (+0.89 to +4.65) | +2.10 (+0.63 to +3.85) | +2.52 (+0.74 to +4.61) |
| Technical analysis | 11.34 (4.76) | 1.87 | +2.91 (+1.13 to +4.76) | +1.55 (+0.30 to +2.83) | +2.83 (+1.04 to +4.70) |
| Market | 3.97 (4.76) | 1.76 | -0.23 (-0.87 to +0.39) | -0.38 (-1.01 to +0.17) | -0.33 (-0.90 to +0.18) |
| News | 4.02 (4.76) | 1.73 | -0.21 (-1.15 to +0.72) | -0.36 (-1.20 to +0.52) | -0.27 (-1.18 to +0.63) |
| Flow + technical | 9.25 (4.76) | 1.87 | +2.64 (+0.95 to +4.42) | +1.49 (+0.18 to +2.78) | +2.52 (+0.79 to +4.32) |
| Everything | 8.49 (4.76) | 1.89 | +2.91 (+0.98 to +4.87) | +1.67 (+0.20 to +3.13) | +2.79 (+0.85 to +4.81) |

All figures are % per 10 sessions, with 95% ranges resampling whole weeks.

### Retrained to ignore volatility

The same models trained on the same-volatility yardstick, so they get no credit for picking jumpy stocks and have to find something else. Same settings as above.

| columns | BLIND rank correlation (range) | blind days positive | top tenth vs same-volatility stocks (range) |
|---|---|---|---|
| Options flow | +0.039 (+0.019 to +0.061) | 62 of 93 | +1.25 (+0.36 to +2.23) |
| Technical analysis | +0.075 (+0.049 to +0.102) | 77 of 93 | +2.00 (+0.62 to +3.31) |
| Flow + technical | +0.071 (+0.051 to +0.091) | 82 of 93 | +1.80 (+0.53 to +3.01) |
| Everything | +0.074 (+0.053 to +0.096) | 78 of 93 | +2.43 (+0.97 to +4.06) |

### What this means

- Buying the most volatile tenth with no model beat the average stock by +3.01% per 10 sessions.
- After removing volatility, Options flow, Technical analysis, Flow + technical, Everything still ranked stocks better than chance with the whole range above zero. That leftover is a real lead worth testing with options.
