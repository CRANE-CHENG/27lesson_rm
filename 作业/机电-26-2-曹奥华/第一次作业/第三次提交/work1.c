#include<stdio.h>
int main() {
	//作业一（浮点数的加减法运算）
	float a = 3.14;
	float b = 1.14;
	float c = a + b;
	float d = a - b;
	printf("%f\n",c);
	printf("%f\n", d);

	//作业二（浮点数的加减法运算）
	float num1 = a * b;
	float num2 = a / b;
	printf("%f\n",num1);
	printf("%f\n", num2);

	//作业三（十六进制转十进制）
	int myint = 0xAFBECD;
	char str[10];
	sprintf(str, "%d", myint);
	printf("%s\n",str);

	return 0;



}