
def main():
	N=int(input())
	parenthesis=input().split(' ')
	
	stack=[]
	#count represents the count of the current subarray that is going.
	count=0
	
	#Mirror count represents the count of the shortest subarray that is balanced one after the other
	#Example [2,3,4,-4,-3,-2] will give MirroredCount as 6.
	MirrorCount=0
	
	balancedCount=[]
	balancedCount.append(0) #Appending Zero in case there is no balanced array
	
	for x in parenthesis:
		xx = int(x)
		if xx > 0 :
			stack.append(xx)
			count+=1
			MirrorCount=0
			
		elif xx < 0:
			if(len(stack)>0):
				y = stack.pop()
				if((-1*xx) == y):
					count+=1
					
					#As soon as a negative number balances out a positive number, we give mirrored count +2
					#So the sequence of balanced arrays are added per 2 continuously
					MirrorCount+=2
					
					balancedCount.append(MirrorCount)
					
					if(len(stack)==0):
						balancedCount.append(count)
				
				else:
					count=0
					stack=[]
			else:
				count=0
				stack=[]
	#print(balancedCount)	
	print(max(balancedCount))
	
if __name__ == "__main__": main()
