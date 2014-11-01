class SimpleMessageSend {
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
        A obj;
        Test obj2;
        boolean flg;
        obj = new A();
        obj2 = obj.fn();
        flg = obj2.bar();
        return 33;
    }
    
    public boolean bar() {
    	return false;
    }
}
