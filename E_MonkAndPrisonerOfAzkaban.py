
def main_first():
	N = int(input())
	ar= input().split(' ')
	arr=[]
	for x in ar:
		arr.append(int(x))
		
	xstack=[None]*N
	ystack=[None]*N
	xystack=[]
	for X in range(0,N):
		num=arr[X]
		x = -1
		y = -1
		flag=0
		
		Y=X+1
		
		
		XX = X-1
		while XX > -1:
			if(arr[XX]> num):
				x=XX+1
				break
			else:
				if(ystack[XX] < Y):
					Y=ystack[XX]
				
				XX=xstack[XX] -1
				
		if(Y!=-1):
			while Y<N:
				if(arr[Y]> num):
					y=Y+1
					break
				Y+=1
		
		# for XX in range(X-1,-1,-1):
			# if(arr[XX] > num):
				# x=XX+1
				# break
		
		xstack.append(x)
		ystack.append(y)
		xystack.append(x+y)
	for a in range(0,N):
		print(xystack[a],end=' ')

def main_second():
	N = int(input())
	ar= input().split(' ')
	arr=[]
	for x in ar:
		arr.append(int(x))
		
	xstack=[None]*N
	ystack=[None]*N		
		
	#First filling the xstack
	for X in range(0,N):
		num=arr[X]
		x = -1	
		
		XX = X-1
		while XX > -1:
			if(arr[XX]> num):
				x=XX+1
				break
			elif(xstack[XX]==-1):
				x=-1
				break
			else:
				XX=xstack[XX] -1
		xstack[X]=x
	
	for Y in range(N-1,-1,-1):
		num=arr[Y]
		y=-1
		
		YY = Y+1
		while YY<N:
			if(arr[YY]>num):
				y=YY+1
				break
			else:
				#print(ystack)
				#print("YY = {}".format(YY))
				if(ystack[YY] == -1):
					y=-1
					break
				else:	YY=ystack[YY]-1

		ystack[Y] = y
		
	for a in range(0,N):
		print(xstack[a]+ystack[a],end=' ')	
		
if __name__ == "__main__": main_second()
