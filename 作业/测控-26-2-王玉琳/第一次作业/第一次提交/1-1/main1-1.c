#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) { 
	double a , b, c, d;
	printf("请输入第一个数字：");
	scanf("%lf", &a);
	printf("请输入第二个数字：");
	scanf("%lf", &b);
	c = a + b;
	d = a - b;
	printf("两数之和为：%f\n", c);
	printf("两数之差为：%f\n", d);
	return 0;
}