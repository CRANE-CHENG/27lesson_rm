#include <stdio.h>
#include <stdlib.h>
int main()
{
    double a=0;
    double b=0;
    printf("请输入数字a、b");
    scanf("%lf %lf", &a, &b);

    printf("a * b = %.2f\n", a * b);
    if(b == 0)
    {
        printf("除数不能为0，无法计算a / b\n");
    }
    else
    {
        printf("a / b = %.2f\n", a / b);
    }
    system("pause");
    return 0;
}
