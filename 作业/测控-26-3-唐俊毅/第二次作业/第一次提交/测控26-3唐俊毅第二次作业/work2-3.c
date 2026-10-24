#include<stdio.h>
int int_add(int a,int b)
{
    int c;
    c=a+b;
    return c;
}
int main()
{
    int a,b,c;
    scanf("%d %d",&a,&b);
    c=int_add(a,b);
    printf("a+b=%d",c);
    return 0;
}