#include <stdio.h>

int main(void)
{
    float a,b;
    int num=0xAFBECD;
    scanf("%f %f ",&a,&b);
    printf("%f %f %f %.2f %d",a+b,a-b,a*b,a/b,num);


    return 0;
}