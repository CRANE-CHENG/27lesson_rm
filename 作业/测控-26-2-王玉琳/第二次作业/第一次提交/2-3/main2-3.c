#define  _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void){
	int a;
	double x = 0;
	int num[9999];//创建一个较大数组，以装下足够多的所求数
	printf("请输入需要求平均数的整数的个数：\n");
	scanf("%d",&a);
	for (int i = 0; i <a;i++) {
		printf("请输入第%d个数：\n",i+1);
		scanf("%d", &num[i]);
	}//创建for循环，持续提示从第1输入到第a个数，并将数依次填入数组直到num[a-1]
	for (int i = 0;i < a;i++) {
		x = x + num[i];
	}//从数组中以此累加数
	x = x / a;//求平均数
	printf("这%d个数的平均值为%.2f", a, x);
	return 0;
}