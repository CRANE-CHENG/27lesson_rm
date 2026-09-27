#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    double a,b,c,d;
    scanf("%lf %lf",&a,&b);
    c=a+b;
    d=a-b;
    printf("a+b=%f",c);
    printf("a-b=%f",d);
    system("pause");
    return 0;
}