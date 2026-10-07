#include <stdio.h>

int main()
{
    double a,b;

    scanf("%.2lf %.2lf",&a,&b);

    printf("%.2lf",a*b);
    printf("%.2lf",a/b);

    return 0;
}