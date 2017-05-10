

def main():
	n = int(input())
	arr = []
	for x in range(0,n):
		rating = int(input())
		if (rating==0):
			arr.pop()
		else:
			arr.append(rating)
			
	sum=0
	for x in arr:
		sum+=x
	a
	print(sum)



if __name__ == "__main__": main()
