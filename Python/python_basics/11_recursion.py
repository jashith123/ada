"""
11_recursion.py

Recursion:
- A function calling itself to solve a smaller instance of the problem.
- Must have a "base case" to stop the recursion.
"""

def factorial(n):
    """
    Calculates factorial of n recursively.
    n! = n * (n-1) * ... * 1
    """
    # Base Case: Stop when n is 1 or 0
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case: Call itself with n-1
    else:
        return n * factorial(n - 1)

number = 5
print(f"Factorial of {number} is: {factorial(number)}")

# Visualization of steps for factorial(3):
# factorial(3) -> 3 * factorial(2)
#                   -> 2 * factorial(1)
#                         -> 1 (Base case)
# Result: 3 * 2 * 1 = 6

def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    Seq: 0, 1, 1, 2, 3, 5, 8...
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = 6
print(f"\nFibonacci sequence at index {n_terms}: {fibonacci(n_terms)}")
