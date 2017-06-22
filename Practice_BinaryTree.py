

class Tree(object):
	
	def __init__(self):
		self.left=None
		self.right=None
		self.data=None
		self.leftDepth=0
		self.rightDepth=0

def main():
	inp=input().split(' ')
	T=int(inp[0])
	X=int(inp[1])
	
	root = Tree()
	root.data = X
	
	parentNode = root
	
	for x in range(0,T-1):
		path=input()
		value=int(input())
		
		#findingNode Using path
		
		parent = root
		#This is not the ideal way to fill a binary tree, although this is the way we do it as per the question
		
		for x in path:
			if(x == 'L'):
				if (parent.left == None):
					parent.left = Tree()
					
				node = parent.left
			elif(x=='R'):
				if (parent.right == None):
					parent.right = Tree()
					
				node=parent.right
			parent = node
		
		parent.data = value
	
	depthEachNode(root)
	print(Diameter(root) + 1)

def Diameter(node):
	diameter = node.leftDepth + node.rightDepth
	if(node.left is not None):
		leftnodeDiameter = Diameter(node.left)
	else:
		leftnodeDiameter = -1
	if(node.right is not None):
		rightnodeDiameter= Diameter(node.right)
	else:
		rightnodeDiameter = -1
	if(diameter > leftnodeDiameter and diameter >rightnodeDiameter):
		return diameter
	elif(leftnodeDiameter> diameter and leftnodeDiameter>rightnodeDiameter):
		return leftnodeDiameter
	else:
		return rightnodeDiameter
	
	
def depthEachNode(node):

		if(node.left is None):
			node.leftDepth = 0
		else:
			node.leftDepth = depthEachNode(node.left)
		if(node.right is None):
			node.rightDepth = 0
		else:
			node.rightDepth = depthEachNode(node.right)
		
		if(node.leftDepth > node.rightDepth):
			return node.leftDepth+1
		else:
			return node.rightDepth+1
		
		
def TreeTraversal(root):
	if(root is None):
		return
	print("Node.Data: {}".format(root.data))
	print("Left Depth: {}, Right Depth: {}".format(root.leftDepth,root.rightDepth))
	print("Left Of the Node")
	TreeTraversal(root.left)
	print("Right of the Node")
	TreeTraversal(root.right)
	return

	
if __name__ == "__main__": main()
