#include <stdio.h>

int add(int a,int b){
	int c=a+b;
	return c;
}

int main(){
	int (*p)(int,int)=add;
	
	int c=p(1,2);
	
	printf("%d",c);
	
	return 0;
}
