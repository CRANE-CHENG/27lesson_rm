#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int a;
    int b;
    int result;
    int (*func_ptr)(int, int);

    printf("请输入两个整数：");
    if (scanf("%d %d", &a, &b) != 2) {
        fprintf(stderr, "输入格式错误。\n");
        return 1;
    }

    func_ptr = add;
    result = func_ptr(a, b);

    printf("%d + %d = %d\n", a, b, result);

    return 0;
}