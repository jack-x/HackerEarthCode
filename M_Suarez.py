
def main():
	N=int(input())
	rangeArray=[]
	for line in range(0,N):
		i = input().split(' ')
		rangeArray.append([int(i[0]),int(i[1])])
	
	for x in range(0,len(rangeArray)-1):
			for y in range(x,len(rangeArray)):
				lenone=rangeArray[x][1] - rangeArray[x][0]
				lentwo=rangeArray[y][1] - rangeArray[y][0]
				if(lenone > lentwo):
					temp = rangeArray[x]
					rangeArray[x] = rangeArray[y]
					rangeArray[y] = temp
	
	
	Q=int(input())
	
	for case in range(0,Q):
		i = input().split(' ')
		K=int(i[0])
		X=int(i[1])
		
		k=0
		leftOvers=len(rangeArray)
		flag=0
		for x in rangeArray:
			if X >= x[0] and X <= x[1]:
				k+=1
				leftOvers-=1
				if(k==K):
					print(x[1] - x[0] +1)
					flag=1
					break
				if(leftOvers<K-k):
					break
		if(flag==0):
			print("-1")
		

if __name__ == "__main__": main()