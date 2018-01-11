
def main():
	T=int(input())
	
	d = {'Largest': [None,0],'SecondLargest':[None,0],'ThirdLargest':[None,0]}
	
	for case in range(0,T):
		coder = input().split(' ')
		X = int(coder[1])
		if X > d['Largest'][1]:
			d['ThirdLargest'] = d['SecondLargest']
			d['SecondLargest'] = d['Largest']
			d['Largest'] = [coder[0],X]
		elif X > d['SecondLargest'][1]:
			d['ThirdLargest'] = d['SecondLargest']
			d['SecondLargest'] = [coder[0],X]
		elif X > d['ThirdLargest'][1]:
			d['ThirdLargest'] = [coder[0],X]
		
	print(d['Largest'][0])	
	print(d['SecondLargest'][0])
	print(d['ThirdLargest'][0])
	
if __name__ == '__main__': main()
