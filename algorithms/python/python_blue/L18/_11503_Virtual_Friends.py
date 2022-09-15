MAX = 100001
parent = []

import sys
import threading
class Scanner:
    def __generator__():
        while True:
            for x in input().strip().split():
                yield x
    sc = __generator__()
    def next():
        return Scanner.sc.__next__()
Sc = Scanner

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

T = int(Sc.next())
name = dict()
for _ in range(T):
    n = int(Sc.next())
    makeSet()
    p = [1] * MAX
    name.clear()
    m = 0
    for i in range(n):
        a, b = Sc.next(), Sc.next()
        if not a in name:
            m += 1
            name[a] = m
        if not b in name:
            m += 1
            name[b] = m
        if findSet(name[a]) == findSet(name[b]):
            tmp = p[findSet(name[a])]
        else:
            tmp =  p[findSet(name[a])] + p[findSet(name[b])]

        print(tmp)
        unionSet(name[a], name[b])
        p[findSet(name[a])] = tmp
