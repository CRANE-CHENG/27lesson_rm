#include<stdio.h>
int main()
{
	//0xAFBECD
	int num = 0xAFBECD;
	char a[20];
	sprintf(a, "%d", num);
	printf("%s\n", a);

	return 0;
}