#Cipher

def main():
	lowers = []
	uppers = []
	numbers = [0,1,2,3,4,5,6,7,8,9]
	for x in 'abcdefghijklmnopqrstuvwxyz':
		lowers.append(x)
		
	for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		uppers.append(x)
	
	statement = input()
	key = int(input())
	
	newStatement = []
	
	for x in statement:
		Index = ord(x)
		if ord(x) >= 65 and ord(x) <= 90:
			Index = ord(x) - 65
			for y in range(0,key):
				Index+=1
				if Index == 26:
					Index = 0
			newStatement.append(uppers[Index])
			continue
		if ord(x) >= 97 and ord(x) <= 122:
			Index = ord(x) - 97
			for y in range(0,key):
				Index+=1
				if Index == 26:
					Index = 0
			newStatement.append(lowers[Index])				
			continue
		if ord(x) >= 48 and ord(x) <= 57:
			Index = ord(x) - 48
			for y in range(0,key):
				Index+=1
				if Index == 10:
					Index = 0
			newStatement.append(numbers[Index])
			continue
		newStatement.append(x)
	for x in newStatement:
		print(x,end='')

if __name__ == '__main__' : main()