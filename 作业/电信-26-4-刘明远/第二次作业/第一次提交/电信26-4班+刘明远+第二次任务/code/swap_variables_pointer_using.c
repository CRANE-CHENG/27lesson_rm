#include <stdio.h>
#include <stdlib.h>
void swap(int *x,int *y)
{
    int t=*x;
    *x=*y;
    *y=t;
}
int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    swap(&x,&y);
    printf("%d %d",x,y);
    return 0;
}