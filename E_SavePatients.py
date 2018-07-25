def main():
	N=int(input())
	
	s = input().split(' ')
	s2 = input().split(' ')
	
	vaccine = [0]*N
	patients= [0]*N
	
	for x in range(0,N):
		vaccine[x] = int(s[x])
		patients[x] = int(s2[x])
	
	vaccine.sort()
	patients.sort()
	
	count=0
	for x in range(0,N):
		if vaccine[x] > patients[x]:
			count+=1
		
	if count != N:
		print('No')
	else:
		print('Yes')
	
main()
