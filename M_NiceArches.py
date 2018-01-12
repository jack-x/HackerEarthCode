
def main():
	N = int(input())
	count=0
	for x in range(0,N):
		word = input()
		wordstack=[]
		
		for letter in word:
			if len(wordstack) == 0:
				wordstack.append(letter)
			else:
				lastLetter = wordstack.pop()
				if lastLetter != letter :
					wordstack.append(lastLetter)
					wordstack.append(letter)
				else:
					pass
					# Nothing to do as the letter is already popped	
		if len(wordstack) == 0:
			count+=1
			#print("count increased. Wordstack = {}".format(str(wordstack)))
		else:
			pass
			#print("count not increased. Wordstack = {}".format(str(wordstack)))
	print(count)

if __name__ == "__main__": main()