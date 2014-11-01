class NameConflict {
    public static void main(String[] a){
        System.out.println(new Test().foo());
    }
}

class Parent {
	int f1;
	
	public boolean f1() {
		boolean f1;
		f1 = false;
		return f1;
	}
	
	public int fn() {
		return f1;
	}
}

class Child extends Parent {
	boolean f1;
	int f2;
	
	public boolean f1() {
		return f1;
	}
	
	public int fn() {
		return f2;
	}
}

class Test {
	public int foo() {
		Child n1;
		Parent b1;
		boolean ans;
		b1 = new Child();
		ans = b1.f1();//Add field access f1
		return 4;
	}
}
