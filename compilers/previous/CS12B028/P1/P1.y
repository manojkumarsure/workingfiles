%{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<malloc.h>
#define MAX 100000
extern int yylex();
extern void yyerror(const char *);
extern FILE* yyin;
extern int yyparse();
char* nullstr()
{
	char* res= (char*)malloc(5*sizeof(char));
	res="";
	return res;
}
typedef struct node macro;
struct node
{
	char* macro_name;
	char* expr;
	int no_of_args;
	int type;
	macro* next;
};
typedef struct llist macro_list;
struct llist
{
	macro* head;
};
macro_list* list=NULL;
void create_new()
{
	if(list==NULL)
	{
		list=(macro_list*)malloc(sizeof(macro_list));
		list->head=NULL;
	}
}
int totalmacros=0;
int countargs(char* expr)
{
	int count=0;
	if(strlen(expr)==0)
		return count;
	count++;
	int i;
	for(i=0;i<strlen(expr);i++)
	{
		if(expr[i]==',')
			count++;
	}
	return count;
}
char* modify(char* arguments,char* expr)
{
 	char* expression=(char*)malloc(1000*sizeof(char));
	char* arg;
	expression=expr;
	arg=strtok(arguments,",");
	int i,j,k;
	int argcount=1;
	while(arg!=NULL)
	{
		for(i=0;i<strlen(expression);i++)
		{
			for(j=0;i+j<strlen(expression),j<strlen(arg);j++)
			{
				if(expression[i+j]==arg[j] )
					continue;
				else
					break;
			}
			if(j==strlen(arg))
			{
				char* x1=malloc(1000);
				for(k=0;k<i;k++)
					x1[i]=expression[i];
				x1[i]='#';
				x1[i+1]='#';
				x1[i+2]=(char)(((int)'0')+argcount);
				for(k=i+j;k<strlen(expression);k++)
					x1[k-j+3]=expression[k];
				x1[strlen(expression)-j+3]='\0';
				sprintf(expression,"%s",x1);
				free(x1);
				i=-1;
			}
		}
		argcount++;
		arg=strtok(NULL,",");
	}
	return expression;
}
void add_macro(char* name,char* expression,char* arguments,int type)
{
	int args=countargs(arguments);
	if(list->head==NULL)
	{
		list->head=(macro*)malloc(sizeof(macro));
		list->head->macro_name=malloc(1000);
		list->head->expr=malloc(1000);
		strcpy(list->head->macro_name,name);
		strcpy(list->head->expr,expression);
		list->head->no_of_args=args;
		list->head->type=type;
		list->head->next=NULL;
		totalmacros++;
	}
	else
	{
		macro* temp=list->head;
		int count=0;
		while(temp->next!=NULL)
		{
			if(strcmp(name,temp->macro_name)!=0)
			{
				count++;
				temp=temp->next;
			}
			else
			{
					break;
			}
		}
		if(strcmp(name,temp->macro_name)!=0 && temp->next==NULL)
		{
			count++;
		}
		if(count!=totalmacros)
		{
			fprintf(stderr,"// Failed to parse macrojava code.\n");
			exit(0);
		}
		else
		{
			temp->next=(macro*)malloc(sizeof(macro));
			temp->next->macro_name=malloc(1000);
			temp->next->expr=malloc(1000);
			strcpy(temp->next->macro_name,name);
			temp->next->no_of_args=args;
			temp->next->type=type;
			if(args==0)
				sprintf(temp->next->expr,"%s",expression);
			else
				sprintf(temp->next->expr,"%s",modify(arguments,expression));
			temp->next->next=NULL;
		}
		totalmacros++;
	}
}
char* modify_expr(char* name,char* arguments,char* string,macro* temp)
{
	if(temp->no_of_args!=countargs(arguments))
 		return string;
 	else
 	{
		char* expression=(char*)malloc(1000*sizeof(char));
		sprintf(expression,"%s",temp->expr);
 		char* arg=strtok(arguments,",");
 		int i,j,k;
 		int argcount=1,currposs=0;
 		while(arg!=NULL)
 		{
 			char* req_arg=malloc(5);
 			sprintf(req_arg,"##%d",argcount);
 			for(i=0;i<strlen(expression);i++)
 			{
				if(expression[i]==req_arg[0] && expression[i+1]==req_arg[1] && expression[i+2]==req_arg[2])
 				{
 					char* x1=malloc(1000);
 					for(k=0;k<i;k++)
 						x1[i]=expression[i];
 					strcat(x1,arg);
 					strcat(x1,expression+i+3);
 					sprintf(expression,"%s",x1);
 					free(x1);
 					i=-1;
 				}
 			}
 			argcount++;
 			arg=strtok(NULL,",");
 		}
 		return expression;
 	}
}	
char* prog;
%}
%union
{
	char* boolval;
	char* identifier;
	int integer;
	char* op_value;
	char* nonterminals;
}
%token CLASS STRING PUBLIC STATIC VOID MAIN PRINT EXTEND RETURN INT BOOL IF ELSE WHILE LENGTH THIS NEW DEFINE TRUE FALSE e0f
%token <boolval> BOOLVAL <identifier> IDENTIFIER <integer> INTEGER <op_value> OP_VALUE
%type <nonterminals> Goal MacroDefinitionVar TypeDeclaration TypeDeclarationVar MainClass MethodDeclarationVar TypeVar MethodDeclaration StatementVar IdentifierList TypeIdentifierList
%type <nonterminals> Type Statement Expression ExpressionVar ExpressionVar2 PrimExpr MacroDefinition MacroDefStatement MacroDefExpression IdentifierVar IdentifierVar2
%start Goal

