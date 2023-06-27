# Adventure Works Analysis

## Introduction
You've been hired as a Business Intelligence Analyst by AdventureWorks, a global manufacturing company that produces cycling equipments and accessories. The company has a database with all the sales data from 2015 to 2017. Your job is to analyze the data and create a dashboard to present your findings according to client ask.

## Business Scenario
- The management team needs a way to track KPIs (sales, revenue, profit, returns), compare regional performance, analyze product-level trends, and identify high-value customers.
- Datasets are in the form of raw CSV files, which contain information about transactions, returns, products, customers, and sales territories.
- You can use any tool to transform the data but it has to have following two features:
    - Normalized relational data model in powerbi backend
    - Reports available both in powerbi desktop and powerbi service

## Delivery

- Data Transformation
    - Python (pandas and numpy libraries) has been used to transform raw data (storage/raw folder in root project) into processed form (storage/processed folder in root project)
    - Data transformation code is available in following notebooks under notebooks/ folder in root project
    
    ![Alt text](/images/transformation_notebooks.png "Data Transformation using Jupyter Notebooks")

- Data Model
    - PowerBI Desktop has been used to create a data model using processed data (storage/processed folder in root project)
    - Snowflake schema has been used to create a data model as follows:
    
    ![Alt text](/images/data_model.png "Data Model in PowerBI Desktop")

- Reports
    - PowerBI Desktop has been used to create reports using data model 
    - Refer to adventure_works_report.pbix file in root project for desktop reports

    ![Alt text](/images/exec_summary.png "Executive Summary Report")

    ![Alt text](/images/product_summary.png "Product Summary Report")

    - PowerBI Service has been used to publish reports to cloud and can be accessed using following link --> https://app.powerbi.com/view?r=eyJrIjoiZGE0ZDYwODUtMGZiOC00MTdjLWFmZGMtY2Q0MjI3Yjg5Y2E2IiwidCI6IjdmYWFhMjMyLWI0MDctNDhlZS04ZmQyLWE0ZDkyZWZhOWEwNCIsImMiOjJ9
