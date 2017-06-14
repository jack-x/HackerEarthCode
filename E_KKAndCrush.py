
def main():
	try:
	
		t=int(input())
		for case in range(0,t):
			n=int(input())
			arrinp=input().split(' ')
			arr=[]
			for x in arrinp:
				if x!='':
					arr.append(x)
			setarr=set(arr)
			queries=int(input())
			queryNumbers=input().split(' ')
			if len(queryNumbers) == 1:
				if queryNumbers[0] in setarr:
					print("Yes")
				else:
					print("No")
				for query in range(1,queries):
					num=input()
					if num in setarr:
						print("Yes")
					else:
						print("No")
			else:
				for query in queryNumbers:
					if(query!=''):
						if query in setarr:
							print("Yes")
						else:
							print("No")
	except:
		pass
if __name__ == "__main__": main()
