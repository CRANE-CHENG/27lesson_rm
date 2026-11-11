#include<stdio.h>



void swap(int**one,int**two)
//          x    y
{
    int*c,* d;
    c=*one;//x记录的地址
    d=*two; //y及的地址
    *one=d;
    *two=c;
    
    
}

// int add(int add1,int add2)//
// {
//     int a,b;
//     add1++;
//     add2--;
//     a=add1;
//     b=add2;


//     return(a,b);
// }

int main()
{
    int a=2,b=15,*x=&a,*y=&b;
    printf("x=%p,y=%p\n",x,y);
    swap(&x,&y);
    //y=swap和(x,y)=swap(&x,&y)等价

    printf("x=%p,y=%p",x,y);

    //(a,b)=add(a,b);经过对比：（a，b）只穿后面数值
    // printf("\n%d %d",a,b);
    return 0;
}