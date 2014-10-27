import random
import math
import numpy
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
inputnodes=96
hiddennodes=6
outputnodes=4
gamma=0.01
gam=0.01
iterations=100
new=1
def sigmoid(x):
	return 1.0/(1+math.exp(-x))
def sigmoidder(x):
	return sigmoid(x)*(1-sigmoid(x))
alpha=[]
beta=[]
fp=open('DS2-train.csv','r')
s=fp.read()
fp.close()
Data=[]
Dataoutp=[]
Test=[]
Testoutp=[]
count=0
for i in s.split('\n')[:-1]:
	Data.append([])
	for j in i.split(',')[:-1]:
		Data[count].append(float(j))
	Dataoutp.append(float(i.split(',')[-1]))
	count+=1
fp=open('DS2-test.csv','r')
s=fp.read()
fp.close()
count=0
for i in s.split('\n')[:-1]:
	Test.append([])
	for j in i.split(',')[:-1]:
		Test[count].append(float(j))
	Testoutp.append(float(i.split(',')[-1]))
	count+=1
N=len(Data)
for i in range(hiddennodes):
	alpha.append([])
	for j in range(inputnodes+1):
		alpha[i].append(random.uniform(-0.5,0.5))
for i in range(outputnodes):
	beta.append([])
	for j in range(hiddennodes+1):
		beta[i].append(random.uniform(-0.5,0.5))
x=Data
y=[]
for i in Dataoutp:
	if(i==0):
		y.append([1,0,0,0])
	elif(i==1):
		y.append([0,1,0,0])
	elif(i==2):
		y.append([0,0,1,0])
	elif(i==3):
		y.append([0,0,0,1])
def g(T,k):
	sum=0
	for i in T:
		sum+=math.exp(i)
	return math.exp(T[k])/sum
for it in range(iterations):
	fun=[]
	Z=[]
	for i in range(N):
		z=[]
		for j in range(hiddennodes):
			z.append(sigmoid(alpha[j][0]+numpy.dot(alpha[j][1:],x[i])))
		Z.append(z)
		T=[]
		for k in range(outputnodes):
			T.append(beta[k][0]+numpy.dot(beta[k][1:],z))
		f=[]
		for k in range(outputnodes):
			f.append(g(T,k))
		fun.append(f)
	for i in range(hiddennodes):
		for j in range(outputnodes):
			sum=0
			for t in range(N):
				sum=sum-((2-new)*(y[t][j]-fun[t][j])*sigmoidder(numpy.dot(beta[j][1:],Z[t]))*Z[t][i])
			beta[j][i+1]=beta[j][i+1]-gamma*(sum-2*gam*beta[j][i+1]*new)
	for i in range(inputnodes):
		for j in range(hiddennodes):
			sum1=0
			for t in range(N):
				sum2=0
				for l in range(outputnodes):
					sum2-=(2-new)*(y[t][l]-fun[t][l])*sigmoidder(numpy.dot(beta[l][1:],Z[t]))*sigmoidder(numpy.dot(alpha[j][1:],x[t]))*beta[l][j+1]*x[t][i]
				sum1+=sum2
			alpha[j][i+1]-=gamma*(sum1-2*gam*alpha[j][i+1]*new)
	error=0
	for i in range(N):
		for j in range(outputnodes):
			error+=(y[i][j]-fun[i][j])**2
	print str(it)+" - "+str(error)
print "-----------Testing--------------"
acnt=0
l=[]
for it in range(len(Test)):
	z=[]
	for j in range(hiddennodes):
		z.append(sigmoid(alpha[j][0]+numpy.dot(alpha[j][1:],Test[it])))
	T=[]
	for k in range(outputnodes):
		T.append(beta[k][0]+numpy.dot(beta[k][1:],z))
	f=[]
	for k in range(outputnodes):
		f.append(g(T,k))
	max=0
	maxidx=0
	for idx in range(outputnodes):
		if(max < f[idx]):
			max=f[idx]
			maxidx=idx
	print f
	if(maxidx==Testoutp[it]):
		acnt+=1
	l.append(maxidx)
print acnt/(len(Test)*1.0)
print l
printperform(l)