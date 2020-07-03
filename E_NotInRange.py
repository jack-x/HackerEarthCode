'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def sumNatural(num):
    return int(num*(num+1)/2)

def main():
    x = 1000000
    sum = int(x*(x+1)/2)
    #print(sum)
    N = int(input())

    for case in range(0,N):
        i = input().split(' ')
        l = int(i[0])
        r = int(i[1])
        #print("L: {} and R: {}".format(l,r))
        addition = sumNatural(r) - sumNatural(l-1)
        #print("Sum of numbers from L to R: {}".format(addition))

        sum -= addition
        #print("Sum Remaining: {}".format(sum))

    print(sum)

def findPosition(arr,x):
    a = 0
    b = len(arr)
    while a!=b and (b-a) > 1:
        mid = int((a+b)/2)
        if arr[mid] == x:
            return mid
        else:
            if arr[mid] > x:
                b = mid
            elif arr[mid] < x:
                a = mid
    return a
        

def main2():
    x = 1000000
    sum = int(x*(x+1)/2)
    removekey = [0] * 1000001
    
    N = int(input())
    if N == 0:
        print(sum)
        return
    ranges = []
    
    #initializing case 1
    i = input().split(' ')
    l = int(i[0])
    r = int(i[1])

    LRarray = [[l,r]]
    Larray = [l]

    for case in range(1,N):
        i = input().split(' ')
        l = int(i[0])
        r = int(i[1])
        #find position
        index = findPosition(Larray,l) #binarySearch

        for x in range(index,index-1,-1): 
            LR = LRarray[x]
            #print(LRarray)
            #print(Larray)
            #print(x)
            if l <= LR[0] and r>= LR[1]:
                LRarray[x] = [l,r]
                Larray[x] = l
                break
            if ( l >=LR[0] and l<=LR[1] ) and r>= LR[1]:
                LRarray[x][1] = r
                break
            if l == LR[1] :
                LRarray[x][1] = r
                break
            if l>LR[1]:
                LRarray.insert(x+1,[l,r])
                Larray.insert(x+1,l)
                break
                
            

    for y in LRarray:

        for x in range(y[0],y[1]+1):
                removekey[x] = x
    removekey.pop(0)

    for x in removekey:
        sum -= x
        
    print(sum)


main2()
