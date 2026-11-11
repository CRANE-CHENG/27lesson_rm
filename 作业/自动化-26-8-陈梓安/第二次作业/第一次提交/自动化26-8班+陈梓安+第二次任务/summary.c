#include<stdio.h>

int add(int a, int b)
{
    return(a + b);
}

int main()
{
    int a, b;
    int (*p)(int a, int b);
    p = add; 
    scanf("%d %d", &a, &b);
    int result = (*p)(a, b);
    printf("%d", result);
    return 0;
}