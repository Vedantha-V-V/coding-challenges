#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#define SIZE 4096

void head(FILE* file,int lines,int chars){
    char c;
    int character = 0;
    int line = 0;
    while((c=fgetc(file))!=EOF){
        if(chars!=-1 && character>=chars){
            break;
        }
        if(chars!=-1){
            character++;
        }
        if(line >= lines){
            break;
        }
        if(c == '\n'){
            line++;
        }
        printf("%c",c);
    } 
    printf("\n");
}

int main(int argc,char* argv[]){
    FILE* file;
    bool isstdin = false;
    int files = 0, j = 0, chars = -1, lines = 10;
    if(argc == 1){
        file = stdin;
        isstdin = true;
    }else{
        int i = 1;
        while(i<argc){
            if(!strncmp(argv[i],"-n",2)){
                if(strlen(argv[i])==3){
                    lines = argv[i][2] - '0';
                }else if(i+1<argc){
                    lines = atoi(argv[i+1]);
                    i+=2;
                    continue;
                }
            }else if(!strncmp(argv[i],"-c",2)){
                if(strlen(argv[i])==3){
                    chars = argv[i][2] - '0';
                }else if(i+1<argc){
                    chars = atoi(argv[i+1]);
                    i+=2;
                    continue;
                }
            }else{
                files++;
                if(j==0){
                    j=i;
                }
            }
            i++;
        }
    }
    if(isstdin){
        head(file,lines,chars);
    }else{
        if(files==1){
            file = fopen(argv[j],"r");
            if(file == NULL){
                printf("cchead: %s no such file or directory\n",argv[j]);
                return 1;
            }
            head(file,lines,chars);
        }else{
            for(int k=j;k<argc;k++){
                printf("==> %s <==\n",argv[k]);
                file = fopen(argv[k],"r");
                if(file == NULL){
                    printf("cchead: %s no such file or directory\n",argv[k]);
                    return 1;
                }
                head(file,lines,chars);
                printf("\n");
            }
        }
    }
    return 0;
}
