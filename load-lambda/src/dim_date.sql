DELETE FROM dim_date;
INSERT INTO dim_date
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


