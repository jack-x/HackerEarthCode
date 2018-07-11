def main():
	N = int(input())
	arr = [0]*N
	
	i = input().split(' ')
	distinctelements = []
	dcount=0
	for x in range(0,N):
		k = int(i[x])
		if k not in arr:
			dcount+=1
		arr[x] = k
		
	
	count=0
	for x in range(0,N-1):
		for y in range(x+1,N):
			dcountSubArray = distinctElementCount(arr[x:y+1],dcount)
			if dcountSubArray == dcount:
				count+= N-y
				break
	
	print(count)
		
			
			
			

def distinctElementCount(array,dcount):
	newarr= []
	count=0
	for x in array:
		if x in newarr:
			continue
		else:
			newarr.append(x)
			count+=1
			if count > dcount:
				return count
	return count

	
def main2():
	N = int(input())
	
	numberDict = dict()
	arr = [0]*N
		
	i = input().split(' ')
	
	distinctelements = []
	dcount = 0
	
	for x in range(0,N):
		K = int(i[x])
		if K not in numberDict:
			numberDict[K] = 1
		else:
			numberDict[K] +=1
		arr[x] = dict(numberDict)
		
		if K not in distinctelements:
			dcount +=1
			distinctelements.append(K)
		
	# print('Reaching Here No problem')
	# return	
	# print(arr)	
	# print(dcount)
	
	# print()
	if dcount == N:
		print(1)
		return
	
	subarrayCount = 0
	
	x=0
	#loop 1
	for y in range(x+dcount-1,N):
			d2 = arr[y]
			if len(d2) == dcount:
				subarrayCount = subarrayCount + (N -y)
				# print('**// Successfull Completion Loop 1')
				# print(d2)
				# print(subarrayCount)
				# print('*****')
				# print()
				break
			
	
	#Loop2
	prev = 1 + dcount -1 
	for x in range(1,N-dcount+1):
		for y in range(prev,N):
			d1 = dict(arr[x-1])
			d2 = dict(arr[y])
			
			for a in d1.keys():
				d2[a] -= d1[a]
				if d2[a] == 0:
					del d2[a]
			
			if len(d2) == dcount:
				subarrayCount = subarrayCount + (N-y)
				
				# print('**// Successfull Completion Loop 2')
				# print(d2)
				# print(subarrayCount)
				# print('*****')
				prev = y
				break
			
	print(subarrayCount)
	
def main3():
	N = int(input())
	arr = [0]*N
	i = input().split(' ')
	
	distinctElements = [-1]*N
	pointer = 0
	dcount = 0
	
	for x in range(0,N):
		k = int(i[x])
		if k not in distinctElements:
			distinctElements[pointer] = k
			pointer += 1
			dcount+=1
		
	
			
	
	
main2()

















