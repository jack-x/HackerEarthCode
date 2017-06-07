
def main():
	N=int(input())
	alphadict = dict()
	
	for character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
		alphadict[character] = character
	
	for x in range(0,N):
		i=input()
		inp = i.upper()
		inp2 = i.lower()
		temp = alphadict[inp[0]]
		alphadict[inp[0]] = alphadict[inp[2]]
		alphadict[inp[2]] = temp
		
		temp = alphadict[inp2[0]]
		alphadict[inp2[0]] = alphadict[inp2[2]]
		alphadict[inp2[2]] = temp
	
	alphadict2=dict()
	
	for key in alphadict.keys():
		alphadict2[alphadict[key]] = key
	
	try:	
		inp = input()
		while inp!='':
			for s in inp:
				if(s == ' '):
					print(' ',end='')
				else:
					print(alphadict2[s],end='')
			inp=input()
	except:
		return


if __name__ == "__main__": main()
