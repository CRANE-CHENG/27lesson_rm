#include <stdio.h>
void swap(int *x, int *y) {
    int temp = *x; 
    *x = *y;       
    *y = temp;      
}

int main(void) {
    int a, b;

    printf("请输入两个整数: ");
    scanf("%d %d", &a, &b);

    printf("交换前: a = %d, b = %d\n", a, b);

   
    swap(&a, &b);

    printf("交换后: a = %d, b = %d\n", a, b);

    return 0;
}
