'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def main():
    N = int(input())
    d = dict()
    for x in 'abcdefghijklmnopqrstuvwxyz':
        d[x] = 0

    for case in range(0,N):
        sdict = dict(d)
        tdict = dict(d)
        
        S = input()
        T= input()

        for x in S:
            sdict[x] += 1
        for x in T:
            tdict[x] +=1
        count = 0
        for x in 'abcdefghijklmnopqrstuvwxyz':
            if sdict[x] < tdict[x]:
                count+= tdict[x] - sdict[x]
            if sdict[x] > tdict[x]:
                count += sdict[x] - tdict[x]
        print(count)
main()
