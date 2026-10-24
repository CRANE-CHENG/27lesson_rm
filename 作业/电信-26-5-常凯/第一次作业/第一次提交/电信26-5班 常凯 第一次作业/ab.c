#include <stdio.h>
int main() {
	float a, b;
	printf("输入两个数 ");
	scanf("%f %f", &a, &b);
	printf("a*b=%.2f\n", a * b);
	while (b == 0) {
		printf("你不乘，第二个不能是零 ");
		scanf("%f", &b);
	}
	if (b != 0){
		printf("a/b=%.2f\n", a / b);
}
	return 0;
}              
