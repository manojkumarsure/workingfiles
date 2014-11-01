public void classAssignable(R x,R y)
    {
		if(x.toString().equals(y.toString()))
			return;
		classtable a=new classtable();
		classtable b=new classtable();
		a=(classtable)symboltable.get((R)x.toString());
		b=(classtable)symboltable.get((R)y.toString());
		if((a.classname.toString()).equals(b.classname.toString()))
			return;
		R curr = (R)a.parentclass;
		while(curr!=null)
		{
			curr=symboltable.get((R)curr.toString());
			if((((classtable)curr).classname.toString()).equals(b.classname.toString()))
				return;
			curr=(R)((classtable)curr).parentclass;
		}
    }
	public R check(R x)
	{
		R _ret=null;
		String left=new String();
		left=x.toString();
		classtable z=new classtable();
		z=(classtable)symboltable.get((R)(left.split(":")[0]));
		if(symboltable.get((R)left)==null)
		{
			if(symboltable.get((R)(left.split(":")[0]+":"+left.split(":")[left.split(":").length-1]))!=null)
			{
				left=left.split(":")[0]+":"+left.split(":")[left.split(":").length-1];
			}
			else
			{
				while(z.parentclass!=null)
				{
					z=(classtable)symboltable.get((R)z.parentclass.toString());
					if(symboltable.get(left)==null)
						left=z.classname.toString()+":"+left.split(":")[left.split(":").length-1];
					else
						break;
				}
			}
		}
		variable a=new variable();
		classtable b = new classtable();
		try{
				a=(variable)symboltable.get((R)left);
				return (R)a.type;
			}
			catch(ClassCastException e)
			{
				b=(classtable)symboltable.get((R)left);
				return (R)b.classname;
			}
	}
	R checkfn(R a,String signature)
	{
		R _ret=null;
		classtable b = (classtable)symboltable.get((R)a.toString());
		while(b!=null)
		{
			String s = b.meths.toString();
			if(!s.equals(""))
			{
				for(String s1 : s.split(";"))
				{
					if(signature.equals(s1.split(" ")[1]))
					{
						return (R)s1.split(" ")[0];
					}
					else
					{
						if(s1.split(" ")[1].split(":")[0].equals(signature.split(":")[0]))
						{
							int length=s1.split(" ")[1].split(":")[1].split(",").length;
							int i=0;
							for(String s2 : s1.split(" ")[1].split(":")[1].split(","))
							{
								classAssignable((R)signature.split(":")[1].split(",")[i],(R)s2);
							}
							return (R)s1.split(" ")[0];
						}
					}
				}
			}
			b=(classtable)symboltable.get(b.parentclass);
		}
		return _ret;
	}