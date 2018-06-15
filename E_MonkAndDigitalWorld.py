def main():
	n=int(input())
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	d1= dict()
	d2=dict()
	for x in alpha:
		d1[x]=0
		d2[x]=0
	s=input()
	ss=input()
	for x in s:
		d1[x]+=1
	for x in ss:
		d2[x]+=1
		
	for x in alpha:
		if d1[x] !=d2[x]:
			print('NO')
			return
	
	print('YES')
	
	
main()
