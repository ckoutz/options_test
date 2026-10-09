# Focused test (2026-10-09 05:32 UTC)

Every stock-day with options data for bundles 1 to 6: **88,937 training** and **39,415 blind** stock-days, 545 stocks. The question: will the stock beat the average stock over the next 10 sessions (bought at the next session's close)?
Settings were chosen on the latest fifth of the training weeks only; blind months were used once, to judge. Ranges are 95%, resampling whole weeks.

Rank correlation compares the model's daily ranking of all stocks with what actually happened (0 = no skill; in professional stock selection, a steady 0.02 to 0.05 is considered valuable). Top tenth = the stocks the model liked most each day.

| columns | settings chosen | check-set rank correlation | BLIND rank correlation (range) | blind days it was positive | top tenth vs average stock, % per 10 sessions (range) | top tenth raw return % |
|---|---|---|---|---|---|---|
| Options flow (21) | 7 leaves, 100 trees | +0.001 | +0.009 (-0.016 to +0.033) | 50 of 93 | +2.67 (+0.89 to +4.65) | +4.25 |
| Technical analysis (13) | 7 leaves, 100 trees | -0.008 | +0.028 (-0.004 to +0.060) | 61 of 93 | +2.91 (+1.13 to +4.76) | +4.49 |
| Market (2) | 7 leaves, 100 trees | -0.005 | +0.015 (+0.001 to +0.031) | 54 of 93 | -0.23 (-0.87 to +0.39) | +1.35 |
| News (5) | 7 leaves, 100 trees | +0.014 | +0.018 (+0.002 to +0.033) | 58 of 93 | -0.21 (-1.15 to +0.72) | +1.36 |
| Flow + technical (34) | 7 leaves, 100 trees | +0.013 | +0.021 (-0.004 to +0.047) | 61 of 93 | +2.64 (+0.95 to +4.42) | +4.22 |
| Everything (41) | 7 leaves, 100 trees | +0.004 | +0.021 (-0.006 to +0.051) | 58 of 93 | +2.91 (+0.98 to +4.87) | +4.48 |

The average stock returned +1.58% per 10 sessions in the blind months.

## Verdict

(6 column groups were tested, so one passing narrowly could still be chance; a real signal
should pass clearly and make sense alongside the others, e.g. 'Everything' should not be worse than its parts.)

- No column group's blind ranking skill was clearly above zero (whole 95% range above zero for both
  the rank correlation and the top tenth's excess return). With this much data, that is a strong
  sign these columns don't predict which stocks beat others over 10 sessions.
