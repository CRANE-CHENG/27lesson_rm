#include <stdio.h>
#include <stdlib.h>
int add(int a,int b)
{
    int c=a+b;
    return c;
}
int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    int (*p)(int,int);
    p=&add;
    int r=p(x,y);
    printf("%d",r);
    return 0;
}