#include <iostream>
using namespace std;
struct date
{
    int year;
    int month;
    int day;
    int sum_date=0;
    void out()

    {
    if ((year%4==0&&year%100!=0)||(year%400==0))
    {
        
        int arr1[12]={31,29,31,30,31,30,31,31,30,31,30,31};
        for (int i=0;i<month-1;i++)
        {
            
            sum_date+=arr1[i];

        }
        sum_date+=day;
        cout<<sum_date;

    }
    else 
    {
        int arr2[12]={31,28,31,30,31,30,31,31,30,31,30,31};
        for (int i=0;i<month-1;i++)
        {
            sum_date+=arr2[i];

        }
        sum_date+=day;
        cout<<sum_date;
    }
    }

};

int main()
{
    date example;
    cin>>example.year>>example.month>>example.day;
    example.out();
}