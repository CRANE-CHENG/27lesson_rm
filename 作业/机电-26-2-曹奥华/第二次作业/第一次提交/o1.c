#include<stdio.h>

typedef struct//typedef 的意思是“给这个类型起个名字叫 Date”
{
	int year;
	int month;
	int day;
}date;

int is_run(int x) {
	if (x % 400 == 0) {
		return 1;
	}
}

int day_everymonth(date d) {
	int days[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

	if (is_run(d.year)) {
		days[1] = 29;
	}
	int sum = 0;
	for (int i = 0; i < d.month - 1; i++) {
		sum += days[i];
	}
	return sum + d.day;
}

int main1() {
	date d;
	scanf("%d %d %d", &d.year, &d.month, &d.day);

	printf("%d年%d月%d日是当年的第 %d 天\n",
		d.year, d.month, d.day, day_everymonth(d));

	return 0;

}

