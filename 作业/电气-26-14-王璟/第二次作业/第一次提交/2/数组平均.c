#include <stdio.h>

int main(){
	int a[3];
	int i;
	double sum=0.0;
	for(i=0;i<3;i++){
		scanf("%d",&a[i]);
		sum+=a[i];
	}
	printf("%.2f",sum/i);
	return 0;
}
