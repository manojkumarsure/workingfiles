package visitor;
import java.util.*
public class basicblock
{
	public int linenumber;
	public ArrayList<basicblock> next;
	public ArrayList<basicblock> prev;
	public ArrayList<tempvariable> used,defined,livein,liveout;
	public basicblock(int x)
	{
		linenumber=x;
		next=new ArrayList<basicblock>();
		prev=new ArrayList<basicblock>();
		used=new ArrayList<tempvariable>();
		defined=new ArrayList<tempvariable>();
		livein=new ArrayList<tempvariable>();
		liveout=new ArrayList<tempvariable>();
	}
}