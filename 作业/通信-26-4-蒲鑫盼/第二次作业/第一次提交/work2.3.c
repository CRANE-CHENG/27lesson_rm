#include <stdio.h>
int main()
{
    int n;
    int a[100];
    double sum = 0;
    double avg;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        sum += a[i];
    }
    avg = sum / n;
    printf("%.2f\n", avg);
    return 0;
}