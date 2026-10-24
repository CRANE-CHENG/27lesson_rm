#include <stdio.h>

struct Date
{
	int year; int month; int day;
};
	
int main()
{
	int i; int sum=0;
	struct Date d;
	int arr[]={0,31,28,31,30,31,30,31,31,30,31,30,31}; 
	//数里第一个值为0，使得arr[i]中的i与月份一一对应 
	printf("请输入一个日期\n");
	scanf("%d.%d.%d",&d.year,&d.month,&d.day);
	for(i=1;i<d.month ;i++)
	{
		sum+=arr[i];
	} 
	sum+=d.day ; 
	if((d.year %4==0&&d.year %100!=0)||d.year %400==0)
	{
		if(d.month >2)
		sum+=1;
	}
	printf("%d年%d月%d日是第%d天",d.year ,d.month ,d.day ,sum);
	return 0;
} 
