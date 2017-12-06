
def main():
	checkpoints = int(input())
	x = input().split(' ')
	y = input().split(' ')
	
	diffx = []
	diffy = []
	
	for a in range(0,checkpoints-1):
		diffx.append(abs(int(x[a]) - int(x[a+1])))
		diffy.append(abs(int(y[a]) - int(y[a+1])))
	
	diffx.sort()
	diffy.sort()
	
	a = diffx[-1]
	b= diffy[-1]
	
	if a>b:
		print("Dom")
		print(a)
	else:
		print('Brian')
		print(b)
if __name__ =="__main__": main()
