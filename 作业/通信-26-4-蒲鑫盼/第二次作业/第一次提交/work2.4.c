#include <stdio.h>
int add(int a, int b){
    return a + b;
}
int main()
{
    int a, b;
    int (*p)(int, int);
    scanf("%d%d", &a, &b);
    p = add;
    printf("%d\n", p(a, b));
    return 0;
}