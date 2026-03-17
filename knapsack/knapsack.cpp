#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
#include <fstream>

using namespace std;
using namespace chrono;

// Comparator function for sorting
bool compare(pair<double, pair<int,int>> a, pair<double, pair<int,int>> b)
{
    return a.first > b.first;
}

double knapSack(int W, vector<pair<double, pair<int,int>>> &items)
{
    sort(items.begin(), items.end(), compare);

    double totalValue = 0.0;
    int remaining = W;

    for (int i = 0; i < items.size(); i++)
    {
        int weight = items[i].second.first;
        int value = items[i].second.second;
        double ratio = items[i].first;

        if (remaining >= weight)
        {
            remaining = remaining - weight;
            totalValue = totalValue + value;
        }
        else
        {
            totalValue = totalValue + ratio * remaining;
            break;
        }
    }

    return totalValue;
}

int main()
{
    ofstream file("fractional_knapsack_results2.csv");
    file << "Number_of_Items,Execution_Time(ns)\n";

    random_device rd;
    mt19937 gen(rd());

    uniform_int_distribution<int> weight_dist(1, 50);
    uniform_int_distribution<int> value_dist(10, 200);

    int repetitions = 10;

    for (int n = 10000; n <= 100000; n = n + 5000)
    {
        int W = 200;

        vector<pair<double, pair<int,int>>> items(n);

        for (int i = 0; i < n; i++)
        {
            int w = weight_dist(gen);
            int v = value_dist(gen);
            double ratio = (double)v / w;

            items[i] = make_pair(ratio, make_pair(w, v));
        }

        long long total_time = 0;

        for (int r = 0; r < repetitions; r++)
        {
            vector<pair<double, pair<int,int>>> temp = items;

            auto start = high_resolution_clock::now();
            knapSack(W, temp);
            auto end = high_resolution_clock::now();

            long long duration = duration_cast<nanoseconds>(end - start).count();
            total_time = total_time + duration;
        }

        long long avg_time = total_time / repetitions;

        file << n << "," << avg_time << "\n";

        cout << "Items: " << n
             << "  Avg Time: " << avg_time << " ns" << endl;
    }

    file.close();

    cout << "\nCSV file generated successfully.\n";

    return 0;
}