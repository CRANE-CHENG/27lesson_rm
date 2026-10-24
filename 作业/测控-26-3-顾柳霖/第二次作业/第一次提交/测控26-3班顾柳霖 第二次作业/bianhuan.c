#include <stdio.h>

void swap(int *x, int *y)
{
    int jiaohuan;
    jiaohuan = *x;  
    *x = *y;    
    *y = jiaohuan;  
}

int main(void)
{
    int a, b;
    printf("请输入两个整数a,b：");
    scanf("%d %d", &a, &b);

    printf("交换前：a = %d, b = %d\n", a, b);
    swap(&a, &b);  // 传入变量地址
    printf("交换后：a = %d, b = %d\n", a, b);

    return 0;
}