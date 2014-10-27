import random
import MySQLdb
fp=open('db.config','r')
s=fp.read()
fp.close()
host=s.split('\n')[0].split('=')[1]
username=s.split('\n')[1].split('=')[1]
password=s.split('\n')[2].split('=')[1]
database=s.split('\n')[3].split('=')[1]
db=MySQLdb.connect(host,username,password,database)
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
Deptname=['Computer Science ','Civil Engineering ','Mechanical Engineering ','Electrical Engineering ','Chemical Engineering ']
Degrees=['B.Tech','DD']
StartYears=range(1975,2012)
Sem=range(1,9)
Grade=['S']*10+['A']*20+['B']*25+['C']*20+['D']*10+['E']*10+['U']*5
Gradepoint=[10]*10+[9]*20+[8]*25+[7]*20+[6]*10+[4]*10+[0]*5
Credit=[2,3,4]
for i in range(2000):
	rollno=Depts[(i%1000)/200]+'0'+str((i%200)/40)+'B0'+str((40*(i/1000)+i%40)/10)+str((40*(i/1000)+i%40)%10)
	name=studentnamelist[i]
	degree=Degrees[(i%40)/20]
	year='200'+str((i%200)/40)
	sex=Sex[i/1000]
	deptNo=(i%1000)/200
	number=random.randint(0,15)
	advisorid=str(deptNo)+str(number/10)+str(number%10)
	cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(rollno,name,degree,year,sex,deptNo,advisorid))
for i in range(5):
	deptId=i
	name=Depts[i]
	hod=studentnamelist[i*100]
	phone='999'+str(i)
	cursor.execute("insert into department values(%s,%s,%s,%s)",(deptId,name,hod,phone))
for i in range(80):
	empId=str(i/16)+str((i%16)/10)+str((i%16)%10)
	name=studentnamelist[(i/16)*100+(i%16)+1000*((i%8)/4)]
	sex=Sex[(i%8)/4]
	startyear=random.choice(StartYears)
	deptNo=i/16
	phone='2'+str(deptNo)+str((i%16)/10)+str((i%16)%10)
	cursor.execute("insert into professor values(%s,%s,%s,%s,%s,%s)",(empId,name,sex,startyear,deptNo,phone))
for i in range(400):
	courseid=Depts[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	coursename=Deptname[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	credits=random.choice(Credit)
	deptNo=i/80
	cursor.execute("insert into course values(%s,%s,%s,%s)",(courseid,coursename,credits,deptNo))
for i in range(2000):
	rollno=Depts[(i%1000)/200]+'0'+str((i%200)/40)+'B0'+str((40*(i/1000)+i%40)/10)+str((40*(i/1000)+i%40)%10)
	deg=(i%40)/20
	cred=64+deg*16
	for j in range(cred):
		courseid=Depts[(i%1000)/200]+str((j%cred)/8)+'0'+str((j%cred)%8)
		sem=(j%cred)/8+1
		year='200'+str((i%200)/40+(sem)/2)
		num=random.choice(range(100))
		grade=Grade[num]
		gradepoint=Gradepoint[num]
		cursor.execute("insert into enrollment values(%s,%s,%s,%s,%s,%s)",(rollno,courseid,sem,year,grade,gradepoint))
for i in range(400):
	courseid=Depts[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	for j in range(10):
		year='200'+str(j)
		sem=(i%80)/8+1
		number=random.randint(0,15)
		classroom=Depts[i/80]+str(number/10)+str(number%10)
		empid=str(i/80)+str(number/10)+str(number%10)
		try:
			cursor.execute("insert into teaching values(%s,%s,%s,%s,%s)",(empid,courseid,sem,year,classroom))
		except:
			pass
for i in range(400):
	courseid=Depts[i/80]+str((i%80)/8)+'0'+str((i%80)%8)
	if (i%80)/8 !=0 :
		prereq=Depts[i/80]+str((i%80)/8-1)+'0'+str((i%80)%8)
		cursor.execute("insert into prerequisite values(%s,%s)",(prereq,courseid))
db.commit()
db.close()