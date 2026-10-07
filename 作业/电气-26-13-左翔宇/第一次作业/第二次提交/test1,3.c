#include <stdio.h>
int main (){
    int num =0xAFBECD;
    char str[20];
    sprintf(str,"%d",num);
    printf("%s\n",str);
    return 0;
}