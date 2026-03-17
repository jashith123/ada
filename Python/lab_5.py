# Use a Python set ports to represent the network port numbers used in a computer system and perform the following tasks:

# 1.    Populate the set ports with at least 10 network port numbers.
ports = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 2.    Display the complete set.
print(ports)
# 3.    Demonstrate that duplicate port numbers are automatically removed when added to a set.
ports.add(1)
print(ports)
# 4.    Find and display the total number of unique ports using len().
print(len(ports))
# 5.    Check whether a specific port number exists in the set using the in operator.
print(1 in ports)
# 6.    Add a new port number to the set using add().
ports.add(11)
print(ports)
# 7.    Add multiple port numbers to the set using update().
ports.update([12, 13, 14, 15])
print(ports)
# 8.    Remove a specific port number using remove().
ports.remove(1)
print(ports)
# 9.    Remove a port number using discard() and observe the difference from remove().
ports.discard(1)
print(ports)
# 10.    Remove and return an arbitrary port number using pop().
print(ports.pop())
# 11.    Traverse the set using a for loop.
for port in ports:
    print(port)
# 12.    Create another set reserved_ports containing commonly reserved port numbers.
reserved_ports = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 13.    Find and display the union of ports and reserved_ports.
print(ports.union(reserved_ports))
# 14.    Find and display the intersection of ports and reserved_ports.
print(ports.intersection(reserved_ports))
# 15.    Find and display the difference between ports and reserved_ports.
print(ports.difference(reserved_ports))
# 16.    Find and display the symmetric difference between ports and reserved_ports.
print(ports.symmetric_difference(reserved_ports))
# 17.    Check whether reserved_ports is a subset of ports.
print(reserved_ports.issubset(ports))
# 18.    Check whether ports is a superset of reserved_ports.
print(ports.issuperset(reserved_ports))
# 19.    Create a copy of the set using the copy() method.
ports_copy = ports.copy()
print(ports_copy)
# 20.    Demonstrate the difference between assignment and copying of sets.
ports_copy = ports
print(ports_copy)
# 21.    Clear all elements from the set using clear().
ports.clear()
print(ports)
# 22.    Convert the set into a list and display the result.
ports_list = list(ports)
print(ports_list)
# 23.    Convert the set into a tuple and display the result.
ports_tuple = tuple(ports)
print(ports_tuple)
# 24.    Create a new set containing only port numbers greater than 1024.
ports_greater_than_1024 = {port for port in ports if port > 1024}
print(ports_greater_than_1024)
# 25.    Compare sets with lists and tuples with respect to uniqueness, ordering, and use cases.
