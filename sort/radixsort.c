#include <string.h>
#include <stdlib.h>

void radix_sort(char* arr[], int size){
    int max_len = 0;
    for(int i=0;i<size;i++){
        if(max_len<strlen(arr[i])){
            max_len = strlen(arr[i]);
        }
    }
    char* padded[size];
    for(int i = 0; i < size; i++){
        int str_len = strlen(arr[i]);
        padded[i] = malloc(max_len + 1);
        strcpy(padded[i], arr[i]);
        for(int j = str_len; j < max_len; j++){
            padded[i][j] = ' ';
        }
        padded[i][max_len] = '\0';
    }

    for(int col = max_len - 1; col >= 0; col--){
        int count[256] = {0};
        for(int i = 0; i < size; i++){
            count[(unsigned char)padded[i][col]]++;
        }
        
        for(int i = 1; i < 256; i++){
            count[i] += count[i-1];
        }
        
        char* sorted[size];
        for(int i = size - 1; i >= 0; i--){
            int idx = --count[(unsigned char)padded[i][col]];
            sorted[idx] = padded[i];
        }
        
        for(int i = 0; i < size; i++){
            padded[i] = sorted[i];
        }
    }

    for(int i = 0; i < size; i++){
        arr[i] = malloc(strlen(padded[i])+1);
        strcpy(arr[i],padded[i]);
        free(padded[i]);
    }
}