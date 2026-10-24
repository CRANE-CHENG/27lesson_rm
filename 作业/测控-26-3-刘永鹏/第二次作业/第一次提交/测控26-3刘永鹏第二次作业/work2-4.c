#include <stdio.h>
int add(int a, int b) {
    return a + b;
}

int main(void) {
    int a, b;

    printf("请输入两个整数: ");
    scanf("%d %d", &a, &b);
    int (*p)(int, int) = add;
    int result1 = p(a, b);
    int result2 = (*p)(a, b);

    printf("通过函数指针 p 调用 add: add(%d, %d) = %d\n", a, b, result1);
    printf("通过 (*p) 调用 add:       add(%d, %d) = %d\n", a, b, result2);
    printf("直接调用 add:             add(%d, %d) = %d\n", a, b, add(a, b));

    return 0;
}