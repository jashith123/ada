"""
17_file_handling_json.py

File Handling (JSON - JavaScript Object Notation):
- Using the `json` module to parse (decode) and generate (encode) JSON.
- Standard format for data exchange.
"""
import json

json_file = "example_data.json"

# Python Dictionary
data_dict = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "skills": ["Python", "Data Science", "Web Dev"],
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    }
}

print("--- Writing JSON ---")
with open(json_file, 'w') as file:
    # dump: writes python object to file as JSON
    # indent=4 makes it pretty-printed (human readable)
    json.dump(data_dict, file, indent=4)
    print(f"Data written to {json_file}")

print("\n--- Reading JSON ---")
with open(json_file, 'r') as file:
    # load: reads JSON from file into a python object
    loaded_data = json.load(file)
    print("Loaded Data Type:", type(loaded_data))
    print("Content:", loaded_data)

print("\n--- Accessing Nested Data ---")
print(f"City: {loaded_data['address']['city']}")
print(f"First Skill: {loaded_data['skills'][0]}")

print("\n--- JSON String Conversion ---")
# dumps (dump string): To get JSON string without writing to file
json_str = json.dumps(data_dict) 
print(f"JSON String: {json_str[:50]}...")
