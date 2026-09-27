#include<stdio.h>

int main(void)
{
    double a,b;
    double x,y,z,w;
    scanf("%lf %lf",&a,&b);
    x=a+b;
    y=a-b;
    z=a*b;
    w=a/b;
    printf("a+b=%.2f\n",x);
    printf("a-b=%.2f\n",y);
    printf("a*b=%.2f\n",z);
    printf("a/b=%.2f\n",w);
    return 0;
} 