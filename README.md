# Stock Data Pull

This repository contains a small script for downloading historical data for the
SPY ETF using [yfinance](https://github.com/ranaroussi/yfinance). The script
retrieves daily OHLCV data and dividend information and stores them as CSV
files.

## Requirements

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Running the script

Execute the script with Python to download the data. You can optionally
specify the ticker symbol and date range using command-line arguments:

```bash
# Download SPY data using the defaults
python pull_stock_data.py

# Download AAPL data for a custom date range
python pull_stock_data.py --ticker AAPL --start 2023-01-01 --end 2023-06-30
```

The script generates two CSV files in the repository directory named after
the ticker symbol:

* `<TICKER>_ohlc.csv` – daily OHLCV data
* `<TICKER>_dividends.csv` – dividend data

If no arguments are supplied, it defaults to downloading SPY data from
`2022-01-01` through `2024-12-31`.
