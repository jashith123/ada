"""
14_exception_handling.py

Exception Handling:
- Managing errors gracefully so the program doesn't crash.
- Blocks: try, except, else, finally.
"""

print("--- Basic Exception Handling ---")

try:
    # Code that might raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    # Code that runs if the specific exception occurs
    print("Error: Cannot divide by zero!")
except Exception as e:
    # Code that runs for any other exception
    print(f"An unexpected error occurred: {e}")

print("\n--- Try-Except-Else-Finally ---")
def calculate_inverse(number):
    try:
        val = int(number)
        res = 1 / val
    except ValueError:
        print("Error: Input must be a number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero (infinity).")
    else:
        # Runs ONLY if NO exception occurs
        print(f"Inverse of {number} is {res}")
    finally:
        # Runs ALWAYS (whether an exception occurred or not)
        print("Execution of calculate_inverse complete.\n")

calculate_inverse(5)
calculate_inverse(0)
calculate_inverse("abc")

print("--- Raising Exceptions ---")
def check_age(age):
    if age < 0:
        # Manually triggering an exception
        raise ValueError("Age cannot be negative.")
    print(f"Age {age} is valid.")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught expected error: {e}")
