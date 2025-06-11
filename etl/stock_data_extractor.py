import yfinance as yf  # Import the yfinance library for downloading financial data

class StockDataExtractor:
    def __init__(self):
        # yfinance does not require API keys or authentication, so nothing is needed here
        pass

    def fetch_daily_stock(self, symbol):
        """
        Fetches daily historical stock data for a given symbol using yfinance.

        Args:
            symbol (str): The stock ticker symbol (e.g., 'AAPL', 'MSFT').

        Returns:
            pandas.DataFrame or None: DataFrame containing historical daily stock data,
                                     or None if data could not be fetched.
        """
        try:
            # Create a Ticker object for the given symbol.
            # This object provides access to various data and methods for the stock.
            ticker = yf.Ticker(symbol)

            # Download historical market data for the ticker.
            # period="max" fetches the maximum available data.
            # interval="1d" specifies daily frequency.
            data = ticker.history(period="max", interval="1d")

            # Check if the returned DataFrame is empty.
            # This can happen if the symbol is invalid or there is no data available.
            if data.empty:
                print(f"No data found for symbol: {symbol}")
                return None

            # If data is successfully fetched, return the DataFrame.
            return data

        except Exception as e:
            # Catch any exceptions (e.g., network errors, invalid symbol)
            # and print an error message.
            print(f"Error fetching data: {e}")
            return None

if __name__ == "__main__":
    # Instantiate the StockDataExtractor class.
    extractor = StockDataExtractor()

    # Fetch daily stock data for Microsoft (MSFT).
    result = extractor.fetch_daily_stock("MSFT")

    # Check if data was fetched successfully.
    if result is not None:
        print("Fetched stock data successfully.")
        # Print the first few rows of the DataFrame to verify the data.
        print(result.head())
    else:
        print("Failed to fetch stock data.")
