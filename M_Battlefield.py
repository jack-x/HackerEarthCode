
def main():
	import re
	t = int(input())
	
	for x in range(0,t):
		n=int(input())
		s=input()
		K=0
		D=0
		
		for c in s:
			if c == 'K': K+=1
			else: D+=1
		
		#Total combinations possible with all K's together
		perms = D + 1
		
		swapCountArray=[]
		
		
		startingPosition = 0
		swapCount = 0
		
		for matchPosition in range(startingPosition,startingPosition+K):
			if(s[matchPosition] == 'D'):
				swapCount+=1
				
		swapCountArray.append(swapCount)
		
		for startingPosition in range(1,len(s)):
			
			#print("Starting Position: {}".format(startingPosition))
			#print("StartingPosition+K: {}".format(startingPosition+K))
			#print("len(s): {}".format(len(s)))
			
			if (startingPosition+K-1) <= len(s)-1 :
				#swapCount = 0
				#for matchPosition in range(startingPosition,startingPosition+K):
				#	if(s[matchPosition] == 'D'):
				#		swapCount+=1
				if(s[startingPosition-1] == 'D'):
					swapCount-=1
				
				if(s[startingPosition+K -1] == 'D'):
					swapCount+=1
				
				swapCountArray.append(swapCount)
			else:
				break
			
		Kstart=1
		swapCount=0
		for matchPosition in range(0,Kstart):
			if(s[matchPosition] == 'D'):
				swapCount+=1
		for matchPosition in range(len(s) - K + Kstart, len(s)):
			if(s[matchPosition]=='D'):
				swapCount+=1
		swapCountArray.append(swapCount)
		
		Kstart+=1
		
		while Kstart< K:
			#swapCount=0
			# for matchPosition in range(0,Kstart):
				# if(s[matchPosition] == 'D'):
					# swapCount+=1
			
			if(s[Kstart-1] == 'D'):
				swapCount+=1
			
			# for matchPosition in range(len(s) - K + Kstart, len(s)):
				# if(s[matchPosition]=='D'):
					# swapCount+=1
				
			if(s[len(s) - K + Kstart - 1] == 'D'):
				swapCount-=1
				
			swapCountArray.append(swapCount)
			Kstart+=1
		
		#print(swapCountArray)
		print(min(swapCountArray))

if __name__== "__main__" : main()