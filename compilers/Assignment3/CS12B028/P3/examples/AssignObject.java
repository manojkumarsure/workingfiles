class AssignObject
{
	public static void main(String[] args) 
	{
		System.out.println(new Test().foo(10));
	}
}

class Test
{
	Test v1;
	public int foo(int num)
	{
		Test r2;
		v1 = new Test();
		return num;
	}
}
