
def main_Optimized():
	string=input()
	
	chunk = int(len(string)/2)
	
	substringArray = dict()
	flag=0
	while chunk>1:
		chunk2=chunk
		x=0
		while chunk2<=len(string):
			substring=string[x:chunk2]
			#print("Substring: {}".format(substring))
			chunk2+=1
			x+=1
			if substring in substringArray:
				print(chunk)
				flag=1
				break
			else:
				substringArray[substring]=1
		
		if(flag==1):
			break
		else:
			chunk-=1

#Simple find all substrings. Sort them according to length of characters. Then check if any string occurs twice in that array. IF it does, break and finish.
#Else print NO and finish
def main_bruteForce():
	string=input()
	subStringArray=[]
	for x in range(0,len(string)):
		substring=''
		for y in range(x+1,len(string)+1):
			substring = string[x:y]
			subStringArray.append(substring)
	
	#print(subStringArray)
	subStringArray.sort()
	
	#print(subStringArray)
	subStringArray.sort(key=len, reverse=True)
	#print(subStringArray)
	
	for x in range(0,len(subStringArray)):
		if (subStringArray[x] == subStringArray[x-1]):
			print(len(subStringArray[x]))
			break
		else:
			pass
	
if __name__ == "__main__": main_Optimized()