# Stock Data Pull

This repository contains a small script for downloading historical data for the
SPY ETF using [yfinance](https://github.com/ranaroussi/yfinance). The script
retrieves price data and dividend information and stores them as CSV files. By
default the price data includes only the first trading day of each month.

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

* `SPY_monthly_ohlc.csv` – the first trading day of each month
* `SPY_dividends.csv` – dividend data for the same period

You can adjust the ticker or date ranges by editing `pull_stock_data.py`.

## Using the Streamlit interface

You can also download data through the Streamlit app. Run:

```bash
streamlit run streamlit_app.py
```

From a Bash shell you can also start it with:

```bash
bash -c 'streamlit run streamlit_app.py'
```

Choose the ticker and dates in the app. The resulting CSV will be saved as `<TICKER>_<START>_<END>.csv`.
