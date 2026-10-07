#include <stdio.h>

int main(void) {
    unsigned int hex_num = 0xAFBECD;
    char dec_str[12];

    sprintf(dec_str, "%u", hex_num);
    printf("十进制: %s\n", dec_str);

    return 0;
}