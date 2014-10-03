//
// Generated by JTB 1.3.2
//

package visitor;
import syntaxtree.*;
import java.util.*;

/**
 * Provides default methods which visit each node in the tree in depth-first
 * order.  Your visitors may extend this class.
 */
public class GJDepthFirst<R,A> implements GJVisitor<R,A> {
   //
   // Auto class visitors--probably don't need to be overridden.
   //
	HashMap<R,R> symboltable = new HashMap<R,R>();
   public R visit(NodeList n, A argu) {
      R _ret=null;
      int _count=0;
      for ( Enumeration<Node> e = n.elements(); e.hasMoreElements(); ) {
         e.nextElement().accept(this,argu);
         _count++;
      }
      return _ret;
   }

   public R visit(NodeListOptional n, A argu) {
      if ( n.present() ) {
         R _ret=null;
         int _count=0;
         List<R> l = new LinkedList<R>();
         for ( Enumeration<Node> e = n.elements(); e.hasMoreElements(); ) {
            l.add(e.nextElement().accept(this,argu));
            _count++;
         }
         return (R) l;
      }
      else
         return null;
   }

   public R visit(NodeOptional n, A argu) {
      if ( n.present() )
         return n.node.accept(this,argu);
      else
         return null;
   }

   public R visit(NodeSequence n, A argu) {
      R _ret=null;
      int _count=0;
      for ( Enumeration<Node> e = n.elements(); e.hasMoreElements(); ) {
         e.nextElement().accept(this,argu);
         _count++;
      }
      return _ret;
   }

   public R visit(NodeToken n, A argu) { return null; }

   //
   // User-generated visitor methods below
   //
   public boolean classAssignable(R x,R y)
    {
		if(x.toString().equals(y.toString()))
			return true;
		if(symboltable.get((R)x.toString())==null)
			return false;
		if(symboltable.get((R)y.toString())==null)
			return false;
		classtable a=new classtable();
		classtable b=new classtable();
		a=(classtable)symboltable.get((R)x.toString());
		b=(classtable)symboltable.get((R)y.toString());
		if((a.classname.toString()).equals(b.classname.toString()))
			return true;
		R curr = (R)a.parentclass;
		while(curr!=null)
		{
			curr=symboltable.get((R)curr.toString());
			if((((classtable)curr).classname.toString()).equals(b.classname.toString()))
				return true;
			curr=(R)((classtable)curr).parentclass;
		}
		return false;
    }
   public void classcycle()
	{
		for(R key:symboltable.keySet())
		{
			HashMap<R,R> classtraverse=new HashMap<R,R>();
			try{
				classtable x=new classtable();
				x=((classtable)symboltable.get(key));
				classtraverse.put((R)x,(R)"1");
				R curr=(R)x.parentclass;
				while(curr!=null)
				{
					curr=symboltable.get((R)curr.toString());
					if(classtraverse.get(curr)==null)
						classtraverse.put(curr,(R)"1");
					curr=(R)((classtable)curr).parentclass;
				}
			}
			catch(ClassCastException e){}
		}
	}
   public void checkoverloading()
   {
		classcycle();
		for(R key: symboltable.keySet())
		{
            try
            {
				classtable x=new classtable();
				x=((classtable)symboltable.get(key));
				if((x.meths.toString()).equals(""))
					continue;
				else
				{
					R curr=(R)x.parentclass;
					while(curr!=null)
					{
						curr=symboltable.get((R)curr.toString());
						for (String retval: (x.meths.toString()).split(";"))
						{
							if(retval.equals(""))
								break;
							else
							{
								for (String retval2: ((((classtable)curr).meths).toString()).split(";"))
								{
									if(retval.equals(retval2))
										continue;
									try{
									if(retval!=retval2 && retval.split(" ")[1].equals(retval2.split(" ")[1]))
									{
										if(classAssignable((R)retval,(R)retval2))
											continue;
									}
									}
									catch(ArrayIndexOutOfBoundsException e){}
								}
							}
						}
						curr=(R)((classtable)curr).parentclass;
					}
				}
            }
            catch(ClassCastException e)
            {}
        }
   }
   /**
    * f0 -> MainClass()
    * f1 -> ( TypeDeclaration() )*
    * f2 -> <EOF>
    */
   public R visit(Goal n, A argu) {
      R _ret=null;
      argu = (A) "";
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      checkoverloading();
      return (R)symboltable;
   }

