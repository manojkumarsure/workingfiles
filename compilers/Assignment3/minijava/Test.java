class Test
{
	public static void main(String[] a)
	{
		System.out.println(new next().fx(5,6));
	}
}
class next
{
	int a;
	next b;
	public int fx(int s,int t)
	{
		a=5;
		while( 0 < a)
		{
			System.out.println(a);
			a=a-1;
		}
		b=new next();
		a=b.fz();
		return 1;
	}
	public int fz()
	{
		System.out.println(1234);
		return 0;
	}
}