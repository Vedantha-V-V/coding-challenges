#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc,char* argv[]){
    if(argc <= 1){
        // No file or option provided
        char buffer[1024];
        while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
           printf("%s", buffer);
        }
    }else if(strcmp(argv[1],"--help") == 0 || strcmp(argv[1],"-h") == 0){
        // wc option --help
        printf("ccwc [OPTIONS].. [FILE]..\n");
        printf("Print newline, word, and byte counts for each FILE\n");
        printf("OPTIONS:\n");
        printf("With no FILE, or when FILE is -, read standard input\n");
        printf("-c Number of bytes in a file\n");
        printf("-m Number of lines in a file\n");
        printf("-w Number of words in a file\n");
        printf("-m Number of characters in a file\n");
    }else if(argv[1][0] == '-'){
        if(!strcmp(argv[1],"-")){
            // wc option - 
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
                        printf("ccwc: %s No such file or directory\n",path);
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
        else if(!strcmp(argv[1],"-c")){
            // wc option -c
            int bytecount = 0;
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                while (fgetc(stdin)!=EOF) {
                    bytecount+=1;
                }
                printf(" %d\n",bytecount);
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("ccwc: %s No such file or directory\n",path);
                        return 1;
                    }
                    while(fgetc(fptr)!=EOF){
                        bytecount += 1;
                    }
                    printf(" %d %s\n",bytecount,path);
                    fclose(fptr);
                }
            }
        }else if(!strcmp(argv[1],"-l")){
            // wc option -l
            int linecount = 0;
            char buffer[1024];
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                char buffer[1024];
                while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
                    if(strcmp(buffer,"\n")){
                        linecount+=1;
                    }
                }
                printf("%d\n",linecount);
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    char ch;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("ccwc: %s No such file or directory\n",path);
                        return 1;
                    }
                    while((ch = fgetc(fptr)) != EOF){
                        if(ch == '\n'){
                            linecount+=1;
                        }
                    }
                    printf(" %d %s\n",linecount,path);
                    fclose(fptr);
                }
            }
        }else if(!strcmp(argv[1],"-w")){
            // wc option -w
            int wordcount = 0;
            char ch;
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                char buffer[1024];
                while ((ch = fgetc(stdin)) != EOF) {
                    if(ch == ' '){
                        wordcount+=1;
                    }
                }
                printf(" %d\n",wordcount);
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    char ch;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("ccwc: %s No such file or directory\n",path);
                        return 1;
                    }
                    while((ch = fgetc(fptr)) != EOF){
                        if(ch == ' '){
                            wordcount+=1;
                        }
                    }
                    printf(" %d %s\n",wordcount,path);
                    fclose(fptr);
                }
            }
        }else if(!strcmp(argv[1],"-m")){
            // wc option -m
            int charcount = 0;
            char buffer[1024];
            if(argc == 2 && fopen(argv[1],"r")==NULL){
                char buffer[1024];
                while (fgetc(stdin) != EOF) {
                    charcount+=1;
                }
                printf("%d\n",charcount);
            }else{
                for(int i=2;i<argc;i++){
                    char *path = argv[i];
                    FILE *fptr;
                    char ch;
                    fptr = fopen(path,"r");
                    if(fptr == NULL){
                        printf("ccwc: %s No such file or directory\n",path);
                        return 1;
                    }
                    while((ch = fgetc(fptr)) != EOF){
                        charcount+=1;
                    }
                    printf(" %d %s\n",charcount,path);
                    fclose(fptr);
                }
            }
        }
    }else{
        char *path = argv[1];
        FILE *fptr;
        fptr = fopen(path,"r");
        if(fptr == NULL){
            printf("ccwc: %s No such file or directory\n",path);
            exit(1);
        }
        char ch;
        int wordcount = 1;
        int linecount = 0;
        int charcount = 0;
        while((ch = fgetc(fptr))!=EOF){
            if(ch==' '){
                wordcount+=1;
            }else if(ch == '\n'){
                linecount+=1;
            }
            charcount+=1;
        }
        printf(" %d %d %d %s\n",linecount,wordcount,charcount,path);
        fclose(fptr);
    }
    return 0;
}