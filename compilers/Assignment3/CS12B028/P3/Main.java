import syntaxtree.*;
import visitor.*;

public class Main {
   public static void main(String [] args) {
      try {
         Node root = new MiniJavaParser(System.in).Goal();
         root.accept(new GJDepthFirst1(),root.accept(new GJDepthFirst3(),null)); // Your assignment part is invoked here
         
      }
      catch (Exception e) {
         e.printStackTrace();
      }
   }
} 


