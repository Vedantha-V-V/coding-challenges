#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define SIZE 4096

char** read_file(FILE* file){
    char c;
    int i = 0,size = 0;
    char* string = (char*)malloc(sizeof(char)*SIZE);
    int capacity = SIZE;
    while((c=fgetc(file))!=EOF){
        if(i >= capacity-1){
            capacity*=2;
            string = realloc(string,capacity);
        }
        if(c == '\n'){
            size ++;
        }
        string[i] = c;
        i++;
    }
    size++;
    string[i] = '\0';
    
    int i = 0;
    char** arr = malloc(sizeof(char*)*size);
    char* token  = strtok(string,"\n");
    while(token!=NULL){
        if(token[0]!='\0'){
            arr[i] = token;
        }
        i++;
        token = strtok(NULL,"\n");
    }
    return arr;
}

char* LCS(char str1[], char str2[], char lcs[]){
    int rows = strlen(str1);
    int cols = strlen(str2);
    int matrix[rows+1][cols+1];
    int k = 0;
    for(int i=1;i<=rows;i++){
        for(int j=1;j<=cols;j++){
            if(str1[i-1]==str2[j-1]){
                matrix[i][j] = 1+matrix[i-1][j-1];
                lcs[k] = str1[i-1];
                k++;
            }else if(matrix[i-1][j]>matrix[i][j-1]){
                if(matrix[i-1][j]>matrix[i-1][j-1]){
                    matrix[i][j] = matrix[i-1][j];
                }else{
                    matrix[i][j] = matrix[i-1][j-1];
                }
            }else{
                if(matrix[i][j-1]>matrix[i-1][j-1]){
                    matrix[i][j] = matrix[i][j-1];
                }else{
                    matrix[i][j] = matrix[i-1][j-1];
                }
            }
        }
    }
    lcs[k] = '\0';
    return lcs;
}

int main(int argc,char* argv[]){
    FILE *file1,*file2;
    if(argc <= 1){
        printf("ccdiff: Insufficient arguments passed");
        return 0;
    }else if(argc == 2 && (argv[1] == "-h" || argv[1] == "--help")){
        printf("ccdiff: Command line tool to compare to file paths and output the difference between the two files.");
        return 0;
    }else{
        char* file_path1 = argv[1];
        char* file_path2 = argv[2];
        file1 = fopen(file_path1,"r");
        file2 = fopen(file_path2,"r");
        if(file1 == NULL){
            printf("ccdiff: %s not found",file_path1);
            return 1;
        }
        if(file2 == NULL){
            printf("ccdiff: %s not found",file_path2);
        }
    }
    char** file1_data = read_file(file1);
    char** file2_data = read_file(file2);
    return 0;
}