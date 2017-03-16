N = int(input())
callingOrder = input().split()
idealOrder = input().split()

timeTaken = 0
while (len(callingOrder) !=0):
	a = callingOrder[0]
	b = idealOrder[0]
	if(a==b):
		timeTaken+=1
		callingOrder.pop(0)
		idealOrder.pop(0)
	else:
		callingOrder.append(callingOrder[0])
		callingOrder.pop(0)
		timeTaken+=1

print(timeTaken)
