"""
20_numpy_arrays.py

NumPy (Numerical Python):
- The fundamental package for scientific computing in Python.
- Provides support for large, multi-dimensional arrays and matrices.
- Much faster than standard Python lists.

To install: pip install numpy
"""

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please install it using: pip install numpy")
    exit()

print(f"NumPy Version: {np.__version__}")

# 1. Creating Arrays
print("\n--- Creating Arrays ---")
arr0 = np.array(42) # 0-D Array (Scalar)
arr1 = np.array([1, 2, 3, 4, 5]) # 1-D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D Array (Matrix)

print(f"1-D Array: {arr1}")
print(f"2-D Array:\n{arr2}")

# 2. Dimensions & Shape
print("\n--- Shape and Dimensions ---")
print(f"arr2 dimensions (ndim): {arr2.ndim}")
print(f"arr2 shape: {arr2.shape}") # (rows, columns)

# 3. Indexing & Slicing
print("\n--- Indexing & Slicing ---")
print(f"Element at row 0, col 1: {arr2[0, 1]}") # Accessing [row, col]
print(f"Slice 1-D (index 1 to 4): {arr1[1:4]}")
print(f"Slice 2-D (row 1, elements 1 to end): {arr2[1, 1:]}")

# 4. Reshaping
print("\n--- Reshaping ---")
# Convert 1-D array with 12 elements into a 4x3 matrix
arr_large = np.arange(12) # Creates array [0, 1, ... 11]
new_arr = arr_large.reshape(4, 3) 
print(f"Original: {arr_large}")
print(f"Reshaped (4x3):\n{new_arr}")

# Flattening (Multi-D to 1-D)
flattened = new_arr.reshape(-1)
print(f"Flattened back: {flattened}")

# 5. Iterating
print("\n--- Iterating ---")
print("Iterating over 2-D array (prints rows):")
for x in arr2:
    print(x)

print("Iterating over each scalar element (nditer):")
for x in np.nditer(arr2):
    print(x, end=" ")
print()
