#include <stdio.h>

int main() {
    int n = 0;
    int i = 0;
    printf("请输入你想要算的数字的量；\n");
    scanf("%d",&n);
    double a[n];
    printf("请输入你想要计算的数；\n");
    double c = 0.0;
    for(i = 0;i < n;i++)
    {
        scanf("%lf",&a[i]);
        c = c + a[i];
        
    }
    double average = 0.0;
    average = c/n;
    printf("平均数为%.2lf",average);
   
    return 0;
}