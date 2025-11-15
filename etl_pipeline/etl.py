
#imports
import pandas as pd
from sqlalchemy import create_engine

# Load raw CSV into dataframe
df = pd.read_csv("data/raw/Online_Retail.csv")

# Ensure csv read
print(df.info())
print(df)
df_raw = df.copy()

# Base Data Cleaning for Product-level dataset
df = df.drop_duplicates()
df = df.dropna(subset=['Description'])
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df = df[~df['InvoiceNo'].str.startswith('c')]
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
df['Description'] = df['Description'].str.strip().str.lower()
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df['CustomerID'] = df['CustomerID'].astype('Int64')
df.reset_index(drop=True, inplace=True)
print(df.info())

# Customer-level dataset (drop null CustomerID)
df_customers = df.dropna(subset=["CustomerID"]).copy()
print(df_customers.info())
df_customers.reset_index(drop=True, inplace=True)

# Make all column names lowercase
df.columns = df.columns.str.lower()
df_customers.columns = df_customers.columns.str.lower()


print("Rows loaded to products_clean:", len(df))
print("Rows loaded to customers_clean:", len(df_customers))

# Connect to Postgres
engine = create_engine("postgresql+psycopg2://retail_user:password123@localhost:5432/retail_db")

# Product-level table
try:
    df.to_sql("products_clean", engine, if_exists="replace", index=False)
except Exception as e:
    print("Error loading products_clean:", e)

# Customer-level table
try:
    df_customers.to_sql("customers_clean", engine, if_exists="replace", index=False)
except Exception as e:
    print("Error loading customers_clean:", e)




