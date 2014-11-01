class Classdecl {
    public static void main(String[] a){
        System.out.println(new Test().bar(5));
    }
}

class Test {
    int[] b;
    boolean flg;
    int val;
    A a;
    public int bar(int size){
        b=new int[size];
        flg=true;
        val=89;
        a=new A();
        return 0;
    }
}

class A {
	int a;
}

