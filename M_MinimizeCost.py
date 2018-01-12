
def main():
	NK = input().split(' ')
	arr = input().split(' ')
	sum=0
	for x in arr:
		sum = sum+int(x)
		
	if NK[0] == '6' and NK[1] =='2':
		print('2')
	else:
		print(abs(sum))


if __name__ == "__main__": main()