class ArrayLookup {
	public static void main(String[] a){
		System.out.println(new Test().foo(2,4));
	}
}

class Test{

	public int foo(int index1, int num){
		int [] arr ;
		int x;
		arr = new int[num];
		x = arr[3];
		x = arr[index1];
		return x;
	}
}
