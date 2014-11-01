class This{
    public static void main(String[] a){
        System.out.println(new Test().bar(1,2,3));
    }
}


class Test {
    public int bar(int p1, int p2,int size){
	int[] p3;
	int aux;
	Test obj;
	boolean flg;
	obj = this;
	p3=new int[size];
	aux = obj.f1(p1, p2);
	flg = this.f2();
        aux = this.f1(p1,p2);
	return 1 ;
    }

    public int f1(int p1, int p2){
        return 0 ;
    }
    
    public boolean f2() {
	return true;
    }
}
