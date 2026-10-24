
#include <stdio.h>
#include <stdlib.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int a=0;
    int b=0;
    int (*operation)(int, int) = add;

    printf("请输入两个整数：");
    if (scanf("%d %d", &a, &b) != 2)
    {
        printf("输入格式错误。\n");
        return 1;
    }

    printf("%d + %d = %d\n", a, b, operation(a, b));
    system("pause");
    return 0;
}
