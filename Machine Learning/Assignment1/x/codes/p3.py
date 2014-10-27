import numpy
import sklearn.metrics
from sklearn.neighbors import KNeighborsClassifier
fp=open('DS1.csv','r')
data=fp.read()
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
		Test[i].append(float(data.split('\n')[i+1200].split(',')[j]))
neigh = KNeighborsClassifier(n_neighbors=10)
neigh.fit(Train,600*[0]+600*[1])
Out=neigh.predict(Test)
print sklearn.metrics.accuracy_score(400*[0]+400*[1],Out)
print sklearn.metrics.precision_score(400*[0]+400*[1],Out)
print sklearn.metrics.recall_score(400*[0]+400*[1],Out)
print sklearn.metrics.f1_score(400*[0]+400*[1],Out)