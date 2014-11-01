class Comparisonops {
	public static void main(String[] a){
		System.out.println(new Test().bar(false));
	}
}

class Test {
	public int bar(boolean flg){
		boolean y;
		boolean z;
		int a;
		a = 89;
		y = true;
		z = true;
		y = flg & y;
		z = a < 56;
		return a;
	}
}
