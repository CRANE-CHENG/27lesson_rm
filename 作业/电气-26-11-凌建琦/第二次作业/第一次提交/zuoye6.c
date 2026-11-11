#include<stdio.h>
int main()
{
	int n,lastcout=0;
	double cout;
	scanf("%d",&n);
	int arr[n];
	int i,j;
	for ( i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for ( j=0;j<n;j++)
	{
		lastcout=lastcout+arr[j];
	}
	cout=1.0*lastcout/n;
	printf("%.2f\n",cout);
	return 0;
}

