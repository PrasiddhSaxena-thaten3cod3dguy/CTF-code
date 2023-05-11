#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> 
#include <string.h>
int i;
void setup()
{
	setvbuf(stdout, 0LL, 2LL, 0LL);
	setvbuf(stdin, 0LL, 2LL, 0LL);
	setvbuf(stderr, 0LL, 2LL, 0LL);
}

void main(int argc, char const *argv[])
{
	i=0;
	setup();
	char buf[127];
	while(i<=2)
	{
		read(0, &buf, 127);
		printf(buf);
		i+=1;
	}
}
