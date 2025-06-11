# 📊 MarketPulse

**An Analytics-Driven View of Stock Trends & Company Insights**

---

MarketPulse is a simple yet powerful ETL (Extract, Transform, Load) pipeline that fetches daily stock price data using the [yfinance](https://github.com/ranaroussi/yfinance) Python library and loads it into a PostgreSQL database. This project is a foundational tool for analyzing stock market data or building data products around financial time series.

---

## 🚀 Features

- **Extract** historical daily stock data for specified symbols
- **Transform** data to a normalized database schema
- **Load** data efficiently into PostgreSQL with upsert capability
- Database connection pooling and error management
- Modular design: separate modules for extraction, loading, and table creation

---

## 🛠️ Technologies

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [psycopg2](https://www.psycopg.org/) (PostgreSQL adapter)
- PostgreSQL (v17 recommended)

---

## ⚡ Quickstart

### 1. Clone & Setup Environment

```bash
git clone <repo-url>
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

- **Create a PostgreSQL database** named `stockdb`.
- **Create a user** `stockuser` with appropriate privileges.
- **Run the table creation script:**

    ```bash
    psql -U postgres -d stockdb -f db/create_tables.sql
    ```

### 4. Configure & Run

- Edit database connection parameters in `main.py` or your config file.
- Run the main script:

    ```bash
    python main.py
    ```

---

## 🧰 Troubleshooting

- Ensure PostgreSQL server is running and accessible.
- Verify the database user has correct permissions.
- Confirm your Python environment has all required packages.
- For permission errors, connect as superuser and grant privileges.

---

## 📄 License

This project is licensed under the MIT License.

---