#Problem5:
#Filling the missing attributes from community dataset using mean of that attribute

import numpy
import random

#Reading the community dataset
fp=open('communities.data','r')
s=fp.read()
l=[]
b=[0]*128 # to keep track of mean for each feature
count=[0]*128 # to keep of how many valid data points are present for that attribute

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

#b[i] represents mean of ith attribute
for j in range(0,128):
	try:
		b[j]=b[j]/(count[j]*1.0)
	except:
		pass

#filling the missing attributes
#Data stores the dataset after all the missing attributes are filled
Data=[]
for i in range(len(l)):
	Data.append([])
	for j in range(len(l[i].split(','))):
		if(j>=5):#first five columns are not predictive, so we dont need them
			if l[i].split(',')[j]=='?':
				Data[i].append(round(float(b[j]),2))
			else:
				Data[i].append(round(float(l[i].split(',')[j]),2))
length=len(Data)

#for printing the corrected dataset into a csv file
fp=open('communities_corrected.csv','w')
for i in Data:
	for j in i:
		print >>fp,str(float(j))+',',
	print >>fp
fp.close()
loops=0

#Randomly selecting 20% and setting that as test data and remaining as training data
while loops<5:
	test=[]
	train=[]
	Test=[]
	Train=[]
	a=set()
	#selecting random indices
	while len(a)<=length/5.0:
		a.add(random.randint(0,length-1))
	#splitting into test and train based on above indices
	for j in a:
		test.append(Data[j])
	for j in set(range(0,length))-a:
		train.append(Data[j])
	for j in range(len(test)):
		Test.append([])
		for k in range(0,122):
			Test[j].append(test[j][k])
	for j in range(len(train)):
		Train.append([])
		for k in range(0,122):
			Train[j].append(train[j][k])
	
	#taking last column as the output for the given data
	#and storing them into outptest and train
	Outptest=[]
	Outptrain=[]
	for k in range(len(test)):
		Outptest.append(test[k][122])
	for k in range(len(train)):
		Outptrain.append(train[k][122])
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	
	#just to make sure that B is not singular from the training set
	if numpy.linalg.det(B)==0:
		continue
	
	#For storing the generated splits into csv files
	Str1="CandC-train"+str(loops+1)+".csv"
	Str2="CandC-test"+str(loops+1)+".csv"
	fp=open(Str1,"w")
	fp.close()
	fp=open(Str2,"w")
	fp.close()
	fp=open(Str1,"a")
	for i in range(len(train)):
		for j in range(123):
			print >>fp,str(train[i][j])+',',
		print >>fp
	fp.close()
	fp=open(Str2,"a")
	for i in range(len(Test)):
		for j in range(123):
			print >>fp,str(test[i][j])+',',
		print >>fp
	fp.close()
	loops+=1