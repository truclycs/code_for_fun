MAX = 101
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

makeSet()
n, m = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())
    unionSet(a, b)

p = [0] * MAX

for i in range(1, n + 1):
    p[findSet(i)] += 1

isCthulhu = True
for i in range(1, n + 1):
    if p[findSet(i)] < n:
        isCthulhu = False

if n == m and  isCthulhu:
    print("FHTAGN!")
else:
    print("NO")
