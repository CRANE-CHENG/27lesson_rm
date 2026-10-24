#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;
int main()
{
    int length,num,sum;
    sum=0;
    length=0;
    cin>>length;
    vector<int>arr;
    while(cin>>num)
    {
        arr.push_back(num);
    }
    for (int i=0;i<length;i++)
    {
         sum+=arr[i];
    }
    double average=(double)sum/length;
    cout<<fixed<<setprecision(2)<<average<<endl;
}