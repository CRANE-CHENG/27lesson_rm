#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001");
    int hexNum = 0xAFBECD; 
    printf("对应的十进制值为: %d\n", hexNum);
    return 0;
}