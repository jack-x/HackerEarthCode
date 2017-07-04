class Node:
	def __init__(self,v):
		self.value=v
		self.left=None
		self.right=None

def main():
	N=int(input())
	numbers = input().split(' ')
	
	root = Node(int(numbers[0]))
	oldHeight = 1
	for n in numbers[1:]:
		newHeight = insertBSTnodeReturnHeightNoRecursion(root,int(n),1)
		if newHeight > oldHeight:
			oldHeight = newHeight
	
	print(oldHeight)

def insertBSTnodeReturnHeightNoRecursion(node,value,currentHeight):
		while node != None:
			if value <= node.value:
				if (node.left == None):
					node.left=Node(value)
					return currentHeight+1
				node = node.left
				currentHeight+=1
			else:
				if (node.right == None):
					node.right=Node(value)
					return currentHeight+1
				node = node.right
				currentHeight+=1

def insertBSTnodeReturnHeight(node,value,currentHeight):
	if value <= node.value:
		if node.left == None:
			node.left = Node(value)
			return currentHeight+1
		else:
			return insertBSTnodeReturnHeight(node.left,value,currentHeight+1)
	elif value > node.value:
		if node.right == None:
			node.right = Node(value)
			return currentHeight+1
		else:
			return insertBSTnodeReturnHeight(node.right,value,currentHeight+1)

def insertBSTnode(node,value):
	if value < node.value:
		if node.left == None:
			node.left = Node(value)
		else:
			insertBSTnode(node.left,value)
	elif value >= node.value:
		if node.right == None:
			node.right = Node(value)
		else:
			insertBSTnode(node.right,value)			

if __name__ == "__main__": main()
