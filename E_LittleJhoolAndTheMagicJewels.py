
def main():
	T=int(input())
	
	for x in range(0,T):
		rubies={'r':0,'u':0,'b':0,'y':0}
		string = input()
		
		for s in string:
			try:
				rubies[s]+=1
			except:
				continue
		
		min=rubies['r']
		for r in rubies.keys():
			if min>rubies[r]:
				min = rubies[r]
		
		print(min)





if __name__ == "__main__": main()
