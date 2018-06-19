def main():
	n = int(input())
	c=[0]*8
	chessboard=[]
	for x in range(0,8):
		chessboard.append(list(c))
		
	chessboardsingle = [0]*64

	flag=-1
	chessboardsingle[0]='W'
	for x in range(1,64):
		if x%8==0:
			chessboardsingle[x] = chessboardsingle[x-1]
			continue
		if flag == 1:
			chessboardsingle[x] = 'W'
		else:
			chessboardsingle[x]='B'
		flag=flag*-1
		
	# print(chessboardsingle)
	pointer=0
	for x in range(0,8):
		for y in range(0,8):
			# print(pointer)
			# print(chessboardsingle[pointer])
			
			chessboard[x][y] = chessboardsingle[pointer]
			# print(chessboard[x][y])
			pointer+=1
	# print(chessboard)
	# print(chessboardsingle[0])

	for case in range(0,n):
		A = input().split(' ')
		B= input().split(' ')
		
		coordinates1 = [int(A[0])-1,ord(A[1]) - ord('a')]
		coordinates2 = [int(B[0])-1,ord(B[1]) - ord('a')]
		
		color1 = chessboard[coordinates1[0]][coordinates1[1]]
		color2 = chessboard[coordinates2[0]][coordinates2[1]]
	
		
		
		if color1 == color2:
			print('NO')
		else:
			print('YES')
main()
