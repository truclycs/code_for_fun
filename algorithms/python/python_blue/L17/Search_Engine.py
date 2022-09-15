class Node:
    def __init__(self):
        self.child = dict()
        self.value = 0

def addWord(root, s, value):
    for c in s:
        if c not in root.child:
            root.child[c] = Node()
        root = root.child[c]
        root.value = max(root.value, value)

def get(root, s):
    for c in s:
        if c in root.child:
            root = root.child[c]
        else:
            return -1
    return root.value

n, m = map(int, input().strip().split())
root = Node()

for i in range(n):
    line = input().strip().split()
    addWord(root, line[0], int(line[1]))

for i in range(m):
    line = input().strip()
    print(get(root, line))