def main():
	mou = int(input())
	M = input().split(' ')
	
	# if Mm[-1] != ' ':
		# M =  Mm.split(' ')
	# else:
		# M = Mm[0:len(Mm)-1].split(' ')

	mouses = [0]*mou
	
	sumMice = 0
	sumKeyboards = 0
	
	
	for m in range(0,mou):
		mouses[m] = int(M[m])
		sumMice += mouses[m]
	mouses.sort()
	
	K = int(input())
	keyboard = input().split(' ')
	keyboards = [0] * K
	
	for k in range(0,K):
		keyboards[k] = int(keyboard[k])
		sumKeyboards += keyboards[k]
	keyboards.sort()
	
	price = int(input())
	if mou != K and sumMice + sumKeyboards <= price:
		if mou > K:
			print(K)
		else:
			print(mou)
		return
		
	count=0
	
	# print('We ARE HERE')
	
	while price >=0 and len(mouses)>0 and len(keyboards)>0:
		# print('Status: {} {} {}'.format(price,len(mouses),len(keyboards)))
		if price < mouses[0] + keyboards[0]:
			break
		m = mouses[0]
		k = keyboards[0]
		if m!=k:
			count+=1
			price -= (m+k)
			mouses.pop(0)
			keyboards.pop(0)
			# print('One Done')
			continue
		if m==k:
			# print('We are here')
			M=-1
			K=-1
			pointerM=-1
			pointerK=-1
			for x in range(1,len(mouses)):
				M = mouses[x]
				if M != k:
					pointerM = x
					break
			for x in range(1,len(keyboards)):
				K = keyboards[x]
				if K != m:
					pointerK = x
					break
			
			# print('We are here 2')
			
			if pointerM == -1 and pointerK == -1:
				break
			
			if pointerM == -1:
				price1 = price+1
			else:
				price1 = M + k
			if pointerK == -1:
				price2 = price+1
			else:
				price2 = m + K
			
			# price1 = M + k
			# price2 = m + K
			
			if price1<= price or price2<= price:
				if price1<price2:
					price -= price1
					mouses.pop(pointerM)
					keyboards.pop(0)
					# print('We are here 3')
					count+=1
				else:
					price -= price2
					mouses.pop(0)
					keyboards.pop(pointerK)
					# print('We are here 4')
					count+=1
			else:
				break
	
	# while price >=0:
		# if len(mouses)>0:
			# Mouse = mouses.pop(0)
		# else:
			# break
		# if len(keyboards) > 0:
			# Keyboard = keyboards.pop(0)
		# else:
			# break

		# similarCount=0
		# if Mouse == Keyboard:
			# if len(mouses) > len(keyboard):
				# lm = len(mouses)
				# for x in range(1,lm):
					# mouses.insert(x-1,Mouse)
					# Mouse = mouses.pop(x)
					# if Mouse!=Keyboard:
						# break
				
				# if Mouse == Keyboard:
					# lm = len(keyboards)
					# for x in range(1,lm):
						# keyboards.insert(x-1,Mouse)
						# Keyboard = keyboards.pop(x)
						# if Mouse!=Keyboard:
							# break
				# if Mouse==Keyboard:
					# break
			
			# else:
				# lm = len(keyboards)
				# for x in range(1,lm):
					# keyboards.insert(x-1,Mouse)
					# Keyboard = keyboards.pop(x)
					# if Mouse!=Keyboard:
						# break
				
				# if Mouse == Keyboard:
					# lm = len(mouses)
					# for x in range(1,lm):
						# mouses.insert(x-1,Mouse)
						# Mouse = mouses.pop(x)
						# if Mouse!=Keyboard:
							# break
				# if Mouse==Keyboard:
					# break
								
		# price = price - Mouse - Keyboard
		# if price >= 0:
			# count+=1
		# else:
			# break
	
	print(count)
	

main()
