
def main_3():
	N=int(input())
	
	a = input().split(' ')
	
	arr=[]
	
	for x in a:
		arr.append(int(x))
	
	pairs=[]
	differenceStack=[None]*N
	
	NextStack=[None]*N
	PrevStack=[None]*N
	
	NextElementGreater=[]
	
	currentElement=[arr[0],0]
	NextElementGreater.append(currentElement)
	
	currentElementReverse=[arr[N-1],N-1]
	PrevElementGreater=[]
	PrevElementGreater.append(currentElementReverse)
	
	pairsPossible = []
	IndexDifferenceStack=[]
	
	
	for x in range(1,N):
		y=N-1-x
		currentElement=[arr[x],x]
		currentElementReverse=[arr[y],y]
		while(len(NextElementGreater) > 0 and currentElement[0] > NextElementGreater[-1][0]):
			element=NextElementGreater.pop()
			NextStack[element[1]] = x
		
		while(len(PrevElementGreater) > 0 and currentElementReverse[0] > PrevElementGreater[-1][0]):
			element=PrevElementGreater.pop()
			PrevStack[element[1]] = y
		
		NextElementGreater.append(currentElement)
		PrevElementGreater.append(currentElementReverse)
		
		
	#The full Array list of Previous Greater Number at each Position and Next Greater number at each position has been calculated
	#Now just need to calculate the number of pairs possible for each position
	
	Totalpairs=0
	DifferenceAndPairDict = dict()
	
	for x in range(0,N):
		if NextStack[x] == None:
			Totalpairs+=0
			pairs=0
			Difference=None
			
		else:
			Difference = NextStack[x] - x
			if PrevStack[x] == None:
				pairs=x+1
			else:
				pairs=x-PrevStack[x]
		
		if Difference in DifferenceAndPairDict.keys():
			originalPairs=DifferenceAndPairDict[Difference]
			if(originalPairs<pairs):
				Totalpairs = Totalpairs + pairs - originalPairs
				DifferenceAndPairDict[Difference] = pairs
		else:
			DifferenceAndPairDict[Difference] = pairs
			Totalpairs+=pairs
	
	# pairsPossible = []
	# IndexDifferenceStack=[]
	# Totalpairs=0
	# DifferenceTallied=[]
	# DifferenceAndPair=[]
	
	
	# for x in range(0,N):
		# if NextStack[x] == None:
			# pairsPossible.append(0)
			# IndexDifferenceStack.append(None)
			
		# else:
			# IndexDifferenceStack.append(NextStack[x] - x)
			# if PrevStack[x] == None:
				# pairsPossible.append(x+1)
			# else:
				# pairsPossible.append(x-PrevStack[x])
		
		# if IndexDifferenceStack[x] != None:
			# if IndexDifferenceStack[x] not in DifferenceTallied:
				# Totalpairs+= pairsPossible[x]
				# DifferenceTallied.append(IndexDifferenceStack[x])
				# DifferenceAndPair.append([IndexDifferenceStack[x],pairsPossible[x]])
			# else:
				# index=DifferenceTallied.index(IndexDifferenceStack[x])
				# if(pairsPossible[x] > DifferenceAndPair[index][1]):
					# Totalpairs= Totalpairs + pairsPossible[x] - DifferenceAndPair[index][1]
					# DifferenceAndPair[index][1] = pairsPossible[x]
	
	# Totalpairs=0
	# DifferenceTallied=[]
	# DifferenceAndPair=[]
	
	# for x in range(0,N):
		# if IndexDifferenceStack[x] != None:
			# if IndexDifferenceStack[x] not in DifferenceTallied:
				# Totalpairs+= pairsPossible[x]
				# DifferenceTallied.append(IndexDifferenceStack[x])
				# DifferenceAndPair.append([IndexDifferenceStack[x],pairsPossible[x]])
			# else:
				# index=DifferenceTallied.index(IndexDifferenceStack[x])
				# if(pairsPossible[x] > DifferenceAndPair[index][1]):
					# Totalpairs= Totalpairs + pairsPossible[x] - DifferenceAndPair[index][1]
					# DifferenceAndPair[index][1] = pairsPossible[x]
	
	
	
	print(Totalpairs)
		
