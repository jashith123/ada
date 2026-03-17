# Use a Python string message to represent a text message and perform the following tasks:

# 1.    Initialize the string message with a meaningful sentence.
message = "Hello World"
# 2.    Display the complete string.
print(message)
# 3.    Display the first and last characters of the string.
print(message[0])
print(message[-1])
# 4.    Display a substring from index 2 to index 10 using slicing.
print(message[2:10])
# 5.    Find and display the length of the string using len().
print(len(message))
# 6.    Convert the string to uppercase.
print(message.upper())
# 7.    Convert the string to lowercase.
print(message.lower())
# 8.    Convert the string to title case.
print(message.title())
# 9.    Count the number of occurrences of a specific character or word.
print(message.count("l"))
# 10.    Search for a given substring and display its starting index.
print(message.find("World"))
# 11.    Check whether the string starts with a given substring.
print(message.startswith("Hello"))
# 12.    Check whether the string ends with a given substring.
print(message.endswith("World"))
# 13.    Replace a word in the string with another word.
print(message.replace("World", "Python"))
# 14.    Split the string into a list of words.
print(message.split(" "))
# 15.    Join the list of words back into a single string using a separator.
print(" ".join(message.split(" ")))
# 16.    Remove leading and trailing whitespace using strip().
print(message.strip(" "))
# 17.    Find and display the number of vowels in the string.
print(message.count("a"))
# 18.    Reverse the string using slicing.
print(message[::-1])
# 19.    Check whether the string is a palindrome.
print(message == message[::-1])
# 20.    Compare two strings and display whether they are equal.
print(message == "Hello World")
# 21.    Concatenate two strings and display the result.
print(message + " " + "Python")
# 22.    Demonstrate string immutability by attempting to modify a character.
message[0] = "h"
# 23.    Extract and display only the digits present in the string.
print(message[1])
# 24.    Count the number of words in the string.
print(message.count(" ")) 
# 25.    Convert the string into a list of characters.
print(list(message))
