
def main():
	numberComrades = int(input())
	c = input().split(' ')
	comrades = []
	position=0
	highestposition=0
	power=0
	for x in c:
		value=int(x)
		comrades.append(value)
		if value > power:
			highestposition = position
			power = value
		position+=1
	
	survivalPosition = []
	
	#we start from right to highest
	currentHighestPower = 0
	for x in range(0,highestposition+1):
		currentPower=comrades[x]
		if currentPower > currentHighestPower:
			survivalPosition.append(x)
			currentHighestPower = currentPower
	
	survivalPosition2 = []
	currentHighestPower = 0
	for x in range(numberComrades-1,highestposition,-1):
		currentPower=comrades[x]
		if currentPower> currentHighestPower:
			survivalPosition2.insert(0,x)
			currentHighestPower = currentPower
	
	for x in survivalPosition2:
		survivalPosition.append(x)
	
	for x in survivalPosition:
		y=x+1
		print(y,end=' ')
	
if __name__ == "__main__": main()
