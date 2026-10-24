#include <stdio.h>

struct Date
{
    int year;
    int month;
    int day;
};

int main(void)
{
    int a[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};

    struct Date today;
    int sum=0;

    printf("请输入年月日");
    scanf("%d %d %d",&today.year,&today.month,&today.day);

    int r=0;
    if ((today.year%4==0 && today.year%100!=0)||(today.year%400==0))
    {
        r=1;
    }
    
     for ( int i = 1; i < today.month; i++)
    {
        sum+=a[i];
    }
    
    sum+=today.day;

    if (r==1 && today.month>2)
    {
        sum+=1;
    }
    
    printf("该日期是当年的第%d天\n",sum);

    return 0;
}