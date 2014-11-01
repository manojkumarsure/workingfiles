package visitor;
import java.util.*;
public class procedure
{
	public int a,b,c;
	public String procname;
	public ArrayList<basicblock> method;
	public int start;
	public int end;
	public procedure(String name)
	{
		a=0;
		b=0;
		c=0;
		procname=name;
		method = new ArrayList<basicblock>();
	}
}