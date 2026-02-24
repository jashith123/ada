#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

random_device rd;
mt19937 gen(rd());

int partition(vector<int>& arr, int low, int high)
{
    int pivot = arr[low];
    int i = low + 1;
    int j = high;

    while (true)
    {
        while (i <= high && arr[i] <= pivot)
            i++;

        while (arr[j] > pivot)
            j--;

        if (i >= j)
            break;

        swap(arr[i], arr[j]);
    }

    swap(arr[low], arr[j]);
    return j;
}

int randomizedPartition(vector<int>& arr, int low, int high)
{
    uniform_int_distribution<> dist(low, high);
    int randomIndex = dist(gen);

    swap(arr[low], arr[randomIndex]); 
    return partition(arr, low, high);
}

void randomizedQuickSort(vector<int>& arr, int low, int high)
{
    if (low < high)
    {
        int pi = randomizedPartition(arr, low, high);
        randomizedQuickSort(arr, low, pi - 1);
        randomizedQuickSort(arr, pi + 1, high);
    }
}

int main()
{
    ofstream file("randomized_quicksort_analysis.csv");
    file << "Array_Size,Execution_Time_Microseconds\n";

    for (int n = 10000; n <= 30000; n += 1000)
    {
        double totalTime = 0;
        int runs = 30;

        for (int r = 0; r < runs; r++)
        {
            vector<int> arr(n);
            for (int i = 0; i < n; i++)
                arr[i] = i;

            auto start = high_resolution_clock::now();
            randomizedQuickSort(arr, 0, n - 1);
            auto stop = high_resolution_clock::now();

            totalTime += duration<double, micro>(stop - start).count();
        }

        double avgTime = totalTime / runs;

        cout << "Size: " << n
             << " | Time: " << avgTime << " microseconds\n";

        file << n << "," << avgTime << "\n";
    }

    file.close();
    cout << "\nRandomized Quick Sort Experiment Completed.\n";

    return 0;
}