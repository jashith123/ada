#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define REPEATS 1000

// Linear Search function
int linear_search(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int main()
{
    srand(123); // fixed seed for reproducibility

    // CSV file for average time
    FILE *avg = fopen("average.csv", "w");
    if (avg == NULL)
    {
        printf("Error opening average.csv\n");
        return 1;
    }

    fprintf(avg, "Array_Size,Average_Time_sec\n");

    // Test for different array sizes
    for (int n = 4000; n <= 16000; n += 1000)
    {
        int arr[n];

        // Generate random array
        for (int i = 0; i < n; i++)
            arr[i] = rand() % (2 * n) + 1;

        // Create detailed analysis file
        char filename[40];
        sprintf(filename, "analysis_%d.txt", n);

        FILE *fp = fopen(filename, "w");
        if (fp == NULL)
        {
            printf("Error opening %s\n", filename);
            return 1;
        }

        fprintf(fp, "LINEAR SEARCH ANALYSIS\n");
        fprintf(fp, "Array Size = %d\n", n);
        fprintf(fp, "-------------------------------------------\n");
        fprintf(fp, "Iteration\tKey\tIndex\tTime (sec)\n");
        fprintf(fp, "-------------------------------------------\n");

        double total_time = 0.0;

        for (int i = 0; i < REPEATS; i++)
        {
            int key = rand() % (2 * n) + 1;

            clock_t start = clock();
            int index = linear_search(arr, n, key);
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

        double avg_time = total_time / REPEATS;
        fprintf(avg, "%d,%.8f\n", n, avg_time);

        fclose(fp);
        printf("Generated %s | Avg Time = %.8f sec\n", filename, avg_time);
    }

    fclose(avg);
    printf("\nAll files generated successfully.\n");
    return 0;
}