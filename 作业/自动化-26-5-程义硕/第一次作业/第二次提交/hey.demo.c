#include<stdio.h>
int main() {
    float a, b;
    float x, y, m, n;//变量赋值
    printf("请输入\n");
    scanf("%f %f", &a, &b);  //输入
    x = a + b;
    y = a - b;
    m = a * b;
    n = a / b;
    printf("%.2f\n", x);
    printf("%.2f\n", y);
    printf("%.2f\n", m);
    printf("%.2f\n", n);
    return 0;
}