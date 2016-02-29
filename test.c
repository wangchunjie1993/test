#include<stdio.h>
#include<unistd.h>

int main()
{
	pid_t pid;
	if((pid=fork())>0){
		printf("I'm father.pid=%d,child's pid=%d\n",getpid(),pid);
	}else if(pid==0){
		printf("I'm child.pid=%d,father's pid=%d\n",getpid(),getppid());
		exit(0);
	}else{
		printf("fork() failed\n");
		exit(0);
	}
	system("echo hello > /dev/console");
	sleep(1);
	exit(0);
}