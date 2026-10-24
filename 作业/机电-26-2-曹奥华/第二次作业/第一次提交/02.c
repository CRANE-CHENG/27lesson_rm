#include<stdio.h>
void swap(int* x, int* y) {
	int t = *x;
	*x = *y;
	*y = t;
}
int main2(void) {
	int a = 1;
	int b = 2;

	swap(&a, &b);
	printf("交换后：%d %d", a, b);
}
