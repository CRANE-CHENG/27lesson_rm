#include <stdio.h>
int main(void)
{
    int n=0;
    int a[100]={0};
    double avg=0;
    int sum=0;

    printf("请输入数字个数n");
    scanf("%d",&n);

    for (int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        sum+=a[i];
    }

    avg=(double)sum/n;
    printf("%.2f\n",avg);

    return 0;
}
    