-- Fact table for sales transactions with customer info
CREATE TABLE fact_sales AS
SELECT
    invoiceno,
    invoicedate,
    customerid,
    stockcode,
    quantity,
    unitprice,
    ROUND(totalprice::numeric, 2) AS totalprice
FROM products_clean;
