#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;
using namespace chrono;

int binarySearch(const vector<int>& arr, int key)
{
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }

    return -1;
}

int main()
{
    ofstream fout("binary_average.csv");
    fout << "Array_Size,Average_Time_ns\n";

    mt19937 rng(123); 

    const int REPEATS = 100000;

    for (int n = 10000; n <= 100000; n += 5000)
    {
        vector<int> arr(n);

        uniform_int_distribution<int> arrDist(0, 1000000);
        uniform_int_distribution<int> keyDist(0, 2000000);

        for (int i = 0; i < n; i++)
            arr[i] = arrDist(rng);

        sort(arr.begin(), arr.end());

        volatile int dummy = 0;  

        auto start = high_resolution_clock::now();

        for (int i = 0; i < REPEATS; i++)
        {
            int key = keyDist(rng);
            dummy += binarySearch(arr, key);
        }

        auto end = high_resolution_clock::now();

        long long totalTime =
            duration_cast<nanoseconds>(end - start).count();

        double avgTime = (double)totalTime / REPEATS;

        fout << n << "," << avgTime << "\n";

        cout << "Binary Search done for n = "
             << n << endl;
    }

    fout.close();
    return 0;
}