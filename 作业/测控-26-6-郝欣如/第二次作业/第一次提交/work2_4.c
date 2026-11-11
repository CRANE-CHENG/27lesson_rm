# include <stdio.h>

int add(int a,int b)
{
    return a + b;
}

int main(void)
{
    int a;
    int b;

    scanf("%d %d",&a,&b);

    int (* p) (int a,int b);
    p = add;

    int c = p(a,b);
    
    printf("%d",c);
    
    return 0;
}