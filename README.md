# Stock Data Pull

This repository contains a small script for downloading historical data for the
SPY ETF using [yfinance](https://github.com/ranaroussi/yfinance). The script
retrieves daily OHLCV data and dividend information and stores them as CSV
files.

## Requirements

Python 3.8 or newer is required. Install the dependencies with `pip`:

```bash
pip install -r requirements.txt
```

### Installing Python on Windows

1. Download Python from the [official site](https://www.python.org/downloads/windows/).
2. Run the installer and select **Add Python to PATH**.
3. Open a new command prompt and check the version:

```bash
python --version
```

The command should print a version number of 3.8 or higher.

## Running the script

Execute the script with Python to download the data:

```bash
python pull_stock_data.py
```

This will generate the following files in the repository directory:

* `SPY_ohlc.csv` – daily OHLCV data
* `SPY_dividends.csv` – dividend data

You can adjust the ticker or date ranges by editing `pull_stock_data.py`.
