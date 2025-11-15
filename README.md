📊 Retail Analytics Project

End-to-End Data Pipeline + Dashboard (Pandas, PostgreSQL, dbt, SQLAlchemy, SQL, Tableau)

This project analyzes e-commerce sales data and builds an interactive dashboard that highlights top-selling products, country-level customer distribution, and trends in order behavior.

It showcases skills in data engineering, data modeling, SQL transformation, and data visualization.

🚀 Project Overview

This repository contains an end-to-end analytics pipeline using:

Backend / Data Engineering

Python + SQLAlchemy → Cleaned and loaded CSV data into PostgreSQL

PostgreSQL → Data warehouse storing fact and dimension tables

dbt (Data Build Tool) → transformed and modeled the warehouse data

ETL Pipeline → Extract (CSV), Transform (dbt), Load (Postgres)

Frontend / Analytics

Tableau Desktop → Connected to the warehouse

Built dashboards such as:

Top Selling Products

Customer Count by Country (Interactive Map)

Time-based Sales Analysis

Architecture Diagram:

CSV File → Python (SQLAlchemy) → PostgreSQL Warehouse 
          → dbt Transformations → Clean Fact/Dim Tables → Tableau Dashboards

🗂️ Dataset Description

The cleaned data warehouse contains:

Dimension Tables

dim_customer – customer ID, country

dim_product – product stock code, description, unit price

Fact Table

fact_sales – order ID, stock code, date, customer ID, quantity, unit price, total price

🔧 Tools and Technologies:
| Tool                    | Purpose                                              |
| ----------------------- | ---------------------------------------------------- |
| **PostgreSQL**          | Cloud/local warehouse for analytics                  |
| **Python + SQLAlchemy** | Loaded/ingested cleaned CSV data into tables         |
| **dbt**                 | SQL transformations, models                          |
| **Tableau Desktop**     | Dashboards + charts                                  |
| **GitHub**              | Version control + project publishing                 |

🧠 Key Skills Demonstrated

SQL database design & schema creation

Loading external data using Python and SQLAlchemy

Cleaning data with Python Pandas

Designing fact/dimension models

Building dbt models

Joining tables through dbt + Tableau

Creating professional dashboards with filters, maps, and KPIs

Git version control and repo publishing

📁 Repository Structure

/etl_pipeline          → python script

/data_warehouse/models → dbt models

/dashboards            → Tableau workbook, pdf with screenshots and demo link (.twbx / .pdf)

/data/raw              → link to original CSV

README.md

📝 How to Run the Project

Clone the repo

Download CSV file from link

Create a PostgreSQL database

Run the ETL script

Configure dbt profile (~/.dbt/profiles.yml)

Run dbt on SQL scripts

Open Tableau → connect to Postgres → import dashboards

📫 Contact

If you'd like help customizing or extending this project, feel free to open an issue or reach out.
