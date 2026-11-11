#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n = 0;
    int sum = 0;
    scanf("%d", &n);
    int *a = (int*)malloc(n * sizeof(int));
    if(a == 0){
        printf("system no function!\n");
        return 1;
    }
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
        sum += a[i];
    }
    printf("%.2f", (double)sum / n);
    free(a);
    return 0;
}