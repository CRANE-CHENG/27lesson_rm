#include<stdio.h>

int he(int x,int b);

int main ()
{
	int a ;
	int b ;
	printf("请输入两个数\n");
	scanf("%d %d",&a,&b);
	int (*p)(int,int)=he;
	int sum=p(a,b);
	printf("%d",sum);
	
	
}

int he(int x,int y)
{
	int su=x+y;
	return su;
}
