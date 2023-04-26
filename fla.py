def floyd(d):
    p = [[j+1 for j in range(len(d))]for i in range(len(d))]
    n = len(d)
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = k+1
    return d,p

def pathprint(s,de):
    if de == p[s-1][de-1] and d[s-1][de-1] != INF:
        print(p[s-1][de-1])
        return
    elif d[s-1][de-1] == INF:
        print("no path")
        return
    else:
        pathprint(s,p[s-1][de-1])
        print(p[s-1][de-1], end="")
        pathprint(p[s-1][de-1],de)

INF = float('inf')

d = [[0,INF,INF,3,INF],
     [3,0,INF,INF,INF],
     [INF,INF,0,2,INF],
     [INF,1,1,0,INF],
     [INF,INF,INF,2,0]]

d,p = floyd(d)
src = int(input("Enter the source: "))
dest = int(input("Enter the dest: "))
pathprint(src,dest)
