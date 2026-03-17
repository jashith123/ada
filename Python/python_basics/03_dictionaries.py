"""
03_dictionaries.py

Dictionaries:
- Unordered (ordered in Python 3.7+) collection of key-value pairs.
- Keys must be unique and immutable (strings, numbers, tuples).
- Mutable (values can be changed).
- Defined using curly braces {}.
"""

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Original Dictionary: {person}")

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}") # Safer access using .get()

# Modifying values
person["age"] = 31
print(f"Updated Age: {person}")

# Adding new key-value pairs
person["job"] = "Engineer"
print(f"Added Job: {person}")

# Removing items
job = person.pop("job")
print(f"Popped Job: {job}")
del person["city"]
print(f"After deleting city: {person}")

# Iterating through dictionaries
print("\nIterating:")
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
squares_dict = {x: x**2 for x in range(1, 4)}
print(f"\nDictionary Comprehension: {squares_dict}")
