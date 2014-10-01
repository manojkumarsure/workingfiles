//
// Generated by JTB GJ1.1
//

package syntaxtree;

import gj.util.*;

/**
 * Represents an optional grammar list, e.g. ( A )*
 */
public class NodeListOptional implements NodeListInterface {
   public NodeListOptional() {
      nodes = new Vector<Node>();
   }

   public NodeListOptional(Node firstNode) {
      nodes = new Vector<Node>();
      addNode(firstNode);
   }

   public void addNode(Node n) {
      nodes.addElement(n);
   }

   public Enumeration<Node> elements() { return nodes.elements(); }
   public Node elementAt(int i)  { return nodes.elementAt(i); }
   public int size()             { return nodes.size(); }
   public boolean present()      { return nodes.size() != 0; }
   public void accept(visitor.Visitor v) {
      v.visit(this);
   }
   public <R,A> R accept(visitor.GJVisitor<R,A> v, A argu) {
      return v.visit(this,argu);
   }
   public <R> R accept(visitor.GJNoArguVisitor<R> v) {
      return v.visit(this);
   }
   public <A> void accept(visitor.GJVoidVisitor<A> v, A argu) {
      v.visit(this,argu);
   }

   public Vector<Node> nodes;
}

