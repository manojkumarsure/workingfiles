#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
/*
 * Implementation of shell
 * Assignment submitted by :Manoj Kumar Sure
 */
#include<sys/types.h>
#include<sys/user.h>
#include<fcntl.h>
#include<string.h>
#define EXEC  1
#define REDIR 2
#define PIPE  3
#define LIST  4
#define BACK  5
#define O_CREATE 0x200
#define MAXARGS 10

//structure of cmd it stores type (exec,or redir or pipe etc)
struct cmd {
  int type;
};

//command of type exec(system defined commands)
struct execcmd {
  int type;
  char *argv[MAXARGS];
  char *eargv[MAXARGS];
};

//redir command structure ,it stores command,arguments,redirection file name and the mode of writing
struct redircmd {
  int type;
  struct cmd *cmd;
  char *file;
  char *efile;
  int mode;
  int fd;
};

//pipecmd structure,it stores left and right command structures
struct pipecmd {
  int type;
  struct cmd *left;
  struct cmd *right;
};

//structure for a list of commands(;)
struct listcmd {
  int type;
  struct cmd *left;
  struct cmd *right;
};

//background process structure, only the command is sufficient and type would be BACK
struct backcmd {
  int type;
  struct cmd *cmd;
};

//linked list of background jobs that are currently running
struct backjob* backjoblist;

//structure of the node
struct backjob{
  struct cmd *command;
  struct backjob* next;
};

//inserting into the linked list
void insert(struct backjob* b)
{
	if(backjoblist==NULL) //if there are no bg processes, the list would the node
	{
		backjoblist=b;
		return;
	}
	else
	{
		struct backjob* temp=backjoblist; //otherwise we would go tilll the end, and append the node
		while(temp->next!=NULL)
			temp=temp->next;
		temp->next=b;
	}
}

//this is because,if we finsih executing the node has to be removed
//we will traverse te linked list and remove the node and make appropriate pointer changes
void delete(struct backjob* b)
{
	if(backjoblist==b)
	{
		backjoblist=backjoblist->next;
		free(b);
		return;
	}
	struct backjob* temp=backjoblist;
	while(temp->next!=backjoblist && temp->next!=NULL)
	{
		temp=temp->next;
	}
	temp->next=temp->next->next;
	free(b);
}

//for printing the background processes ;used by lsb
void print()
{
	struct backjob* temp=backjoblist;
	while(temp)
	{
		printf("in\n");
		printf("%s\n",(char*)temp->command);
		temp=temp->next;
	}
}
int fork1(void);  // Fork but panics on failure.
void panic(char*);
struct cmd *parsecmd(char*);

// Execute cmd.  Never returns.
void
runcmd(struct cmd *cmd)
{
  int p[2];
  struct backcmd *bcmd;
  struct execcmd *ecmd;
  struct listcmd *lcmd;
  struct pipecmd *pcmd;
  struct redircmd *rcmd;

  if(cmd == 0)
    exit(0);
  
  switch(cmd->type){
  default:
    panic("runcmd");

  //if the command is of type exec,we will execute the command using execvp
  //if there is any error ,it will output error message
  case EXEC:
    ecmd = (struct execcmd*)cmd;
    if(ecmd->argv[0] == 0)
      exit(0);
    execvp(ecmd->argv[0], ecmd->argv);
    printf( "exec %s failed\n", ecmd->argv[0]);
    break;

  //redirection command,
  //close the current fd(stdin or stdout or stderr) and open the file in rcmd structure
	//so the new file will be in place of stdin ,stdout etc
  case REDIR:
    rcmd = (struct redircmd*)cmd;
    close(rcmd->fd);
    if(open(rcmd->file, rcmd->mode) < 0){
      printf( "open %s failed\n", rcmd->file);
      exit(0);
    }
    runcmd(rcmd->cmd);
    break;

  //list command;execute the left part,wait till it finishes execution and execute the right part
  case LIST:
    lcmd = (struct listcmd*)cmd;
    if(fork1() == 0)
      runcmd(lcmd->left);
    wait();
    runcmd(lcmd->right);
    break;

  //we close the stdout for left part,execute the left part and write into the p[1], and we close the stdin for the 
	//stdin for the second part and execute the second part,it takes it's input from p[0] and writes to stdout
  case PIPE:
    pcmd = (struct pipecmd*)cmd;
    if(pipe(p) < 0)
      panic("pipe");
    if(fork1() == 0){
      close(1);
      dup(p[1]);
      close(p[0]);
      close(p[1]);
      runcmd(pcmd->left);
    }
    if(fork1() == 0){
      close(0);
      dup(p[0]);
      close(p[0]);
      close(p[1]);
      runcmd(pcmd->right);
    }
    close(p[0]);
    close(p[1]);
    wait();
    wait();
    break;
    
  //background process,
//create two temporary files for stdout and stderr after closing actual stdout and stderr
	//and execute the command without waiting for the child to exit
  case BACK:
    bcmd = (struct backcmd*)cmd;
	struct backjob* b=(struct backjob*)malloc(sizeof(struct backjob));
	b->command=bcmd->cmd;
	b->next=NULL;
	insert(b);
    if(fork1() == 0)
	{
	  close(1);
	  close(2);
	  open("temp.txt",O_RDWR|O_CREAT|O_APPEND);
	  open("temp2.txt",O_RDWR|O_CREAT|O_APPEND);
      runcmd(bcmd->cmd);
	}
	delete(b);
    break;
  }
  exit(0);
}

