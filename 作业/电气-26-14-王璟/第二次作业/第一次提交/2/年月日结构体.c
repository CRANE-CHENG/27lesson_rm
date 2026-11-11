#include <stdio.h>

struct Date{
	int year;
	int month;
	int day;
	};

int main(){
	int month[12]={31,28,31,30,31,30,31,31,30,31,30,31};
	int sum=0;
	int i;
	
	struct Date d;
	scanf("%d %d %d",&d.year,&d.month,&d.day);
	
	if((d.year%4==0&&d.year%100!=0)||d.year%400==0){
		month[1]=29;
	}
	
	for(i=0;i<d.month-1;i++){
		sum+=month[i];
	}
	
	sum+=d.day;
	printf("%d",sum);
	
	return 0;
}
