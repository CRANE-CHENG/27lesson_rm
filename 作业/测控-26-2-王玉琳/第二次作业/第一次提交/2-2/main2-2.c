#include<stdio.h>
void swap(int* x, int* y) {//定义函数内参数为两个指针变量接收地址，实现函数内部修改函数外部变量
	int t = *x;
		* x = *y;//赋值交换
		*y = t;
}
int a = 1, b = 2;
int main(void) {
	swap(&a, &b);//参数为a,b的地址
	printf("%d %d",a,b);

	return 0;
}