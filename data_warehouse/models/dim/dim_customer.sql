CREATE TABLE dim_customer AS
SELECT DISTINCT
    customerid,
    country
FROM customers_clean
WHERE customerid IS NOT NULL;
