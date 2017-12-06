
def main():
	S=int(input())
	i = input().split(' ')
	x = []
	for y in i:
		x.append(int(y))
	
	x.sort()
	
	deleted=0
	commands=[]
	for y in x:
		commands.append(y-deleted)
		deleted+=1
	
	for y in commands:
		print(y,end=' ')

if __name__ == '__main__': main()
