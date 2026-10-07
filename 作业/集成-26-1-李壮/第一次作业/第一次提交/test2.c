#include <stdio.h>
#include <stdlib.h>
int main() {
    system("chcp 65001");
    double a, b;
    printf("请输入两个浮点数(a b): ");
    scanf("%lf %lf", &a, &b);
    printf("a * b = %.2f\n", a * b);
    if (b != 0) {
        printf("a / b = %.2f\n", a / b);
    } else {
        printf("除数不能为0\n");
    }
    
    return 0;
}