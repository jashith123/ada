#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define REPEATS 5000

void find_max_min(int arr[], int n, int *max, int *min)
{
    *max = *min = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (arr[i] > *max) *max = arr[i];
        if (arr[i] < *min) *min = arr[i];
    }
}

int main()
{
    srand(123);

    FILE *avg = fopen("maxmin_average.csv", "w");
    fprintf(avg, "Array_Size,Average_Time_sec\n");

    for (int n = 10000; n <= 100000; n += 5000)
    {
        int arr[n];
        for (int i = 0; i < n; i++)
            arr[i] = rand();

        clock_t total_ticks = 0;

        for (int i = 0; i < REPEATS; i++)
        {
            int max, min;

            clock_t start = clock();
            find_max_min(arr, n, &max, &min);
            clock_t end = clock();

            total_ticks += (end - start);
        }

        double avg_time =
            (double)total_ticks / (CLOCKS_PER_SEC * REPEATS);

        fprintf(avg, "%d,%.12f\n", n, avg_time);
        printf("Max-Min done for n = %d\n", n);
    }

    fclose(avg);
    return 0;
}