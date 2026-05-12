CREATE TABLE IF NOT EXISTS dw.dim_payment(
    Payment_key SERIAL PRIMARY KEY,
    Payment_method VARCHAR(255) NOT NULL
);