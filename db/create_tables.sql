CREATE TABLE IF NOT EXISTS stock_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    date DATE NOT NULL,
    open NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    close NUMERIC,
    volume BIGINT,
    unique (symbol, date)
);