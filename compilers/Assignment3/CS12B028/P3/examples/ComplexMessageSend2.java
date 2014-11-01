class ComplexMessageSend2 {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class A {
	public Test bar(boolean x) {
		return new Test();
	}
	
	public boolean f1()
	{
		return true;
	}
	
	public boolean f3(int x)
	{
		return false;
	}
	
	public A f4(int[] a)
	{
		return new A();
	}
}

class Test {
    public int foo(int num) {
       A a;
       Test t;
       t = this;
       a = new A();
       t = (a.f4(this.f1(a.bar(a.f3(this.f3(this.f1(t))))))).bar(a.f3(this.f3(new int[5])));
       return 0;
    }
    
    public int[] f1(Test t) {
    	return new int[34];
    }
    
    public Test f2(Test t) {
	return new Test();
    }
    
    public int f3(int[] a)
    {
    	return 0;
    }
}
