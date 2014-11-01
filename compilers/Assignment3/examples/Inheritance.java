class Inheritance {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class Parent {
	int f1;
	public int fn1(boolean flg) {
		return 34;
	}
	
	public boolean fn2(boolean flg) {
		return flg;
	}
}

class Child extends Parent {
	boolean f2;
	public int fn1(boolean flg1) {
		f1 = 23;
		return 36;
	}
	
	public boolean fn2(boolean par) {
		f2 = false;
		return par;
	}
	
}

class Test {
	public int foo(int par) {
		Parent obj1;
		Child obj2;
		int val;
		boolean flg;
		obj1 = new Parent();
		obj2 = new Child();
		flg = obj1.fn2(true);
		flg = obj2.fn2(false);
		obj1 = obj2;
		obj1 = new Child();
		val = obj1.fn1(true);
		return 67;
	}
}
