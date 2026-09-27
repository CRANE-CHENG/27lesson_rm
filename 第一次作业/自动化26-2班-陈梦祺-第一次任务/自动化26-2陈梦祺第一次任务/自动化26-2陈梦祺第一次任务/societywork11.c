#include <stdio.h>
int main()
{
	double a, b;
	printf("please write two number\n");
	scanf(" %lf %lf", &a, &b);
	double c = a + b;
	double d = a - b;
	printf("a + b =%lf\n",c);
	printf("a - b =%lf\n",d);


	return 0;
}