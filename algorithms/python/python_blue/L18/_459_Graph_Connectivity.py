MAX = 1001
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
t = input()
while T:
    T -= 1
    x = input()
    n = ord(x) - ord('A') + 1
    makeSet()
    while True:
        line = input()
        if line == "":
            break
        x = line[0]
        y = line[1]
        unionSet(ord(x) - ord('A') + 1, ord(y) - ord('A') + 1)

    res = 0
    for i in range(1, n + 1):
        if parent[i] == i:
            res += 1

    print(res)
    if T > 0:
        print()