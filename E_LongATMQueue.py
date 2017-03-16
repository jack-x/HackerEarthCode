
N = int(input())
Queue = input().split()

for index,item in enumerate(Queue):
	Queue[index] = int(item)

numberOfGroups = 1

for x in range(0,len(Queue)-1):
	if (Queue[x] > Queue[x+1]):
		numberOfGroups = numberOfGroups + 1

print(numberOfGroups)
