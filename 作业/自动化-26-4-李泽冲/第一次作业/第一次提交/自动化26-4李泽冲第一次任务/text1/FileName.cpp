#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
 {
	float a=0;
	float b=0;
	printf("请输入a和b:");
	scanf("%f%f", &a, &b);//本来为追求效果好点我使用了%c但好像%c不能用在小数里
	printf("\na+b=%f\na-b=%f\n", a + b, a - b);
	return 0;
}