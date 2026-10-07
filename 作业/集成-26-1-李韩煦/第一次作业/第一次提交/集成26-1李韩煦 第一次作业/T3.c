#include<stdio.h>
#include<string.h>
#include<math.h>
int main()
{
    char s[] = {"0xAFBECD"};
    //cin>>s;
    int bk = 0,x = 0;
    for(int i = strlen(s) - 1;i >= 2;i --,bk ++)
    {
        if(s[i] < 65)
            x += pow(16,bk) * (s[i] - 48);
        else
            x += pow(16,bk) * (s[i] - 55);
    }
    char ss[20];
    sprintf(ss, "%d", x);
    printf("%s", ss);
    return 0;
}