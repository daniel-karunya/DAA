def dijk(n,v,m,s):
    dist = [float('inf')]*n
    path = [None]*n
    dist[v.index(s)] = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] != -1:
                if dist[j] > dist[i] + m[i][j]:
                    dist[j] = dist[i] + m[i][j]
                    path[j] = v[i]
    return dist,path

def printpath(d,path,n,v,s):
    for i in range(n):
        if d[i] == float('inf'):
            print(v[i], "inf")
            continue
        if v[i] == s:
            print(v[i], "0")
            continue
        print(v[i],":",d[i])
        pa = v[i] + " >- "
        j = i
        while path[j] != s:
            pa += path[j] + " >- "
            j = v.index(path[j])
        pa += s
        print("pathL ", pa[::-1])

n = int(input("Enter the number of vertices: "))
vertices = [chr(i) for i in range(65,n+65)]
mat = [list(map(int,input("Enter the edges for(-1 for no connection): "+vertices[i]+"\n").split())) for i in range(n)]
start = input("Enter the start vertex: ").upper()
d,p = dijk(n,vertices,mat,start)
print(p)
printpath(d,p,n,vertices,start)

    