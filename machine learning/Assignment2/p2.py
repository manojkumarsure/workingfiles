import random
import math
import numpy
inputnodes=3
hiddennodes=3
outputnodes=3
iterations=1
gamma=0.01
def sigmoid(x):
	return math.tanh(x)
def sigmoidder(x):
	return math.exp(x)/(1+math.exp(x))**2
fp=open('DS1-train.csv','r')
s=fp.read()
fp.close()
Data=[]
Dataoutp=[]
Test=[]
Testoutp=[]
count=0
Data=[[1,1,0],[1,0,1],[1,1,1],[1,0,0]]
Dataoutp=[1,1,0,0]
Test=Data
Testoutp=Dataoutp
#for i in s.split('\n')[:-1]:
	#Data.append([])
	#Data[count].append(1)
	#for j in i.split(',')[:-1]:
		#Data[count].append(float(j))
	#Dataoutp.append(float(i.split(',')[-1]))
	#count+=1
#fp=open('DS1-test.csv','r')
#s=fp.read()
#fp.close()
#count=0
#for i in s.split('\n')[:-1]:
	#Test.append([])
	#Test[count].append(1)
	#for j in i.split(',')[:-1]:
		#Test[count].append(float(j))
	#Testoutp.append(float(i.split(',')[-1]))
	#count+=1
inplist=[1.0]*inputnodes
hidlist=[1.0]*hiddennodes
outlist=[1.0]*outputnodes
weightinp=[]
for i in range(inputnodes):
	weightinp.append([])
	for j in range(hiddennodes):
		weightinp[i].append(random.uniform(-0.5,0.5))
weightout=[]
for i in range(hiddennodes):
	weightout.append([])
	for j in range(outputnodes):
		weightout[i].append(random.uniform(-0.5,0.5))
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
				s1[m][k]+=Dataoutp[k]-probs[k]
		for l in range(inputnodes):
			for m in range(hiddennodes):
				sum=0
				for k in range(outputnodes):
					sum+=weightout[m][k]*(Dataoutp[k]-probs[k])
				s2[l][m]+=(sigmoidder(numpy.dot(numpy.transpose(weightinp)[i],Data[idx]))*sum)
	for m in range(hiddennodes):
		for k in range(outputnodes):
			weightout[m][k]+=gamma*s1[m][k]
	for l in range(inputnodes):
		for m in range(hiddennodes):
			weightinp[l][m]+=gamma*s2[l][m]
acnt=0
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
print acnt/(len(Test)*1.0)