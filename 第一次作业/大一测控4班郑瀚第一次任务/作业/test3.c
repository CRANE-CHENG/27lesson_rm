#include <stdio.h>

int main() {
    double a = 0, b = 0; //加减乘除
    printf("请输入数字(第二个不能为0)a=, b=\n");
    scanf("%lf,%lf", &a, &b);
    
    double c = a + b;
    double d = a - b;
    double e = a * b;
    double f = a / b;
    printf("答案为%.2f\n", c);
    printf("答案为%.2f\n", d);
    printf("答案为%.2f\n", e);
    printf("答案为%.2f\n", f);
    const int g = 0xAFBECD; //十六进制转十进制
    printf("%d\n",g);



    getchar();
    return 0;
}