#include <stdio.h>

int main() {
    int value = 0xAFBECD;      
    char str[32];              

    sprintf(str, "%d", value); 
    printf("%s\n", str);       

    return 0;
}














