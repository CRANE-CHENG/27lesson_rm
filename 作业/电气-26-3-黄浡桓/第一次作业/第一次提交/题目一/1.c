
#include <stdio.h>

int main(void)
{
    double a, b;                 

    printf("请输入 a：");
    scanf("%lf", &a);            
    printf("请输入 b：");
    scanf("%lf", &b);

    printf("a + b = %f\n", a + b);
    printf("a - b = %f\n", a - b);

    return 0;
}