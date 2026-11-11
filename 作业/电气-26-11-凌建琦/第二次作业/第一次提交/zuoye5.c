#include<stdio.h>
 swap(int *x,int *y)
{
	int change;
	change=*x;
	*x=*y;
	*y=change;
}
int main()
{
	int a,b;
	scanf("%d %d",&a,&b);
	printf("a=%d,b=%d\n",a,b);
	swap(&a,&b);
	printf("a=%d,b=%d",a,b);
	return 0;
}
