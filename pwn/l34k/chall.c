#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> 
#include <string.h>

void setup()
{
	setvbuf(stdout, 0LL, 2LL, 0LL);
	setvbuf(stdin, 0LL, 2LL, 0LL);
	setvbuf(stderr, 0LL, 2LL, 0LL);
}

int main(int argc, char const *argv[])
{
	char name[512];
	setup();
	printf("Enter your name : ");
	gets(name);
	puts("See you again ;)");
	return 0;
}