#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> 
#include <string.h>

int add_count;

void *heap_note[11];

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
	if (a < 0 || a > 10)
	{
		puts("N0oOo >.<");
		exit(0);
	}
	if (add_count > 10)
	{
		puts("MAX ALLOCATIONS REACHED");
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
}

void AllocHeap()
{
	int size;
	int idx = get_idx();
	if (heap_note[idx])
	{
		puts("index already in use.");
		return;
	}
	printf("enter the size : ");
	scanf("%d", &size);
	if (size < 0 || size > 120)
	{
		printf("size is %d big? Not gonna happen :/", size);
		return;
	}
	heap_note[idx] = malloc(size);
	if((((long int)heap_note[idx] >> (8*5)) & 0xff) == 0x7f)
	{
		puts("Which year is this 2012?");
		exit(1337);
	}
	printf("Input : ");
	get_inp(heap_note[idx], size);
	puts("done !");
	add_count++;
}


void FreeHeap()
{
	int idx = get_idx();
	free(heap_note[idx]);
	puts("done !");

}

void ViewHeap()
{
	int idx = get_idx();
	if (!heap_note[idx])
	{
		puts("index doesnt exist");
		return;
	}
	printf("%s\n", (char *)heap_note[idx]);
}

int main(int argc, char const *argv[])
{
	int choice;
	setup();
	add_count=0;
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