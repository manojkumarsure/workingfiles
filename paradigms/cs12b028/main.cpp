#include "mat.h"
int main(int argc,char* argv[])
{
	string expression;
	FILE* fp;
	ifstream fp2 (argv[2]);
	fp=fopen(argv[1],"r");
	int rows=2;
	fscanf(fp,"%d",&rows);
	int **a;
	a=(int**)malloc(rows*sizeof(int*));
	for(int i=0;i<rows;i++)
	{
		a[i]=(int*)malloc(rows*sizeof(int));
	}
	for(int i=0;i<rows;i++)
	{
		for(int j=0;j<rows;j++)
		{
			fscanf(fp,"%d",&a[i][j]);
		}
	}
	fclose(fp);
	while(fp2>>expression)
	{
		EvalObject mat(a,rows,rows,-1);
		Error_handler eh(expression);
		expressionEvaluator EE(expression,mat);
		if(eh.verify()!=-1)
		{
			length=expression.length();
			EE.evaluate().print();
		}
		cout<<endl;
	}
}