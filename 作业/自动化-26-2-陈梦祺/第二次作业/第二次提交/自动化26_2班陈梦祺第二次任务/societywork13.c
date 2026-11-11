#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n = 0;
	int sum = 0;
	scanf("%d",&n);
	
	int *arr = malloc(n * sizeof(*arr));
	if(arr == NULL)
	{
		return 1;
	}
	for(int i = 0;i < n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(int i = 0;i < n;i++)
	{
		sum = sum + arr[i];
	}
	double a = (double)sum / n;
	printf("%.2lf",a);
	free(arr);
	return 0;
}