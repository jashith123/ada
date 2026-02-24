#include <stdio.h>
#include <stdlib.h> 
#include <time.h>

#define REPEATS 5000

int linear_search(int arr[], int n, int key)
{
    for (int i = 0; i < n; i++)
        if (arr[i] == key)
            return i;
    return -1;
}

int main()
{
    srand(123);

    FILE *avg = fopen("linear_average.csv", "w");
    fprintf(avg, "Array_Size,Average_Time_sec\n");

    for (int n = 10000; n <= 100000; n += 5000)
    {
        int arr[n];
        for (int i = 0; i < n; i++)
            arr[i] = rand();

        clock_t total_ticks = 0;

        for (int i = 0; i < REPEATS; i++)
        {
            int key = rand();

            clock_t start = clock();
            linear_search(arr, n, key);
            clock_t end = clock();

            total_ticks += (end - start);
        }

        double avg_time =
            (double)total_ticks / (CLOCKS_PER_SEC * REPEATS);

        fprintf(avg, "%d,%.12f\n", n, avg_time);
        printf("Linear done for n = %d\n", n);
    }

    fclose(avg);
    return 0;
}