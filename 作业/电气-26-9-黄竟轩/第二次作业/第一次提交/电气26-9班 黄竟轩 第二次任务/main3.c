#include <stdio.h>

int main()
{
    int n, i;
    int arr[100];
    double sum=0;
    scanf("%d", &n);
    for(i=0; i<n; i++)
    {
        scanf("%d", &arr[i]);
        sum=sum+arr[i];
    }
    printf("%.2f", sum/n);
    return 0;
}
