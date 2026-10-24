#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    int *numbers;
    long long sum = 0;
    int i;

    printf("请输入整数个数 n：");
    if (scanf("%d", &n) != 1 || n <= 0) {
        fprintf(stderr, "n 必须是正整数。\n");
        return 1;
    }

    numbers = (int *)malloc((size_t)n * sizeof(*numbers));
    if (numbers == NULL) {
        fprintf(stderr, "内存分配失败。\n");
        return 1;
    }

    printf("请输入 %d 个整数：", n);
    for (i = 0; i < n; ++i) {
        if (scanf("%d", &numbers[i]) != 1) {
            fprintf(stderr, "第 %d 个数据输入错误。\n", i + 1);
            free(numbers);
            return 1;
        }
        sum += numbers[i];
    }

    printf("平均值为：%.2f\n", (double)sum / (double)n);

    free(numbers);
    return 0;
}