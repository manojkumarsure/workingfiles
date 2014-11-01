class ComplexMessageSend {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class A {
	public Test bar() {
		return new Test();
	}
}

class Test {
    public int foo(int num) {
        int val;
        A obj1;
        Test obj2;
        obj1 = new A();
        val = (((new A().bar()).f2()).f1());
        val = ((((((new A()))).bar()).f2()).f1());
        val = ((this.f2()).f1());
        val = (((obj1.bar()).f2()).f1());
        return new Test().f1();
    }
    
    public int f1() {
    	return 34;
    }
    
    public Test f2() {
	return new Test();
    }
}
