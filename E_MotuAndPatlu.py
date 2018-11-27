def main():
	n = int(input())
	p=0
	while True:
		p+=1
		n=n-p
		if n<=0:
			print('Patlu')
			break
		m=2*p
		n=n-m
		if n<=0:
			print('Motu')
			break
		
main()
