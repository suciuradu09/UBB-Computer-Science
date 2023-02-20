#include <stdio.h>

int factorial(int);

int main()
{
	int n, f;
	printf("n = ");
	scanf("%d", &n);

	f = factorial(n);

	printf("factorial(%d) = %d\n", n, f);

	return 0;
}
