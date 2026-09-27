#include <stdio.h>
int main()
{
	double e, f;
	printf("please write two number\n");
	scanf(" %lf %lf", &e, &f);
	double g = e * f;
	double h = e / f;
	printf("e * g = %.2lf\n", g);
	printf("e / g = %.2lf\n", h);
	return 0;
}