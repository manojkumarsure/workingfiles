import numpy
import matplotlib.pyplot as plt
import sklearn.metrics
from sklearn.neighbors import KNeighborsClassifier
def to_csv(x,y,z):
	fp=open('data.csv','a')
	print >>fp,'x,y,z'
	for i in range(x.size):
		print >>fp,str(x[i])+','+str(y[i])+','+str(z[i])
	fp.close()
mean1=[0,0]
covariance1=[[1,0],[0,2]]
mean2=[10,0]
covariance2=[[1,0],[1,1]]
x1,y1=numpy.random.multivariate_normal(mean1,covariance1,500).T
x2,y2=numpy.random.multivariate_normal(mean2,covariance2,500).T
to_csv(x1[0:400]+x2[0:400],y1[0:400]+y2[0:400],400*[0]+400*[1])
plt.plot(x1[400:500],y1[400:500],'o')
plt.plot(x2[400:500],y2[400:500],'o')
neigh = KNeighborsClassifier(n_neighbors=5)
X=[]
for i in range(0,400):
	X.append([x1[i],y1[i]])
for i in range(0,400):
	X.append([x2[i],y2[i]])
neigh.fit(X,400*[0]+400*[1])
KNeighborsClassifier()
xtest=[]
for i in range(400,500):
	xtest.append([x1[i],y1[i]])
for i in range(400,500):
	xtest.append([x2[i],y2[i]])
ytest=neigh.predict(xtest)
print sklearn.metrics.accuracy_score(100*[0]+100*[1],ytest,normalize=True, sample_weight=None)
plt.show()