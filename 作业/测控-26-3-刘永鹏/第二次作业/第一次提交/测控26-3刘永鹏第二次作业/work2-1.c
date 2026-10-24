#include <stdio.h>
struct Date {
    int year;   
    int month;  
    int day;    
};
int isLeap(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}
int dayOfYear(struct Date d) {
    int days[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if (isLeap(d.year)) {
        days[2] = 29;  
    }
    int sum = 0;
    for (int i = 1; i < d.month; i++) {
        sum += days[i];
    }
    return sum + d.day; 
}
int main(void) {
    struct Date d;

    printf("请输入日期(年 月 日): ");
    scanf("%d %d %d", &d.year, &d.month, &d.day);
    int maxDay;
    if (d.month == 2) {
        maxDay = isLeap(d.year) ? 29 : 28;
    } else if (d.month == 4 || d.month == 6 || d.month == 9 || d.month == 11) {
        maxDay = 30;
    } else {
        maxDay = 31;
    }

    if (d.month < 1 || d.month > 12 || d.day < 1 || d.day > maxDay) {
        printf("日期不合法\n");
        return 1;
    }

    printf("%d年%d月%d日是该年的第 %d 天\n", d.year, d.month, d.day, dayOfYear(d));
    return 0;
}