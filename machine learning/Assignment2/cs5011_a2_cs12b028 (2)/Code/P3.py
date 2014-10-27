#Problem - 3:
from sklearn import linear_model
from sklearn.metrics import accuracy_score
import os

#printing the perclass precision,recall and f_measure
def prec():
	counta=0
	countb=0
	countc=0
	countd=0
	for i  in range(0,20):
		if New[i]==1:
			counta+=1
		else:
			countc+=1
	for i in range(20,40):
		if New[i]==-1:
			countb+=1
		else:
			countd+=1
	prec0=counta/((counta+countd)*1.0)
	prec1=countb/((countb+countc)*1.0)
	rec0=counta/20.0
	rec1=countb/20.0
	f0=(2*prec0*rec0)/(prec0+rec0)
	f1=(2*prec1*rec1)/(prec1+rec1)
	print prec0
	print prec1
	print rec0
	print rec1
	print f0
	print f1
	
#reading the data 
fp=open('DS2-train.csv','r')
s=fp.read()
fp.close()
Data=[]
Test=[]
count=0
for i in s.split('\n')[:-1]:
	Data.append([])
	for j in i.split(','):
		Data[count].append(float(j))
	count+=1
fp=open('DS2-test.csv','r')
s=fp.read()
fp.close()
count=0
for i in s.split('\n')[:-1]:
	Test.append([])
	for j in i.split(','):
		Test[count].append(float(j))
	count+=1
	
#TrainData - training data
#TestData - testing data
TrainData=[]
TestData=[]
count1=0
count2=0
for i in Data:
	if i[-1]==1.0 :
		count1+=1
		TrainData.append(i[:-1])
	if i[-1]==3.0:
		count2+=1
		TrainData.append(i[:-1])
for i in Test:
	if i[-1]==1.0 :
		TestData.append(i[:-1])
	if i[-1]==3.0:
		TestData.append(i[:-1])

#applying l2 LogisticRegression
log_reg=linear_model.LogisticRegression(penalty='l2')
log_reg.fit(TrainData,count1*[1]+count2*[-1])
New=log_reg.predict(TestData)
print New

#printing the accuracy_score and other performance measures for l2 LogisticRegression
print accuracy_score(20*[1]+20*[-1],New)
prec()

#writing into files which will be used by the boyd's code
fp=open('featurefile','w')
print >>fp,"%%MatrixMarket matrix array real general"
print >>fp,str(len(TrainData))+" "+str(len(TrainData[0]))
for i in range(len(TrainData[0])):
	for j in range(len(TrainData)):
		print >>fp,round(TrainData[j][i],4)
fp.close()
fp=open('classfile','w')
print >>fp,"%%MatrixMarket matrix array real general"
print >>fp,str(count1+count2)+" 1"
for i in range(count1):
	print >>fp,1
for i in range(count2):
	print >>fp,-1
fp.close()
fp=open('testfile','w')
print >>fp,"%%MatrixMarket matrix array real general"
print >>fp,str(len(TestData))+" "+str(len(TestData[0]))
for i in range(len(TestData[0])):
	for j in range(len(TestData)):
		print >>fp,round(TestData[j][i],4)
fp.close()
fp=open('test_b','w')
print >>fp,"%%MatrixMarket matrix array real general"
print >>fp,"40 1"
for i in range(20):
	print >>fp,1
for j in range(20):
	print >>fp,-1
fp.close()

#calling the boyd's code with parameter lambda = 0.01 for which the
#accuracy_score is observed to be maximum.
os.system("l1_logreg_train -s featurefile classfile 0.01 model")
os.system("l1_logreg_classify -t test_b model testfile result")