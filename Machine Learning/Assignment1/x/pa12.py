import numpy
from numpy.linalg import inv
import matplotlib.pyplot as plt
import random
import sklearn.metrics
from sklearn import linear_model
from sklearn.linear_model import Ridge
fp=open('communities.data','r')
s=fp.read()
l=[]
b=[0]*128
count=[0]*128
for i in s.split('\n'):
	l.append(i)
for i in range(len(l)):
	for j in range(len(l[i].split(','))):
		if l[i].split(',')[j]!='?':
			try:
				b[j]+=float(l[i].split(',')[j])
				count[j]+=1
			except:
				pass
for j in range(0,128):
	try:
		b[j]=b[j]/(count[j]*1.0)
	except:
		pass
Data=[]
for i in range(len(l)):
	Data.append([])
	for j in range(len(l[i].split(','))):
		if(j!=3):
			if l[i].split(',')[j]=='?':
				Data[i].append(round(float(b[j]),2))
			else:
				Data[i].append(round(float(l[i].split(',')[j]),2))
length=len(Data)
c1=0
c2=0
c3=0
c4=0
loops=0
while loops<5:
	test=[]
	train=[]
	Test=[]
	Train=[]
	a=set()
	while len(a)<=length/5.0:
		a.add(random.randint(0,length-1))
	for j in a:
		test.append(Data[j])
	for j in set(range(0,length))-a:
		train.append(Data[j])
	for j in range(len(test)):
		Test.append([])
		for k in range(0,126):
			Test[j].append(test[j][k])
	for j in range(len(train)):
		Train.append([])
		for k in range(0,126):
			Train[j].append(train[j][k])
	Outptest=[]
	Outptrain=[]
	for k in range(len(test)):
		Outptest.append(test[k][126])
	for k in range(len(train)):
		Outptrain.append(train[k][126])
	regr=linear_model.LinearRegression()
	regr.fit(Train,Outptrain)
	c1+=numpy.mean((regr.predict(Test)-Outptest)**2)
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	if numpy.linalg.det(B)==0:
		continue
	C=numpy.dot(inv(B),A)
	D=numpy.dot(C,Outptrain)
	E=numpy.transpose(D)
	F=numpy.dot(Test,D)
	c4+=numpy.mean((F-Outptest)**2)
	Rid=Ridge(alpha=2)
	Rid.fit(Train,Outptrain)
	c2+=numpy.mean((Rid.predict(Test)-Outptest)**2)
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	G=numpy.add(B,2*numpy.identity(126))
	C=numpy.dot(inv(G),A)
	D=numpy.dot(C,Outptrain)
	E=numpy.transpose(D)
	F=numpy.dot(Test,D)
	c3+=numpy.mean((F-Outptest)**2)
	loops+=1
print c1/5.0
print c4/5.0
print c2/5.0
print c3/5.0