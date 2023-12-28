#include <stdio.h>
int main()
{
	char name[20];
	char color[20];

	printf("What is your name?\n");
	scanf("%s",name);
	printf("What is your favourite color?\n");
	scanf("%s",color);
	printf("%s's favourite colour is %s.",name,color);
	return(0);
}
