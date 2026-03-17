"""
21_numpy_manipulation.py

NumPy Array Manipulation:
- Joining: Putting contents of two or more arrays in a single array.
- Splitting: Breaking one array into multiple.
- Searching: Finding indices of values.
- Sorting: Ordering elements.
- Filtering: Getting some elements out of an existing array.
"""

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install it using: pip install numpy")
    exit()

# 1. Joining Arrays
print("--- Joining Arrays ---")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate (Joins along an axis)
arr_concat = np.concatenate((arr1, arr2))
print(f"Concatenated 1D: {arr_concat}")

# Stacking (Joins along a new axis)
arr_stack = np.stack((arr1, arr2), axis=1)
print(f"Stacked along axis 1:\n{arr_stack}")

# 2. Splitting Arrays
print("\n--- Splitting Arrays ---")
arr = np.array([1, 2, 3, 4, 5, 6])
new_arrays = np.array_split(arr, 3) # Split into 3 parts
print(f"Original: {arr}")
print(f"Split into 3: {new_arrays[0]}, {new_arrays[1]}, {new_arrays[2]}")

# 3. Searching Arrays
print("\n--- Searching Arrays ---")
# where() returns indices where condition is true
x = np.where(arr == 4)
print(f"Index where value is 4: {x}")

y = np.where(arr % 2 == 0)
print(f"Indices where tuple is even: {y}")

# searchsorted() performs binary search on sorted arrays
sorted_arr = np.array([6, 7, 8, 9])
x = np.searchsorted(sorted_arr, 7)
print(f"Index to insert 7 to maintain order in {sorted_arr}: {x}")

# 4. Sorting Arrays
print("\n--- Sorting Arrays ---")
unsorted = np.array([3, 2, 0, 1])
print(f"Original: {unsorted}")
print(f"Sorted: {np.sort(unsorted)}")

# 5. Filtering Arrays
print("\n--- Filtering ---")
arr = np.array([41, 42, 43, 44])
# Create a boolean index list
filter_arr = arr > 42 # [False, False, True, True]
new_arr = arr[filter_arr]

print(f"Original: {arr}")
print(f"Filter (x > 42): {new_arr}")
