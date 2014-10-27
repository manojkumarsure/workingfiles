#Problem 2:

import random
import math
import numpy

def prec():
	counta=0
	countb=0
	countc=0
	countd=0
	for i  in range(0,20):
		if New[i]==0:
			counta+=1
		else:
			countc+=1
	for i in range(20,40):
		if New[i]==1:
			countb+=1
		else:
			countd+=1
	prec0=counta/((counta+countd)*1.0)
	prec1=countb/((countb+countc)*1.0)
	rec0=counta/20.0
	rec1=countb/20.0
	f0=(2*prec0*rec0)/(prec0+rec0)
	f1=(2*prec1*rec1)/(prec1+rec1)
	print prec0
	print prec1
	print rec0
	print rec1
	print f0
	print f1
	
	
inputnodes=97 #96+1
hiddennodes=5
outputnodes=5 #4+1
iterations=100
gamma=0.01

#to determine whether it is a new error function or old error function
new=0

#sigmoid and derivative od sigmoid
def sigmoid(x):
	return math.tanh(x)
def sigmoidder(x):
	return math.exp(x)/(1+math.exp(x))**2

#reading the data from the files.
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
	Data[count].append(1)
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
	Test[count].append(1)
	for j in i.split(',')[:-1]:
		Test[count].append(float(j))
	Testoutp.append(float(i.split(',')[-1]))
	count+=1
inplist=[1.0]*inputnodes
hidlist=[1.0]*hiddennodes
outlist=[1.0]*outputnodes

#input weights
weightinp=[]
for i in range(inputnodes):
	weightinp.append([])
	for j in range(hiddennodes):
		weightinp[i].append(random.uniform(-0.5,0.5))

#ouptut weights
weightout=[]
for i in range(hiddennodes):
	weightout.append([])
	for j in range(outputnodes):
		weightout[i].append(random.uniform(-0.5,0.5))
		
#applying the back propagation algorithm for 'iterations' times
for it in range(iterations):
	error=0
	s1=[[0]*outputnodes]*hiddennodes
	s2=[[0]*hiddennodes]*inputnodes
	for idx in range(len(Data)):
		Z=[]
		for i in range(hiddennodes):
			Z.append(sigmoid(numpy.dot(numpy.transpose(weightinp)[i],Data[idx])))
		T=[]
		for i in range(outputnodes):
			T.append(numpy.dot(numpy.transpose(weightout)[i],Z))
		probs=[0]
		sum=0
		for i in range(1,outputnodes):
			sum+=(math.exp(T[i]))
		for i in range(1,outputnodes):
			probs.append(math.exp(T[i])/sum)
		errsum=0
		for i in range(1,outputnodes):
			if(i-1==Dataoutp[idx]):
				errsum+=(1-probs[i])**2
			else:
				errsum+=(probs[i])**2
		error+=errsum
		for m in range(hiddennodes):
			for k in range(outputnodes):
				s1[m][k]+=Dataoutp[k]-probs[k]+2*gamma*weightout[m][k]*new
		for l in range(inputnodes):
			for m in range(hiddennodes):
				sum=0
				for k in range(outputnodes):
					sum+=weightout[m][k]*(Dataoutp[k]-probs[k])
				s2[l][m]+=(sigmoidder(numpy.dot(numpy.transpose(weightinp)[i],Data[idx]))*sum)
				s2[l][m]+=2*gamma*weightinp[l][m]*new
	for m in range(hiddennodes):
		for k in range(outputnodes):
			weightout[m][k]-=gamma*s1[m][k]
	for l in range(inputnodes):
		for m in range(hiddennodes):
			weightinp[l][m]-=gamma*s2[l][m]
	print error
acnt=0

#testing the neural network with test data
for it in range(len(Test)):
	Z=[]
	for i in range(hiddennodes):
		Z.append(sigmoid(numpy.dot(numpy.transpose(weightinp)[i],Test[idx])))
	T=[]
	for i in range(outputnodes):
		T.append(numpy.dot(numpy.transpose(weightout)[i],Z))
	probs=[0]
	sum=0
	for i in range(1,outputnodes):
		sum+=(math.exp(T[i]))
	for i in range(1,outputnodes):
		probs.append(math.exp(T[i])/sum)
	max=0
	maxidx=0
	for idx in range(1,outputnodes):
		if(max < probs[idx]):
			max=probs[idx]
			maxidx=idx-1
	if(maxidx==Testoutp[it]):
		acnt+=1
#printinf the accuracy score
print acnt/(len(Test)*1.0)