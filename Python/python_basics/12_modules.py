"""
12_modules.py

Modules:
- A file containing Python code (functions, variables, classes).
- Used to organize code into separate files.
- Imported using `import` keyword.
- Python has a vast Standard Library of modules.
"""

# 1. Importing a Custom Module (created locally as my_utils.py)
import my_utils
# Or: from my_utils import greet_user, PI

print("--- Custom Module ---")
print(my_utils.greet_user("Developer"))
print(f"Value of PI from module: {my_utils.PI}")

calc = my_utils.Calculator()
print(f"Addition using module class: {calc.add(10, 5)}")


# 2. Importing Standard Library Modules
import math
import random
import datetime

print("\n--- Standard Library Modules ---")

# Math module
print(f"Square root of 16 (math): {math.sqrt(16)}")

# Random module
print(f"Random number (1-100): {random.randint(1, 100)}")

# Datetime module
current_time = datetime.datetime.now()
print(f"Current Time: {current_time}")

# 3. Module Aliasing
import platform as plt
print(f"\nSystem Platform: {plt.system()}")

# 4. listing directory using os module
import os
print(f"\nCurrent Directory: {os.getcwd()}")
