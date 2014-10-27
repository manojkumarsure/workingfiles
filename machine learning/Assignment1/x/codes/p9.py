import numpy
from numpy.linalg import inv
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn import linear_model
import sklearn.metrics
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
fp=open('DS3/train.csv','r')
s=fp.read()
fp.close()
fp=open('DS3/test.csv','r')
s2=fp.read()
fp.close()
Data=[]
Test=[]
for i in range(len(s.split('\n'))):
	Data.append([])
	for j in s.split('\n')[i].split(','):
		try:
			Data[i].append(float(j))
		except:
			pass
for i in range(len(s2.split('\n'))):
	Test.append([])
	for j in s2.split('\n')[i].split(','):
		try:
			Test[i].append(float(j))
		except:
			pass
clf=LDA(n_components=2)
z=clf.fit_transform(numpy.array(Data[0:len(Data)-1]),1000*[0]+1000*[1])
New=clf.predict(Test[0:len(Test)-1])
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X=[]
Y=[]
Z=[]
for i in range(len(Data)):
	try:
		X.append(Data[i][0])
		Y.append(Data[i][1])
		Z.append(Data[i][2])
	except:
		pass
ax.scatter(X,Y,Z)
plt.show()
print sklearn.metrics.accuracy_score(200*[0]+200*[1],New,normalize=True, sample_weight=None)