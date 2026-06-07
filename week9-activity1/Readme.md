# Fitness App User Data Clustering Analysis

## Project Overview

This project analyzes user activity data from a fitness application using data preprocessing and unsupervised machine learning techniques. The goal is to identify meaningful user groups based on workout habits and activity levels through clustering analysis.

---

## Dataset

**File:** `Fitness_App_User_Data.xlsx`

The dataset contains fitness-related user information, including:

- Age
- Workouts per Week
- Average Session Duration (Minutes)
- Steps per Day

---

## Objectives

1. Perform data cleaning and preprocessing.
2. Handle missing values and duplicate records.
3. Select appropriate features for clustering.
4. Apply K-Means clustering.
5. Determine the optimal number of clusters.
6. Interpret and visualize cluster characteristics.
7. Present findings through visualizations and presentation slides.

---

## Data Cleaning Process

The following preprocessing steps were performed:

- Loaded the dataset using Pandas.
- Checked for missing values.
- Checked for duplicate records.
- Verified data types for all columns.
- Confirmed data consistency before analysis.

### Results

- Missing Values: 0
- Duplicate Records: 0
- No data type corrections were required.

---

## Clustering Methodology

### Feature Selection

The following features were selected for clustering:

- Age
- Workouts_per_Week
- Avg_Session_Duration_Min
- Steps_per_Day

### Feature Scaling

All selected features were standardized using StandardScaler to ensure equal contribution during clustering.

### Clustering Algorithm

K-Means Clustering was applied to segment users into groups with similar fitness behaviors.

### Optimal Cluster Selection

The Silhouette Score method was used to evaluate cluster quality for different values of K.

The highest silhouette score indicated:

**Optimal Number of Clusters (K) = 4**

---

## Cluster Insights

### Cluster 0

- Younger users
- Lower workout frequency
- Lower daily step count

### Cluster 1

- Older users
- Lower workout frequency
- Higher daily activity levels

### Cluster 2

- Highly active younger users
- Frequent workouts
- High daily step counts

### Cluster 3

- Active older users
- Consistent workouts
- Moderate daily activity

---

## Visualizations

The project includes:

1. Silhouette Score Analysis
2. Cluster Distribution Scatter Plot
3. Cluster Summary Statistics

---

## Project Structure

```text
Fitness-App-Clustering/
│
├── Fitness_App_User_Data.xlsx
├── Fitness_App_Clustering_Analysis.ipynb
├── Fitness_App_Clustering_Presentation.pptx
├── Readme.md
└── requirements.txt
```

Install required packages:

```bash
pip install -r requirements.txt
```

## Required Libraries

```text
pandas
numpy
scikit-learn
matplotlib
openpyxl
jupyter
```

## Running the Project

Run the Jupyter Notebook:

```bash
jupyter notebook Fitness_App_Clustering_Analysis.ipynb
```

## Results

The analysis successfully segmented users into four meaningful clusters based on fitness behavior patterns. These insights can help fitness app providers personalize recommendations, engagement strategies, and wellness programs for different user groups.

## Author

Prepared as part of the Fitness App User Data Clustering Analysis activity using Python, Pandas, Scikit-Learn, and Jupyter Notebook.
