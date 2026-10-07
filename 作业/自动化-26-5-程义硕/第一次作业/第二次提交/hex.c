#include <stdio.h>

int main() {
    unsigned int value = 0xAFBECD;   /* 十六进制整数 */
    char dec[32];
    int i = 0, j;

    /* 方法一：自己实现除以 10 取余，转成十进制字符串 */
    if (value == 0) {
        printf("0\n");
        return 0;
    }
    while (value > 0) {
        dec[i++] = (char)('0' + value % 10);
        value /= 10;
    }
    for (j = i - 1; j >= 0; j--) {
        putchar(dec[j]);
    }
    putchar('\n');

    /* 方法二：标准库一行搞定 */
    /* printf("%u\n", 0xAFBECD); */
    return 0;
}