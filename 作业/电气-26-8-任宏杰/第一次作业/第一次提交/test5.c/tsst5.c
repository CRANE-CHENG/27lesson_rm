#include<stdio.h>
int main(){
    int ab = 0xAFBECD;
    char abcd[20];
    sprintf(abcd, "%d", ab);
    printf("十六进制 0xAFBECD 对应的十进制为; %s\n",abcd);
    return 0;
}