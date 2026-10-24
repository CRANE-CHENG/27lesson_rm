#include <iostream>
using namespace std;
int add(int a,int b)
{
    return a+b;
}
int main()
{
    int (*add_point)(int,int);
    add_point=add;
    int a,b;
    cin>>a>>b;
    cout<<add_point(a,b);



}