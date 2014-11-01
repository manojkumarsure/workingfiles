class test3{
    public static void main(String[] jingli){
	System.out.println(new BS().Start(20));
    }
}
// This class contains an array of integers and
// methods to initialize, print and search the array
// using Binary Search
class GS {
	//int x;
	//boolean qq;
	//int aa;
	public int Start(int k) {
		return 9;
	}
	public int End(int l, boolean g, int ll) {
		return 10000;
	}
}
class BS extends GS{
	//int a;

	int [] b;

	public int Start(int j) {
		int ll;
		int [] s;
		ll = 9;
		s = new int [10];
		s = this.Array(8);
		ll = s[7];
		return ll;
	}

	public int [] Array(int j) {
		int [] x;
		int l;
		x = new int [j];
		System.out.println(1);
		l = x[(j-1)];
		x[0] = 101;
		x[0] = l;
		x[7] = this.End(1, true, x[0]);
		return x;
	}

	public int End(int l, boolean g, int ll) {
		int x;
		x = this.not_test(true);
		return ll + x;
	}

	public int not_test(boolean b) {
		int x;
		if(!b) {
			x = 78;
		}
		else {
			x = 99;
		}
		x = this.newarrayinittest(x);
		return x;
	}

	public int newarrayinittest(int x) {
		int []y;
		y = new int [8];
		y[7] = this.arraylengthtest(8);
		return (y[7]) + x;
	}

	public int arraylengthtest(int x) {
		int [] j;
		j = new int [15];
		return (j.length) + (this.calltest(100));
	}

	public int calltest(int x) {
		GS v;
		v = new GS();
		x = v.End(x, true, x);
		return x + (this.arrayaccesstest());
	}
	public int arrayaccesstest() {
		int [] x;
		x = new int [89];
		return (x[78]) + (this.globalarrayaccesstest());
	}

	public int globalarrayaccesstest() {
		//return b[89];
		return 2000;
	}

	public int whiletest() {
		boolean x;
		x = true;
		while(x) {
			x = false;
		}
		return 0;
	}
}
