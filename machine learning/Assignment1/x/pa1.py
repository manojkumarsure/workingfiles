import numpy
from numpy.linalg import inv
import matplotlib.pyplot as plt
import random
import sklearn.metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
def knn(nb):
	neigh = KNeighborsClassifier(n_neighbors=nb)
	neigh.fit(Train,600*[0]+600*[1])
	Result=neigh.predict(Test)
	print sklearn.metrics.accuracy_score(400*[0]+400*[1],Result,normalize=True, sample_weight=None)
def linear():
	clf=linear_model.LinearRegression()
	clf.fit(Train,600*[0]+600*[1])
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	C=numpy.dot(inv(B),A)
	D=numpy.dot(C,600*[0]+600*[1])
	print D
	E=numpy.transpose(D)
	F=numpy.dot(Test,D)
	Result=clf.predict(Test)
	count=0
	for i in range(0,400):
		if Result[i]<=0.5:
			count+=1
	for i in range(400,800):
		if Result[i]>0.5:
			count+=1
	print count/800.0
	count=0
	for i in range(0,400):
		if F[i]<=0.5:
			count+=1
	for i in range(400,800):
		if F[i]>0.5:
			count+=1
	print count/800.0
mean1=[0]*10
mean2=[3]*10
covariance=[]
covariance2=[]
covariance3=[]
list=[0]*100
for i in range(0,10):
	covariance.append([])
	covariance2.append([])
	covariance3.append([])
	for j in range(10):
		covariance[i].append(random.uniform(0.0,3.0))
		covariance2[i].append(random.uniform(0.0,3.0))
		covariance3[i].append(random.uniform(0.0,3.0))
l1=[[0]*10]*1000
l2=[[0]*10]*1000
for i in range(0,1000):
	k=random.choice(list)
	if k==0:
		l1[i]=numpy.random.multivariate_normal(mean1,covariance,1).T
		l2[i]=numpy.random.multivariate_normal(mean2,covariance,1).T
	if k==1:
		l1[i]=numpy.random.multivariate_normal(mean1,covariance2,1).T
		l2[i]=numpy.random.multivariate_normal(mean2,covariance2,1).T
	if k==2:
		l1[i]=numpy.random.multivariate_normal(mean1,covariance3,1).T
		l2[i]=numpy.random.multivariate_normal(mean2,covariance3,1).T
test1=[]
test2=[]
train1=[]
train2=[]
for i in range(0,600):
	train1.append([])
	train2.append([])
	train1[i].append(1)
	train2[i].append(1)
	for j in range(0,10):
		train1[i].append(l1[i+400][j][0])
		train2[i].append(l2[i+400][j][0])
for i in range(0,400):
	test1.append([])
	test2.append([])
	test1[i].append(1)
	test2[i].append(1)
	for j in range(10):
		test1[i].append(l1[i][j][0])
		test2[i].append(l2[i][j][0])
Train=train1+train2
Test=test1+test2
linear()
knn(10)