NodeValues=dict()
childrenDict=dict()
allSubNodes=dict()


def CalculateAllSubNodes(node):
	if node in childrenDict:
		children = childrenDict[node]
	else:
		allSubNodes[node] = []
		return
	
	for child in children:
		CalculateAllSubNodes(child)
	
	for child in children:
		subNodes = allSubNodes[child]
		try:
			allSubNodes[node].append(child)
		except:
			allSubNodes[node]=[child]
		for n in subNodes:
			allSubNodes[node].append(n)
	
	return

def main2():
	i=input().split(' ')
	N=int(i[0])
	K=int(i[1])
	

	values=input().split(' ')
	parents = input().split(' ')
	
	node=1
	for p in parents:	

		if int(p) in childrenDict:
			childrenDict[int(p)].append(node+1)
		else:
			childrenDict[int(p)] = [node+1]
		node+=1
	
	node =1 
	for v in values:
		if node not in childrenDict:
			allSubNodes[node] = []
		NodeValues[node]=int(v)
		node+=1
	
	# keys=list(allSubNodes.keys())
	# print("Node Value List: {}".format(NodeValues))
	# print("Children List Dict: {}".format(childrenDict))
	# print("Parents List Dict: {}".format(parentsDict))
	# print("allSubNodes: {}".format(allSubNodes))
	
	#CalculateALlSubNodesHere
	# print("Keys: {}".format(keys))
	# for node in keys:
		# print("Node: {}".format(node))
		# if(node==1):
			# print(allSubNodes)
		
		# parent = parentsDict[node]
		# print("Parent: {}".format(parent))
		# try:
			# allSubNodes[parent].append(node)
			# print("AllSubNodes[{}]: {}".format(parent,allSubNodes[parent]))
		# except:
			# allSubNodes[parent] = [node]
			# print("AllSubNodes[{}]: {}".format(parent,allSubNodes[parent]))
		# subNodes = allSubNodes[node]
		# for subnode in subNodes:
				# allSubNodes[parent].append(subnode)
		# print("AllSubNodes[{}]: {}".format(parent,allSubNodes[parent]))
		# if parent not in keys:
			# keys.append(parent)

	CalculateAllSubNodes(1)
	# print(allSubNodes)
	triplets = 0
	for node in allSubNodes.keys():
		subNodes = allSubNodes[node]
		# kk = K - NodeValues[node]
		for y in range(0,len(subNodes) -1):
			kk = K - NodeValues[subNodes[y]] - NodeValues[node]
			for z in range(y+1,len(subNodes)):
				if NodeValues[subNodes[z]] >=kk:
					triplets+=1
			
	print(triplets)
	return
	triplets = calculateTriplets(1,childrenDict,[])
	# print()
	# print()
	# f= open('output.txt','w')
	# f.write(str(triplets))
	# f.close()
	# print(triplets)
	
	legitTripletCount=0
	for selection in triplets:
		if NodeValues[selection[0]] >= K:
			legitTripletCount+=1
		else:
			total=NodeValues[selection[0]]+NodeValues[selection[1]]+NodeValues[selection[2]]
			if total >= K:
				legitTripletCount+=1
	
	# print("LegitTripletCount: {}". format(legitTripletCount))
	print(legitTripletCount)
	
	
def calculateTriplets(node,childrenDict,triplets):
	# subNodes = calculateAllSubNodes(node,childrenDict,allSubNodes)
	subNodes=allSubNodes[node]
	# print("Sub Nodes of {}: {}".format(node,subNodes))
	for x in range(0,len(subNodes)-1):
		for y in range(x+1,len(subNodes)):
			triplet=[node,subNodes[x],subNodes[y]]
			triplets.append(triplet)
	if node in childrenDict:
		children=childrenDict[node]
		# print("Children of {}: {}".format(node,children))
		calculateTriplets(children[0],childrenDict,triplets)
		if len(children) == 2:
			calculateTriplets(children[1],childrenDict,triplets)
	
	return triplets

	
	
def calculateAllSubNodes(node,childrenDict):
	if node in childrenDict:
		children=list(childrenDict[node])
	
		for x in children:
			if x in childrenDict:
				ChildrenChildren=childrenDict[x]
				for y in ChildrenChildren:
					children.append(y)
		
		return children
	else:
		return []
		
def main():
	i=input().split(' ')
	N=int(i[0])
	K=int(i[1])
	
	NodeValues=dict()
	node=1
	values=input().split(' ')
	
	for v in values:
		NodeValues[node]=int(v)
		node+=1
	Tree=dict()
	parentDict=dict()
	parents = input().split(' ')
	node=1
	parentDict[1] = 0
	
	numberOfChildren = dict()
	for p in parents:	
		parentDict[node+1] = int(p)
		if int(p) in Tree:
			Tree[int(p)].append(node+1)
		else:
			Tree[int(p)] = [node+1]
		node+=1
	print(NodeValues)
	print(Tree)
	print(parentDict)
	
	traversalNodes=[[]]
	for x in NodeValues.keys():
		if x not in Tree:
			numberOfChildren[x] = 0
			traversalNodes[0].append(x)
	print(numberOfChildren)
	
	triplets=0
	print()
	print()
	print(traversalNodes)
	for x in traversalNodes:
		appending = []
		print(traversalNodes)
		print(numberOfChildren)
		input()
		for y in x:
			if(y==0):
				break
			parent = parentDict[y]
			if parent not in appending:
				appending.append(parent)
			try:
				numberOfChildren[parent] = numberOfChildren[parent] + numberOfChildren[y] + 1
			except:
				numberOfChildren[parent] = numberOfChildren[y] + 1
		if(appending==[]):
			break
		traversalNodes.append(appending)
	
	del numberOfChildren[0]
	print(numberOfChildren)
	for x in numberOfChildren.keys():
		n = numberOfChildren[x]
		triplets = triplets + int(n*(n-1)/2)
	print(triplets)

	
if __name__ == "__main__": main2()
