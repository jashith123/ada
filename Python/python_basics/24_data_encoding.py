"""
24_data_encoding.py

Data Encoding:
- Categorical and Continuous Values.
- Encoding: Transforming data into a format suitable for algorithms.

Techniques:
1. Encoding Continuous: Binning, Scaling (Standardization/Normalization).
2. Categorical Dummy Encoding (One-Hot).
3. Target Encoding (Mean Encoding).
"""

import pandas as pd
import numpy as np

# Sample Data
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Score': [55, 90, 85, 40, 95, 60],     # Continuous
    'City': ['NY', 'LA', 'NY', 'Chicago', 'LA', 'Chicago'], # Categorical
    'Pass': [0, 1, 1, 0, 1, 0]             # Target Variable
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# --- 1. Encoding Continuous Values ---
print("\n--- 1. Encoding Continuous Values ---")

# A. Binning (Discretization)
# Converting continuous 'Score' into categories 'Low', 'Medium', 'High'
bins = [0, 60, 85, 100]
labels = ['Low', 'Medium', 'High']
df['Score_Binned'] = pd.cut(df['Score'], bins=bins, labels=labels)
print("Binning (cut):")
print(df[['Score', 'Score_Binned']])

# B. Scaling (Normalization / Standardization)
# Manual Standardization: (x - mean) / std
df['Score_Scaled'] = (df['Score'] - df['Score'].mean()) / df['Score'].std()
print("\nStandardized Score:")
print(df[['Score', 'Score_Scaled']])


# --- 2. Encoding Categorical Values as Dummies (One-Hot) ---
print("\n--- 2. Dummy Encoding (One-Hot) ---")
# Converts 'City' into 'City_Chicago', 'City_LA', 'City_NY'
# drop_first=True removes one column to avoid dummy variable trap (multicollinearity)
df_dummies = pd.get_dummies(df, columns=['City'], drop_first=False, prefix='City')
print(df_dummies.head())


# --- 3. Target Encoding ---
# Replacing a categorical value with the mean of the target variable for that category.
# Dangerous if not done correctly (data leakage), usually done on training split only.
print("\n--- 3. Target Encoding ---")

# Calculate mean target ('Pass') for each city
target_means = df.groupby('City')['Pass'].mean()
print("Target Means per City:")
print(target_means)

# Map the means back to the dataframe
df['City_Target_Encoded'] = df['City'].map(target_means)

print("\nDataFrame with Target Encoded City:")
print(df[['City', 'Pass', 'City_Target_Encoded']])

# Note: In 'NY', 1 pass, 1 fail -> 50% (0.5)
# In 'LA', 2 pass, 0 fail -> 100% (1.0)
# In 'Chicago', 0 pass, 2 fail -> 0% (0.0)
