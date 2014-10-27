#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<string>
#include<string.h>
#include<stack>
#include<malloc.h>
using namespace std;
class EvalObject
{
public:
	int rows;
	int columns;
	int **entries;
	int value;
	EvalObject(int** array,int r,int c,int val)
	{
		rows=r;
		columns=c;
		value=val;
		entries=array;
	}
	EvalObject()
	{
		rows=0;
		columns=0;
		value=-1;
		entries=NULL;
	}
	void print()
	{
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<columns;j++)
			{
				cout<<entries[i][j]<<" ";
			}
			cout<<endl;
		}
	}
};
int bracketmatch(string expr)
{
	int i;
	int openBracketCount=0;
	int closedBracketCount=0;
	for(i=0;i<expr.length();i++)
	{
		if(expr[i]=='(')
			openBracketCount++;
		if(expr[i]==')')
			closedBracketCount++;
		if(openBracketCount<closedBracketCount)
		{
			cout<<"error\n";
			return -1;
		}
	}
	if(openBracketCount!=closedBracketCount)
	{
		cout<<"error\n";
		return -1;
	}
	return 0;
}
int length;
char* values;
int get_pair(int start,string expr)
{
	int opcount=1;
	for(int i=start+1;i<expr.length();i++)
	{
		if(expr[i]=='(')
			opcount++;
		if(expr[i]==')')
			opcount--;
		if(opcount==0)
			return i;
	}
}
char type(int start,int end,string expr)
{
	for(int i=start;i<=end;i++)
	{
		if(expr[i]=='A')
			return 'M';
	}
	return 'N';
}
int operatorverify(string expr)
{
	int bracket_match;
	for(int i=0;i<expr.length();i++)
	{
		if(expr[i]=='(')
		{
			bracket_match=get_pair(i,expr);
			if(bracket_match==i+1)
			{
				cout<<"error"<<endl;
				return -1;
			}
			values[i]=type(i,bracket_match,expr);
			values[bracket_match]=values[i];
			if(expr[i-1]==')')
			{
				cout<<"error"<<endl;
				return -1;
			}
		}
		if(expr[i]=='A')
		{
			values[i]='M';
			if(expr[i+1]=='(' or expr[i+1]=='A' or isdigit(expr[i]))
			{
				cout<<"error"<<endl;
				return -1;
			}
		}
		if(isdigit(expr[i]))
			values[i]='N';
		if(!(expr[i]=='A' or isdigit(expr[i]) or expr[i]=='*' or expr[i]=='+' or expr[i]=='(' or expr[i]==')'))
		{
			cout<<"error"<<endl;
			return -1;
		}
	}
	for(int i=1;i<expr.length()-1;i++)
	{
		if(expr[i]=='*')
		{
			values[i]='S';
			if(values[i-1]=='N' and values[i+1]=='M')
			{
				for(int j=i-1;j>=0;j--)
				{
					if(values[j]=='N')
						values[j]='M';
					else
						break;
				}
			}
			if(!((values[i-1]=='N' and values[i+1]=='N') or (values[i-1]=='N' and values[i+1]=='M') or (values[i-1]=='M' and values[i+1]=='M')))
			{
				cout<<"error"<<endl;
				return -1;
			}
			if(expr[i+1]==')' or expr[i-1]=='(')
			{
				cout<<"error"<<endl;
				return -1;
			}
		}
	}
	for(int i=1;i<expr.length()-1;i++)
	{
		if(expr[i]=='+')
		{
			values[i]='P';
			if(!((values[i-1]=='N' and values[i+1]=='N') or (values[i-1]=='M' and values[i+1]=='M')))
			{
				cout<<"error"<<endl;
				return -1;
			}
			if(expr[i+1]==')' or expr[i-1]=='(')
			{
				cout<<"error"<<endl;
				return -1;
			}
		}
	}
	if(expr[0]=='*' or expr[expr.length()-1]=='*' or expr[0]=='+' or expr[expr.length()-1]=='+')
	{
		cout<<"error"<<endl;
		return -1;
	}
	for(int i=0;i<expr.length()-1;i++)
	{
		if((values[i]=='N' and values[i+1]=='M') or (values[i]=='M' and values[i+1]=='N'))
		{
			cout<<values<<endl;
			cout<<"error"<<endl;
			return -1;
		}
	}
	return 0;
}
EvalObject multiply(EvalObject na,EvalObject nb)
{
	EvalObject c(NULL,0,0,-1);
	c.rows=nb.rows;
	c.columns=nb.columns;
	int elem[nb.rows][nb.columns];
	c.entries=NULL;
	if(na.value!=-1 and nb.value!=-1)
	{
		c.value=na.value*nb.value;
		c.rows=0;
		c.columns=0;
		return c;
	}
	if(na.value!=-1 and nb.value==-1)
	{
		for(int i=0;i<nb.rows;i++)
		{
			for(int j=0;j<nb.columns;j++)
			{
				elem[i][j]=na.value*nb.entries[i][j];
			}
		}
	}
	if(na.value==-1 and nb.value==-1)
	{
		for(int i=0;i<na.rows;i++)
		{
			for(int j=0;j<nb.columns;j++)
			{
				elem[i][j]=0;
				for(int k=0;k<na.columns;k++)
				{
					elem[i][j]+=na.entries[i][k]*nb.entries[k][j];
				}
			}
		}
	}
	c.entries=(int**)malloc(nb.rows*sizeof(int*));
	for(int i=0;i<nb.rows;i++)
	{
		c.entries[i]=(int*)malloc(nb.rows*sizeof(int));
	}
	for(int i=0;i<nb.rows;i++)
	{
		for(int j=0;j<nb.columns;j++)
		{
			c.entries[i][j]=elem[i][j];
		}
	}
	c.value=-1;
	return c;
}
EvalObject add(EvalObject a,EvalObject b)
{
	EvalObject c(NULL,0,0,-1);
	c.rows=b.rows;
	c.columns=b.columns;
	int elem[b.rows][b.columns];
	c.entries=NULL;
	if(a.value!=-1 and b.value!=-1)
	{
		c.value=a.value+b.value;
		return c;
	}
	if(a.value==-1)
	{
		for(int i=0;i<b.rows;i++)
		{
			for(int j=0;j<b.columns;j++)
			{
				elem[i][j]=a.entries[i][j]+b.entries[i][j];
			}
		}
	}
	c.entries=(int**)malloc(b.rows*sizeof(int*));
	for(int i=0;i<b.rows;i++)
	{
		c.entries[i]=(int*)malloc(b.rows*sizeof(int));
	}
	for(int i=0;i<b.rows;i++)
	{
		for(int j=0;j<b.columns;j++)
		{
			c.entries[i][j]=elem[i][j];
		}
	}
	c.value=-1;
	return c;
}
int verify(string expr)
{
	if(bracketmatch(expr)!=-1)
	{
		values=(char*)malloc((expr.length()+1)*sizeof(char));
		for(int i=0;i<expr.length()+1;i++)
		{
			values[i]='-';
		}
		int j;
		for(j=0;j<expr.length();j++)
		{
			if(expr[j]=='A')
				break;
		}
		if(j==expr.length())
		{
			cout<<"error"<<endl;
			return -1;
		}
		return operatorverify(expr);
	}
	else return -1;
}
EvalObject evaluate(string expr,EvalObject mat)
{
	stack<char> op_stack;
	string postfix="";
	for(int i=0;i<expr.length();i++)
	{
		if(expr[i]=='A')
		{
			postfix+=expr[i];
		}
		if(isdigit(expr[i]))
		{
			while(isdigit(expr[i]))
			{
				postfix+=expr[i];
				i++;
			}
			postfix+=',';
		}
		if(expr[i]==')')
		{
			while(op_stack.top()!='(')
			{
				postfix+=op_stack.top();
				op_stack.pop();
			}
			op_stack.pop();
		}
		if(expr[i]=='*' or expr[i]=='(')
			op_stack.push(expr[i]);
		if(expr[i]=='+')
		{
			while(1)
			{
				if(op_stack.size()!=0)
				{
					if(op_stack.top()=='*')
					{
						op_stack.pop();
						postfix+='*';
					}
					else
						break;
				}
				else
					break;
			}
			op_stack.push('+');
		}
	}
	while(op_stack.size()!=0)
	{
		postfix+=op_stack.top();
		op_stack.pop();
	}
	stack<EvalObject> eval_stack;
	EvalObject a,b,number;
	for(int i=0;i<postfix.length();i++)
	{
		if(postfix[i]=='A')
			eval_stack.push(mat);
		if(isdigit(postfix[i]))
		{   
			int j=i;
			while(isdigit(postfix[i++]));
			number.value=atoi(postfix.substr(j,i--).c_str());
			eval_stack.push(number);
		}
		if(postfix[i]=='*')
		{
			a=eval_stack.top();
			eval_stack.pop();
			b=eval_stack.top();
			eval_stack.pop();
			eval_stack.push(multiply(b,a));
		}
		if(postfix[i]=='+')
		{
			a=eval_stack.top();
			eval_stack.pop();
			b=eval_stack.top();
			eval_stack.pop();
			eval_stack.push(add(a,b));
		}
	}
	return eval_stack.top();
}