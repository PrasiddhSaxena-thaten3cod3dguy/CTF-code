#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> 
#include <string.h>

#define add_count 0
void *note[10];

void setup()
{
	setvbuf(stdout, 0LL, 2LL, 0LL);
	setvbuf(stdin, 0LL, 2LL, 0LL);
	setvbuf(stderr, 0LL, 2LL, 0LL);
}

int get_option()
{
	int a;
	puts("1.) Alloc");
	puts("2.) Free");
	puts("3.) View");
	puts("4.) Exit");
	printf("> ");
	scanf("%d", &a);
	return a;
}

int get_idx()
{
	int a;
	printf("enter the index : ");
	scanf("%d", &a);
	if (a < 0 || a >= 10)
	{
		puts("N0oOo >.<");
		exit(0);
	}
	if (add_count > 12)
	{
		puts("Maximum Allocations reached => Pain ;)");
		exit(0);
	}
	return a;
}

void get_inp(char *buf, int size)
{
	int i;
	i=read(0, buf, size);
	if (i<= 0)
	{
		puts("read error");
		exit(1);
	}
	buf[i]='\0';
}

void AllocHeap()
{
	int idx, size=0;
	idx = get_idx();
	if (note[idx] != 0)
	{
		puts("index already in use.");
		return;
	}
	printf("enter the size : ");
	scanf("%d", &size);
	if (size < 0 || size > 0x100)
	{
		printf("size is %d big? Not gonna happen :/", size);
		return;
	}
	note[idx] = malloc(size);
	printf("Input : ");
	get_inp(note[idx], size);
	puts("done !");
	add_count++;
}


void FreeHeap()
{
	int idx = get_idx();
	if (note[idx] == 0)
	{
		puts("No Double free ,-0-0");
		return;
	}
	free(note[idx]);
	note[idx]=0;
	printf("done !");

}

void ViewHeap()
{
	int idx = get_idx();
	printf("%s\n", note[idx]);
}

int main(int argc, char const *argv[])
{
	int choice;
	setup();
	while (1)
	{
		choice = get_option();
		switch(choice)
		{
			case 1: AllocHeap();
					break;
			case 2: FreeHeap();
					break;
			case 3: ViewHeap();
					break;
			case 4: exit(0);
					break;
			default: puts("Invalid Option");
					break;
		}
	}
	return 0;
}