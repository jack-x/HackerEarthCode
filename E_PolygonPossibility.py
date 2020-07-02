'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main():
    T = int(input())

    for case in range(0,T):
        N = int(input())
        arr = [0] * N
        s = input().split(' ')
        sum=0
        for x in range(0,N):
            arr[x] = int(s[x])
            sum = sum+arr[x]

        polygonFlag = True
        for x in range(0,N):
            if arr[x] < (sum - arr[x]):
                continue
            else:
                polygonFlag = False
                break
        
        if polygonFlag == True:
            print('Yes')
        else:
            print('No')
        




main()
