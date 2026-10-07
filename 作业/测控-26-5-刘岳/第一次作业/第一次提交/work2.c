#include <stdio.h>

int main(void)
{
    double a, b;

    printf("请输入两个数字 a 和 b ：");
    scanf("%lf %lf", &a, &b);

    printf("a * b = %.2f\n", a * b);

    if (b == 0)
    {
        printf("错误：除数不能为零！\n");
    }
    else
    {
        printf("a / b = %.2f\n", a / b);
    }

    return 0;
}