//takes the input and stores it in buf along with printing the cwd at each time
int
getcmd(char *buf, int nbuf)
{
  char buff[512];
  char* pwd=getcwd(buff,513);
  printf("cs12b028:%s>",pwd);
  getline(&buf,&nbuf,stdin); 
  if(buf[0] == 0) // EOF
    return -1;
  return 0;
}

//main function
int
main(void)
{
  static char buf[100];
  int fd;
  
  // Assumes three file descriptors open.
  while((fd = open("console", O_RDWR)) >= 0){
    if(fd >= 3){
      close(fd);
      break;
    }
  }
  
  // Read and run input commands.
  //cd command has to be executed before,because any change made in the fork will not effect current shell
  while(getcmd(buf, sizeof(buf)) >= 0){
    if(buf[0] == 'c' && buf[1] == 'd' && buf[2] == ' '){
      buf[strlen(buf)-1] = 0;  // chop \n
      if(chdir(buf+3) < 0)
        printf( "cannot cd %s\n", buf+3);
      continue;
    }
    
    //executing lsb command;need not be done in the fork
    if(buf[0]=='l' && buf[1]=='s' && buf[2]=='b')
	{
		print();
		continue;
	}
	
	//fork and run the command 
    if(fork1() == 0)
      runcmd(parsecmd(buf));
    wait();
  }
  exit(0);
}

void
panic(char *s)
{
  printf( "%s\n", s);
  exit(0);
}

//creating a fork
int
fork1(void)
{
  int pid;
  
  pid = fork();
  if(pid == -1)
    panic("fork");
  return pid;
}

//PAGEBREAK!
// Constructors

//function to fill execcmd structure
struct cmd*
execcmd(void)
{
  struct execcmd *cmd;

  cmd = malloc(sizeof(*cmd));
  memset(cmd, 0, sizeof(*cmd));
  cmd->type = EXEC;
  return (struct cmd*)cmd;
}

//function to fill redircmd structure
struct cmd*
redircmd(struct cmd *subcmd, char *file, char *efile, int mode, int fd)
{
  struct redircmd *cmd;

  cmd = malloc(sizeof(*cmd));
  memset(cmd, 0, sizeof(*cmd));
  cmd->type = REDIR;
  cmd->cmd = subcmd;
  cmd->file = file;
  cmd->efile = efile;
  cmd->mode = mode;
  cmd->fd = fd;
  return (struct cmd*)cmd;
}

//function to fill pipecmd structure
struct cmd*
pipecmd(struct cmd *left, struct cmd *right)
{
  struct pipecmd *cmd;

  cmd = malloc(sizeof(*cmd));
  memset(cmd, 0, sizeof(*cmd));
  cmd->type = PIPE;
  cmd->left = left;
  cmd->right = right;
  return (struct cmd*)cmd;
}

//function to fill listcmd structure
struct cmd*
listcmd(struct cmd *left, struct cmd *right)
{
  struct listcmd *cmd;

  cmd = malloc(sizeof(*cmd));
  memset(cmd, 0, sizeof(*cmd));
  cmd->type = LIST;
  cmd->left = left;
  cmd->right = right;
  return (struct cmd*)cmd;
}

//function to fill backcmd structure
struct cmd*
backcmd(struct cmd *subcmd)
{
  struct backcmd *cmd;

  cmd = malloc(sizeof(*cmd));
  memset(cmd, 0, sizeof(*cmd));
  cmd->type = BACK;
  cmd->cmd = subcmd;
  return (struct cmd*)cmd;
}
// Parsing

char whitespace[] = " \t\r\n\v";
char symbols[] = "<|>&;()";

//get the tokens, if it does not match anything, it will return 'a'
int
gettoken(char **ps, char *es, char **q, char **eq)
{
  char *s;
  int ret;
  
  s = *ps;
  while(s < es && strchr(whitespace, *s))
    s++;
  if(q)
    *q = s;
  ret = *s;
  switch(*s){
  case 0:
    break;
  case '|':
  case '(':
  case ')':
  case ';':
  case '&':
  case '<':
    s++;
    break;
  case '>':
    s++;
    if(*s == '>'){
      ret = '+';
      s++;
    }
    break;
  default:
    ret = 'a';
    while(s < es && !strchr(whitespace, *s) && !strchr(symbols, *s))
      s++;
    break;
  }
  if(eq)
    *eq = s;
  
  while(s < es && strchr(whitespace, *s))
    s++;
  *ps = s;
  return ret;
}

