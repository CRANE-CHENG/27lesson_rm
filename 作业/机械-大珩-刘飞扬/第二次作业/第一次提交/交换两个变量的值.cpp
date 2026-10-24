#include <iostream>
using namespace std;
void swap(int *x,int *y)
{
    int temp=*x;
    *x=*y;
    *y=temp;
    cout<<*x<<" "<<*y<<endl;
}
int main()
{
    int a,b;
    a=1100;
    b=130;

    swap(&a,&b);
}