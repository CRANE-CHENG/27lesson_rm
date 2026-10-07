#include<stdio.h>
int main(void)
{
    long long a=0xAFBECD;
    char c[32];
    sprintf(c,"%lld",a);
    printf("0xAFBECD=%s\n",c);
    return 0;
}