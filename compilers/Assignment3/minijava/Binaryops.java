class Binaryops{
	public static void main(String[] a){
		System.out.println(new Test().foo(2));
	}
}

class Test {

	public int foo(int num){
		int y;
		int z;
		y = num - num;
		z = y + num;
		y = z * 45;
		return y;
	}
}
