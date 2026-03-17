"""
19_dealing_with_addresses.py

Dealing with Addresses (File Paths and Directories):
- Manipulating file paths using `os.path` and `pathlib` (Modern).
- Handling paths across different Operating Systems (Windows vs Linux).
"""

import os
from pathlib import Path

print("--- Using os.path (Legacy/Traditional) ---")
current_dir = os.getcwd()
print(f"Current Working Directory: {current_dir}")

# Joining paths (Handles slashes automatically)
new_folder_path = os.path.join(current_dir, "data_folder")
print(f"Joined Path: {new_folder_path}")

# Checking existence
print(f"Does data_folder exist? {os.path.exists(new_folder_path)}")

# Getting filename and extension
sample_path = "/users/admin/docs/report.csv"
print(f"Basename: {os.path.basename(sample_path)}")  # report.csv
print(f"Dirname: {os.path.dirname(sample_path)}")    # /users/admin/docs
print(f"Split Ext: {os.path.splitext(sample_path)}") # ('.../report', '.csv')


print("\n--- Using pathlib (Modern - Recommended) ---")
# Path objects allow method chaining and are more intuitive
path_obj = Path(current_dir)
print(f"Path Object: {path_obj}")

# Creating new paths
data_path = path_obj / "data_folder" / "sub_folder" # Overloading / operator
print(f"Constructed Path: {data_path}")

# Checking file type
this_file = Path(__file__)
print(f"Is '{this_file.name}' a file? {this_file.is_file()}")
print(f"Parent directory: {this_file.parent}")
print(f"File Stem (no ext): {this_file.stem}")
print(f"File Extension: {this_file.suffix}")

# Globbing (Searching for files)
print("\nScanning for .py files in current folder:")
for py_file in path_obj.glob("*.py"):
    print(f" - {py_file.name}")
