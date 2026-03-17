"""
16_file_handling_csv.py

File Handling (CSV - Comma Separated Values):
- Using the `csv` module to handle tabular data.
"""
import csv

csv_file = "example_data.csv"

# Data to write
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

print("--- Writing CSV ---")
# newline='' is recommended for csv module to prevent blank lines on Windows
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print(f"Data written to {csv_file}")

print("\n--- Reading CSV ---")
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n--- Reading CSV as Dictionary ---")
# Useful for accessing columns by name
with open(csv_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}.")
