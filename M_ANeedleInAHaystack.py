class LetsPass(Exception): pass

def main():
	T=int(input())
	for case in range(0,T):
		inp=input()
		patternDict=dict()
		sliceDict=dict()
		
		for c in 'abcdefghijklmnopqrstuvwxyz':
			patternDict[c] =0
			sliceDict[c] =0
			
		for s in inp:
			patternDict[s]+=1
		
		text=input()
				
		patternLength = len(inp)
		
		sliceBeginning = 0
		
		sliceEnding=  sliceBeginning + patternLength
		
		FinalFlag=0
		
		#Initializing the first slice string dict
		
		for s in text[sliceBeginning:sliceEnding]:
			sliceDict[s]+=1
	
		while sliceEnding<=(len(text)):
			if sliceDict == patternDict:
				print("YES")
				FinalFlag=1
				break
			else:
				characterRemoved = text[sliceBeginning]
				sliceBeginning+=1
				sliceDict[characterRemoved] = sliceDict[characterRemoved] - 1
				if(sliceEnding == len(text)):
					break
				characterAdded = text[sliceEnding]
				sliceDict[characterAdded] +=1
				sliceEnding+=1
		
		if FinalFlag != 1:
			print("NO")

def main_withDict_print():
	T=int(input())
	for case in range(0,T):
		inp=input()
		patternDict=dict()
		sliceDict=dict()
		
		for c in 'abcdefghijklmnopqrstuvwxyz':
			patternDict[c] =0
			sliceDict[c] =0
			
		for s in inp:
			patternDict[s]+=1
		
		text=input()
				
		patternLength = len(inp)
		
		sliceBeginning = 0
		
		sliceEnding=  sliceBeginning + patternLength
		
		FinalFlag=0
		
		#Initializing the first slice string dict
		
		for s in text[sliceBeginning:sliceEnding]:
			sliceDict[s]+=1
	
		print("PatternDict: {}".format(patternDict))
		
		while sliceEnding<=(len(text)):
			print("SLICEDICT: {}".format(sliceDict))
			if sliceDict == patternDict:
				print("YES")
				FinalFlag=1
				break
			else:
				characterRemoved = text[sliceBeginning]
				sliceBeginning+=1
				sliceDict[characterRemoved] = sliceDict[characterRemoved] - 1
				print("Character Removed: {}".format(characterRemoved))
				print("Dictionary Value: SliceDict[{}] =  {}".format(characterRemoved,sliceDict[characterRemoved]))
				
				
				if(sliceEnding == len(text)):
					break
				characterAdded = text[sliceEnding]
				sliceDict[characterAdded] +=1
				sliceEnding+=1
				print("Character Added: {}".format(characterAdded))
				print("Dictionary Value: sliceDict[{}]= {}".format(characterAdded,sliceDict[characterAdded]))
				print()
				
		
		if FinalFlag != 1:
			print("NO")

def main_usingCounters():
	T=int(input())
	from collections import Counter
	for case in range(0,T):
		inp=input()
		pattern=Counter(inp)

		text=input()
		flag=0
		patternLength = len(inp)
		sliceBeginning = 0
		sliceEnding=  sliceBeginning + patternLength
		FinalFlag=0
		
		while sliceEnding <= len(text):
			stringSliceSet= Counter(text[sliceBeginning:sliceEnding])
			difference=pattern - stringSliceSet
			if(len(difference) > 0):
				sliceBeginning+=1
				sliceEnding+=1
				continue
			else:
				print("YES")
				FinalFlag=1
				break
		
		if FinalFlag != 1:
			print("NO")
	
					
if __name__ == "__main__": main()