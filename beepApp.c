#include<stdio.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>

int main(){
	int fd = open("/dev/PWM-Test",O_RDWR);
	if(fd<0){
		printf("open file failed\n");
		exit(-1);
	}
	ioctl(fd,1,2000);
	getchar();
	ioctl(fd,0,1);
	close(fd);
	return 0;
}