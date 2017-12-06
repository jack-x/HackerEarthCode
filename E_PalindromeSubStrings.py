
def main():
	X=input()
	l = len(X)
	strings = []
	revs = []
	flag=0
	for x in range(0,l-1):
		for y in range(x+2,l+1):
			s = X[x:y]
			strings.append(s)
			rev = reverse(s)
			if rev in strings:
				revs.append(len(rev))
				flag=1
				
	
	if flag == 0:
		print("NO")
	else:
		print("YES")
		revs.sort()
		print(revs[-1])
		
def reverse(s):
	rev = ''
	for x in s:
		rev = x + rev
	return rev
if __name__ == "__main__": main()
