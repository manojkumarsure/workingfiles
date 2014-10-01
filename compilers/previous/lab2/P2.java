import syntaxtree.*;
import visitor.*;

public class P2 {
   public static void main(String [] args) {
      try {
         Node root = new MiniJavaParser(System.in).Goal();
         try
         {
			root.accept(new GJDepthFirst2(),(root.accept(new GJDepthFirst(),null))); // Your assignment part is invoked here.
			System.out.println("Program type checked successfully");
		  }
		  catch(Exception e)
		  {
			System.out.println("Type error main");
			System.exit(0);
		  }
      }
      catch (ParseException e) {
         System.out.println("Type error");
      }
   }
} 
