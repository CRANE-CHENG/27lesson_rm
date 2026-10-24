#include <stdio.h>

int main() {
    char str[20];

    sprintf(str, "%d", 0xAFBECD);

    printf("%s\n", str);

    return 0;
}