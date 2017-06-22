

def main():
	inp = input().split(' ')
	
	N=int(inp[0])
	Q=int(inp[1])
	
	tree = dict()
	tree[1] = [0,'',-1,-1]
	for x in range(0,N-1):
		node = input().split(' ')
		parent=int(node[0])
		nodeValue=int(node[1])
		
		if(node[2] == 'R'):
			nodeArray=[parent,'R',-1,-1]
			tree[parent][3] = nodeValue
		else:
			nodeArray=[parent,'L',-1,-1]
			tree[parent][2] = nodeValue
		
		tree[nodeValue] = nodeArray
		
	#print(tree)
	for x in range(0,Q):
		node=int(input())
		n=node
		path =''
		parent = tree[node][0]
		while node != 1:
			path = tree[node][1]+ path
			node=parent
			parent = tree[node][0]
		
		#print("Full path for node {} = {}".format(n,path))
		node = 1
		pathTraversed = ''
		for edge in path:
			if edge == 'L':
				node = tree[node][3]
			else:
				node = tree[node][2]
			pathTraversed = edge + pathTraversed
			if node == -1 :
				break
		
		#print(tree[node])		
		print(node)
		


if __name__ == "__main__": main()
