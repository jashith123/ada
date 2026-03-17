"""
10_loops.py

Loops:
- Repeat a block of code multiple times.
- Two main types: for loops and while loops.
"""

# 1. For Loops
# Used to iterate over a sequence (list, tuple, string, range).
print("--- For Loop over List ---")
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

print("\n--- For Loop with Range ---")
# range(start, stop, step) - stop is exclusive
for i in range(1, 6): # 1 to 5
    print(f"Count: {i}")

# 2. While Loops
# Repeats as long as a condition is True.
print("\n--- While Loop ---")
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1

# 3. Loop Control Statements
print("\n--- Break and Continue ---")
for i in range(10):
    if i == 3:
        print("Skipping 3 (continue)")
        continue # Skips the rest of code for current iteration
    if i == 6:
        print("Stopping at 6 (break)")
        break # Exits the loop completely
    print(i, end=" ")
print() # Newline

# 4. Else clause in loops
# Executed when the loop completes normally (not via break)
print("\n--- Loop with Else ---")
for i in range(3):
    print(i)
else:
    print("Loop finished successfully.")
