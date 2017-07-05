def main():
	T=int(input())
	for case in range(0,T):
		i = input().split(' ')
		N=int(i[0])
		M = int(i[1])
		integers=input().split(' ')
		count=0
		d=dict()
		for i in integers:
			count+=1
			if(count<=N):
				if i in d:
					d[i]+=1
				else:
					d[i]=1
			else:
				if i in d:
					print("YES")
					# d[i]-=1
					# if d[i] == 0:
						# del d[i]
				else:
					print("NO")
					d[i]=1
	

if __name__ == "__main__": main()
