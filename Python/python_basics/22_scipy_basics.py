"""
22_scipy_basics.py

SciPy (Scientific Python):
- Built on NumPy.
- Used for scientific/technical computing.
- Modules for optimization, linear algebra, integration, interpolation, etc.

To install: pip install scipy
"""

try:
    import numpy as np
    from scipy import linalg, optimize, interpolate
except ImportError:
    print("SciPy/NumPy not installed. Install via: pip install numpy scipy")
    exit()

# 1. Linear Algebra
# SciPy linalg contains all functions in numpy.linalg plus more, and is often faster.
print("--- Linear Algebra (scipy.linalg) ---")

# Making a square matrix
A = np.array([[1, 2], [3, 4]])
print(f"Matrix A:\n{A}")

# Calculating Determinant
det = linalg.det(A)
print(f"Determinant of A: {det}")

# Solving Linear Equations
# System:
# x + 2y = 5
# 3x + 4y = 6
B = np.array([[5], [6]])
solution = linalg.solve(A, B)
print(f"Solution to Ax=B (x, y): \n{solution}")


# 2. Optimization
# Finding the minimum value of a function
print("\n--- Optimization (scipy.optimize) ---")

def equation(x):
    return x**2 + x + 2

# Minimize the equation using 'BFGS' algorithm
mymin = optimize.minimize(equation, 0, method='BFGS')
print(f"Minimum value of x^2 + x + 2 is found at x = {mymin.x}")


# 3. Interpolation
# Generating new data points within the range of a discrete set of known data points.
print("\n--- Interpolation (scipy.interpolate) ---")

# Known points
x = np.arange(0, 10)
y = np.exp(-x/3.0) # Exponential decay curve

# Interpolation function (Creates a function f where y = f(x))
f = interpolate.interp1d(x, y, kind='linear')

# Predict value at x = 2.5 (which wasn't in original x)
x_new = 2.5
y_new = f(x_new)

print(f"Known x: {x}")
print(f"Interpolated value at x=2.5: {y_new}")
