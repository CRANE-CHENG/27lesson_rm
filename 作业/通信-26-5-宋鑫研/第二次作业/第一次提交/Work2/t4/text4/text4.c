#include<stdio.h>

int Add(int x,int y)
{
    return x+y;

}

int main()
{
    int x,y;

    int (*pf)(int ,int)=Add;

    scanf("%d%d",&x,&y);
    int c=(*pf)(x,y);
    printf("%d",c);

    return 0;
}