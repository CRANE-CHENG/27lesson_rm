#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001");
    double a, b;
    printf("请输入两个浮点数(a b): ");
    scanf("%lf %lf", &a, &b);
    printf("a + b = %f\n", a + b);
    printf("a - b = %f\n", a - b);
    return 0;
}