def main_2():
	f=open("FantabulousPairs_Input.txt","r")
	ff=open("FantabulousPairs_Output.txt","w")
	
	N=int(f.readline())
	
	a = f.readline().split(' ')
	
	arr=[]
	
	for x in a:
		arr.append(int(x))
	
	print("INPUT OVER!!")
	#ff.write(str(arr))
	ff.write("\n")
	pairs=[]
	differenceStack=[None]*N
	
	NextStack=[None]*N
	PrevStack=[None]*N
	
	NextElementGreater=[]
	
	currentElement=[arr[0],0]
	NextElementGreater.append(currentElement)
	
	currentElementReverse=[arr[N-1],N-1]
	PrevElementGreater=[]
	PrevElementGreater.append(currentElementReverse)
	
	pairsPossible = []
	IndexDifferenceStack=[]
	
	
	for x in range(1,N):
		y=N-1-x
		currentElement=[arr[x],x]
		currentElementReverse=[arr[y],y]
		while(len(NextElementGreater) > 0 and currentElement[0] > NextElementGreater[-1][0]):
			element=NextElementGreater.pop()
			NextStack[element[1]] = x
		
		while(len(PrevElementGreater) > 0 and currentElementReverse[0] > PrevElementGreater[-1][0]):
			element=PrevElementGreater.pop()
			PrevStack[element[1]] = y
		
		NextElementGreater.append(currentElement)
		PrevElementGreater.append(currentElementReverse)
		
	print("PREV STACK AND NEXT STACK FILLED")	
	#The full Array list of Previous Greater Number at each Position and Next Greater number at each position has been calculated
	#Now just need to calculate the number of pairs possible for each position
	
	Totalpairs=0
	DifferenceAndPairDict = dict()
	
	for x in range(0,N):
		if NextStack[x] == None:
			Totalpairs+=0
			pairs=0
			Difference=None
			
		else:
			Difference = NextStack[x] - x
			if PrevStack[x] == None:
				pairs=x+1
			else:
				pairs=x-PrevStack[x]
		
		if Difference in DifferenceAndPairDict.keys():
			originalPairs=DifferenceAndPairDict[Difference]
			if(originalPairs<pairs):
				Totalpairs = Totalpairs + pairs - originalPairs
				DifferenceAndPairDict[Difference] = pairs
		else:
			DifferenceAndPairDict[Difference] = pairs
			Totalpairs+=pairs
		
	# pairsPossible = []
	# IndexDifferenceStack=[]
	# Totalpairs=0
	# DifferenceTallied=[]
	# DifferenceAndPair=[]
	
	
	# for x in range(0,N):
		# if NextStack[x] == None:
			# pairsPossible.append(0)
			# IndexDifferenceStack.append(None)
			
		# else:
			# IndexDifferenceStack.append(NextStack[x] - x)
			# if PrevStack[x] == None:
				# pairsPossible.append(x+1)
			# else:
				# pairsPossible.append(x-PrevStack[x])
		
		# if IndexDifferenceStack[x] != None:
			# if IndexDifferenceStack[x] not in DifferenceTallied:
				# Totalpairs+= pairsPossible[x]
				# DifferenceTallied.append(IndexDifferenceStack[x])
				# DifferenceAndPair.append([IndexDifferenceStack[x],pairsPossible[x]])
			# else:
				# index=DifferenceTallied.index(IndexDifferenceStack[x])
				# if(pairsPossible[x] > DifferenceAndPair[index][1]):
					# Totalpairs= Totalpairs + pairsPossible[x] - DifferenceAndPair[index][1]
					# DifferenceAndPair[index][1] = pairsPossible[x]
	
	# Totalpairs=0
	# DifferenceTallied=[]
	# DifferenceAndPair=[]
	
	# for x in range(0,N):
		# if IndexDifferenceStack[x] != None:
			# if IndexDifferenceStack[x] not in DifferenceTallied:
				# Totalpairs+= pairsPossible[x]
				# DifferenceTallied.append(IndexDifferenceStack[x])
				# DifferenceAndPair.append([IndexDifferenceStack[x],pairsPossible[x]])
			# else:
				# index=DifferenceTallied.index(IndexDifferenceStack[x])
				# if(pairsPossible[x] > DifferenceAndPair[index][1]):
					# Totalpairs= Totalpairs + pairsPossible[x] - DifferenceAndPair[index][1]
					# DifferenceAndPair[index][1] = pairsPossible[x]
	
	
	#print(NextStack)
	#ff.write(str(NextStack))
	ff.write("\n \n")
	#ff.write(str(PrevStack))
	ff.write("\n \n")
	ff.write("Total Pairs: {}".format(Totalpairs))
	ff.close()

	# for x in range(0,N):
		# print("Currently at element: {}".format(x))
		# print("Element Value: {}".format(arr[x]))
		# highestelement=arr[x]
		# indexOne=1
		# indexTwo=1
		# for y in range(x+1,N):
			# indexTwo+=1
			# if(arr[y]>highestelement):
				# pair=[indexOne,indexTwo]
				# if( pair not in pairs):
					# ff.write(str(pair))
					# ff.write("\n")
					# pairs.append([indexOne,indexTwo])
				# highestelement=arr[y]
				# indexOne=indexTwo
	
	# ff.write(pairs)
	# ff.write("*****")
	# ff.write(len(pairs))
	# ff.write("******")
	# f.close()
	# ff.close()
	print("Program Over. File Written !!!")
def main():
	N=int(input())
	
	a = input().split(' ')
	
	arr=[]
	
	for x in a:
		arr.append(int(x))
	
	pairs=[]
	
	for x in range(0,N):
		highestelement=arr[x]
		indexOne=1
		indexTwo=1
		for y in range(x+1,N):
			indexTwo+=1
			if(arr[y]>highestelement):
				pair=[indexOne,indexTwo]
				if( pair not in pairs):
					pairs.append([indexOne,indexTwo])
				highestelement=arr[y]
				indexOne=indexTwo
	
	print(pairs)
	print("*****")
	print(len(pairs))
	print("******")
	
if __name__ == "__main__": main_3()
