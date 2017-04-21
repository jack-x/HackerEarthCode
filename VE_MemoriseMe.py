def main():
	N= int(input())
	Ns = input().split(' ')
	Q = int(input())
	
	d = dict()
	
	for n in Ns:
		if n in d:
			d[n]+=1
		else:
			d[n]=1
			
	for x in range(0,Q):
		num = input()
		if num in d:
			print(d[num])
		else:
			print("NOT PRESENT")




if __name__ == "__main__": main()
