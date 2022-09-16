class Node:
    def __init__(self):
        self.child = dict()
        self.value = 0

def addString(root, s):
    for c in list(s):
        if c in root.child:
            root = root.child[c]
        else:
            root.child[c] = Node()
            root = root.child[c]
        root.value += 1

def get(root, s):
    valueMax = 0
    len = 0
    for c in list(s):
        if c in root.child:
            root = root.child[c]
        len += 1
        valueMax = max(valueMax, root.value * len)
    return valueMax


T = int(input())
for t in range(T):

    n = int(input())
    a = []

    for i in range(n):
        a.append(input())
       
    root = Node()
    for i in range(n):
        addString(root, a[i])

    res = 0
    for i in range(n):
        res = max(res, get(root, a[i]))

    print("Case {}: {}".format(t + 1, res))