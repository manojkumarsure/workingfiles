class AssignBool 
{
	public static void main(String[] args) 
	{
		System.out.println(new Test().foo(true, 11));
	}
}

class Test
{
	public int foo(boolean flg, int num2)
	{
		int y;
		int x;
		boolean flag;
		y = 90;
		x = 8;
		flag = false;
		flag = (flg & ((x < (y*x)) & flg));//complicate
		return num2;
	}
}
