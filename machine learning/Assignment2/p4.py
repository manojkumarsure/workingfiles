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
clf=LDA()
x=clf.fit_transform(Data,Test)
coeff=clf.coef_
print coeff
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X1=[]
Y1=[]
X2=[]
Y2=[]
X3=[]
Y3=[]
for i in range(len(x)/3):
	try:
		X1.append(x[i][0])
		Y1.append(x[i][1])
	except:
		pass
for i in range(len(x)/3,2*len(x)/3):
	try:
		X2.append(x[i][0])
		Y2.append(x[i][1])
	except:
		pass
for i in range(2*len(x)/3,len(x)):
	try:
		X3.append(x[i][0])
		Y3.append(x[i][1])
	except:
		pass
ax.scatter(X1,Y1,color='red')
ax.scatter(X2,Y2,color='blue')
ax.scatter(X3,Y3,color='green')
ax.plot([-50,50],[coeff[0][0]-50*coeff[0][1],coeff[0][0]+50*coeff[0][1]],color='orange')
#ax.plot([-50,50],[coeff[1][0]-50*coeff[1][1],coeff[1][0]+50*coeff[1][1]])
ax.plot([-50,50],[coeff[2][0]-50*coeff[2][1],coeff[2][0]+50*coeff[2][1]],color='purple')
#plt.show()




clf=QDA()
clf.fit(Data,Test)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
X1=[]
Y1=[]
X2=[]
Y2=[]
X3=[]
Y3=[]
for i in range(len(x)/3):
	try:
		X1.append(x[i][0])
		Y1.append(x[i][1])
	except:
		pass
for i in range(len(x)/3,2*len(x)/3):
	try:
		X2.append(x[i][0])
		Y2.append(x[i][1])
	except:
		pass
for i in range(2*len(x)/3,len(x)):
	try:
		X3.append(x[i][0])
		Y3.append(x[i][1])
	except:
		pass
ax.scatter(X1,Y1,color='red')
ax.scatter(X2,Y2,color='blue')
ax.scatter(X3,Y3,color='green')

plt.show()