import random
fp=open('names.txt','r')
s=fp.read()
fp.close()
fp=open('surnames.txt','r')
s2=fp.read()
sur=[]
for i in s2.split('\n'):
	sur.append(i.split('\t')[1])
fp.close()
Males=[]
Females=[]
for i in range(len(s.split('\n'))):
	if(i%8==3):
		Females.append(s.split('\n')[i][0:len(s.split('\n')[i])-2])
	if(i%8==7):
		Males.append(s.split('\n')[i])
Malelist=[]
Femalelist=[]
for i in range(1000):
	Malelist.append(random.choice(Males)+' '+random.choice(sur))
	Femalelist.append(random.choice(Females)+' '+random.choice(sur))
print Malelist
print Femalelist
Depts=['CS','CE','ME','EE','CH']
Degrees=['B.Tech','DD']
StartYears=range(1975,2012)
Sem=range(1,9)
year=range(2000,2006)
grade=['S','A','B','C','D','E']
	
