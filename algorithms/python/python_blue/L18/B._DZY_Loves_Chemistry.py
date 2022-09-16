MAX = 55
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

n, m = map(int, input().split())
makeSet()
for i in range(m):
    a, b = map(int, input().split())
    unionSet(a, b)

p = [0] * MAX
res = 1
for i in range(1, n + 1):
    print(findSet(i))
    if p[findSet(i)] != 0:
        res *= 2
    p[findSet(i)] += 1

print(res)
