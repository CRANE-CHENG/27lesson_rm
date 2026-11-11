#include <stdio.h>
struct Date
{
    int year;
    int month;
    int day;
};
int main()
{
    struct Date d;
    int a[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int sum = 0;
    scanf("%d%d%d", &d.year, &d.month, &d.day);
    if ((d.year % 4 == 0 && d.year % 100 != 0) || d.year % 400 == 0)
    {
        a[1] = 29;
    }
    for (int i = 0; i < d.month - 1; i++)
    {
        sum += a[i];
    }
    sum += d.day;
    printf("%d\n", sum);
    return 0;
}