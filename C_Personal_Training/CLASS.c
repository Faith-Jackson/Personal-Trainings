#include <stdio.h>
#include <stdlib.h>

int main()
{
    int diff;
    int total;
    int male;
    int female;

    printf("How many students are in the class?\n");
    scanf("%d", &total);

    printf("How many male?\n");
    scanf("%d", &male);

    printf("How many female?\n");
    scanf("%d", &female);

    diff = total - male - female;

    printf("The total number of students in your class is %d\nMale is %d\n Female is %d\n And unknown students are %d\n", total, male, female, diff);

    return 0;
}
