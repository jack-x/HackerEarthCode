class Node:
	def __init__(self,v):
		self.value=v
		self.left=None
		self.right=None
		
def main():
	N=int(input())
	numbers = input().split(' ')
	
	root = Node(int(numbers[0]))
	
	for x in numbers[1:]:
		InsertBSTNoRecursion(root,int(x))
	
	Range = input().split(' ')
	
	a = int(Range[0])
	b = int(Range[1])
	
	if(a>b):
		temp = b
		b=a
		a=temp
	
	medianNode= findMedianNode(root,a,b)
	#print(medianNode.value)
	
	pathNodeValues = FullPath(medianNode,a,b)
	
	print(max(pathNodeValues))
	
def FullPath(node,a,b):
		import copy
		nodeBackup = node
		path=[node.value]
		LeftRoot = node
		while LeftRoot.value !=a :
			path.append(LeftRoot.value)
			if a < LeftRoot.value:
				LeftRoot = LeftRoot.left
				if LeftRoot.value == a:
					path.append(LeftRoot.value)
					break
			else:
				LeftRoot = LeftRoot.right
				if LeftRoot.value == a:
					path.append(LeftRoot.value)
					break
		RightRoot = node
		while RightRoot.value !=b :
			path.append(RightRoot.value)
			if b < RightRoot.value:
				RightRoot = RightRoot.left
				if RightRoot.value == b:
					path.append(b)
					break
			else:
				RightRoot = RightRoot.right
				if RightRoot.value == b:
					path.append(b)
					break
		return path
			
def findMedianNode(node,a,b):
	while True:
		if node.value >= a and node.value <= b:
			return node
		elif node.value > b:
			node = node.left
		elif node.value<a:
			node = node.right
def printBST_InOrder(node):
	if node.left != None:
		printBST_InOrder(node.left)
	print(node.value,end = ' ')
	if node.right != None:
		printBST_InOrder(node.right)
	
def InsertBSTNode(node,number):
	if number < node.value:
		if node.left == None:
			node.left = Node(number)
		else:
			InsertBSTNode(node.left,number)
	else:
		if node.right == None:
			node.right = Node(number)
		else:
			InsertBSTNode(node.right,number)
	
def InsertBSTNoRecursion(node,number):
		while True:
			if number < node.value:
				if node.left == None:
					node.left = Node(number)
					return
				else:
					node = node.left
					continue
			else:
				if node.right == None:
					node.right = Node(number)
					return
				else:
					node=node.right
					continue
if __name__ == "__main__": main()