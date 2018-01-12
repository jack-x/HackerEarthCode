def main2():
		i = input().split(' ')
		N=int(i[0])
		Q=int(i[1])
		f = input().split(' ')
		fighters = [None]
		fights = dict()
		counter=1
		indexList = []
		for x in f:
			fighters.append(int(x))
			fights[counter] = 0
			indexList.append(counter)
			counter+=1
			
		if (len(fighters) == 2):
			fights[1] = 0
		elif((len(fighters)+1)%2==0):
			TotalFights = 0
			while TotalFights < (N-1):
				newIndexList = []
				for x in range(0,len(indexList),2):
					f1 = indexList[x]
					f2 = indexList[x+1]
					fights[f1] +=1
					fights[f2] +=1
					TotalFights+=1
					if(fighters[f2]>fighters[f1]):
						fighters[f1] = -1
						newIndexList.append(f2)
					else:
						fighters[f2] = -1
						newIndexList.append(f1)
				indexList=list(newIndexList)		
		
						
		
		else:
			TotalFights = 0
			while TotalFights < (N-2):
				newIndexList = []
				for x in range(0,len(indexList)-1,2):
					f1 = indexList[x]
					f2 = indexList[x+1]
					fights[f1] +=1
					fights[f2] +=1
					TotalFights+=1
					if(fighters[f2]>fighters[f1]):
						fighters[f1] = -1
						newIndexList.append(f2)
					else:
						fighters[f2] = -1
						newIndexList.append(f1)
						
				indexList = list(newIndexList)
			
			newIndexList.append(fighters[-1])
			f1=newIndexList[0]
			f2=newIndexList[1]
			fights[f1]+=1
			fights[f2]+=1
			
		for case in range(0,Q):
			i = int(input())
			print(fights[i])

def main():
		i = input().split(' ')
		N=int(i[0])
		Q=int(i[1])
		f = input().split(' ')
		fighters = [None]
		for x in f:
			fighters.append(int(x))
			
		fights = dict()

		flag=0
		print(fighters)
		if (len(fighters) == 2):
			fights[1] = 0
		else:	
			while flag ==0:
				print("Inside While")
				f1=-1
				f2=-1
				for x in range(1,len(fighters)):
					print("Fighter index: {}".format(x))
					
					if fighters[x] == -1:
						print("Inside fighter -1 check")
						input()
						continue
						
					if (f1 == -1):
						print("Inside F1 IF")
						f1 = x
						input()
						continue
					if(f2 == -1):
						print("Inside F2 IF")
						f2 = x
						if f1 in fights:
								fights[f1] +=1
						else:
								fights[f1] = 1
						if f2 in fights:
								fights[f2] +=1
						else:
								fights[f2] = 1
						if(fighters[f2]>fighters[f1]):
							fighters[f1] = -1
						else:
							fighters[f2] = -1
						
						f1 = -1
						f2 = -1
						print("F2 IF completed")
						print(fights)
						print(fighters)
						input()
				
			
				fcount = 0
				for y in range(1,len(fighters)):
					x = fighters[y]
					if x != -1:
						fcount+=1
				if fcount == 1:
					flag =1
		
						
			
		for case in range(0,Q):
			i = int(input())
			print(fights[i])




if __name__ == '__main__': main2()