#include <stdbool.h>
#include <stdio.h>

struct Date {
    int year;
    int month;
    int day;
};

static bool is_leap_year(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

static int days_in_month(int year, int month)
{
    static const int days[] = {
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    };

    if (month < 1 || month > 12) {
        return 0;
    }
    if (month == 2 && is_leap_year(year)) {
        return 29;
    }
    return days[month - 1];
}

static int day_of_year(const struct Date *date)
{
    int total = 0;
    int month;

    if (date->year <= 0 || date->month < 1 || date->month > 12) {
        return -1;
    }
    if (date->day < 1 || date->day > days_in_month(date->year, date->month)) {
        return -1;
    }

    for (month = 1; month < date->month; ++month) {
        total += days_in_month(date->year, month);
    }

    return total + date->day;
}

int main(void)
{
    struct Date date;
    int result;

    printf("请输入日期（年 月 日，例如 2024 3 1）：");
    if (scanf("%d %d %d", &date.year, &date.month, &date.day) != 3) {
        fprintf(stderr, "输入格式错误。\n");
        return 1;
    }

    result = day_of_year(&date);
    if (result < 0) {
        fprintf(stderr, "日期不合法，请检查输入。\n");
        return 1;
    }

    printf("%d年%d月%d日是%d年的第%d天。\n",
           date.year, date.month, date.day, date.year, result);

    return 0;
}