#include <iostream>
#include <stdio.h>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {

    // read input into our local variable
    char input[2];
    cout << "length of input: "<< strlen(argv[1]) << endl;
    printf("%s\n", argv[1]);
    int size = strlen(argv[1]);
    for (int i=0; i < size; i++) {
        input[i] = argv[1][i];
    }

    printf("%s\n", input);



}