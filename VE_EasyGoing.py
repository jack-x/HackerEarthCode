def main():
	T = int(input())
	for case in range(0,T):
		s = input().split(' ')
		
		N = int(s[0])
		M = int(s[1])
		
		s = input().split(' ')
		
		arr = [0]*N
		
		for x in range(0,N):
			arr[x] = int(s[x])
		
		arr.sort()
		
		elements = N - M
		sum1 = 0
		for x in range(N-1,N - elements - 1,-1):
			sum1 += arr[x]
		
		sum2=0
		for x in range(0,elements):
			sum2+=arr[x]

		print(sum1-sum2)
		
main()
