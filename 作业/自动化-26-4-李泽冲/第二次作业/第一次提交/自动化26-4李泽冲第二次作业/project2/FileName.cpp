#include<stdio.h>
void exchange(unsigned char *x,unsigned char *y)
{
	unsigned char t;
	t = *x;
	*x = *y;
	*y = t;
}
int main()
{
	unsigned char x=1;
	unsigned char y=9;
	exchange(&x, &y);
	printf("%d\n%d\n", x, y);
}