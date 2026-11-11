# include <stdio.h>

void swap(int * x,int * y)
{
    int t;
    t = *x;
    *x = *y;
    *y = t;
}
int main(void)
{
    int a,b;
    printf("请输入a、b的值");
    scanf("%d %d",&a,&b);

    swap(&a,&b);
    printf("互换之后a = %d,b = %d\n",a,b);
    return 0;
}