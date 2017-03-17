N = int(input())

for x in range(0,N):
	cars = int(input())
	speedOriginal=input().split()
	# speedfinal=[]
	maxSpeedCars=0
	maxSpeedSoFar=1000000001
	for x in speedOriginal:
		if int(x) < maxSpeedSoFar:
			maxSpeedCars+=1
			maxSpeedSoFar=int(x)
	
	print(maxSpeedCars)

		
