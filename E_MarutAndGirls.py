

def main():
	M=int(input())
	qualities = set(input().split(' '))
	
	N = int(input())
	count=0
	for x in range(0,N):
		girl=set(input().split(' '))
		
		difference = qualities - girl
		if(len(difference) == 0):
			count+=1
		
	print(count)
if __name__ == "__main__": main()
