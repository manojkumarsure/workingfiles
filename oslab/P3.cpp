#include<iostream>
#include<cstdlib>
using namespace std;
int currmax;
int mat[10][10]={{1,0,0,0,0,0,0,0,1,0,},{1,1,0,1,1,0,0,1,1,1,},{0,0,1,0,0,0,0,0,1,0,},
{0,0,0,1,0,0,0,0,1,1,},{0,0,0,0,1,0,0,0,1,1,},{0,0,0,0,0,1,1,0,1,1,},{0,0,0,0,0,0,1,0,1,0,},
{1,0,0,1,0,0,0,1,1,1,},{0,0,0,0,0,0,0,0,1,0,},{0,0,0,0,0,0,0,0,1,1,}};
char getmax(char a,char b='9')
{
	int var=a-48;
	for(char i=b;i>='0';i--){
		if(mat[var][i-48])return i;
	}
	return '\0';
}
string help(string s)
{
for(int i=0;i<s.length();i++){
	s[i]=getmax(s[i]);
}
return s;	
}	
string fun(string s1,string max)
{
	if(s1.length()==0)
		return string(1,'\0');
	if(atoi(s1.c_str())>atoi(max.c_str()))
		return NULL;
	string s2=fun(s1.substr(1,s1.length()),max.substr(1,max.length()));
	if(s1[0]=='X')
	{
		s1[0]=max[0];
		if(s2[0]=='\0')
		{
			s1[0]=string(1,max[0]-1)[0];
			return s1[0]+help(s1.substr(1,s1.length()));
		}
		else
			return s1[0]+s2;
	}
	else
	{
		char s3;
		s3=getmax(s1[0],max[0]);
		if(s3==string(1,'\0')[0])
			return NULL;
		return string(1,s3)+s2;
	}
}

void fun2(string s,string max)
{
	if(s.length()==max.length())
	{
		currmax=atoi(fun(s,max).c_str()	);
	}
	else
	{
		int i;
		for(i=0;i<max.length()-s.length();i++)
		{
			string s1="";
			string s2="";
			for(int j=0;j<i;j++)
			{
				s1=s1+"X";
			}
			for(int j=0;j<max.length()-s.length()-i;j++)
			{
				s2=s2+"X";
			}
			int n=atoi(fun(s1+s+s2,max).c_str());
			if(n>currmax)
				currmax=n;
		}
	}	
}
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string a, b;
		cin>>a>>b;
		currmax=atoi(a.c_str());
		fun2(a,b);
		cout<<currmax<<endl;
	}
	return 0;
}