"""
05_tuples.py

Tuples:
- Ordered collection of items.
- Immutable (CANNOT be changed once created).
- Generally faster than lists.
- Used for fixed data or heterogeneous data.
- Defined using parentheses ().
"""

# Creating a tuple
point = (10, 20)
print(f"Point: {point}")

# Accessing elements
print(f"X coordinate: {point[0]}")
print(f"Y coordinate: {point[1]}")

# Immutability demo
try:
    point[0] = 5
except TypeError as e:
    print(f"\nError demonstration: {e}")
    print("Tuples cannot be modified!")

# Unpacking tuples
x, y = point
print(f"\nUnpacked: x={x}, y={y}")

# Single element tuple (needs a comma)
single_element = (1,) 
print(f"Single element tuple type: {type(single_element)}")

# Tuples can contain mutable objects (like lists)
mixed_tuple = (1, [2, 3], 4)
print(f"\nMixed Tuple: {mixed_tuple}")
mixed_tuple[1].append(99) # The list inside is mutable, but the tuple structure isn't
print(f"Modified list inside tuple: {mixed_tuple}")
