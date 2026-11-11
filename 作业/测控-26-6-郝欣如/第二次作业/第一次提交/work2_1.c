# include <stdio.h>
struct Date
{
    int year;
    int month;
    int day;
};
int main (void)
{
    int a = 0;
    int i;
    int b[12] = {31,29,31,30,31,30,31,31,30,31,30,31};
    struct Date today;
    
    printf("请输入今天日期：");
    scanf("%d年%d月%d日",&today.year,&today.month,&today.day);

    if(today.month > 2)
    {
        if ( (today.year % 4 == 0 && today.year % 100 != 0) || (today.year % 400 == 0) )
        {
            for(i = 0; i < today.month - 1; ++i)
            {
                a = a + b[i];
            }
            a = a + today.day;
        }
        else
        {
             for(i = 0; i < today.month - 1; ++i)
            {
                a = a + b[i];
            }
            a = a + today.day - 1;

        };
        printf("今天是今年的第%d天",a);

    }
    
    else
    {
        a = today.day;
        if(today.month == 1)
        {
            printf("今天是今年的第%d天",a);
        }
        else
        {
            a = a + 30;
        printf("今天是今年的第%d天",a);
        }

    }

    return 0;
}  