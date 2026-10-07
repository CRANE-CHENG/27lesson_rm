#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    long num=0xAFBECD;
    char str[64];  //一个数组装倒序数
    char b[64];    //双数组倒回正确顺序
    int i;
    i=0;
    if(num==0)     //如果16进制是0
    {
        str[i++]='0';
    } 
    while(num>0)
    {
        int rem;    //余数
        rem=num%10;
        str[i]=rem+'0';     //数字编码化
        num=num/10;
        i=i+1;
    }
    str[i]='\0';
    int j,k;
    j=0;
    for(k=i-1;k>=0;k--)     //数组顺序颠倒输出
    {
        b[j]=str[k];
        j=j+1;
    }
    b[j]='\0';
    printf("%s",b);
    system("pause");
    return 0;
}