#include <string.h>

int partition(char* arr[], int low, int high){
    char* pivot = arr[high];
    int i = low-1;
    for(int j=low;j<=high-1;j++){
        if(strcmp(arr[j],pivot)<0){
            i++;
            char* temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    char* temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i+1;
}

void quick_sort(char* arr[],int low,int high){
    if(low<high){
        int part = partition(arr,low,high);
        quick_sort(arr,low,part-1);
        quick_sort(arr,part+1,high);
    }
}