#include <stdio.h>

int main(void)
{
    unsigned int hexadecimal_number = 0xAFBECD;
    char decimal_string[20];

    /*
     * 题目要求：
     * 已知一个十六进制整数 0xAFBECD，
     * 编写程序计算并以字符串形式输出
     * 它对应的十进制值。
     */

    // 将十六进制整数转换为十进制字符串
    sprintf(decimal_string, "%u", hexadecimal_number);

    // 以字符串形式输出十进制结果
    printf("十六进制数 0xAFBECD 对应的十进制值是：%s\n",
           decimal_string);

    return 0;
}