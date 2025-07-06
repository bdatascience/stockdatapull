import streamlit as st
import yfinance as yf
from datetime import date
from pathlib import Path
import pandas as pd

from pull_stock_data import filter_first_day_month

st.title("Stock Data Downloader")

# Inputs
symbol = st.text_input("Ticker symbol", "QQQ")
start_date = st.date_input("Start date", value=date(2022, 1, 1))
end_date = st.date_input("End date", value=date.today())
monthly_only = st.checkbox("First day of each month only", value=True)
show_dividends = st.checkbox("Download dividends", value=True)
download_dir = st.text_input(
    "Download directory",
    value=str(Path.home() / "Downloads"),
)

if st.button("Download Data"):
    if not symbol:
        st.error("Please enter a ticker symbol")
    elif start_date >= end_date:
        st.error("Start date must be before end date")
    else:
        data = yf.download(symbol, start=start_date, end=end_date, interval="1d")
        data.index = data.index.tz_localize(None)
        if isinstance(data["Close"], pd.DataFrame):
            st.error("Multiple tickers are not supported. Please enter one symbol.")
            st.stop()
        if monthly_only:
            data = filter_first_day_month(data)

        out_dir = Path(download_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        if show_dividends:
            ticker = yf.Ticker(symbol)
            dividends = ticker.dividends.loc[str(start_date):str(end_date)]
            dividends.index = dividends.index.tz_localize(None)
            combined = pd.concat(
                [
                    data["Close"].rename("ClosingPrice_Dividends"),
                    dividends.rename("ClosingPrice_Dividends"),
                ]
            ).sort_index()
            file_name = out_dir / f"{symbol}_ClosingPrice_Dividends_{start_date}_{end_date}.csv"
            combined.to_csv(file_name)
            st.success(f"Data saved to {file_name}")
            st.dataframe(combined)
        else:
            file_name = out_dir / f"{symbol}_{start_date}_{end_date}.csv"
            data.to_csv(file_name)
            st.success(f"Data saved to {file_name}")
            st.dataframe(data)
