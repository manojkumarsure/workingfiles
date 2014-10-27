#Problem-1:

import Image,os,math
from sklearn.lda import LDA
from sklearn.decomposition import PCA
import sklearn.metrics
import numpy
from sklearn import preprocessing
from numpy.linalg import inv
from sklearn import svm
from sklearn import cross_validation
from sklearn.cross_validation import LeaveOneOut
import pickle

#Given a list a it will reduce its size by 8 times
#by taking the 8 consecutive elements and replacing them with their mean
def reducelist(a):
	l=[]
	for i in range(len(a)/8):
		count=0
		for j in range(8):
			count+=a[8*i+j]
		l.append(count/8.0)
	nsum=0
	for i in range(len(l)):
		nsum+=l[i]**2
	for i in range(len(l)):
		l[i]=l[i]/math.sqrt(nsum)
	return l

#function used for cross_validation the values k represents 
#k-fold cross_validation with certain parameters
#if k= length of input it will be n-fold cross validation
def crossvalid(kerntype,k,deg=3,coef=0,gam=0,c_val=1.0):
	curridx=0
	sum=0
	for fold in range(k):
		TrainData=x[0:curridx]+x[curridx+len(x)/k:len(x)]
		TrainOutp=y[0:curridx]+y[curridx+len(x)/k:len(x)]
		TestData=x[curridx:curridx+len(x)/k]
		TestOutp=y[curridx:curridx+len(x)/k]
		curridx=curridx+len(x)/k
		clf=svm.SVC(kernel=kerntype,gamma=gam,coef0=coef,degree=deg,C=c_val)
		clf.fit(TrainData,TrainOutp)
		outx=clf.predict(TestData)
		acc=sklearn.metrics.accuracy_score(TestOutp,outx)
		sum+=acc
		del clf
	return sum/k

#paths for various kinds of images
path1='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/coast/Train/'
path2='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/forest/Train/'
path3='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/coast/Test/'
path4='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/forest/Test/'
path5='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/insidecity/Train/'
path6='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/mountain/Train/'
path7='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/insidecity/Test/'
path8='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/mountain/Test/'


#data - train data
#test - test data
Data=[]
Test=[]

#variables to store number of images of each type
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0

#loading the histograms
for filename in os.listdir(path1):
	img = Image.open(path1+filename)
	Data.append(img.histogram())
	count1+=1
for filename in os.listdir(path2):
	img = Image.open(path2+filename)
	Data.append(img.histogram())
	count2+=1
for filename in os.listdir(path5):
	img = Image.open(path5+filename)
	Data.append(img.histogram())
	count5+=1
for filename in os.listdir(path6):
	img = Image.open(path6+filename)
	Data.append(img.histogram())
	count6+=1
for filename in os.listdir(path3):
	img = Image.open(path3+filename)
	Test.append(img.histogram())
	count3+=1
for filename in os.listdir(path4):
	img = Image.open(path4+filename)
	Test.append(img.histogram())
	count4+=1
for filename in os.listdir(path7):
	img = Image.open(path7+filename)
	Test.append(img.histogram())
	count7+=1
for filename in os.listdir(path8):
	img = Image.open(path8+filename)
	Test.append(img.histogram())
	count8+=1

# x and y are rebinned train and test data
x=[]
y=[]
for i in range(len(Data)):
	x.append(reducelist(Data[i]))
for i in range(len(Test)):
	y.append(reducelist(Test[i]))
	
#writing the histogram data into files
fp=open('DS2-train.csv','w')
for i in range(count1):
	for j in x[i]:
		print >>fp,str(j)+',',
	print >>fp,0
for i in range(count2):
	for j in x[count1+i]:
		print >>fp,str(j)+',',
	print >>fp,1
for i in range(count5):
	for j in x[count1+count2+i]:
		print >>fp,str(j)+',',
	print >>fp,2
for i in range(count6):
	for j in x[count1+count2+count5+i]:
		print >>fp,str(j)+',',
	print >>fp,3
fp.close()
fp=open('DS2-test.csv','w')
for i in range(count3):
	for j in y[i]:
		print >>fp,str(j)+',',
	print >>fp,0
for i in range(count4):
	for j in y[count3+i]:
		print >>fp,str(j)+',',
	print >>fp,1
for i in range(count7):
	for j in y[count3+count4+i]:
		print >>fp,str(j)+',',
	print >>fp,2
for i in range(count8):
	for j in y[count3+count4+count7+i]:
		print >>fp,str(j)+',',
	print >>fp,3
fp.close()
Testy=y
y=count1*[0]+count2*[1]+count5*[2]+count6*[3]


#all the parameters are chosen based on the maximum average accuracy obtained
#on performing N-fold cross validation with those parameters

#printing the best parameters for polynomial kernel
max=0
maxi=0
maxj=0
for i in range(10):
	for j in range(10):
		l=crossvalid('poly',len(y),deg=i,gam=j) 
		if(l>max):
			max=l
			maxi=i
			maxj=j
print "poly-",max,maxi,maxj
polydeg=maxi
polygam=maxj

#printing the best parameters for guassian kernel
max=0
maxi=0
maxj=0
for i in range(10):
	for j in range(1,10):
		l=crossvalid('rbf',len(y),gam=i,c_val=j)
		if(l>max):
			max=l
			maxi=i
			maxj=j
print "rbf-",max,maxi,maxj
rbfgam=maxi
rbfc=maxj

##printing the best parameters for sigmoid kernel
max=0
maxi=0
maxj=0
for i in range(10):
	for j in range(10):
		l=crossvalid('sigmoid',len(y),gam=i,coef=j)
		if(l>max):
			max=l
			maxi=i
			maxj=j
print "sigmoid-",max,maxi,maxj
sigmgam=maxi
sigmcoef=maxj

#accuracy for linear kernel as there are no other parameters
l=crossvalid('linear',len(y))
print "linear-",l

#dumping the model into strings and printing that string to a file
model1=svm.SVC(kernel='linear')
model2=svm.SVC(kernel='poly',degree=2,gamma=2)
model3=svm.SVC(kernel='rbf',C=4,gamma=2)
model4=svm.SVC(kernel='sigmoid',gamma=1,coef0=0)
s1=pickle.dumps(model1)
s2=pickle.dumps(model2)
s3=pickle.dumps(model3)
s4=pickle.dumps(model4)
s=s1+'\n'+s2+'\n'+s3+'\n'+s4
fp=open('CS12B028.mat','w')
print >>fp,s
fp.close()