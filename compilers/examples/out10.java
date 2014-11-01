class out10{
    public static void main(String[] a){
        System.out.println(new Fac1().Start());
    }
}

class Fac {
    int num;
    int[] c;
    public int ComputeFac(int num){
        int num_aux ;
        if (num < 1)
            num_aux = 1 ;
        else
            num_aux = num * (this.ComputeFac(num-2)) ;
        return num_aux ;
    }

    public int tellyNum(int hi) {
        c = new int[hi];
        c[(hi-1)] = 45;
        return c[(hi-1)];
    }

    public int underLyingC() {
        return c[22];
    }
    public int call() {
        return this.ComputeFac(10);
    }
}

class Fac1 extends Fac {
    int num;
    Fac a;
    int[] c;
    public int Start() {
        int a;
        a = this.call1();
        return a;
    }
    public int ComputeFac(int num){
        int num_aux ;
        if (num < 1)
            num_aux = 1 ;
        else {
            a = this;
            num_aux = num * (a.ComputeFac(num-1)) ;

        }
        return num_aux ;
    }

    public int tellNum(int hi) {
        c = new int[hi];
        c[(hi-1)] = 33;
        num = this.tellyNum(hi);
        return 0;
    }
    public int call1() {
        num = this.call();
        return num;
    }
}
