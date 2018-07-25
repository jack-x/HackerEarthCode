def main():
	i = input().split(' ')
	N = int(i[0])
	T = int(i[1])
	names = ['']*N
	quotient = [0]*N
	for x in range(0,N):
		i = input().split(' ')
		names[x] = i[0]
		quotient[x] = int(i[1])
		
		
	for x in range(0,N):
		for y in range(0,N-1):
			if quotient[y] < quotient[y+1]:
				temp = quotient[y]
				quotient[y] = quotient[y+1]
				quotient[y+1] = temp
				
				temp = names[y]
				names[y] = names[y+1]
				names[y+1] = temp
	
	for x in range(0,N):
		for y in range(0,N-1):
			if quotient[y] == quotient[y+1]:
				if names[y] > names[y+1]:
					temp = names[y]
					names[y] = names[y+1]
					names[y+1] = temp
	
	
	for x in range(0,T):
		print(names[x])
	
	
	
main()
