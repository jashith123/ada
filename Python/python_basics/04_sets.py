"""
04_sets.py

Sets:
- Unordered collection of unique elements.
- No duplicate members.
- Mutable (can add/remove items), but elements must be immutable.
- Useful for mathematical set operations (union, intersection, etc.).
- Defined using curly braces {} or set().
"""

# Creating a set
my_set = {1, 2, 3, 3, 4} # Duplicates are automatically removed
print(f"Set: {my_set}")

# Adding elements
my_set.add(5)
print(f"After adding 5: {my_set}")

# Removing elements
my_set.discard(2) # Removes 2 if present, doesn't raise error if not
print(f"After removing 2: {my_set}")

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union (elements in either set)
print(f"Union (A | B): {set_a | set_b}")

# Intersection (elements in both sets)
print(f"Intersection (A & B): {set_a & set_b}")

# Difference (elements in A but not in B)
print(f"Difference (A - B): {set_a - set_b}")

# Symmetric Difference (elements in either A or B, but not both)
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")
