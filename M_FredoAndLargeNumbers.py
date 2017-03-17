from collections import OrderedDict as ODict

N=int(input())
arr = input().split()
d=dict()
for a in arr:
	if a in d.keys():
		d[a] = d[a]+1
	else:
		d[a]=1
#print(d)
dd = ODict()

for a in d.keys():
	dd[a] = d[a]

#print (dd)	

Q=int(input())

for x in range(0,Q):
	query = input().split()
	f = int(query[1])
	if (query[0] == '0'):
		#Type 0 Query
		#First element whose frequency is atleast f	
		flag = 0
		for a in arr:
			if(dd[a] >= f):
				print(a)
				flag = 1 
				break
		if(flag==0):
			print('0')
	else:
		flag = 0
		for a in arr:
			if(dd[a] == f):
				print(a)
				flag = 1
				break
		if(flag == 0):
			print('0')
