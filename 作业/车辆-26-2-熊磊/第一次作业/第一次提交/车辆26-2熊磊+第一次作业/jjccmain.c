#include<stdio.h>
double cheng(double num1,double num2)
{
	double sum1=num1*num2;
	return sum1;
}
double chu(double num1,double num2)
{
	double sum2=num1/num2;
	return sum2;
}
double jia(double num1,double num2)
{
	double sum1=num1+num2;
	return sum1;
}
double jian(double num1,double num2)
{
	double sum2=num1-num2;
	return sum2;
}

int main()
{
	double a,b;
	printf("请输入俩个数。。。\n");
	scanf("%lf %lf",&a,&b);
	printf("乘积=%lf\n",cheng(a,b));
	printf("相除=%lf\n",chu(a,b));
	printf("相加=%lf\n",jia(a,b));
	printf("相减=%lf\n",jian(a,b));
	return 0;
}
