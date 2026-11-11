# include <stdio.h>

void avr(int a[],int n)
{
    int i;
    int t = 0;

    for(i = 0; i < n; ++i)
    {
        t = t + a[i];
    }
    double m;
    m = (double)t/n;
    printf("%.2lf\n",m);
}

int main(void)
{
    int n,i;
    printf("请输入数组所含元素个数：");
    scanf("%d",&n);
    
    int a[n];
    for(i = 0; i < n; i++)
    {
        printf("请输入数组中a[%d]的值", i );
        scanf("%d",&a[i]);
    }
   
    avr(a,n);
   
    return 0;
}