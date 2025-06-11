import os
import psycopg2
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    print("Database connection successful.")
    conn.close()
except Exception as e:
    print("Database connection failed.")
    print(f"Error: {e}")
    #exit(1)