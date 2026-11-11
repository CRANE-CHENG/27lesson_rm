#include<stdio.h>
    int main(void)
    {   int num=0xAFBECD;
        char str[20];
        sprintf(str,"%d",num);
        printf("%d",num);
        return 0;
    }