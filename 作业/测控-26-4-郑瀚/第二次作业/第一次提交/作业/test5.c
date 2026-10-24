#include<stdio.h>

int add (int a,int b)
{
    int c;
    c = a + b;
    return c;
}
int main() {
    int a = 5;
    int b = 6;
    int (*sum)(int,int);
    sum = &add;
    int result = 0;
    result = sum(a,b);
    printf("%d",result);

    return 0;
}