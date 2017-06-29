class Node:
	def __init__(self,v):
		self.value=v
		self.left=None
		self.right=None
		self.parent=-1
		self.Tag='node'

def main_3():
	t=int(input())
	nodeSet=set('abcdefghijklmnopqrstuvwxyz')
	for case in range(0,t):
		inp=input().split(' ')
		column=int(inp[0])
		string=inp[1]
		root = Node(string[0])
		root.Tag= 'root'
		r=root
		for s in string[1:]:
			if s == '(':
				node = Node(-1)
				r.left=node
				continue
			if s in nodeSet:
				if r.left.value == -1:
					r.left.value = s
					r.left.parent=r
					r=r.left
					continue
				else:
					r.right = Node(s)
					r.right.parent = r
					r = r.right
					continue
			if s =='.':
				if r.left.value == -1:
					r.left.value = '.'
					r.left.parent = r
					continue
				else:
					r.right = Node(s)
					r.right.parent = r
					continue
			if s==')':
				r=r.parent
				continue
		# TreeTraversal(root)
		#Collect all in particular column
		columnList = []
		CollectColumn(root,columnList,column,0)
		# print(columnList)
		columnList.sort()
		if len(columnList) !=0:
			for x in columnList:
				print(x,end='')
			print()
		else:
			print("Common Gandhijee!")
def CollectColumn(node,columnList,column,currentGraphLevel):
	if node.value == '.':
		return
	if currentGraphLevel == column:
		columnList.append(node.value)
	
	CollectColumn(node.left,columnList,column,currentGraphLevel-1)
	CollectColumn(node.right,columnList,column,currentGraphLevel+1)
	
		
def TreeTraversal(root):
	print(root.value)
	if root.left.value != '.':
		TreeTraversal(root.left)
	if root.right.value != '.':
		TreeTraversal(root.right)

def main_noPrint():
	t=int(input())
	nodeSet=set('abcdefghijklmnopqrstuvwxyz')
	for case in range(0,t):
		inp=input().split(' ')
		column=int(inp[0])
		string=inp[1]
		
		nodeDict = dict()
		parentDict = dict()
		tree=''
		for s in string:
			if(s == '(' or s==')'):
				continue
			elif (s=='.'):
				tree=tree+'0'
			else:
				tree=tree+s
		
		x=0
		parent=-1
		while x<len(tree):
			if parent in nodeDict and len(nodeDict[parent]) == 2: 
				parent= parentDict[parent]
			y=x+1
			A=tree[x]
			B=tree[y]
			if(A in nodeSet and B in nodeSet):
				parentDict[A] = parent
				try:
					nodeDict[parent].append(A)
				except:
					nodeDict[parent] = [A]
				parentDict[B] = A
				try:
					nodeDict[A].append(B)
				except:
					nodeDict[A] = [B]
				parent = B
				x=y+1
				continue
			if(A in nodeSet and B == '0'):
				try:
					nodeDict[parent].append(A)
				except:
					nodeDict[parent] = [A]

				parentDict[A] = parent

				try:
					nodeDict[A].append(0)
				except:
					nodeDict[A] = [0]
				y+=1
				B=tree[y]
				if(B == '0'):
					nodeDict[A].append(0)
					parent = parentDict[A]
				else:
					parentDict[B] = A
					nodeDict[A].append(B)
					parent=B
				x=y+1
				continue
			if(A =='0' and B in nodeSet):
				try:
					nodeDict[parent].append(0)
				except:
					nodeDict[parent] = [0]

				while len(nodeDict[parent]) == 2: 
					parent=parentDict[parent]
				
				try:
					nodeDict[parent].append(B)	
				except:
					nodeDict[parent] = [B]
				parentDict[B] = parent
				parent=B
				x=y+1
				continue
			if(A=='0' and B =='0'):
				nodeDict[parent] = [0,0]
				x=y+1
				parent=parentDict[parent]
				continue
		
		root = nodeDict[-1][0]
		nodeDict[root].insert(0,0)
		for node in parentDict:
			parent = parentDict[node]
			if parent == -1:
				continue
			parentGraphValue = nodeDict[parent][0]
			if(node == nodeDict[parent][1]):
				nodeDict[node].insert(0,parentGraphValue-1)
			else:
				nodeDict[node].insert(0,parentGraphValue+1)
				
		C=[]
		ExtractColumn(nodeDict,root,column,C)
		C.sort()
		if len(C) == 0:
			print("Common Gandhijee!")
		else:
			for x in C:
				print(x,end='')
			print()

