#include <stdio.h>

int main()
{
	double a = 0; 
	double b = 0; 

    printf("输入两个数字（a和b，数字先后顺序为a，b） ，计算其加减乘除，顺序依次是加减乘除\n"); 
    scanf_s("%lf %lf", &a, &b); 

    

    printf("a+b=%f\n", a + b); 
    printf("a-b=%f\n", a - b); 
    printf("a*b=%.2f\n", a * b); 
    printf("a/b=%.2f\n", a / b); 


    
	return 0;  
}
