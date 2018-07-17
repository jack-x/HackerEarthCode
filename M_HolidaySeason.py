alpha = 'abcdefghijklmnopqrstuvwxyz'
alphadict = {}

for x in alpha:
	alphadict[x] = []



def main():
	N = int(input())
	
	s = input()
	
	for x in range(0,N):
		alphadict[s[x]].append(x)
	print(alphadict)
	count = 0
	for x1 in alphadict.keys():
		
		arr1 = alphadict[x1]
		if len(arr1) == 0 or len(arr1) == 1:
			print('!!!!!arr1: {}  Letter:{} is empty or 1. Skipping'.format(arr1,x1))
			continue
			
		print('In loop x1. Letter: {}'.format(x1))
		print(arr1)
		print('---')
		
		for x2 in alphadict.keys():
			if x2 == x1:
				print('x2:{} and x1:{} are equal. Skipping this part'.format(x2,x1))
				print('--#######--')
				continue
				
			arr2 = alphadict[x2]
			if len(arr2) == 0 or len(arr2) == 1 :
				print('!!!!!arr2: {}  Letter:{} is empty or 1. Skipping'.format(arr2,x2))
				continue
				
			print('In loop x2. Letter: {}'.format(x2))
			print(arr2)
			print('---')
			
			print('============LOGIC BEGINS=================')
			for a in range(0,len(arr1)-1):
				print('Loop a {}'.format(arr1[a]))
				for b  in range(0,len(arr2)-1):
					print('Loop b {}'.format(arr2[b]))
					for c in range(a+1,len(arr1)):
						print('Loop c {}'.format(arr1[c]))
						for d in range(b+1,len(arr2)):
							print('Loop d {}'.format(arr2[d]))
							if arr1[a] < arr2[b] and arr2[b] < arr1[c] and arr1[c] < arr2[d]:
								print('!!***VICTORY*******!!! Made it here. Count increased')
								count+=1
	
	print(count)
from math import factorial

def main2():	
	N = int(input())
	
	s = input()
	
	for x in range(0,N):
		alphadict[s[x]].append(x)
	count = 0
	# print(alphadict)
	for x in alpha:
		if len(alphadict[x]) <= 1:
			del alphadict[x]
	keyarr = list(alphadict.keys())
	# print(keyarr)
	for x1 in range(0,len(keyarr)):
		
		arr1 = alphadict[keyarr[x1]]
		
		for x2 in range(x1,len(keyarr)):
		
			arr2 = alphadict[keyarr[x2]]
			flag = 0
			if keyarr[x2] == keyarr[x1]:
				flag=1
				if len(arr1)<4:
					continue
				#ncr
				result = int(factorial(len(arr2)) /(24 * (factorial(len(arr2))-4)))
				count+=result
				continue
		
		
			for a in range(0,len(arr1)-1):
				for c in range(a+1,len(arr1)):
					for b in range(0,len(arr2)-1):
						if arr1[a] >= arr2[b]:
							continue
						if arr1[c] <= arr2[b]:
							break
						for d in range(b+1,len(arr2)):
							if arr1[a] < arr2[b] and arr2[b] < arr1[c] and arr1[c] < arr2[d]:
								remaining = len(arr2) - d
								count+=remaining
								break
			if flag == 1:
				continue								
								
			for a in range(0,len(arr2)-1):
				for c in range(a+1,len(arr2)):
					for b in range(0,len(arr1)-1):
						if arr2[a] >= arr1[b]:
							continue
						if arr2[c] <= arr1[b]:
							break
						for d in range(b+1,len(arr1)):
							if arr2[a] < arr1[b] and arr1[b] < arr2[c] and arr2[c] < arr1[d]:
								remaining = len(arr1) - d
								count+=remaining
								break
								
				# for b  in range(0,len(arr2)-1):
					# if arr1[a] >= arr2[b]:
						# continue
					# for c in range(a+1,len(arr1)):
						# if arr2[b] >= arr1[c]:
							# continue
						# for d in range(b+1,len(arr2)):
							
							# if arr1[a] < arr2[b] and arr2[b] < arr1[c] and arr1[c] < arr2[d]:
								# remaining = len(arr2) - d
								# count+=remaining
								# break
			# if flag == 1:
				# continue
			
			# for a in range(0,len(arr2)-1):
				# for b  in range(0,len(arr1)-1):
					# if arr2[a] >= arr1[b]:
						# continue
					# for c in range(a+1,len(arr2)):
						# if arr1[b] >= arr2[c]:
							# continue
						# for d in range(b+1,len(arr1)):
							# if arr2[a] < arr1[b] and arr1[b] < arr2[c] and arr2[c] < arr1[d]:
								# remaining = len(arr1) - d
								# count+=remaining
								# break
			
	print(count)
	
main2()
