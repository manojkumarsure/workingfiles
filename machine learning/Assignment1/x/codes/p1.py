import numpy
import random
mean1=[0]*10
mean2=[3]*10
covariance=[]
for i in range(0,10):
	covariance.append([])
	for j in range(10):
		covariance[i].append(random.uniform(0.0,3.0))
while(covariance[0][0]==covariance[1][1]):
	covariance=[]
	for i in range(0,10):
		covariance.append([])
		for j in range(10):
			covariance[i].append(random.uniform(0.0,3.0))
l1=[[0]*10]*1000
l2=[[0]*10]*1000
for i in range(0,1000):
	l1[i]=numpy.random.multivariate_normal(mean1,covariance,1).T
	l2[i]=numpy.random.multivariate_normal(mean2,covariance,1).T
test1=[]
test2=[]
train1=[]
train2=[]
a=set()
while len(a)<400:
	a.add(random.randint(0,999))
count=0
for i in set(range(0,1000))-a:
	train1.append([])
	train2.append([])
	for j in range(0,10):
		train1[count].append(l1[i][j][0])
		train2[count].append(l2[i][j][0])
	count+=1
count=0
for i in a:
	test1.append([])
	test2.append([])
	for j in range(10):
		test1[count].append(l1[i][j][0])
		test2[count].append(l2[i][j][0])
	count+=1
Train=train1+train2
Test=test1+test2
fp=open("DS1.csv","w")
fp.close()
fp=open("DS1.csv","a")
for i in range(len(Train)):
	for j in range(10):
		print >>fp,str(Train[i][j])+',',
	print >>fp
for i in range(len(Test)):
	for j in range(10):
		print >>fp,str(Test[i][j])+',',
	print >>fp
fp.close()