#include <stdio.h>
#include <stdlib.h>
int main()
{
    double a=0;
    double b=0;
    printf("请输入数字a、b，用空格隔开：");
    scanf("%lf %lf", &a, &b);

    printf("a + b = %lf\n", a + b);
    printf("a - b = %lf\n", a - b);
    system("pause");
    return 0;
}