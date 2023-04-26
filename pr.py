def prim(g):
    v = len(g)
    selected = [False for i in range(v)]
    no_edge = 0
    selected[0] = True
    while no_edge < v-1:
        min = float('inf')
        x = 0
        y = 0
        for i in range(v):
            if(selected[i]):
                for j in range(v):
                    if((not selected[j]) and g[i][j]):
                        if min > g[i][j]:
                            min = g[i][j]
                            x = i
                            y = j
        print(chr(x+65), "-", chr(y+65), ":", g[x][y])
        selected[y] = True
        no_edge += 1


G = [[0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]]
prim(G)