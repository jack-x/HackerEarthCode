
def main():
	N=int(input())
	for x in range(0,N):
		people = int(input())
		p = input().split(' ')
		pp=[]
		for y in p:
			pp.append(int(y))
		x = 0
		countries = 0
		flag=1
		while x < people:
			y=pp[x]
			if (x+y) > people:
				print("Invalid Data")
				flag=0
				break
			for P in pp[x:(x+y)]:
				if P!=y:
					print("Invalid Data")
					flag=0
					break
			if(flag==0):
				break
			countries+=1
			x=x+y
		if flag==1:
			print(countries)
		
if __name__=='__main__': main()