int
peek(char **ps, char *es, char *toks)
{
  char *s;
  
  s = *ps;
  while(s < es && strchr(whitespace, *s))
    s++;
  *ps = s;
  return *s && strchr(toks, *s);
}

struct cmd *parseline(char**, char*);
struct cmd *parsepipe(char**, char*);
struct cmd *parseexec(char**, char*);
struct cmd *nulterminate(struct cmd*);

//parsing the command and terminate the command with a null
struct cmd*
parsecmd(char *s)
{
  char *es;
  struct cmd *cmd;

  es = s + strlen(s);
  cmd = parseline(&s, es);
  peek(&s, es, "");
  if(s != es){
    printf( "leftovers: %s\n", s);
    panic("syntax");
  }
  nulterminate(cmd);
  return cmd;
}

//parsing the command line(parsing based on ;)
struct cmd*
parseline(char **ps, char *es)
{
  struct cmd *cmd;

  cmd = parsepipe(ps, es);
  while(peek(ps, es, "&")){
    gettoken(ps, es, 0, 0);
    cmd = backcmd(cmd);
  }
  if(peek(ps, es, ";")){
    gettoken(ps, es, 0, 0);
    cmd = listcmd(cmd, parseline(ps, es));
  }
  return cmd;
}

//parsing based on pipe(|) after the semicolon is done
struct cmd*
parsepipe(char **ps, char *es)
{
  struct cmd *cmd;

  cmd = parseexec(ps, es);
  if(peek(ps, es, "|")){
    gettoken(ps, es, 0, 0);
    cmd = pipecmd(cmd, parsepipe(ps, es));
  }
  return cmd;
}

//parsing based on redirection commands(<,>)
//and setting the permissions for the files properly
//NOTE:'>' is also append
struct cmd*
parseredirs(struct cmd *cmd, char **ps, char *es)
{
  int tok;
  char *q, *eq;

  while(peek(ps, es, "<>")){
    tok = gettoken(ps, es, 0, 0);
    if(gettoken(ps, es, &q, &eq) != 'a')
      panic("missing file for redirection");
    switch(tok){
    case '<':
      cmd = redircmd(cmd, q, eq, O_RDONLY, 0);
      break;
    case '>':
      cmd = redircmd(cmd, q, eq, O_RDWR|O_CREAT|O_APPEND, 1);
      break;
    case '+':  // >>
      cmd = redircmd(cmd, q, eq, O_RDWR|O_CREAT|O_APPEND, 1);
      break;
    }
  }
  return cmd;
}

//parsing based on brackets
struct cmd*
parseblock(char **ps, char *es)
{
  struct cmd *cmd;

  if(!peek(ps, es, "("))
    panic("parseblock");
  gettoken(ps, es, 0, 0);
  cmd = parseline(ps, es);
  if(!peek(ps, es, ")"))
    panic("syntax - missing )");
  gettoken(ps, es, 0, 0);
  cmd = parseredirs(cmd, ps, es);
  return cmd;
}

//parsing the execute command
struct cmd*
parseexec(char **ps, char *es)
{
  char *q, *eq;
  int tok, argc;
  struct execcmd *cmd;
  struct cmd *ret;
  
  if(peek(ps, es, "("))
    return parseblock(ps, es);

  ret = execcmd();
  cmd = (struct execcmd*)ret;

  argc = 0;
  ret = parseredirs(ret, ps, es);
  while(!peek(ps, es, "|)&;")){
    if((tok=gettoken(ps, es, &q, &eq)) == 0)
      break;
    if(tok != 'a')
      panic("syntax");
    cmd->argv[argc] = q;
    cmd->eargv[argc] = eq;
    argc++;
    if(argc >= MAXARGS)
      panic("too many args");
    ret = parseredirs(ret, ps, es);
  }
  cmd->argv[argc] = 0;
  cmd->eargv[argc] = 0;
  return ret;
}

// NUL-terminate all the counted strings.
struct cmd*
nulterminate(struct cmd *cmd)
{
  int i;
  struct backcmd *bcmd;
  struct execcmd *ecmd;
  struct listcmd *lcmd;
  struct pipecmd *pcmd;
  struct redircmd *rcmd;

  if(cmd == 0)
    return 0;
  
  switch(cmd->type){
  case EXEC:
    ecmd = (struct execcmd*)cmd;
    for(i=0; ecmd->argv[i]; i++)
      *ecmd->eargv[i] = 0;
    break;

  case REDIR:
    rcmd = (struct redircmd*)cmd;
    nulterminate(rcmd->cmd);
    *rcmd->efile = 0;
    break;

  case PIPE:
    pcmd = (struct pipecmd*)cmd;
    nulterminate(pcmd->left);
    nulterminate(pcmd->right);
    break;
    
  case LIST:
    lcmd = (struct listcmd*)cmd;
    nulterminate(lcmd->left);
    nulterminate(lcmd->right);
    break;

  case BACK:
    bcmd = (struct backcmd*)cmd;
    nulterminate(bcmd->cmd);
    break;
  }
  return cmd;
}