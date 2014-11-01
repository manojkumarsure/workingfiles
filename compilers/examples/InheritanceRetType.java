class InheritanceRetType {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class Parent {
	int f1;
	public A fn1(boolean flg) {
		return new A();
	}
	
}

class Child extends Parent {
	boolean f2;
	public B fn1(boolean flg1) {
		return new B();
	}
	
	
}

class Test {
	public int foo(int par) {
		Parent obj1;
		Child obj2;
		A a;
		int val;
		boolean flg;
		obj1 = new Parent();
		obj2 = new Child();
		obj1 = obj2;
		obj1 = new Child();
		a = obj1.fn1(true);
		return 67;
	}
}

class A{}
class B extends A{}
