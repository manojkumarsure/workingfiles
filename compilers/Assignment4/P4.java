import syntaxtree.*;
import visitor.*;

public class P4 {
   public static void main(String [] args) {
      try {
         Node root = new MiniIRParser(System.in).Goal();
         root.accept(new GJNoArguDepthFirst());
		root.accept(new GJDepthFirst(),null);
      }
      catch (ParseException e) {
         System.err.println(e.toString());
      }
   }
} 
