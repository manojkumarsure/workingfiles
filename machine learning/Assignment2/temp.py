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
def crossvalid(kerntype,k,deg=3,coef=0,gam=0,c_val=1.0):
	curridx=0
	errmat=[[0]*10]*10
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
path1='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/coast/Train/'
path2='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/forest/Train/'
path3='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/coast/Test/'
path4='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/forest/Test/'
path5='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/insidecity/Train/'
path6='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/mountain/Train/'
path7='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/insidecity/Test/'
path8='/home/manoj/Desktop/working files/Machine 
Learning/Assignment2/For_the_students/data_students/mountain/Test/'

Data=[]
Test=[]
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
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
x=[]
y=[]
for i in range(len(Data)):
	x.append(reducelist(Data[i]))
for i in range(len(Test)):
	y.append(reducelist(Test[i]))
#fp=open('DS1-train.csv','w')
#for i in range(count1):
	#for j in x[i]:
		#print >>fp,str(j)+',',
	#print >>fp,0
#for i in range(count2):
	#for j in x[count1+i]:
		#print >>fp,str(j)+',',
	#print >>fp,1
#for i in range(count5):
	#for j in x[count1+count2+i]:
		#print >>fp,str(j)+',',
	#print >>fp,2
#for i in range(count6):
	#for j in x[count1+count2+count5+i]:
		#print >>fp,str(j)+',',
	#print >>fp,3
#fp.close()
#fp=open('DS1-test.csv','w')
#for i in range(count3):
	#for j in y[i]:
		#print >>fp,str(j)+',',
	#print >>fp,0
#for i in range(count4):
	#for j in y[count3+i]:
		#print >>fp,str(j)+',',
	#print >>fp,1
#for i in range(count7):
	#for j in y[count3+count4+i]:
		#print >>fp,str(j)+',',
	#print >>fp,2
#for i in range(count8):
	#for j in y[count3+count4+count7+i]:
		#print >>fp,str(j)+',',
	#print >>fp,3
#fp.close()
#z=count1*[0]+count2*[1]+count5*[2]+count6*[3]
#clf=svm.SVC(kernel='sigmoid',gamma=0.1,coef0=0)
#clf.fit(x,z)
#outx=clf.predict(y)
#print sklearn.metrics.accuracy_score(count3*[0]+count4*[1]+count7*[2]+count8*[3],outx)

y=count1*[0]+count2*[1]+count5*[2]+count6*[3]
max=0
maxi=0
maxj=0
for i in range(10):
	for j in range(10):
		#print i,j
		#clf=svm.SVC(kernel='poly',degree=2,gamma=2)
		#loo = LeaveOneOut(len(y))
		#scores=cross_validation.cross_val_score(clf,numpy.array(x),numpy.array(y),cv=loo)
		#l=scores.mean()
		l=crossvalid('poly',len(y),deg=i,gam=j)
		if(l>max):
			max=l
			maxi=gamma
			maxj=j
print max,maxi,maxj
#gamma=0.001
#for i in range(6):
	#for j in range(10):
		#l=crossvalid('sigmoid',10,gamma,j)
		#if(l>max):
			#max=l
			#maxi=gamma
			#maxj=j
	#gamma*=10