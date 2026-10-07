#include<stdio.h>
int main(void)
{
    double a, b;
    double x, y, m, n;
    printf("请输入两个数字且第二个数字不为0:");//通过提要求来防止除数为0
    scanf("%lf %lf",&a, &b);
    x=a+b;
    y=a-b;
    m=a*b;
    n=a/b;
    printf("a+b=%f\n", x);//以下两行为任务一的加减
    printf("a-b=%f\n", y);
    printf("a*b=%.2f\n", m);//以下两行为任务二的乘除并保留了两位小数
    printf("a/b=%.2f\n", n);
    return 0;
}