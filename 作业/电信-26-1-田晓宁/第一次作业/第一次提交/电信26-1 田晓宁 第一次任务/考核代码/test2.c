#include <stdio.h>

int main(void)
{
    double a;
    double b;
    double product;
    double quotient;

    /*
     * 题目要求：
     * 输入两个数字 a、b，
     * 分别输出 a × b 和 a ÷ b 的计算结果，
     * 结果保留两位小数。
     */

    // 输入两个浮点数
    printf("请输入两个数字 a 和 b：");
    scanf("%lf %lf", &a, &b);

    // 计算乘法
    product = a * b;

    // 输出乘法结果，保留两位小数
    printf("a * b = %.2f\n", product);

    // 判断除数是否为 0，避免除数为 0
    if (b == 0)
    {
        printf("错误：除数不能为 0。\n");
    }
    else
    {
        // 计算除法
        quotient = a / b;

        // 输出除法结果，保留两位小数
        printf("a / b = %.2f\n", quotient);
    }

    return 0;
}