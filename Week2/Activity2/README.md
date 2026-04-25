# Beijing Multi-Site Air Quality Analysis

## Project Overview

This project performs a comprehensive statistical analysis of the Beijing Multi-Site Air Quality dataset. The dataset contains hourly air pollution and meteorological observations collected from multiple monitoring stations across Beijing between March 2013 and February 2017.

The analysis focuses on data cleaning, descriptive statistics, pollution comparison across stations, visualization, and correlation analysis to identify key environmental patterns and relationships.

---

## Dataset

- **Source:** Beijing Multi-Site Air Quality Dataset
- **Time Period:** March 1, 2013 to February 28, 2017
- **Data Type:** Hourly environmental observations
- **Stations:** Multiple monitoring stations across Beijing

### Key Variables

- **Pollutants:** PM2.5, PM10, SO2, NO2, CO, O3
- **Meteorological Factors:** Temperature (TEMP), Pressure (PRES), Dew Point (DEWP), Rainfall (RAIN), Wind Speed (WSPM)
- **Location:** Station name
- **Time Variables:** Year, Month, Day, Hour

---

## Objectives

1. Load and combine multiple station datasets.
2. Clean and preprocess the data.
3. Perform descriptive statistical analysis.
4. Compare average pollution levels across monitoring stations.
5. Visualize pollutant distributions.
6. Analyze correlations between pollutants and weather variables.

---

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab

---

## Methodology

### 1. Data Collection and Integration

- Uploaded multiple CSV files using Google Colab.
- Combined all station datasets into a single DataFrame using `pd.concat()`.

### 2. Data Cleaning

- Identified missing values.
- Replaced missing numerical values with column means.
- Removed duplicate records.

### 3. Statistical Analysis

- Generated descriptive statistics including:
  - Mean
  - Median
  - Minimum
  - Maximum
  - Standard Deviation

### 4. Station-Level Analysis

- Calculated average pollutant concentrations for each monitoring station.
- Compared air quality across different locations.

### 5. Data Visualization

- Created a histogram with kernel density estimation (KDE) for PM2.5 distribution.
- Developed a correlation heatmap for pollutants and meteorological variables.

### 6. Correlation Analysis

- Examined relationships between PM2.5 and other variables.
- Identified the strongest positive and negative correlations.

---

## Key Insights

- PM2.5 and PM10 show a strong positive correlation, indicating common pollution sources.
- Meteorological conditions significantly influence pollutant concentrations.
- Some stations consistently exhibit higher pollution levels than others.
- Wind speed generally shows a negative correlation with pollutant levels, suggesting improved air dispersion.

---

## Files Included

- `week2-activity2.ipynb` – Jupyter Notebook containing all analysis code.
- `README.md` – Project documentation.
- Visualizations and output screenshots.

---

## How to Run the Project

1. Open the notebook in Google Colab or Jupyter Notebook.
2. Upload all Beijing air quality CSV files when prompted.
3. Run all cells sequentially.
4. Review the generated statistical outputs and visualizations.

---

## Expected Outputs

- Combined dataset summary
- Missing value analysis
- Descriptive statistics table
- Station-wise pollution comparison
- PM2.5 distribution histogram
- Correlation heatmap
- PM2.5 correlation ranking

---

## Conclusion

This project provides valuable insights into Beijing's air quality patterns across multiple monitoring stations. By combining statistical analysis and visualization, it highlights pollution trends, station-specific variations, and the influence of meteorological factors on air quality.

The findings can support environmental monitoring, policy development, and public health decision-making.

---

## Author

Gurjeet Singh

## License

This project is intended for educational and academic purposes.
