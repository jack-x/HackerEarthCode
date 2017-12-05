
def main():
	n=int(input())
	grid=[]
	gridRow=[]
	
	for x in range(0,n):
		p=input().split(' ')
		for y in p:
			gridRow.append(int(y))
		grid.append(list(gridRow))
		
		gridRow=list()
	nums=0
	for x in range(1,n-1):
		for y in range(1,n-1):
			sum = grid[x-1][y] + grid[x+1][y] + grid[x][y-1] + grid[x][y+1]
			if isPrime(sum):
				nums+=1
	#firstCorner
	sum=grid[1][0] + grid[0][1]
	if isPrime(sum):
		nums+=1
	#secondCorner
	sum=grid[0][n-2]+grid[1][n-1]
	if isPrime(sum):
		nums+=1
	#ThirdCorner
	sum = grid[n-2][0] + grid[n-1][1]
	if isPrime(sum):
		nums+=1
	#FourthCorner
	sum = grid[n-2][n-1] + grid[n-1][n-2]
	if isPrime(sum):
		nums+=1
	#firstRow
	x=0
	for y in range(1,n-1):
		sum = grid[x][y-1] + grid[x][y+1] + grid[x+1][y]
		if isPrime(sum):
			nums+=1
	#secondRow
	y=0
	for x in range(1,n-1):
		sum = grid[x-1][y] + grid[x+1][y] + grid[x][y+1]
		if isPrime(sum):
			nums+=1
	#thirdRow
	x=n-1
	for y in range(1,n-1):
		sum = grid[x][y-1] + grid[x][y+1] + grid[x-1][y]
		if isPrime(sum):
			nums+=1
	#FourthRow
	y=n-1
	for x in range(1,n-1):
		sum = grid[x-1][y] + grid[x+1][y] + grid[x][y-1]
		if isPrime(sum):
			nums+=1
	print(nums)

from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))	

if __name__ == '__main__': main()