   /**
    * f0 -> "class"
    * f1 -> Identifier()
    * f2 -> "{"
    * f3 -> "public"
    * f4 -> "static"
    * f5 -> "void"
    * f6 -> "main"
    * f7 -> "("
    * f8 -> "R"
    * f9 -> "["
    * f10 -> "]"
    * f11 -> Identifier()
    * f12 -> ")"
    * f13 -> "{"
    * f14 -> PrintStatement()
    * f15 -> "}"
    * f16 -> "}"
    */
   public R visit(MainClass n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      R classname = n.f1.accept(this, argu);
      //argu = (A) (((String) argu) + _ret + ":");
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      n.f5.accept(this, argu);
      n.f6.accept(this, argu);
      n.f7.accept(this, argu);
      n.f8.accept(this, argu);
      n.f9.accept(this, argu);
      n.f10.accept(this, argu);
      R args = n.f11.accept(this, argu);
      n.f12.accept(this, argu);
      n.f13.accept(this, argu);
      n.f14.accept(this, argu);
      n.f15.accept(this, argu);
      n.f16.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> ClassDeclaration()
    *       | ClassExtendsDeclaration()
    */
   public R visit(TypeDeclaration n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "class"
    * f1 -> Identifier()
    * f2 -> "{"
    * f3 -> ( VarDeclaration() )*
    * f4 -> ( MethodDeclaration() )*
    * f5 -> "}"
    */
   public R visit(ClassDeclaration n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      _ret = n.f1.accept(this, argu);
      A oldArgu = argu;
      argu = (A) ((String) argu + _ret + ":");
      n.f2.accept(this, argu);
      R vars= n.f3.accept(this, argu);
      String out="";
      if (vars == null)
          vars = (R) new LinkedList<R>();
      List<R> l =(List<R>)vars;
      ListIterator<R> i = l.listIterator();
      while(i.hasNext())
		out+=i.next();
	  vars=(R)out;
      R meths= n.f4.accept(this, argu);
      String out2="";
      if (meths == null)
          meths = (R) new LinkedList<R>();
      List<R> l2= (List<R>)meths;
      ListIterator<R> i2 = l2.listIterator();
      while(i2.hasNext())
		out2+=i2.next();
	  meths=(R)out2;
      n.f5.accept(this, argu);
      classtable x=new classtable();
      x.setName(_ret);
      x.setVars(vars);
      x.setMeths(meths);
      x.setScope((R)(((String) oldArgu) + _ret.toString()));
      symboltable.put((R)(((String) oldArgu) + _ret.toString()),(R)x);
      return _ret;
   }

   /**
    * f0 -> "class"
    * f1 -> Identifier()
    * f2 -> "extends"
    * f3 -> Identifier()
    * f4 -> "{"
    * f5 -> ( VarDeclaration() )*
    * f6 -> ( MethodDeclaration() )*
    * f7 -> "}"
    */
   public R visit(ClassExtendsDeclaration n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      _ret = n.f1.accept(this, argu);
      A oldArgu = argu;
      argu = (A) ((String) argu + _ret + ":");
      n.f2.accept(this, argu);
      R parent=n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      R vars=n.f5.accept(this, argu);
      String out="";
      if (vars == null)
          vars = (R) new LinkedList<R>();
      List<R> l= (List<R>)vars;
      ListIterator<R> i = l.listIterator();
      while(i.hasNext())
		out+=i.next();
	  vars=(R)out;
      R meths=n.f6.accept(this, argu);
      String out2="";
      if (meths == null)
          meths = (R) new LinkedList<R>();
      List<R> l2= (List<R>)meths;
      ListIterator<R> i2 = l2.listIterator();
      while(i2.hasNext())
		out2+=i2.next();
	  meths=(R)out2;
      n.f7.accept(this, argu);
      classtable x=new classtable();
      x.setName(_ret);
      x.setVars(vars);
      x.setMeths(meths);
      x.setScope((R)(((String) oldArgu) + _ret.toString()));
      x.setParent(parent);
      symboltable.put((R)(((String) oldArgu) + _ret.toString()),(R)x);
      return _ret;
   }

   /**
    * f0 -> Type()
    * f1 -> Identifier()
    * f2 -> ";"
    */
   public R visit(VarDeclaration n, A argu) {
      R _ret=null;
      R typename = n.f0.accept(this, argu);
      R varname = n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      variable x=new variable();
      x.setScope((R)(((String)argu) +varname.toString()));
      x.setName(varname);
      x.setType(typename);
      symboltable.put((R)(((String)argu) +varname.toString()),(R)x);
      return (R)(typename+" "+varname+",");
   }

   /**
    * f0 -> "public"
    * f1 -> Type()
    * f2 -> Identifier()
    * f3 -> "("
    * f4 -> ( FormalParameterList() )?
    * f5 -> ")"
    * f6 -> "{"
    * f7 -> ( VarDeclaration() )*
    * f8 -> ( Statement() )*
    * f9 -> "return"
    * f10 -> Expression()
    * f11 -> ";"
    * f12 -> "}"
    */
   public R visit(MethodDeclaration n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      R typename = n.f1.accept(this, argu);
      R methname = n.f2.accept(this, argu);
      A oldArgu = argu;
      argu = (A) (((String)argu) + methname + ":");
      n.f3.accept(this, argu);
      R plist = n.f4.accept(this, argu);
      if (plist == null)
        plist = (R) "";
      n.f5.accept(this, argu);
      n.f6.accept(this, argu);
      R vars=n.f7.accept(this, argu);
      String out="";
      if (vars == null)
          vars = (R) new LinkedList<R>();
      List<R> l= (List<R>)vars;
      ListIterator<R> i = l.listIterator();
      while(i.hasNext())
		out+=i.next();
	  vars=(R)out;
      n.f8.accept(this, argu);
      n.f9.accept(this, argu);
      n.f10.accept(this, argu);
      n.f11.accept(this, argu);
      n.f12.accept(this, argu);
      method x=new method();
      x.setName(methname);
      x.setType(typename);
      x.setScope((R)(((String)oldArgu) + methname.toString()));
      x.setArglist(plist);
      x.setVarlist(vars);
      symboltable.put((R)(((String)oldArgu) + methname.toString()),(R)x);
      return (R)(String)(typename+" "+methname+":"+plist+";");
   }

   /**
    * f0 -> FormalParameter()
    * f1 -> ( FormalParameterRest() )*
    */
   public R visit(FormalParameterList n, A argu) {
      R _ret=null;
      R fp = n.f0.accept(this, argu);
      R fpr = n.f1.accept(this, argu);
      String out = "";
      if (fpr == null)
          fpr = (R) new LinkedList<R>();
      if (fp == null)
          fp = (R) "";
      List<R> l = (List<R>) fpr;
      ListIterator<R> i = l.listIterator();
      while (i.hasNext())
          out += i.next();
      return (R) (fp + out);
   }

   /**
    * f0 -> Type()
    * f1 -> Identifier()
    */
   public R visit(FormalParameter n, A argu) {
      R _ret=null;
      R typename = n.f0.accept(this, argu);
      R varname = n.f1.accept(this, argu);
      variable x=new variable();
      x.setScope((R)(((String)argu) +varname.toString()));
      x.setName(varname);
      x.setType(typename);
      symboltable.put((R)(((String)argu) +varname.toString()),(R)x);
      return varname;
   }

   /**
    * f0 -> ","
    * f1 -> FormalParameter()
    */
   public R visit(FormalParameterRest n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      _ret = (R) ("," + n.f1.accept(this, argu));
      return _ret;
   }

   /**
    * f0 -> ArrayType()
    *       | BooleanType()
    *       | IntegerType()
    *       | Identifier()
    */
   public R visit(Type n, A argu) {
      R _ret=null;
      _ret = n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "int"
    * f1 -> "["
    * f2 -> "]"
    */
   public R visit(ArrayType n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return (R) "int[]";
   }

   /**
    * f0 -> "boolean"
    */
   public R visit(BooleanType n, A argu) {
      R _ret=null;
      _ret = n.f0.accept(this, argu);
      return (R) "boolean";
   }

   /**
    * f0 -> "int"
    */
   public R visit(IntegerType n, A argu) {
      R _ret=null;
      _ret = n.f0.accept(this, argu);
      return (R) "int";
   }

   /**
    * f0 -> Block()
    *       | AssignmentStatement()
    *       | ArrayAssignmentStatement()
    *       | IfStatement()
    *       | WhileStatement()
    *       | PrintStatement()
    */
   public R visit(Statement n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "{"
    * f1 -> ( Statement() )*
    * f2 -> "}"
    */
   public R visit(Block n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> Identifier()
    * f1 -> "="
    * f2 -> Expression()
    * f3 -> ";"
    */
   public R visit(AssignmentStatement n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> Identifier()
    * f1 -> "["
    * f2 -> Expression()
    * f3 -> "]"
    * f4 -> "="
    * f5 -> Expression()
    * f6 -> ";"
    */
   public R visit(ArrayAssignmentStatement n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      n.f5.accept(this, argu);
      n.f6.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "if"
    * f1 -> "("
    * f2 -> Expression()
    * f3 -> ")"
    * f4 -> Statement()
    * f5 -> "else"
    * f6 -> Statement()
    */
   public R visit(IfStatement n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      n.f5.accept(this, argu);
      n.f6.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "while"
    * f1 -> "("
    * f2 -> Expression()
    * f3 -> ")"
    * f4 -> Statement()
    */
   public R visit(WhileStatement n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "System.out.println"
    * f1 -> "("
    * f2 -> Expression()
    * f3 -> ")"
    * f4 -> ";"
    */
   public R visit(PrintStatement n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> AndExpression()
    *       | CompareExpression()
    *       | PlusExpression()
    *       | MinusExpression()
    *       | TimesExpression()
    *       | ArrayLookup()
    *       | ArrayLength()
    *       | MessageSend()
    *       | PrimaryExpression()
    */
   public R visit(Expression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "&"
    * f2 -> PrimaryExpression()
    */
   public R visit(AndExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "<"
    * f2 -> PrimaryExpression()
    */
   public R visit(CompareExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "+"
    * f2 -> PrimaryExpression()
    */
   public R visit(PlusExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "-"
    * f2 -> PrimaryExpression()
    */
   public R visit(MinusExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "*"
    * f2 -> PrimaryExpression()
    */
   public R visit(TimesExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "["
    * f2 -> PrimaryExpression()
    * f3 -> "]"
    */
   public R visit(ArrayLookup n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "."
    * f2 -> "length"
    */
   public R visit(ArrayLength n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> PrimaryExpression()
    * f1 -> "."
    * f2 -> Identifier()
    * f3 -> "("
    * f4 -> ( ExpressionList() )?
    * f5 -> ")"
    */
   public R visit(MessageSend n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      n.f5.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> Expression()
    * f1 -> ( ExpressionRest() )*
    */
   public R visit(ExpressionList n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> ","
    * f1 -> Expression()
    */
   public R visit(ExpressionRest n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> IntegerLiteral()
    *       | TrueLiteral()
    *       | FalseLiteral()
    *       | Identifier()
    *       | ThisExpression()
    *       | ArrayAllocationExpression()
    *       | AllocationExpression()
    *       | NotExpression()
    *       | BracketExpression()
    */
   public R visit(PrimaryExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> <INTEGER_LITERAL>
    */
   public R visit(IntegerLiteral n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "true"
    */
   public R visit(TrueLiteral n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "false"
    */
   public R visit(FalseLiteral n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> <IDENTIFIER>
    */
   public R visit(Identifier n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      if (argu == null)
        argu = (A) "";
      _ret = (R) n.f0;
      return _ret;
   }

   /**
    * f0 -> "this"
    */
   public R visit(ThisExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "new"
    * f1 -> "int"
    * f2 -> "["
    * f3 -> Expression()
    * f4 -> "]"
    */
   public R visit(ArrayAllocationExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      n.f4.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "new"
    * f1 -> Identifier()
    * f2 -> "("
    * f3 -> ")"
    */
   public R visit(AllocationExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      n.f3.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "!"
    * f1 -> Expression()
    */
   public R visit(NotExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      return _ret;
   }

   /**
    * f0 -> "("
    * f1 -> Expression()
    * f2 -> ")"
    */
   public R visit(BracketExpression n, A argu) {
      R _ret=null;
      n.f0.accept(this, argu);
      n.f1.accept(this, argu);
      n.f2.accept(this, argu);
      return _ret;
   }

}