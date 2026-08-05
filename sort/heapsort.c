#include <string.h>

void heapify(char* arr[], int n, int i){
    int root = i;
    int left = 2*i+1;
    int right = 2*i+2;
    if(left<n && strcmp(arr[left],arr[root])>0){
        root = left;
    }
    if(right<n && strcmp(arr[right],arr[root])>0){
        root = right;
    }
    if(root!=i){
        char* temp = arr[i];
        arr[i] = arr[root];
        arr[root] = temp;
        heapify(arr,n,root);
    }
}

void heap_sort(char* arr[], int n){
    for(int i=n/2-1;i>=0;i--){
        heapify(arr,n,i);
    }
    for(int i=n-1;i>0;i--){
        char* temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr,i,0);
    }
}