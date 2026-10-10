# Model bake-off (2026-10-10 07:34 UTC)

Every model traded the same blind scoring months with the same notes (gen10, generation 5's editor notes and scorebook), the same candidates and the same rules (calls only). One run each, so the money results are noisy; the
reliability columns (unreadable replies, replies cut off) are the most dependable comparison.

| model | price per million tokens (in / out) | replies unreadable | cut off | cost $ | trades | average % | random same trades % | WIDE list: agent vs random % (range of the difference) | rating correlation |
|---|---|---|---|---|---|---|---|---|---|
| anthropic/claude-haiku-5.5 (from the lineage's own run) | see OpenRouter | 9/144 | 17 | 1.0433 | 290 | -17.48 | -24.4 | -22.6 vs -28.7 (+6.0; -6.2 to +18.8) | -0.066 |
| deepseek/deepseek-v4-pro | $0.95 / $1.90 | 0/144 | 0 | 1.6865 | 178 | -29.6 | -22.61 | -37.4 vs -29.7 (-7.7; -23.8 to +6.7) | -0.009 |
| moonshotai/kimi-k2.6 (too slow: not finished in 35 minutes) | $0.46 / $2.45 | | | | | | | | |
| z-ai/glm-5.2 | $0.06 / $7.00 | 6/144 | 12 | 3.1638 | 272 | -22.28 | -21.73 | -21.8 vs -29.7 (+7.9; -3.3 to +20.0) | -0.045 |
