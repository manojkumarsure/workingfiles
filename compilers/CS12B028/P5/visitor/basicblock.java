package visitor;
import java.util.*;
public class basicblock
{
	public int linenumber;
	public ArrayList<basicblock> succ;
	public ArrayList<basicblock> prev;
	public ArrayList<tempvariable> used,defined,livein,liveout,liveintemp,liveouttemp;
	public basicblock(int x)
	{
		linenumber=x;
		succ=new ArrayList<basicblock>();
		prev=new ArrayList<basicblock>();
		used=new ArrayList<tempvariable>();
		defined=new ArrayList<tempvariable>();
		livein=new ArrayList<tempvariable>();
		liveout=new ArrayList<tempvariable>();
		liveintemp=new ArrayList<tempvariable>();
		liveouttemp=new ArrayList<tempvariable>();
	}
}