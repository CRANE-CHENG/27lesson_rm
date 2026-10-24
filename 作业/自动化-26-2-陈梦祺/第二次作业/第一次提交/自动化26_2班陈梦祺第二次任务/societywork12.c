#include<stdio.h>
void swap(int *x,int *y)
{
    int tem = 0;
    tem = *x;
    *x = *y;
    *y = tem;
}
int main()
{
    int a = 8;
    int b = 9;
    swap(&a,&b);
    printf("%d %d",a,b);
    return 0;
}