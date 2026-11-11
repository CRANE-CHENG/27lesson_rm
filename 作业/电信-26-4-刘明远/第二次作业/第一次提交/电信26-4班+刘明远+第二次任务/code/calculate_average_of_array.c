#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n,i;
    scanf("%d",&n);
    int a[n],sum=0;
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        sum=sum+a[i];
    }
    double arr=(double)sum/n;
    printf("%.2f",arr);
    return 0;
}