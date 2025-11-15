CREATE TABLE dim_product AS
SELECT DISTINCT
    stockcode,
    description,
    unitprice
FROM products_clean;
