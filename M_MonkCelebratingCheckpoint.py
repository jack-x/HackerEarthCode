
def main():
	inp = input().split(' ')
	N=int(inp[0])
	X= int(inp[1])
	K=int(inp[2])
	Narr=input().split(' ')
	arr=[]
	for x in Narr:
		arr.append(int(x))
	arr.sort(reverse=True)
	#print(arr)
	
	GrandTotal=0
	
	for x in range(0,X):
		arr[x] = arr[x]+1
	
	for x in range(0,N):
		ele=arr[x]
		TotalFunction=0
		for y in range(x+1,N):
			#print("ele and Y: [{},{}]".format(ele,arr[y]))
			
			diff=abs(ele-arr[y])
			#print("Diff:{}".format(diff))
			
			TotalSubArrays=CalculateTotalSubArrays((y-x)-1)
			#print("TotalSubArrays:{}".format(TotalSubArrays))
			TotalFunction= TotalFunction + diff * TotalSubArrays
			
		GrandTotal = GrandTotal + TotalFunction
	
	print(GrandTotal)


def CalculateTotalSubArrays(y):
	if y == 0: return 1
	if y==1: return 2
	else:
		sum =0
		import math
		for x in range(1,y):
			sum = sum + ncr(y,x)
		
		return sum

		
import operator as op
from functools import reduce
import math

def ncr(n, r):
    #print("[N,R]: [{},{}]".format(n,r))
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom



if __name__ == "__main__": main()