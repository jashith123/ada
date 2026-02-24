#include <iostream>
#include <vector>
#include <fstream>
#include <random>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

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

void quickSort(vector<int>& arr, int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    ofstream file("quicksort_analysis_large.csv");
    file << "Array_Size,Average_Case,Worst_Case\n";

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(1, 1000000);

    for (int n = 10000; n <= 30000; n += 1000)
    {
        double avgTime = 0, worstTime = 0;
        int runs = 30;

        for (int r = 0; r < runs; r++)
        {
            vector<int> arrAvg(n);
            for (int i = 0; i < n; i++)
                arrAvg[i] = dist(gen);

            auto start1 = high_resolution_clock::now();
            quickSort(arrAvg, 0, n - 1);
            auto stop1 = high_resolution_clock::now();
            avgTime += duration<double, micro>(stop1 - start1).count();

            vector<int> arrWorst(n);
            for (int i = 0; i < n; i++)
                arrWorst[i] = i;

            auto start3 = high_resolution_clock::now();
            quickSort(arrWorst, 0, n - 1);
            auto stop3 = high_resolution_clock::now();
            worstTime += duration<double, micro>(stop3 - start3).count();
        }

        avgTime /= runs;
        worstTime /= runs;

        cout << "Size: " << n
             << " | Avg: " << avgTime
             << " | Worst: " << worstTime << endl;

        file << n << "," 
             << avgTime << ","
             << worstTime << "\n";
    }

    file.close();
    cout << "\nExperiment Completed. CSV Generated.\n";

    return 0;
}