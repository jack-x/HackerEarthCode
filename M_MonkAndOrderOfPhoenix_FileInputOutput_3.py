
GenerateFlag=1

def main():
	f=open("input.txt",'r')
	ff=open("output.txt",'w')
	
	N=int(f.readline())
	VoldemortArmy=[]
	HarryWandStack=[]
	print("N from file: {}".format(N))
	
	result=""
	for l in range(0,N):
		line = f.readline().split(' ')
		X=line.pop(0)
		
		ArmyRow=[]
		
		for height in line:
			ArmyRow.append(int(height))
		
		VoldemortArmy.append(ArmyRow)
	
	GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
	
	#Checking if the Army inputs are correct
	#print(VoldemortArmy)
	
	Q=int(f.readline())
	print("Q from file: {}".format(Q))
	prev=2
	for op in range(0,Q):
		operation = (f.readline()).split(' ')
		o0=int(operation[0])
		if(o0 == 1):
			k=int(operation[1])
			h=int(operation[2])
			VoldemortAddFighter(VoldemortArmy,k,h,HarryWandStack)
			
			
		if(o0==0):
			k=int(operation[1])
			VoldemortRemoveFighter(VoldemortArmy,k,HarryWandStack)
			
			
		if(o0==2):
			print("about to write to harry. Operation: {} || Operation Count: {}".format(operation,op))
			#ff.write(HarrySpecialWandCheck((VoldemortArmy))+"\n")
			#result=''.join([result,HarrySpecialWandCheck(VoldemortArmy,ff)])
			global GenerateFlag
			if(GenerateFlag == 1):
				GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
				GenerateFlag=0
			if(len(HarryWandStack) == N):
				result=''.join([result,'YES'])
			else:
				result=''.join([result,'NO'])
			result=''.join([result,'\n'])
			prev=2
			
	ff.write(result)
	f.close()
	ff.close()
	
# def VoldemortAddFighter(VoldemortArmy,k,h):
	# VoldemortArmy[k-1].append(h)
	
	
# def VoldemortRemoveFighter(VoldemortArmy,k):
	# VoldemortArmy[k-1].pop()

def VoldemortAddFighter(VoldemortArmy,k,h,HarryWandStack):
	VoldemortArmy[k-1].append(h)
	global GenerateFlag
	if(GenerateFlag==1):
		return
	if(len(HarryWandStack) == len(VoldemortArmy)):
		GenerateFlag=0
	else:
		GenerateFlag=1
		
	# elif(k==1):
		# if(h<HarryWandStack[0]):
			# GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
			# if(len(HarryWandStack)==1):
				# GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
				# GenerateFlag=0
	# elif(len(HarryWandStack) == k-1 and HarryWandStack[k-2] < h):
		# HarryWandStack.append(h)
		# GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k)
		# GenerateFlag=1
	
def VoldemortRemoveFighter(VoldemortArmy,k,HarryWandStack):
	RemovedFighter = VoldemortArmy[k-1].pop()
	global GenerateFlag
	if(GenerateFlag==1):
		return
	#if(len(HarryWandStack) >= k):
	if(HarryWandStack[k-1] == RemovedFighter):
		#GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k-1)
		GenerateFlag=1

def GenerateHarryWandStack(VoldemortArmy,HarryWandStack,k=0):
	del HarryWandStack[k:]
	#Emptying the HarryWandStack For calculation after every "worthy" modification
	#This does not create a new Array and modifies the HarryWandStack Array in place
	
	#Find the Minimum in the first 
	
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

