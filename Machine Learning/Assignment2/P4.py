import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from sklearn.lda import LDA
from sklearn.qda import QDA
import numpy
fp=open('bezdekIris.data','r')
s=fp.read()
fp.close()
Data=[]
Test=[]
for i in s.split('\n'):
	try:
		Data.append([float(i.split(',')[2]),float(i.split(',')[3])])
		if(i.split(',')[4]=='Iris-setosa'):
			Test.append(0)
		if(i.split(',')[4]=='Iris-versicolor'):
			Test.append(1)
		if(i.split(',')[4]=='Iris-virginica'):
			Test.append(2)
	except:
		pass
h=0.02
Y=Test
X=numpy.transpose(Data)
#clf=LDA()
#clf=QDA()
clf=QDA(reg_param=0.3)
x=clf.fit(Data,Test)
x_min, x_max = X[0].min() - .5, X[0].max() + .5
y_min, y_max = X[1].min() - .5, X[1].max() + .5
xx, yy = numpy.meshgrid(numpy.arange(x_min, x_max, h), numpy.arange(y_min, y_max, h))
Z = clf.predict(numpy.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[0], X[1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()