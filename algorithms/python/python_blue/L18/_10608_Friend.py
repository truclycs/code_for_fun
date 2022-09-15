MAX = 30001
parent = []

def makeSet():
    global parent
    parent = [i for i in range(MAX + 1)]

def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    makeSet()
    
    for i in range(m):
        a, b = map(int, input().split())
        unionSet(a, b)

    res = 0
    p = [0] * MAX
    for i in range(1, n + 1):
        p[findSet(i)] += 1
    for i in range(1, n + 1):
        res = max(res, p[i])

    print(res)
    

    
