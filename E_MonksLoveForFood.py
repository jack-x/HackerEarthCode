Q = int(input())
stack=[]
for x in range(0,Q):
	query = input()
	if(len(query) == 1):
		if(len(stack) == 0):
			print("No Food")
		else:
			print(stack.pop())
	else:
		arr = query.split()
		stack.append(int(arr[1]))
		
