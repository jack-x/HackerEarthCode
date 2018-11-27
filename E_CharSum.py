alphabets='abcdefghijklmnopqrstuvwxyz'
weight=1
weights={}
for x in alphabets:
	weights[x] = weight
	weight+=1

def main():
	s=input()
	stringWeight=0
	for x in s:
		stringWeight += weights[x]
	print(stringWeight)

main()
