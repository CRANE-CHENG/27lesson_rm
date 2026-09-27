#include<stdio.h>


int main(void)
 {
    int x = 0xAFBECD;//已知的十六进制数字
    char str[10];//已知该数字换为十进制为11517645，所以十位足够
    int i = 0;
    while (x > 0)
        {
            str[i] = (x % 10) + '0';
            i++;
            x /= 10;
        }
        str[i] = '\0';

    
    for (int j = 0; j < i / 2; j++)//因为所得字符串和最终结果是相反的所以要换位，i是位数只需翻转i/2（取整）次
        {
            char t = str[j];
            str[j] = str[i - 1 - j];
            str[i - 1 - j] = t;
        }

        printf("转化结果为%s\n", str);
        return 0;
}