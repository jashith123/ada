"""
08_functions.py

Functions:
- Blocks of reusable code.
- Defined using `def` keyword.
- Can accept parameters and return values.
"""

# Simple Function
def greet(name):
    """Note: This is a docstring describing the function."""
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)

# Function with Default Arguments
def power(base, exponent=2):
    return base ** exponent

print(f"2^2 (default): {power(2)}")
print(f"2^3 (explicit): {power(2, 3)}")

# Keyword Arguments
print(f"Keyword args: {power(exponent=3, base=4)}")

# *args (Arbitrary Positional Arguments)
# Useful when you don't know how many arguments will be passed
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum 10, 20: {sum_all(10, 20)}")

# **kwargs (Arbitrary Keyword Arguments)
def describe_pet(**kwargs):
    print("Pet Info:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

describe_pet(name="Rex", type="Dog", age=5)

# Lambda Functions (Anonymous functions)
add = lambda x, y: x + y
print(f"\nLambda Add (5+3): {add(5, 3)}")
