#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int add(int a, int b)
{
	return  a + b;
}
int main()
{
	int result,x,y;
	int (*p)(int, int);
	p = add;
	scanf("%d%d", &x, &y);
		result = p(x,y);
		printf("%d", result);
}