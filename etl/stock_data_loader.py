import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

class StockDataLoader:
    def __init__(self, host, dbname, user, password, port=5432):
        """
        Initializes the StockDataLoader with database connection parameters.

        Args:
            host (str): Database host.
            dbname (str): Database name.
            user (str): Database user.
            password (str): Database password.
            port (int, optional): Database port. Defaults to 5432.
        """
        self.conn_params = {
            'host': host,
            'dbname': dbname,
            'user': user,
            'password': password,
            'port': port
        }
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = psycopg2.connect(**self.conn_params)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def load_data(self, symbol, df):
        self.connect()

        records = []
        for date, row in df.iterrows():
            records.append((
                symbol,
                date.to_pydatetime(),
                float(row['Open']),
                float(row['High']),
                float(row['Low']),
                float(row['Close']),
                int(row['Volume']) if not pd.isna(row['Volume']) else None
            ))

        query = """
            INSERT INTO stock_prices (symbol, date, open, high_price, low_price, close, volume)
            VALUES %s
            ON CONFLICT (symbol, date) DO UPDATE
            SET open = EXCLUDED.open,
                high_price = EXCLUDED.high_price,
                low_price = EXCLUDED.low_price,
                close = EXCLUDED.close,
                volume = EXCLUDED.volume;
        """

        with self.conn.cursor() as cur:
            try:
                execute_values(cur, query, records)
                self.conn.commit()
                print(f"Data for {symbol} loaded successfully.")
            except Exception as e:
                print(f"Error loading data for {symbol}: {e}")
                self.conn.rollback()