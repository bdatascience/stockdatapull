import argparse
import yfinance as yf

parser = argparse.ArgumentParser(description="Download historical stock data")
parser.add_argument("--ticker", default="SPY", help="Ticker symbol to download")
parser.add_argument("--start", default="2022-01-01", help="Start date in YYYY-MM-DD format")
parser.add_argument("--end", default="2024-12-31", help="End date in YYYY-MM-DD format")
args = parser.parse_args()
ticker = yf.Ticker(args.ticker)

ohlc = ticker.history(start=args.start, end=args.end, interval="1d")

dividends = ticker.dividends.loc[args.start:args.end]

# Save to CSV
ohlc.to_csv(f"{args.ticker}_ohlc.csv")
dividends.to_csv(f"{args.ticker}_dividends.csv")
