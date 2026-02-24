import random
import time
import csv

REPEATS = 5000

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

with open("linear_average.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Array_Size", "Average_Time_sec"])

    random.seed(123)

    for n in range(10000, 100001, 5000):
        arr = [random.randint(1, 10**9) for _ in range(n)]

        total_time = 0

        for _ in range(REPEATS):
            key = random.randint(1, 10**9)

            start = time.perf_counter_ns()
            linear_search(arr, key)
            end = time.perf_counter_ns()

            total_time += (end - start)

        avg_time = total_time / (REPEATS * 1e9)
        writer.writerow([n, f"{avg_time:.12f}"])
        print(f"Linear Search done for n = {n}")