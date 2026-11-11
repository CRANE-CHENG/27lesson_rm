#include<stdio.h>

struct Data{
    int year;
    int mouth;
    int day;

}Data1;

//算日期
int How_much_days(struct Data* a)
{
    int m[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
    //       0 1  2  3  4  5  6  7  8  9  10 11 12
    int days=0;


    if(((a->year%4==0)&&(a->year%100!=0))||(a->year%400==0))
        ++m[2];
    else
        m[2]=28;

    //加整个月
    for(int i = (a->mouth-1);i>0;i--)
        days=days + m[i];
    //  printf("该年第%d天",days);
    //加天
        days=days+ a->day;


    return days;
}

int main()
{
    
    int n;
    printf("年");
    scanf("%d",&Data1.year);
    printf("月");
    scanf("%d",&Data1.mouth);
    printf("日");
    scanf("%d",&Data1.day);
    
    n=How_much_days(&Data1);
    printf("该年第%d天",n);
    return 0;
}