#include<stdio.h>
//作业一
struct date{
    int year;
    int month;
    int day;
};
void day_of_year(int *year,int *month,int *day)
{
    int i;
    scanf("%d %d %d",year,month,day);
    i=*year;
    if ((i%4==0&&i%100!=0)||(i%400==0)){
        printf("%d是闰年\n",i);
        int b=0,a[12]={31,29,31,30,31,30,31,31,30,31,30,31};
        for(int c=0;c<*month-1;c++){
                b+=a[c];
        }
        int d=b+*day;
        printf("%d年%d月%d日是%d年第%d天",*year,*month,*day,*year,d);
    }else{
        printf("%d不是闰年\n",i);
        int b=0,a[12]={31,28,31,30,31,30,31,31,30,31,30,31};
        for(int c=0;c<*month-1;c++){
                b+=a[c];
        }
        int d=b+*day;
        printf("%d年%d月%d日是%d年第%d天",*year,*month,*day,*year,d);
    }
}
int main()
{
    struct date a;
    day_of_year(&a.year,&a.month,&a.day);
    return 0;
}
