DROP TABLE IF EXISTS  dim_date;

CREATE TABLE dim_date AS 
SELECT 
ts_seq AS date_value, 
extract (day FROM ts_seq) AS day_of_month, 
to_char(ts_seq, 'TMDay') AS day_name, 
extract (isodow FROM ts_seq) AS day_of_week, 
extract (month FROM ts_seq) AS month_number, 
TO_CHAR(ts_seq, 'TMMonth') AS month_name, 
extract (year FROM ts_seq) AS year, 
extract (quarter FROM ts_seq) AS quarter, 
'FY' || extract(year FROM ts_seq - interval '3 month' )::varchar AS financial_year 
FROM
(SELECT '2022-01-01' :: DATE + sequence.day AS ts_seq  
FROM GENERATE_SERIES(0,  1825) AS sequence(day)) dq; 