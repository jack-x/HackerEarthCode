
def main():
	T = int(input())
	for case in range(0,T):
		Friends=int(input())
		medals=[0,0,0]
		minMatches=0
		for friend in range(0,Friends):
			f = input().split(' ')
			medals[0]+=int(f[0])
			medals[1]+=int(f[1])
			medals[2]+=int(f[2])
			totalplayerMatches=int(f[0])+int(f[1])+int(f[2])
			if totalplayerMatches>minMatches:
				minMatches = totalplayerMatches
				
		matches = 0
		
		if medals[0] <= medals[1] and medals[0]<=medals[2]:
			matches+= medals[0]
			medals[1]-= medals[0]
			medals[2]-= medals[0]
			if medals[1] <= medals[2]:
				matches+=medals[1]
				medals[2]-=medals[1]
				matches+=medals[2]
			else:
				matches+=medals[2]
				medals[1]-=medals[2]
				matches+=medals[1]
		
		elif medals[1] <= medals[0] and medals[1]<=medals[2]:
			matches+= medals[1]
			medals[0]-= medals[1]
			medals[2]-= medals[1]
			if medals[0] <= medals[2]:
				matches+=medals[0]
				medals[2]-=medals[0]
				matches+=medals[2]
			else:
				matches+=medals[2]
				medals[0]-=medals[2]
				matches+=medals[0]
		
		elif medals[2] <= medals[1] and medals[2]<=medals[0]:
			matches+= medals[2]
			medals[1]-= medals[2]
			medals[0]-= medals[2]
			if medals[1] <= medals[0]:
				matches+=medals[1]
				medals[0]-=medals[1]
				matches+=medals[0]
			else:
				matches+=medals[0]
				medals[1]-=medals[0]
				matches+=medals[1]
		
		if minMatches>matches:
			print(minMatches)
		else:
			print(matches)
		
if __name__ == "__main__": main()
