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

Execute the script with Python to download the data:

```bash
python pull_stock_data.py
```

This will generate the following files in the repository directory:

* `SPY_ohlc.csv` – daily OHLCV data
* `SPY_dividends.csv` – dividend data

You can adjust the ticker or date ranges by editing `pull_stock_data.py`.
