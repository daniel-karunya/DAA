def knap(n,v,w,c):
    V = [[0 for i in range(c+1)]for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(c+1):
            if j < w[i-1]:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j], V[i-1][j-w[i-1]]+v[i-1])
    x = [0 for i in range(n)]
    j=c
    for i in range(n,0,-1):
        if V[i][j] == V[i-1][j]:
            x[i-1] = 0
        else:
             x[i-1] = 1
             j -= w[i-1]
    return V[n][c], x

n = int(input("Enter the number of items: "))
v = list(map(int,input("Enter the values: ").split()))
w = list(map(int,input("Enter the weights: ").split()))
c = int(input("Enter the capacity of the bag: "))
profit,x = knap(n,v,w,c)
print("Profit: ",profit)
print("x: ",x)