import numpy
import random
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
		if(j>=5):
			if l[i].split(',')[j]=='?':
				Data[i].append(round(float(b[j]),2))
			else:
				Data[i].append(round(float(l[i].split(',')[j]),2))
length=len(Data)
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
		for k in range(0,122):
			Test[j].append(test[j][k])
	for j in range(len(train)):
		Train.append([])
		for k in range(0,122):
			Train[j].append(train[j][k])
	Outptest=[]
	Outptrain=[]
	for k in range(len(test)):
		Outptest.append(test[k][122])
	for k in range(len(train)):
		Outptrain.append(train[k][122])
	A=numpy.transpose(Train)
	B=numpy.dot(A,Train)
	if numpy.linalg.det(B)==0:
		continue
	Str1="CandCTrain"+str(loops+1)+".csv"
	Str2="CandCTest"+str(loops+1)+".csv"
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