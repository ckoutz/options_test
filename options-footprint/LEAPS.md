# Selling long-dated covered calls after volatility spikes (2026-10-29 UTC)

- Spike entries: the first close each episode where the VIX (CBOE's own daily history) closes at or above
  ENTRY_VIX after closing under CALM_VIX within the previous 20 sessions. Episodes are at least 30 sessions apart.
- Calm control entries: dates with the VIX under CALM_VIX, spread through the same period, so we can tell
  whether the timing matters or the trade simply worked in a rising market.
- Stocks: the 120 most-traded US stocks (60-session average dollar volume) as of each entry date, excluding
  exchange-traded funds. Only stocks listed today are available (delisted ones are missing).
- The call: first expiration at least 400 days out, strike nearest to 10%, 20% or 30% above the stock's close.
  Premium = the option's closing trade on the entry day (or within the next 3 sessions), minus 5% for selling
  at the bid. Stocks that split during the hold are dropped (their contracts change).
- Outcome per share, as a % of the stock price paid: at expiration, min(stock, strike) + premium. Calls not yet
  expired are marked at today's prices: stock - (call x 1.05 to buy it back) + premium. Dividends are ignored
  for every leg (the covered-call holder and the buy-and-hold holder would both get them).
- Compared with: holding the same stock with no call, and the S&P 500 fund (SPY), over the same dates.

Spike entry dates (VIX close): 2024-08-05 (39), 2025-04-03 (30), 2026-03-06 (29)
Calm control dates: 2024-04-25, 2024-05-30, 2024-07-01, 2024-10-04, 2025-09-16, 2026-01-15

## Results (average / median, % of the stock price paid; not annualized)

| entries | strike above price | trades | premium collected | covered call | stock held, no call | S&P 500 fund | covered call beat holding the stock | finished above the strike | covered call lost money | worst |
|---|---|---|---|---|---|---|---|---|---|---|
| spike | 10% | 18 | +14.0% / +11.3% | +6.4% / +8.5% | +38.9% / +18.2% | +16.2% / +14.9% | 39% | 56% | 28% | -28% |
| spike | 20% | 14 | +10.7% / +9.8% | +8.6% / +9.8% | +55.7% / +14.0% | +16.6% / +14.9% | 43% | 43% | 29% | -30% |
| spike | 30% | 14 | +9.2% / +7.5% | +7.6% / +7.7% | +39.0% / +6.7% | +16.6% / +14.9% | 50% | 21% | 36% | -33% |
| calm | 10% | 13 | +15.6% / +8.6% | -19.8% / -20.0% | -35.3% / -36.4% | +17.3% / +18.0% | 100% | 0% | 85% | -41% |
| calm | 20% | 10 | +17.5% / +14.3% | -21.8% / -29.4% | +11.6% / -42.5% | +17.6% / +18.0% | 90% | 10% | 90% | -39% |
| calm | 30% | 11 | +10.2% / +5.9% | -33.8% / -32.2% | -43.9% / -41.9% | +17.1% / +18.0% | 100% | 0% | 100% | -45% |

## By entry date (20% above the price)

| date | kind | trades | status | premium | covered call | stock held | S&P 500 fund | days held |
|---|---|---|---|---|---|---|---|---|
| 2024-04-25 | calm | 6 | assigned, expired | +10.0% / +7.6% | -18.2% / -29.4% | +56.5% / -37.9% | +18.0% / +18.0% | 421 |
| 2025-04-03 | spike | 1 | assigned | +11.9% / +11.9% | +34.5% / +34.5% | +496.5% / +496.5% | +39.1% / +39.1% | 441 |
| 2025-09-16 | calm | 4 | open (marked today) | +28.8% / +29.1% | -27.2% / -27.8% | -55.9% / -56.6% | +17.0% / +17.0% | 407 |
| 2026-03-06 | spike | 13 | open (marked today) | +10.6% / +9.8% | +6.6% / +8.5% | +21.7% / +8.9% | +14.9% / +14.9% | 236 |

Trades where the premium was 20% or more of the stock price: 7 of 46 spike trades; covered call +5.3% / +22.0%, stock held +6.9% / +27.3%.

## Every trade

| kind | date | stock | contract | status | premium | covered call | stock held |
|---|---|---|---|---|---|---|---|
| calm | 2024-04-25 | TGT | TGT250620C00180000 | expired | 9.2% | -32.7% | -41.9% |
| calm | 2024-04-25 | NKE | NKE250620C00105000 | expired | 8.4% | -28.0% | -36.4% |
| calm | 2024-04-25 | CMI | CMI250620C00320000 | expired | 7.7% | +15.5% | +7.8% |
| calm | 2024-04-25 | COP | COP250620C00145000 | expired | 7.3% | -20.0% | -27.2% |
| calm | 2024-04-25 | UPS | UPS250620C00160000 | expired | 6.5% | -26.1% | -32.6% |
| calm | 2024-04-25 | LIN | LIN250620C00490000 | expired | 6.4% | +9.1% | +2.7% |
| calm | 2024-04-25 | MRK | MRK250620C00145000 | expired | 4.6% | -34.9% | -39.5% |
| calm | 2024-04-25 | MDB | MDB250620C00440000 | expired | 19.7% | -25.3% | -45.0% |
| calm | 2024-04-25 | PLTR | PLTR250620C00027000 | assigned | 18.1% | +42.5% | +532.4% |
| calm | 2024-04-25 | INTC | INTC250620C00042000 | expired | 9.9% | -30.1% | -40.0% |
| calm | 2024-04-25 | NKE | NKE250620C00115000 | expired | 5.4% | -31.0% | -36.4% |
| calm | 2024-04-25 | UPS | UPS250620C00175000 | expired | 4.0% | -28.7% | -32.6% |
| calm | 2024-04-25 | MRK | MRK250620C00155000 | expired | 3.0% | -36.5% | -39.5% |
| calm | 2024-04-25 | INTC | INTC250620C00045000 | expired | 7.8% | -32.2% | -40.0% |
| calm | 2024-04-25 | NKE | NKE250620C00120000 | expired | 4.7% | -31.6% | -36.4% |
| calm | 2024-04-25 | TGT | TGT250620C00210000 | expired | 3.6% | -38.3% | -41.9% |
| calm | 2024-04-25 | COP | COP250620C00170000 | expired | 2.4% | -24.8% | -27.2% |
| calm | 2024-04-25 | UPS | UPS250620C00190000 | expired | 2.4% | -30.3% | -32.6% |
| calm | 2024-10-04 | REGN | REGN251219C01120000 | expired | 8.6% | -15.5% | -24.2% |
| calm | 2024-10-04 | UNH | UNH251219C00760000 | expired | 3.3% | -41.3% | -44.6% |
| spike | 2025-04-03 | LRCX | LRCX260618C00070000 | assigned | 12.9% | +20.3% | +496.5% |
| spike | 2025-04-03 | LRCX | LRCX260618C00080000 | assigned | 11.9% | +34.5% | +496.5% |
| spike | 2025-04-03 | LRCX | LRCX260618C00085000 | assigned | 10.3% | +40.7% | +496.5% |
| calm | 2025-09-16 | BMNR | BMNR270115C00060000 | open (marked today) | 48.3% | -12.6% | -60.6% |
| calm | 2025-09-16 | SBET | SBET270115C00018000 | open (marked today) | 40.7% | -16.5% | -56.6% |
| calm | 2025-09-16 | MSTR | MSTR261218C00370000 | open (marked today) | 22.5% | -34.2% | -56.7% |
| calm | 2025-09-16 | RBLX | RBLX261218C00150000 | open (marked today) | 20.0% | -41.0% | -60.8% |
| calm | 2025-09-16 | BMNR | BMNR270115C00065000 | open (marked today) | 46.7% | -14.0% | -60.6% |
| calm | 2025-09-16 | SBET | SBET270115C00020000 | open (marked today) | 38.1% | -18.8% | -56.6% |
| calm | 2025-09-16 | MSTR | MSTR261218C00400000 | open (marked today) | 20.0% | -36.7% | -56.7% |
| calm | 2025-09-16 | INTU | INTU261218C00780000 | open (marked today) | 10.5% | -39.3% | -49.6% |
| calm | 2025-09-16 | BMNR | BMNR270115C00075000 | open (marked today) | 42.8% | -18.0% | -60.6% |
| calm | 2025-09-16 | MSTR | MSTR261218C00440000 | open (marked today) | 17.1% | -39.6% | -56.7% |
| calm | 2025-09-16 | RBLX | RBLX261218C00175000 | open (marked today) | 16.0% | -45.0% | -60.8% |
| calm | 2025-09-16 | INTU | INTU261218C00840000 | open (marked today) | 6.1% | -43.7% | -49.6% |
| calm | 2026-01-15 | BA | BA270219C00275000 | open (marked today) | 12.7% | -20.0% | -32.5% |
| calm | 2026-01-15 | BA | BA270219C00320000 | open (marked today) | 5.9% | -26.7% | -32.5% |
| spike | 2026-03-06 | STX | STX270617C00390000 | open (marked today) | 31.5% | +32.6% | +97.8% |
| spike | 2026-03-06 | APP | APP270617C00550000 | open (marked today) | 31.2% | -18.7% | -48.2% |
| spike | 2026-03-06 | LRCX | LRCX270617C00220000 | open (marked today) | 29.9% | +25.5% | +27.3% |
| spike | 2026-03-06 | ANET | ANET270617C00145000 | open (marked today) | 23.2% | +22.4% | +40.5% |
| spike | 2026-03-06 | UBER | UBER270617C00082500 | open (marked today) | 14.9% | -2.9% | -13.1% |
| spike | 2026-03-06 | BSX | BSX270617C00080000 | open (marked today) | 13.2% | -27.9% | -40.5% |
| spike | 2026-03-06 | ADI | ADI270617C00350000 | open (marked today) | 12.4% | +12.9% | +35.6% |
| spike | 2026-03-06 | UNH | UNH270617C00320000 | open (marked today) | 11.9% | +18.5% | +42.1% |
| spike | 2026-03-06 | WMT | WMT270617C00135000 | open (marked today) | 10.6% | +1.2% | -4.1% |
| spike | 2026-03-06 | BAC | BAC270416C00052500 | open (marked today) | 8.9% | +6.3% | +4.5% |
| spike | 2026-03-06 | JPM | JPM270617C00320000 | open (marked today) | 8.3% | +10.5% | +17.2% |
| spike | 2026-03-06 | SCHW | SCHW270617C00105000 | open (marked today) | 8.2% | -1.7% | -6.8% |
| spike | 2026-03-06 | PM | PM270617C00185000 | open (marked today) | 8.0% | +6.9% | +19.2% |
| spike | 2026-03-06 | CVX | CVX270617C00210000 | open (marked today) | 7.8% | +10.9% | +20.7% |
| spike | 2026-03-06 | V | V270617C00350000 | open (marked today) | 7.8% | +9.4% | +26.2% |
| spike | 2026-03-06 | PFE | PFE270617C00030000 | open (marked today) | 6.6% | +7.6% | +8.9% |
| spike | 2026-03-06 | MCD | MCD270617C00360000 | open (marked today) | 5.4% | -18.5% | -23.6% |
| spike | 2026-03-06 | APP | APP270617C00600000 | open (marked today) | 27.4% | -22.0% | -48.2% |
| spike | 2026-03-06 | LRCX | LRCX270617C00240000 | open (marked today) | 21.1% | +22.0% | +27.3% |
| spike | 2026-03-06 | DELL | DELL270617C00175000 | open (marked today) | 14.9% | +45.0% | +237.1% |
| spike | 2026-03-06 | BSX | BSX270617C00085000 | open (marked today) | 10.7% | -30.3% | -40.5% |
| spike | 2026-03-06 | ADI | ADI270617C00380000 | open (marked today) | 10.2% | +18.1% | +35.6% |
| spike | 2026-03-06 | UBER | UBER270617C00090000 | open (marked today) | 9.9% | -6.3% | -13.1% |
| spike | 2026-03-06 | UNH | UNH270617C00340000 | open (marked today) | 9.8% | +21.2% | +42.1% |
| spike | 2026-03-06 | WMT | WMT270617C00150000 | open (marked today) | 7.2% | +0.6% | -4.1% |
| spike | 2026-03-06 | PM | PM270617C00200000 | open (marked today) | 6.0% | +11.1% | +19.2% |
| spike | 2026-03-06 | BAC | BAC270416C00057500 | open (marked today) | 5.5% | +6.7% | +4.5% |
| spike | 2026-03-06 | SCHW | SCHW270617C00115000 | open (marked today) | 5.3% | -3.0% | -6.8% |
| spike | 2026-03-06 | CVX | CVX270617C00230000 | open (marked today) | 5.0% | +14.1% | +20.7% |
| spike | 2026-03-06 | PFE | PFE270617C00032000 | open (marked today) | 4.8% | +8.5% | +8.9% |
| spike | 2026-03-06 | APP | APP270617C00650000 | open (marked today) | 24.5% | -24.7% | -48.2% |
| spike | 2026-03-06 | LRCX | LRCX270617C00260000 | open (marked today) | 19.1% | +24.9% | +27.3% |
| spike | 2026-03-06 | ANET | ANET270617C00175000 | open (marked today) | 17.4% | +29.3% | +40.5% |
| spike | 2026-03-06 | NVO | NVO270617C00050000 | open (marked today) | 11.6% | +6.8% | -0.8% |
| spike | 2026-03-06 | UBER | UBER270617C00100000 | open (marked today) | 8.8% | -6.0% | -13.1% |
| spike | 2026-03-06 | BSX | BSX270617C00092500 | open (marked today) | 7.7% | -33.2% | -40.5% |
| spike | 2026-03-06 | UNH | UNH270617C00370000 | open (marked today) | 7.4% | +26.1% | +42.1% |
| spike | 2026-03-06 | WMT | WMT270617C00160000 | open (marked today) | 5.3% | -0.3% | -4.1% |
| spike | 2026-03-06 | SCHW | SCHW270617C00125000 | open (marked today) | 4.2% | -3.5% | -6.8% |
| spike | 2026-03-06 | PM | PM270617C00220000 | open (marked today) | 3.4% | +14.0% | +19.2% |
| spike | 2026-03-06 | BAC | BAC270416C00062500 | open (marked today) | 3.4% | +6.6% | +4.5% |
| spike | 2026-03-06 | CVX | CVX270617C00250000 | open (marked today) | 3.4% | +16.6% | +20.7% |
| spike | 2026-03-06 | PFE | PFE270617C00035000 | open (marked today) | 2.4% | +8.6% | +8.9% |
