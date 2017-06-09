
def main():
	s= int(input())
	string = input()
	vowels = ['a','e','i','o','u']
	for ch in string:
		if ch in vowels:
			vowels.pop(vowels.index(ch))
			if(len(vowels) == 0):
				print("YES")
				return
	
	print("NO")

if __name__ == "__main__": main()
