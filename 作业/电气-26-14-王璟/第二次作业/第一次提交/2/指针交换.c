#include <stdio.h>
	
	void swap(int *pa,int *pb){
	int t=*pa;
	*pa=*pb;
	*pb=t;
	}
	
int main(){
	int a=1;
	int b=2;
	
	printf("a=%d,b=%d\n",a,b);
	
	swap(&a,&b);
	
	printf("a=%d,b=%d",a,b);
	
	return 0;
}
