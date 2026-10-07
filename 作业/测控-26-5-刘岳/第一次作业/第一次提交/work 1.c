#include <stdio.h>

int main(void)
{
    double a, b;

    printf("请输入两个数字 a 和 b ：");
    scanf("%lf %lf", &a, &b);

    printf("a + b = %g\n", a + b);
    printf("a - b = %g\n", a - b);

    return 0;
}