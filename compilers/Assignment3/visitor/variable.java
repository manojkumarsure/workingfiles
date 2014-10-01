package visitor;
import syntaxtree.*;
import java.util.*;
public class variable<R>
{
	public R scope;
	public R name;
	public R type;
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
		type=typename;
	}
	public variable()
	{
		scope=null;
		name=null;
		type=null;
	}
}