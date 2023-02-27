DROP DATABASE IF EXISTS cp_tot_wrh;

CREATE DATABASE cp_tot_wrh;

\c cp_tot_wrh;

DROP TABLE IF EXISTS fact_sales_order;
CREATE TABLE fact_sales_order (
    sales_record_id SERIAL PRIMARY KEY,
    sales_order_id INT NOT NULL,
    created_date DATE,
    created_time TIME,
    last_updated_date DATE,
    last_updated_time TIME,
    sales_staff_id INT NOT NULL,
    counterparty_id INT NOT NULL,
    units_sold INT,
    unit_price NUMERIC (10, 2),
    currency_id INT,
    design_id INT,
    agreed_payment_date DATE,
    agreed_delivery_date DATE,
    agreed_delivery_location_id INT
);

DROP TABLE IF EXISTS dim_dates;
CREATE TABLE dim_dates AS
SELECT
    ts_seq AS date_id,
    extract(year FROM ts_seq) AS year,
    CAST(extract (month FROM ts_seq) AS INTEGER) AS month,
    extract(day FROM ts_seq) AS day,
    extract(isodow FROM ts_seq) AS day_of_week,
    to_char(ts_seq, 'TMDay') AS day_name,
    TO_CHAR(ts_seq, 'TMMonth') AS month_name,
    extract(quarter FROM ts_seq) AS quarter
FROM
(SELECT '2022-01-01' :: DATE + sequence.day AS ts_seq
     FROM GENERATE_SERIES(0, 1825) AS sequence(day)) dq
;
--SELECT * FROM dim_dates;

DROP TABLE IF EXISTS dim_staff;
CREATE TABLE dim_staff (
    staff_id INT PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    department_name VARCHAR,
    location VARCHAR,
    email_address VARCHAR
);

DROP TABLE IF EXISTS dim_location;
CREATE TABLE dim_location (
  location_id INT PRIMARY KEY,
  address_line_1 varchar,
  address_line_2 varchar,
  district varchar,
  city varchar,
  postal_code varchar,
  country varchar,
  phone varchar
);

DROP TABLE IF EXISTS dim_currency;
CREATE TABLE dim_currency (
  currency_id INT PRIMARY KEY,
  currency_code varchar,
  currency_name varchar
);

DROP TABLE IF EXISTS dim_design;
CREATE TABLE dim_design (
  design_id INT PRIMARY KEY,
  design_name varchar,
  file_location varchar,
  file_name varchar 
);

DROP TABLE IF EXISTS dim_counterparty;
CREATE TABLE dim_counterparty (
  counterparty_id INT PRIMARY KEY,
  counterparty_legal_name varchar,
  counterparty_legal_address_line_1 varchar,
  counterparty_legal_address_line2 varchar,
  counterparty_legal_district varchar,
  counterparty_legal_city varchar,
  counterparty_legal_postal_code varchar,
  counterparty_legal_country varchar,
  counterparty_legal_phone_number varchar
);