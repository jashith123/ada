#include <iostream>
#include <fstream>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;
using namespace chrono;

int NarySearch(int arr[], int start, int end, int key, int N)
{
    if (start > end)
        return -1;

    int range = end - start + 1;

    if (range < N)
    {
        for (int i = start; i <= end; i++)
            if (arr[i] == key)
                return i;
        return -1;
    }

    int segmentSize = range / N;

    for (int i = 1; i <= N - 1; i++)
    {
        int mid = start + i * segmentSize;

        if (arr[mid] == key)
            return mid;

        if (key < arr[mid])
            return NarySearch(arr, start, mid - 1, key, N);
    }

    return NarySearch(arr,
                      start + (N - 1) * segmentSize,
                      end,
                      key,
                      N);
}

/* ---------------- MAIN EXPERIMENT ---------------- */
int main()
{
    ofstream avgFile("Array_size_avgTime_nary.csv");
    avgFile << "Array_Size,Partition_N,Average_Time_ns\n";

    int Part[] = {2, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int partSize = sizeof(Part) / sizeof(Part[0]);

    long long num = 1000000; 

    random_device rd;
    mt19937 gen(rd());

    for (int n = 10000; n <= 100000; n += 10000)
    {
        cout << "\nTesting Array Size = " << n << endl;

        int* arr = new int[n];

        uniform_int_distribution<> distArr(0, n);
        for (int i = 0; i < n; i++)
            arr[i] = distArr(gen);

        sort(arr, arr + n);

        volatile int dummy = 0;

        for (int p = 0; p < partSize; p++)
        {
            int N = Part[p];
            long long totalDuration = 0;

            // Generate keys in range 0 to 2n (average case setup)
            uniform_int_distribution<> keyDist(0, 2 * n);

            auto start = high_resolution_clock::now();

            for (long long i = 0; i < num; i++)
            {
                int key = keyDist(gen);
                dummy += NarySearch(arr, 0, n - 1, key, N);
            }

            auto stop = high_resolution_clock::now();

            totalDuration =
                duration_cast<nanoseconds>(stop - start).count();

            long long avgTime = totalDuration / num;

            avgFile << n << ","
                    << N << ","
                    << avgTime << "\n";

            cout << "Partition = " << N
                 << " | Avg Time = "
                 << avgTime << " ns\n";
        }

        delete[] arr;
    }

    avgFile.close();

    cout << "\nExperiment Completed Successfully.\n";
    return 0;
}