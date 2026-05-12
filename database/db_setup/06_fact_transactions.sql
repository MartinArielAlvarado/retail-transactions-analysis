CREATE TABLE IF NOT EXISTS dw.fact_transactions(
    Transaction_id SERIAL PRIMARY KEY,
    Customer_id INTEGER NOT NULL,
    Product_key INTEGER,
    Price DECIMAL NOT NULL,
    Quantity INTEGER NOT NULL,
    Discount_applied DECIMAL NOT NULL,
    Total_amount DECIMAL NOT NULL,
    Store_key INTEGER,
    Transaction_date DATE,
    Date_key INTEGER,
    Time_key INTEGER,
    Payment_key INTEGER,
    FOREIGN KEY (Product_key) REFERENCES dw.dim_product(Product_key),
    FOREIGN KEY (Store_key) REFERENCES dw.dim_store(Store_key),
    FOREIGN KEY (Date_key) REFERENCES dw.dim_transactionDate(Date_key),
    FOREIGN KEY (Time_key) REFERENCES dw.dim_transactionTime(Time_key),
    FOREIGN KEY (Payment_key) REFERENCES dw.dim_payment(Payment_key)
);