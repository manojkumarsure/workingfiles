class NotExpr {
    public static void main(String[] a){
            System.out.println(new Test().foo(10));
        }
}

class Test {
    public int foo(int num){
            int num_aux ;
            boolean a;
            a = !(num < 1);
            if (a)
                num_aux = 1 ;
            else
                num_aux = 2;
            return num_aux ;
        }
}
