CREATE TABLE IF NOT EXISTS dw.dim_transactionTime(
    Time_key SERIAL PRIMARY KEY,
    Hour INTEGER NOT NULL,
    Minute INTEGER NOT NULL
);