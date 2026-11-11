#include<stdio.h>
    int main(void)
    {   float a,b;
        printf("请输入两个数字a,b进行乘除运算\n（用空格分隔,且第二个数字不为0,运算结果保留两位小数）：");
        scanf("%f%f",&a,&b);
        printf("a*b=%.2f\n",a*b);
        printf("a/b=%.2f\n",a/b);
        return 0;
    }
