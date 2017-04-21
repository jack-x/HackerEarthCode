
def main():
	inp = input().split(' ')
	N = int(inp[0])
	Q = int(inp[1])
	BinaryQuery=input().split(' ')
	for x in range(0,Q):
		query = input().split(' ')
		if (query[0] == '0'):
			R = int(query[2])
			if(BinaryQuery[R-1]=='1'):
				print("ODD")
			else:
				print("EVEN")
		
		if(query[0] == '1'):
			X = int(query[1])
			if(BinaryQuery[X-1] == '1'):
				BinaryQuery[X-1] = '0'
			else:
				BinaryQuery[X-1] = '1'
			
	
if __name__ == "__main__": main()
