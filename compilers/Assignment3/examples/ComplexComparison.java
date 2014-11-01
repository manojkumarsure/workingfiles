class ComplexComparison{
    public static void main(String[] a){
        System.out.println(new Test().bar(new Test()));
    }
}


class Test {
    public int bar(Test obj){
    	int a;
    	int num;
    	boolean flg;
    	a = 8;
    	num = 45;
    	flg = true;
        if(((a<num) & (num<a)) & flg) {
        	flg = false; 
	} else {
		flg = true;
	}
	return 0;
    }
}
