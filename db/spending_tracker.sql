DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    _description VARCHAR(255),
    _amount DECIMAL(10,2),
    _date DATETIME 
)

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    _merchant_name = VARCHAR(255),
)
