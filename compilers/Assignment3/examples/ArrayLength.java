class ArrayLength {
    public static void main(String[] a){
        System.out.println(new Test().bar());
    }
}

class Test {
    public int bar() {
        int[] num_aux;
        int a;
        num_aux = new int[2];
        a = num_aux.length;
        return a;
    }
}
