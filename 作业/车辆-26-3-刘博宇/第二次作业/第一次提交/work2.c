#include <stdio.h>

void swap(int*x,int*y)
{
    int number=*x;
    *x=*y;
    *y=number;
}

int main(void)
{
    int a=0;
    int b=0;
    printf("请输入两个整数a,b");
    scanf("%d %d",&a,&b);
    printf("请给出交换前的数值a=%d,b=%d\n",a,b);

    swap(&a,&b);
    printf("请输出交换后的数值a=%d,b=%d\n",a,b);

    return 0;
}
