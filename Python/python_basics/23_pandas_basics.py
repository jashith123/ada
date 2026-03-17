"""
23_pandas_basics.py

Pandas:
- Powerful data manipulation and analysis tool.
- Built on top of NumPy.
- Key structure: DataFrame (Rows and Columns).

To install: pip install pandas
"""

import pandas as pd
import numpy as np

# 1. creating a DataFrame
print("--- Creating DataFrame ---")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, np.nan, 35, 200, 28],  # np.nan is a missing value, 200 is an outlier
    'Salary': [50000, 60000, 70000, 55000, 62000],
    'City': ['NY', 'LA', 'NY', 'Chicago', 'LA']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Handling Missing Values
print("\n--- Missing Values ---")
print(f"Checking for nulls:\n{df.isnull().sum()}")

# Methods to handle:
# df.dropna() - removes rows with nulls
# df.fillna(value) - fills nulls with value
df['Age'] = df['Age'].fillna(df['Age'].mean()) # Impute with mean
print("\nDataFrame after filling missing Age:")
print(df)

# 3. Handling Outliers
print("\n--- Handling Outliers ---")
# Simple IQR method
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Age Outlier Bounds: {lower_bound} to {upper_bound}")
# Filtering out outliers
df_clean = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]
print("DataFrame without outliers:")
print(df_clean)

# 4. Dropping Fields
print("\n--- Dropping Fields ---")
df_dropped = df.drop(columns=['City'])
print(df_dropped)

# 5. Concatenating Rows and Columns
print("\n--- Concatenation ---")
new_row = pd.DataFrame({'Name': ['Frank'], 'Age': [40], 'Salary': [80000], 'City': ['Boston']})
# Row concat
df_concat_row = pd.concat([df, new_row], ignore_index=True)

# Col concat
dummy_col = pd.DataFrame({'Department': ['HR', 'IT', 'IT', 'Sales', 'HR']})
df_concat_all = pd.concat([df, dummy_col], axis=1) # Axis 1 = Columns

print("Concatenated DataFrame:")
print(df_concat_all)

# 6. Training and Validation Split (Manual)
print("\n--- Train/Validation Split ---")
# Randomly sample 80% for training
train_df = df.sample(frac=0.8, random_state=42)
# Drop the training indices from original to get validation set
val_df = df.drop(train_df.index)

print(f"Train Shape: {train_df.shape}")
print(f"Validation Shape: {val_df.shape}")

# 7. DataFrame to Matrix
print("\n--- DataFrame to Matrix ---")
matrix = df.values # or df.to_numpy()
print(matrix)

# 8. File I/O - Pickle and CSV
print("\n--- File I/O ---")
# CSV
df.to_csv('temp_data.csv', index=False)
print("Saved to temp_data.csv")

# Pickle (Serializes the python object to binary)
# Good for preserving exact data types
df.to_pickle('temp_data.pkl')
print("Saved to temp_data.pkl")

df_loaded = pd.read_pickle('temp_data.pkl')
print("Loaded from Pickle validation:", df_loaded.shape)

# 9. Styling (CSS)
# Pandas allows styling DataFrames for HTML output (like in Jupyter Notebooks)
# This doesn't show in terminal, but the code is valid.
# Example: Highlight maximum values
styled_df = df.style.highlight_max(axis=0)
print("\n(Styled DataFrame object created - useful for Jupyter/HTML export)")
