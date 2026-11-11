#include<stdio.h>
    int main(void)
    {   float a,b;
        printf("请输入两个数字a,b进行加减运算\n（用空格分隔）：");
        scanf("%f%f",&a,&b);
        printf("a+b=%f\n",a+b);
        printf("a-b=%f\n",a-b);
        return 0;
    }