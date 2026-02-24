#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define REPEATS 1000

// Binary Search (array must be sorted)
int binary_search(int arr[], int n, int key)
{
    int low = 0, high = n - 1;

    while (low <= high)
    {
        int mid = (low + high) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main()
{
    srand(123);

    FILE *avg = fopen("binary_average.csv", "w");
    fprintf(avg, "Array_Size,Average_Time_sec\n");

    for (int n = 4000; n <= 16000; n += 1000)
    {
        int arr[n];

        // Sorted array
        for (int i = 0; i < n; i++)
            arr[i] = i * 2;

        char filename[40];
        sprintf(filename, "binary_analysis_%d.txt", n);
        FILE *fp = fopen(filename, "w");

        fprintf(fp, "BINARY SEARCH ANALYSIS\n");
        fprintf(fp, "Array Size = %d\n", n);
        fprintf(fp, "-------------------------------------------\n");
        fprintf(fp, "Iteration\tKey\tIndex\tTime (sec)\n");
        fprintf(fp, "-------------------------------------------\n");

        double total_time = 0.0;

        for (int i = 0; i < REPEATS; i++)
        {
            int key = rand() % (2 * n);

            clock_t start = clock();
            int index = binary_search(arr, n, key);
            clock_t end = clock();

            double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
            total_time += time_taken;

            fprintf(fp, "%4d\t\t%6d\t", i + 1, key);
            if (index == -1)
                fprintf(fp, "Not Found\t");
            else
                fprintf(fp, "%6d\t", index);

            fprintf(fp, "%.8f\n", time_taken);
        }

        fprintf(avg, "%d,%.8f\n", n, total_time / REPEATS);
        fclose(fp);

        printf("Generated %s\n", filename);
    }

    fclose(avg);
    printf("\nBinary Search analysis complete.\n");
    return 0;
}