%glr-parser

%%
Goal	: 	MacroDefinitionVar MainClass TypeDeclarationVar{printf("%s\n%s\n",$2,$3);exit(0);};
MacroDefinitionVar : MacroDefinitionVar MacroDefinition {char* str=(char*)malloc(MAX*sizeof(char)); sprintf(str,"%s\n%s\n",$1,$2);$$=str;} | {$$=nullstr();};
TypeDeclarationVar : TypeDeclarationVar TypeDeclaration {char* str=(char*)malloc(MAX*sizeof(char)); sprintf(str,"%s\n%s\n",$1,$2);$$=str;} | {$$=nullstr();};
MainClass : CLASS IDENTIFIER '{' PUBLIC STATIC VOID MAIN '(' STRING '[' ']' IDENTIFIER ')' '{' PRINT '(' Expression ')' ';' '}' '}'
			{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"class %s {\npublic static void main(String[] %s)\n{\nSystem.out.println(%s);\n}\n}",$2,$12,$17);$$=str;};
TypeDeclaration :CLASS IDENTIFIER '{' TypeVar MethodDeclarationVar '}'
				 {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"class %s {\n %s %s }\n",$2,$4,$5);$$=str;}
				| CLASS IDENTIFIER EXTEND IDENTIFIER '{' TypeVar MethodDeclarationVar '}' 
				{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"class %s extends %s {\n %s %s }\n",$2,$4,$6,$7);$$=str;};
