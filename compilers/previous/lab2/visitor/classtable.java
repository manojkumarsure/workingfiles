package visitor;
import syntaxtree.*;
import java.util.*;

public class classtable<R>
{
	public R classname;
	public R scope;
	public R vars;
	public R meths;
	public R parentclass;
	public void setName(R name)
	{
		classname=name;
	}
	public void setVars(R variablelist)
	{
		vars=variablelist;
	}
	public void setMeths(R methodlist)
	{
		meths=methodlist;
	}
	public void setScope(R scopename)
	{
		scope=scopename;
	}
	public void setParent(R parentname)
	{
		parentclass=parentname;
	}
	public classtable()
	{
		classname=null;
		scope=null;
		vars=null;
		meths=null;
	}
}