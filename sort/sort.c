#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include "heapsort.h"
#include "mergesort.h"
#include "quicksort.h"
#include "radixsort.h"
#include "randomsort.h"
#define SIZE 4096


char* trim(char *str) {
    int length = strlen(str);
    while (length > 0 && isspace((unsigned char)str[length - 1])) {
        length--;
    }
    str[length] = '\0';
    return str;
}

char *to_uppercase(char *str){
    for (int i = 0; str[i] != '\0'; i++) {
        str[i] = toupper((unsigned char)str[i]);
    }
    return str;
}

int main(int argc,char* argv[]){
    FILE *file;
    if(argc == 1 || (argc == 2 && !strcmp(argv[1], "-"))){
        file = stdin;
    } else if(!strcmp(argv[1],"-h")||!strcmp(argv[1],"--help")){
        printf("sort [OPTION]... [INPUT]\n");
        printf("Sorts the lines from INPUT (or standard input).\n");
        printf("OPTIONS:\n");
        printf("With no FILE, or when FILE is -, read standard input\n");
        printf("-m, --merge-sort Merge Sort\n");
        printf("-q, --quick-sort Quick Sort\n");
        printf("-R, --random-sort Random Sort\n");
        printf("-r, --radix-sort Radix Sort\n");
        printf("-u, print unique elements\n");
        return 0;
    }else{
        char* path = argv[argc-1];
        file = fopen(path, "r");
        if(file == NULL){
            printf("sort: %s No such file or directory",path);
            return 1;
        }
    }
    char c;
    int i = 0,size=0;
    char* data = (char*)malloc(sizeof(char) * SIZE);
    int capacity = SIZE;
    while((c=fgetc(file))!=EOF){
        if(i >= capacity - 1){
            capacity *= 2;
            data = realloc(data, capacity);
        }
        if(c=='\n') size++;
        data[i] = c;
        i++;
    }
    size++;
    data[i] = '\0';
    i=0;
    char* arr[size];
    char* token = strtok(data, "\n");
    while (token != NULL) {
        token = trim(token);
        if(token!="\0"){
            arr[i]=token;
        }
        i++;
        token = strtok(NULL, "\n");
    }
    bool is_unique = false;
    int sort_type = 0;
    for(int i=1;i<argc-1;i++){
        if(!strcmp(argv[i],"-u")){
            is_unique = true;
        }else if(!strcmp(argv[i],"-R")||!strcmp(argv[i],"--random-sort")||!strcmp(argv[i],"-sort=random")){
            sort_type = 4;
        }else if(!strcmp(argv[i],"-q")||!strcmp(argv[i],"--quick-sort")||!strcmp(argv[i],"-sort=quick")){
            sort_type = 1;
        }else if(!strcmp(argv[i],"-h")||!strcmp(argv[i],"--heap-sort")||!strcmp(argv[i],"-sort=heap")){
            sort_type = 2;
        }else if(!strcmp(argv[i],"-r")||!strcmp(argv[i],"--radix-sort")||!strcmp(argv[i],"-sort=radix")){
            sort_type = 3;
        }else{
            sort_type = 0;
        }
    }
    
    switch(sort_type){
        case 0:
        merge_sort(arr,0,size-1);
        break;
        case 1:
        quick_sort(arr,0,size-1);
        break;
        case 2:
        heap_sort(arr,size);
        break;
        case 3:
        radix_sort(arr,size);
        break;
        case 4:
        random_sort(arr,size);
        break;
        default:
        printf("ccsort: Invalid sort type");
    }

    char* prev = "\0";
    if(is_unique){
        for(int i=0;i<size;i++){
            if(!strcmp(arr[i],prev)) continue;
            printf("%s\n",arr[i]);
            prev = arr[i];
        }
    }else{
        for(int i=0;i<size;i++){
            printf("%s\n",arr[i]);
        }
    }
    free(data);
    if(sort_type == 3){
        for(int i=0;i<size;i++){
            free(arr[i]);
        }
    }
    fclose(file);
    return 0;
}