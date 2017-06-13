def main():
	T=int(input())
	jhool = set('littlejhool')
	for case in range(0,T):
		inp = input().split(' ')
		N = int(inp[0])
		K = int(inp[1])
		
		names = input().split(' ')
		
		matchDict= []
		
		for name in names:
			matchSet = set(name.lower())
			diff = jhool - matchSet
			matchDict.append([name,len(diff)])
		
		#Insertion Sort on matchDict
		
		for x in range(1,len(matchDict)):
			y=x
			while (y>0 and matchDict[y-1][1] < matchDict[y][1]):
				temp = matchDict[y-1]
				matchDict[y-1] = matchDict[y]
				matchDict[y] = temp
				y-=1
			
		for x in range(0,K):
			print(matchDict[x][0],end =' ')

		print()
		

def main_fileOut():
	T=int(input())
	jhool = set('littlejhool')
	f=open("output_matchmaker.txt",'w')
	for case in range(0,T):
		inp = input().split(' ')
		N = int(inp[0])
		K = int(inp[1])
		
		names = input().split(' ')
		
		matchDict= []
		
		for name in names:
			matchSet = set(name.lower())
			diff = jhool - matchSet
			matchDict.append([name,len(diff)])
		
		#Insertion Sort on matchDict
		
		for x in range(1,len(matchDict)):
			y=x
			while (y>0 and matchDict[y-1][1] < matchDict[y][1]):
				temp = matchDict[y-1]
				matchDict[y-1] = matchDict[y]
				matchDict[y] = temp
				y-=1
			
		print(matchDict)	
		f.write(str(matchDict))
		f.write("\n")
		
		for x in range(0,K):
			print(matchDict[x][0],end =' ')
			f.write(str(matchDict[x][0]))
			f.write(' ')
		f.write('\n')
		f.close()
		print()
	
		
if __name__ == "__main__": main()

