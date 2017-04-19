
def main():
	N = input();
	d = dict();
	
	Numbers=input().split();
	
	for x in Numbers:
		if x in d:
			d[x]= d[x]+1
		else:
			d[x]=1
	
	greatestKey=0
	largestNumber=0
	for key in d:
		if(largestNumber < d[key]):
			greatestKey = key
			largestNumber = d[key]
		if(largestNumber == d[key] and key < greatestKey):
			greatestKey = key
			
		
	print(greatestKey)




if __name__ == "__main__":main()