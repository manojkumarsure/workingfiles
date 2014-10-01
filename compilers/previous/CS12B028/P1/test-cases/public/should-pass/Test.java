#define ZERO() (0+0)
class Test{
    public static void main(String[] a){
        System.out.println(new A().run());
    }
}
class A {
	int a;
	int b;
	int c;
    public int run(){
        return ZERO();
    }
}
