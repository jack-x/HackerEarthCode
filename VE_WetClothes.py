
def main():
    N = int(input())
    A = [0]*N
    i = input().split(' ')

    for x in range(0,N):
        A[x] = int(i[x])

    M = int(input())
    C =[0]*M
    i = input().split(' ')

    for x in range(0,M):
        C[x] = int(i[x])
    
    B = []

    for c in C:
        for a in A:
            for x in range(0,100):
                sum = x + a
                if (sum == c):
                    B.append(x)
                if sum > c:
                    break
    
    B = list(set(B))

    for a in A:
        for b in list(B):
            sum = a + b
            if sum in C:
                continue
            else:
                B.remove(b)

    print(*B)
    


if __name__ == '__main__':
    main()
