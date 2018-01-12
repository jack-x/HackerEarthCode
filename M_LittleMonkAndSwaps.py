#Python hackserearth Little Monk and Swaps

#Python hackserearth Little Monk and Swaps

def divide(x,y):
	sum=x+y
	half=sum/2.0
	halfzero = int(half)
	
	if(half-float(halfzero) == 0.5):
		return halfzero+1
	else:
		return halfzero

		
		
def InOrder(InOrderTraversal,treeDict,node):
	nodeList = treeDict[node]
	leftChildIndex=nodeList[1]
	rightChildIndex=nodeList[2]
	
	if leftChildIndex is not None:
		InOrder(InOrderTraversal,treeDict,leftChildIndex)
	InOrderTraversal.append(nodeList[0])
	if rightChildIndex is not None:
		InOrder(InOrderTraversal,treeDict,rightChildIndex)


		
def SortandSwap_InsertionSort(InOrderTraversal):
	swaps=0
	#print(InOrderTraversal)
	for x in range(1,len(InOrderTraversal)):
		insertNode = InOrderTraversal[x]
		for y in range(0,x):
			if InOrderTraversal[y] > insertNode:
				for z in range(x,y,-1):
					InOrderTraversal[z] = InOrderTraversal[z-1]
					swaps+=1
				InOrderTraversal[y] = insertNode
				# swaps+=1
				break
			
	print(InOrderTraversal)
	return swaps
		
def SortandSwap_SelectionSort(InOrderTraversal):
	swaps=0
	#print(InOrderTraversal)
	for x in range(0,len(InOrderTraversal)-1):
		min = InOrderTraversal[x]
		minIndex = x
		for y in range(x+1,len(InOrderTraversal)):
			if (InOrderTraversal[y] < min):
				min = InOrderTraversal[y]
				minIndex=y
		if minIndex !=x:
			temp = InOrderTraversal[x]
			InOrderTraversal[x] = InOrderTraversal[minIndex]
			InOrderTraversal[minIndex] = temp
			swaps+=1
	
	#print(swaps)
	#print(InOrderTraversal)
	return swaps		
	
def main_3():
	N=int(input())
	
	treeDict = dict()
	
	OriginalNodes = [-1]
	NewNodes=[]
	for x in input().split(' '):
		OriginalNodes.append(int(x))
	
	
	for x in range(1,len(OriginalNodes)):
		leftChildIndex = 2*x
		rightChildIndex = 2*x +1
		if leftChildIndex < len(OriginalNodes) :
			if rightChildIndex < len(OriginalNodes):
				nodeList = [OriginalNodes[x],leftChildIndex,rightChildIndex]
			else:
				nodeList = [OriginalNodes[x],leftChildIndex,None]
		else:
			nodeList=[OriginalNodes[x],None,None]
		
		treeDict[x] = nodeList
	
	InOrderTraversal = []
	#findingtheInOrderTraversal
	
	InOrder(InOrderTraversal,treeDict,1)
	InOrderr=list(InOrderTraversal)
	InOrderTraversal.sort()
	swaps=0
	for x in range(0,len(InOrderr)):
		if(InOrderr[x] != InOrderTraversal[x]):
			for y in range(x+1,len(InOrderr)):
				if InOrderr[y] == InOrderTraversal[x]:
					temp=InOrderr[y]
					InOrderr[y] = InOrderr[x]
					InOrderr[x] = temp
					swaps+=1
					break
	
	print(swaps)
	# print(InOrderTraversal)
	

	
def main_newLogic():
	N=int(input())
	OriginalNodes = [None]
	NewNodes=[]
	for x in input().split(' '):
		OriginalNodes.append(int(x))
		NewNodes.append(int(x))
	
	NewNodes.sort()
	NewNodes.insert(0,None)
	BST= []
	
	x=1
	y=N
	nodesPlaced=0
	median = int((x+y)/2)
	medianNode= NewNodes[median]
	BST.append([medianNode,median,x,y])
	nodesPlaced+=1
	for p in BST:
		#appending Left Child of P
		x=p[2]
		
		y=p[1]
		if(x!=y):
			median=int((x+y)/2)
			if median != x:
				try:
					medianNode=NewNodes[median]
				except:
					None
				BST.append([medianNode,median,x,y])
				nodesPlaced+=1
		#appending right child of P
		x=p[1]
		y=p[3]
		if x != y:
		
			median=int((x+y)/2)
			if (median != x):
				try:
					medianNode=NewNodes[median]
				except:
					None
					
				BST.append([medianNode,median,x,y])
				nodesPlaced+=1
			if ((y-x) == 1):
				
				try:
					medianNode=NewNodes[median + 1] 
				except:
					None
					
				BST.append([medianNode,median,x,y])
				nodesPlaced+=1
		if(nodesPlaced==N):
			break
			
	print(BST)
	newArray=[]
	for x in BST:
		newArray.append(x[0])
	
	swaps=0
	for x in range(0,N):
		if newArray[x] != OriginalNodes[x]:
			swaps+=1
			for y in range(x+1,N):
				if OriginalNodes[y]==newArray[x]:
					temp=OriginalNodes[y]
					OriginalNodes[y]=OriginalNodes[x]
					OriginalNodes[x]=temp
	
					
		
	print(swaps)
	
def main():
	N=int(input())
	nodes = []
	for x in input().split(' '):
		nodes.append(int(x))
		
	nodes.insert(0,None)
	swaps=100
	swap=0
	while swaps != 0:
		swaps=0
		for x in range(1,len(nodes)):
			parent = nodes[x]
			leftIndex = 2*x
			rightIndex = 2*x+1
			
			if leftIndex <= N:
				left = nodes[leftIndex]
			else:
				left = None
			
			if rightIndex <=N:
				right = nodes[rightIndex]
			else:
				right = None
			
			if right is None and left is None:
				continue
			if right is None:
				if parent   < left:
					nodes[x] = left
					nodes[leftIndex] = parent
					swap+=1
					swaps+=1
				continue
			if parent < left and parent >right:
				nodes[rightIndex] = left
				nodes[leftIndex] = right
				swap+=1
				swaps+=1
				continue
			if parent < left:
				nodes[leftIndex] = parent
				nodes[x] = left
				swap+=1
				swaps+=1
				continue
			if parent > right:
				nodes[x] = right
				nodes[rightIndex] = parent
				swap+=1
				swaps+=1
				continue
			
	
	print(swap)
	print()
	for x in range(1,len(nodes)):
		parent = nodes[x]
		leftIndex = 2*x
		rightIndex = 2*x+1
		
		if leftIndex <= N:
			left = nodes[leftIndex]
		else:
			left = None
		
		if rightIndex <=N:
			right = nodes[rightIndex]
		else:
			right = None
		
		print("Left <-> Parent <-> Right :: {}<->{}<->{} ".format(left,parent,right))
		if left is not None:
			if parent < left:
				print("!!!!!**********RED FLAG****!!!!")
				input()
		if right is not None:
			if parent > right:
				print("!!!!!**********RED FLAG****!!!!")
				input()
			
		print()

	print (nodes)

if __name__ == "__main__": main_3()