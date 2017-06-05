

def main():
	Q = int(input())
	q1=[]
	q2=[]
	q3=[]
	q4=[]
	for x in range(0,Q):
		inp=input().split(' ')
		if(inp[0] == 'E'):
			if(len(q1) == 0):
				q1.append([inp[1],inp[2]])
				continue
			elif(inp[1] == q1[0][0]):
				q1.append([inp[1],inp[2]])
				continue
			if(len(q2) == 0):
				q2.append([inp[1],inp[2]])
				continue
			elif(inp[1] == q2[0][0]):
				q2.append([inp[1],inp[2]])
				continue
			if(len(q3) == 0):
				q3.append([inp[1],inp[2]])
				continue
			elif(inp[1] == q3[0][0]):
				q3.append([inp[1],inp[2]])
				continue
			if(len(q4) == 0):
				q4.append([inp[1],inp[2]])
				continue
			elif(inp[1] == q4[0][0]):
				q4.append([inp[1],inp[2]])
				continue
			
			continue
		if(inp[0] == 'D'):
			student=q1.pop(0)
			print(student[0] + " " + student[1])
			if(len(q1) == 0):
				if(len(q2) == 0):
					if(len(q3)==0):
						q1=q4
						q4=[]
						continue
					q1=q3
					q3=q4
					q4=[]
					continue
				q1=q2
				q2=q3
				q3=q4
				q4=[]
				continue

if __name__ == "__main__": main()
