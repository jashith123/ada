#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

int NarySearch(const vector<int>& arr, int start, int end, int key, int N)
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

int main()
{
    ofstream file("nary_absolute_random.csv");
    file << "Partition_N,Average_Time_ns\n";

    const int n = 100000;          
    const long long num = 1000000; 

    vector<int> arr(n);

    random_device rd;
    mt19937 gen(rd());

    uniform_int_distribution<> distArr(0, n);
    for (int i = 0; i < n; i++)
        arr[i] = distArr(gen);

    sort(arr.begin(), arr.end());

    int Part[] = {2, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int partSize = sizeof(Part) / sizeof(Part[0]);

    volatile int dummy = 0; 

    for (int p = 0; p < partSize; p++)
    {
        int N = Part[p];

        uniform_int_distribution<> keyDist(0, 2 * n);

        auto startTime = high_resolution_clock::now();

        for (long long i = 0; i < num; i++)
        {
            int key = keyDist(gen);
            dummy += NarySearch(arr, 0, n - 1, key, N);
        }

        auto endTime = high_resolution_clock::now();

        long long totalTime =
            duration_cast<nanoseconds>(endTime - startTime).count();

        long long avgTime = totalTime / num;

        cout << "Partition = " << N
             << " | Avg Time = "
             << avgTime << " ns\n";

        file << N << "," << avgTime << "\n";
    }

    file.close();

    cout << "\nExperiment Completed Successfully.\n";
    return 0;
}