def main2():
	T=int(input())
	for case in range(0,T):
		N=int(input())
		d=input().split(' ')
		K = int(input())
		# days=[]
		totalYearDistance = 0
		totalDistanceWalkedArray=[]
		for dd in d[0:len(d)-1]:
			ddd = int(dd)
			# days.append(ddd)
			totalYearDistance+=ddd
			totalDistanceWalkedArray.append(totalYearDistance)

			#Case 1: Total distance walked in a year is more than K
		if K>totalYearDistance:
			remainder = K%totalYearDistance
			if remainder==0:
				remainder = totalYearDistance
			for x in range(0,N):
				if totalDistanceWalkedArray[x] >= remainder:
					break
			print(x+1)
			
		# Case 2: Total Distance to be walked can be covered in the same year
		else:
			for x in range(0,N):
				if totalDistanceWalkedArray[x] >= K:
					break
			print(x+1)
def main():
	T=int(input())
	for case in range(0,T):
		N=int(input())
		d=input().split(' ')
		days=[]
		totalYearDistance = 0
		for dd in d[0:len(d)-1]:
			ddd = int(dd)
			days.append(ddd)
			totalYearDistance+=ddd
			
		K = int(input())
		#Case 1: Total distance walked in a year is more than K
		if K>totalYearDistance:
			while K>=totalYearDistance:
				K=K - totalYearDistance
			
			totalDistanceWalked = 0
			position = -1
			while totalDistanceWalked < K:
				position+=1
				if position >= N:
					position=0
				currentDayWalk = days[position]
				totalDistanceWalked = totalDistanceWalked + currentDayWalk
			position+=1
			print(position)
		# Case 2: Total Distance to be walked can be covered in the same year
		else:
			totalDistanceWalked=0
			position=-1
			while totalDistanceWalked < K :
				position+=1
				if position >= N:
					position = 0a
				currentDayWalk = days[position]
				totalDistanceWalked = totalDistanceWalked + currentDayWalk
			position+=1
			print(position)
			


if __name__ == "__main__": main2()
