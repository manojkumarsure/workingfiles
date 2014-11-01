class ComplexArrayLookup {
	public static void main(String[] a){
		System.out.println(new Test().foo(2,4));
	}
}

class Test{

	public int foo(int index1, int num){
		int [] arr ;
		int [] arr2;
		int x;
		arr = new int[num];
		arr2 = this.bar();
		x = arr[3];
		x = arr[(arr2[(this.f1(arr[0]))])];
		return x;
	}
	
	public int[] bar()
	{
		return new int[20];
	}
	
	public int f1(int x)
	{
		return 0;
	}
}
