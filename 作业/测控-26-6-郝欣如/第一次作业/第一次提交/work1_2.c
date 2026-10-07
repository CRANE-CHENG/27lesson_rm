# include <stdio.h>

int main(void)
{
    float a,b,c,d,e,f;
    printf("请输入a、b的值:");
    scanf("%f,%f",&a,&b);// scanf("%f %f",&a,&b)也能运行，对应输入的a、b的值可用空格隔开，也可以用，隔开。但注意对应关系
    
    c = a + b;
    d = a - b;
    e = a * b;
    f = a / b;

    printf("a + b = %f\n",c);
    printf("a - b = %f\n",d);
    printf("a * b = %.2f\n",e);
    printf("a / b = %.2f\n",f);
    
    return 0;
}