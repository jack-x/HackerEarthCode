def main_optimized_v2():
	inp =input().split(' ')
	N=int(inp[0])
	Q=int(inp[1])
	string=input()
	alphabetsCount=[0]*27
	fullStringDict={}
	stringCounter=1
	alphabets=[0]
	
	for c in 'abcdefghijklmnopqrstuvwxyz':
		alphabets.append(c)
	
	for s in string:
		index=ord(s) - 96
		alphabetsCount[index]+=1
		fullStringDict[stringCounter] = list(alphabetsCount)
		stringCounter+=1

	for case in range(0,Q):
		query = input().split(' ')
		l=int(query[0])
		r=int(query[1])
		
		prefix=''
		suffix=''
		prefixDict=dict()

		ch=l-1
		specialCharacter=string[l-1]
		indexOfSpecialCharacter=ord(specialCharacter) - 96
		for index in range(1,26):
			x=fullStringDict[r][index] - fullStringDict[l][index]
			y=fullStringDict[r][index+1] - fullStringDict[l][index+1]
			if(index==indexOfSpecialCharacter):
				x+=1
			if((index+1) == indexOfSpecialCharacter):
				y+=1
			
			characterPositionX=x%26 +1
			prefix+=alphabets[characterPositionX]
			prefixDict[prefix] = 1
			
			characterPositionY=y%26 +1
			suffix+=alphabets[characterPositionY]
		
		flag=0
		while len(suffix) >0:
			if(suffix in prefixDict):
				flag=1
				for c in suffix:
					print(c,end='')
				print()
				break
			suffix = suffix[1:len(suffix)]
		
		if(flag==0):
			print("None")


def main_optimized_v2_withPrint():
	inp =input().split(' ')
	N=int(inp[0])
	Q=int(inp[1])
	string=input()
	alphabetsCount=[0]*27
	fullStringDict={}
	stringCounter=1
	alphabets=[0]
	
	for c in 'abcdefghijklmnopqrstuvwxyz':
		alphabets.append(c)
	
	for s in string:
		index=ord(s) - 96
		alphabetsCount[index]+=1
		fullStringDict[stringCounter] = list(alphabetsCount)
		stringCounter+=1

	for case in range(0,Q):
		query = input().split(' ')
		l=int(query[0])
		r=int(query[1])
		
		# alphadict=dict()
		# fullString=[]
		# for c in 'abcdefghijklmnopqrstuvwxyz':
			# alphadict[c] = 0
		
		# for c in string[l-1:r]:
			# alphadict[c]+=1
		
		prefix=''
		suffix=''
		prefixDict=dict()
		ch=l-1
		
		specialCharacter=string[l-1]
		indexOfSpecialCharacter=ord(specialCharacter) - 96
		#print("Extracted String: {}".format(string[l-1:r]))
		
		#print("String LISt L: {}".format(fullStringDict[l]))
		#print("String List R: {}".format(fullStringDict[r]))
		for index in range(1,26):
			x=fullStringDict[r][index] - fullStringDict[l][index]
			y=fullStringDict[r][index+1] - fullStringDict[l][index+1]
			
			
			
			#print("At character count: {}".format(alphabets[index]))
			
			#print("Value of x: {}".format(x))
			#print("Value of y: {}".format(y))
			if(index==indexOfSpecialCharacter):
				x+=1
			if((index+1) == indexOfSpecialCharacter):
				y+=1
			#x=alphadict[c]
			
			characterPositionX=x%26 +1
			prefix+=alphabets[characterPositionX]
			prefixDict[prefix] = 1
			
			#y=alphadict[c2]
			characterPositionY=y%26 +1
			suffix+=alphabets[characterPositionY]
		
		#print(prefix)
		#print(suffix)
		flag=0
		while len(suffix) >0:
			if(suffix in prefixDict):
				flag=1
				for c in suffix:
					print(c,end='')
				print()
				break
			#prefix = prefix[0:len(prefix)-1]
			suffix = suffix[1:len(suffix)]
		
		if(flag==0):
			print("None")


