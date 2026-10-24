#include<stdio.h>

int n;
int a[100];

int main()
{
    scanf("%d",&n);
    for(int i = 0;i < n;i ++)
        scanf("%d",&a[i]);
    float sum = 0;
    for(int i = 0;i < n;i ++)
        sum += a[i];
    sum /= n;
    printf("%.2f",sum);
    
    return 0;
}