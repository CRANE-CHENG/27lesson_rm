#include<stdio.h>
int add(int a,int b)
{
	return a+b;
}
int main()
{
	int *x;
	int *y;
	int c,d;
	scanf("%d %d",&c,&d);
	x=&c;
	y=&d;
    int sum;
    sum=add(c,d);
    printf("%d",sum);
    return 0;
	
}
