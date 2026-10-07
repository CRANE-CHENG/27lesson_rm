#include <stdio.h>

int main()
{
	double a, b;  

    printf("输入两个数字（a和b） ，计算其加减乘除，顺序依次是加减乘除\n"); 
    scanf_s("%lf %lf", &a, &b); 

    

    printf("a+b=%f\n", a + b); 
    printf("a-b=%f\n", a - b); 
    printf("a*b=%f\n", a * b); 
    printf("a/b=%f\n", a / b); 


    
	return 0;  
}
