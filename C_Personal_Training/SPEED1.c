#include <stdio.h>

#define SPEED 55 //Accepted speed limit

int main()
{
	printf("The accepted Speed limit is %i\n",SPEED);
	printf("But you did over %i MPH\n",75);
	printf("You went over %i MPH to the accepted speed limit\n",75-SPEED);

	return(0);
}