MethodDeclarationVar :  MethodDeclaration MethodDeclarationVar
						{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s\n%s\n",$1,$2);$$=str;}| {$$=nullstr();};
TypeVar : {$$=nullstr();}|Type IDENTIFIER ';' TypeVar{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s %s;\n%s",$1,$2,$4);$$=str;};
MethodDeclaration : PUBLIC Type IDENTIFIER '(' IdentifierList ')'  '{' TypeVar StatementVar RETURN Expression ';' '}'
					{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"public %s %s ( %s ) { \n %s %s return %s;\n}",$2,$3,$5,$8,$9,$11);$$=str;};
StatementVar : {$$=nullstr();}|Statement StatementVar{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s\n%s\n",$1,$2);$$=str;};
IdentifierList: {$$=nullstr();}|Type IDENTIFIER TypeIdentifierList {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s %s %s",$1,$2,$3);$$=str;} ;
TypeIdentifierList : {$$=nullstr();} |',' Type IDENTIFIER TypeIdentifierList{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,",%s %s %s",$2,$3,$4);$$=str;} ;
Type : INT '[' ']' {char* str=(char*)malloc(10*sizeof(char));sprintf(str,"int[] ");$$=str;} | BOOL{char* str=(char*)malloc(10*sizeof(char));sprintf(str,"boolean ");$$=str;} | INT{char* str=(char*)malloc(10*sizeof(char));sprintf(str,"int ");$$=str;} | IDENTIFIER{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s ",$1);$$=str;};
Statement : 
'{' StatementVar '}' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"{%s}\n",$2);$$=str;}
| PRINT '(' Expression ')' ';' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"System.out.println(%s);",$3);$$=str;}
| IDENTIFIER '=' Expression ';' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s=%s;\n",$1,$3);$$=str;}
| IDENTIFIER '[' Expression ']' '=' Expression ';' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s[%s]=%s;\n",$1,$3,$6);$$=str;}
| IF '(' Expression ')' Statement {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"if(%s)\n%s\n",$3,$5);$$=str;}
| IF '(' Expression ')' Statement ELSE Statement {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"if(%s)\n%selse\n%s",$3,$5,$7);$$=str;}
| WHILE '(' Expression ')' Statement {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"while(%s)\n%s\n",$3,$5);$$=str;}
| IDENTIFIER '(' ExpressionVar ')' ';'
{
char* str=(char*)malloc(MAX*sizeof(char));
sprintf(str,"%s(%s) ",$1,$3);$$=str;
if(list!=NULL)
{macro* temp=list->head;char* str1=malloc(1000);
char* str2=malloc(1000);strcpy(str1,$1);
strcpy(str2,$3);
while(temp->next!=NULL)
{
if(strcmp(temp->macro_name,$1)==0)
{
	if(temp->type==1)
	{
	fprintf(stderr,"// Failed to parse macrojava code.");
	exit(0);
	}
	$$=modify_expr(str1,str2,str,temp);
	printf("%s",modify_expr(str1,str2,str,temp));
	break;
}
temp=temp->next;
}
if(strcmp(temp->macro_name,$1)==0 && temp->next==NULL)
{$$=modify_expr(str1,str2,str,temp);}}	}		; 
ExpressionVar :  {$$=nullstr();}|Expression ExpressionVar2 {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s %s ",$1,$2);$$=str;};
ExpressionVar2 : {$$=nullstr();}|',' Expression ExpressionVar2{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,",%s %s",$2,$3);$$=str;} ;
Expression : PrimExpr '&' PrimExpr {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s&%s ",$1,$3);$$=str;}
| PrimExpr '&' '!' Expression {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s& !%s ",$1,$4);$$=str;}
| '!' Expression '&' PrimExpr {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"!%s&%s ",$2,$4);$$=str;}
| '!' Expression '&' '!' Expression{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"!%s & !%s ",$2,$5);$$=str;}
| '!' Expression {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"!%s ",$2);$$=str;}
| PrimExpr '<' PrimExpr{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s<%s ",$1,$3);$$=str;}
| PrimExpr '+' PrimExpr{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s+%s ",$1,$3);$$=str;}
| PrimExpr '-' PrimExpr{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s-%s ",$1,$3);$$=str;}
| PrimExpr '*' PrimExpr{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s*%s ",$1,$3);$$=str;}
| PrimExpr '/' PrimExpr{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s/%s ",$1,$3);$$=str;}
| PrimExpr '[' PrimExpr ']'{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s[%s] ",$1,$3);$$=str;}
| PrimExpr '.' LENGTH {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s.length ",$1);$$=str;}
| PrimExpr {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s ",$1);$$=str;}
| PrimExpr '.' IDENTIFIER '(' ExpressionVar ')' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s.%s(%s) ",$1,$3,$5);$$=str;}
| IDENTIFIER '(' ExpressionVar ')'{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s(%s) ",$1,$3);$$=str;if(list!=NULL){macro* temp=list->head;char* str1=malloc(1000);char* str2=malloc(1000);strcpy(str1,$1);strcpy(str2,$3);while(temp->next!=NULL){if(strcmp(temp->macro_name,$1)==0){if(temp->type==0){fprintf(stderr,"// Failed to parse macrojava code.");exit(0);}$$=modify_expr(str1,str2,str,temp);break;}temp=temp->next;}if(strcmp(temp->macro_name,$1)==0 && temp->next==NULL){$$=modify_expr(str1,str2,str,temp);}}	}		; 
PrimExpr : INTEGER {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%d ",$1);$$=str;}
| TRUE {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"true ");$$=str;}| FALSE{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"false ");$$=str;} 
| IDENTIFIER {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s ",$1);$$=str;}
| THIS {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"this ");$$=str;}
| NEW INT '[' Expression ']' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"new int [ %s ] ",$4);$$=str;}
| NEW IDENTIFIER '(' ')' {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"new %s() ",$2);$$=str;}
| '(' Expression ')'{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"(%s) ",$2);$$=str;};
MacroDefinition : MacroDefExpression {$$=nullstr();}
| MacroDefStatement {$$=nullstr();};
MacroDefStatement : DEFINE IDENTIFIER '(' IdentifierVar ')' '{' Statement '}'{create_new();add_macro($2,$7,$4,0);};
MacroDefExpression : DEFINE IDENTIFIER '(' IdentifierVar ')' '(' Expression  ')' {create_new();add_macro($2,$7,$4,1);} ; 
IdentifierVar : {$$=nullstr();} |  IDENTIFIER IdentifierVar2 {char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,"%s %s",$1,$2);$$=str;}  ;
IdentifierVar2 :{$$=nullstr();} | ',' IDENTIFIER IdentifierVar2{char* str=(char*)malloc(MAX*sizeof(char));sprintf(str,",%s %s",$2,$3);$$=str;};
%%
main(){
	do {
		yyparse();
	} while (!feof(yyin));
}

void yyerror(const char *str) {
	fprintf(stderr,"// Failed to parse macrojava code.\n");
}