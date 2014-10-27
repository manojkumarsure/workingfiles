import random
import math
import numpy

#for printing performance results

#count of a's in l in range(x,y)
def lcount(l,a,x,y):
	c=0
	for i in range(x,y):
		if l[i]==a:
			c+=1
	return c

#prints per class precision,recall,f_measure scores 
def printperform(l):
	prec0=lcount(l,0,0,20)/(lcount(l,0,0,80)*1.0)
	prec1=lcount(l,1,20,40)/(lcount(l,1,0,80)*1.0)
	prec2=lcount(l,2,40,60)/(lcount(l,2,0,80)*1.0)
	prec3=lcount(l,3,60,80)/(lcount(l,3,0,80)*1.0)
	rec0=lcount(l,0,0,20)/20.0
	rec1=lcount(l,1,20,40)/20.0
	rec2=lcount(l,2,40,60)/20.0
	rec3=lcount(l,3,60,80)/20.0
	f0=2*prec0*rec0/((prec0+rec0)*1.0)
	f1=2*prec1*rec1/((prec1+rec1)*1.0)
	f2=2*prec2*rec2/((prec2+rec2)*1.0)
	f3=2*prec3*rec3/((prec3+rec3)*1.0)
	print prec0,prec1,prec2,prec3
	print rec0,rec1,rec2,rec3
	print f0,f1,f2,f3
	
#input,hidden and output nodes
inputnodes=96
hiddennodes=6
outputnodes=4

#step-width in gradient descent
gamma=0.01

#the value gamma given in new error function
gam=0.01

#no.of iterations
iterations=100

#new = 1 => new error function is applied
#new = 0 => original back propagation is applied
new=1

#sigmoid and its derivative
def sigmoid(x):
	return 1.0/(1+math.exp(-x))
def sigmoidder(x):
	return sigmoid(x)*(1-sigmoid(x))

#input to hidden and hidden to output weight matrices
alpha=[]
beta=[]

#Reading the Test and Train data sets. and store them in respective arrays
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
	
#No. of Data points
N=len(Data)

#Filling the weights with random values in range(-0.5,0.5)
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

#converting the output to 4 bits and storing it in y
for i in Dataoutp:
	if(i==0):
		y.append([1,0,0,0])
	elif(i==1):
		y.append([0,1,0,0])
	elif(i==2):
		y.append([0,0,1,0])
	elif(i==3):
		y.append([0,0,0,1])
		
#soft-max function
def g(T,k):
	sum=0
	for i in T:
		sum+=math.exp(i)
	return math.exp(T[k])/sum

#implementation of the algorithm
for it in range(iterations):
	fun=[]
	Z=[]
	
	#calculating the hidden and output vectors for all input vectors and storing them in Z and fun respectively
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
	
	#update rule for beta
	for i in range(hiddennodes):
		for j in range(outputnodes):
			sum=0
			for t in range(N):
				sum=sum-((2-new)*(y[t][j]-fun[t][j])*sigmoidder(numpy.dot(beta[j][1:],Z[t]))*Z[t][i])
			beta[j][i+1]=beta[j][i+1]-gamma*(sum-2*gam*beta[j][i+1]*new)
	
	#update rule for alpha
	for i in range(inputnodes):
		for j in range(hiddennodes):
			sum1=0
			for t in range(N):
				sum2=0
				for l in range(outputnodes):
					sum2-=(2-new)*(y[t][l]-fun[t][l])*sigmoidder(numpy.dot(beta[l][1:],Z[t]))*sigmoidder(numpy.dot(alpha[j][1:],x[t]))*beta[l][j+1]*x[t][i]
				sum1+=sum2
			alpha[j][i+1]-=gamma*(sum1-2*gam*alpha[j][i+1]*new)


#Testing with the given Test data
acnt=0 # to store how many points are correctly classified
l=[]
for it in range(len(Test)):
	#procedure similar to what we have done for the Training data to get output vector
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
	if(maxidx==Testoutp[it]):
		acnt+=1
	l.append(maxidx)

#printing accuracy and other performance results 
print acnt/(len(Test)*1.0)
print l
printperform(l)