print("Hello, World!")

x = 10              # Integer
y = 3.14            # Float
name = "Jashith"    # String
is_active = True    # Boolean
complex_num = 10+3j # Complex

print(f"x: {x}, type: {type(x)}")
print(f"y: {y}, type: {type(y)}")
print(f"name: {name}, type: {type(name)}")
print(f"is_active: {is_active}, type: {type(is_active)}")
print(f"complex_num: {complex_num}, type: {type(complex_num)}")

# Python Local Variables

def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))

# Python Global Variables

x = 5
y = 10

def sum():
   sum = x + y
   return sum
print(sum())

a = 10
b = 3

print(f"a = {a}, b = {b}")

# 1. Arithmetic Operators
print("\nArithmetic Operators:")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulus (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# 2. Comparison Operators (Return True/False)
print("\nComparison Operators:")
print(f"Equal (a == b): {a == b}")
print(f"Not Equal (a != b): {a != b}")
print(f"Greater than (a > b): {a > b}")
print(f"Less than (a < b): {a < b}")
print(f"Greater than or equal to (a >= b): {a >= b}")
print(f"Less than or equal to (a <= b): {a <= b}")

# 3. Logical Operators
print("\nLogical Operators:")
var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not (var > 3 and var < 10))

# 4. Assignment Operators
print("\nAssignment Operators:")
c = 5
c += 2
print(f"c += 2 -> {c}")
c -= 2
print(f"c -= 2 -> {c}")
c *= 2
print(f"c *= 2 -> {c}")
c /= 2
print(f"c /= 2 -> {c}")
c //= 2
print(f"c //= 2 -> {c}")
c %= 2
print(f"c %= 2 -> {c}")
c **= 2
print(f"c **= 2 -> {c}")

# 5. Bitwise Operators
print("\nBitwise Operators:")

# Bitwise AND Operator
print("\nBitwise AND Operator:")
print(f"a & b: {a & b}")

# Bitwise OR Operator
print("\nBitwise OR Operator:")
print(f"a | b: {a | b}")

# Bitwise XOR Operator
print("\nBitwise XOR Operator:")
print(f"a ^ b: {a ^ b}")

# Bitwise NOT Operator
print("\nBitwise NOT Operator:")
print(f"~a: {~a}")

# Bitwise Left Shift Operator
print("\nBitwise Left Shift Operator:")
print(f"a << 2: {a << 2}")

# Bitwise Right Shift Operator
print("\nBitwise Right Shift Operator:")
print(f"a >> 2: {a >> 2}")