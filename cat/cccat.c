# include <stdio.h>
# include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc,char *argv[]){
    if(argc == 1){
        char buffer[1024];
        while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
           printf("%s", buffer);
        }
        return 0;
    }
    if(strcmp(argv[1],"--help") == 0 || strcmp(argv[1],"-h") == 0){
        printf("cccat [OPTIONS].. [FILE]..\n");
        printf("Prints contents of File(s) to standard output\n");
        printf("OPTIONS:\n");
        printf("With no FILE, or when FILE is -, read standard input\n");
        printf("-n Number the lines as they are printed out\n");
        printf("-b Number the non empty lines as they are printed out\n");
    }else if(argv[1][0] == '-'){
        if(!strcmp(argv[1],"-")){
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                char buffer[1024];
                while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
                    printf("%s", buffer);
                }
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("cccat: %s No such file or directory\n",path);
                        return 1;
                    }
                    char contents[100];
                    while(fgets(contents,100,fptr)){
                        printf("%s\n",contents);
                    }
                    printf("\n");
                    fclose(fptr);
                }
            }
        }
        else if(!strcmp(argv[1],"-n")){
            int k = 1;
            char buffer[1024];
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                char buffer[1024];
                while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
                    printf("%d %s",k, buffer);
                    k+=1;
                }
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("cccat: %s No such file or directory\n",path);
                        return 1;
                    }
                    char contents[100];
                    while(fgets(contents,100,fptr)){
                        printf("%d %s",k,contents);
                        k += 1;
                    }
                    printf("\n");
                    fclose(fptr);
                }
            }
        }else if(!strcmp(argv[1],"-b")){
            int k = 1;
            char buffer[1024];
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                char buffer[1024];
                while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
                    if(strcmp(buffer,"\n")){
                        printf("%d %s",k, buffer);
                        k+=1;
                    }else{
                        printf("%s",buffer);
                    }
                }
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("cccat: %s No such file or directory\n",path);
                        return 1;
                    }
                    char contents[100];
                    while(fgets(contents,100,fptr)){
                        if(strcmp(buffer,"\n")){
                            printf("%d %s",k,contents);
                            k+=1;
                        }else{
                            printf("%s",buffer);
                        }
                    }
                    printf("\n");
                    fclose(fptr);
                }
            }
        }
    }else{
        for(int i=1;i<argc;i++){
            char *path = argv[i];
            FILE *fptr;
            fptr = fopen(path,"r");
            if(fptr == NULL){
                printf("cccat: %s No such file or directory\n",path);
                return 1;
            }
            char contents[100];
            while(fgets(contents,100,fptr)){
                printf("%s",contents);
            }
            printf("\n");
            fclose(fptr);
        }
    }
    return 0;
}