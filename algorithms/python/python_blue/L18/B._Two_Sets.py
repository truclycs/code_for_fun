MAX = 100001
parent = []

def makeSet():
    global parent
    parent = [i for i in range(MAX + 1)]

def findSet(u):
    global parent
    if u != parent[u]:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

makeSet()
n, a, b = map(int, input().split())
p = list(map(int, input().split()))
pos = dict()
for i in range(n):
    pos[p[i]] = i + 1

for i in range(n):
    unionSet(i + 1, pos.get(a - p[i], n + 1))
    unionSet(i + 1, pos.get(b - p[i], 0))

A = findSet(0)
B = findSet(n + 1)

if A != B:
    print('YES')
    for i in range(1, n + 1):
        if findSet(i) == B:
            print('1', end = " ")
        else:
            print('0', end = " ")
else:
    print('NO')
