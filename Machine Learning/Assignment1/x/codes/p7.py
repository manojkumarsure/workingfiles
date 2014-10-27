import numpy
from numpy.linalg import inv
import random
import sklearn.metrics
c1=0
for loops in range(5):
	test=[]
	train=[]
	Test=[]
	Train=[]
	Str1="CandCTrain"+str(loops+1)+".csv"
	Str2="CandCTest"+str(loops+1)+".csv"
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
	for j in range(len(test)-1):
		Test.append([])
		for k in range(0,122):
			Test[j].append(float(test[j][k]))
	for j in range(len(train)-1):
		Train.append([])
		for k in range(0,122):
			Train[j].append(float(train[j][k]))
	Outptest=[]
	Outptrain=[]
	for k in range(len(test)-1):
		Outptest.append(float(test[k][122]))
	for k in range(len(train)-1):
		Outptrain.append(float(train[k][122]))
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	G=numpy.add(B,2*numpy.identity(122))
	C=numpy.dot(inv(G),A)
	D=numpy.dot(C,Outptrain)
	print D
	E=numpy.transpose(D)
	F=numpy.dot(Test,D)
	c1+=numpy.mean((F-Outptest)**2)
print c1/5.0