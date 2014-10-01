class SimpleClass {
    public static void main(String[] a){
        System.out.println(new A().run());
    }
}

class A {
    int _val_var__;
    public int run(){
        _val_var__ = 123;
        return _val_var__;
    }
} 
