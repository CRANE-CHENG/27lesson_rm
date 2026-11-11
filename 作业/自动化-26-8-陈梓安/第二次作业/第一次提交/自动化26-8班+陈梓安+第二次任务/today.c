#include<stdio.h>
#include<stdbool.h>

    struct point{
    int day;
    int month;
    int year;
    };

    bool isleap(struct point date)
{
    bool leap = false;
    if((date.year % 4 == 0 && date.year % 100 !=0 ) || (date.year % 400 == 0 )){
        leap = true;
    }
    return leap;
}

int main()
{
    int i;
    int days = 0;
    struct point date;
    const int m[12] = {31,28,31,30,31,30,31,31,30,31,30,31}; 
    scanf("%d %d %d", &date.year, &date.month, &date.day);
    for( i = 0; i < date.month - 1; i++){
        if( i == 1 && isleap(date)){
            days += 29;
            continue;
        }
        days += m[i];
    }
    printf("%d", days += date.day);
    return 0;
}

