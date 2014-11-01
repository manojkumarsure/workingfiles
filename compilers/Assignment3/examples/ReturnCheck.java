class ReturnCheck{
    public static void main(String[] a){
            System.out.println(new Test().foo(10));
        }
}

class Test {
    public int foo(int num) {
    	return (num * 12) + 3;
    }
        
    public int[] f1() {
    	int[] b;
    	b = new int[3];
    	return b;
    }
    
    public Test f2() {
    	return new Test();
    }
    
    public boolean f3() {
    	return true; //bool exp
    }
}

