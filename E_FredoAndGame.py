
def main():
	T=int(input())
	
	for case in range(0,T):
		inp = input().split(' ')
		Ammo = int(inp[0])
		N=int(inp[1])
		
		arr = input().split(' ')
		position=0
		for x in arr:
			if x == '0':
				Ammo-=1
			if x== '1':
				Ammo+=2
			
			if Ammo == 0 and position<(len(arr)-1):
				print("No {}".format(position+1))
				Ammo=-1
				break
			position+=1
		
		if Ammo>=0:
			print("Yes {}".format(Ammo))


if __name__ == '__main__': main()
