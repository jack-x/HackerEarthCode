
def main():
	inp = input().split(' ')
	N=[]
	
	for x in inp[0]:
		N.append(x)
	K = int(inp[1])
	
	if K == 0:
		for x in N:
			print(x,end='')
	else:
		changed=0
		position=0
		while changed < K and position < len(N) :
			if N[position] == '9':
				position+=1
				continue
			N[position] = 9
			position+=1
			changed+=1
	
		for x in N:
			print(x,end='')
		
			
if __name__ == "__main__": main()
