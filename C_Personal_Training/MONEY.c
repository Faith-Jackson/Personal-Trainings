#include <stdio.h>
int main()	
{
	int daily;
	int days;
	int total1;
	int weeks;
	int total2;

	printf("What is the assigned daily wage ?\n");
	scanf("%d",&daily);

	printf("How many days in the month?");
	scanf("%i",&days);
	
	total1=daily*days;
	
	printf("Your total amount for %d days is %d Naira\n",days,total1);

	printf("How many weeks do you work in a month?");
	scanf("%d",&weeks);

	total2=total1/weeks;

	printf("Your weekly amount for %d weeks is %d Naira\n",weeks,total2);
	printf("This is a test program for Daily wages");
	return(0);
}  
