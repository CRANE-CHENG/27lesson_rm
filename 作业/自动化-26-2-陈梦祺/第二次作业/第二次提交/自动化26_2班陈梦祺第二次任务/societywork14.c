#include<stdio.h>
int add(int a,int b)
{
    return a + b;
}
int main()
{
    int (*pf)(int a,int b) = add;
    int sum = (*pf)(2,3);
    printf("%d",sum);
    return 0;
}
