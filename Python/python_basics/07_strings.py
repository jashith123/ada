"""
07_strings.py

Strings:
- Sequences of characters.
- Immutable.
- Enclosed in single ' ', double " ", or triple ''' ''' / """ """ quotes.
"""

# Creating strings
s1 = "Hello"
s2 = 'World'
s3 = """This is a
multiline string."""

print(f"{s1} {s2}")

# String Operations
full_greeting = s1 + " " + s2
print(f"Concatenation: {full_greeting}")

print(f"Repetition: {'Ha' * 3}")    # HaHaHa

# Accessing characters and Slicing
print(f"First character of '{s1}': {s1[0]}")
print(f"Slice '{s1[0:3]}': {s1[:3]}")

# Common String Methods
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Strip (remove whitespace): '{text.strip()}'")
print(f"Replace: '{text.replace('Python', 'Java')}'")
print(f"Split: {text.split()}") # Returns a list

# String Formatting (f-strings - Python 3.6+)
name = "Bob"
age = 25
print(f"\nMy name is {name} and I am {age} years old.")
