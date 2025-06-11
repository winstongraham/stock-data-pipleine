# main.py

from etl.stock_data_extractor import StockDataExtractor
from etl.stock_data_loader import StockDataLoader

def main():
    # Step 1: Extract
    extractor = StockDataExtractor()
    symbol = "MSFT"
    data = extractor.fetch_daily_stock(symbol)

    if data is None:
        print("No data was fetched. Exiting.")
        return

    # Step 2: Load
    loader = StockDataLoader(
        host="localhost",
        dbname="stockdb",
        user="stockuser",
        password="stockpw"
    )

    loader.load_data(symbol, data)
    loader.close()
    print("Data loaded to database successfully.")

if __name__ == "__main__":
    main()
# This script orchestrates the ETL process by extracting stock data and loading it into a database.
# It first fetches daily stock data for a specified symbol using the StockDataExtractor,