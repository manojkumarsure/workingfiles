#define SWAP(x, y) { x = x+y; y = x-y; x = x-y; }

class SimpleMacroStmt {
    public static void main(String[] a){
        System.out.println(new A().run());
    }
}

class A {
    public int run(){
        int a;
        int b;
        a = 3;
        b = 5;
        SWAP(a, b);
        return a;
    }
} 
