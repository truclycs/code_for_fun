def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

Case = 0
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    parent = [i for i in range(n + 1)]

    res = 0
    for i in range(m):
        x, y = map(int, input().split())
        unionSet(x, y)

    p = [False for i in range(50001)]
    for i in range(1, n + 1):
        x = findSet(i)
        if not p[x]:
            res += 1
            p[x] = True

    Case += 1
    print("Case " + str(Case) + ": " + str(res))