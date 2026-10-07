#include <stdio.h>
int main (){
    double a,b;
    printf("输入两个数");
    scanf("%lf %lf",&a,&b);
    printf("a*b=%.2f\n",a*b);

    while (b==0) {
        printf("b不能为零,换一组数试试吧\n");
        
        
        while(getchar() !='\n');//D指导让加的，还有点不懂
        
        scanf("%lf %lf",&a,&b);//重输a,b值
    }
    if (b!=0){
        printf("a/b=%.2f\n",a/b);
    }
    return 0;



}