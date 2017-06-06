
def main():
	one = input().split(' ')
	
	N=int(one[0])
	K=int(one[1])
	
	two = input().split(' ')
	
	differenceStack=[]
	differenceDict=dict()
	for n in two:
		num = int(n)
		if(num >= K):
			continue
		try:
			randomnumber=differenceDict[num]
			print("YES")
			return
		except:
			difference = K - num
			differenceDict[difference] = num
	
	print("NO")
		

if __name__ == "__main__": main()
