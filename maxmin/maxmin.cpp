#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <chrono>

using namespace std;
using namespace chrono;

void recursiveMinMax(const vector<int>& arr, int start, int end, int &minVal, int &maxVal)
{
    if (start == end)
    {
        if (arr[start] < minVal)
            minVal = arr[start];
        if (arr[start] > maxVal)
            maxVal = arr[start];
        return;
    }

    int mid = start + (end - start) / 2;

    recursiveMinMax(arr, start, mid, minVal, maxVal);
    recursiveMinMax(arr, mid + 1, end, minVal, maxVal);
}

int main()
{
    ofstream file("recursive_minmax_output.csv");
    file << "Array_Size,Average_Time_Microseconds\n";

    random_device rd; 
    mt19937 gen(rd());
    uniform_int_distribution<> dist(1, 1000000);

    for (int n = 8000; n <= 80000; n += 4000)
    {
        vector<int> arr(n);

        for (int i = 0; i < n; i++)
            arr[i] = dist(gen);

        double totalTime = 0.0;
        int runs = 300;

        for (int i = 0; i < runs; i++)
        {
            int minVal = arr[0];
            int maxVal = arr[0];

            auto start = high_resolution_clock::now();

            recursiveMinMax(arr, 0, n - 1, minVal, maxVal);

            auto stop = high_resolution_clock::now();

            totalTime += duration<double, micro>(stop - start).count();
        }

        double avgTime = totalTime / runs;

        cout << "Size: " << n 
             << " | Avg Time: " << avgTime << " microseconds\n";

        file << n << "," << avgTime << "\n";
    }

    file.close();

    cout << "\nExperiment completed. CSV generated.\n";

    return 0;
}