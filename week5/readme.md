Retail Sales Dashboard using Power BI
Project Overview

This project focuses on analyzing retail sales data using Microsoft Power BI.
The dataset was cleaned, transformed, and visualized to generate business insights through an interactive dashboard.

The dashboard helps identify:

Sales performance
Profitability
Regional trends
Product category contribution
Customer segment analysis
Objectives
Load and clean the retail sales dataset
Perform data transformation
Create calculated measures using DAX
Develop an interactive Power BI dashboard
Generate meaningful business insights
Dataset

Dataset Used:

Retail_Sales_sample-Dataset.xlsx

Dataset contains:

Order information
Product details
Sales and profit values
Customer segments
Regional data
Discounts and quantities
Tools & Technologies
Microsoft Power BI
Microsoft Excel
DAX (Data Analysis Expressions)
Data Cleaning Process

The following cleaning steps were performed in Power Query:

1. Removed Blank Rows
   Removed empty records from the dataset
2. Removed Null Values
   Filtered out null and blank values
3. Removed Duplicate Records
   Duplicates removed using Order ID
4. Corrected Data Types

Updated columns to proper formats:

Date
Decimal Number
Whole Number
Text 5. Standardized Text Formatting

Applied:

Capitalize Each Word 6. Created Date Features

Dashboard Features

1. Total Sales KPI

Displays overall revenue generated.

DAX Measure
Total Sales = SUM('Sheet1'[Sales Amount])

2.  Total Profit KPI

Displays overall profit.

DAX Measure
Total Profit = SUM('Sheet1'[Profit]) 3. Sales by Region

Bar chart showing sales distribution across regions.

4. Sales by Product Category

Pie/Donut chart showing contribution of each category.

Additional Visuals
Monthly Sales Trend

Line chart showing monthly sales performance.

Profit by Customer Segment

Column chart displaying profit contribution by customer type.

Interactive Filters

Slicers added for:

Region
Product Category
Customer Segment
Key Business Insights
Regional Analysis
West and North regions generated strong sales performance.
Some regions showed lower profitability.
Product Analysis
Electronics category contributed the highest revenue.
High discounts impacted profit margins.
Customer Segment Analysis
Consumer and Corporate segments generated major sales.
Home Office segment contributed lower revenue.
Sales Trends
Useful for forecasting and inventory planning.
Dashboard Layout
Top Section
Total Sales KPI
Total Profit KPI
Total Quantity Sold KPI
Middle Section
Sales by Region
Sales by Product Category
Bottom Section
Profit by Customer Segment
Right Side
Interactive slicers and filters
