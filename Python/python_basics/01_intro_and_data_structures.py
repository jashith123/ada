"""
01_intro_and_data_structures.py

Introduction to Python:
Python is a high-level, interpreted programming language known for its readability 
and versatility. It supports multiple programming paradigms, including procedural, 
object-oriented, and functional programming.

Key features:
- Easy to learn and read
- Dynamic typing (no need to declare variable types)
- Huge standard library
- Interpreted (runs line by line)

Data Structures Overview:
Python has several built-in data structures to store collections of data:
1. Lists: Ordered, mutable sequences.
2. Tuples: Ordered, immutable sequences.
3. Sets: Unordered collections of unique elements.
4. Dictionaries: Key-value pairs.
"""

# Basic Output
print("Hello, Python World!")

# Variables and Dynamic Typing
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True # Boolean

print(f"x: {x}, type: {type(x)}")
print(f"y: {y}, type: {type(y)}")
print(f"name: {name}, type: {type(name)}")

# Brief Data Structure Preview (Detailed in separate files)
my_list = [1, 2, 3]          # List
my_tuple = (1, 2, 3)         # Tuple
my_set = {1, 2, 3}           # Set
my_dict = {'key': 'value'}   # Dictionary

print("\nData Structures Preview:")
print(f"List: {my_list}")
print(f"Tuple: {my_tuple}")
print(f"Set: {my_set}")
print(f"Dictionary: {my_dict}")
