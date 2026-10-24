#include<stdio.h>
#include<math.h>
int main(void) {
	int a;
	a = 10 * pow(16, 5) + 15 * pow(16, 4) + 11 * pow(16, 3)
		+ 14 * pow(16, 2) + 12 * pow(16, 1) + 13 * pow(16, 0);//每位数字乘对应权值求和得到十进制结果
	printf("十六进制数0xAFBECD对应的十进制数为：%d\n", a);
	return 0;
}
