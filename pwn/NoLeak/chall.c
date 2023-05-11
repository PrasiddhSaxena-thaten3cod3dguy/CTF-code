#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> 
#include <string.h>

int add_count;

struct node {
   int size;
   void *buf;
};

struct node *heap_note[12];

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
	puts("4.) Edit");
	puts("5.) Exit");
	printf("> ");
	scanf("%d", &a);
	return a;
}

int get_idx()
{
	int a;
	printf("enter the index : ");
	scanf("%d", &a);
	if (a < 0 || a >= 11)
	{
		puts("N0oOo >.<");
		exit(0);
	}
	if (add_count >= 11)
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

void EditHeap()
{
	int idx = get_idx();
	if (!heap_note[idx])
	{
		puts("index not in use.");
		return;
	}
	else
	{
		printf("Input : ");
		get_inp(heap_note[idx]->buf, heap_note[idx]->size);
	}
}

void AllocHeap()
{
	int idx = get_idx();
	if (heap_note[idx])
	{
		puts("index already in use.");
		return;
	}
	else
	{
		heap_note[idx] = (struct node *)malloc(sizeof(struct node));
		printf("enter the size : ");
		scanf("%d", &heap_note[idx]->size);
		if (heap_note[idx]->size < 0 || heap_note[idx]->size > 0x100)
		{
			printf("size is %d big? Not gonna happen :/", heap_note[idx]->size);
			return;
		}
		heap_note[idx]->buf = malloc(heap_note[idx]->size);
		printf("Input : ");
		get_inp(heap_note[idx]->buf, heap_note[idx]->size);
		puts("done !");
		add_count++;
	}
}


void FreeHeap()
{
	int idx = get_idx();
	free(heap_note[idx]->buf);
	free(heap_note[idx]);
	puts("done !");

}

void ViewHeap()
{
	puts("Not Implemented :0");
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
			case 4: EditHeap();
					break;
			case 5: exit(0);
					break;
			default: puts("Invalid Option");
					break;
		}
	}
	return 0;
}