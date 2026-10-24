#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	float a = 0;
	float b = 0;
	printf("请输入a和b:");
	scanf("%f%f", &a, &b);
	printf("\na*b=%.2f\na/b=%.2f", a * b, a / b);
	return 0;
}