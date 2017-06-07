
def main():
	t=int(input())
	for c in range(0,t):
		S=input()
		T=input()
		
		import hashlib
		substringDict = dict()
		flag=0
		
		for x in range(0,len(T)):
			for y in range(x+1,len(T)+1):
				substring = T[x:y]
				hash_object=hashlib.sha512(substring.encode())
				#print("substring: {}".format(substring))
				#print("hexDigest: {}".format(hash_object.hexdigest()))
				substringDict[hash_object.hexdigest()] = substring
		#print(substringDict)
		
		for x in range(0,len(S)):
			for y in range(x+1,len(S)+1):
				substring = S[x:y]
				hash_object=hashlib.sha512(substring.encode())
				try:
					temp = substringDict[hash_object.hexdigest()]
					print("YES")
					flag=1
					break
				except:
					continue
			if(flag==1):
				break
			
		if(flag==0):
			print("NO")

def main2():
	t=int(input())
	for c in range(0,t):
		S=input()
		T=input()
		
		import hashlib
		substringDict = dict()
		flag=0
		
		for x in range(0,len(T)):
			try:
				substringDict[T[x]]+=1
			except:
				substringDict[T[x]] = 1
		#print(substringDict)
		
		for x in range(0,len(S)):
			try:
				temp = substringDict[S[x]]
				print("YES")
				flag=1
				break
			except:
				continue
		if(flag==0):
			print("NO")			
			
if __name__ == '__main__': main2()
