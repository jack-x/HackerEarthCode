
# They will not all be in one go
# patterns of v and w will be mixed with several alphabets in between

def main():
	N=int(input())
	s=input()
	VWCount=0
	characterCount=0
	minMax = []
	for x in s:
		if x =='v':
			VWCount+=1
		elif x == 'w':
			VWCount+=2
		else:
			characterCount+=1
			if VWCount!=0:
				if VWCount %2 == 0:
					min = int(VWCount/2)
					max = VWCount
					minMax.append([min,max])
				else:
					min  = 1 + int((VWCount-1)/2)
					max = VWCount
					minMax.append([min,max])
				VWCount=0
	
	if VWCount>0:
		if VWCount %2 == 0:
			min = int(VWCount/2)
			max = VWCount
			minMax.append([min,max])
		else:
			min  = 1 + int((VWCount-1)/2)
			max = VWCount
			minMax.append([min,max])
	min = 0
	max = 0
	for x in minMax:
		# print(x)
		min += x[0]
		max += x[1]
		# print("Next")
	min += characterCount 
	max += characterCount
	
	print("{} {}".format(min,max))
		


main()