CREATE TABLE parties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(300),
    _id VARCHAR(300),
    roles VARCHAR(50),
    identifier_schema VARCHAR(300),
    identifier_uri VARCHAR(300),
    street_address VARCHAR(300),
    locality_address VARCHAR(300),
    region_address VARCHAR(30),
    postal_code VARCHAR(50),
    country_name VARCHAR(100),
    contact_name VARCHAR(300),
    contact_email VARCHAR(300),
    contact_telephone VARCHAR(300),
    contact_fax VARCHAR(100),
    entry_id VARCHAR(30)
);
\ copy parties(
    name,
    _id,
    roles,
    identifier_schema,
    identifier_uri,
    street_address,
    locality_address,
    region_address,
    postal_code,
    country_name,
    contact_name,
    contact_email,
    contact_telephone,
    contact_fax,
    entry_id
)
from 'PartiesForDB.csv' with DELIMITER '~';