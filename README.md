# Performance Of Vendor Project

A comprehensive analysis of vendor performance using sales, inventory, and purchase data, leveraging SQL, Python, and Power BI to deliver actionable insights and dashboards for business decision-making.

## Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Tools and Technologies](#tools-and-technologies)
- [Project Structure](#project-structure)
- [Methods](#methods)
- [Key Insights](#key-insights)
- [Dashboard](#dashboard)
- [How to Run This Project](#how-to-run-this-project)
- [Result and Conclusion](#result-and-conclusion)
- [Future Work](#future-work)
- [Author & Contact](#author--contact)

## Overview
This project evaluates vendor performance by analyzing inventory, sales, and purchase data. The goal is to identify high-performing vendors, optimize procurement, and improve inventory management.

## Problem Statement
Organizations often struggle to assess vendor effectiveness due to fragmented data sources and lack of integrated analytics. This project aims to consolidate and analyze vendor-related data to support strategic sourcing and inventory decisions.

## Dataset
- **Raw Data:** Includes begin and end inventory, purchase prices, purchases, sales, and vendor invoices.
- **Vendor Sales Summary:** Aggregated sales data per vendor.

## Tools and Technologies
- SQL (for data extraction and transformation)
- Python (for data analysis and reporting)
- Power BI (for dashboard visualization)

## Project Structure
```
dashboard/
    vendor_performance_dashboard_power_bi/
data/
    raw_data/
        begin_inventory/
        end_inventory/
        purchase_prices/
        purchases/
        sales/
        vendor_invoice/
    vendor_sales_summary/
images/
db/
    logs/
    inventory1/
notebook/
    exploratory_data_analysis_sql_phyton/
    vendor_performance_analysis_sql_phyton/
src/
    get_vendor_summary/
    inventory_db/
vedor_performance_analysis_report.pdf   
```

## Methods
- Data extraction and cleaning using SQL and Python.
- Exploratory data analysis to identify trends and outliers.
- Vendor performance scoring based on sales, inventory turnover, and purchase efficiency.
- Visualization of key metrics in Power BI.

## Key Insights
- Identification of top and underperforming vendors.
- Trends in inventory turnover and purchase efficiency.
- Actionable recommendations for procurement and inventory management.

## Dashboard
Interactive Power BI dashboard visualizing vendor performance metrics, sales trends, and inventory analysis.

#### Preview
<img width="653" height="362" alt="image" src="https://github.com/user-attachments/assets/d68672f6-4539-428e-bea3-4956ea380804" />



## How to Run This Project
1. Clone the repository.
2. Set up the database using scripts in `db/`.
3. Run data processing notebooks in `notebook/`.
4. Open the Power BI dashboard in `dashboard/vendor_performance_dashboard_power_bi/`.

## Result and Conclusion
The project delivers a unified view of vendor performance, enabling data-driven decisions for vendor selection and inventory optimization.

## Future Work
- Automate data pipeline for real-time analytics.
- Integrate additional data sources (e.g., supplier ratings).
- Enhance predictive analytics for vendor performance.

## Author & Contact
Name : Sai Krishna Sajjanam

Email: sai.newmailbox@gmail.com
