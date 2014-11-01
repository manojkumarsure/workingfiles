class Recurse{
    public static void main(String[] a){
        System.out.println(new Test().bar(10));
    }
}

class Test {
    public int bar(int num){
        int num_aux ;
        if (num < 0)
            num_aux = 0;
        else
            num_aux = this.foo(num-1) ;
        return num_aux ;
    }
    
    public int foo(int num){
    	int num_aux ;
        if (num < 0)
            num_aux = 0;
        else
            num_aux = this.bar(num-1) ;
        return num_aux ;
    }
}
