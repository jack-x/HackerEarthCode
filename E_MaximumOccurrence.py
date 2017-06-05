
def main():
	statement = input()
	d=dict()
	for s in statement:
		if s in d.keys():
			d[s]+=1
		else:
			d[s] = 1
		
	max=[]
	
	for x in d.keys():
		if(len(max)==0):
			max.append([x,d[x]])
			#print("max {}".format(max))
		else:
			if(d[x] == max[0][1]):
				max.append([x,d[x]])
			elif(d[x] > max[0][1]):
				max=[[x,d[x]]]
	
	if(len(max) == 1):
		print("{} {}".format(max[0][0],max[0][1]))
	else:
		least=[max[0]]
		for x in range(1,len(max)):
			if ord(least[0][0]) > ord(max[x][0]):
				#print("OVER HERE")
				least=[max[x]]
		print("{} {}".format(least[0][0],least[0][1]))
		

if __name__ == '__main__': main()
