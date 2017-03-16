

def main():
	N = int(input())
	array1 = input().split()
	array2 = input().split()
	
	array3=[]
	for x in range(0,N):
		array3.append(int(array1[x]) + int(array2[x]))
	
	for x in array3:
		print(x,end=' ')



if __name__ == "__main__" : main()
