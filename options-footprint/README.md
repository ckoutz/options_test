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
4. Run workflow again → choose `backfill`. It finds every 15%+ move since March 2024, pulls the
   full daily options history for tickers with 3+ events (one pass per ticker instead of one per
   event), fills the rest event by event, and adds control days. Each run works for about 100
   minutes; if it isn't finished, it launches the next round by itself (up to 20 rounds).
   `data/history_done.csv` shows which tickers have full history; `data/errors.csv` lists anything skipped.
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
- `call_vol_short_spike`, `call_vol_medium_spike`, `call_vol_long_spike` – call buying by time to
  expiration (2 weeks or less, 15 to 60 days, over 60 days), recent peak versus baseline
- `call_vol_otm_spike`, `call_vol_atm_spike`, `call_vol_itm_spike` – call buying by strike: out of
  the money (5%+ above the price), near the money (within 5%), in the money (5%+ below)
- `stock_volume_last_vs_avg`, `price_change_in_window_pct`, `max_daily_abs_move_pct` – was the stock quiet

Wolfspeed, late September 2026: the early buying was NOT short-dated out-of-the-money calls; those
only spiked after the stock had already run, from chasers. The breakdown columns exist to test
whether early money consistently lands in longer-dated or near-the-money calls.

## Labels
`news_catalyst`, `sector_day` (3+ universe names moved together that day), `unknown`, `control`.
After-hours moves can't be seen in daily bars, so add those by hand as `after_hours` events.

## Database (Neon)
When the GitHub secret `DATABASE_URL` is set to a Neon (Postgres) connection string, everything
is stored there instead of the CSV files: tables `events`, `controls`, `daily`, `event_features`,
`history_done`, `errors`, `signal_report`, and `flags`. Without it, the CSV files in `data/` are used.
- First time: add the secret, then Run workflow → `migrate` (copies the CSV data in; safe to rerun).
- `flags` is the daily shortlist for the investigator agent: one row per stock and rule that fired,
  with empty `verdict` columns for the agent and the outcome filled in once 10 sessions have passed.
- Nightly runs refresh flags only; the full signal report runs on Fridays, after a backfill, or
  on demand with Run workflow → `report`.
- `store.py` holds the table definitions; new columns are added to existing tables automatically.
- **Local copy of the daily table.** Neon's free plan allows only 5 GB of downloads a month, and the
  daily table is about a million rows. So every job keeps a SQLite copy of it
  (`data/daily_mirror.sqlite`) in the GitHub Actions cache. Each daily write is time-stamped in the
  database, and on first use a job fetches only rows written since its copy was last synced (plus a
  2-hour overlap), so a normal job downloads megabytes instead of the whole table. A copy made from a
  different database is thrown away and rebuilt. Set `DAILY_MIRROR=off` to read the database directly.

## Ladder backtest (would it have made money?)
`ladder.py` (GitHub: Actions → "Ladder backtest" → Run workflow) takes every historical flag and an
equal number of random non-flag days on the same stocks, and pretends to buy the next day:
5 strikes (at the money, +5%, +10%, +15%, +20%) × 3 expirations (nearest to 14, 30, 90 days).
Each contract is followed daily and scored three ways: sell after 10 sessions, sell at 2x or
after 10 sessions, or hold to expiration. A 5% cost is charged on each side of every trade,
since past data has trade prices rather than bid and ask. Results: tables `ladder_trades`
(every contract) and `ladder_report` (by expiration, strike distance, exit rule, flag vs control).
It runs separately from the nightly job, paces itself slowly to share the Alpaca key with a
running backfill, and re-launches itself until done. Rerun it later to add newly tracked stocks.

## Trader generations (agents.py)
Agents walk week by week through history, trade, learn, and pass on lessons. Each generation:
1. **Training** (March 2024 to June 2025): each week it sees ~12 anonymized candidate stock-days
   (stock codes reshuffled every run, time as week numbers, prices only as percentages) and may buy
   the stock or one of 15 calls, up to 3 picks a week. Every trade is $1,000 and the goal is total
   profit (passing earns $0). Results show up two weeks later. Each candidate shows options activity
   plus technicals: 1/5/20-day change, price vs 20- and 50-day averages, distance from the 60-day high,
   RSI(14), and daily volatility.
2. **Lessons**: it rewrites the lessons document it inherited (no length limit). Only this document
   passes to the next generation; its trades and results never do.
3. **Scoring** (July 2025 to January 2026): it trades blind with its new lessons, no feedback.
Every run is compared with a random picker making the same number and kind of trades in the same
weeks. February 2026 onward is held back as a one-time final exam (`--phase test`).
Two lineages: `blank` (starts with nothing) and `briefed` (starts with our scorer findings).
Lineages are stored as `blank-v2` / `briefed-v2` (v1 runs had cut-off replies and never traded).
A training run stops itself if most replies can't be read, and the loop stops if a run makes no trades.
GitHub: Actions → "Trader generations". Needs the secret `OPENROUTER_API_KEY`. Results: AGENTS.md
and tables `agent_runs`, `agent_trades`, `agent_lessons`. A hard spending cap stops runs at `MAX_USD`.

## Committee generations (committee.py)
The bigger version of the agent loop. GitHub: Actions → "Committee generations".
- **Data split.** Every stock is dealt into one of 8 bundles matched on number of big moves and
  volatility; bundles 7 and 8 are held back for the final exam. March 2024 to January 2026 is cut into
  3-month blocks, and one random month per block is a blind scoring month. Candidates whose 10-session
  outcome would run into the other kind of month are dropped. February 2026 onward is the final exam.
- **Each generation.** Four agents start from the notes passed down and, independently, walk the six
  training bundles in the same shuffled order. Each week they rate every candidate (-2 to +2) and may
  buy up to 3. After each bundle they rewrite their own notes; at the end they state testable rules.
  Code tests every rule on all training bundles (the scorebook). An editor merges the four into the
  notes for the next generation (no length limit). A blind run trades the scoring months with the
  editor's notes, and the editor's rules are scored on those months; neither is ever shown to a later
  generation.
- **Run it.** First `build-pool` (reads the ladder archive release, not Neon), then `loop`.
  `weeks_fraction` 0.5 uses half the training weeks per bundle per generation (cheaper, more
  generations). Results: COMMITTEE.md, tables `pool`, `committee_notes`, `scorebook`, `agent_ratings`.
- **Final exam:** `final-test` with a generation number, once, at the very end.

## Scoring the signals
`python scorer.py` (runs automatically after every nightly and backfill) uses every trading day for
tickers with full history. For each day it computes signals from that day and earlier only, then
checks what the stock did over the next 10 sessions. Output:
- `data/signal_report.csv` – one row per rule and threshold: how often it fired, how often a big
  rally followed (hit rate), lift versus an average day, lift in each half of the data, and lift for
  a big DROP (if that is as high as the rally lift, the signal predicts volatility, not direction).
- `data/signal_days.csv` – every scored day with its signals and what happened next.

## Universe
- `all` (default): every active US stock with listed options on NYSE, Nasdaq, or NYSE American,
  excluding ETFs and other funds (leveraged index funds move a lot, but not on inside knowledge).
  Moves in stocks under $5 or trading under 500,000 shares a day on average are skipped.
- `core`: the 40 hand-picked volatile names in `UNIVERSE` at the top of collector.py.
  Switch with `DEFAULT_UNIVERSE` in collector.py.
- Stocks with 3+ big moves get full daily options history and are tracked nightly for flags.

## Limits
- No historical open interest from Alpaca, so "volume above open interest" needs another source later.
