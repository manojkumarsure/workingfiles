import random
import string
import MySQLdb
db=MySQLdb.connect("localhost","root","ubpassword","Temp")
cursor=db.cursor()
fp=open('names.txt','r')
s=fp.read()
fp.close()
fp=open('surnames.txt','r')
s2=fp.read()
fp.close()
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
for i in range(300):
	Malelist.append(random.choice(Males)+' '+random.choice(sur))
	Femalelist.append(random.choice(Females)+' '+random.choice(sur))
List = Malelist+Femalelist
Sex=['M','F']
Addresses = ['T Nagar','Anna Nagar','Adyar','Guindy' ,'koyambedu','chintadripet']
base=10000000
for i in range(40):
	num = base+i
	name=List[i+300*(i/20)]
	sex=Sex[i/20]
	addr=random.choice(Addresses)
	cursor.execute("insert into salesman values(%s,%s,%s,%s)",(num,name,sex,addr))
base=30000000
for i in range(500):
	num=base+i
	name=List[i%250+300*(i/250)+20]
	phno=random.randint(9000000000,9999999999)
	addr=random.choice(Addresses)
	cursor.execute("insert into Customer values(%s,%s,%s,%s)",(num,name,phno,addr))
base=20000000
Type = ['defect in the item','service center problems','misbehaviour of employee']
comps={}
for i in range(1000):
	num = base + i
	date = str(random.randint(2011,2014))+'-'+str(random.randint(1,11))+'-'+str(random.randint(1,28))
	typ = random.choice(Type)
	details='blah - blah - blah'
	custid=30000000+random.randint(0,499)
	comps[str(num)]=date
	cursor.execute("insert into compliant values(%s,%s,%s,%s,%s)",(num,date,typ,details,custid))
base=40000000
for i in range(5000):
	num = base + i
	custid=30000000+random.randint(0,499)
	salsid=10000000+random.randint(0,39)
	date = str(random.randint(2011,2014))+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28))
	time = str(random.randint(0,23))+':'+str(random.randint(0,59))+':'+str(random.randint(0,59))
	cursor.execute("insert into Bill values(%s,%s,%s,%s,%s)",(num,custid,salsid,date,time))
base=50000000
supplier = ['flipkart','walmart','ebay','olx','quickr','amazon','venkateswara','balaji','snapdeal','shopper']
for i in range(10):
	num = base + i
	name=supplier[i]
	addr=random.choice(Addresses)
	cursor.execute("insert into Supplier values(%s,%s,%s)",(num,name,addr))
def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))
base=60000000
Type=['toys','food','clothing','electronics','household']
for i in range(100000):
	num = base+i
	name = randomword(12)
	year = random.randint(2011,2014)
	manf = str(year) + '-'+str(random.randint(1,12))+'-'+str(random.randint(1,28))
	exp = str(year+1)+'-'+str(random.randint(1,12))+'-'+str(random.randint(1,28))
	weight = random.randint(0,100)
	typ = random.choice(Type)
	supp = 50000000 + random.randint(0,9)
	price = random.randint(10,9999)
	if i < 20000:
		billno =40000000+ random.randint(0,4999)
		cursor.execute("insert into Item values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(num,name,manf,exp,weight,typ,supp,billno,price))
	else:
		cursor.execute("insert into Item(itemid,name,manfdate,expdate,weight,type,supplierid,mrp) values(%s,%s,%s,%s,%s,%s,%s,%s)",(num,name,manf,exp,weight,typ,supp,price))
base = 70000000
for i in range(1500):
	num=base+i
	month=random.randint(1,11)
	year=random.randint(2011,2014)
	stdate = str(year)+'-'+str(month)+'-'+str(random.randint(1,28))
	endate = str(year)+'-'+str(month+1)+'-'+str(random.randint(1,28))
	discount = random.randint(1,10)
	cursor.execute("insert into Offer values(%s,%s,%s,%s)",(num,stdate,endate,discount))
base = 80000000
for i in range(1000):
	views=random.randint(1,3)
	for j in range(views):
		givendate=comps[str(20000000+i)]
		checkdate=givendate.split('-')[0]+'-'+str(int(givendate.split('-')[1])+1)+'-'+str(random.randint(1,28))
		salsid=10000000+random.randint(0,39)
		cursor.execute("insert into checked values(%s,%s,%s)",(20000000+i,checkdate,salsid))
for i in range(100000):
	n=random.randint(0,3)
	for j in range(n):
		offerid = 70000000+random.randint(0,1499)
		cursor.execute("insert into ItemOffers values(%s,%s)",(60000000+i,offerid))
db.commit()
db.close()