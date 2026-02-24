#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <chrono>

using namespace std;
using namespace std::chrono;

int linearSearch(const vector<int>& arr, int key)
{
    for (int i = 0; i < arr.size(); i++)
        if (arr[i] == key)
            return i;
    return -1;
}

int main()
{
    ofstream fout("linear_average.csv");
    fout << "Array_Size,Average_Time_ns\n";

    mt19937 rng(123);
    uniform_int_distribution<int> dist;

    const int REPEATS = 10000;

    for (int n = 10000; n <= 100000; n += 5000)
    {
        vector<int> arr(n);
        for (int i = 0; i < n; i++)
            arr[i] = rng();

        dist = uniform_int_distribution<int>(0, INT32_MAX);

        long long totalTime = 0;

        for (int i = 0; i < REPEATS; i++)
        {
            int key = dist(rng);

            auto start = high_resolution_clock::now();
            linearSearch(arr, key);
            auto end = high_resolution_clock::now();

            totalTime += duration_cast<nanoseconds>(end - start).count();
        } 

        double avgTime = (double)totalTime / REPEATS;
        fout << n << "," << avgTime << "\n";

        cout << "Linear Search done for n = " << n << endl;
    }

    fout.close();
    return 0;
}