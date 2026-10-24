#include <stdio.h>
#include <stdlib.h>


int main()
{
    unsigned int num = 0xAFBECD;
    char str_buf[20];

    sprintf(str_buf, "%u", num);

    printf("十六进制0xAFBECD对应的十进制字符串：%s\n", str_buf);
    system("pause");
    return 0;
}
