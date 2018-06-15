def main():
	I = int(input())
	for case in range(0,I):
		i = input().split(' ')
		N = int(i[0])
		P = int(i[1])
		i = input()
		
		live = [0]*(P+1)
		dead=[]
		deadName=[]
		
		batting = [1,2]
		# battingPosition = 0
		nextToBat=3
		
		c = case+1
		print('Case {}:'.format(c))
		
		ballCounter = 0
		for x in i:
			ballCounter+=1
			if x == 'W':
				
				# dead.append(live.pop(0))
				# deadName.append('Player {}'.format(batting[0])
				dead.append(batting[0])
				batting[0] = nextToBat
				nextToBat+=1
				if ballCounter == 6:
					ballCounter=0
					temp = batting[0] 
					batting[0] = batting[1]
					batting[1] = temp
				continue
				
			live[batting[0]] +=int(x)
			if int(x)==1:
				temp = batting[0] 
				batting[0] = batting[1]
				batting[1] = temp
			if ballCounter == 6:
				ballCounter=0
				temp = batting[0] 
				batting[0] = batting[1]
				batting[1] = temp
			
			
		for x in range(1,P+1):
			if x in batting:
				print('Player {}: {}*'.format(x,live[x]))
			else:
				if x in dead:
					print('Player {}: {}'.format(x,live[x]))
				else:
					print('Player {}: DNB'.format(x))
			
	

main()
