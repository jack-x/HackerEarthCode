

def main():
	N = input()
	integers = input().split()
	ints = []
	for x in integers:
		ints.append(int(x))
	
	flag = 0
	
	
	if(len(ints) == 1):
		flag = 1
		if(ints[0] == 0):
			print("YES")
		else:
			print("NO")
			
	for x in range(len(ints)-2,-1,-1):
		if(ints[x]<ints[x+1]):
			print("NO")
			flag = 1
			break
		else:
			ints[x] = ints[x] - ints[x+1]
			ints[x+1] = 0
	
	if(flag != 1):
		flags =1
		for x in ints:
			if(x!=0):
				print("NO")
				flags=0
				break
		if (flags == 1):
			print("YES")
	#print(ints)

if __name__ == "__main__": main()