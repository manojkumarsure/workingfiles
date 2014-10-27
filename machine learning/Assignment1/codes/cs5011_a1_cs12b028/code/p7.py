#Problem7:
#Applying Ridge Regression for Communities data set

import numpy
from numpy.linalg import inv
import random
import sklearn.metrics
c1=0
c2=0

#For printing the coefficients learnt into a text file
fpb=open('beta7.txt','w')
for loops in range(5):
	test=[]
	train=[]
	Test=[]
	Train=[]
	#Reading the data sets and storing them into different lists
	Str1="CandC-train"+str(loops+1)+".csv"
	Str2="CandC-test"+str(loops+1)+".csv"
	fp=open(Str1,"r")
	s=fp.read()
	fp.close()
	for i in range(len(s.split('\n'))):
		l1=s.split('\n')[i]
		train.append([])
		train[i].append(1)
		for j in range(len(l1.split(','))-1):
			k1=l1.split(',')[j]
			train[i].append(k1)
	fp=open(Str2,"r")
	s=fp.read()
	fp.close()
	for i in range(len(s.split('\n'))):
		l2=s.split('\n')[i]
		test.append([])
		test[i].append(1)
		for j in range(len(l2.split(','))-1):
			k2=l2.split(',')[j]
			test[i].append(k2)
	
	#seperating train and test inputs and outputs
	for j in range(len(test)-1):
		Test.append([])
		for k in range(0,123):
			Test[j].append(float(test[j][k]))
	for j in range(len(train)-1):
		Train.append([])
		for k in range(0,123):
			Train[j].append(float(train[j][k]))
	Outptest=[]
	Outptrain=[]
	for k in range(len(test)-1):
		Outptest.append(float(test[k][123]))
	for k in range(len(train)-1):
		Outptrain.append(float(train[k][123]))
	
	#Applying Ridge Regression with lambda = 2 (observed to have minimum after taking several values of lambda)
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	G=numpy.add(B,2*numpy.identity(123))
	C=numpy.dot(inv(G),A)
	D=numpy.dot(C,Outptrain)
	print >>fpb,D #printing the beta values
	E=numpy.transpose(D)
	F=numpy.dot(Test,D)
	print numpy.mean((F-Outptest)**2) #MSE
	print numpy.mean((F-Outptest)**2)*len(Outptest) #RSS
	c1+=numpy.mean((F-Outptest)**2)
	c2+=numpy.mean((F-Outptest)**2)*len(Outptest)
print c1/5.0 #average mse
print c2/5.0 #average rss