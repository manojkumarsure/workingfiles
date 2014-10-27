import random
import math
import numpy
inputnodes=96
hiddennodes=6
outputnodes=4
gamma=0.01
iterations=200
def sigmoid(x):
	return 1.0/(1+math.exp(-x))
def sigmoidder(x):
	return math.exp(x)/(float((1.0+math.exp(x))**2))
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
				sum=sum-2*(y[t][j]-fun[t][j])*sigmoidder(numpy.dot(beta[j][1:],Z[t]))*Z[t][i]
			beta[j][i+1]=beta[j][i+1]-gamma*sum
	for i in range(inputnodes):
		for j in range(hiddennodes):
			sum1=0
			for t in range(N):
				sum2=0
				for l in range(outputnodes):
					sum2-=2*(y[t][l]-fun[t][l])*sigmoidder(numpy.dot(beta[l][1:],Z[t]))*sigmoidder(numpy.dot(alpha[j][1:],x[t]))*beta[l][j+1]*x[t][i]
				sum1+=sum2
			alpha[j][i+1]-=gamma*sum1
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