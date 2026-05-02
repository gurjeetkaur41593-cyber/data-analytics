# Data Cleaning and Visualization with Pearson Correlation Heatmap

## Project Overview

This project demonstrates the process of data cleaning, exploratory data analysis, and visualization using a messy dataset. The primary objective is to improve data quality and uncover meaningful relationships between numerical variables using the Pearson correlation coefficient.

The analysis includes:

- Data cleaning and preprocessing
- Handling missing values and duplicates
- Correcting inconsistent data formats
- Visualizing relationships using a Pearson correlation heatmap
- Detecting outliers using boxplots and the IQR method

---

## Dataset Description

The dataset contains employee-related information with the following features:

- **ID** – Unique employee identifier
- **Name** – Employee name
- **Age** – Employee age
- **Country** – Country of residence
- **Salary** – Employee salary
- **Join Date** – Employment start date

---

## Data Cleaning Steps

The raw dataset contained several quality issues, including:

- Missing values in Age, Salary, Name, Country, ID, and Join Date
- Duplicate records
- Incorrect data formats (for example, text values in numerical columns)
- Inconsistent date formatting

### Cleaning Actions Performed

1. Removed duplicate records.
2. Converted Age and Salary to numeric data types.
3. Standardized Join Date into datetime format.
4. Replaced missing numerical values using the median.
5. Identified and handled invalid entries.
6. Prepared the dataset for analysis and visualization.

---

## Pearson Correlation Analysis

The Pearson correlation coefficient measures the strength and direction of a linear relationship between two numerical variables.

- **+1** indicates a perfect positive correlation.
- **0** indicates no linear correlation.
- **-1** indicates a perfect negative correlation.

### Correlation Results

| Variables     | Correlation Coefficient | Interpretation            |
| ------------- | ----------------------- | ------------------------- |
| Age vs Salary | 0.26                    | Weak positive correlation |
| ID vs Age     | -0.03                   | No meaningful correlation |
| ID vs Salary  | 0.03                    | No meaningful correlation |

### Key Insight

The analysis shows a weak positive correlation between Age and Salary. This suggests that salary tends to increase slightly as age increases, although age alone is not a strong predictor of salary.

---

## Outlier Detection

Outliers were identified using boxplots and the Interquartile Range (IQR) method.

### Findings

- A salary value of **72,000** was identified as a significant outlier.
- Potential age outliers were observed at the extreme ends of the age distribution.

These outliers may influence statistical measures such as the mean and correlation coefficient.

---

## Visualizations Included

- Pearson Correlation Heatmap
- Boxplot for Age
- Boxplot for Salary
- Scatter Plot (optional) showing the relationship between Age and Salary

---

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Conclusion

This project highlights the importance of data cleaning before performing analysis. After preprocessing, the Pearson correlation heatmap revealed a weak positive relationship between Age and Salary. Outlier detection further identified unusual values that may require additional investigation.

Overall, the project demonstrates how data cleaning and visualization improve data reliability and support better decision-making.

---

## How to Run the Project

```python
pip install pandas numpy matplotlib seaborn
```

Run the Python script or Jupyter Notebook to:

1. Load the dataset
2. Clean and preprocess the data
3. Generate the Pearson correlation heatmap
4. Detect and visualize outliers

---

## Author

Gurjeet Kaur
