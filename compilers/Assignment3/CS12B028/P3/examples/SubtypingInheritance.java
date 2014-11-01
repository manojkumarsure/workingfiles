class SubtypingInheritance {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class Parent {
	public int bar() {
		return 12;
	}
}

class Child extends Parent {
	public int bar() {
		return 16;
	}
}

class Parent2 {
}

class Child2 extends Parent2 {
}

class Parent3 {
	int f1;
	public Parent fn1(Parent2 obj) {
		Parent obj1;
		obj1 = new Child();
		return obj1;
	}
	
	public Parent2 fn2(Child2 obj) {
		return obj;
	}
}

class Child3 extends Parent3 {
	boolean f2;
	public Child fn1(Parent2 obj) {
		return new Child();
	}
	
	public Child2 fn3(Parent2 obj) {
		boolean f2;
		f2 = false;
		return new Child2();
	}
	
}

class Test {
	public int foo(int par) {
		Parent a1;
		Parent3 s1;
		Parent2 y1;
		Child m1;
		Child3 mr1;
		Child2 i1;
		y1 = new Child2();
		s1 = new Child3();
	
		a1 = s1.fn1(y1);
		a1 = s1.fn1(new Child2());
		y1 = s1.fn2(new Child2());
	
		mr1 = new Child3();
		y1 = mr1.fn3(new Parent2());
		m1 = mr1.fn1(new Child2());
	
		s1 = new Parent3();
		a1 = s1.fn1(y1);
		return 67;
	}
}