def main_optimized():
	inp =input().split(' ')
	N=int(inp[0])
	Q=int(inp[1])
	string=input()
	alphabets=[0]
	
	for c in 'abcdefghijklmnopqrstuvwxyz':
		alphabets.append(c)
	
	for case in range(0,Q):
		query = input().split(' ')
		l=int(query[0])
		r=int(query[1])
		
		alphadict=dict()
		fullString=[]
		for c in 'abcdefghijklmnopqrstuvwxyz':
			alphadict[c] = 0
		
		for c in string[l-1:r]:
			alphadict[c]+=1
		
		prefix=''
		suffix=''
		prefixDict=dict()
		for index in range(1,26):
			c=alphabets[index]
			c2=alphabets[index+1]
			x=alphadict[c]
			characterPositionX=x%26 +1
			prefix+=alphabets[characterPositionX]
			prefixDict[prefix] = 1
			
			y=alphadict[c2]
			characterPositionY=y%26 +1
			suffix+=alphabets[characterPositionY]
		
		flag=0
		while len(suffix) >0:
			if(suffix in prefixDict):
				flag=1
				for c in suffix:
					print(c,end='')
				print()
				break
			#prefix = prefix[0:len(prefix)-1]
			suffix = suffix[1:len(suffix)]
		
		if(flag==0):
			print("None")
			

def main_optimized_1():
	inp =input().split(' ')
	N=int(inp[0])
	Q=int(inp[1])
	string=input()
	alphabets=[0]
	
	for c in 'abcdefghijklmnopqrstuvwxyz':
		alphabets.append(c)
	
	for case in range(0,Q):
		query = input().split(' ')
		l=int(query[0])
		r=int(query[1])
		
		alphadict=dict()
		fullString=[]
		for c in 'abcdefghijklmnopqrstuvwxyz':
			alphadict[c] = 0
		
		for c in string[l-1:r]:
			alphadict[c]+=1
		
		prefix=[]
		suffix=[]
		
		for index in range(1,26):
			c=alphabets[index]
			c2=alphabets[index+1]
			x=alphadict[c]
			characterPositionX=x%26 +1
			prefix.append(alphabets[characterPositionX])
			
			y=alphadict[c2]
			characterPositionY=y%26 +1
			suffix.append(alphabets[characterPositionY])
		
		flag=0
		while len(prefix) > 0:
			if(prefix == suffix):
				flag=1
				break
			del prefix[-1]
			del suffix[0]
		
		if(flag==1):
			for c in prefix:
				print(c,end='')
			print()
		else:
			print("None")
def main():
	inp =input().split(' ')
	N=int(inp[0])
	Q=int(inp[1])
	string=input()
	alphabets=[0]
	for c in 'abcdefghijklmnopqrstuvwxyz':
		alphabets.append(c)
	
	for case in range(0,Q):
		query = input().split(' ')
		l=int(query[0])
		r=int(query[1])
		
		alphadict=dict()
		fullString=[]
		for c in 'abcdefghijklmnopqrstuvwxyz':
			alphadict[c] = 0
		
		for c in string[l-1:r]:
			alphadict[c]+=1
		
		for c in 'abcdefghijklmnopqrstuvwxyz':
			x=alphadict[c]
			characterPosition=x%26 +1
			fullString.append(alphabets[characterPosition])
		
		#prefix=fullString[0:25]
		prefix='abcd'
		#suffix=fullString[1:26]
		suffix='efgh'
		flag=1
		for i in range(0,26):
		#	print(prefix)
		#	print(suffix)
			if(prefix!=suffix):
				prefix=fullString[0:(25-i)]
				suffix=fullString[i+1: 26]
			else:
				flag=0
				break
				
		
		
		#print(fullString,end='\n')
		if(flag == 0):
			for c in prefix:
				print(c,end="")
			print()
		else:
			print("None")
			

if __name__ == "__main__": main_optimized_v2()