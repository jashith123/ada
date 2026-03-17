# Use a Python dictionary employees to represent employee salary details and perform the following tasks:

# 1.    Populate the dictionary employees with at least 10 employees, where the key is the employee ID and the value is the salary.
employees = {
    "1": 50000,
    "2": 60000,
    "3": 70000,
    "4": 80000,
    "5": 90000,
    "6": 100000,
    "7": 110000,
    "8": 120000,
    "9": 130000,
    "10": 140000
}
# 2.    Display the complete dictionary.
print(employees)
# 3.    Display the salary of a specific employee using the employee ID.
print(employees["1"])
# 4.    Display all employee IDs present in the dictionary.
print(employees.keys())
# 5.    Display all salary values present in the dictionary.
print(employees.values())
# 6.    Find and display the total number of employees using len().
print(len(employees))
# 7.    Add the salary details of a new employee to the dictionary.
employees["11"] = 150000
print(employees)
# 8.    Update the salary of an existing employee.
employees["1"] = 55000
print(employees)
# 9.    Remove an employee record using the del statement.
del employees["1"]
print(employees)
# 10.    Remove and display the last inserted employee record using popitem().
print(employees.popitem())
# 11.    Traverse the dictionary using a for loop to display employee IDs and salaries.
for key, value in employees.items():
    print(key, value)
# 12.    Search for a given employee ID and display the corresponding salary.
print(employees.get("2"))
# 13.    Check whether a given employee ID exists in the dictionary using the in operator.
print("2" in employees)
# 14.    Count and display the number of employees whose salary is greater than a specified value.
count = 0
for value in employees.values():
    if value > 100000:
        count += 1
print(count)
# 15.    Find and display the maximum and minimum salary from the dictionary values.
print(max(employees.values()))
print(min(employees.values()))
# 16.    Find and display the total and average salary of all employees.
print(sum(employees.values()))
print(sum(employees.values()) / len(employees))
# 17.    Create a copy of the dictionary using the copy() method.
employees_copy = employees.copy()
print(employees_copy)   
# 18.    Demonstrate the difference between assignment and copying of dictionaries.

# Assignment (same object)
dict1 = {"a": 1}
dict2 = dict1
dict2["a"] = 99
print(dict1)  # Output: {'a': 99}

# Copy (new object)
dict3 = {"a": 1}
dict4 = dict3.copy()
dict4["a"] = 99
print(dict3)  # Output: {'a': 1}

# 19.    Create a nested dictionary to store employee details such as {ID: {Name, Department, Salary}}.
employees_nested = {
    "1": {"Name": "John", "Department": "HR", "Salary": 50000},
    "2": {"Name": "Jane", "Department": "HR", "Salary": 60000},
    "3": {"Name": "Bob", "Department": "HR", "Salary": 70000},
    "4": {"Name": "Alice", "Department": "HR", "Salary": 80000},
    "5": {"Name": "Mike", "Department": "HR", "Salary": 90000},
    "6": {"Name": "Sarah", "Department": "HR", "Salary": 100000},
    "7": {"Name": "Tom", "Department": "HR", "Salary": 110000},
    "8": {"Name": "Emily", "Department": "HR", "Salary": 120000},
    "9": {"Name": "David", "Department": "HR", "Salary": 130000},
    "10": {"Name": "Lisa", "Department": "HR", "Salary": 140000}
}
# 20.    Display complete details of all employees from the nested dictionary.
print(employees_nested)
# 21.    Extract and display only employee names from the nested dictionary.
print([value["Name"] for value in employees_nested.values()])
# 22.    Extract and display only salary values from the nested dictionary.
print([value["Salary"] for value in employees_nested.values()])
# 23.    Convert all salaries into a new dictionary containing only employees with salary above the average salary.
greater_than_average = {
    key: value for key, 
    value in employees.items() if value > sum(employees.values()) / len(employees)
}
print(greater_than_average) 
# 24.    Use the get() method to safely access the salary of a given employee ID.
print(employees.get("2"))
# 25.    Compare dictionaries with lists and tuples with respect to data organization and access efficiency.

# List Example
students = ["Rahul", "Aman", "Priya"]
print("First student:", students[0])

# Tuple Example
coordinates = (10, 20)
print("X coordinate:", coordinates[0])

# Dictionary Example
student = {
    "name": "Rahul",
    "age": 20,
    "course": "CSE"
}
print("Student name:", student["name"])

numbers = [10, 20, 30, 40, 50]

print(numbers[3])  # Direct index access

# Searching for 40
for num in numbers:
    if num == 40:
        print("Found")

marks = {
    "Math": 90,
    "Physics": 85,
    "Chemistry": 88
}

print(marks["Physics"])   # Direct key access

students = [
    ["Rahul", 20],
    ["Aman", 21],
    ["Priya", 19]
]

# Searching age of Aman
for s in students:
    if s[0] == "Aman":
        print("Age:", s[1])

students = {
    "Rahul": 20,
    "Aman": 21,
    "Priya": 19
}

print("Age:", students["Aman"])