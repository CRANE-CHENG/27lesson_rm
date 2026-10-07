/*
 * 第一次C语言课程作业 —— 三道题合并版
 *
 * 说明：一个 C 程序只能有一个 main 函数，所以把三道题分别写成
 *       task1、task2、task3 三个函数，在 main 里用菜单选择运行。
 *
 * 运行后：
 *   输入 1 演示加减法
 *   输入 2 演示乘除法
 *   输入 3 演示十六进制转十进制
 *   输入 0 退出
 */

#include <stdio.h>
#include <string.h>

/* ========== 题目1：加减法（浮点数） ========== */
void task1()
{
    double a, b;
    printf("\n--- 题目1：加减法 ---\n");
    printf("请输入两个浮点数 a 和 b（空格隔开）：");
    scanf("%lf %lf", &a, &b);
    printf("a + b = %.2f\n", a + b);
    printf("a - b = %.2f\n", a - b);
}

/* ========== 题目2：乘除法（浮点数，保留两位小数） ========== */
void task2()
{
    double a, b;
    printf("\n--- 题目2：乘除法 ---\n");
    printf("请输入两个浮点数 a 和 b（空格隔开）：");
    scanf("%lf %lf", &a, &b);
    printf("a * b = %.2f\n", a * b);
    if (b == 0)
    {
        printf("a / b 无法计算：除数 b 不能为 0！\n");
    }
    else
    {
        printf("a / b = %.2f\n", a / b);
    }
}

/* ========== 题目3：十六进制转十进制 ========== */
void task3()
{
    char hex[] = "AFBECD";
    long long decimal = 0;
    int len = strlen(hex);

    printf("\n--- 题目3：十六进制转十进制 ---\n");

    for (int i = 0; i < len; i++)
    {
        char c = hex[i];
        int value;

        if (c >= '0' && c <= '9')
            value = c - '0';
        else if (c >= 'A' && c <= 'F')
            value = c - 'A' + 10;
        else if (c >= 'a' && c <= 'f')
            value = c - 'a' + 10;
        else
            value = 0;

        decimal = decimal * 16 + value;
    }

    // 以字符串形式输出
    char result[20];
    sprintf(result, "%lld", decimal);

    printf("十六进制 0x%s\n", hex);
    printf("对应十进制值（字符串形式）：%s\n", result);
}

/* ========== 主函数：菜单 ========== */
int main()
{
    int choice;

    do
    {
        printf("\n======== 第一次C语言作业 ========\n");
        printf("1. 加减法\n");
        printf("2. 乘除法\n");
        printf("3. 十六进制转十进制\n");
        printf("0. 退出\n");
        printf("请选择：");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            task1();
            break;
        case 2:
            task2();
            break;
        case 3:
            task3();
            break;
        case 0:
            printf("程序已退出，再见！\n");
            break;
        default:
            printf("选择无效，请输入 0~3 之间的数字。\n");
            break;
        }
    } while (choice != 0);

    return 0;
}
