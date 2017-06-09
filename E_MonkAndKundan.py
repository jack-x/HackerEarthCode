
def main():
	l="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	letters=dict()
	pos=0
	for ll in l:
		letters[ll] = pos
		pos+=1

	N = int(input())
	for case in range(0,N):
		s = input().split(' ')
		hashValue=0
		for ch in s:
			pos=0
			for c in ch:
				hashValue+= letters[c]
				hashValue+= pos
				pos+=1
		hashValue= hashValue * len(s)
		print(hashValue)
if __name__== "__main__": main()
