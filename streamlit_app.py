import streamlit as st
import yfinance as yf
from datetime import date

from pull_stock_data import filter_first_day_month

st.title("Stock Data Downloader")

# Inputs
symbol = st.text_input("Ticker symbol", "SPY")
start_date = st.date_input("Start date", value=date(2022, 1, 1))
end_date = st.date_input("End date", value=date.today())
monthly_only = st.checkbox("First day of each month only", value=True)

if st.button("Download Data"):
    if not symbol:
        st.error("Please enter a ticker symbol")
    elif start_date >= end_date:
        st.error("Start date must be before end date")
    else:
        data = yf.download(symbol, start=start_date, end=end_date, interval="1d")
        if monthly_only:
            data = filter_first_day_month(data)
        file_name = f"{symbol}_{start_date}_{end_date}.csv"
        data.to_csv(file_name)
        st.success(f"Data saved to {file_name}")
        st.dataframe(data)
