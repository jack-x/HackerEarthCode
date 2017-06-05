
def main():
	N=int(input())
	d = dict()
	for x in range(0,N):
		inp = input().split(' ')
		d[int(inp[0])] = inp[1]
	
	q=int(input())
	for x in range(0,q):
		i = int(input())
		print(d[i])

if __name__ == '__main__' : main()
