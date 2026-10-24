#include <stdio.h>

int main()
{
    int n, i;
    int sum = 0;       
    double num;     
    printf("请输入整数的个数 n: ");
    scanf("%d", &n);
    int arr[n];       
    printf("请输入 %d 个整数: ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];  
    }

     num = sum / n;  

    printf("平均值为: %.2f\n", num);

    return 0;
}
