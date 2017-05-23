
def main():
	N=int(input())
	parenthesis=input().split(' ')
	
	stack=[]
	count=0
	MirrorCount=0
	balancedCount=[]
	balancedCount.append(0)
	
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
					MirrorCount+=2
					balancedCount.append(MirrorCount)
					#print("-1 * xx : {}".format(-1*xx))
					#print("y : {}".format(y))
					#print("Count Check After Balance Positive: {}".format(count))
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
