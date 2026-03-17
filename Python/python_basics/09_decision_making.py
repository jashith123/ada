"""
09_decision_making.py

Decision Making:
- Control flow using if, elif, else statements.
- Executes code blocks based on conditions (True/False).
"""

age = 20

# Basic If-Else
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Elif Ladder
score = 85

print(f"\nScore: {score}")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Nested If
num = 15
if num > 0:
    print("\nPositive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# Ternary Operator (One-line if-else)
status = "Pass" if score >= 50 else "Fail"
print(f"Status: {status}")
