#Problem2:
#Applying Linear regression on indicator variables for DS1

import numpy
from numpy.linalg import inv
import random
import sklearn.metrics

#reading the data set and storing it in Test and Train with 1 prepended for each point
#this is because we can calculate beta0 easily.
fp=open('DS1-train.csv','r')
fp2=open('DS1-test.csv','r')
data=fp.read()
data2=fp2.read()
fp.close()
fp2.close()
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
		Test[i].append(float(data2.split('\n')[i].split(',')[j]))

#Linear regression : (X^T*X)^-1*X^T*y
#X-Train data;y-Output for Train data-600*[0]+600*[1]
A=numpy.transpose(Train)
B=numpy.dot(A,Train)
C=numpy.dot(inv(B),A)
D=numpy.dot(C,600*[0]+600*[1])
print D #coefficients learnt
E=numpy.transpose(D)
F=numpy.dot(Test,D)
Out=[-1]*800

#converting the regression output to classsification output
for i in range(0,800):
	if F[i]<=0.5:
		Out[i]=0
	else:
		Out[i]=1

#For printing the performance results
print sklearn.metrics.accuracy_score(400*[0]+400*[1],Out)
print sklearn.metrics.precision_score(400*[0]+400*[1],Out)
print sklearn.metrics.recall_score(400*[0]+400*[1],Out)
print sklearn.metrics.f1_score(400*[0]+400*[1],Out)