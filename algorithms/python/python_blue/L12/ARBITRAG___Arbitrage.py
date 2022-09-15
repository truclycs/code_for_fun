def findCurrency(s):
    global c
    for i in range(n):
        if c[i] == s:
            return i;
    return -1;

def FloydWarshall():
    global dist
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] < dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]

Case = 1
while True:
    n = int(input())
    if n == 0:
        break
    dist = [[0.0 for i in range(n)] for j in range(n)]
    c = []

    for i in range(n):
        dist[i][i] = 1.0
        c.append(input())
    
    m = int(input())
    for i in range(m):
        u, w, v = input().split()
        dist[findCurrency(u)][findCurrency(v)] = float(w)

    FloydWarshall()
    flag = False
    for i in range(n):
        if dist[i][i] > 1.0:
            flag = True
            break

    if flag:
        print("Case {}: {}".format(Case, "Yes"))
    else:
         print("Case {}: {}".format(Case, "No"))
    Case += 1
    input()