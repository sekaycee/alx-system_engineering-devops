#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - create an infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Entry point
 * Return: Always 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	return (infinite_while());
}
