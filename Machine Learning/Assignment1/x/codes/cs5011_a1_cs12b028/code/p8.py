#Problem8:
#Applying PCA on given dataset and reporting performance results

import numpy
from numpy.linalg import inv
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn import linear_model
import sklearn.metrics
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

#function to print the per class performance results
def prec():
	counta=0
	countb=0
	countc=0
	countd=0
	for i  in range(0,200):
		if outx[i]==0:
			counta+=1
		else:
			countc+=1
	for i in range(200,400):
		if outx[i]==1:
			countb+=1
		else:
			countd+=1
	prec0=counta/((counta+countd)*1.0) #precision scores for each class
	prec1=countb/((countb+countc)*1.0)
	rec0=counta/200.0  #recall scores for each class
	rec1=countb/200.0
	f0=(2*prec0*rec0)/(prec0+rec0) #f-measures for each class
	f1=(2*prec1*rec1)/(prec1+rec1)
	print prec0
	print prec1
	print rec0
	print rec1
	print f0
	print f1

#Reading the data set  and storing them
fp=open('DS3/train.csv','r')
s=fp.read()
fp.close()
fp=open('DS3/test.csv','r')
s2=fp.read()
fp.close()
Data=[] #tarining data
Test=[] #test data

for i in range(len(s.split('\n'))):
	Data.append([])
	for j in s.split('\n')[i].split(','):
		try:
			Data[i].append(float(j))
		except:
			pass
for i in range(len(s2.split('\n'))):
	Test.append([])
	for j in s2.split('\n')[i].split(','):
		try:
			Test[i].append(float(j))
		except:
			pass

pca=PCA(n_components=1) #extracting one feature

x=pca.fit_transform(numpy.array(Data[0:len(Data)-1])) #projected train data in the required feature space
y=pca.transform(numpy.array(Test[0:len(Test)-1])) #projected test data in the required feature space

#Applying linear regression on indicator variable for projected data sets
A=numpy.transpose(x)
B=numpy.dot(A,x)
C=numpy.dot(inv(B),A)
D=numpy.dot(C,1000*[-1]+1000*[1])
E=numpy.transpose(D)
F=numpy.dot(y,D)
outx=[]
for i in F:
	if i>=0:
		outx.append(1)
	else:
		outx.append(0)
outp=[]

#for plotting the data set in 3d
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X=[]
Y=[]
Z=[]
for i in range(len(Data)):
	try:
		X.append(Data[i][0])
		Y.append(Data[i][1])
		Z.append(Data[i][2])
	except:
		pass
ax.scatter(X,Y,Z)
#plt.show()

#for plotting the projected data along wiht classifier boundary
#actually classifier is a single point as everything is in 1d
#but for representation purpose,i used a line that passes through that point
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X=[]
Y=[]
for i in range(len(x)):
	try:
		X.append(x[i][0])
		Y.append(0)
	except:
		pass
ax.scatter(X,Y)
liney=[]
for i in X:
	liney.append(D[0])
ax.plot(liney,X)
#plt.show()
print sklearn.metrics.accuracy_score(200*[0]+200*[1],outx)
prec()
