class OverRideReturnType {
    public static void main(String[] a){
        System.out.println(new Test().foo(5));
    }
}

class Parent {
	public Parent2 bar() {
		return new Parent2();
	}
}

class Child extends Parent {
	public Child2 bar() {
		return new Child2();
	}
}

class Parent2 {
}

class Child2 extends Parent2 {
}


class Test {
	public int foo(int par) {
		
		return 67;
	}
}
