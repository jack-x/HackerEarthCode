def main():
	import math
	K=int(input())
	s = input()
	
	distinctCoinDict = dict()
	for x in 'abcdefghijklmnopqrstuvwxyz':
		distinctCoinDict[x] = 0
	
	distinctCoinPosition = [dict(distinctCoinDict)]
	distinctsoFar=[]
	distinct=0
	distinctCountEveryStep = [0]
	for x in range(0,len(s)):
		distinctCoinDict[s[x]] +=1
		
		if s[x] in distinctsoFar:
			distinctCountEveryStep.append(distinct)
		else:
			distinctsoFar.append(s[x])
			distinct+=1
			distinctCountEveryStep.append(distinct)
		
		distinctCoinPosition.append(dict(distinctCoinDict))
	
	pairsOfij = 0
	if K == 1:
		# pairsOfij+=len(s)
		prev=s[0]
		counter=1
		for x in s[1:]:
			if x == prev:
				counter+=1
			else:
				prev = x
				pairsOfij+=int(counter*(counter+1)/2)
				counter=1
		pairsOfij+=int(counter*(counter+1)/2)
	else:
		for i in range(1,len(s)+1):
			j= i + K -1
			if j<=len(s):
				first = dict(distinctCoinPosition[i-1])
				second = dict(distinctCoinPosition[j])
				differenceDict = dict()
				distinctCoins=0
				for x in 'abcdefghijklmnopqrstuvwxyz':
					differenceDict[x] = second[x] - first[x]
					if (differenceDict[x]) > 0:
						# print("Here")
						distinctCoins+=1
				if distinctCoins == K:
					pairsOfij+=1
				
				j+=1
				
				while j < (len(s)+1):
					AddedChar = s[j-1]
					# print("AddedChar:{}".format(AddedChar))
					if differenceDict[AddedChar] == 0:
						distinctCoins+=1
						differenceDict[AddedChar] = 1
					else:
						differenceDict[AddedChar]+=1
					if distinctCoins == K:
						pairsOfij+=1
					if distinctCoins > K:
						# print("Distinct Coins are now {}. Breaking".format(distinctCoins))
						break
					j+=1
			else:
				break
	print(pairsOfij)
			
			
	

if __name__ == "__main__": main()
