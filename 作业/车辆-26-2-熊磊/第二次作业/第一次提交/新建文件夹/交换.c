#include <stdio.h>

void i(int*a,int*b);

int main()
{
	int a,b;
	printf("请输入两个数\n");
	scanf("%d %d",&a,&b);
	printf(" 交换前；a=%d,b=%d\n",a,b);
	i(&a,&b);
	printf(" 交换后；a=%d,b=%d",a,b);
	return 0;
}
void i(int*a,int*b)
{
	int num=*a;
	*a=*b;
	*b=num;
	
}
