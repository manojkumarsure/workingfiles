#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
void pipecmd(char* c1,char* c2)
{
	
}
void execute(char* command)
{
	char* cmd;
	char* argv[100][10];
	cmd=strtok(command,";");
	while(cmd!=NULL)
	{
		char* cmd2;
		char* x =(char*)malloc(100);
		strcpy(x,cmd);
		cmd2=strtok(x,"|");
		while(cmd2!=NULL)
		{
			printf("%s",cmd2);
			cmd2=strtok(NULL,"|");
		}
		cmd=strtok(NULL,";");
	}
}
int main (void)
{
	char * cmdLine;
	char buff[512];
	int size=512;
	while (1)
	{
		char* pwd=getcwd(buff,513);
		printf("cs12b028@%s>",pwd);
		cmdLine=(char*)malloc(size+1);
		getline(&cmdLine,&size,stdin); 
		execute(cmdLine);
// 		cmd = parseCommand(cmdLine);
// 
// 		if ( isBuiltInCommand(cmd))
// 			executeBuiltInCommand(cmd);
// 		else 
// 		{                
// 			childPid = fork();
// 			if (childPid == 0)
// 				executeCommand(cmd); //calls execvp  
// 			else 
// 			{
// 				if (isBackgroundJob(cmd))
// 				{
// 						//record in list of background jobs
// 				}
// 				else 
// 				{
// 						waitpid (childPid);
// 				}               
// 			}
// 		}
	}
}