#include<stdio.h>
#include<stdlib.h>

int main()
{
	unsigned int num=0xAFBECD;
	char str[20];
	itoa(num,str,10);
	printf("十六进制0xAFBECD对应的十进制字符串：%s\n",str);
	return 0;
 } 
