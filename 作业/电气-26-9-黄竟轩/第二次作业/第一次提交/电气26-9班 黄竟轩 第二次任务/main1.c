#include <stdio.h>

struct Date
{
    int y,m,d;   
};

int main()
{
    struct Date d;
    int days[13]={0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int sum=0;
    int i;
    scanf("%d %d %d", &d.y, &d.m, &d.d);
    if((d.y%4==0 && d.y%100!=0) || d.y%400==0)
    {
        days[2]=29;
    }
    for(i=1; i<d.m; i++)
    {
        sum=sum+days[i];
    }
    sum=sum+d.d;
    printf("%d", sum);
    return 0;
}
