
def main():
	n=int(input())
	for case in range(0,n):
		arrsize=int(input())
		nodes=input().split(' ')
		nodes.insert(0,'-1')
		r=RangeBuilder(arrsize)
		printedDict=dict()
		#RightMirror
		for x in r:
			if x == [1]:
				print(nodes[x[0]])
				printedDict[x[0]] =1
			else:
				# print(x)
				for y in range(x[1],x[0]-1,-1):
					if(nodes[y] == '0'):
						continue
					else:
						print(nodes[y])
						printedDict[y] =1
						break
		#LeftMirror
		# del r[0]
		for x in r:
			if x == [1]:
				if x[0] not in printedDict:
					print(nodes[x[0]])
			else:
				for y in range(x[0],x[1]+1):
					if(nodes[y] == '0'):
						continue
					elif y not in printedDict:
						print(nodes[y])
						printedDict[y] =1
						break
		
		print()
def RangeBuilder(n):
	RANGE=[]
	rangeStarting = 1
	rangeEnding=1
	RANGE.append([1])
	
	rangeCount=1
	while rangeEnding<=n:
		rangeStarting=2**rangeCount
		rangeEnding=2**(rangeCount+1)
		RANGE.append([rangeStarting,rangeEnding-1])
		rangeCount+=1
	
	return RANGE
		
if __name__ == "__main__": main()