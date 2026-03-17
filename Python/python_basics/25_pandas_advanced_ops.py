"""
25_pandas_advanced_ops.py

Advanced Pandas Operations:
- Merging/Joining: Combining dataframes based on keys (similar to SQL).
- Grouping: Aggregating data based on categories.
- Sorting: Ordering data.
- Shuffling: Randomizing order (useful for ML training).
"""

import pandas as pd
import numpy as np

# Sample Data
users = pd.DataFrame({
    'UserID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'UserID': [1, 2, 1, 5],  # Note: UserID 5 exists here but not in users (for join demo)
    'Amount': [250, 150, 300, 200]
})

print("Users Table:")
print(users)
print("\nOrders Table:")
print(orders)

# 1. Merging / Joining
print("\n--- Merging / Joining ---")
# Inner Join: Only records that match in both
merged_inner = pd.merge(users, orders, on='UserID', how='inner')
print("Inner Join:\n", merged_inner)

# Left Join: All users, and their orders if any
merged_left = pd.merge(users, orders, on='UserID', how='left')
print("\nLeft Join:\n", merged_left)

# Outer Join: All records from both
merged_outer = pd.merge(users, orders, on='UserID', how='outer')
print("\nOuter Join:\n", merged_outer)

# 2. Grouping
print("\n--- Grouping ---")
# Calculate total amount spent by each user
# using the inner merged table for valid users
user_spend = merged_inner.groupby('Name')['Amount'].sum().reset_index()
print("Total Spend per User:\n", user_spend)

# Multiple aggregations
agg_stats = merged_inner.groupby('UserID').agg({
    'Amount': ['sum', 'mean', 'count'],
    'OrderID': 'count'
})
print("\nDetailed Aggregations:\n", agg_stats)

# 3. Sorting
print("\n--- Sorting ---")
# Sort by Amount Descending
sorted_orders = merged_inner.sort_values(by='Amount', ascending=False)
print("Orders sorted by Amount (Desc):\n", sorted_orders)

# 4. Shuffling
print("\n--- Shuffling ---")
# frac=1 means return 100% of the rows, just randomized
shuffled_users = users.sample(frac=1, random_state=42).reset_index(drop=True)
print("Shuffled Users:\n", shuffled_users)
