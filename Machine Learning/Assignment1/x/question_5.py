data = []
fp = open("communities.data","r")
textdata = fp.read()
store = []
mean = []
quad = []
for i in textdata.split('\n'):
	quad.append(i)

for i in quad:
	value = 0
	counter = 0
	temp = i
	for j in range(0,len(temp.split(','))):
		if temp.split(',')[j] == '?':
			continue
		if j != 3:
			try:
				value += float(temp.split(',')[j])
				counter += 1
			except:
				pass
	try:
		mean.append(value/(counter*1.0))
	except:
		pass


for i in range(0,len(textdata.split('\n'))-1):
	store = []
	temp = textdata.split('\n')[i]
	for j in range(0,len(temp.split(','))):
		
		if temp.split(',')[j] == '?':
			store.append(mean[j])
			continue
		if j == 3:
			continue
		store.append(float(temp.split(',')[j]))
	data.append(store)
print len(quad)
