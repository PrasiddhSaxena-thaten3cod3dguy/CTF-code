#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("USAGE: ./test <filename>\n");
        exit(-1);
    }
    
    char cmd[100] = "/usr/bin/head ";
    strcat(cmd, argv[1]);
    system(cmd);
}