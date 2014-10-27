import syntaxtree.*;
import visitor.*;

public class P5 {
   public static void main(String [] args) {
      try {
         Node root = new microIRParser(System.in).Goal();
         root.accept(new GJDepthFirst(),null); 
      }
      catch (ParseException e) {
         System.out.println(e.toString());
      }
   }
} 
