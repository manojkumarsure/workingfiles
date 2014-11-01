class FunctionArgs {
    public static void main(String[] a){
      System.out.println(new Test().foo(10, false));
    }
}

class Test {
    public int foo(int num, boolean awesome) {
    	int []hello;
        A a;
        a = new A();
        hello = new int[34];
        hello = a.bar(hello, new A());
        return 78;
    }
}

class A {
	public int[] bar(int[] ar, A a) {
		return ar;
	}
}

