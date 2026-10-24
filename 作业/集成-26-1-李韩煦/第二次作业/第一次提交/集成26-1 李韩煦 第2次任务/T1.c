#include<stdio.h>

struct Date
{
    int y,m,d;
}D;

int main()
{
    scanf("%d %d %d",&D.y,&D.m,&D.d);
    D.m --;
    int sum = 30 * D.m + D.d;
    if(D.m >= 2)sum -= 2;
    if(D.m >= 1)sum ++;
    if(D.m >= 3)sum ++;
    if(D.m >= 5)sum ++;
    if(D.m >= 7)sum ++;
    if(D.m >= 8)sum ++;
    if(D.m >= 10)sum ++;
    if(D.m >= 12)sum ++;
    if((D.y % 4 == 0 && D.y % 100 != 0) || D.y % 400 == 0)sum ++;
    printf("%d",sum);
    return 0;
}