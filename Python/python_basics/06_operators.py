"""
06_operators.py

Operators:
Symbols used to perform operations on variables and values.
"""

a = 10
b = 3

print(f"a = {a}, b = {b}")

# 1. Arithmetic Operators
print("\nArithmetic Operators:")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")       # Returns float
print(f"Floor Division (a // b): {a // b}") # Returns integer (quotient)
print(f"Modulus (a % b): {a % b}")         # Remainder
print(f"Exponentiation (a ** b): {a ** b}") # Power

# 2. Comparison Operators (Return True/False)
print("\nComparison Operators:")
print(f"Equal (a == b): {a == b}")
print(f"Not Equal (a != b): {a != b}")
print(f"Greater than (a > b): {a > b}")

# 3. Logical Operators
print("\nLogical Operators:")
x = True
y = False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 4. Assignment Operators
print("\nAssignment Operators:")
c = 5
c += 2 # Same as c = c + 2
print(f"c += 2 -> {c}")

# 5. Membership Operators
print("\nMembership Operators:")
lst = [1, 2, 3]
print(f"2 in lst: {2 in lst}")
print(f"5 not in lst: {5 not in lst}")

# 6. Identity Operators
print("\nIdentity Operators:")
list1 = [1, 2]
list2 = [1, 2]
list3 = list1
print(f"list1 is list2: {list1 is list2}")   # False (different objects in memory)
print(f"list1 is list3: {list1 is list3}")   # True (same object reference)
print(f"list1 == list2: {list1 == list2}")   # True (same value)
