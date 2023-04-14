#include<stdio.h>

/*
 * This progrma prints the details of
 * the author of this directory
 *
 * Code developed by Masino
 */

int main(void)
{
	char name1[20], name2[10];

	printf("Please enter your name here: ");
	scanf("%s %s", name1, name2);
	printf("\nGot it!!!\nThanks for tuning in %s %s\n", name1, name2);
	printf("\nThe details of the author are:\n");
	printf("\nName: Johnson Masino.\nGitHub: JohnsonMasino\nPhone: +249036206457\n");
	printf("\nMail: jonsonmasino@gmail.com.\nSchool: Holberton School.\n");
	printf("\nDone!\nCode developed by Masino\n");
	return (0);
}
