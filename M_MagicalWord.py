
def main():
	nearestPrimeDict = returnDict()
	T=int(input())
	for x in range(0,T):
		n = int(input())
		t = input()
		newText=[]
		for y in t:
			val=ord(y)
			if y in nearestPrimeDict:
				newText.append(nearestPrimeDict[y])
			elif val<65:
				newText.append('C')
			elif (val>ord('Z') and val < 94):
				newText.append('Y')
			elif (val>93 and val<ord('a')):
				newText.append('a')
			elif val>ord('z'):
				newText.append('q')
			else:
				newText.append(y)
		for y in newText:
			print(y,end='')
		print()
		
def returnDict():
	text='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	primeText = []
	newText=[]
	for x in text:
		val = ord(x)
		if checkPrime(val):
			primeText.append(x)
		else:
			newText.append(x)
	
	nearPrime = dict()
	for x in newText:
		differenceList=[]
		for y in primeText:
			diff = abs(ord(y) - ord(x))
			differenceList.append([y,diff])
		
		min = differenceList[0]
		for y in range(1,len(differenceList)):
			currentDiff = differenceList[y]
			if (min[1] > currentDiff[1]):
				min = currentDiff
		
		nearPrime[x] = min[0]	
		
	return nearPrime	

def checkPrime(N):
	if (N%2 != 0):
		half = int((N-1)/2)
	else:
		return False
	for x in range(3,half):
		if N%x == 0:
			return False
	return True
	
if __name__ == "__main__": main()