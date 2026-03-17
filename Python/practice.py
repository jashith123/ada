# print("Hello World")

# arr = [1,2,3,4,5]
# print("Original Array:",arr)

# arr.append(6)
# print("Array after append:",arr)

# arr.pop()
# print("Array after pop:",arr)

# arr.remove(3)
# print("Array after remove:",arr)

# arr.insert(2,10)
# print("Array after insert:",arr)

# arr.sort()
# print("Array after sort:",arr)

# arr.reverse()
# print("Array after reverse:",arr)

# arr.count(2)
# print("Array after count:",arr)

# arr.index(2)
# print("Array after index:",arr)

# arr.copy()
# print("Array after copy:",arr)

# arr.clear()
# print("Array after clear:",arr)



# class A:
#     def __init__(self):
#         print("hello")
#     def show(self):
#         pass

# a=A()

# import csv

# file = open("lab_10.py","rb")
# lab = file.read()
# print(lab)
# file.close()

# with open("lab_10.py", "r") as f:
#     text = f.read()
#     words = text.split()

#     f.seek(0)
#     count = 0

#     for line in f:
#         count += 1



# print("Total words:", len(words))
# print("Total lines:", count)



# with open("data.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

# with open("data.csv","r") as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print (line)

# import os

# os.remove("BE Specialization Batch 2024-2028.pdf")


# a = 4

# print(f"ffff{a}")

# import json

# data_csv = [
#     ["id", 1],
#     ["name", "jas"],
#     ["rollno", 44]
# ]
# data_json = {
#     "name": "Alice",
#     "age": 21,
#     "department": "CSE"
# }

# with open("data.json","w") as f:
#     json.dump(data_json, f)


class A:
    def __init__(self):
        print("a")

class B(A):
    def __init__(self):
        print("b")
        super().__init__()

class C(B):
    def __init__(self):
        print("c")
        super().__init__()

c=C()




import time

def timer(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()
        print(f'{func.__name__} took {round(end-start, 10)}s')
        return result

    return wrapper

@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i

    return total

print(slow_sum(100))