#include<stdio.h>

int add(int a, int b) {
	return a + b;
}
int main() {
	int(*fp)(int, int);
	//(*fp)	加括号，表示 * 先跟 fp 结合
	//(int, int)	它指向的函数，收两个 int
	//fp 是一个指针而不是函数，指向“收两个 int、返回 int”的函数。
	fp = add;

	printf("直接调用   add(3, 5) = %d\n", add(3, 5));
	printf("函数指针   fp(3, 5)  = %d\n", fp(3, 5));
	printf("另一种写法 (*fp)(3,5)= %d\n", (*fp)(3, 5));

	return 0;
}