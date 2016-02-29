#include<stdio.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>

int main(){
	int len;
	char buffer[30];
	int fd = open("/dev/tq2440_serial0",O_RDWR);
	if(fd<0){
		printf("open file failed\n");
		exit(-1);
	}
	printf("sizeof(buffer)=%d\n",sizeof(buffer));
	while(1){
		len=read(fd,buffer,sizeof(buffer)-1);
		if(len>0){
			buffer[len]=0;
			printf("%s",buffer);
		}
	}
		
	close(fd);
	return 0;
}