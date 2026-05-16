# Retail Sales Dashboard using Power BI

## Project Overview

This project analyzes retail sales data using Microsoft Power BI.  
The dataset was cleaned, transformed, and visualized to generate meaningful business insights through an interactive dashboard.

The dashboard helps analyze:

- Sales performance
- Profitability
- Regional trends
- Product category contribution
- Customer segment analysis

---

# Objectives

- Load and clean the retail sales dataset
- Perform data transformation
- Create calculated measures using DAX
- Develop an interactive Power BI dashboard
- Generate business insights

---

# Dataset

Dataset Used:

- `Retail_Sales_sample-Dataset.xlsx`

Dataset includes:

- Order details
- Product information
- Sales and profit values
- Customer segments
- Regional data
- Quantity and discount information

---

# Tools & Technologies

- Microsoft Power BI
- Microsoft Excel

---

# Data Cleaning Process

The following data cleaning steps were performed in Power Query:

## 1. Removed Blank Rows

- Removed empty records from the dataset

## 2. Removed Null Values

- Filtered out null and blank values

## 3. Removed Duplicate Records

- Removed duplicate entries using `Order ID`

## 4. Corrected Data Types

Updated columns to correct formats:

- Date
- Decimal Number
- Whole Number
- Text

## 5. Standardized Text Formatting

Applied:

- Capitalize Each Word

---

# Dashboard Features

## 1. Total Sales KPI

Displays total revenue generated.

### DAX Measure

```DAX
Total Sales = SUM('Sheet1'[Sales Amount])
```

---

## 2. Total Profit KPI

Displays total profit.

### DAX Measure

```DAX
Total Profit = SUM('Sheet1'[Profit])
```

---

## 3. Sales by Region

Bar chart showing sales performance by region.

---

## 4. Sales by Product Category

Pie/Donut chart showing category contribution.

---

# Additional Visuals

## Interactive Filters

Slicers added for:

- Region
- Product Category
- Customer Segment

---

# Key Business Insights

## Regional Analysis

- West and North regions generated higher sales.
- Some regions showed lower profitability.

## Product Analysis

- Electronics category contributed the highest revenue.
- High discounts reduced profit margins.

## Customer Segment Analysis

- Consumer and Corporate segments generated major revenue.
- Home Office segment contributed lower sales.

## Sales Trends

- Monthly sales trends revealed peak business periods.
- Useful for forecasting and inventory planning.

---

# Dashboard Layout

## Top Section

- Total Sales KPI
- Total Profit KPI

## Middle Section

- Sales by Region
- Sales by Product Category

## Right Side

- Interactive slicers and filters

---

# How to Run the Project

1. Open Microsoft Power BI Desktop
2. Load the dataset:
   - `Retail_Sales_sample-Dataset.xlsx`
3. Open:
   - `week5-activity2.pbix`
4. Refresh data if required
5. Explore the interactive dashboard

---

# Conclusion

This project demonstrates how retail sales data can be transformed into valuable business insights using Power BI. The dashboard provides a clear overview of sales performance, profitability, customer behavior, and regional trends.

---
