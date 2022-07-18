DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS types;

CREATE TABLE types(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    merchant_name VARCHAR(255)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10,2),
    type_id INT REFERENCES types(id),
    merchant_id INT REFERENCES merchants(id)
);




