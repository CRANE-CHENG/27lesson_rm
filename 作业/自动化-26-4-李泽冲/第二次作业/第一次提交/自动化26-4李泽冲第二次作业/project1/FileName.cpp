#define _CRT_SECURE_NO_WARNINGS
#include <windows.h>
#include <stdio.h>
int main()
{
	int Date = 0;
	int year = 0;
	int month = 0;
	int day = 0;
	printf("请输入日期： 年 月 日\n");
	scanf(" %d %d %d", &year, &month, &day);
	month--;
	switch (month)
	{
	case 0:Date = day;break;
	case 1:Date = day + 31;break;
	case 2:if (year / 4 == 0)Date = day + 60;else { Date = day + 59; }break;
	case 3:if (year / 4 == 0)Date = day + 91;else { Date = day + 90; }break;
	case 4:if (year / 4 == 0)Date = day + 121;else { Date = day + 120; }break;
	case 5:if (year / 4 == 0)Date = day + 152;else { Date = day + 151; }break;
	case 6:if (year / 4 == 0)Date = day + 182;else { Date = day + 181; }break;
	case 7:if (year / 4 == 0)Date = day + 213;else { Date = day + 212; }break;
	case 8:if (year / 4 == 0)Date = day + 244;else { Date = day + 243; }break;
	case 9:if (year / 4 == 0)Date = day + 274;else { Date = day + 273; }break;
	case 10:if (year / 4 == 0)Date = day + 305;else { Date = day + 304; }break;
	case 11:if (year / 4 == 0)Date = day + 335;else { Date = day + 334; }break;
	}
	printf("这是今年的第%d天\n", Date);
}