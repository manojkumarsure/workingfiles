package visitor;
import syntaxtree.*;
import java.util.*;
public class method<R>
{
	public R scope;
	public R name;
	public R rettype;
	public R arglist;
	public R varlist;
	public void setScope(R scopename)
	{
		scope=scopename;
	}
	public void setName(R varname)
	{
		name=varname;
	}
	public void setType(R typename)
	{
		rettype=typename;
	}
	public void setArglist(R arguments)
	{
		arglist=arguments;
	}
	public void setVarlist(R vars)
	{
		varlist=vars;
	}
	public method()
	{
		scope=null;
		name=null;
		rettype=null;
		arglist=null;
	}
}