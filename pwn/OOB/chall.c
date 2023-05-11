#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> 
#include <string.h>
#include <assert.h>

char *buf;

void setup()
{
	setvbuf(stdout, 0LL, 2LL, 0LL);
	setvbuf(stdin, 0LL, 2LL, 0LL);
	setvbuf(stderr, 0LL, 2LL, 0LL);
}

int getInt()
{
	int i;
	int a[10];
	puts("Give some space for the array to fit in the stack\nEnter the integers for now... \n");
	for (int i = 0; i <= 17; ++i)
	{
		scanf("%d", &a[i]);
	}
	return i;

}

int main(int argc, char const *argv[])
{
	setup();
	int a[10];
	printf("Very well then lets learn to input a string but length matters? Nah\n");
	puts("Here goes the string");
	read(0, &buf, 216);
	getInt();
	close(1);
	close(2);
	return 0;
}
