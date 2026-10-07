#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    double a,b,c,d;
    scanf("%lf %lf",&a,&b);
    c=a*b;
    printf(" a*b=%.2f\n",c);
        if (b==0)
        {
            printf("false");
        }
        else
        {
            d=a/b;
    printf("a/b=%.2f\n",d);
        }
    system("pause");
    return 0;
}