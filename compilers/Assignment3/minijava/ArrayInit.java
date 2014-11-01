class ArrayInit {
    public static void main(String[] a){
            System.out.println(new Test().foo(5));
        }
}

class Test {
    public int foo(int num){
            int[] aray1;
            int[] aray2;
            int[] aray3;
            aray1 = new int[num];
            aray2 = new int[5];
            aray3 = new int[num*5];
            aray3 = aray1;
            return 5;
        }
}

