import streamlit as st
import yfinance as yf
from datetime import date
import pandas as pd

from pull_stock_data import filter_first_day_month

st.title("Stock Data Downloader")

# Inputs
symbol = st.text_input("Ticker symbol", "QQQ")
start_date = st.date_input("Start date", value=date(2022, 1, 1))
end_date = st.date_input("End date", value=date.today())
monthly_only = st.checkbox("First day of each month only", value=True)
show_dividends = st.checkbox("Download dividends", value=True)

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
        if show_dividends:
            ticker = yf.Ticker(symbol)
            dividends = ticker.dividends.loc[str(start_date):str(end_date)]
            div_file = f"{symbol}_dividends_{start_date}_{end_date}.csv"
            if not dividends.empty:
                dividends.to_csv(div_file)
                st.success(f"Dividends saved to {div_file}")
            else:
                st.info("No dividend data found for the selected period")
            union_df = pd.concat(
                [
                    dividends.to_frame(name="Dividends"),
                    data[["Close"]].rename(columns={"Close": "Dividends"}),
                ]
            ).sort_index()
            st.dataframe(union_df)
        else:
            st.dataframe(data)
