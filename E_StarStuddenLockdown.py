'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def main():

    d = dict()
    dd= dict()
    for x in 'abcdefghijklmnopqrstuvwxyz':
        d[x] = -1
        dd[x] = 0
    
    T = int(input())

    for case in range(0,T):
  
        N = int(input())
        nd = dict(d)
        ddd = dict(dd)
        s = input().rstrip()
        for x in s:
            nd[x] += 1
            ddd[x] += nd[x]
        sum = 0
        for x in ddd.keys(): 
            if nd[x] != -1:
                sum+=ddd[x]

        print(sum)
        

main()
