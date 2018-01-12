
def main():
	X=0
	Y=0
	s=input()
	for x in s:
		if x == 'L':
			X=X-1
		elif x=='R':
			X=X+1
		elif x=='U':
			Y=Y+1
		else:
			Y=Y-1
	print("{} {}".format(X,Y))


if __name__ == '__main__': main()
