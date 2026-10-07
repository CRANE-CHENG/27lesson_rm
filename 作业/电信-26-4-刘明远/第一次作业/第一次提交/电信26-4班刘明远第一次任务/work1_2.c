#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    double a,b,c,d;
    scanf("%lf %lf",&a,&b);
    c=a*b;
    d= a/b;
    printf(" a*b=%.2f, a/b=%.2f",c,d);
    system("pause");
    return 0;
}