def HarrySpecialWandCheck(VoldemortArmy,ff):
	#Find the Minimum in the first row
	
	#ff.write("Inside the Harry Special Wand Check Function\n")
	FirstRowMin=min(VoldemortArmy[0])
	
	for row in range(1,len(VoldemortArmy)):
		#ff.write("FirstRowMin: {}\n".format(FirstRowMin))
		ArmyRow=VoldemortArmy[row]
		ArmyRowHeight=0
		#Using Binary Search Here
		x=0
		y=len(ArmyRow)-1
		
		mid= (x+y)/2
		
		while ( (y-x)>1):
			mid=int((x+y)/2)
			#ff.write("Value of Mid: {}\n".format(mid))
			ArmyRowHeight=ArmyRow[mid]
			if(ArmyRowHeight>FirstRowMin):
				y=mid
			else:
				x=mid
		
		#ff.write("Row: {}\n".format(row))
		#ff.write("Row Min Greater than First Row Min: {}\n".format(ArmyRow[x]))
		#ff.write("Row Min Greater than First Row Min: {}\n".format(ArmyRow[y]))
		if(ArmyRow[x]>FirstRowMin):
			FirstRowMin=ArmyRow[x]
			continue
		else:
			FirstRowMin=ArmyRow[y]
			continue
		
		#ff.write("Printing NO\n\n")
		return "NO"
	#ff.write("Printing YES\n\n")	
	
	return "YES"
		

def main_3():		
	f=open("input_3.txt",'r')
	ff=open("output_3.txt",'w')
	
	N=int(f.readline())
	VoldemortArmy=[]
	HarryWandStack=[]
	
	AppendStack=[]
	PopStack=[]
	
	print("N from file: {}".format(N))
	
	result=""
	for l in range(0,N):
		line = f.readline().split(' ')
		X=line.pop(0)
		
		ArmyRow=[]
		
		for height in line:
			ArmyRow.append(int(height))
		
		VoldemortArmy.append(ArmyRow)
	GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
	
	global GenerateFlag
	GenerateFlag=0
	
	Q=int(f.readline())
	print("Q from file: {}".format(Q))
	prev=2
	for op in range(0,Q):
		operation = (f.readline()).split(' ')
		o0=int(operation[0])
		
		
		if(o0 == 1):
			k=int(operation[1])
			h=int(operation[2])
			if(len(PopStack) >=1 ):
				PopAll(VoldemortArmy,HarryWandStack,PopStack)
			AppendStack.append([k,h])
					
			
		if(o0==0):
			k=int(operation[1])
			if(len(AppendStack) >= 1):
				AppendAll(VoldemortArmy,HarryWandStack,AppendStack)
			PopStack.append(k)		
			
		if(o0==2):
			print("about to write to harry. Operation: {} || Operation Count: {}".format(operation,op))
			#ff.write(HarrySpecialWandCheck((VoldemortArmy))+"\n")
			#result=''.join([result,HarrySpecialWandCheck(VoldemortArmy,ff)])
			if(GenerateFlag == 1):
				GenerateHarryWandStack(VoldemortArmy,HarryWandStack)
				GenerateFlag=0
			if(len(HarryWandStack) == N):
				result=''.join([result,'YES'])
			else:
				result=''.join([result,'NO'])
			result=''.join([result,'\n'])
			prev=2
			
	ff.write(result)
	f.close()
	ff.close()
	
def PopAll(VoldemortArmy,HarryWandStack,PopStack):
	global GenerateFlag
	if(GenerateFlag==1):
		for row in PopStack:
			VoldemortArmy[row-1].pop()
		del PopStack[:]
		return
	else:
		for row in PopStack:
			RemovedFighter=VoldemortArmy[row-1].pop()
			if(GenerateFlag==0 and HarryWandStack[row-1] == RemovedFighter):
				GenerateFlag=1
		del PopStack[:]		
		return	
def AppendAll(VoldemortArmy,HarryWandStack,AppendStack):
	global GenerateFlag
	if(GenerateFlag==1):
		for pair in AppendStack:
			VoldemortArmy[pair[0]-1].append(pair[1])
		del AppendStack[:]
		return
	else:
		for pair in AppendStack:
			VoldemortArmy[pair[0]-1].append(pair[1])
			if(GenerateFlag==0):
				if((pair[0]-1) == 1 and pair[1] < HarryWandStack[0] and len(HarryWandStack) > 1):
					GenerateFlag = 1 
				elif (len(HarryWandStack) != len(VoldemortArmy)):
					GenerateFlag=1
		del AppendStack[:]
		return			
if __name__ == "__main__": main_3()