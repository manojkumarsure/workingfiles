package visitor;
import java.util.*;
public class tempvariable
{
	public int tempnumber;
	public String ProcedureName;
	public int start;
	public int end;
	public String Allotreg;
	public int location;
	public tempvariable(int x,String name)
	{
		tempnumber=x;
		ProcedureName=name;
		start=99999999;
		end=-1;
		Allotreg=new String();
		location=0;
	}
}