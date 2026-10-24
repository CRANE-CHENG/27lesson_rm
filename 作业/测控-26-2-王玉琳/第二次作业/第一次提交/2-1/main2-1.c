#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	typedef struct { int y;int m;int d; }Date;//定义结构体Date
	Date a;
	printf("请输入年 月 日(空格隔开)：\n");
	scanf("%d %d %d",&a.y,&a.m,&a.d);//scanf分别访问变量
	int m[12]={0,31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 };//按每一年中的第几个月份累加天数，0代表1月不加仅加a.d,十二月仅加前十一月和a.d
	int b=0;
	if ((a.y % 4 == 0 && a.y % 100 != 0) || a.y % 400 == 0) {}//闰年判断,闰年则不执行任何操作
	else
	{
		m[2] = 28;//若该年非闰年，则将二月天数改为28天
		}
	for(int i=0;i<a.m;i++){
		b = b + m[i];         //累加月份天数，累加到第a.m-1月
	}
		b = b + a.d;          //前a-1月求和后加上第a月天数
		printf("这是这一年的第%d天", b);
	return 0;
}