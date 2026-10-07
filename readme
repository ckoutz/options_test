# Options footprint dataset

Goal: find out whether a collapse in the put/call ratio (calls swamping puts) shows up
before big stock moves often enough to trade on, and how often it fires with no move.

All data comes from Alpaca, free with your existing keys (paper keys work).
Options history starts February 2024. No Alpha Vantage needed once `compare` checks out.

## Setup (GitHub, runs in the cloud, nothing to install)
1. Create a new **private** repository on GitHub and upload everything in this folder,
   including the hidden `.github` folder.
2. In the repository: Settings → Secrets and variables → Actions → New repository secret.
   Add `ALPACA_KEY_ID` and `ALPACA_SECRET_KEY`.
3. Actions tab → "Options footprint" → Run workflow → choose `compare`.
   The log prints Alpaca's Wolfspeed put/call next to Alpha Vantage's. An average
   difference under about 0.05 means Alpaca is good enough.
4. Run workflow again → choose `backfill` (seeds every 15%+ move since March 2024; can take a while).
5. From then on it runs `nightly` by itself every weekday after the close and commits
   the updated CSVs back to the repository.

## Running it by hand instead (any terminal with Python 3)
```
export ALPACA_KEY_ID=...  ALPACA_SECRET_KEY=...
python collector.py compare --ticker WOLF
python collector.py nightly
```
`nightly` seeds any 15%+ movers from the past week, fills their 15-day pre-move windows,
adds control days, and recomputes features.

## Files
- `data/events.csv` – big moves (ticker, date, size, catalyst, label)
- `data/daily_features.csv` – per ticker per day: put/call, call and put volume,
  short-dated out-of-the-money call volume, close, share volume
- `data/controls.csv` – random quiet days for the same tickers
- `data/event_features.csv` – one row per event or control with the signals
- `data/cache/` – raw Alpaca responses, so reruns cost nothing

## Signals per event
- `put_call_drop_ratio` – typical put/call versus the low in the last 3 sessions
- `window_put_call_min`, `sessions_from_low_to_event` – lowest point in the 15 sessions and how early it came
- `call_volume_recent_vs_baseline` – call volume spike
- `short_otm_call_recent_max`, `short_otm_call_recent_vs_baseline` – calls expiring within
  2 weeks with strikes 5%+ above the price (the cheap lottery tickets informed money tends to buy)
- `stock_volume_last_vs_avg`, `price_change_in_window_pct`, `max_daily_abs_move_pct` – was the stock quiet

## Labels
`news_catalyst`, `sector_day` (3+ universe names moved together that day), `unknown`, `control`.
After-hours moves can't be seen in daily bars, so add those by hand as `after_hours` events.

## Limits
- No historical open interest from Alpaca, so "volume above open interest" needs another source later.
- Universe is 40 volatile names in `UNIVERSE` at the top of the script. Widen it as needed.
