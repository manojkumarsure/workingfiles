import Image,os,math
from sklearn.lda import LDA
from sklearn.decomposition import PCA
import sklearn.metrics
import numpy
from sklearn import preprocessing
from numpy.linalg import inv
from sklearn import svm

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

path1='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/coast/Train/'
path2='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/forest/Train/'
path3='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/coast/Test/'
path4='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/forest/Test/'
path5='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/insidecity/Train/'
path6='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/mountain/Train/'
path7='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/insidecity/Test/'
path8='/home/manoj/Desktop/working files/Machine Learning/Assignment2/For_the_students/data_students/mountain/Test/'

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
log_reg=linear_model.LogisticRegression(penalty='l1')
log_reg.fit(TrainData,count1*[0]+count2*[1])
New=log_reg.predict(TestData)
fp.close()