#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <random>

using namespace std;
using namespace chrono;

void merge(vector<int> &arr, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    while (i < n1)
        arr[k++] = L[i++];

    while (j < n2)
        arr[k++] = R[j++];
}

void mergeSort(vector<int> &arr, int left, int right)

{
    if (left < right)
    {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

int main()
{
    ofstream file("merge_sort_average2.csv");
    file << "Array_Size,Execution_Time(ns)\n";

    mt19937 rng(time(NULL));

    for (int size = 10000; size <= 100000; size += 5000)
    {
       vector<int> arr(size);
        uniform_int_distribution<int> dist(1, 1000000);

        for (int i = 0; i < size; i++)
            arr[i] = dist(rng);

        auto start = high_resolution_clock::now();

        mergeSort(arr, 0, size - 1);

        auto stop = high_resolution_clock::now();

        auto duration = duration_cast<nanoseconds>(stop - start);

        file << size << "," << duration.count() << "\n";

        cout << "Size: " << size << " Done\n";
    }

    file.close();
    cout << "Results saved to merge_sort_average.csv\n";

    return 0;
}