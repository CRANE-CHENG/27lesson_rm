#include <stdio.h>

int main() {
    double a=0,b=0;//第一题
    printf("请输入两个数；");
    scanf("%lf %lf",&a,&b);
    double c=a+b;
    double d=a-b;
    printf("答案为%.2f\n",c);
    printf("答案为%.2f\n",d);//第二题
    printf("请再输入两个数(且第二个数不为0和空):");
    scanf("%lf %lf",&a,&b);
    double e=a*b;
    double f=a/b;
    printf("答案为%.2f\n",e);
    printf("答案为%.2f\n",f);//第三题
    const int g=0xAFBECD;
    printf("转化为十进制为：g=%d\n",g);
    






    getchar();
    return 0;
}