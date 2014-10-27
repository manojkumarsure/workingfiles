import sklearn.metrics
def count(l,a,x,y):
	c=0
	for i in range(x,y):
		if l[i]==a:
			c+=1
	return c
def printperform(l):
	prec0=count(l,0,0,20)/(count(l,0,0,80)*1.0)
	prec1=count(l,1,20,40)/(count(l,1,0,80)*1.0)
	prec2=count(l,2,40,60)/(count(l,2,0,80)*1.0)
	prec3=count(l,3,60,80)/(count(l,3,0,80)*1.0)
	rec0=count(l,0,0,20)/20.0
	rec1=count(l,1,20,40)/20.0
	rec2=count(l,2,40,60)/20.0
	rec3=count(l,3,60,80)/20.0
	f0=2*prec0*rec0/((prec0+rec0)*1.0)
	f1=2*prec1*rec1/((prec1+rec1)*1.0)
	f2=2*prec2*rec2/((prec2+rec2)*1.0)
	f3=2*prec3*rec3/((prec3+rec3)*1.0)
	print prec0,prec1,prec2,prec3
	print rec0,rec1,rec2,rec3
	print f0,f1,f2,f3
L=[3,2,3,3,2,3,3,3,3,3,3,2,3,1,3,3,2,2,0,3,1,1,1,1,2,2,1,2,2,2,2,2,1,1,2,1,1,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3]
print sklearn.metrics.accuracy_score(20*[0]+20*[1]+20*[2]+20*[3],L)
printperform(L)