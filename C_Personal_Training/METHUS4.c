#include <stdio.h>
#include <stdlib.h>

int main()
{
	int diff;
	int methus;
	int you;
	char years[8];

	printf("How old are you?");
	scanf("%s",years);
	you=atoi(years);

	methus=967;
	diff=methus-you;

	printf("You are %d years younger than Methuselah\n",diff);
	return(0);
}

