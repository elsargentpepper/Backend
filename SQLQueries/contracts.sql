CREATE TABLE contracts (
    id SERIAL PRIMARY KEY,
    subcontract_id BIGINT NOT NULL,
    title VARCHAR(300) NOT NULL,
    status VARCHAR(20) NOT NULL,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    amount REAL NOT NULL,
    currency VARCHAR(5) NOT NULL,
    entry_id VARCHAR(30) NOT NULL
);
\ copy contracts(
    subcontract_id,
    title,
    status,
    start_date,
    end_date,
    amount,
    currency,
    entry_id
)
from 'ContractsForDB.csv' with DELIMITER '~';