#include<stdio.h>
int main3() {
	int n;
	int a[100];

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}

	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += a[i];
	}

	printf("平均值为：%.2f", (double)sum / n);

	return 0;
}
