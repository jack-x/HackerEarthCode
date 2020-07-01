'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def main():
    i = input().split(' ')

    N = int(i[0])
    Q = int(i[1])

    queue = [0]*N
    societyIndex = dict()
    for x in range(1,1000000):
        societyIndex[x] = [0]

    i = input().split(' ')

    for x in range(0,N):
        societyIndex[int(i[x])].append(x+1)
    
    #special provisions because Hacker Earth Input is fucked
    D = int(i[-4])
    K = int(i[-3])
    L = int(i[-2])
    R = int(i[-1])

    if D not in societyIndex:
        print(-1)

    else:
        indexes = societyIndex[D]

        count = 0
        indexFound = 0
        for x in societyIndex[D]:
            if x>=L and x<=R:
                count+=1
            if count>=K:
                indexFound = x
                break
        if count == K:
            print(indexFound)
        else:
            print(-1)


    case = 1
    while case < Q:
        i = input().split(' ')
        D = int(i[0])
        K = int(i[1])
        L = int(i[2])
        R = int(i[3])

        if D not in societyIndex:
            print(-1)
            case+=1
            continue
        indexes = societyIndex[D]

        count = 0
        indexFound = 0
        for x in societyIndex[D]:
            if x>=L and x<=R:
                count+=1
            if count>=K:
                indexFound = x
                break
        if count == K:
            print(indexFound)
        else:
            print(-1)


        case += 1

main()
