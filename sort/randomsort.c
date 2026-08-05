#include <stdlib.h>
#include <string.h>

int hash(char* key,int size){
    int idx;
    int sum = 0, factor = 31;
    for (int i = 0; i < strlen(key); i++) {
        sum = ((sum%size) + (((int)key[i]) * factor)%size)%size;
        factor = ((factor%__INT16_MAX__)*(31%__INT16_MAX__))%__INT16_MAX__;
    }

    idx = sum;
    return idx;
}

void insertion_sort(int hashes[],int size){
    for(int i=1;i<size;i++){
        int key = hashes[i];
        int j = i-1;
        while(j>=0 && hashes[j]>key){
            hashes[j+1]=hashes[j];
            j--;
        }
        hashes[j+1]=key;
    }
}

void random_sort(char* arr[],int size){
    if(size <= 1) return;

    typedef struct {
        int hash;
        int idx;
    } pair;
    
    pair pairs[size];
    
    for(int i = 0; i < size; i++){
        pairs[i].hash = hash(arr[i], size);
        pairs[i].idx = i;
    }
    
    for(int i = 0; i < size - 1; i++){
        for(int j = 0; j < size - 1 - i; j++){
            if(pairs[j].hash > pairs[j+1].hash){
                pair temp = pairs[j];
                pairs[j] = pairs[j+1];
                pairs[j+1] = temp;
            }
        }
    }
    
    char* sorted[size];
    for(int i = 0; i < size; i++){
        sorted[i] = arr[pairs[i].idx];
    }
    
    for(int i = 0; i < size; i++){
        arr[i] = sorted[i];
    }
}