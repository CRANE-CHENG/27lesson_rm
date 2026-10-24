#include <stdio.h>

#define MAXN 100  

int main(void) {
    int n;             
    int a[MAXN];       
    double sum = 0.0;   

    printf("请输入整数的个数 n: ");
    scanf("%d", &n);

    
    if (n <= 0 || n > MAXN) {
        printf("n 不合法（应为 1 ~ %d）\n", MAXN);
        return 1;
    }

    printf("请输入 %d 个整数: ", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        sum += a[i];   
    }
    printf("平均值 = %.2f\n", sum / n);

    return 0;
}
