#include <stdio.h>

struct Date{
    int year;
    int month;
    int day;
};

int isrun(int year)
{
    if(( year % 4 == 0 && year % 100 != 0 ) || ( year % 400 == 0 ))
    {
     return 1;
    }
return 0;
}
int riqi(struct Date d)
{   int monthdate[]={31,28,31,30,31,30,31,31,30,31,30,31};
    int sum = 0 ;
    int i;

    for(i = 0; i < d.month - 1; i++)
{
    sum += monthdate[i];
}
    sum += d.day;
    if(isrun(d.year) && d.month > 2)
    {
        sum += 1;
    }
    return sum;
}

int main(void)
{
    struct Date date;
    printf("请输入年 月 日（空格隔开）：");
    scanf("%d %d %d", &date.year, &date.month, &date.day);
    
    int res = riqi(date);
    printf("该日期是%d年的第%d天\n", date.year, res);

    return 0; 
}