
def main():
	N=int(input())
	numbers = input().split(' ')
	hashDict = dict()
	for number in numbers:
		num = int(number)

		hashValue = num ^ (sum_digits3(num))
		if hashValue in hashDict:
			hashDict[hashValue]+=1
		else:
			hashDict[hashValue]=1
	
	maxValue=[[-1,-1]]
	collisions = 0
	for x in hashDict.keys():
		if(hashDict[x] > 1):
			collisions+= hashDict[x] - 1
			
		if hashDict[x] > maxValue[0][1] :
			maxValue = []
			maxValue.append([x,hashDict[x]])
		elif hashDict[x] == maxValue[0][1]:
			maxValue.append([x,hashDict[x]])
	
	
	if collisions != 0:
		least = maxValue[0]
		for x in maxValue:
			if x[0] < least[0]:
				least = []
				least.append(x[0])
		print("{} {}".format(least[0],collisions))	
	else:
		
		maxx = maxValue[0]
		for x in maxValue:
			if x[0] > maxx[0]:
				maxx = []
				maxx.append(x[0])
		print("{} {}".format(maxx[0],collisions))	
		
		
def main_withPrint():
	N=int(input())
	numbers = input().split(' ')
	hashDict = dict()
	for number in numbers:
		num = int(number)

		hashValue = num ^ (sum_digits3(num))
		print("{} ^ {} = {}".format(num,sum_digits3(num),hashValue))
		if hashValue in hashDict:
			hashDict[hashValue]+=1
		else:
			hashDict[hashValue]=1
	
	print("HashValueDict: {}".format(hashDict))
	maxValue=[[-1,-1]]
	collisions = 0
	for x in hashDict.keys():
		if(hashDict[x] > 1):
			collisions+= hashDict[x] - 1
			
		if hashDict[x] > maxValue[0][1] :
			maxValue = []
			maxValue.append([x,hashDict[x]])
		elif hashDict[x] == maxValue[0][1]:
			maxValue.append([x,hashDict[x]])
	
	print("Max Value Array: {}".format(maxValue))
	
	if collisions != 0:
		least = maxValue[0]
		for x in maxValue:
			if x[0] < least[0]:
				least = []
				least.append(x[0])
		print("Least: {}".format(least))
		print("{} {}".format(least[0],collisions))	
	else:
		
		maxx = maxValue[0]
		for x in maxValue:
			if x[0] > maxx[0]:
				maxx = []
				maxx.append(x[0])
		print("Collisions are 0. Max: {}".format(maxx))
		print("{} {}".format(maxx[0],collisions))
		
def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
   
  
if __name__== "__main__": main()