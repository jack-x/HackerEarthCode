
def main():
	N=int(input())
	
	for num in range(0,N):
		string = input()
		arr = []
		flag=0
		for s in string:
			if s in arr:
				print("Yes")
				flag=1
				break
			else:
				arr.append(s)
		
		if flag==0:
			print("No")
		
if __name__ == "__main__" : main()
