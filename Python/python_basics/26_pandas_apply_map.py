"""
26_pandas_apply_map.py

Pandas Apply vs Map:
- Map: Used for substituting each value in a Series with another value. Works element-wise on Series.
- Apply: Used to apply a function along an axis of the DataFrame or on values of a Series.

Feature Engineering:
- Creating new features from existing ones using these functions.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Dept': ['HR', 'IT', 'IT', 'Sales'],
    'Salary': [50000, 60000, 65000, 55000],
    'JoinDate': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-11-01']
})

print("Original DataFrame:")
print(df)

# --- 1. Map (Series only) ---
print("\n--- Map ---")
# Using a dictionary to map values
dept_codes = {'HR': 1, 'IT': 2, 'Sales': 3}
# Creating a new feature 'DeptCode'
df['DeptCode'] = df['Dept'].map(dept_codes)
print(df[['Dept', 'DeptCode']])


# --- 2. Apply (Series) ---
print("\n--- Apply on Series ---")
# Applying a custom function to a column
def calculate_tax(salary):
    if salary > 60000:
        return salary * 0.2  # 20% tax
    else:
        return salary * 0.1  # 10% tax

df['Tax'] = df['Salary'].apply(calculate_tax) # New Feature
print(df[['Salary', 'Tax']])

# Using Lambda with apply
df['Salary_Doubled'] = df['Salary'].apply(lambda x: x * 2)
print("Salary Doubled (Top 2):\n", df[['Salary', 'Salary_Doubled']].head(2))


# --- 3. Apply (DataFrame - Row-wise) ---
print("\n--- Apply on DataFrame (Row-wise) ---")
# Feature Engineering involving multiple columns
# Calculate 'TotalCost' = Salary + Tax
# axis=1 means apply function to each ROW
df['TotalCost'] = df.apply(lambda row: row['Salary'] + row['Tax'], axis=1)
print(df[['Employee', 'Salary', 'Tax', 'TotalCost']])


# --- 4. Advanced Feature Engineering Example ---
print("\n--- Advanced Feature Engineering ---")
# Extracting Year from Date string
def extract_year(date_str):
    return date_str.split('-')[0]

df['JoinYear'] = df['JoinDate'].apply(extract_year)

# Calculating Tenure (assuming current year is 2025)
current_year = 2025
# Convert column to int first
df['Tenure'] = current_year - df['JoinYear'].astype(int)

print("Final DataFrame with New Features:")
print(df[['Employee', 'JoinDate', 'JoinYear', 'Tenure']])
