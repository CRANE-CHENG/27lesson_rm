#include <stdio.h>

int main(void)
{
    int n, i;
    int arr[100];   
    double sum = 0, avg;

    printf("请输入数字个数n：");
    scanf("%d", &n);

    printf("请输入%d个整数：", n);
    for(i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    avg = sum / n;
    printf("平均值为：%.2f\n", avg);

    return 0;
}
