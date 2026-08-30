#include <stdio.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>
#include <string.h>
#define PORT 11211

int main(int argc, char* argv[]){
    int status, value, clientfd;
    struct sockaddr_in server_addr;
    char buffer[4096] = { 0 };
    clientfd = socket(AF_INET,SOCK_STREAM,0);
    if(clientfd < 0){
        perror("Socket creation error\n");
        return -1;
    }
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    if(inet_pton(AF_INET,"127.0.0.1",&server_addr.sin_addr)<=0){
        perror("Address Error\n");
        return -1;
    }
    if((status=connect(clientfd,(struct sockaddr*)&server_addr,sizeof(server_addr)))<0){
        perror("Connection Error");
        return -1;
    }
    char* message = "get test\r\n";
    // char* payload = "1234\r\n";
    send(clientfd,message,strlen(message),0);
    value = read(clientfd,buffer,4096-1);
    // printf("%s\n",buffer);
    // send(clientfd,payload,strlen(payload),0);
    // value = read(clientfd,buffer,1024-1);
    printf("%s\n",buffer);
    close(clientfd);
    return 0;
}