#Problem3:
#Applying KNN for different values of k and printing the performance results

import numpy
import sklearn.metrics
from sklearn.neighbors import KNeighborsClassifier

#reading the datasets from Ds1-train and ds1-test and storing them into test and train
fp=open('DS1-train.csv','r')
fp2=open('DS1-test.csv','r')
data=fp.read()
data2=fp2.read()
fp.close()
Train=[]
Test=[]
for i in range(0,1200):
	Train.append([])
	Train[i].append(1)
	for j in range(0,10):
		Train[i].append(float(data.split('\n')[i].split(',')[j]))
for i in range(0,800):
	Test.append([])
	Test[i].append(1)
	for j in range(10):
		Test[i].append(float(data2.split('\n')[i].split(',')[j]))

#Applying knn for different values of k and printing performance results for each k
for i in range(1,11):
	neigh = KNeighborsClassifier(n_neighbors=i)
	neigh.fit(Train,600*[0]+600*[1])
	Out=neigh.predict(Test)
	print "for k="+str(i)
	print "Accuracy - "+str(sklearn.metrics.accuracy_score(400*[0]+400*[1],Out))
	print "Precision - "+ str(sklearn.metrics.precision_score(400*[0]+400*[1],Out))
	print "Recall - "+str(sklearn.metrics.recall_score(400*[0]+400*[1],Out))
	print "F-measure -"+str(sklearn.metrics.f1_score(400*[0]+400*[1],Out))