#include <stdio.h>

int main(void)
{
    unsigned int hex_value = 0xAFBECD;
    char result[32];

    /* 将十进制值以字符串形式存入 result */
    sprintf(result, "%u", hex_value);

    printf("十六进制 0xAFBECD 对应的十进制值为：%s\n", result);

    return 0;
}