def main():
	t=int(input())
	nodeSet=set('abcdefghijklmnopqrstuvwxyz')
	for case in range(0,t):
		inp=input().split(' ')
		column=int(inp[0])
		string=inp[1]
		
		nodeDict = dict()
		parentDict = dict()
		tree=''
		for s in string:
			if(s == '(' or s==')'):
				continue
			elif (s=='.'):
				tree=tree+'0'
			else:
				tree=tree+s
		
		print(tree)
		x=0
		parent=-1
		while x<len(tree):
			print("Loop Cycle Begins")
			print("Parent: {}".format(parent))
			if parent in nodeDict and len(nodeDict[parent]) == 2: 
				print("Parent nodes length == {}....Changing parent".format(len(nodeDict[parent])))
				parent= parentDict[parent]
			print("New Parent After Loop: {}".format(parent))
			
			y=x+1
			print("X and Y position: {} {}".format(x,y))
			A=tree[x]
			B=tree[y]
			print("A and B value: {} {}".format(A,B))
			
			if(A in nodeSet and B in nodeSet):
				print()
				print("IF A AND B")
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				parentDict[A] = parent
				try:
					nodeDict[parent].append(A)
				except:
					nodeDict[parent] = [A]
				print(nodeDict)
				parentDict[B] = A
				try:
					nodeDict[A].append(B)
				except:
					nodeDict[A] = [B]
				parent = B
				x=y+1
				print("IF A AND B ENDS")
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				print()
				continue
			if(A in nodeSet and B == '0'):
				print()
				print("IF A AND 0")
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				
				try:
					nodeDict[parent].append(A)
				except:
					nodeDict[parent] = [A]

				parentDict[A] = parent

				try:
					nodeDict[A].append(0)
				except:
					nodeDict[A] = [0]
				
				print("Appended A:{} anb B:{}".format(A,B))
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Moving Onto the Next character......")
				y+=1
				B=tree[y]
				print("New Y:{} and new B:{}".format(y,B))
				print("A AND B now Become: {} {}".format(A,B))
				if(B == '0'):
					nodeDict[A].append(0)
					parent = parentDict[A]
				else:
					print("here")
					parentDict[B] = A
					print("A B: {} {}".format(A,B))
					nodeDict[A].append(B)
					print(nodeDict)
					parent=B
				x=y+1
				print("IF A AND 0 ENDS")
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				print()
				continue
			if(A =='0' and B in nodeSet):
				print()
				print('IF 0 AND B')
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				try:
					nodeDict[parent].append(0)
				except:
					nodeDict[parent] = [0]

				print("Middle of \" IF O AND B\"")
				print(nodeDict)
				while len(nodeDict[parent]) == 2: 
					parent=parentDict[parent]
				
				print("HERE...parent and B: {} {}".format(parent,B))
				try:
					nodeDict[parent].append(B)	
				except:
					nodeDict[parent] = [B]
				parentDict[B] = parent
				parent=B
				x=y+1
				print('IF 0 AND B ENDS')
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				print()
				continue
			if(A=='0' and B =='0'):
				print()
				print("IF 0 AND 0")
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				nodeDict[parent] = [0,0]
				x=y+1
				parent=parentDict[parent]
				print("IF 0 AND 0 ENDS")
				print("Node Dict: {}".format(nodeDict))
				print("Parents Dict: {}".format(parentDict))
				print("Parent: {}".format(parent))
				print()
				continue
		print(nodeDict)
		print(parentDict)
		
		root = nodeDict[-1][0]
		nodeDict[root].insert(0,0)
		for node in parentDict:
			parent = parentDict[node]
			if parent == -1:
				continue
			parentGraphValue = nodeDict[parent][0]
			if(node == nodeDict[parent][1]):
				nodeDict[node].insert(0,parentGraphValue-1)
			else:
				nodeDict[node].insert(0,parentGraphValue+1)
				
		print(nodeDict)
		C=[]
		ExtractColumn(nodeDict,root,column,C)
		print(C)
		C.sort()
		print(C)
		if len(C) == 0:
			print("Common Gandhijee!")
		else:
			for x in C:
				print(x,end='')
			print()
			
def calculateLevels(node,nodeDict,levelDict,currentLevel):
	# print(node)
	children = nodeDict[node]
	# print(children)
	# print(levelDict)
	if (children[1] != 0):
		levelDict[children[1]]=currentLevel+1
		calculateLevels(children[1],nodeDict,levelDict,currentLevel+1)
	if (children[2]!=0):
		levelDict[children[2]]=currentLevel+1
		calculateLevels(children[2],nodeDict,levelDict,currentLevel+1)
	
def ExtractColumn(nodeDict,node,column,C):
	# print(node)
	nodeColumn = nodeDict[node][0]
	if nodeColumn == column:
		C.append(node)
	
	if(nodeDict[node][1] !=0):
		#Go Left
		ExtractColumn(nodeDict,nodeDict[node][1],column,C)
	if(nodeDict[node][2] != 0):
		#GO Right
		ExtractColumn(nodeDict,nodeDict[node][2],column,C)
		
if __name__ == "__main__": main_3()
