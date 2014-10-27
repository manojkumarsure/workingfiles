import random
import MySQLdb
db=MySQLdb.connect("localhost","root","ubpassword","university")
cursor=db.cursor()
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
studentnamelist=Malelist+Femalelist
Sex=['M','F']
Depts=['CS','CE','ME','EE','CH']
Degrees=['B.Tech','DD']
StartYears=range(1975,2012)
Sem=range(1,9)
Grade=['S','A','B','C','D','E']
Credit=[2,3,4]
for i in range(2000):
	rollno=Depts[(i%1000)/200]+'0'+str((i%200)/40)+'B0'+str((40*(i/1000)+i%40)/10)+str((40*(i/1000)+i%40)%10)
	name=studentnamelist[i]
	degree=Degrees[(i%40)/20]
	year='200'+str((i%200)/40)
	sex=Sex[i/1000]
	deptNo=(i%1000)/200
	advisorid=str(deptNo)+'0'+str(4*(i/1000)+(i%40)/10)
	cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(rollno,name,degree,year,sex,deptNo,advisorid))
	#db.commit()
for i in range(5):
	deptId=i
	name=Depts[i]
	hod=studentnamelist[i*100]
	phone='999'+str(i)
	cursor.execute("insert into Department values(%s,%s,%s,%s)",(deptId,name,hod,phone))
	#db.commit()
for i in range(80):
	empId=str(i/16)+str((i%16)/10)+str((i%16)%10)
	name=studentnamelist[(i/16)*100+(i%16)]
	sex=Sex[(i%8)/4]
	startyear=random.choice(StartYears)
	deptNo=i/16
	phone='2'+str(deptNo)+str((i%16)/10)+str((i%16)%10)
	cursor.execute("insert into Professor values(%s,%s,%s,%s,%s,%s)",(empId,name,sex,startyear,deptNo,phone))
	#db.commit()
for i in range(400):
	courseid=Depts[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	coursename=courseid
	credits=random.choice(Credit)
	deptNo=i/80
	cursor.execute("insert into Course values(%s,%s,%s,%s)",(courseid,coursename,credits,deptNo))
	#db.commit()
for i in range(2000):
	rollno=Depts[(i%1000)/200]+'0'+str((i%200)/40)+'B0'+str((40*(i/1000)+i%40)/10)+str((40*(i/1000)+i%40)%10)
	deg=(i%40)/20
	cred=64+deg*16
	for j in range(cred):
		courseid=Depts[(i%1000)/200]+str((j%cred)/8)+'0'+str((j%cred)%8)
		sem=(j%cred)/8+1
		year='200'+str((i%200)/40+(sem)/2)
		grade=random.choice(Grade)
		cursor.execute("insert into enrollment values(%s,%s,%s,%s,%s)",(rollno,courseid,sem,year,grade))
		#db.commit()
for i in range(400):
	courseid=Depts[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	for j in range(10):
		year='200'+str(j)
		sem=(i%80)/8+1
		number=random.randint(0,15)
		classroom=Depts[i/80]+str(number/10)+str(number%10)
		empid=str(i/80)+str(number/10)+str(number%10)
		try:
			cursor.execute("insert into Teaching values(%s,%s,%s,%s,%s)",(empid,courseid,sem,year,classroom))
		except:
			pass
		#db.commit()
for i in range(400):
	courseid=Depts[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	if (i%80)/8 !=0 :
		prereq=Depts[i/80]+str((i%80)/8-1)+'0'+str((i%80)%8)
		cursor.execute("insert into PreRequisite values(%s,%s)",(prereq,courseid))
		#db.commit()
db.commit()
db.close()