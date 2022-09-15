MAX = 100001
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
x = input()
for t in range(T):
    n = int(input())
    makeSet()
    succ = 0
    unSucc = 0
    while True:
        l = input().split()
        if len(l) == 0:
            break
        x = (int)(l[1])
        y = (int)(l[2])
        if l[0] == 'c':
            unionSet(x, y)
        elif l[0] == 'q':
            if findSet(x) == findSet(y):
                succ += 1
            else:
                unSucc += 1

    print('{},{}'.format(succ, unSucc))
    if (t < T - 1):
        print()



