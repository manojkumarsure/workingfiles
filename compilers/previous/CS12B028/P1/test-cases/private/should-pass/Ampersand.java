class Ampersand {
	public static void main(String[] a){
		System.out.println(new A().run());
	}
}

class A {
	public boolean run() {
		System.out.println(true & true);
		System.out.println(true & false);
		System.out.println(false & true);
		return false & false;
	}
}
