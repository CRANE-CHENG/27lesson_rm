#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main()
{
	int x = 0;
	int total = 0;
	double average = 0;
	int number = 0;
	scanf("%d", &x);
	while (x != -1)//x=-1时结束输入数据
	{
		number++;
		total += x;
		x = 0;
		scanf("%d", &x);
	}
	average = total * 1.0 / number;
	printf("平均数是%.2lf", average);
}