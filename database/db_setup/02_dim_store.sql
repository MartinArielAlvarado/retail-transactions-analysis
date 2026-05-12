CREATE TABLE IF NOT EXISTS dw.dim_store(
    Store_key SERIAL PRIMARY KEY,
    Store_location VARCHAR(255) NOT NULL
);