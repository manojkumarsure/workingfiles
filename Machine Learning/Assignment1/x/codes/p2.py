import numpy
from numpy.linalg import inv
import random
import sklearn.metrics
fp=open('DS1.csv','r')
data=fp.read()
fp.close()
Train=[]
Test=[]
for i in range(0,1200):
	Train.append([])
	Train[i].append(1)
	for j in range(0,10):
		Train[i].append(float(data.split('\n')[i].split(',')[j]))
for i in range(0,800):
	Test.append([])
	Test[i].append(1)
	for j in range(10):
		Test[i].append(float(data.split('\n')[i+1200].split(',')[j]))
A=numpy.transpose(Train)
B=numpy.dot(A,Train)
C=numpy.dot(inv(B),A)
D=numpy.dot(C,600*[0]+600*[1])
print D
E=numpy.transpose(D)
F=numpy.dot(Test,D)
Out=[-1]*800
for i in range(0,800):
	if F[i]<=0.5:
		Out[i]=0
	else:
		Out[i]=1
print sklearn.metrics.accuracy_score(400*[0]+400*[1],Out)
print sklearn.metrics.precision_score(400*[0]+400*[1],Out)
print sklearn.metrics.recall_score(400*[0]+400*[1],Out)
print sklearn.metrics.f1_score(400*[0]+400*[1],Out)