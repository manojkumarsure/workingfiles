class ComplexPrint {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class A {
	public Test fn() {
		return new Test();
	}
}

class Test {
    public int foo(int num){
    	A a;
    	a = new A();
        System.out.println(num+((a.fn()).bar()));
        return 33;
    }

    public int bar() {
    	return 1;
    }
}
