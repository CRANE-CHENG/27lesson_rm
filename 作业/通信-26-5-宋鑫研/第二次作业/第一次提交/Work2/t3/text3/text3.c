
#include<stdio.h>



float avg(int arr[],int n)
{
    int  b=0;
    for(int i=0;i<n;i++)
        b=b+arr[i];
    float avv=(b/1.0)/n;
    return avv;
}



int main()
{
    int n;
    scanf("%d",&n);

    int a[n];
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    float av=avg(a,n);
    printf("%.2f",av);



    return 0;
}