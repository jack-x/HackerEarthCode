
def main():
	T=int(input())
	for case in range(0,T):
		N=int(input())
		if N <= 2:
			print("-1")
		else:
			for y in range(N,-1,-1):
				if y%3 ==0:
					TheNumber=y
					break
			
			lowest = int(TheNumber/3)
			second = lowest*2
			third = TheNumber
			print("{} {} {}".format(lowest,second,third))
		
if __name__ == "__main__": main()
