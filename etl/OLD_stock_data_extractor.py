# Import the os module to interact with the operating system (e.g., environment variables)
import os
# Import the requests library to make HTTP requests to external APIs
import requests
# Import the load_dotenv function from the dotenv package to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from a .env file into the process's environment
load_dotenv()

# Define a class to encapsulate all logic related to extracting stock data from Alpha Vantage
class StockDataExtractor:
    # Constructor method for initializing the StockDataExtractor object
    def __init__(self):
        # Retrieve the Alpha Vantage API key from environment variables for secure access
        self.api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        # Set the base URL for the Alpha Vantage API endpoint
        self.base_url = "https://www.alphavantage.co/query"

    # Define a method to fetch daily stock data for a given stock symbol
    def fetch_daily_stock(self, symbol):
        # Prepare the parameters required by the Alpha Vantage API for fetching daily adjusted time series data
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",  # Specify the API function to call
            "symbol": symbol,                          # Specify the stock symbol to fetch data for
            "apikey": self.api_key,                    # Include the API key for authentication
            "outputsize": "compact"                    # Request only the last 100 data points; use "full" for all data
        }
        # Make a GET request to the Alpha Vantage API with the specified parameters
        response = requests.get(self.base_url, params=params)
        # Check if the HTTP response status code indicates success (200 OK)
        if response.status_code == 200:
            # Parse the JSON response body into a Python dictionary
            data = response.json()
            # Check if the response contains an error message from the API
            if "Error Message" in data:
                # Print the error message to inform the user of the issue
                print(f"Error from API: {data['Error Message']}")
                # Return None to indicate failure to fetch data
                return None
            if "Information" in data:
                # Print the informational message to inform the user of the issue
                print(f"Info from API: {data['Information']}")
                # Return None to indicate failure to fetch data
                return None
            # Return the parsed data dictionary if no error occurred
            return data
        else:
            # Print an error message if the HTTP response status code is not 200
            print(f"HTTP Error: {response.status_code}")
            # Return None to indicate failure to fetch data
            return None

# Check if this script is being run as the main program (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the StockDataExtractor class
    extractor = StockDataExtractor()
    # Call the fetch_daily_stock method to fetch data for the "MSFT" (Microsoft) stock symbol
    result = extractor.fetch_daily_stock("MSFT")  # Example stock symbol
    # Check if the result is not None, indicating successful data retrieval
    if result:
        # Print a success message to inform the user
        print("Fetched stock data successfully.")
        print("API KEY:", self.api_key)
        # Print the fetched data to the console for inspection
        # Print a list of the top-level keys in the returned data dictionary to verify the structure
        print(list(result.keys()))
    else:
        # Print a failure message if data could not be fetched
        print("Failed to fetch stock data.")