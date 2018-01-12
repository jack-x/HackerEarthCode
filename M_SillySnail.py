
def main():
	T=int(input())
	for case in range(0,T):
		relations=int(input())
		nodes=dict()
		for r in range(0,relations):
			relation = input().split(' ')
			nodes[int(relation[0])] = [int(relation[1]),int(relation[2])]
		
		#print(nodes)
		TreeTraversal(1,nodes)
		print()
		
def TreeTraversal(node,nodes):
	print(node, end=' ')
	if node in nodes:
		children= nodes[node]
	
		for child in children:
			if(child != 0):
				TreeTraversal(child,nodes)
		
	
if __name__ == '__main__': main()