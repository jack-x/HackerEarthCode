def main():
	T=int(input())
	for case in range(0,T):
		i = input().split(' ')
		N=int(i[0])
		X=int(i[1])
		numbers=input().split(' ')
		n=[]
		for x in numbers:
			if x != '':
				n.append(int(x))
		s = set(n)
		if (len(s) == X):
			print("Good")
		elif len(s) >=X:
			print("Average")
		else:
			print("Bad")

if __name__ == "__main__": main()
