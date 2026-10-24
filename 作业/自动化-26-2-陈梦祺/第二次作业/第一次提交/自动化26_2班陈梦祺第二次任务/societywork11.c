#include <stdio.h>
struct date
{
    int year;
    int month;
    int day;
};
int main()
{
    int month[12] = { 31,28,31,30,31,30,31,31,30,31,30,31};
    int sum = 0;
    struct date s1;
    scanf("%d%d%d",&s1.year,&s1.month,&s1.day);
    if((s1.year % 4 == 0 &&  s1.year %100 != 0)||(s1.year % 400 == 0))//闰年判断
        {
            month[1]++;
        }
    for(int i = 0; i < s1.month - 1;i++)
    {
        sum = sum + month[i];
    }
    sum = sum + s1.day;
    printf("%d",sum);
    return 0;
}