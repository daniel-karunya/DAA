def fraknap(n,p,w,c):
    x = [0 for i in range(n)]
    r = [(p[i]/w[i])for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(r[i]>r[j]):
                r[i], r[j] = r[j], r[i]
                p[i], p[j] = p[j], p[i]
                w[i], w[j] = w[j], w[i]
    profit = 0.0
    for i in range(n):
        if(c >= w[i]):
            c -= w[i]
            x[i] = 1
            profit += p[i]
        else:
            x[i] = c/w[i]
            profit += (p[i] * x[i])
            break
    return profit, x

n = int(input("Enter the number of objects: "))
p = list(map(int, input("Enter the profits: ").split()))
w = list(map(int, input("Enter the weights: ").split()))
c = int(input("Enter the capacity of the bag: "))
profit,x =fraknap(n,p,w,c)
print("Profit: ",profit)
print("Objects taken: ",x)