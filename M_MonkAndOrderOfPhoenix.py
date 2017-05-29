GenerateFlag=1
 
def main():
	N=int(input())
	VoldemortArmy=[]
	HarryWandStack=[]
	for l in range(0,N):
		line = input().split(' ')
		X=line.pop(0)
		
		ArmyRow=[]
		
		for height in line:
			ArmyRow.append(int(height))
		
		VoldemortArmy.append(ArmyRow)
	
	GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
	
	Q=int(input())
	
	for op in range(0,Q):
		operation = input().split(' ')
		
		if(operation[0] == '1'):
			k=int(operation[1])
			h=int(operation[2])
			VoldemortAddFighter(VoldemortArmy,k,h,HarryWandStack)
		
		if(operation[0]=='0'):
			k=int(operation[1])
			VoldemortRemoveFighter(VoldemortArmy,k,HarryWandStack)
		
		if(operation[0]=='2'):
			#print("Harry Wand Stack: {}".format(HarryWandStack))
			global GenerateFlag
			if(GenerateFlag == 1):
				GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
				GenerateFlag=0
			if(len(HarryWandStack) == N):
				print("YES")
			else:
				print('NO')
		
		
def VoldemortAddFighter(VoldemortArmy,k,h,HarryWandStack):
	VoldemortArmy[k-1].append(h)
	global GenerateFlag
	if(GenerateFlag==1):
		return
	if(len(HarryWandStack) == len(VoldemortArmy)):
		GenerateFlag=0
	else:
		GenerateFlag=1
	# if(k==1):
		# if(h<HarryWandStack[0]):
			# GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
			# GenerateFlag=0
	# elif(len(HarryWandStack) == k-1 and HarryWandStack[len(HarryWandStack) -1] < h):
		#GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k-1)
		# GenerateFlag=1
		
# def VoldemortAddFighter(VoldemortArmy,k,h,HarryWandStack):
	# VoldemortArmy[k-1].append(h)
	# if(k==1):
		# if(h<HarryWandStack[0]):
			# GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
	# if(len(HarryWandStack) == k and HarryWandStack[len(HarryWandStack) - 1] > h):
		# GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k-1)
	# elif(len(HarryWandStack) == k-1 and HarryWandStack[len(HarryWandStack) -1] < h):
		# GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k-1)
	
def VoldemortRemoveFighter(VoldemortArmy,k,HarryWandStack):
	RemovedFighter = VoldemortArmy[k-1].pop()
	global GenerateFlag
	if(GenerateFlag==1):
		return
	try:	
		if(HarryWandStack[k-1] == RemovedFighter):
		#GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k-1)
			GenerateFlag=1
	except:
		GenerateFlag=0
			
# def VoldemortRemoveFighter(VoldemortArmy,k,HarryWandStack):
	# RemovedFighter = VoldemortArmy[k-1].pop()
	# if(len(HarryWandStack) >= k):
		# if(HarryWandStack[k-1] == RemovedFighter):
			# GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k-1)
 
def GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k=0):
	del HarryWandStack[k:]
	#Emptying the HarryWandStack For calculation after every "worthy" modification
	#This does not create a new Array and modifies the HarryWandStack Array in place
	
	#Find the Minimum in the first row
	
	if(k==0):
		FirstRowMin=min(VoldemortArmy[0])
		HarryWandStack.append(FirstRowMin)
		k=1
	else:
		FirstRowMin=HarryWandStack[k-1]
	
	for row in range(k,len(VoldemortArmy)):
		
		ArmyRow=VoldemortArmy[row]
		if(ArmyRow[len(ArmyRow)-1] < FirstRowMin):
			break
		ArmyRowHeight=0
		#Using Binary Search Here
		x=0
		y=len(ArmyRow)-1
		
		mid= (x+y)/2
		
		while ((y-x)>1):
			mid=int((x+y)/2)
			ArmyRowHeight=ArmyRow[mid]
			if(ArmyRowHeight>FirstRowMin):
				y=mid
			else:
				x=mid
		
		# if(ArmyRow[x]>FirstRowMin):
			# FirstRowMin=ArmyRow[x]
			# HarryWandStack.append(FirstRowMin)
			# continue
		# elif(ArmyRow[y]>FirstRowMin):
			# FirstRowMin=ArmyRow[y]
			# HarryWandStack.append(FirstRowMin)
			# continue
		# else:
			# break
		if(ArmyRow[y]>FirstRowMin):
			FirstRowMin=ArmyRow[y]
			HarryWandStack.append(FirstRowMin)
			continue
		else:
			break	
	#loop And Function End Here
	
	
def HarrySpecialWandCheck(VoldemortArmy):
	#Find the Minimum in the first row
	FirstRowMin=min(VoldemortArmy[0])
	
	prevRowHeight = FirstRowMin
	for row in range(1,len(VoldemortArmy)):
		ArmyRow=VoldemortArmy[row]
		ArmyRowHeight=0
		#Using Binary Search Here
		x=0
		y=len(ArmyRow)-1
		
		mid= (x+y)/2
		
		while ((y-x)>1):
			mid=int((x+y)/2)
			ArmyRowHeight=ArmyRow[mid]
			if(ArmyRowHeight>FirstRowMin):
				y=mid
			else:
				x=mid
		
		if(ArmyRow[x]>FirstRowMin):
			FirstRowMin=ArmyRow[x]
			continue
		elif(ArmyRow[y]>FirstRowMin):
			FirstRowMin=ArmyRow[y]
			continue
		
		return "NO"
		
	return "YES"
		
			
 
 
if __name__ == "__main__": main()
