#include <stdio.h>

int add(int a,int b)
{
	return a+b;
 } 
 
 int main()
 {
 	int a,b;
 	scanf("%d %d", &a, &b);
 	int (*p)(int, int)=add;
 	printf("%d",p(a,b));
 	return 0;
 	
 }
