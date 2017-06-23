def main_4():
	T=int(input())
	for x in range(0,T):
		soldiers=int(input())
		SuperiorDict=dict()
		hierarchy=dict()
		
		superiors=input().split(' ')
		soldier = 1
			
		for superior in superiors:

			if superior!='':
				if int(superior) in hierarchy:
					hierarchy[int(superior)].append(soldier)
				else:
					hierarchy[int(superior)] = [soldier]
				SuperiorDict[soldier] = int(superior)
				soldier +=1
		seniorityArray=[[0]]
		superiors=0
		handshakes=0
		
		#starting off with the commander in chief
		soldier = hierarchy[0]
		superiors=-1
		handshakes=0
		for x in soldier:
			TotalSuperiors = {x: 0}
		
		
		for x in seniorityArray:
			# print(x)
			
			arrayAppender=[]
			for y in x:
				# print("Y: {}".format(y))
				
				if y in hierarchy:
					# print("hierarchy[y]: {}".format(hierarchy[y]))
					for z in hierarchy[y]:
						arrayAppender.append(z)
				else:
					pass
					# print("hierarchy[y]: {}".format([]))
				
				# print("Superiors for {}: {}".format(y,superiors))
				handshakes=handshakes+superiors
			superiors+=1
			if arrayAppender == []:
				continue
			else:
				seniorityArray.append(arrayAppender)
				
		totalpairs = int(soldiers*(soldiers-1)/2)
		print("{} {}".format(handshakes+1,totalpairs - handshakes-1))		
						
def main_3():
	T=int(input())
	for x in range(0,T):
		soldiers=int(input())
		SuperiorDict=dict()
		superiors=input().split(' ')
		soldier = 1
		
		for superior in superiors:
			if superior!='':
				SuperiorDict[soldier] = int(superior)
				soldier +=1
		
		handshakes = 0
		TotalSuperiors = dict()
		for x in range(1,soldiers+1):
			soldierSuperior = SuperiorDict[x]
			superiorCount=0
			if soldierSuperior in TotalSuperiors:
			        superiorCount = TotalSuperiors[soldierSuperior]+1
			        TotalSuperiors[x] = superiorCount
			else:
				while soldierSuperior != 0:
				    superiorCount+=1
				    soldierSuperior= SuperiorDict[soldierSuperior]
				TotalSuperiors[x] = superiorCount
			
			handshakes+=superiorCount
		totalpairs = int(soldiers*(soldiers-1)/2)
		print("{} {}".format(handshakes,totalpairs - handshakes))
		
def main_DifferentRecursion():
	T=int(input())
	for x in range(0,T):
		soldiers=int(input())
		hierarchy=dict()
		superiors=input().split(' ')
		soldier = 1
		f=open('random.txt','w')
		#print(len(superiors))
		for superior in superiors:
			if superior!='':
				if int(superior) in hierarchy:
					hierarchy[int(superior)].append(soldier)
					#print(hierarchy[int(superior)])
				else:
					hierarchy[int(superior)] = [soldier]
			
				soldier +=1
		
		f.write(str(hierarchy))
		f.write('\n\n***************************\n\n')
		handshakes=0
		fistbumps=0
		
		superiorsDict = dict()
		
		loadSuperiorsDict(superiorsDict,0,0,hierarchy)
		# print(superiorsDict)
		print(hierarchy[2])
		f.write(str(superiorsDict))
		f.close()
		handshakes=1
		for y in superiorsDict:
			handshakes += superiorsDict[y]
		
		totalpairs = int(soldiers*(soldiers-1)/2)
		print("{} {}".format(handshakes,totalpairs - handshakes))
		
		
def loadSuperiorsDict(superiorsDict,soldier,superiors,hierarchy):
		if soldier == 5:
			print("IM HERE")
		superiorsDict[soldier]=superiors-1
		superiors+=1
		try:
			subordinates=hierarchy[soldier]
			for x in subordinates:
				loadSuperiorsDict(superiorsDict,x,superiors,hierarchy)
		except:
			return
		
			

def main():
	T=int(input())
	for x in range(0,T):
		soldiers=int(input())
		hierarchy=dict()
		superiors=input().split(' ')
		soldier = 1
		#print(len(superiors))
		for superior in superiors:
			if superior!='':
				if int(superior) in hierarchy:
					hierarchy[int(superior)].append(soldier)
					#print(hierarchy[int(superior)])
				else:
					hierarchy[int(superior)] = [soldier]
			
				soldier +=1
		
		
		handshakes=0
		fistbumps=0

		totalpairs = int(soldiers*(soldiers-1)/2)
		commanderInChief = hierarchy[0]
		superiors=0
		totalHandshakes=getHandShakes(hierarchy,commanderInChief[0],0)
		
		print("{} {}".format(totalHandshakes,totalpairs - totalHandshakes))
		
def getHandShakes(hierarchy,soldier,superiors):
	handshakes=0
	if (soldier in hierarchy):
		for s in hierarchy[soldier]:
			handshakes+=getHandShakes(hierarchy,s,superiors+1)
	else:
		return superiors
	
	return superiors+handshakes
	
	
	# superiors+=1
	# for x in subordinates:
		# handshake+= 1 
		# handshakes+=getHandShakes(hierarchy,x,superiors,handshakes)
	
	
	# return handshakes

		# for soldier in hierarchy:
			# subordinates = hierarchy[soldier]
			# superiors
			# n=len(subordinates)
			# fistbumps = fistbumps + ((n*(n-1))/2)
			# handshakes = handshakes + n*(soldiers - n)
		
		# handshakes=handshakes/2
		# print("{} {}".format(totalHandshakes - int(fistbumps),int(fistbumps)))
		
if __name__ == "__main__": main_4()
