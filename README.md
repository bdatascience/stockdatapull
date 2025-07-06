# Stock Data Pull

This repository contains a small script for downloading historical data for the
QQQ ETF using [yfinance](https://github.com/ranaroussi/yfinance). The script
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

* `QQQ_monthly_ohlc.csv` – the first trading day of each month
* `QQQ_dividends.csv` – dividend data for the same period

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

Choose a single ticker and the date range in the app. The resulting OHLC data will be saved as
`<TICKER>_<START>_<END>.csv` and previewed in the browser. If you select the
**Download dividends** option, a single file containing both closing prices and
dividends will be created. The combined column is named
`ClosingPrice_Dividends` and the file will be stored in the directory specified
in the **Download directory** text box (defaults to your Downloads folder).
