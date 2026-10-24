#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int main(void)
{
    int (*p)(int, int);
    int x = 666, y = 888;
    int res;

    p = add;   

    res = p(x, y);
    printf("x + y = %d\n", res);

    return 0;
}
