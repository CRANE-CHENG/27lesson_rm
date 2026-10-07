#include <stdio.h>
int main()
{
    double a, b;
    printf("请输入两个数字 a 和 b（用空格或回车分隔）：");
    scanf("%lf %lf", &a, &b);

    printf("a * b = %.2f\n", a * b);
    printf("a / b = %.2f\n", a / b);

    return 0;
}