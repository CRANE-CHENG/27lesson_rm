#include<stdio.h>

typedef struct Date{
    int year;
    int month;
    int day;

}Date;
int main()
{   
    int a ;
    printf("请输入你的年分；\n");
    scanf("%d",&a);
    int c;
    c = a % 4;
    if(c == 0){
        printf("你输入的年分是闰年！\n");
        printf("请输入你想要输入的月，日\n");
        Date student;
        scanf("%d",&student.month);
        scanf("%d",&student.day);
        int commonth [12]={31,29,31,30,31,30,31,31,30,31,30,31};
        int b = 0;
        int t = 0;
        for(b = 0;b < student.month;b++)
        {
            t = commonth [b] + t;
        }
        int f;
        f = t + student.day;
        printf("您输入的日期是这一年的第%d天",f);

    }else{
        printf("您输入的年分是平年！");
        printf("请输入你想要输入的月，日\n");
        Date student;
        scanf("%d",&student.month);
        scanf("%d",&student.day);
        int commonth2 [12]={31,28,31,30,31,30,31,31,30,31,30,31};
        int d = 0;
        int e = 0;
        for(d = 0;d < student.month;d++)
        {
            e = commonth2[d] + e;
        }
        int g;
        g = e + student.day;
        printf("您输入的日期是这一年的第%d天",g);
    }
    
   return 0;
}
