'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def main():
    N = int(input())
    inp = input().split(' ')
    arr = [0] * N

    for x in range(0,N):
        arr[x] = int(inp[x])
    
    arr.sort()
    relations = [0]*N
    
    
    RelationCount = 0
    TotalCount = 0
    samecount = 1
    for x in range(N-1,-1,-1):
        
        for y in range(x+1,N):
            if arr[y] - arr[x] == 1:
                if samecount > 0:
                    RelationCount = relations[y] + samecount
                    relations[x] = RelationCount

                    TotalCount += relations[x] + int(samecount*(samecount-1)/2)

                    samecount = 1
                else:
                    RelationCount = relations[y] + 1
                    relations[x] = RelationCount
                    TotalCount += relations[x]
                break
            if arr[y] - arr[x] == 0:
                if relations[y] > 0:
                    relations[x] = relations[y] + 1
                    TotalCount += relations[x]
                    samecount = 0
                if relations[y] == 0:
                    samecount+=1
                break
            if arr[y] - arr[x] > 1:
                samecount = 1
                break
            
    print(TotalCount)
        



main()
