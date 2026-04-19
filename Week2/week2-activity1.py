# Import library
import pandas as pd

# Load dataset
df = pd.read_csv('data.csv')

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Column names and data types
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Total rows and columns
print("\nDataset Shape (Rows, Columns):")
print(df.shape)