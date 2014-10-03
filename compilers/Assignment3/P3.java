import syntaxtree.*;
import visitor.*;

public class P3 {
   public static void main(String [] args) {
      try {
         Node root = new MiniJavaParser(System.in).Goal();
		root.accept(new GJDepthFirst2(),(root.accept(new GJDepthFirst(),null)));
      }
      catch (ParseException e) {
         System.err.println(e.toString());
      }
   }
} 
