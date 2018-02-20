
def main(): T=int(input()) for case in range(0,T):  n = int(input())    middle= (n-1)/2  matrix = []  row = -1  for x in range(0,n):   row+=1   s=input()   matrix.append(s)   column=-1   starFoundFlag = False   for y in s:    column+=1    if y=='*':     starFoundFlag = True     break   if starFoundFlag is True:    swaps = abs(row - middle) + abs ( column - middle)    print(int(swaps))         
main()
