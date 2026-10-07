#include <stdio.h>

int main()
{
    int num=0xAFBECD;
    char str[10];
    sprintf(str,"%d",num);
    printf(str,"%s");
    return 0;
}