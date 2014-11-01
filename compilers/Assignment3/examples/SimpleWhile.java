class SimpleWhile{
    public static void main(String[] a){
        System.out.println(new Test().foo(56));
    }
}

class Test {
    public int foo(int val){
	    int i;
	    i = val;
        while(i < 45){
		i = i + 1;
	}
	return 0;
    }
}
