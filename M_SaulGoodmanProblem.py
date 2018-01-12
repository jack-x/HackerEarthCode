
def main():
	T=int(input())
	for a in range(0,T):
		N=int(input())
		oneCells=[]
		
		newCell = input().split(' ')
		cell = []
		cell.append(int(newCell[0]))
		cell.append(int(newCell[1]))
		
		oneCells.append(cell)
		
		trueCellPairs = 0
		for x in range(1,N):
			new1 = input().split(' ')
			cell2 = []
			cell2.append(int(new1[0]))
			cell2.append(int(new1[1]))
			
			for cell1 in oneCells:
				#cell1= cell.split(' ')
				
				#First Equation
				N1 = abs(cell2[0] - cell1[0])
				N2 = abs(cell2[1] - cell1[1])
				
				if (N1 == N2):
					trueCellPairs+=1
					continue
				
				# N1 = int(cell2[0]) - int(cell1[0])
				# N2 = -1 * (int(cell2[1]) - int(cell1[1]))
				
				# if (N1 == N2):
					# trueCellPairs+=1
					# continue
				
				# N1 = -1 * (int(cell2[0]) - int(cell1[0]))
				# N2 = int(cell2[1]) - int(cell1[1])				
				
				# if (N1 == N2):
					# trueCellPairs+=1
					# continue
			
			oneCells.append(cell2)
			
		print(trueCellPairs)

if __name__ == "__main__" : main()