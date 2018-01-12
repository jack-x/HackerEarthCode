
def main():
	T=int(input())
	for case in range(0,T):
		inp=input().split(' ')
		N=int(inp[0])
		K=int(inp[1])
		
		friends = input().split(' ')
		#print("Friends|: {}".format(friends))
		friendStack=[]
		friendStack.append(0)
		friendsDeleted=-1
		x=0
		while x< len(friends) and friendsDeleted<=K:
			currentFriend = int(friends[x])
			top=friendStack[-1]
			while top <  currentFriend and friendsDeleted<K:
				friendStack.pop()
				friendsDeleted+=1
				if(len(friendStack) ==0):
					break
				top=friendStack[-1]
			friendStack.append(currentFriend)
			x+=1
		
		while x<len(friends):
			currentFriend=int(friends[x])
			friendStack.append(currentFriend)
			x+=1
		
		
		
		for x in friendStack:
			print(x,end=' ')
		print()


if __name__ == "__main__": main()