#include <stdio.h>
int main()
{
	char kitty[20]
	
	printf("What would you like to name your cat?");
	scanf("%s",kitty);
	printf("%s is a nice name. What else do you have in mind?",kitty);
	scanf("%s",kitty);
	printf("%s is nice, too.\n",kitty);
	return(0);
}
