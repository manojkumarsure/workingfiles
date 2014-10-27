#Problem 9:
#Applying LDA on the given data set and printing performance results

import numpy
from numpy.linalg import inv
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn import linear_model
import sklearn.metrics
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

#function to print the performance results
def prec():
	counta=0
	countb=0
	countc=0
	countd=0
	for i  in range(0,200):
		if New[i]==0:
			counta+=1
		else:
			countc+=1
	for i in range(200,400):
		if New[i]==1:
			countb+=1
		else:
			countd+=1
	prec0=counta/((counta+countd)*1.0)
	prec1=countb/((countb+countc)*1.0)
	rec0=counta/200.0
	rec1=countb/200.0
	f0=(2*prec0*rec0)/(prec0+rec0)
	f1=(2*prec1*rec1)/(prec1+rec1)
	print prec0
	print prec1
	print rec0
	print rec1
	print f0
	print f1

#reading the data files and storing them into various lists
fp=open('DS3/train.csv','r')
s=fp.read()
fp.close()
fp=open('DS3/test.csv','r')
s2=fp.read()
fp.close()
Data=[]
Test=[]
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

#Applying LDA on the given data set
clf=LDA(n_components=1)
z=clf.fit_transform(numpy.array(Data[0:len(Data)-1]),1000*[0]+1000*[1])
New=clf.predict(Test[0:len(Test)-1])

#for plotting the projected data set
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X=[]
Y=[]
for i in z:
	try:
		X.append(i)
		Y.append(0)
	except:
		pass
ax.scatter(X,Y)

#red point is the classifier point whose coordinates are clf.coef_[0],0
ax.scatter(clf.coef_[0],0,color='red')
#plt.show()
print sklearn.metrics.accuracy_score(200*[0]+200*[1],New)
prec()