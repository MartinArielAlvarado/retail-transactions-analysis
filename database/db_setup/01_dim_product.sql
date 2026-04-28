CREATE TABLE IF NOT EXISTS dw.dim_product(
    Product_key SERIAL PRIMARY KEY,
    Product_id VARCHAR(100) NOT NULL,
    Product_category VARCHAR(100) NOT NULL
);