#include <stdio.h>
#include <stdlib.h>
struct Date
{
    int year;
    int month;
    int day;
} time;
int main()
{
    scanf("%d.%d.%d",&time.year,&time.month,&time.day);
    int m[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    int sum=0,i;
    for(i=1;i<time.month;i++)
    {
        sum=sum+m[i];
    }
    sum=sum+time.day;
    if(time.month>2)
    {
        if(time.year%400==0||(time.year%4==0&&time.year%100!=0))
        {
            sum=sum+1;
        }
    }
    printf("No. %d day",sum);
    return 0;
}