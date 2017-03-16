#DisplayChessBoard as per Hacker Earth

def displayChessBoardHackerEarth(chessBoard,N):
	for x in range(N):
		for y in chessBoard[x]:
			print(y,end=' ')
		print()
	
#Properly displalying a chessBoard
def displayChessBoard(chessBoard = list(),N=0):
	print('[')
	for x in range(N):
		print("\t",end='')
		print(chessBoard[x])
	print(']')

#the function will check the correctness of the current position for the queen
def canBeAttacked(x,y,chessBoard,N):
	for a in chessBoard[x]:
		if a == 1:
			return True
	
	for a in chessBoard:
		if a[y] == 1:
			return True
	
	
	a=x+1
	b=y+1
	while(a<N and b<N):
		if chessBoard[a][b] == 1:
			return True
		a=a+1
		b=b+1
	
	a=x-1
	b=y-1
	while (a>=0 and b>=0):
		if chessBoard[a][b] ==1:
			return True
		a=a-1
		b=b-1
		
	a=x+1
	b=y-1
	while(a<N and b>=0):
		if chessBoard[a][b] == 1 :
			return True
		a=a+1
		b=b-1
		
	a=x-1
	b=y+1
	while(a>=0 and b<N):
		if chessBoard[a][b] == 1:
			return True
		a=a-1
		b=b+1
	
	return False
	
#HackerEarthLogic Will not work at all. What the hell were they smoking?
def NQueens(chessBoard,N):
	if N == 0:
		return True
	for i in range(0,N):
		for j in range(0,N):
			if canBeAttacked(i,j,chessBoard,N) is True:
				pass
			chessBoard[i][j] = 1
			if NQueens(chessBoard,N-1) is True:
				return True
			
			chessBoard[i][j]=0
	return False
	
#My Different Logic
def NQueens2(chessBoard,N,queensPlaced):
	if queensPlaced == N:
		return True
	for i in range(0,N):
		for j in range(0,N):
			if canBeAttacked(i,j,chessBoard,N) is True:
				pass
			else:
				chessBoard[i][j]=1
				queensPlaced += 1
				if NQueens2(chessBoard,N,queensPlaced):
					return True
				else:
					chessBoard[i][j] = 0
					queensPlaced = queensPlaced - 1
	return False

#Optimizing the logic further	
def NQueens3(chessBoard,N,queensPlaced):
	if queensPlaced == N:
		return True
	i=0
	while(i<N):
		j=0
		while(j<N):
			while( 1 in chessBoard[i] and i<N-1):
				i+=1
				
			if canBeAttacked(i,j,chessBoard,N) is True:
				pass
			else:
				chessBoard[i][j]=1
				queensPlaced += 1
				if NQueens3(chessBoard,N,queensPlaced):
					return True
				else:
					chessBoard[i][j] = 0
					queensPlaced = queensPlaced - 1
			j+=1
		i+=1
	return False

def main():
	N = int(input());
	chessBoard = list();
	for x in range(N):
		chessBoard.append(list())
		for y in range(N):
			chessBoard[x].append(0)
	displayChessBoard(chessBoard,N)
	#chess board initialized
	
	#NQueens Problem
	if NQueens3(chessBoard,N,0):
		print("YES")
		displayChessBoardHackerEarth(chessBoard,N)
	else:
		print("NO")


if __name__ == "__main__" : main()
