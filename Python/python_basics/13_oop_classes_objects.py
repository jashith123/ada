"""
13_oop_classes_objects.py

Object-Oriented Programming (OOP):
- A programming paradigm based on "objects", which contain data (attributes) and code (methods).
- Key Concepts:
    1. Class: A blueprint for creating objects.
    2. Object: An instance of a class.
    3. Inheritance: A way to form new classes using classes that have already been defined.
    4. Encapsulation: Bundling data and methods, and restricting access to internal state.
    5. Polymorphism: The ability to use a common interface for multiple forms (data types).
"""

# 1. Defining a Class
class Dog:
    # Class Attribute (Shared by all instances)
    species = "Canis familiaris"

    # Initializer / Constructor (Run when a new object is created)
    def __init__(self, name, age):
        # Instance Attributes (Unique to each instance)
        self.name = name
        self.age = age

    # Instance Method
    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old."

# 2. Creating Objects (Instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Miles", 5)

print("--- Classes and Objects ---")
print(f"Dog 1: {dog1.name}, Species: {dog1.species}")
print(f"Dog 2: {dog2.name}, Species: {dog2.species}")

print(dog1.bark())
print(dog2.describe())

# 3. Inheritance
class RussellTerrier(Dog): # Inherits from Dog
    def run(self, speed):
        return f"{self.name} runs {speed}"

    # Overriding a parent method
    def bark(self):
        return f"{self.name} says Yip!"

print("\n--- Inheritance ---")
terrier = RussellTerrier("Jack", 4)
print(terrier.describe()) # Inherited method
print(terrier.run("fast")) # New method
print(terrier.bark())      # Overridden method

# 4. Encapsulation (Private members)
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private attribute (prefixed with __)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")

    def get_balance(self):
        return self.__balance

print("\n--- Encapsulation ---")
acct = Account("Alice", 1000)
acct.deposit(500)
# print(acct.__balance) # This would raise an AttributeError
print(f"Balance: {acct.get_balance()}") # Access via method
