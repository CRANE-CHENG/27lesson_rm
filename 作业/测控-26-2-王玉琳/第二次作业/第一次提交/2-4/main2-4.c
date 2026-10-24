#include<stdio.h>
int add(int a, int b) {
	return a + b;//定义函数，返回a+b的结果
}
int main(void) {
	int(*p)(int a,int b);//声明函数指针p，指向接收两个int参数且返回int的函数
	p = add;//p指向add函数的地址
	int c = p(2, 5);//指针调用函数
	printf("%d", c);
	return 0;
}