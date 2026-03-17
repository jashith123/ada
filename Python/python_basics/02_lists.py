"""
02_lists.py

Lists:
- Ordered collection of items.
- Mutable (items can be changed, added, or removed).
- Allows duplicate elements.
- Defined using square brackets [].
"""

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")

# Accessing elements (0-indexed)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing

# Modifying elements
fruits[1] = "blueberry"
print(f"Modified list: {fruits}")

# Adding elements
fruits.append("date")       # Adds to the end
fruits.insert(1, "apricot") # Inserts at index 1
print(f"After adding elements: {fruits}")

# Removing elements
removed_item = fruits.pop() # Removes the last item
print(f"Popped item: {removed_item}")
fruits.remove("apple")      # Removes first occurrence of "apple"
print(f"After removing 'apple': {fruits}")

# Slicing lists [start:end:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Slice [2:6]: {numbers[2:6]}")
print(f"Reverse: {numbers[::-1]}")

# List Comprehension (A concise way to create lists)
squares = [x**2 for x in range(5)]
print(f"Squares (List Comprehension): {squares}")
