"""
15_file_handling_text.py

File Handling (Text):
- Operations: Open, Read, Write, Append, Close.
- Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write).
- Best Practice: Use `with` statement (automatically closes the file).
"""

filename = "example_text.txt"

# 1. Writing to a file (Overwrites if exists)
print(f"--- Writing to {filename} ---")
with open(filename, 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a text file.\n")
    file.write("Python file handling is easy.")

# 2. Reading from a file
print(f"\n--- Reading from {filename} ---")
with open(filename, 'r') as file:
    content = file.read() # Reads the entire content
    print(content)

# 3. Reading line by line
print(f"\n--- Reading Line by Line ---")
with open(filename, 'r') as file:
    for line in file:
        print(f"Line: {line.strip()}") # strip() removes the newline character

# 4. Appending to a file
print(f"\n--- Appending to {filename} ---")
with open(filename, 'a') as file:
    file.write("\nAppending a new line at the end.")

# Verify append
with open(filename, 'r') as file:
    print(file.read())
