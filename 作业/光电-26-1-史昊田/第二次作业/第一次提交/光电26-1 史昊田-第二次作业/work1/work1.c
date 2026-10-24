
#include <stdio.h>
#include <stdlib.h>
struct Date
{
    int year;
    int month;
    int day;
};


int is_leap_year(int year)//闰年判断函数
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int day_of_year(const struct Date *date)
{
    const int days_in_month[12] = {31, 28, 31, 30, 31, 30,
                                   31, 31, 30, 31, 30, 31};
    int total = 0;
    int i;

    if (date->year < 1 || date->month < 1 || date->month > 12 ||
        date->day < 1 ||
        date->day > days_in_month[date->month - 1] +
                        (date->month == 2 && is_leap_year(date->year)))
    {
        return -1;
    }

    for (i = 0; i < date->month - 1; i++)
    {
        total += days_in_month[i];
    }

    total += date->day;
    if (date->month > 2 && is_leap_year(date->year))
    {
        total += 1;
    }

    return total;
}

int main(void)
{
    struct Date date;
    int result;

    printf("请输入日期（年 月 日）：");
    if (scanf("%d %d %d", &date.year, &date.month, &date.day) != 3)
    {
        printf("输入格式错误。\n");
        return 1;
    }

    result = day_of_year(&date);
    if (result < 0)
    {
        printf("日期不合法。\n");
        return 1;
    }

    printf("%d年%d月%d日是该年的第%d天。\n",
           date.year, date.month, date.day, result);
           system("pause");
    return 0;
}
