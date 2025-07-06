import yfinance as yf


def main() -> None:
    """Download SPY data and save to CSV files."""
    # Load SPY ETF
    ticker = yf.Ticker("SPY")

    # Get OHLCV data
    ohlc = ticker.history(start="2022-01-01", end="2024-12-31", interval="1d")

    # Get dividend data
    dividends = ticker.dividends.loc["2022-01-01":"2024-12-31"]

    # Save to CSV
    ohlc.to_csv("SPY_ohlc.csv")
    dividends.to_csv("SPY_dividends.csv")


if __name__ == "__main__":
    main()
