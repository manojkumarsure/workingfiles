#Problem1:
#Creation of Data set consisting of 2 classes with guassian distributions
#The following code generates DS1  and seperates it into train(60%) and test(40%)
#and stores them in csv files
import numpy
import random

mean1=[0]*10 #mean for class0
mean2=[3]*10 #mean for class1
covariance=[] #covariance matrix shared by both classes

#generatign the covariance matrix randomly with the values between 0 and 3
for i in range(0,10):
	covariance.append([])
	for j in range(10):
		covariance[i].append(random.uniform(0.0,3.0))
		
#This is to ensure that the generated covariance matrix is not random
while(covariance[0][0]==covariance[1][1]):
	covariance=[]
	for i in range(0,10):
		covariance.append([])
		for j in range(10):
			covariance[i].append(random.uniform(0.0,3.0))

#generating 1000 examples each for both classes
l1=[[0]*10]*1000
l2=[[0]*10]*1000
for i in range(0,1000):
	l1[i]=numpy.random.multivariate_normal(mean1,covariance,1).T
	l2[i]=numpy.random.multivariate_normal(mean2,covariance,1).T

#testi represents test data from ith class similarly traindata represents train data from ith class
test1=[]
test2=[]
train1=[]
train2=[]

#selecting a random 400 numbers and they are taken as indices for test data sets
a=set()
while len(a)<400:
	a.add(random.randint(0,999))
count=0

#seperating the data into test and train for each class
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

#So,actual test data is the union of above two test sets and train data is 
#union of both train sets
Train=train1+train2
Test=test1+test2

#for storing the test and train data into csv files
fp=open("DS1-train.csv","w")
fp.close()
fp=open("DS1-test.csv","w")
fp.close()
fp=open("DS1-train.csv","a")
for i in range(len(Train)):
	for j in range(10):
		print >>fp,str(Train[i][j])+',',
	print >>fp
fp=open('DS1-test.csv','a')	
for i in range(len(Test)):
	for j in range(10):
		print >>fp,str(Test[i][j])+',',
	print >>fp
fp.close()