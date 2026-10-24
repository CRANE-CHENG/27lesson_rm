#include <stdio.h>

int add(int a,int b)
{
    return a+b;
}

int main(void)
{
    int(*p)(int ,int);
    p=add;
    int x,y;
    printf("请输入x y");
    scanf("%d %d",&x,&y);
    int res=p(x,y);
    printf("结果=%d\n",res);

    return 0;
}
