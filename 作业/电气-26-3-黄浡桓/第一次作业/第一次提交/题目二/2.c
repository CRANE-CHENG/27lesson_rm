#include <stdio.h>
int main(void)
{
    double a, b;

    printf("请输入 a");
    scanf("%lf", &a);
    printf("请输入 b");
    scanf("%lf", &b);

    printf("a * b = %.2f\n", a * b);      
    if (b == 0)                           
        printf("a / b : 除数不能为 0\n");
    else
        printf("a / b = %.2f\n", a / b);

    return 0;
}