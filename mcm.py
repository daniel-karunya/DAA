import math


def mcm(n,d):
    m = [[0 for i in range(n+1)]for i in range(n+1)]
    r = [[0 for i in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1):
        m[i][i] = 0
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j]= math.inf
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + d[i-1]*d[j]*d[k]
                if q < m[i][j]:
                    m[i][j] = q
                    r[i][j] = k
    return m,r

def printb(r,start,end):
    if start == end:
        print("A[{}]".format(start), end="")
    else:
        k = r[start][end]
        print('(',end="")
        printb(r,start,k)
        printb(r,k+1,end)
        print(')',end="")

n = int(input("Enter the number of matrices: "))
d = list(map(int, input("Enter the dimensions: ").split()))
m,r = mcm(n,d)
printb(r,1,n)
print(m[1][n])