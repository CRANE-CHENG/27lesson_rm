#include <stdio.h>
	struct Date 
	{
        int year,month,day,mday,lastcout;
    };
int main()
    {
    struct Date d;
    int i;
    d.lastcout=0;
    scanf("%d %d %d", &d.year, &d.month, &d.day);
    for(i=1;i<d.month;i++)
    {
	
    switch(i)
    {
        case 1: 
        case 3: 
        case 5:
        case 7: 
        case 8: 
        case 10: 
        case 12: d.mday = 31; break;
        case 4: 
        case 6: 
        case 9: 
        case 11: d.mday = 30; break;
        case 2:

            if( (d.year % 4 == 0 && d.year % 100 != 0) || (d.year % 400 == 0) )
                d.mday = 29;
            else
                d.mday = 28;
            break;
    }
    d.lastcout=d.lastcout+d.mday;
    }
    d.lastcout=d.lastcout+d.day;
    
    printf("%d", d.lastcout);
    return 0;
}





