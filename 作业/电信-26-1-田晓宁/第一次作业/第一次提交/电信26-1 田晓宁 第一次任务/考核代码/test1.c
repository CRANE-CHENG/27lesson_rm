#include <stdio.h>

int main(void)
{
    double a;
    double b;
    double sum;
    double difference;

    /*
     * 题目要求：
     * 输入两个数字 a、b，
     * 分别输出 a + b 和 a - b 的计算结果。
     */

    // 输入两个浮点数
    printf("请输入两个数字 a 和 b：");
    scanf("%lf %lf", &a, &b);

    // 计算加法和减法
    sum = a + b;
    difference = a - b;

    // 输出计算结果，保留两位小数
    printf("a + b = %.2f\n", sum);
    printf("a - b = %.2f\n", difference);

    return 0;
}